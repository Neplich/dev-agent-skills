from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts import eval_identity
from scripts import run_skill_eval


def test_identity_v2_has_exact_freshness_fields_and_complete_source_lock(tmp_path: Path) -> None:
    repository = run_skill_eval_test_repository(tmp_path)
    definition = run_skill_eval.load_eval_definition(
        repository, "qa", "bug-analyzer", "eval-001-real-user",
    )

    identity = run_skill_eval.source_identity(definition)

    assert identity["identity_schema"] == 2
    assert set(identity["freshness"]) == set(eval_identity.FRESHNESS_FIELDS)
    assert set(identity["source_manifest"]) == set(eval_identity.SOURCE_LOCK_FILES)
    assert identity["source_lock_sha256"] == eval_identity.source_lock_sha256(
        identity["source_manifest"]
    )


def test_current_identity_v2_does_not_invoke_git(
    tmp_path: Path, monkeypatch,
) -> None:
    repository = run_skill_eval_test_repository(tmp_path)
    definition = run_skill_eval.load_eval_definition(
        repository, "qa", "bug-analyzer", "eval-001-real-user",
    )
    monkeypatch.setattr(
        eval_identity.subprocess, "run",
        lambda *_args, **_kwargs: (_ for _ in ()).throw(AssertionError("git must not run")),
    )

    identity = eval_identity.current_identity_v2(definition)

    assert identity["identity_schema"] == 2
    assert set(identity["freshness"]) == set(eval_identity.FRESHNESS_FIELDS)


def test_protocol_hashes_follow_explicit_module_boundaries(tmp_path: Path) -> None:
    root = tmp_path / "scripts"
    root.mkdir()
    files = {
        "run_skill_eval.py": b"cli\n",
        "eval_identity.py": b"identity\n",
        "eval_execution.py": b"execution\n",
        "eval_judging.py": b"judging\n",
        "eval_runtime.py": b"runtime\n",
        "eval_persistence.py": b"persistence\n",
        "eval_judge_result.schema.json": b"schema\n",
    }
    for name, content in files.items():
        (root / name).write_bytes(content)

    initial = eval_identity.protocol_hashes(root)
    (root / "eval_persistence.py").write_bytes(b"changed persistence\n")
    persistence = eval_identity.protocol_hashes(root)
    (root / "eval_execution.py").write_bytes(b"changed execution\n")
    execution = eval_identity.protocol_hashes(root)
    (root / "eval_runtime.py").write_bytes(b"changed runtime\n")
    runtime = eval_identity.protocol_hashes(root)
    (root / "eval_judge_result.schema.json").write_bytes(b"changed schema\n")
    schema = eval_identity.protocol_hashes(root)

    assert persistence == initial
    assert execution["execution_protocol_sha256"] != initial["execution_protocol_sha256"]
    assert execution["runtime_protocol_sha256"] == initial["runtime_protocol_sha256"]
    assert runtime["runtime_protocol_sha256"] != execution["runtime_protocol_sha256"]
    assert schema["judge_schema_sha256"] != runtime["judge_schema_sha256"]


def test_source_lock_detects_persistence_and_identity_drift(tmp_path: Path) -> None:
    root = tmp_path / "scripts"
    root.mkdir()
    for name in eval_identity.SOURCE_LOCK_FILES:
        (root / name).write_text(name + "\n", encoding="utf-8")
    before = eval_identity.source_manifest(root)

    (root / "eval_persistence.py").write_text("persistence changed\n", encoding="utf-8")
    after_persistence = eval_identity.source_manifest(root)
    (root / "eval_identity.py").write_text("identity changed\n", encoding="utf-8")
    after_identity = eval_identity.source_manifest(root)

    assert eval_identity.source_lock_sha256(before) != eval_identity.source_lock_sha256(
        after_persistence
    )
    assert eval_identity.source_lock_sha256(after_persistence) != eval_identity.source_lock_sha256(
        after_identity
    )


def run_skill_eval_test_repository(tmp_path: Path) -> Path:
    root = tmp_path / "repo"
    skill = root / "agents/qa/skills/bug-analyzer"
    workspace = root / "agents/qa/test/bug-analyzer/evals/workspace/eval-001-real-user"
    skill.mkdir(parents=True)
    workspace.mkdir(parents=True)
    (skill / "SKILL.md").write_text("---\nname: bug-analyzer\n---\n", encoding="utf-8")
    (workspace / "incident.md").write_text("checkout returns 500", encoding="utf-8")
    (workspace / "comparison.md").write_text("Overall result: BLOCKED", encoding="utf-8")
    (workspace / "eval_metadata.json").write_text(json.dumps({
        "eval_id": "eval-001-real-user",
        "skill_dependencies": [],
        "runtime_isolation": {name: "not_used" for name in (
            "processes", "ports", "database", "browser", "login_state", "downloads",
        )},
    }), encoding="utf-8")
    (workspace.parents[1] / "evals.json").write_text(json.dumps({
        "schema_version": "1.0", "agent": "qa", "skill_name": "bug-analyzer",
        "evals": [{
            "id": "eval-001-real-user", "name": "real-user", "description": "incident",
            "scenario": {"persona": "support", "situation": "incident", "trigger": "500",
                         "goal": "diagnose", "materials": ["incident.md"],
                         "constraints": ["read only"], "success_criteria": ["assessment"]},
            "prompt": "请分析 incident.md。", "workspace": "workspace/eval-001-real-user",
            "expected_output": "assessment",
            "assertions": [{"id": "uses_evidence", "description": "evidence", "text": "uses 500"}],
        }],
    }), encoding="utf-8")
    return root
