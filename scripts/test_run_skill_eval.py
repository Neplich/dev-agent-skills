from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts import run_skill_eval


def permission_probe(*args, writable: bool, **_kwargs) -> dict:
    dependency_run = None
    if writable and args:
        dependency_run = True if list(args[0].workspace_root.rglob("package-lock.json")) else None
    return {
        "status": "PASS", "workspace_read": True, "workspace_write": writable,
        "home_write": writable, "codex_home_read": False,
        "source_read": False, "sibling_read": False,
        "git_available": True, "git_read": True, "git_write": writable,
        "git_cleanup": True,
        "node_run": True if writable else None,
        "npm_run": True if writable else None,
        "python_run": True if writable else None,
        "dependency_run": dependency_run,
    }


def judge_payload() -> dict:
    return {
        "assertion_results": [
            {"id": "uses_evidence", "status": "PASS", "evidence": "Both outputs reviewed"}
        ],
        "lane_summaries": {
            "without_skill": {
                "run_source": "fresh Luna medium baseline from this paired run",
                "behavior_summary": "Used incident evidence without the skill",
            },
            "with_skill": {
                "run_source": "fresh Luna medium candidate from this paired run",
                "behavior_summary": "Used incident evidence with the skill",
            },
        },
        "behavior_result": "PASS", "coverage_result": "FULL", "overall_result": "PASS",
        "uncovered_reasons": [], "blockers": [], "failures": [], "next_steps": [],
    }


def write_eval(tmp_path: Path) -> Path:
    root = tmp_path / "repo"
    skill = root / "agents/qa/skills/bug-analyzer"
    workspace = root / "agents/qa/test/bug-analyzer/evals/workspace/eval-001-real-user"
    skill.mkdir(parents=True)
    workspace.mkdir(parents=True)
    (skill / "SKILL.md").write_text("---\nname: bug-analyzer\n---\n", encoding="utf-8")
    (workspace / "incident.md").write_text("checkout returns 500", encoding="utf-8")
    (workspace / "comparison.md").write_text("Overall result: BLOCKED", encoding="utf-8")
    (workspace / "eval_metadata.json").write_text(
        json.dumps(
            {
                "eval_id": "eval-001-real-user",
                "skill_dependencies": [],
                "runtime_isolation": {
                    "processes": "not_used",
                    "ports": "not_used",
                    "database": "not_used",
                    "browser": "not_used",
                    "login_state": "not_used",
                    "downloads": "not_used",
                },
            }
        ),
        encoding="utf-8",
    )
    evals = root / "agents/qa/test/bug-analyzer/evals/evals.json"
    evals.write_text(
        json.dumps(
            {
                "schema_version": "1.0",
                "agent": "qa",
                "skill_name": "bug-analyzer",
                "evals": [
                    {
                        "id": "eval-001-real-user",
                        "name": "real-user",
                        "description": "Analyze a customer incident",
                        "scenario": {
                            "persona": "support lead",
                            "situation": "checkout incident",
                            "trigger": "customer reports",
                            "goal": "find likely cause",
                            "materials": ["incident.md"],
                            "constraints": ["read only"],
                            "success_criteria": ["evidence-backed assessment"],
                        },
                        "prompt": "结账接口刚开始返回 500，请根据 incident.md 判断可能原因。",
                        "workspace": "workspace/eval-001-real-user",
                        "expected_output": "An evidence-backed assessment",
                        "assertions": [
                            {
                                "id": "uses_evidence",
                                "description": "Uses incident evidence",
                                "text": "The assessment cites the observed 500 response",
                            }
                        ],
                    }
                ],
            }
        ),
        encoding="utf-8",
    )
    return root


def write_inventory(repository: Path) -> Path:
    path = repository / (
        "docs/engineer/repository-governance/eval-scenario-isolation/migration-inventory.json"
    )
    path.parent.mkdir(parents=True)
    path.write_text(
        json.dumps(
            {
                "counts": {"migration_status": {"pending": 1, "complete": 0}},
                "old_evals": [{
                    "agent": "qa", "skill": "bug-analyzer",
                    "new_eval_id": "eval-001-real-user", "migration_status": "pending",
                    "disposition": "retained",
                }],
            }
        ),
        encoding="utf-8",
    )
    return path


