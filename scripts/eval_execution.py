#!/usr/bin/env python3
"""Run paired skill evals with one shared isolation and judging boundary."""

from __future__ import annotations

import base64
import hashlib
import json
import os
import re
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
from scripts import eval_identity, eval_judging, eval_persistence  # noqa: E402


MODEL = "gpt-5.6-luna"
REASONING_EFFORT = "medium"
DEFAULT_TIMEOUT_SECONDS = 600
MAX_CANDIDATE_TRACE_CHARS = 250_000
JUDGE_SCHEMA = eval_judging.JUDGE_SCHEMA


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


def build_judge_schema_bytes(assertions: list[dict[str, Any]]) -> bytes:
    return eval_judging.build_judge_schema_bytes(assertions, schema_path=JUDGE_SCHEMA)


def source_identity(
    definition: EvalDefinition, *, judge_schema_bytes: bytes | None = None,
) -> dict[str, Any]:
    schema_bytes = judge_schema_bytes or build_judge_schema_bytes(definition.item["assertions"])
    return eval_identity.source_identity(definition, judge_schema_bytes=schema_bytes)


def _same_source_inputs(left: dict[str, Any], right: dict[str, Any]) -> bool:
    return eval_identity.same_source_inputs(left, right)


def _current_run_identity(definition: EvalDefinition) -> dict[str, Any]:
    return source_identity(
        definition,
        judge_schema_bytes=build_judge_schema_bytes(definition.item["assertions"]),
    )


def _prune_runtime_parents(runtime_root: Path, repository_root: Path) -> None:
    stop = (repository_root.resolve() / "tmp/eval-runs").resolve()
    current = runtime_root.resolve().parent
    if current != stop and stop not in current.parents:
        return
    while current == stop or stop in current.parents:
        try:
            current.rmdir()
        except OSError:
            return
        if current == stop:
            return
        current = current.parent


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
    command = _codex_command(workspace, output_path)
    command.insert(command.index("--output-last-message"), "--json")
    return command


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
        return {
            "returncode": completed.returncode,
            "timed_out": False,
            "stdout_tail": completed.stdout[-MAX_CANDIDATE_TRACE_CHARS:],
            "stderr_tail": completed.stderr[-50_000:],
        }
    except subprocess.TimeoutExpired as exc:
        stdout = exc.stdout.decode(errors="replace") if isinstance(exc.stdout, bytes) else exc.stdout or ""
        stderr = exc.stderr.decode(errors="replace") if isinstance(exc.stderr, bytes) else exc.stderr or ""
        return {
            "returncode": 124,
            "timed_out": True,
            "stdout_tail": stdout[-MAX_CANDIDATE_TRACE_CHARS:],
            "stderr_tail": stderr[-50_000:],
        }


def check_model_available(repository_root: Path) -> bool:
    if shutil.which("codex") is None:
        return False
    try:
        completed = subprocess.run(["codex", "debug", "models"], cwd=repository_root,
                                   capture_output=True, text=True, timeout=30)
    except (OSError, subprocess.TimeoutExpired):
        return False
    return completed.returncode == 0 and MODEL in completed.stdout


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
    return result


# Compatibility exports remain here while implementation ownership follows the
# explicit execution/judging/persistence module boundaries.
judge_command = eval_judging.judge_command
recompute_overall = eval_judging.recompute_overall
validate_judge_result = eval_judging.validate_judge_result
_prepare_judge_package = eval_judging.prepare_judge_package
_judge_prompt = eval_judging.judge_prompt
_stage_file = eval_persistence._stage_file
_transactional_replace = eval_persistence.transactional_replace
_durable_comparison = eval_persistence.durable_comparison
_updated_inventory = eval_persistence.updated_inventory
persist_durable_result = eval_persistence.persist_durable_result


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
    judge_schema_bytes = build_judge_schema_bytes(definition.item["assertions"])
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
    materialized: MaterializedEvalRun | None = None
    try:
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
            boundary_definition = load_eval_definition(repository_root, agent, skill, eval_id)
            if not _same_source_inputs(
                _current_run_identity(boundary_definition), identity,
            ):
                return _blocked_result(
                    definition, materialized,
                    ["eval source inputs changed during the isolated run"], candidate_runs,
                )
            if run["dependency_evidence"].get("status") != "PASS":
                return _blocked_result(
                    definition, materialized,
                    [f"{run['mode']} runtime dependencies changed during candidate execution"],
                    candidate_runs,
                )
            if run["status"].get("returncode") != 0 or not run["output_exists"]:
                status = run["status"]
                return _blocked_result(
                    definition, materialized,
                    [
                        f"{run['mode']} candidate did not complete with a final output "
                        f"(returncode={status.get('returncode')}, "
                        f"timed_out={bool(status.get('timed_out'))})"
                    ],
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
        if not _same_source_inputs(
            _current_run_identity(final_definition), identity,
        ):
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
        return result
    finally:
        if materialized is not None:
            materialized.cleanup()
        if runtime_root.exists():
            shutil.rmtree(runtime_root)
        _prune_runtime_parents(runtime_root, repository_root)
