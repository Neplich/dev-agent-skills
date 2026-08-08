#!/usr/bin/env python3
"""Run paired skill evals with one shared isolation and judging boundary."""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.eval_runtime import (  # noqa: E402
    IsolatedContext,
    MaterializedEvalRun,
    PermissionProbe,
    close_context,
    content_tree_hash,
    copy_canonical_fixture,
    evaluate_context_preflight,
    fixture_manifest,
    manifest_hash,
    materialize_eval_run,
    open_context,
    record_preflight,
    run_permission_probe,
    skill_overlay_hash,
    verify_context_dependencies,
)


MODEL = "gpt-5.6-luna"
REASONING_EFFORT = "medium"
DEFAULT_TIMEOUT_SECONDS = 300
JUDGE_SCHEMA = Path(__file__).with_name("eval_judge_result.schema.json")


@dataclass(frozen=True)
class EvalDefinition:
    repository_root: Path
    agent: str
    skill: str
    eval_id: str
    workspace_root: Path
    item: dict[str, Any]
    metadata: dict[str, Any]
    evals_bytes: bytes
    metadata_bytes: bytes


CommandRunner = Callable[..., dict[str, Any]]


def _load_json(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"JSON root must be an object: {path}")
    return payload


def source_identity(
    definition: EvalDefinition, *, judge_schema_bytes: bytes | None = None,
) -> dict[str, Any]:
    head = subprocess.run(
        ["git", "rev-parse", "--verify", "HEAD"], cwd=definition.repository_root,
        capture_output=True, text=True,
    )
    status = subprocess.run(
        ["git", "status", "--porcelain", "--untracked-files=all"],
        cwd=definition.repository_root, capture_output=True, text=True,
    )
    executor = Path(__file__).resolve()
    runtime = executor.with_name("eval_runtime.py")
    target = definition.repository_root / f"agents/{definition.agent}/skills/{definition.skill}"
    overlay_paths = [target, *(
        definition.repository_root / value
        for value in definition.metadata.get("skill_dependencies", [])
    )]
    overlay_hash = skill_overlay_hash(overlay_paths, definition.repository_root)
    schema_bytes = JUDGE_SCHEMA.read_bytes() if judge_schema_bytes is None else judge_schema_bytes
    with tempfile.TemporaryDirectory() as temporary:
        canonical = Path(temporary) / "canonical"
        copy_canonical_fixture(
            definition.workspace_root, canonical,
            cleanup_paths=definition.metadata.get("execution_cleanup", []),
        )
        fixture_hash = manifest_hash(fixture_manifest(canonical))
    return {
        "repository_head": head.stdout.strip() if head.returncode == 0 else "unavailable",
        "repository_dirty": status.returncode != 0 or bool(status.stdout),
        "target_skill_sha256": content_tree_hash(target),
        "skill_overlay_sha256": overlay_hash,
        "judge_schema_sha256": hashlib.sha256(schema_bytes).hexdigest(),
        "eval_definition_sha256": hashlib.sha256(json.dumps(
            definition.item, ensure_ascii=False, sort_keys=True, separators=(",", ":"),
        ).encode()).hexdigest(),
        "metadata_sha256": hashlib.sha256(definition.metadata_bytes).hexdigest(),
        "executor_sha256": hashlib.sha256(executor.read_bytes()).hexdigest(),
        "runtime_sha256": hashlib.sha256(runtime.read_bytes()).hexdigest(),
        "fixture_sha256": fixture_hash,
    }


def _resolve_workspace(evals_path: Path, workspace: str) -> Path:
    for candidate in (evals_path.parents[1] / workspace, evals_path.parent / workspace):
        if candidate.exists():
            return candidate.resolve()
    raise ValueError(f"eval workspace does not exist: {workspace}")


def load_eval_definition(
    repository_root: Path,
    agent: str,
    skill: str,
    eval_id: str,
    *,
    metadata_snapshot: tuple[dict[str, Any], bytes] | None = None,
) -> EvalDefinition:
    repository_root = repository_root.resolve()
    evals_path = repository_root / f"agents/{agent}/test/{skill}/evals/evals.json"
    evals_bytes = evals_path.read_bytes()
    payload = json.loads(evals_bytes)
    if not isinstance(payload, dict):
        raise ValueError(f"JSON root must be an object: {evals_path}")
    if payload.get("agent") != agent or payload.get("skill_name") != skill:
        raise ValueError(f"eval suite identity does not match {agent}/{skill}")
    item = next(
        (candidate for candidate in payload.get("evals", []) if candidate.get("id") == eval_id),
        None,
    )
    if item is None:
        raise ValueError(f"eval {eval_id!r} not found in {evals_path}")
    workspace = item.get("workspace")
    if not isinstance(workspace, str):
        raise ValueError(f"eval {eval_id!r} has no workspace")
    workspace_root = _resolve_workspace(evals_path, workspace)
    metadata_path = workspace_root / "eval_metadata.json"
    if metadata_snapshot is None:
        metadata_bytes = metadata_path.read_bytes()
        metadata = json.loads(metadata_bytes)
    else:
        metadata, metadata_bytes = metadata_snapshot
    if not isinstance(metadata, dict):
        raise ValueError(f"JSON root must be an object: {metadata_path}")
    if metadata.get("eval_id") != eval_id:
        raise ValueError(f"metadata eval_id does not match {eval_id!r}")
    return EvalDefinition(
        repository_root, agent, skill, eval_id, workspace_root, item, metadata,
        evals_bytes, metadata_bytes,
    )