def git_evidence_context(tmp_path: Path):
    root = tmp_path / "candidate"
    root.mkdir()
    subprocess.run(["git", "init", "-q", "-b", "main"], cwd=root, check=True)
    (root / "host.txt").write_text("host fact\n", encoding="utf-8")
    subprocess.run(["git", "add", "."], cwd=root, check=True)
    subprocess.run([
        "git", "-c", "user.name=Host Maintainer", "-c", "user.email=host@example.invalid",
        "commit", "-q", "-m", "host baseline",
    ], cwd=root, check=True)
    return SimpleNamespace(
        git_root=root, workspace_root=root,
        dependency_evidence={"status": "PASS", "sites": []},
    )


def candidate_commit(root: Path, message: str) -> str:
    subprocess.run(["git", "add", "-A"], cwd=root, check=True)
    subprocess.run([
        "git", "-c", "user.name=Candidate", "-c", "user.email=candidate@example.invalid",
        "commit", "-q", "-m", message,
    ], cwd=root, check=True)
    return subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=root, check=True, capture_output=True, text=True,
    ).stdout.strip()


def test_git_evidence_preserves_clean_committed_delivery_bytes(tmp_path: Path) -> None:
    context = git_evidence_context(tmp_path)
    before = run_skill_eval._capture_git_baseline(context)
    unique = "unique-clean-commit-delivery-content"
    (context.git_root / "delivered.txt").write_text(unique, encoding="utf-8")
    commit = candidate_commit(context.git_root, "deliver result")

    evidence = run_skill_eval._git_evidence(context, before)

    assert evidence["git_status"] == ""
    assert evidence["git_evidence"]["head"]["changed"] is True
    assert commit in evidence["git_evidence"]["new_commits"]
    assert any(
        item["path"] == "delivered.txt" and item["content"] == unique
        and item["kind"] == "git_blob"
        for item in evidence["delivery_snapshot"]
    )


def test_git_evidence_records_ref_moves_and_result_diffs(tmp_path: Path) -> None:
    context = git_evidence_context(tmp_path)
    before = run_skill_eval._capture_git_baseline(context)
    (context.git_root / "ref-delivery.txt").write_text("ref move bytes", encoding="utf-8")
    commit = candidate_commit(context.git_root, "move ref")
    subprocess.run(["git", "branch", "candidate-result", commit], cwd=context.git_root, check=True)

    evidence = run_skill_eval._git_evidence(context, before)["git_evidence"]

    assert evidence["ref_delta"]["refs/heads/candidate-result"]["after"]["commit"] == commit
    assert any(
        result["commit"] == commit and "ref-delivery.txt" in result["name_status"]
        for result in evidence["result_diffs"]
    )


def test_git_evidence_finds_commit_then_reset_from_reflog_and_objects(tmp_path: Path) -> None:
    context = git_evidence_context(tmp_path)
    initial = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=context.git_root, check=True,
        capture_output=True, text=True,
    ).stdout.strip()
    before = run_skill_eval._capture_git_baseline(context)
    unique = "unique-reset-delivery-content"
    (context.git_root / "reset-delivery.txt").write_text(unique, encoding="utf-8")
    hidden_commit = candidate_commit(context.git_root, "temporary delivery")
    subprocess.run(["git", "reset", "--hard", initial], cwd=context.git_root, check=True,
                   capture_output=True)

    result = run_skill_eval._git_evidence(context, before)
    evidence = result["git_evidence"]

    assert result["git_status"] == ""
    assert evidence["head"]["changed"] is False
    assert hidden_commit in evidence["new_commits"]
    assert any(entry["oid"] == hidden_commit for entry in evidence["reflog_delta"])
    assert any(
        item["path"] == "reset-delivery.txt" and item["content"] == unique
        for item in result["delivery_snapshot"]
    )
    cleanup = evidence["temporary_worktree_cleanup"]
    assert cleanup["used"] == "unknown"
    assert cleanup["residual_delta"] == []
    assert cleanup["cleaned"] is True


