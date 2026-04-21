#!/usr/bin/env python3

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path


DEFAULT_TIMEOUT_SECONDS = 180
DEFAULT_MODEL = "gpt-5.4-mini"

SKILL_PATHS = {
    "qa-agent": "agents/qa/skills/qa-agent/SKILL.md",
    "spec-based-tester": "agents/qa/skills/spec-based-tester/SKILL.md",
    "exploratory-tester": "agents/qa/skills/exploratory-tester/SKILL.md",
    "bug-analyzer": "agents/qa/skills/bug-analyzer/SKILL.md",
    "regression-suite": "agents/qa/skills/regression-suite/SKILL.md",
}


@dataclass
class EvalDefinition:
    metadata_path: Path
    eval_root: Path
    evals_path: Path
    skill_name: str
    eval_item: dict
    metadata: dict


def repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def remove_path(path: Path) -> None:
    if path.is_dir():
        shutil.rmtree(path)
    elif path.exists():
        path.unlink()


def load_eval_definition(metadata_path: Path | str) -> EvalDefinition:
    metadata_path = Path(metadata_path)
    if not metadata_path.is_absolute():
        metadata_path = repo_root() / metadata_path
    metadata_path = metadata_path.resolve()
    eval_root = metadata_path.parent
    skill_dir = metadata_path.parents[3]
    evals_path = skill_dir / "evals/evals.json"
    evals = load_json(evals_path)
    metadata = load_json(metadata_path)

    for item in evals["evals"]:
        if item["id"] == metadata["eval_id"]:
            return EvalDefinition(
                metadata_path=metadata_path,
                eval_root=eval_root,
                evals_path=evals_path,
                skill_name=evals["skill_name"],
                eval_item=item,
                metadata=metadata,
            )

    raise ValueError(f"Eval id {metadata['eval_id']} not found in {evals_path}")


def rel(path: Path) -> str:
    return path.resolve().relative_to(repo_root()).as_posix()


def fixture_list(defn: EvalDefinition) -> str:
    items = defn.metadata.get("fixture_context", [])
    if not items:
        return "- None"
    return "\n".join(f"- {item}" for item in items)


def assertion_list(defn: EvalDefinition) -> str:
    assertions = defn.eval_item.get("assertions", [])
    if not assertions:
        return "- None"
    return "\n".join(f"- {item['name']}: {item['text']}" for item in assertions)


def build_candidate_prompt(defn: EvalDefinition, label: str) -> str:
    if label not in {"with_skill", "without_skill"}:
        raise ValueError(f"Unsupported label: {label}")

    skill_path = SKILL_PATHS[defn.skill_name]
    if label == "with_skill":
        skill_instruction = (
            f"Read and apply `{skill_path}` and `agents/qa/README.md` before "
            "answering."
        )
    else:
        skill_instruction = (
            f"Do not read or apply `{skill_path}` or `agents/qa/README.md`. "
            "Answer from the prompt, fixture context, and general QA knowledge only."
        )

    return f"""You are generating a candidate QA output for an availability eval.
Do not edit files and do not run product tests. If the QA skill would create
files, include the intended paths and concise content outline in the response.

Mode: {label}
Skill under eval: {defn.skill_name}
{skill_instruction}

Read:
- `{rel(defn.evals_path)}`
- `{rel(defn.metadata_path)}`
- Fixture files listed in the metadata, relative to
  `{defn.metadata['workspace_root']}`:
{fixture_list(defn)}

User prompt:
{defn.metadata['prompt']}

Expected output:
{defn.eval_item.get('expected_output', '')}

Produce the candidate QA output that would be returned to the user.
"""


def build_judge_prompt(
    defn: EvalDefinition,
    label: str,
    candidate_path: str,
) -> str:
    skill_path = SKILL_PATHS[defn.skill_name]
    return f"""You are a fresh Codex eval judge. Do not edit files and do not run product tests.

Read:
- `{skill_path}`
- `agents/qa/README.md`
- `{rel(defn.evals_path)}`
- `{rel(defn.metadata_path)}`
- `{candidate_path}`
- Fixture files listed in the metadata, relative to
  `{defn.metadata['workspace_root']}`:
{fixture_list(defn)}

Evaluate whether the {label} candidate output satisfies the eval assertions.
For `without_skill`, judge the candidate on the same assertions; it is allowed
to fail if it lacks the skill behavior.

Eval prompt:
{defn.metadata['prompt']}

Assertions:
{assertion_list(defn)}

Return Markdown exactly with these sections:
# Verdict
- Overall: PASS or FAIL
# Assertion Results
- [PASS/FAIL] <assertion name>: <short reason>
# Notes
- Mention any blocker or ambiguity. If none, say None.
"""


def codex_command(output_path: Path) -> list[str]:
    return [
        "codex",
        "exec",
        "-C",
        str(repo_root()),
        "-s",
        "read-only",
        "--ephemeral",
        "--ignore-user-config",
        "--ignore-rules",
        "-m",
        DEFAULT_MODEL,
        "-c",
        'model_reasoning_effort="low"',
        "-o",
        str(output_path),
        "-",
    ]


def run_codex(prompt: str, output_path: Path, timeout_seconds: int) -> dict:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    started = time.time()
    try:
        completed = subprocess.run(
            codex_command(output_path),
            input=prompt,
            text=True,
            capture_output=True,
            timeout=timeout_seconds,
        )
        returncode = completed.returncode
        stdout = completed.stdout
        stderr = completed.stderr
        timed_out = False
    except subprocess.TimeoutExpired as exc:
        returncode = 124
        stdout = exc.stdout or ""
        stderr = exc.stderr or ""
        timed_out = True

    return {
        "command": codex_command(output_path),
        "returncode": returncode,
        "timeout": timed_out,
        "duration_ms": int((time.time() - started) * 1000),
        "stdout_length": len(stdout),
        "stderr_tail": stderr[-2000:],
        "output_path": rel(output_path),
        "output_exists": output_path.exists() and output_path.stat().st_size > 0,
    }