def definition_from_metadata(
    metadata_path: Path,
    *,
    repository_root: Path | None = None,
) -> EvalDefinition:
    metadata_path = metadata_path.resolve()
    repository_root = (repository_root or Path(__file__).resolve().parents[1]).resolve()
    relative = metadata_path.relative_to(repository_root)
    parts = relative.parts
    if len(parts) < 7 or parts[0] != "agents" or parts[2] != "test":
        raise ValueError(f"metadata path is not in an agent eval workspace: {metadata_path}")
    agent = parts[1]
    skill = parts[3]
    metadata_bytes = metadata_path.read_bytes()
    metadata = json.loads(metadata_bytes)
    if not isinstance(metadata, dict):
        raise ValueError(f"JSON root must be an object: {metadata_path}")
    eval_id = metadata.get("eval_id")
    if not isinstance(eval_id, str):
        raise ValueError(f"metadata is missing eval_id: {metadata_path}")
    definition = load_eval_definition(
        repository_root, agent, skill, eval_id,
        metadata_snapshot=(metadata, metadata_bytes),
    )
    if definition.workspace_root / "eval_metadata.json" != metadata_path:
        raise ValueError("metadata path does not match the eval definition workspace")
    return definition


def _codex_command(
    workspace: Path,
    output_path: Path,
    *,
    schema: Path | None = None,
) -> list[str]:
    command = [
        "codex", "--ask-for-approval", "never", "--strict-config", "exec", "-C", str(workspace),
        "--ephemeral", "--ignore-rules",
        "--model", MODEL, "-c", f'model_reasoning_effort="{REASONING_EFFORT}"',
    ]
    if schema is not None:
        command.extend(["--output-schema", str(schema)])
    return [*command, "--output-last-message", str(output_path), "-"]


def candidate_command(workspace: Path, output_path: Path) -> list[str]:
    return _codex_command(workspace, output_path)


def judge_command(
    workspace: Path, output_path: Path, *, schema: Path | None = None,
) -> list[str]:
    return _codex_command(workspace, output_path, schema=schema or JUDGE_SCHEMA)


def run_command(
    command: list[str],
    *,
    prompt: str,
    env: dict[str, str],
    timeout_seconds: int,
) -> dict[str, Any]:
    try:
        completed = subprocess.run(command, input=prompt, text=True, capture_output=True,
                                   env=env, timeout=timeout_seconds)
        return {"returncode": completed.returncode, "timed_out": False}
    except subprocess.TimeoutExpired:
        return {"returncode": 124, "timed_out": True}


def check_model_available(repository_root: Path) -> bool:
    if shutil.which("codex") is None:
        return False
    try:
        completed = subprocess.run(["codex", "debug", "models"], cwd=repository_root,
                                   capture_output=True, text=True, timeout=30)
    except (OSError, subprocess.TimeoutExpired):
        return False
    return completed.returncode == 0 and MODEL in completed.stdout


def recompute_overall(behavior_result: str, coverage_result: str) -> str:
    if behavior_result == "FAIL":
        return "FAIL"
    if behavior_result == "PASS" and coverage_result in {"FULL", "PARTIAL"}:
        return "PASS" if coverage_result == "FULL" else "PASS (partial coverage)"
    raise ValueError(f"invalid judge result pair: {behavior_result}/{coverage_result}")


def validate_judge_result(
    payload: dict[str, Any],
    assertion_ids: set[str],
) -> dict[str, Any]:
    required = {"assertion_results", "lane_summaries", "behavior_result", "coverage_result", "overall_result",
                "uncovered_reasons", "blockers", "failures", "next_steps"}
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

    behavior, coverage = payload.get("behavior_result"), payload.get("coverage_result")
    expected_behavior = "FAIL" if "FAIL" in statuses else "PASS"
    expected_coverage = "PARTIAL" if "NOT_EXERCISED" in statuses else "FULL"
    if behavior != expected_behavior:
        raise ValueError("judge behavior_result contradicts assertion verdicts")
    if coverage != expected_coverage:
        raise ValueError("judge coverage_result contradicts assertion verdicts")
    for field in ("uncovered_reasons", "blockers", "failures", "next_steps"):
        value = payload.get(field)
        if not isinstance(value, list) or not all(isinstance(item, str) and item.strip() for item in value):
            raise ValueError(f"judge result {field} must be an array of non-empty strings")
    if coverage == "PARTIAL" and not payload["uncovered_reasons"]:
        raise ValueError("partial coverage requires uncovered_reasons")

    normalized = dict(payload)
    normalized["overall_result"] = recompute_overall(behavior, coverage)
    return normalized


