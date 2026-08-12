"""Compute eval identity schema v2 and the complete same-run source lock."""

from __future__ import annotations

import hashlib
import json
import subprocess
import tempfile
from pathlib import Path
from typing import Any

from scripts.eval_runtime import (
    content_tree_hash,
    copy_canonical_fixture,
    fixture_manifest,
    manifest_hash,
    skill_overlay_hash,
)


IDENTITY_SCHEMA_VERSION = 2
FRESHNESS_FIELDS = (
    "target_skill_sha256",
    "eval_definition_sha256",
    "metadata_sha256",
    "fixture_sha256",
    "execution_protocol_sha256",
    "runtime_protocol_sha256",
    "judge_schema_sha256",
)
EXECUTION_PROTOCOL_FILES = (
    "eval_execution.py",
    "eval_judging.py",
)
RUNTIME_PROTOCOL_FILES = ("eval_runtime.py",)
SOURCE_LOCK_FILES = (
    "run_skill_eval.py",
    "eval_identity.py",
    "eval_execution.py",
    "eval_judging.py",
    "eval_runtime.py",
    "eval_persistence.py",
    "check_eval_contract.py",
    "eval_judge_result.schema.json",
)


def _hash_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _manifest_hash(manifest: dict[str, str]) -> str:
    canonical = json.dumps(
        manifest, ensure_ascii=False, sort_keys=True, separators=(",", ":"),
    ).encode()
    return _hash_bytes(canonical)


def source_manifest(script_root: Path | None = None) -> dict[str, str]:
    root = (script_root or Path(__file__).resolve().parent).resolve()
    return {name: _hash_bytes((root / name).read_bytes()) for name in SOURCE_LOCK_FILES}


def source_lock_sha256(manifest: dict[str, str]) -> str:
    if set(manifest) != set(SOURCE_LOCK_FILES):
        raise ValueError("source manifest must contain the exact eval source lock files")
    return _manifest_hash(manifest)


def protocol_hashes(
    script_root: Path | None = None, *, judge_schema_bytes: bytes | None = None,
) -> dict[str, str]:
    root = (script_root or Path(__file__).resolve().parent).resolve()
    execution = {name: _hash_bytes((root / name).read_bytes()) for name in EXECUTION_PROTOCOL_FILES}
    runtime = {name: _hash_bytes((root / name).read_bytes()) for name in RUNTIME_PROTOCOL_FILES}
    schema = (
        (root / "eval_judge_result.schema.json").read_bytes()
        if judge_schema_bytes is None else judge_schema_bytes
    )
    return {
        "execution_protocol_sha256": _manifest_hash(execution),
        "runtime_protocol_sha256": _manifest_hash(runtime),
        "judge_schema_sha256": _hash_bytes(schema),
    }


def current_identity_v2(
    definition: Any, *, judge_schema_bytes: bytes | None = None,
) -> dict[str, Any]:
    repository_root = definition.repository_root
    target = repository_root / f"agents/{definition.agent}/skills/{definition.skill}"
    with tempfile.TemporaryDirectory() as temporary:
        canonical = Path(temporary) / "canonical"
        copy_canonical_fixture(
            definition.workspace_root, canonical,
            cleanup_paths=definition.metadata.get("execution_cleanup", []),
        )
        fixture_hash = manifest_hash(fixture_manifest(canonical))
    protocols = protocol_hashes(judge_schema_bytes=judge_schema_bytes)
    freshness = {
        "target_skill_sha256": content_tree_hash(target),
        "eval_definition_sha256": _hash_bytes(json.dumps(
            definition.item, ensure_ascii=False, sort_keys=True, separators=(",", ":"),
        ).encode()),
        "metadata_sha256": _hash_bytes(definition.metadata_bytes),
        "fixture_sha256": fixture_hash,
        **protocols,
    }
    return {
        "identity_schema": IDENTITY_SCHEMA_VERSION,
        "freshness": freshness,
        **freshness,
    }


def source_identity(
    definition: Any, *, judge_schema_bytes: bytes | None = None,
) -> dict[str, Any]:
    repository_root = definition.repository_root
    identity = current_identity_v2(definition, judge_schema_bytes=judge_schema_bytes)
    head = subprocess.run(
        ["git", "rev-parse", "--verify", "HEAD"], cwd=repository_root,
        capture_output=True, text=True,
    )
    status = subprocess.run(
        ["git", "status", "--porcelain", "--untracked-files=all"],
        cwd=repository_root, capture_output=True, text=True,
    )
    target = repository_root / f"agents/{definition.agent}/skills/{definition.skill}"
    overlay_paths = [target, *(
        repository_root / value for value in definition.metadata.get("skill_dependencies", [])
    )]
    manifest = source_manifest()
    return {
        **identity,
        "repository_head": head.stdout.strip() if head.returncode == 0 else "unavailable",
        "repository_dirty": status.returncode != 0 or bool(status.stdout),
        "skill_overlay_sha256": skill_overlay_hash(overlay_paths, repository_root),
        "source_manifest": manifest,
        "source_lock_sha256": source_lock_sha256(manifest),
    }


def same_source_inputs(left: dict[str, Any], right: dict[str, Any]) -> bool:
    return (
        left.get("identity_schema") == right.get("identity_schema") == IDENTITY_SCHEMA_VERSION
        and left.get("freshness") == right.get("freshness")
        and left.get("skill_overlay_sha256") == right.get("skill_overlay_sha256")
        and left.get("source_manifest") == right.get("source_manifest")
        and left.get("source_lock_sha256") == right.get("source_lock_sha256")
    )