def test_git_evidence_does_not_attribute_preexisting_dirty_state_to_candidate(
    tmp_path: Path,
) -> None:
    context = git_evidence_context(tmp_path)
    (context.git_root / "host.txt").write_text("preexisting unstaged\n", encoding="utf-8")
    (context.git_root / "staged.txt").write_text("preexisting staged\n", encoding="utf-8")
    (context.git_root / "untracked.txt").write_text("preexisting untracked\n", encoding="utf-8")
    subprocess.run(["git", "add", "staged.txt"], cwd=context.git_root, check=True)
    before = run_skill_eval._capture_git_baseline(context)

    result = run_skill_eval._git_evidence(context, before)

    assert result["delivery_snapshot"] == []
    evidence = result["git_evidence"]
    assert evidence["result_diffs"] == []
    assert "host.txt" in evidence["initial_state"]["worktree_diff"]
    assert "staged.txt" in evidence["initial_state"]["index_diff"]
    assert any(
        item["path"] == "untracked.txt" and item["content"] == "preexisting untracked\n"
        for item in evidence["initial_state"]["untracked"]
    )


def test_candidate_command_uses_permission_profile_config_and_fixed_model(
    tmp_path: Path,
) -> None:
    command = run_skill_eval.candidate_command(
        tmp_path,
        tmp_path / "result.md",
    )

    assert command[:4] == ["codex", "--ask-for-approval", "never", "--strict-config"]
    assert "--sandbox" not in command
    assert "--ignore-user-config" not in command
    assert command[command.index("--model") + 1] == "gpt-5.6-luna"
    assert 'model_reasoning_effort="medium"' in command
    assert "--output-schema" not in command


def test_judge_command_uses_profile_and_schema_constraint(tmp_path: Path) -> None:
    command = run_skill_eval.judge_command(
        tmp_path,
        tmp_path / "verdict.json",
    )

    assert command[:4] == ["codex", "--ask-for-approval", "never", "--strict-config"]
    assert "--sandbox" not in command
    assert "--ignore-user-config" not in command
    assert command[command.index("--output-schema") + 1].endswith(
        "scripts/eval_judge_result.schema.json"
    )


def test_overall_is_recomputed_from_behavior_and_coverage() -> None:
    assert run_skill_eval.recompute_overall("FAIL", "FULL") == "FAIL"
    assert run_skill_eval.recompute_overall("PASS", "FULL") == "PASS"
    assert (
        run_skill_eval.recompute_overall("PASS", "PARTIAL")
        == "PASS (partial coverage)"
    )


def test_validate_judge_result_rejects_model_supplied_wrong_overall() -> None:
    payload = judge_payload()
    payload["overall_result"] = "FAIL"

    normalized = run_skill_eval.validate_judge_result(payload, {"uses_evidence"})

    assert normalized["overall_result"] == "PASS"


def test_judge_prompt_applies_assertion_verdicts_only_to_with_skill_lane() -> None:
    prompt = run_skill_eval._judge_prompt().lower()

    assert "assertion verdicts evaluate only the with_skill lane" in prompt
    assert "without_skill is comparison context" in prompt
    assert "must not make an assertion fail" in prompt


def test_blocked_preflight_never_calls_candidate_or_judge(tmp_path: Path) -> None:
    repository = write_eval(tmp_path)
    calls: list[str] = []

    def forbidden_runner(*_args, **_kwargs):
        calls.append("called")
        raise AssertionError("model command must not run")

    result = run_skill_eval.run_selected_eval(
        repository_root=repository,
        agent="qa",
        skill="bug-analyzer",
        eval_id="eval-001-real-user",
        runtime_root=tmp_path / "runs",
        model_available=False,
        command_runner=forbidden_runner,
        permission_probe=permission_probe,
    )

    assert calls == []
    assert result["overall_result"] == "BLOCKED"
    assert result["candidate_runs"] == []
    assert result["judge_run"] is None
    assert (repository / (
        "agents/qa/test/bug-analyzer/evals/workspace/eval-001-real-user/comparison.md"
    )).read_text(encoding="utf-8") == "Overall result: BLOCKED"


def test_failed_candidate_keeps_comparison_stale_and_inventory_pending(tmp_path: Path) -> None:
    repository = write_eval(tmp_path)
    inventory = write_inventory(repository)

    result = run_skill_eval.run_selected_eval(
        repository_root=repository, agent="qa", skill="bug-analyzer",
        eval_id="eval-001-real-user", runtime_root=tmp_path / "runs",
        model_available=True,
        command_runner=lambda *_args, **_kwargs: {"returncode": 1, "timed_out": False},
        permission_probe=permission_probe,
    )

    assert result["overall_result"] == "BLOCKED"
    comparison = repository / (
        "agents/qa/test/bug-analyzer/evals/workspace/eval-001-real-user/comparison.md"
    )
    assert comparison.read_text(encoding="utf-8") == "Overall result: BLOCKED"
    assert json.loads(inventory.read_text())["old_evals"][0]["migration_status"] == "pending"


