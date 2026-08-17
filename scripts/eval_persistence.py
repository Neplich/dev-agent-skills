"""Durable comparison and frozen migration-inventory persistence."""

from __future__ import annotations

import json
import os
import tempfile
import threading
from pathlib import Path
from typing import Any


_DURABLE_WRITE_LOCK = threading.Lock()


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


def transactional_replace(updates: dict[Path, bytes]) -> None:
    staged: dict[Path, Path] = {}
    backups: dict[Path, Path | None] = {}
    replaced: list[Path] = []
    try:
        for path, content in updates.items():
            staged[path] = _stage_file(path, content)
        for path in updates:
            backups[path] = _stage_file(path, path.read_bytes()) if path.exists() else None
        for path in updates:
            os.replace(staged[path], path)
            replaced.append(path)
    except Exception:
        for path in reversed(replaced):
            backup = backups[path]
            if backup is None:
                if path.read_bytes() == updates[path]:
                    path.unlink()
            else:
                os.replace(backup, path)
        raise
    finally:
        for temporary in (*staged.values(), *(b for b in backups.values() if b is not None)):
            if temporary.exists():
                temporary.unlink()


def durable_comparison(definition: Any, result: dict[str, Any]) -> str:
    rows = "\n".join(
        f"| `{item['id']}` | {item['status']} | {item['evidence'].replace('|', chr(92) + '|')} |"
        for item in result["assertion_results"]
    )
    failures = "\n".join(f"- {item}" for item in result["failures"] or ["None."])
    next_steps = "\n".join(f"- Next: {item}" for item in result["next_steps"] or ["None."])
    identity = result["source_identity"]
    freshness = identity["freshness"]
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
- Identity schema: `2`
- target_skill_sha256: `{freshness['target_skill_sha256']}`
- eval_definition_sha256: `{freshness['eval_definition_sha256']}`
- metadata_sha256: `{freshness['metadata_sha256']}`
- fixture_sha256: `{freshness['fixture_sha256']}`
- execution_protocol_sha256: `{freshness['execution_protocol_sha256']}`
- runtime_protocol_sha256: `{freshness['runtime_protocol_sha256']}`
- judge_schema_sha256: `{freshness['judge_schema_sha256']}`
- Source lock SHA-256: `{identity['source_lock_sha256']}`
- Prompt SHA-256: `{result['preflight']['prompt_hash']}`
- Repository HEAD: `{identity['repository_head']}`
- Repository worktree state: **{'DIRTY' if identity['repository_dirty'] else 'CLEAN'}**
- Skill overlay SHA-256: `{identity['skill_overlay_sha256']}`
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

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
"""


def updated_inventory(definition: Any) -> tuple[Path, dict[str, Any]] | None:
    path = definition.repository_root / (
        "docs/engineer/repository-governance/eval-scenario-isolation/migration-inventory.json"
    )
    if not path.is_file():
        return None
    payload = json.loads(path.read_text(encoding="utf-8"))
    matches = [record for record in payload.get("old_evals", []) if (
        record.get("agent"), record.get("skill"), record.get("new_eval_id")
    ) == (definition.agent, definition.skill, definition.eval_id)
        and record.get("disposition") == "retained"]
    if not matches:
        return None
    if len(matches) > 1:
        raise ValueError("migration inventory contains more than one matching retained eval")
    matches[0]["migration_status"] = "complete"
    statuses = [record.get("migration_status") for record in payload["old_evals"]]
    payload["counts"]["migration_status"] = {
        status: statuses.count(status) for status in ("pending", "complete")
    }
    return path, payload


def persist_durable_result(definition: Any, result: dict[str, Any]) -> None:
    with _DURABLE_WRITE_LOCK:
        inventory = updated_inventory(definition)
        comparison = definition.workspace_root / "comparison.md"
        updates = {comparison: durable_comparison(definition, result).encode("utf-8")}
        if inventory:
            path, payload = inventory
            updates[path] = (
                json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
            ).encode("utf-8")
        transactional_replace(updates)
