from __future__ import annotations

import hashlib
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts import migrate_eval_identity_v2 as migration


def _identity(marker: str = "a") -> dict[str, str | int]:
    return {"identity_schema": 2, **{key: marker * 64 for key in migration.FRESHNESS_KEYS}}


def _comparison(executor: str, runtime: str, *, target: str = "a", definition: str = "a") -> str:
    return f"""# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `bug-analyzer`
- Eval: `eval-001-real-user`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Repository worktree state: **CLEAN**
- Target skill tree SHA-256: `{target * 64}`
- Eval definition SHA-256: `{definition * 64}`
- Metadata SHA-256: `{'a' * 64}`
- Fixture SHA-256: `{'a' * 64}`
- Judge schema SHA-256: `{'a' * 64}`
- Executor SHA-256: `{executor}`
- Runtime SHA-256: `{runtime}`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_evidence` | PASS | exact evidence bytes |

## With-Skill Behavior

- Behavior: done
"""


def _target(tmp_path: Path) -> migration.Target:
    return migration.Target("qa", "bug-analyzer", "eval-001-real-user", tmp_path / "comparison.md")


def test_trusted_source_attests_actual_git_blobs(tmp_path: Path) -> None:
    root = tmp_path / "repo"
    (root / "scripts").mkdir(parents=True)
    (root / "scripts/run_skill_eval.py").write_bytes(b"executor")
    (root / "scripts/eval_runtime.py").write_bytes(b"runtime")
    subprocess.run(["git", "init", "-q", "-b", "main"], cwd=root, check=True)
    subprocess.run(["git", "add", "."], cwd=root, check=True)
    subprocess.run([
        "git", "-c", "user.name=Test", "-c", "user.email=test@example.invalid",
        "commit", "-q", "-m", "source",
    ], cwd=root, check=True)

    attestation = migration.trusted_source(root, "HEAD")

    assert attestation["source_commit"] == subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=root, check=True, capture_output=True, text=True,
    ).stdout.strip()
    assert attestation["executor_sha256"] == hashlib.sha256(b"executor").hexdigest()
    assert attestation["runtime_sha256"] == hashlib.sha256(b"runtime").hexdigest()


def test_trusted_source_rejects_unreachable_ref(tmp_path: Path) -> None:
    with pytest.raises(ValueError):
        migration.trusted_source(tmp_path, "missing-ref")


def test_classify_rejects_forged_legacy_protocol_hash(tmp_path: Path) -> None:
    source = {"executor_sha256": "e" * 64, "runtime_sha256": "r" * 64}
    text = _comparison("f" * 64, "r" * 64)

    with pytest.raises(ValueError, match="legacy protocol hash"):
        migration.classify(_target(tmp_path), text, _identity(), source)


def test_classify_current_input_change_only_allows_trd_stale(tmp_path: Path) -> None:
    source = {"executor_sha256": "e" * 64, "runtime_sha256": "r" * 64}
    text = _comparison("e" * 64, "r" * 64, target="b")

    with pytest.raises(ValueError, match="unexpected current input mismatch"):
        migration.classify(_target(tmp_path), text, _identity(), source)

    trd = migration.Target("engineer", "trd-gen", "eval-001-trd", tmp_path / "trd.md")
    category, reasons = migration.classify(trd, text, _identity(), source)
    assert category == "stale"
    assert reasons == ["input_changed:target_skill_sha256"]


def test_identity_replacement_preserves_verdict_and_assertion_bytes(tmp_path: Path) -> None:
    before = _comparison("e" * 64, "r" * 64).encode()
    migrated = migration._replace_identity(
        before.decode(), _identity(), {"source_commit": "c" * 40},
    ).encode()

    assert migration._preserved(before) == migration._preserved(migrated)
    assert b"Executor SHA-256" not in migrated
    assert b"Runtime SHA-256" not in migrated
    assert b"Prompt SHA-256" not in migrated
    assert b"- Identity schema: `2`" in migrated
    assert b"MIGRATED_WITHOUT_MODEL_RERUN" in migrated


def test_checker_policy_keeps_nonfreshness_audit_fields_outside_migration():
    before = _comparison("e" * 64, "r" * 64)
    before = before.replace(
        "- Executor SHA-256:",
        f"- Prompt SHA-256: `{'p' * 64}`\n- Skill overlay SHA-256: `{'s' * 64}`\n"
        "- Executor SHA-256:",
    )
    migrated = migration._replace_identity(before, _identity(), {"source_commit": "c" * 40})
    assert "Prompt SHA-256" not in migrated
    assert "Skill overlay SHA-256" not in migrated


def test_preserved_digest_detects_evidence_tampering() -> None:
    before = _comparison("e" * 64, "r" * 64).encode()
    after = before.replace(b"exact evidence bytes", b"altered evidence bytes")
    assert migration._preserved(before) != migration._preserved(after)


def test_atomic_write_rolls_back_all_replaced_files(tmp_path: Path, monkeypatch) -> None:
    first, second = tmp_path / "first", tmp_path / "second"
    first.write_bytes(b"old-first")
    second.write_bytes(b"old-second")
    real_replace = migration.os.replace
    calls = 0

    def fail_second(source: Path, target: Path) -> None:
        nonlocal calls
        calls += 1
        if calls == 2:
            raise OSError("injected replacement failure")
        real_replace(source, target)

    monkeypatch.setattr(migration.os, "replace", fail_second)
    with pytest.raises(OSError, match="injected"):
        migration.atomic_write({first: b"new-first", second: b"new-second"})

    assert first.read_bytes() == b"old-first"
    assert second.read_bytes() == b"old-second"


def test_identity_replacement_is_idempotent() -> None:
    source = {"source_commit": "c" * 40}
    once = migration._replace_identity(_comparison("e" * 64, "r" * 64), _identity(), source)
    twice = migration._replace_identity(once, _identity(), source)
    assert twice == once


def test_classify_accepts_matching_already_migrated_v2() -> None:
    source = {"source_commit": "c" * 40}
    migrated = migration._replace_identity(
        _comparison("e" * 64, "r" * 64), _identity(), source,
    )

    category, reasons = migration.classify(
        _target(Path(".")), migrated, _identity(),
        {"executor_sha256": "e" * 64, "runtime_sha256": "r" * 64},
    )

    assert category == "mechanical"
    assert reasons == ["identity_v2_already_migrated"]


def test_classify_only_refreshes_protocol_fields_for_attested_migration() -> None:
    source = {
        "source_commit": "c" * 40,
        "executor_sha256": "e" * 64,
        "runtime_sha256": "r" * 64,
    }
    migrated = migration._replace_identity(
        _comparison("e" * 64, "r" * 64), _identity("a"), source,
    )
    protocol_update = _identity("a")
    protocol_update["execution_protocol_sha256"] = "b" * 64
    assert migration.classify(
        _target(Path(".")), migrated, protocol_update, source,
    ) == ("mechanical", ["identity_v2_protocol_finalized"])

    business_update = _identity("a")
    business_update["target_skill_sha256"] = "b" * 64
    with pytest.raises(ValueError, match="schema v2 input mismatch"):
        migration.classify(_target(Path(".")), migrated, business_update, source)