def test_declared_outputs_use_lane_delta_with_nested_or_and_baseline_is_report_only(
    tmp_path: Path,
) -> None:
    repository = write_eval(tmp_path)
    definition = run_skill_eval.load_eval_definition(
        repository, "qa", "bug-analyzer", "eval-001-real-user",
    )
    metadata = json.loads(definition.metadata_path.read_text()) if hasattr(definition, "metadata_path") else definition.metadata
    metadata["with_skill_outputs"] = [["missing.md", "fresh.md"]]
    metadata["without_skill_outputs"] = ["missing-baseline.md"]
    (definition.workspace_root / "eval_metadata.json").write_text(json.dumps(metadata), encoding="utf-8")
    (definition.workspace_root / "fresh.md").write_text("committed fixture must not satisfy gate", encoding="utf-8")

    def fake_runner(command, *, prompt, env, timeout_seconds):
        output = Path(command[command.index("--output-last-message") + 1])
        output.parent.mkdir(parents=True, exist_ok=True)
        if "--output-schema" in command:
            output.write_text(json.dumps(judge_payload()), encoding="utf-8")
        else:
            output.write_text("candidate response", encoding="utf-8")
        return {"returncode": 0, "timed_out": False}

    result = run_skill_eval.run_selected_eval(
        repository_root=repository, agent="qa", skill="bug-analyzer",
        eval_id="eval-001-real-user", runtime_root=tmp_path / "runs",
        model_available=True, command_runner=fake_runner, permission_probe=permission_probe,
    )

    assert result["overall_result"] == "BLOCKED"
    assert result["candidate_runs"][0]["declared_outputs"][0]["ok"] is False
    assert result["candidate_runs"][1]["declared_outputs"][0]["ok"] is False


def test_declared_output_normalizes_matching_lane_prefix_and_rejects_wrong_lane() -> None:
    snapshot = [{"path": "outputs/report.md", "kind": "file", "content": "fresh"}]

    checks = run_skill_eval._output_checks(
        snapshot, [["with_skill/missing.md", "with_skill/outputs/report.md"]], "with_skill",
    )

    assert checks == [{
        "paths": ["with_skill/missing.md", "with_skill/outputs/report.md"],
        "semantics": "OR", "ok": True,
    }]
    with pytest.raises(ValueError, match="wrong lane prefix"):
        run_skill_eval._output_checks(
            snapshot, ["without_skill/outputs/report.md"], "with_skill",
        )

    assert run_skill_eval._output_checks([{
        "path": "ghost.md", "kind": "git_blob", "content": "reset away",
        "final_reachable": False,
    }], ["ghost.md"], "with_skill")[0]["ok"] is False
    assert run_skill_eval._output_checks([{
        "path": "committed.md", "kind": "git_blob", "content": "final commit",
        "final_reachable": True,
    }], ["committed.md"], "with_skill")[0]["ok"] is True


def test_compatibility_skip_generate_reports_existing_isolated_status(
    tmp_path: Path, capsys: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch,
) -> None:
    repository = write_eval(tmp_path)
    definition = run_skill_eval.load_eval_definition(
        repository, "qa", "bug-analyzer", "eval-001-real-user",
    )
    runtime = repository / "tmp/eval-runs/qa/bug-analyzer/eval-001-real-user"
    runtime.mkdir(parents=True)
    (runtime / "run_status.json").write_text(
        json.dumps({
            "agent": "qa", "skill": "bug-analyzer", "eval_id": "eval-001-real-user",
            "overall_result": "PASS", "runtime_evidence": "isolated",
            "candidate_runs": [
                {"mode": "without_skill", "declared_outputs": [{"ok": False}]},
                {"mode": "with_skill", "declared_outputs": [], "delivery_snapshot": []},
            ],
        }),
        encoding="utf-8",
    )
    monkeypatch.setattr(run_skill_eval, "definition_from_metadata", lambda _path: definition)

    exit_code = run_skill_eval.compatibility_main(
        "qa", [str(definition.workspace_root / "eval_metadata.json"), "--skip-generate"],
    )

    assert exit_code == 0
    assert '"runtime_evidence": "isolated"' in capsys.readouterr().out


