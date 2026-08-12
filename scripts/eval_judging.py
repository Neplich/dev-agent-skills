"""Independent judge protocol and schema handling for paired skill evals."""

from __future__ import annotations

import json
import shutil
from pathlib import Path
from typing import Any

JUDGE_SCHEMA = Path(__file__).with_name("eval_judge_result.schema.json")
MODEL = "gpt-5.6-luna"
REASONING_EFFORT = "medium"


def _judge_codex_command(workspace: Path, output_path: Path, schema: Path) -> list[str]:
    return [
        "codex", "--ask-for-approval", "never", "--strict-config", "exec", "-C", str(workspace),
        "--ephemeral", "--ignore-rules", "--model", MODEL,
        "-c", f'model_reasoning_effort="{REASONING_EFFORT}"',
        "--output-schema", str(schema), "--output-last-message", str(output_path), "-",
    ]


def build_judge_schema_bytes(
    assertions: list[dict[str, Any]], *, schema_path: Path | None = None,
) -> bytes:
    schema = json.loads((schema_path or JUDGE_SCHEMA).read_text(encoding="utf-8"))
    assertion_ids = [assertion["id"] for assertion in assertions]
    results = schema["properties"]["assertion_results"]
    results["minItems"] = len(assertion_ids)
    results["maxItems"] = len(assertion_ids)
    results["items"]["properties"]["id"] = {"enum": assertion_ids}
    return json.dumps(
        schema, ensure_ascii=False, sort_keys=True, separators=(",", ":"),
    ).encode()


def judge_command(
    workspace: Path, output_path: Path, *, schema: Path | None = None,
) -> list[str]:
    return _judge_codex_command(workspace, output_path, schema or JUDGE_SCHEMA)


def recompute_overall(behavior_result: str, coverage_result: str) -> str:
    if behavior_result == "FAIL":
        return "FAIL"
    if behavior_result == "PASS" and coverage_result in {"FULL", "PARTIAL"}:
        return "PASS" if coverage_result == "FULL" else "PASS (partial coverage)"
    raise ValueError(f"invalid judge result pair: {behavior_result}/{coverage_result}")


def validate_judge_result(payload: dict[str, Any], assertion_ids: set[str]) -> dict[str, Any]:
    required = {
        "assertion_results", "lane_summaries", "behavior_result", "coverage_result",
        "overall_result", "uncovered_reasons", "blockers", "failures", "next_steps",
    }
    if set(payload) != required:
        raise ValueError("judge result fields do not match the required schema")
    results = payload.get("assertion_results")
    if not isinstance(results, list) or not results:
        raise ValueError("judge result assertion_results must be non-empty")
    seen: set[str] = set()
    statuses: list[str] = []
    for result in results:
        if not isinstance(result, dict) or set(result) != {"id", "status", "evidence"}:
            raise ValueError("judge assertion result fields are invalid")
        assertion_id, status, evidence = result.get("id"), result.get("status"), result.get("evidence")
        if assertion_id not in assertion_ids or assertion_id in seen:
            raise ValueError(f"judge assertion id is missing, unknown, or duplicate: {assertion_id}")
        if status not in {"PASS", "FAIL", "NOT_EXERCISED"}:
            raise ValueError(f"judge assertion status is invalid: {status}")
        if not isinstance(evidence, str) or not evidence.strip():
            raise ValueError("judge assertion evidence must be non-empty")
        seen.add(assertion_id)
        statuses.append(status)
    if seen != assertion_ids:
        raise ValueError("judge result does not cover every assertion")
    summaries = payload.get("lane_summaries")
    if not isinstance(summaries, dict) or set(summaries) != {"without_skill", "with_skill"}:
        raise ValueError("judge lane_summaries must cover both lanes")
    for summary in summaries.values():
        if not isinstance(summary, dict) or set(summary) != {"run_source", "behavior_summary"}:
            raise ValueError("judge lane summary fields are invalid")
        if not all(isinstance(value, str) and value.strip() for value in summary.values()):
            raise ValueError("judge lane summary values must be non-empty strings")
    expected_behavior = "FAIL" if "FAIL" in statuses else "PASS"
    expected_coverage = "PARTIAL" if "NOT_EXERCISED" in statuses else "FULL"
    for field in ("uncovered_reasons", "blockers", "failures", "next_steps"):
        value = payload.get(field)
        if not isinstance(value, list) or not all(isinstance(item, str) and item.strip() for item in value):
            raise ValueError(f"judge result {field} must be an array of non-empty strings")
    if expected_coverage == "PARTIAL" and not payload["uncovered_reasons"]:
        raise ValueError("partial coverage requires uncovered_reasons")
    normalized = dict(payload)
    normalized["behavior_result"] = expected_behavior
    normalized["coverage_result"] = expected_coverage
    normalized["overall_result"] = recompute_overall(expected_behavior, expected_coverage)
    return normalized