def _git(context: IsolatedContext, *args: str, check: bool = True) -> str:
    result = subprocess.run(
        ["git", *args], cwd=context.git_root, capture_output=True, text=True,
    )
    if check and result.returncode:
        raise ValueError(f"git evidence command failed: git {' '.join(args)}")
    return result.stdout


def _git_ref_state(context: IsolatedContext) -> dict[str, dict[str, str | None]]:
    refs: dict[str, dict[str, str | None]] = {}
    for name in filter(None, _git(context, "for-each-ref", "--format=%(refname)").splitlines()):
        commit = _git(context, "rev-parse", "--verify", f"{name}^{{commit}}", check=False).strip()
        tree = _git(context, "rev-parse", "--verify", f"{name}^{{tree}}", check=False).strip()
        refs[name] = {
            "object": _git(context, "rev-parse", "--verify", name).strip(),
            "commit": commit or None,
            "tree": tree or None,
        }
    return refs


def _git_reflog(context: IsolatedContext) -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []
    output = _git(context, "reflog", "--all", "--format=%H%x00%gs", check=False)
    for line in output.splitlines():
        oid, separator, subject = line.partition("\0")
        if separator and oid:
            entries.append({"oid": oid, "subject": subject})
    return entries


def _capture_git_baseline(context: IsolatedContext) -> dict[str, Any]:
    head = _git(context, "rev-parse", "--verify", "HEAD").strip()
    untracked: list[dict[str, Any]] = []
    for relative in filter(None, _git(
        context, "ls-files", "--others", "--exclude-standard", "-z",
    ).split("\0")):
        path = context.workspace_root / relative
        if path.is_file() and not path.is_symlink():
            untracked.append(_render_snapshot(relative, "untracked", path.read_bytes()))
    return {
        "head": head,
        "branch": _git(context, "symbolic-ref", "-q", "--short", "HEAD", check=False).strip() or None,
        "refs": _git_ref_state(context),
        "commits": sorted(filter(None, _git(
            context, "rev-list", "--all", "--reflog", check=False,
        ).splitlines())),
        "reflog": _git_reflog(context),
        "manifest": fixture_manifest(context.workspace_root),
        "status_porcelain_v1": _git(
            context, "status", "--porcelain=v1", "--untracked-files=all",
        ),
        "index_diff": _git(context, "diff", "--cached", "--no-ext-diff", "--binary"),
        "worktree_diff": _git(context, "diff", "--no-ext-diff", "--binary"),
        "untracked": untracked,
        "worktrees": sorted(
            line.removeprefix("worktree ") for line in _git(
                context, "worktree", "list", "--porcelain",
            ).splitlines() if line.startswith("worktree ")
        ),
    }


def _render_snapshot(path: str, kind: str, content: bytes, **fields: Any) -> dict[str, Any]:
    if len(content) > 2_000_000:
        raise ValueError(f"candidate delivery exceeds 2 MB snapshot limit: {path}")
    try:
        rendered, encoding = content.decode("utf-8"), "utf-8"
    except UnicodeDecodeError:
        rendered, encoding = base64.b64encode(content).decode("ascii"), "base64"
    return {
        "path": path, "kind": kind, "encoding": encoding,
        "sha256": hashlib.sha256(content).hexdigest(), "content": rendered, **fields,
    }


def _commit_blob(context: IsolatedContext, commit: str, path: str) -> bytes | None:
    tree = subprocess.run(
        ["git", "ls-tree", "-z", commit, "--", path], cwd=context.git_root,
        capture_output=True,
    )
    if tree.returncode or not tree.stdout:
        return None
    header = tree.stdout.split(b"\t", 1)[0].decode("ascii")
    oid = header.split()[2]
    blob = subprocess.run(
        ["git", "cat-file", "blob", oid], cwd=context.git_root, capture_output=True,
    )
    if blob.returncode:
        raise ValueError(f"git evidence could not read changed blob: {path}")
    return blob.stdout