def test_compatibility_skip_generate_rejects_forged_pass_status(
    tmp_path: Path, capsys: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch,
) -> None:
    repository = write_eval(tmp_path)
    definition = run_skill_eval.load_eval_definition(
        repository, "qa", "bug-analyzer", "eval-001-real-user",
    )
    runtime = repository / "tmp/eval-runs/qa/bug-analyzer/eval-001-real-user"
    runtime.mkdir(parents=True)
    (runtime / "run_status.json").write_text(json.dumps({
        "agent": "qa", "skill": "other", "eval_id": "eval-001-real-user",
        "overall_result": "PASS",
        "candidate_runs": [{"mode": "with_skill", "declared_outputs": [{"ok": True}]}],
    }))
    monkeypatch.setattr(run_skill_eval, "definition_from_metadata", lambda _path: definition)

    exit_code = run_skill_eval.compatibility_main(
        "qa", [str(definition.workspace_root / "eval_metadata.json"), "--skip-generate"],
    )

    assert exit_code == 1
    assert "does not match metadata identity" in capsys.readouterr().err


def test_paired_run_uses_identical_prompt_in_without_then_with_order_and_fresh_judge(
    tmp_path: Path,
) -> None:
    repository = write_eval(tmp_path)
    inventory = write_inventory(repository)
    calls: list[dict] = []
    candidate_roots: list[Path] = []

    def fake_runner(command, *, prompt, env, timeout_seconds):
        is_judge = "--output-schema" in command
        role = "judge" if is_judge else "candidate"
        workspace = Path(command[command.index("-C") + 1])
        output = Path(command[command.index("--output-last-message") + 1])
        output.parent.mkdir(parents=True, exist_ok=True)
        calls.append({"command": command, "prompt": prompt, "role": role})
        if is_judge:
            assert all(not root.exists() for root in candidate_roots)
            package = (workspace / "judge-package.json").read_text(encoding="utf-8")
            assert "unique-untracked-delivery-content" in package
            payload = judge_payload()
            payload["lane_summaries"]["without_skill"]["run_source"] = "FORGED BY JUDGE"
            payload["lane_summaries"]["with_skill"]["run_source"] = "FORGED BY JUDGE"
            output.write_text(json.dumps(payload), encoding="utf-8")
        else:
            if candidate_roots:
                assert not candidate_roots[-1].exists()
            candidate_roots.append(workspace.parent)
            (workspace / "new-delivery.txt").write_text(
                "unique-untracked-delivery-content", encoding="utf-8",
            )
            output.write_text("candidate response", encoding="utf-8")
        return {"returncode": 0, "timed_out": False, "stderr_tail": ""}

    result = run_skill_eval.run_selected_eval(
        repository_root=repository,
        agent="qa",
        skill="bug-analyzer",
        eval_id="eval-001-real-user",
        runtime_root=tmp_path / "runs",
        model_available=True,
        command_runner=fake_runner,
        permission_probe=permission_probe,
    )

    assert [call["role"] for call in calls] == ["candidate", "candidate", "judge"]
    assert calls[0]["prompt"] == calls[1]["prompt"]
    assert "without_skill" not in calls[0]["prompt"]
    assert "with_skill" not in calls[1]["prompt"]
    assert calls[2]["prompt"] != calls[0]["prompt"]
    assert result["candidate_runs"][0]["mode"] == "without_skill"
    assert result["candidate_runs"][1]["mode"] == "with_skill"
    assert result["judge_run"] is not None
    assert result["overall_result"] == "PASS"
    assert "FORGED BY JUDGE" not in json.dumps(result)
    assert "model=gpt-5.6-luna" in result["lane_summaries"]["with_skill"]["run_source"]
    assert "output_sha256=" in result["lane_summaries"]["with_skill"]["run_source"]
    comparison = (
        repository
        / "agents/qa/test/bug-analyzer/evals/workspace/"
        "eval-001-real-user/comparison.md"
    ).read_text(encoding="utf-8")
    assert "Evidence status: **FRESH**" in comparison
    assert "Preflight status: **PASS**" in comparison
    assert "fresh judge" in comparison
    assert "Overall result: PASS" in comparison
    assert "## Historical Context (Superseded)" in comparison
    assert "Overall result: BLOCKED" in comparison
    assert "## Evaluation Target" in comparison
    assert "Fixture version/source:" in comparison
    assert "Repository HEAD:" in comparison
    assert "Repository worktree state:" in comparison
    assert "Target skill tree SHA-256:" in comparison
    assert "Skill overlay SHA-256:" in comparison
    assert "Judge schema SHA-256:" in comparison
    assert "Eval definition SHA-256:" in comparison
    assert "Metadata SHA-256:" in comparison
    assert "Executor SHA-256:" in comparison
    assert "Runtime SHA-256:" in comparison
    assert "## With-Skill Behavior" in comparison
    assert "## Fresh Without-Skill Baseline" in comparison
    assert "## Runtime Artifact Policy" in comparison
    updated_inventory = json.loads(inventory.read_text(encoding="utf-8"))
    assert updated_inventory["old_evals"][0]["migration_status"] == "complete"
    assert updated_inventory["counts"]["migration_status"] == {
        "pending": 0,
        "complete": 1,
    }