def candidate_path(defn: EvalDefinition, label: str) -> Path:
    return defn.eval_root / label / "outputs/candidate-output.md"


def verdict_path(defn: EvalDefinition, label: str) -> Path:
    outputs = defn.metadata.get(f"{label}_outputs", [])
    if outputs and isinstance(outputs[0], str):
        return defn.eval_root / outputs[0]
    return defn.eval_root / label / "outputs/subagent-verdict.md"


def parse_overall(text: str) -> str:
    match = re.search(r"Overall:\s*(PASS|FAIL)", text)
    if match:
        return match.group(1)
    return "MISSING"


def run_label(defn: EvalDefinition, label: str, timeout_seconds: int) -> dict:
    cand_path = candidate_path(defn, label)
    verd_path = verdict_path(defn, label)

    candidate_status = run_codex(
        build_candidate_prompt(defn, label),
        cand_path,
        timeout_seconds,
    )
    verdict_status = run_codex(
        build_judge_prompt(defn, label, rel(cand_path)),
        verd_path,
        timeout_seconds,
    )

    verdict_text = verd_path.read_text() if verd_path.exists() else ""
    return {
        "label": label,
        "candidate_path": rel(cand_path),
        "verdict_path": rel(verd_path),
        "candidate_ok": candidate_status["returncode"] == 0
        and candidate_status["output_exists"],
        "verdict_ok": verdict_status["returncode"] == 0
        and verdict_status["output_exists"],
        "overall": parse_overall(verdict_text),
        "candidate_status": candidate_status,
        "verdict_status": verdict_status,
    }


def write_run_diagnostics(defn: EvalDefinition, results: list[dict]) -> None:
    diagnostics_paths = defn.metadata.get("run_diagnostics", ["diagnostics/run.json"])
    path = defn.eval_root / diagnostics_paths[0]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n")


def clean_outputs(defn: EvalDefinition) -> None:
    for item in defn.metadata.get("execution_cleanup", []):
        remove_path(defn.eval_root / item)
    remove_path(defn.eval_root / "comparison.auto.md")


def render_report(defn: EvalDefinition, results: list[dict]) -> str:
    lines = [
        f"# Eval {defn.metadata['eval_id']}: {defn.metadata['eval_name']}",
        "",
        "## Prompt",
        "",
        defn.metadata["prompt"],
        "",
        "## Candidate And Verdict Outputs",
        "",
    ]

    for result in results:
        label = result["label"]
        lines.append(f"### {label}")
        lines.append("")
        lines.append(
            f"- [{'PASS' if result['candidate_ok'] else 'FAIL'}] "
            f"`{label}` candidate output: `{result['candidate_path']}`"
        )
        lines.append(
            f"- [{'PASS' if result['verdict_ok'] else 'FAIL'}] "
            f"`{label}` fresh judge verdict: `{result['verdict_path']}`"
        )
        semantic_ok = result["overall"] == "PASS"
        lines.append(
            f"- [{'PASS' if semantic_ok else 'FAIL'}] "
            f"`{label}` semantic verdict: {result['overall']}"
        )
        lines.append("")

    lines.extend(["## Expected Assertions", ""])
    for item in defn.eval_item.get("assertions", []):
        lines.append(f"- `{item['name']}`: {item['text']}")

    lines.extend(
        [
            "",
            "## Runner Policy",
            "",
            "- `with_skill` must produce candidate output and receive a PASS verdict.",
            "- `without_skill` is generated for comparison; a FAIL verdict is diagnostic, not a runner failure.",
        ]
    )
    return "\n".join(lines) + "\n"


def run_eval(
    metadata_path: Path | str,
    *,
    skip_generate: bool = False,
    timeout_seconds: int = DEFAULT_TIMEOUT_SECONDS,
) -> tuple[EvalDefinition, list[dict]]:
    defn = load_eval_definition(metadata_path)

    if not skip_generate:
        clean_outputs(defn)
        results = [
            run_label(defn, "with_skill", timeout_seconds),
            run_label(defn, "without_skill", timeout_seconds),
        ]
        write_run_diagnostics(defn, results)
    else:
        results = []
        for label in ("with_skill", "without_skill"):
            cand = candidate_path(defn, label)
            verd = verdict_path(defn, label)
            verdict_text = verd.read_text() if verd.exists() else ""
            results.append(
                {
                    "label": label,
                    "candidate_path": rel(cand),
                    "verdict_path": rel(verd),
                    "candidate_ok": cand.exists() and cand.stat().st_size > 0,
                    "verdict_ok": verd.exists() and verd.stat().st_size > 0,
                    "overall": parse_overall(verdict_text),
                }
            )

    report = render_report(defn, results)
    (defn.eval_root / "comparison.auto.md").write_text(report)
    return defn, results


def main() -> int:
    if len(sys.argv) not in (2, 3):
        print("Usage: run_eval.py <path-to-eval_metadata.json> [--skip-generate]")
        return 2

    skip_generate = "--skip-generate" in sys.argv[2:]
    defn, results = run_eval(sys.argv[1], skip_generate=skip_generate)
    report_path = defn.eval_root / "comparison.auto.md"
    print(report_path)

    by_label = {result["label"]: result for result in results}
    with_result = by_label["with_skill"]
    failed = (
        not with_result["candidate_ok"]
        or not with_result["verdict_ok"]
        or with_result["overall"] != "PASS"
    )
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