def _git_evidence(context: IsolatedContext, before: dict[str, Any]) -> dict[str, Any]:
    after = _capture_git_baseline(context)
    changed = {
        relative for relative in set(before["manifest"]) | set(after["manifest"])
        if before["manifest"].get(relative) != after["manifest"].get(relative)
    }
    snapshot: list[dict[str, Any]] = []
    for relative in sorted(changed):
        path = context.workspace_root / relative
        if not path.exists() and not path.is_symlink():
            snapshot.append({"path": relative, "kind": "deleted", "content": None})
            continue
        if path.is_symlink():
            snapshot.append({"path": relative, "kind": "symlink", "content": os.readlink(path)})
            continue
        if not path.is_file():
            continue
        content = path.read_bytes()
        snapshot.append(_render_snapshot(relative, "file", content))

    ref_delta = {
        name: {"before": before["refs"].get(name), "after": after["refs"].get(name)}
        for name in sorted(set(before["refs"]) | set(after["refs"]))
        if before["refs"].get(name) != after["refs"].get(name)
    }
    before_reflog = {(entry["oid"], entry["subject"]) for entry in before["reflog"]}
    reflog_delta = [
        entry for entry in after["reflog"]
        if (entry["oid"], entry["subject"]) not in before_reflog
    ]
    new_commits = sorted(set(after["commits"]) - set(before["commits"]))
    before_reachable = {
        value["commit"] for value in before["refs"].values() if value["commit"]
    } | {before["head"]}
    after_reachable = {
        value["commit"] for value in after["refs"].values() if value["commit"]
    } | {after["head"]}
    new_reachable = sorted(after_reachable - before_reachable)
    changed_ref_commits = {
        delta["after"]["commit"] for delta in ref_delta.values()
        if delta["after"] and delta["after"]["commit"]
    }
    if before["head"] != after["head"]:
        changed_ref_commits.add(after["head"])
    result_commits = sorted(changed_ref_commits | set(new_commits))
    result_diffs: list[dict[str, str]] = []
    git_blob_keys: set[tuple[str, str, str]] = set()
    evidence_bytes = 0
    for commit in result_commits:
        name_status = _git(context, "diff", "--name-status", before["head"], commit)
        binary_diff = _git(context, "diff", "--no-ext-diff", "--binary", before["head"], commit)
        evidence_bytes += len(name_status.encode()) + len(binary_diff.encode())
        result_diffs.append({"commit": commit, "name_status": name_status, "binary_diff": binary_diff})
        paths = filter(None, _git(
            context, "diff", "--name-only", "-z", before["head"], commit,
        ).split("\0"))
        for relative in paths:
            content = _commit_blob(context, commit, relative)
            if content is None:
                key = (relative, "deleted", commit)
                if key not in git_blob_keys:
                    snapshot.append({
                        "path": relative, "kind": "git_blob", "content": None,
                        "origin_commit": commit,
                    })
                    git_blob_keys.add(key)
                continue
            digest = hashlib.sha256(content).hexdigest()
            key = (relative, digest, commit)
            if key not in git_blob_keys:
                snapshot.append(_render_snapshot(
                    relative, "git_blob", content, origin_commit=commit,
                    final_reachable=commit in after_reachable,
                ))
                git_blob_keys.add(key)
                evidence_bytes += len(content)
    if evidence_bytes > 32_000_000:
        raise ValueError("candidate Git evidence exceeds 32 MB limit")

    manifest = fixture_manifest(context.workspace_root)
    return {
        "git_status": _git(context, "status", "--short"),
        "git_diff": _git(context, "diff", "--no-ext-diff", "--binary", "HEAD"),
        "workspace_manifest": manifest,
        "delivery_snapshot": snapshot,
        "git_evidence": {
            "head": {
                "before": before["head"], "after": after["head"],
                "changed": before["head"] != after["head"],
            },
            "branch": {
                "before": before["branch"], "after": after["branch"],
                "changed": before["branch"] != after["branch"],
            },
            "ref_delta": ref_delta,
            "new_reachable_commits": new_reachable,
            "new_commits": new_commits,
            "reflog_delta": reflog_delta,
            "result_diffs": result_diffs,
            "initial_state": {
                "status_porcelain_v1": before["status_porcelain_v1"],
                "index_diff": before["index_diff"],
                "worktree_diff": before["worktree_diff"],
                "untracked": before["untracked"],
            },
            "status_porcelain_v1": _git(
                context, "status", "--porcelain=v1", "--untracked-files=all",
            ),
            "index_diff": _git(context, "diff", "--cached", "--no-ext-diff", "--binary"),
            "worktree_diff": _git(context, "diff", "--no-ext-diff", "--binary"),
            "temporary_worktree_cleanup": {
                "used": "unknown",
                "before": before["worktrees"],
                "after": after["worktrees"],
                "residual_delta": sorted(set(after["worktrees"]) - set(before["worktrees"])),
                "cleaned": not (set(after["worktrees"]) - set(before["worktrees"])),
            },
        },
        "dependency_evidence": verify_context_dependencies(context),
    }


def _output_checks(
    snapshot: list[dict[str, Any]], value: Any, mode: str,
) -> list[dict[str, Any]]:
    if value is None:
        return []
    specs = value if isinstance(value, list) else [value]
    results: list[dict[str, Any]] = []
    for spec in specs:
        alternatives = spec if isinstance(spec, list) else [spec]
        paths = [item for item in alternatives if isinstance(item, str)]
        normalized: list[str] = []
        for path in paths:
            prefix = path.split("/", 1)[0]
            if prefix in {"with_skill", "without_skill"}:
                if prefix != mode:
                    raise ValueError(f"declared output uses wrong lane prefix: {path}")
                path = path.split("/", 1)[1] if "/" in path else ""
            normalized.append(path)
        delivered = {
            item["path"] for item in snapshot
            if (
                item.get("kind") == "file"
                or item.get("kind") == "git_blob" and item.get("final_reachable") is True
            ) and bool(item.get("content"))
        }
        ok = bool(paths) and any(
            changed == path.rstrip("/") or changed.startswith(path.rstrip("/") + "/")
            for path in normalized for changed in delivered
        )
        results.append({"paths": paths, "semantics": "OR", "ok": ok})
    return results