def test_source_identity_records_dirty_current_skill_dependency_and_schema_content(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch,
) -> None:
    repository = write_eval(tmp_path)
    dependency = repository / "agents/product_manager/skills/idea-to-spec"
    dependency.mkdir(parents=True)
    (dependency / "SKILL.md").write_text("dependency v1\n", encoding="utf-8")
    metadata_path = repository / (
        "agents/qa/test/bug-analyzer/evals/workspace/eval-001-real-user/eval_metadata.json"
    )
    metadata = json.loads(metadata_path.read_text())
    metadata["skill_dependencies"] = ["agents/product_manager/skills/idea-to-spec"]
    metadata_path.write_text(json.dumps(metadata), encoding="utf-8")
    schema = tmp_path / "judge-schema.json"
    schema.write_text('{"version": 1}\n', encoding="utf-8")
    monkeypatch.setattr(run_skill_eval, "JUDGE_SCHEMA", schema)
    subprocess.run(["git", "init", "-q", "-b", "main"], cwd=repository, check=True)
    subprocess.run(["git", "add", "."], cwd=repository, check=True)
    subprocess.run([
        "git", "-c", "user.name=Test", "-c", "user.email=test@example.com",
        "commit", "-q", "-m", "base",
    ], cwd=repository, check=True)
    definition = run_skill_eval.load_eval_definition(
        repository, "qa", "bug-analyzer", "eval-001-real-user",
    )

    clean = run_skill_eval.source_identity(definition)
    loaded_metadata_hash = clean["metadata_sha256"]
    metadata_path.write_text('{"eval_id":"changed-after-load"}', encoding="utf-8")
    assert run_skill_eval.source_identity(definition)["metadata_sha256"] == loaded_metadata_hash
    metadata_path.write_text(json.dumps(metadata), encoding="utf-8")
    (repository / "agents/qa/skills/bug-analyzer/SKILL.md").write_text(
        "---\nname: bug-analyzer\n---\ncurrent dirty instructions\n", encoding="utf-8",
    )
    dirty = run_skill_eval.source_identity(definition)
    (dependency / "SKILL.md").write_text("dependency v2\n", encoding="utf-8")
    dependency_dirty = run_skill_eval.source_identity(definition)
    schema.write_text('{"version": 2}\n', encoding="utf-8")
    schema_dirty = run_skill_eval.source_identity(definition)
    metadata["runtime_isolation"]["browser"] = {
        "state": "isolated", "evidence": "fresh browser profile",
    }
    metadata_path.write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    metadata_dirty = run_skill_eval.source_identity(
        run_skill_eval.load_eval_definition(
            repository, "qa", "bug-analyzer", "eval-001-real-user",
        )
    )
    evals_path = repository / "agents/qa/test/bug-analyzer/evals/evals.json"
    evals = json.loads(evals_path.read_text())
    evals["evals"][0]["expected_output"] = "A changed current result"
    evals_path.write_text(json.dumps(evals), encoding="utf-8")
    definition_dirty = run_skill_eval.source_identity(
        run_skill_eval.load_eval_definition(
            repository, "qa", "bug-analyzer", "eval-001-real-user",
        )
    )

    assert clean["repository_head"] == dirty["repository_head"]
    assert clean["repository_dirty"] is False
    assert dirty["repository_dirty"] is True
    assert clean["target_skill_sha256"] != dirty["target_skill_sha256"]
    assert dirty["target_skill_sha256"] == dependency_dirty["target_skill_sha256"]
    assert dirty["skill_overlay_sha256"] != dependency_dirty["skill_overlay_sha256"]
    assert dependency_dirty["judge_schema_sha256"] != schema_dirty["judge_schema_sha256"]
    assert schema_dirty["metadata_sha256"] != metadata_dirty["metadata_sha256"]
    assert metadata_dirty["eval_definition_sha256"] != definition_dirty["eval_definition_sha256"]
    assert len(dirty["executor_sha256"]) == len(dirty["runtime_sha256"]) == 64


