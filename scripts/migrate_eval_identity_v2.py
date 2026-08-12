#!/usr/bin/env python3
"""One-time, Git-attested migration of durable eval identities to schema v2."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.eval_identity import FRESHNESS_FIELDS as FRESHNESS_KEYS
from scripts.eval_identity import current_identity_v2
from scripts.run_skill_eval import build_judge_schema_bytes, load_eval_definition


AUDIT_RELATIVE_PATH = Path(
    "docs/engineer/repository-governance/eval-scenario-isolation/"
    "eval-identity-v2-migration-audit.json"
)
INVENTORY_RELATIVE_PATH = Path(
    "docs/engineer/repository-governance/eval-scenario-isolation/migration-inventory.json"
)
MANUAL_COMPARISON = Path("agents/docs/test/manual-gen/comparison.md")
LEGACY_LABELS = {
    "Target skill tree SHA-256": "target_skill_sha256",
    "Eval definition SHA-256": "eval_definition_sha256",
    "Metadata SHA-256": "metadata_sha256",
    "Fixture SHA-256": "fixture_sha256",
    "Judge schema SHA-256": "judge_schema_sha256",
}
EXPECTED_COUNTS = {"mechanical": 187, "stale": 6, "pending": 3, "manual_excluded": 1}
PRESERVED_PATTERNS = {
    "behavior": re.compile(rb"^- Behavior result:.*(?:\n|\Z)", re.M),
    "coverage": re.compile(rb"^- Coverage result:.*(?:\n|\Z)", re.M),
    "overall": re.compile(rb"^Overall result:.*(?:\n|\Z)", re.M),
    "assertions": re.compile(rb"^## Assertion Results\n\n.*?(?=^## |\Z)", re.M | re.S),
}


@dataclass(frozen=True)
class Target:
    agent: str
    skill: str
    eval_id: str
    comparison: Path


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _git(root: Path, *args: str) -> bytes:
    completed = subprocess.run(["git", *args], cwd=root, capture_output=True)
    if completed.returncode:
        raise ValueError(completed.stderr.decode(errors="replace").strip())
    return completed.stdout


def trusted_source(root: Path, source_ref: str) -> dict[str, str]:
    commit = _git(root, "rev-parse", "--verify", f"{source_ref}^{{commit}}").decode().strip()
    executor = _git(root, "show", f"{commit}:scripts/run_skill_eval.py")
    runtime = _git(root, "show", f"{commit}:scripts/eval_runtime.py")
    return {
        "source_ref": source_ref,
        "source_commit": commit,
        "executor_sha256": sha256(executor),
        "runtime_sha256": sha256(runtime),
    }


def enumerate_targets(root: Path) -> list[Target]:
    targets: list[Target] = []
    for evals_path in sorted(root.glob("agents/*/test/*/evals/evals.json")):
        payload = json.loads(evals_path.read_text(encoding="utf-8"))
        agent, skill = payload["agent"], payload["skill_name"]
        for item in payload["evals"]:
            definition = load_eval_definition(root, agent, skill, item["id"])
            targets.append(Target(
                agent, skill, item["id"], definition.workspace_root / "comparison.md",
            ))
    return targets


def _line_value(text: str, label: str) -> str | None:
    matches = re.findall(rf"^- {re.escape(label)}:\s*`([^`]+)`\s*$", text, re.M)
    if len(matches) > 1:
        raise ValueError(f"duplicate comparison field: {label}")
    return matches[0] if matches else None


def _preserved(data: bytes) -> dict[str, str]:
    result: dict[str, str] = {}
    for name, pattern in PRESERVED_PATTERNS.items():
        match = pattern.search(data)
        if match is None:
            raise ValueError(f"missing preserved comparison section: {name}")
        result[name] = sha256(match.group(0))
    return result


def _identity_lines(identity: dict[str, Any]) -> list[str]:
    if identity.get("identity_schema") not in {2, "2"}:
        raise ValueError("current identity is not schema v2")
    return ["- Identity schema: `2`", *(
        f"- {key}: `{identity[key]}`" for key in FRESHNESS_KEYS
    )]


def _replace_identity(
    text: str, identity: dict[str, Any], migration: dict[str, str], *, annotate: bool = True,
) -> str:
    lines = text.splitlines(keepends=True)
    removable = {
        "Fixture SHA-256", "Prompt SHA-256", "Target skill tree SHA-256",
        "Skill overlay SHA-256", "Judge schema SHA-256", "Eval definition SHA-256",
        "Metadata SHA-256", "Executor SHA-256", "Runtime SHA-256", "Identity schema",
        "Identity migration", "Identity migration source commit", "Identity migration audit",
        *FRESHNESS_KEYS,
    }
    kept: list[str] = []
    insertion: int | None = None
    for line in lines:
        label = re.match(r"^- ([^:]+):", line)
        if label and label.group(1) in removable:
            if insertion is None:
                insertion = len(kept)
            continue
        kept.append(line)
    if insertion is None:
        marker = next((i + 1 for i, line in enumerate(kept)
                       if line.startswith("- Repository worktree state:")), None)
        if marker is None:
            marker = next((i + 1 for i, line in enumerate(kept)
                           if line.startswith("- Preflight status:")), None)
        if marker is None:
            raise ValueError("comparison has no identity insertion point")
        insertion = marker
    block = [f"{line}\n" for line in _identity_lines(identity)]
    if annotate:
        block.extend([
            "- Identity migration: **MIGRATED_WITHOUT_MODEL_RERUN**\n",
            f"- Identity migration source commit: `{migration['source_commit']}`\n",
            f"- Identity migration audit: `{AUDIT_RELATIVE_PATH.as_posix()}`\n",
        ])
    kept[insertion:insertion] = block
    return "".join(kept)


def _mark_state(text: str, state: str, target: Target) -> str:
    text = re.sub(
        r"^- Evidence status:.*$", f"- Evidence status: **{state}**", text,
        count=1, flags=re.M,
    )
    if state == "PENDING":
        text = text.replace("- Eval: `PENDING`", f"- Eval: `{target.eval_id}`", 1)
    elif state == "STALE":
        text = re.sub(r"^Overall result:.*$", "Overall result: BLOCKED", text, count=1, flags=re.M)
    return text


def classify(target: Target, text: str, identity: dict[str, Any], source: dict[str, str]) -> tuple[str, list[str]]:
    evidence = re.search(r"^- Evidence status:\s*\*\*([^*]+)\*\*", text, re.M)
    if evidence and evidence.group(1) == "PENDING":
        return "pending", ["no_fresh_evidence"]
    if _line_value(text, "Identity schema") == "2":
        mismatches = [key for key in FRESHNESS_KEYS if _line_value(text, key) != identity[key]]
        if evidence and evidence.group(1) == "STALE":
            return "stale", [f"input_changed:{key}" for key in mismatches] or ["awaiting_fresh_rerun"]
        if mismatches:
            protocol_fields = {
                "execution_protocol_sha256", "runtime_protocol_sha256", "judge_schema_sha256",
            }
            if (
                not set(mismatches).issubset(protocol_fields)
                or "MIGRATED_WITHOUT_MODEL_RERUN" not in text
                or _line_value(text, "Identity migration source commit") != source["source_commit"]
            ):
                raise ValueError(f"{target.eval_id}: schema v2 input mismatch: {mismatches}")
            return "mechanical", ["identity_v2_protocol_finalized"]
        if "MIGRATED_WITHOUT_MODEL_RERUN" not in text:
            raise ValueError(f"{target.eval_id}: schema v2 comparison lacks migration evidence")
        return "mechanical", ["identity_v2_already_migrated"]
    old_executor = _line_value(text, "Executor SHA-256")
    old_runtime = _line_value(text, "Runtime SHA-256")
    if old_executor != source["executor_sha256"] or old_runtime != source["runtime_sha256"]:
        raise ValueError(f"{target.eval_id}: legacy protocol hash does not match --source-ref")
    mismatches = [
        key for label, key in LEGACY_LABELS.items()
        if _line_value(text, label) != identity[key]
    ]
    if mismatches:
        if target.agent == "engineer" and target.skill == "trd-gen":
            return "stale", [f"input_changed:{key}" for key in mismatches]
        raise ValueError(f"{target.eval_id}: unexpected current input mismatch: {mismatches}")
    return "mechanical", ["trusted_legacy_protocol", "current_inputs_match"]


def build_migration(root: Path, source_ref: str) -> tuple[dict[Path, bytes], dict[str, Any]]:
    inventory_path = root / INVENTORY_RELATIVE_PATH
    inventory_before = inventory_path.read_bytes()
    inventory = json.loads(inventory_before)
    inventory_paths = {record["comparison_path"] for record in inventory["old_evals"]}
    if len(inventory["old_evals"]) != 193 or len(inventory_paths) != 193:
        raise ValueError("frozen inventory must contain 193 unique comparison paths")
    source = trusted_source(root, source_ref)
    updates: dict[Path, bytes] = {}
    entries: list[dict[str, Any]] = []
    counts = {key: 0 for key in EXPECTED_COUNTS}
    assertion_rows = {"total": 0, "PASS": 0, "NOT_EXERCISED": 0, "FAIL": 0}

    for target in enumerate_targets(root):
        path = target.comparison
        rel = path.relative_to(root).as_posix()
        before = path.read_bytes()
        text = before.decode("utf-8")
        definition = load_eval_definition(root, target.agent, target.skill, target.eval_id)
        identity = current_identity_v2(
            definition,
            judge_schema_bytes=build_judge_schema_bytes(definition.item["assertions"]),
        )
        category, reasons = classify(target, text, identity, source)
        counts[category] += 1
        preserved_before = _preserved(before) if category != "pending" else {}
        migrated = _replace_identity(text, identity, source, annotate=category == "mechanical")
        if category == "stale":
            migrated = _mark_state(migrated, "STALE", target)
        elif category == "pending":
            migrated = _mark_state(migrated, "PENDING", target)
        after = migrated.encode("utf-8")
        preserved_after = _preserved(after) if category != "pending" else {}
        if category == "mechanical" and preserved_before != preserved_after:
            raise ValueError(f"{target.eval_id}: verdict or assertion evidence changed")
        if category == "mechanical":
            section = PRESERVED_PATTERNS["assertions"].search(before)
            assert section is not None
            rows = re.findall(rb"^\| `[^`]+` \| (PASS|FAIL|NOT_EXERCISED) \|", section.group(0), re.M)
            assertion_rows["total"] += len(rows)
            for status in rows:
                assertion_rows[status.decode()] += 1
        updates[path] = after
        entries.append({
            "agent": target.agent, "skill": target.skill, "eval_id": target.eval_id,
            "comparison_path": rel, "inventory_match_count": int(rel in inventory_paths),
            "classification": category, "reason_codes": reasons,
            "legacy_executor_sha256": _line_value(text, "Executor SHA-256"),
            "legacy_runtime_sha256": _line_value(text, "Runtime SHA-256"),
            "identity_v2": {key: identity[key] for key in FRESHNESS_KEYS},
            "preserved_raw_sha256_before": preserved_before,
            "preserved_raw_sha256_after": preserved_after,
            "before_sha256": sha256(before), "after_sha256": sha256(after),
        })

    if (root / MANUAL_COMPARISON).is_file():
        counts["manual_excluded"] = 1
    if counts != EXPECTED_COUNTS:
        raise ValueError(f"migration classification counts differ: {counts}")
    if assertion_rows != {"total": 807, "PASS": 717, "NOT_EXERCISED": 70, "FAIL": 20}:
        raise ValueError(f"mechanical assertion counts differ: {assertion_rows}")
    if inventory_path.read_bytes() != inventory_before:
        raise ValueError("frozen inventory changed during migration planning")
    audit = {
        "schema_version": "2.0", "migration": "eval-identity-v2",
        "mode": "dry-run", "source_attestation": source,
        "audit_path": AUDIT_RELATIVE_PATH.as_posix(),
        "verification_contract": [
            "uv run --with pytest pytest scripts/test_migrate_eval_identity_v2.py agents/test_eval_contract.py",
            "uv run scripts/check_eval_contract.py",
            "uv run scripts/check_eval_artifacts.py",
            "git diff --check",
        ],
        "counts": counts, "mechanical_assertion_rows": assertion_rows,
        "inventory_sha256_before": sha256(inventory_before),
        "inventory_sha256_after": sha256(inventory_path.read_bytes()),
        "entries": entries,
    }
    return updates, audit


def atomic_write(updates: dict[Path, bytes]) -> None:
    staged: dict[Path, Path] = {}
    backups: dict[Path, bytes] = {}
    existed: dict[Path, bool] = {}
    replaced: list[Path] = []
    try:
        for path, content in updates.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as handle:
                handle.write(content)
                staged[path] = Path(handle.name)
            existed[path] = path.exists()
            backups[path] = path.read_bytes() if existed[path] else b""
            os.chmod(staged[path], path.stat().st_mode if existed[path] else 0o644)
        for path, temporary in staged.items():
            os.replace(temporary, path)
            replaced.append(path)
    except Exception:
        for path in reversed(replaced):
            if existed[path]:
                path.write_bytes(backups[path])
            else:
                path.unlink(missing_ok=True)
        raise
    finally:
        for temporary in staged.values():
            temporary.unlink(missing_ok=True)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-ref", required=True)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--audit-output", type=Path)
    args = parser.parse_args(argv)
    root = Path(__file__).resolve().parents[1]
    updates, audit = build_migration(root, args.source_ref)
    if args.apply:
        if args.audit_output not in {None, AUDIT_RELATIVE_PATH}:
            parser.error(f"--apply audit path must be {AUDIT_RELATIVE_PATH.as_posix()}")
        audit["mode"] = "applied"
        audit_path = root / AUDIT_RELATIVE_PATH
        updates[audit_path] = (json.dumps(audit, ensure_ascii=False, indent=2) + "\n").encode()
        atomic_write(updates)
    elif args.audit_output:
        if args.audit_output != AUDIT_RELATIVE_PATH:
            parser.error(f"audit path must be {AUDIT_RELATIVE_PATH.as_posix()}")
        audit_path = args.audit_output if args.audit_output.is_absolute() else root / args.audit_output
        atomic_write({audit_path: (json.dumps(audit, ensure_ascii=False, indent=2) + "\n").encode()})
    else:
        print(json.dumps(audit, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