def prepare_judge_package(definition: Any, materialized: Any, judge: Any,
                          candidate_runs: list[dict[str, Any]]) -> None:
    fixture_destination = judge.workspace_root / "fixture"
    shutil.copytree(materialized.canonical_root, fixture_destination)
    package = {
        "prompt": materialized.prompt,
        "assertions": definition.item["assertions"],
        "candidate_outputs": [{
            "mode": run["mode"], "output": run["output"], "git_status": run["git_status"],
            "git_diff": run["git_diff"], "workspace_manifest": run["workspace_manifest"],
            "delivery_snapshot": run["delivery_snapshot"], "git_evidence": run["git_evidence"],
            "dependency_evidence": run["dependency_evidence"],
            "declared_outputs": run["declared_outputs"],
            "runner_captured_trace": {
                "stdout_jsonl_tail": run["status"].get("stdout_tail", ""),
                "stderr_tail": run["status"].get("stderr_tail", ""),
            },
        } for run in candidate_runs],
        "preflight": materialized.preflight.as_dict(),
    }
    (judge.workspace_root / "judge-package.json").write_text(
        json.dumps(package, ensure_ascii=False, indent=2) + "\n", encoding="utf-8",
    )


def judge_prompt() -> str:
    return (
        "Read judge-package.json and the read-only fixture directory. Independently judge "
        "each assertion from the two locked candidate outputs and raw evidence. Assertion "
        "verdicts evaluate only the with_skill lane. The without_skill is comparison context: "
        "its failure to satisfy an assertion must not make an assertion FAIL when with_skill "
        "satisfies it. Use without_skill only to describe the fresh baseline and contrast the "
        "two behaviors. Copy each assertion id exactly from judge-package.json; never invent "
        "positional ids such as assertion_1. Return only the JSON object required by the supplied "
        "output schema. Treat each delivery_snapshot file or git_blob content as locked primary "
        "evidence: inspect that content directly, and do not fail a file-backed requirement merely "
        "because the candidate's final prose does not restate the delivered file. Judge user-visible "
        "behavior semantically: accept semantic equivalents and do not require an exact internal "
        "label, skill path, or wording unless the assertion makes that literal form part of the "
        "user's observable result. For an interactive workflow, when the candidate correctly performs "
        "the next required step but a later step cannot yet occur without user confirmation or missing "
        "runtime evidence, mark that later assertion NOT_EXERCISED and coverage PARTIAL rather than FAIL. "
        "Likewise, a hidden process or read-order assertion is NOT_EXERCISED when the locked raw evidence "
        "cannot prove it; do not infer failure merely because the final prose omits process narration. "
        "Treat runner_captured_trace JSONL command and tool events as locked raw evidence, but do not "
        "treat agent-message claims inside that trace as independent proof. Use FAIL only when the "
        "with_skill lane contradicts an exercised requirement, omits an exercised user-visible result, "
        "makes an unsupported claim, or performs a forbidden mutation. Return only the JSON object "
        "required by the supplied output schema. Do not use lane self-ratings or any historical comparison."
    )