def test_transient_skill_and_schema_changes_use_locked_inputs(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch,
) -> None:
    repository = write_eval(tmp_path)
    write_inventory(repository)
    skill = repository / "agents/qa/skills/bug-analyzer/SKILL.md"
    original_skill = skill.read_bytes()
    dependency = repository / "agents/product_manager/skills/idea-to-spec"
    dependency.mkdir(parents=True)
    (dependency / "SKILL.md").write_text("dependency original\n", encoding="utf-8")
    original_dependency = (dependency / "SKILL.md").read_bytes()
    metadata_path = repository / (
        "agents/qa/test/bug-analyzer/evals/workspace/eval-001-real-user/eval_metadata.json"
    )
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    metadata["skill_dependencies"] = ["agents/product_manager/skills/idea-to-spec"]
    metadata_path.write_text(json.dumps(metadata), encoding="utf-8")
    schema = tmp_path / "judge-schema.json"
    original_schema = b'{"version":1}\n'
    schema.write_bytes(original_schema)
    monkeypatch.setattr(run_skill_eval, "JUDGE_SCHEMA", schema)
    candidate_count = 0

    def transient_runner(command, *, prompt, env, timeout_seconds):
        nonlocal candidate_count
        output = Path(command[command.index("--output-last-message") + 1])
        output.parent.mkdir(parents=True, exist_ok=True)
        if "--output-schema" in command:
            locked_schema = Path(command[command.index("--output-schema") + 1])
            assert locked_schema != schema
            assert locked_schema.read_bytes() == original_schema
            schema.write_bytes(original_schema)
            output.write_text(json.dumps(judge_payload()), encoding="utf-8")
        else:
            candidate_count += 1
            if candidate_count == 1:
                skill.write_text("transient untrusted instructions\n", encoding="utf-8")
                (dependency / "SKILL.md").write_text(
                    "transient dependency instructions\n", encoding="utf-8",
                )
                schema.write_text('{"version":2}\n', encoding="utf-8")
            else:
                workspace = Path(command[command.index("-C") + 1])
                assert (workspace / ".agents/skills/bug-analyzer/SKILL.md").read_bytes() \
                    == original_skill
                assert (workspace / ".agents/skills/idea-to-spec/SKILL.md").read_bytes() \
                    == original_dependency
                skill.write_bytes(original_skill)
                (dependency / "SKILL.md").write_bytes(original_dependency)
            output.write_text("candidate response", encoding="utf-8")
        return {"returncode": 0, "timed_out": False}

    result = run_skill_eval.run_selected_eval(
        repository_root=repository, agent="qa", skill="bug-analyzer",
        eval_id="eval-001-real-user", runtime_root=tmp_path / "runs",
        model_available=True, command_runner=transient_runner,
        permission_probe=permission_probe,
    )

    assert result["overall_result"] == "PASS"
    assert "Evidence status: **FRESH**" in (
        repository / "agents/qa/test/bug-analyzer/evals/workspace/"
        "eval-001-real-user/comparison.md"
    ).read_text(encoding="utf-8")