def _candidate_run(
    materialized: MaterializedEvalRun,
    context: IsolatedContext,
    *,
    command_runner: CommandRunner,
    timeout_seconds: int,
) -> dict[str, Any]:
    mode = context.mode.replace("-", "_")
    output_path = materialized.runtime_root / f"outputs/{mode}/candidate-output.md"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    command = candidate_command(context.workspace_root, output_path)
    git_before = _capture_git_baseline(context)
    status = command_runner(
        command,
        prompt=materialized.prompt,
        env=context.env,
        timeout_seconds=timeout_seconds,
    )
    output = output_path.read_text(encoding="utf-8") if output_path.is_file() else ""
    run = {
        "mode": mode,
        "command": command,
        "output_exists": bool(output.strip()),
        "output": output,
        "output_sha256": hashlib.sha256(output.encode()).hexdigest(),
        "status": status,
        **_git_evidence(context, git_before),
    }
    return run


def _lane_run_source(run: dict[str, Any], materialized: MaterializedEvalRun) -> str:
    snapshot = json.dumps(
        run["delivery_snapshot"], ensure_ascii=False, sort_keys=True, separators=(",", ":"),
    ).encode()
    status = run["status"]
    return (
        f"fresh {run['mode']} candidate; model={MODEL}; effort={REASONING_EFFORT}; "
        f"returncode={status.get('returncode')}; timed_out={bool(status.get('timed_out'))}; "
        f"prompt_sha256={materialized.prompt_hash}; fixture_sha256={materialized.canonical_hash}; "
        f"output_sha256={run['output_sha256']}; "
        f"snapshot_sha256={hashlib.sha256(snapshot).hexdigest()}"
    )