@pytest.mark.parametrize("drift", ["judge_schema", "fixture"])
def test_source_drift_blocks_durable_persist(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, drift: str,
) -> None:
    repository = write_eval(tmp_path)
    inventory = write_inventory(repository)
    comparison = repository / (
        "agents/qa/test/bug-analyzer/evals/workspace/"
        "eval-001-real-user/comparison.md"
    )
    original_comparison = comparison.read_bytes()
    original_inventory = inventory.read_bytes()
    schema = tmp_path / "judge-schema.json"
    schema.write_text('{"version":1}\n', encoding="utf-8")
    monkeypatch.setattr(run_skill_eval, "JUDGE_SCHEMA", schema)
    candidate_count = 0

    def drifting_runner(command, *, prompt, env, timeout_seconds):
        nonlocal candidate_count
        output = Path(command[command.index("--output-last-message") + 1])
        output.parent.mkdir(parents=True, exist_ok=True)
        if "--output-schema" in command:
            output.write_text(json.dumps(judge_payload()), encoding="utf-8")
        else:
            output.write_text("candidate response", encoding="utf-8")
            candidate_count += 1
            if candidate_count == 1:
                if drift == "judge_schema":
                    schema.write_text('{"version":2}\n', encoding="utf-8")
                else:
                    (comparison.parent / "incident.md").write_text(
                        "checkout now returns 503", encoding="utf-8",
                    )
        return {"returncode": 0, "timed_out": False}

    result = run_skill_eval.run_selected_eval(
        repository_root=repository, agent="qa", skill="bug-analyzer",
        eval_id="eval-001-real-user", runtime_root=tmp_path / "runs",
        model_available=True, command_runner=drifting_runner,
        permission_probe=permission_probe,
    )

    assert result["overall_result"] == "BLOCKED"
    assert result["blockers"] == ["eval source inputs changed during the isolated run"]
    assert comparison.read_bytes() == original_comparison
    assert inventory.read_bytes() == original_inventory


def test_snapshot_failure_returns_blocked_with_recorded_preflight(tmp_path: Path) -> None:
    repository = write_eval(tmp_path)

    def oversized_delivery(command, *, prompt, env, timeout_seconds):
        workspace = Path(command[command.index("-C") + 1])
        output = Path(command[command.index("--output-last-message") + 1])
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text("candidate response", encoding="utf-8")
        (workspace / "oversized.bin").write_bytes(b"x" * 2_000_001)
        return {"returncode": 0, "timed_out": False}

    result = run_skill_eval.run_selected_eval(
        repository_root=repository, agent="qa", skill="bug-analyzer",
        eval_id="eval-001-real-user", runtime_root=tmp_path / "runs",
        model_available=True, command_runner=oversized_delivery,
        permission_probe=permission_probe,
    )

    assert result["overall_result"] == "BLOCKED"
    assert result["preflight"]["checks"]["without_skill.os_boundary"] is True
    assert "exceeds 2 MB" in result["blockers"][0]


@pytest.mark.parametrize("failure_at", [1, 2])
def test_durable_update_rolls_back_both_files_when_replace_fails(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, failure_at: int,
) -> None:
    repository = write_eval(tmp_path)
    inventory = write_inventory(repository)
    definition = run_skill_eval.load_eval_definition(
        repository, "qa", "bug-analyzer", "eval-001-real-user",
    )
    comparison = definition.workspace_root / "comparison.md"
    original_comparison = comparison.read_bytes()
    original_inventory = inventory.read_bytes()
    result = {
        "preflight": {"fixture_hash": "f" * 64, "prompt_hash": "p" * 64},
        "source_identity": run_skill_eval.source_identity(definition),
        **judge_payload(),
    }
    real_replace = run_skill_eval.os.replace
    calls = 0

    def fail_second(source, destination):
        nonlocal calls
        calls += 1
        if calls == failure_at:
            raise OSError("injected replace failure")
        return real_replace(source, destination)

    monkeypatch.setattr(run_skill_eval.os, "replace", fail_second)
    with pytest.raises(OSError, match="injected"):
        run_skill_eval.persist_durable_result(definition, result)

    assert comparison.read_bytes() == original_comparison
    assert inventory.read_bytes() == original_inventory


def test_transaction_cleans_staged_files_when_staging_fails(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch,
) -> None:
    first, second = tmp_path / "first", tmp_path / "second"
    first.write_bytes(b"old-first")
    second.write_bytes(b"old-second")
    real_stage = run_skill_eval._stage_file
    created: list[Path] = []

    def fail_after_first(path: Path, content: bytes) -> Path:
        if created:
            raise OSError("injected staging failure")
        temporary = real_stage(path, content)
        created.append(temporary)
        return temporary

    monkeypatch.setattr(run_skill_eval, "_stage_file", fail_after_first)
    with pytest.raises(OSError, match="staging"):
        run_skill_eval._transactional_replace({first: b"new-first", second: b"new-second"})

    assert all(not path.exists() for path in created)
    assert first.read_bytes() == b"old-first"
    assert second.read_bytes() == b"old-second"