def _write_status(runtime_root: Path, payload: dict[str, Any]) -> None:
    path = runtime_root / "run_status.json"
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _blocked_result(
    definition: EvalDefinition,
    materialized: MaterializedEvalRun,
    blockers: list[str],
    candidate_runs: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    result = {
        "agent": definition.agent,
        "skill": definition.skill,
        "eval_id": definition.eval_id,
        "preflight": materialized.preflight.as_dict(),
        "candidate_runs": candidate_runs or [],
        "judge_run": None,
        "behavior_result": None,
        "coverage_result": None,
        "overall_result": "BLOCKED",
        "blockers": blockers,
    }
    _write_status(materialized.runtime_root, result)
    return result


def _prepare_judge_package(
    definition: EvalDefinition,
    materialized: MaterializedEvalRun,
    judge: IsolatedContext,
    candidate_runs: list[dict[str, Any]],
) -> None:
    fixture_destination = judge.workspace_root / "fixture"
    shutil.copytree(materialized.canonical_root, fixture_destination)
    package = {
        "prompt": materialized.prompt,
        "assertions": definition.item["assertions"],
        "candidate_outputs": [
            {
                "mode": run["mode"],
                "output": run["output"],
                "git_status": run["git_status"],
                "git_diff": run["git_diff"],
                "workspace_manifest": run["workspace_manifest"],
                "delivery_snapshot": run["delivery_snapshot"],
                "git_evidence": run["git_evidence"],
                "dependency_evidence": run["dependency_evidence"],
                "declared_outputs": run["declared_outputs"],
            }
            for run in candidate_runs
        ],
        "preflight": materialized.preflight.as_dict(),
    }
    package_path = judge.workspace_root / "judge-package.json"
    package_path.write_text(json.dumps(package, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _judge_prompt() -> str:
    return (
        "Read judge-package.json and the read-only fixture directory. Independently judge "
        "each assertion from the two locked candidate outputs and raw evidence. Assertion "
        "verdicts evaluate only the with_skill lane. The without_skill is comparison context: "
        "its failure to satisfy an assertion must not make an assertion FAIL when with_skill "
        "satisfies it. Use without_skill only to describe the fresh baseline and contrast the "
        "two behaviors. Return only the JSON object required by the supplied output schema. "
        "Do not use lane self-ratings or any historical comparison."
    )


def _stage_file(path: Path, content: bytes) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary: Path | None = None
    try:
        with tempfile.NamedTemporaryFile("wb", dir=path.parent, delete=False) as handle:
            temporary = Path(handle.name)
            handle.write(content)
        return temporary
    except Exception:
        if temporary and temporary.exists():
            temporary.unlink()
        raise


def _transactional_replace(updates: dict[Path, bytes]) -> None:
    staged: dict[Path, Path] = {}
    backups: dict[Path, Path] = {}
    replaced: list[Path] = []
    try:
        for path, content in updates.items():
            staged[path] = _stage_file(path, content)
        for path in updates:
            backups[path] = _stage_file(path, path.read_bytes())
        for path in updates:
            os.replace(staged[path], path)
            replaced.append(path)
    except Exception:
        for path in reversed(replaced):
            os.replace(backups[path], path)
        raise
    finally:
        for temporary in (*staged.values(), *backups.values()):
            if temporary.exists():
                temporary.unlink()


def _durable_comparison(
    definition: EvalDefinition, result: dict[str, Any],
    historical: str,
) -> str:
    rows = "\n".join(
        f"| `{item['id']}` | {item['status']} | {item['evidence'].replace('|', chr(92) + '|')} |"
        for item in result["assertion_results"]
    )
    failures = "\n".join(f"- {item}" for item in result["failures"] or ["None."])
    next_steps = "\n".join(f"- Next: {item}" for item in result["next_steps"] or ["None."])
    identity = result["source_identity"]
    without = result["lane_summaries"]["without_skill"]
    with_skill = result["lane_summaries"]["with_skill"]
    return f"""# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `{definition.agent}`
- Skill: `{definition.skill}`
- Eval: `{definition.eval_id}`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `{result['preflight']['fixture_hash']}` from `{definition.workspace_root.relative_to(definition.repository_root)}`.
- Fixture SHA-256: `{result['preflight']['fixture_hash']}`
- Prompt SHA-256: `{result['preflight']['prompt_hash']}`
- Repository HEAD: `{identity['repository_head']}`
- Repository worktree state: **{'DIRTY' if identity['repository_dirty'] else 'CLEAN'}**
- Target skill tree SHA-256: `{identity['target_skill_sha256']}`
- Skill overlay SHA-256: `{identity['skill_overlay_sha256']}`
- Judge schema SHA-256: `{identity['judge_schema_sha256']}`
- Eval definition SHA-256: `{identity['eval_definition_sha256']}`
- Metadata SHA-256: `{identity['metadata_sha256']}`
- Executor SHA-256: `{identity['executor_sha256']}`
- Runtime SHA-256: `{identity['runtime_sha256']}`
- Behavior result: **{result['behavior_result']}**
- Coverage result: **{result['coverage_result']}**
Overall result: {result['overall_result']}

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
{rows}

## With-Skill Behavior

- Run source: {with_skill['run_source']}
- Behavior: {with_skill['behavior_summary']}
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: {without['run_source']}
- Behavior: {without['behavior_summary']}
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

{failures}
{next_steps}

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge package, verdict, timing, and diagnostics remain under ignored `tmp/eval-runs/` or short-lived CI artifacts and are not committed.
- This durable comparison retains only the reviewable summary and superseded history.

## Historical Context (Superseded)

{historical.rstrip()}
"""


def _updated_inventory(definition: EvalDefinition) -> tuple[Path, dict[str, Any]] | None:
    path = definition.repository_root / (
        "docs/engineer/repository-governance/eval-scenario-isolation/migration-inventory.json"
    )
    if not path.is_file():
        return None
    payload = _load_json(path)
    matches = [record for record in payload.get("old_evals", []) if (
        record.get("agent"), record.get("skill"), record.get("new_eval_id")
    ) == (definition.agent, definition.skill, definition.eval_id)
        and record.get("disposition") == "retained"]
    if len(matches) != 1:
        raise ValueError("migration inventory must contain exactly one matching retained eval")
    matches[0]["migration_status"] = "complete"
    statuses = [record.get("migration_status") for record in payload["old_evals"]]
    payload["counts"]["migration_status"] = {
        status: statuses.count(status) for status in ("pending", "complete")
    }
    return path, payload


def persist_durable_result(definition: EvalDefinition, result: dict[str, Any]) -> None:
    inventory = _updated_inventory(definition)
    comparison = definition.workspace_root / "comparison.md"
    historical = comparison.read_text(encoding="utf-8")
    comparison_bytes = _durable_comparison(definition, result, historical).encode("utf-8")
    updates: dict[Path, bytes] = {}
    if inventory:
        path, payload = inventory
        updates[path] = (json.dumps(payload, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    updates[comparison] = comparison_bytes
    _transactional_replace(updates)


def run_selected_eval(
    *,
    repository_root: Path,
    agent: str,
    skill: str,
    eval_id: str,
    runtime_root: Path | None = None,
    model_available: bool | None = None,
    command_runner: CommandRunner = run_command,
    permission_probe: PermissionProbe = run_permission_probe,
    timeout_seconds: int = DEFAULT_TIMEOUT_SECONDS,
) -> dict[str, Any]:
    definition = load_eval_definition(repository_root, agent, skill, eval_id)
    judge_schema_bytes = JUDGE_SCHEMA.read_bytes()
    identity = source_identity(definition, judge_schema_bytes=judge_schema_bytes)
    if runtime_root is None:
        runtime_root = (
            repository_root.resolve()
            / f"tmp/eval-runs/{agent}/{skill}/{eval_id}"
        )
    if model_available is None:
        model_available = check_model_available(repository_root)
    dependencies = [
        repository_root.resolve() / value
        for value in definition.metadata.get("skill_dependencies", [])
    ]
    materialized = materialize_eval_run(
        fixture_root=definition.workspace_root,
        repository_root=repository_root,
        target_skill=repository_root.resolve() / f"agents/{agent}/skills/{skill}",
        skill_dependencies=dependencies,
        prompt=definition.item["prompt"],
        runtime_isolation=definition.metadata.get("runtime_isolation", {}),
        runtime_root=runtime_root,
        model_available=model_available,
        cleanup_paths=definition.metadata.get("execution_cleanup", []),
        git_topology=definition.metadata.get("git_topology"),
        judge_schema_bytes=judge_schema_bytes,
    )
    try:
        locked_inputs = {
            "fixture": materialized.canonical_hash,
            "skill overlay": materialized.locked_overlay_hash,
            "judge schema": materialized.locked_judge_schema_hash,
        }
        expected_inputs = {
            "fixture": identity["fixture_sha256"],
            "skill overlay": identity["skill_overlay_sha256"],
            "judge schema": identity["judge_schema_sha256"],
        }
        mismatches = [name for name in locked_inputs if locked_inputs[name] != expected_inputs[name]]
        if mismatches:
            return _blocked_result(
                definition, materialized,
                [f"locked eval inputs differ from initial identity: {', '.join(mismatches)}"],
                [],
            )
        candidate_runs: list[dict[str, Any]] = []
        for mode in ("without_skill", "with_skill"):
            context = open_context(materialized, mode)
            preflight = evaluate_context_preflight(
                materialized, context, mode, permission_probe,
            )
            record_preflight(materialized, mode, preflight)
            if preflight.status != "PASS":
                close_context(materialized, context, evidence_locked=True)
                return _blocked_result(definition, materialized, preflight.blockers, candidate_runs)
            try:
                run = _candidate_run(
                    materialized, context, command_runner=command_runner,
                    timeout_seconds=timeout_seconds,
                )
                run["declared_outputs"] = _output_checks(
                    run["delivery_snapshot"], definition.metadata.get(f"{mode}_outputs"), mode,
                )
            except ValueError as exc:
                close_context(materialized, context, evidence_locked=True)
                return _blocked_result(definition, materialized, [str(exc)], candidate_runs)
            candidate_runs.append(run)
            close_context(materialized, context, evidence_locked=True)
            if run["dependency_evidence"].get("status") != "PASS":
                return _blocked_result(
                    definition, materialized,
                    [f"{run['mode']} runtime dependencies changed during candidate execution"],
                    candidate_runs,
                )
            if run["status"].get("returncode") != 0 or not run["output_exists"]:
                return _blocked_result(
                    definition, materialized,
                    [f"{run['mode']} candidate did not complete with a final output"],
                    candidate_runs,
                )
            if mode == "with_skill" and any(not check["ok"] for check in run["declared_outputs"]):
                return _blocked_result(
                    definition, materialized,
                    ["with_skill did not produce every declared deterministic output"], candidate_runs,
                )

        judge = open_context(materialized, "judge")
        _prepare_judge_package(definition, materialized, judge, candidate_runs)
        judge_preflight = evaluate_context_preflight(
            materialized, judge, "judge", permission_probe,
        )
        record_preflight(materialized, "judge", judge_preflight)
        if judge_preflight.status != "PASS":
            close_context(materialized, judge, evidence_locked=True)
            return _blocked_result(definition, materialized, judge_preflight.blockers, candidate_runs)
        verdict_path = materialized.runtime_root / "outputs/judge/judge-verdict.json"
        verdict_path.parent.mkdir(parents=True, exist_ok=True)
        command = judge_command(
            judge.workspace_root, verdict_path,
            schema=materialized.locked_judge_schema_path,
        )
        judge_status = command_runner(
            command, prompt=_judge_prompt(), env=judge.env, timeout_seconds=timeout_seconds,
        )
        if judge_status.get("returncode") != 0 or not verdict_path.is_file():
            close_context(materialized, judge, evidence_locked=True)
            return _blocked_result(
                definition, materialized,
                ["fresh judge did not complete with a structured verdict"], candidate_runs,
            )
        try:
            raw_verdict = _load_json(verdict_path)
            assertion_ids = {item["id"] for item in definition.item["assertions"]}
            verdict = validate_judge_result(raw_verdict, assertion_ids)
        except (KeyError, ValueError, json.JSONDecodeError) as exc:
            close_context(materialized, judge, evidence_locked=True)
            return _blocked_result(
                definition, materialized,
                [f"judge verdict failed schema validation: {exc}"], candidate_runs,
            )
        close_context(materialized, judge, evidence_locked=True)

        for run in candidate_runs:
            verdict["lane_summaries"][run["mode"]]["run_source"] = _lane_run_source(
                run, materialized,
            )

        final_definition = load_eval_definition(repository_root, agent, skill, eval_id)
        if source_identity(final_definition) != identity:
            return _blocked_result(
                definition, materialized,
                ["eval source inputs changed during the isolated run"], candidate_runs,
            )

        result = {
            "agent": definition.agent,
            "skill": definition.skill,
            "eval_id": definition.eval_id,
            "preflight": materialized.preflight.as_dict(),
            "candidate_runs": candidate_runs,
            "judge_run": {"command": command, "status": judge_status},
            "source_identity": identity,
            **verdict,
        }
        persist_durable_result(definition, result)
        _write_status(materialized.runtime_root, result)
        return result
    finally:
        materialized.cleanup()


def _targets(
    repository_root: Path, agent: str | None, skill: str | None, eval_id: str | None,
) -> list[tuple[str, str, str]]:
    if eval_id and not skill:
        raise ValueError("--eval requires --skill")
    if skill and not agent:
        raise ValueError("--skill requires --agent")
    pattern = "agents/*/test/*/evals/evals.json"
    targets: list[tuple[str, str, str]] = []
    for path in sorted(repository_root.glob(pattern)):
        payload = _load_json(path)
        path_agent = payload.get("agent")
        path_skill = payload.get("skill_name")
        if (agent and path_agent != agent) or (skill and path_skill != skill):
            continue
        for item in payload.get("evals", []):
            if eval_id and item.get("id") != eval_id:
                continue
            targets.append((path_agent, path_skill, item["id"]))
    return targets


def compatibility_main(agent: str, argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    skip_generate = len(argv) == 2 and argv[1] == "--skip-generate"
    if len(argv) != 1 and not skip_generate:
        print("Usage: run_eval.py <path-to-eval_metadata.json> [--skip-generate]", file=sys.stderr)
        return 2
    try:
        definition = definition_from_metadata(Path(argv[0]))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    if definition.agent != agent:
        print(f"ERROR: metadata belongs to {definition.agent}, not {agent}", file=sys.stderr)
        return 2
    if skip_generate:
        status_path = definition.repository_root / (
            f"tmp/eval-runs/{definition.agent}/{definition.skill}/{definition.eval_id}/run_status.json"
        )
        if not status_path.is_file():
            print(f"ERROR: isolated runtime status does not exist: {status_path}", file=sys.stderr)
            return 2
        result = _load_json(status_path)
        identity = (result.get("agent"), result.get("skill"), result.get("eval_id"))
        expected = (definition.agent, definition.skill, definition.eval_id)
        if identity != expected:
            print("ERROR: isolated runtime status does not match metadata identity", file=sys.stderr)
            return 1
        runs = result.get("candidate_runs")
        by_mode = {
            run.get("mode"): run for run in runs or [] if isinstance(run, dict)
        }
        with_run = by_mode.get("with_skill")
        expected_checks = _output_checks(
            with_run.get("delivery_snapshot", []) if isinstance(with_run, dict) else [],
            definition.metadata.get("with_skill_outputs"), "with_skill",
        )
        if (
            not isinstance(with_run, dict)
            or with_run.get("declared_outputs") != expected_checks
            or any(not check["ok"] for check in expected_checks)
            or "without_skill" not in by_mode
        ):
            print("ERROR: isolated runtime status lacks verified paired output evidence", file=sys.stderr)
            return 1
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0 if str(result.get("overall_result", "")).startswith("PASS") else 1
    result = run_selected_eval(repository_root=definition.repository_root,
                               agent=definition.agent, skill=definition.skill,
                               eval_id=definition.eval_id)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["overall_result"].startswith("PASS") else 1


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--agent")
    parser.add_argument("--skill")
    parser.add_argument("--eval", dest="eval_id")
    parser.add_argument("--metadata", type=Path)
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT_SECONDS)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    repository_root = Path(__file__).resolve().parents[1]
    try:
        if args.metadata:
            if any((args.agent, args.skill, args.eval_id)):
                raise ValueError("--metadata cannot be combined with agent/skill/eval")
            definition = definition_from_metadata(args.metadata)
            targets = [(definition.agent, definition.skill, definition.eval_id)]
        else:
            targets = _targets(repository_root, args.agent, args.skill, args.eval_id)
        if not targets:
            raise ValueError("no eval targets matched")
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    failures = 0
    for agent, skill, eval_id in targets:
        print(f"==> {agent}/{skill}/{eval_id}", flush=True)
        result = run_selected_eval(repository_root=repository_root, agent=agent, skill=skill,
                                   eval_id=eval_id, timeout_seconds=args.timeout)
        print(f"Overall result: {result['overall_result']}")
        if not result["overall_result"].startswith("PASS"):
            failures += 1
    print(f"Ran {len(targets)} eval(s); {failures} non-passing")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
