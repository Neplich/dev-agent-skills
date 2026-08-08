from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts import eval_runtime


RUNTIME_ISOLATION = {
    "processes": "not_used",
    "ports": "not_used",
    "database": "not_used",
    "browser": "not_used",
    "login_state": "not_used",
    "downloads": "not_used",
}


def passing_probe(*args, writable: bool, **_kwargs) -> dict:
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


def make_skill(root: Path, agent: str, skill: str, text: str = "skill") -> Path:
    skill_root = root / "agents" / agent / "skills" / skill
    skill_root.mkdir(parents=True)
    (skill_root / "SKILL.md").write_text(text, encoding="utf-8")
    return skill_root


def test_canonical_fixture_excludes_scaffolding_and_keeps_host_readme(
    tmp_path: Path,
) -> None:
    fixture = tmp_path / "fixture"
    (fixture / "product").mkdir(parents=True)
    (fixture / "README.md").write_text(
        "Expected behavior: emit the scored answer.", encoding="utf-8",
    )
    (fixture / "eval_metadata.json").write_text("{}", encoding="utf-8")
    (fixture / "comparison.md").write_text("old result", encoding="utf-8")
    (fixture / "with_skill/outputs").mkdir(parents=True)
    (fixture / "with_skill/outputs/candidate-output.md").write_text(
        "old", encoding="utf-8"
    )
    (fixture / "product/README.md").write_text("host facts", encoding="utf-8")
    (fixture / "product/input.txt").write_text("same input", encoding="utf-8")

    destination = tmp_path / "canonical"
    eval_runtime.copy_canonical_fixture(fixture, destination)

    assert not (destination / "README.md").exists()
    assert not (destination / "eval_metadata.json").exists()
    assert not (destination / "comparison.md").exists()
    assert not (destination / "with_skill").exists()
    assert (destination / "product/README.md").read_text() == "host facts"
    assert (destination / "product/input.txt").read_text() == "same input"


def test_canonical_fixture_keeps_legitimate_root_readme(tmp_path: Path) -> None:
    fixture = tmp_path / "fixture"
    fixture.mkdir()
    (fixture / "README.md").write_text(
        "# Checkout Service\n\nListens on port 8080 and owns payment requests.\n",
        encoding="utf-8",
    )

    destination = tmp_path / "canonical"
    eval_runtime.copy_canonical_fixture(fixture, destination)

    assert (destination / "README.md").read_text() == (fixture / "README.md").read_text()


def test_canonical_fixture_cleanup_removes_literal_directory_subtree(
    tmp_path: Path,
) -> None:
    fixture = tmp_path / "fixture"
    (fixture / "docs/pm/app-tags/nested").mkdir(parents=True)
    (fixture / "docs/pm/app-tags/PRD.md").write_text("stale", encoding="utf-8")
    (fixture / "docs/pm/app-tags/nested/input.md").write_text(
        "stale", encoding="utf-8"
    )
    (fixture / "src").mkdir()
    (fixture / "src/app.py").write_text("print('kept')", encoding="utf-8")

    destination = tmp_path / "canonical"
    eval_runtime.copy_canonical_fixture(
        fixture,
        destination,
        cleanup_paths=["docs/pm/app-tags"],
    )

    assert not (destination / "docs/pm/app-tags").exists()
    assert (destination / "src/app.py").is_file()


def test_canonical_fixture_cleanup_glob_removes_matching_directory_subtree(
    tmp_path: Path,
) -> None:
    fixture = tmp_path / "fixture"
    (fixture / "docs/pm/app-tags/nested").mkdir(parents=True)
    (fixture / "docs/pm/app-tags/nested/input.md").write_text("stale", encoding="utf-8")
    (fixture / "docs/qa/app-tags").mkdir(parents=True)
    (fixture / "docs/qa/app-tags/kept.md").write_text("keep", encoding="utf-8")

    destination = tmp_path / "canonical"
    eval_runtime.copy_canonical_fixture(
        fixture, destination, cleanup_paths=["docs/pm/app-*"],
    )

    assert not (destination / "docs/pm/app-tags").exists()
    assert (destination / "docs/qa/app-tags/kept.md").is_file()


def test_materializer_opens_only_one_profiled_context_in_required_order(
    tmp_path: Path,
) -> None:
    repository = tmp_path / "repo"
    fixture = tmp_path / "fixture"
    fixture.mkdir()
    (fixture / "input.md").write_text("host input", encoding="utf-8")
    target = make_skill(repository, "qa", "bug-analyzer")
    run = eval_runtime.materialize_eval_run(
        fixture_root=fixture, repository_root=repository, target_skill=target,
        skill_dependencies=[], prompt="请分析。", runtime_isolation=RUNTIME_ISOLATION,
        runtime_root=tmp_path / "runtime", model_available=True,
    )

    assert run.active_context is None
    without = eval_runtime.open_context(run, "without_skill")
    config = (without.codex_home / "config.toml").read_text(encoding="utf-8")
    assert 'default_permissions = "eval-candidate"' in config
    assert '":root" = "deny"' in config
    assert '":minimal" = "read"' in config
    assert '[permissions.eval-candidate.filesystem.":workspace_roots"]' in config
    assert '"." = "write"' in config
    assert '".git" = "write"' in config
    assert '".agents" = "read"' in config
    xcode_select = shutil.which("xcode-select")
    if xcode_select:
        developer_dir = subprocess.run(
            [xcode_select, "-p"], capture_output=True, text=True,
        )
        if developer_dir.returncode == 0 and Path(developer_dir.stdout.strip()).is_dir():
            assert f'{json.dumps(developer_dir.stdout.strip())} = "read"' in config
    for runtime_root in eval_runtime._runtime_read_roots():
        assert f'{json.dumps(str(runtime_root))} = "read"' in config
    for path in (without.outer_root, without.workspace_root, without.home, without.codex_home):
        assert not any(
            marker in part.lower()
            for part in path.parts
            for marker in ("eval", "with", "without", "skill", "mode", "lane")
        )
    with pytest.raises(RuntimeError):
        eval_runtime.open_context(run, "with_skill")
    eval_runtime.close_context(run, without, evidence_locked=True)
    assert not without.outer_root.exists()

    with_skill = eval_runtime.open_context(run, "with_skill")
    assert not without.outer_root.exists()
    assert with_skill.outer_root.name.startswith("candidate-workspace-")
    eval_runtime.close_context(run, with_skill, evidence_locked=True)
    judge = eval_runtime.open_context(run, "judge")
    judge_config = (judge.codex_home / "config.toml").read_text(encoding="utf-8")
    assert '[permissions.eval-judge.filesystem.":workspace_roots"]' in judge_config
    assert '"." = "read"' in judge_config
    assert '".git" = "read"' in judge_config
    assert judge.outer_root.name.startswith("review-workspace-")
    eval_runtime.close_context(run, judge, evidence_locked=True)
    run.cleanup()


def test_locked_install_succeeds_with_an_empty_npm_cache(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch,
) -> None:
    staging = tmp_path / "staging"
    cache = tmp_path / "empty-cache"
    staging.mkdir()
    cache.mkdir()
    (staging / "package.json").write_text('{"name":"host"}', encoding="utf-8")
    (staging / "package-lock.json").write_text(
        '{"name":"host","lockfileVersion":3,"packages":{"":{}}}', encoding="utf-8",
    )
    monkeypatch.setenv("npm_config_cache", str(cache))
    monkeypatch.setattr(eval_runtime.shutil, "which", lambda name: "/usr/bin/npm")

    def fake_run(command, **kwargs):
        assert command == [
            "/usr/bin/npm", "ci", "--ignore-scripts", "--no-audit", "--no-fund",
        ]
        assert kwargs["env"]["npm_config_cache"] == str(cache)
        assert "npm_config_offline" not in kwargs["env"]
        assert list(cache.iterdir()) == []
        (staging / "node_modules").mkdir()
        return subprocess.CompletedProcess(command, 0, "", "")

    monkeypatch.setattr(eval_runtime.subprocess, "run", fake_run)

    completed = eval_runtime._run_locked_npm_ci(staging)

    assert completed.returncode == 0
    assert (staging / "node_modules").is_dir()


def test_materializer_installs_locked_dependencies_per_lane(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch,
) -> None:
    repository = tmp_path / "repo"
    fixture = tmp_path / "fixture"
    site = fixture / "docs/site"
    site.mkdir(parents=True)
    (fixture / "package.json").write_text(
        json.dumps({"name": "host-root", "dependencies": {"root-dep": "1.0.0"}}),
        encoding="utf-8",
    )
    (fixture / "package-lock.json").write_text(json.dumps({
        "name": "host-root", "lockfileVersion": 3,
        "packages": {
            "": {"dependencies": {"root-dep": "1.0.0"}},
            "node_modules/root-dep": {"version": "1.0.0", "integrity": "sha512-root"},
        },
    }), encoding="utf-8")
    (site / "package.json").write_text(
        json.dumps({"name": "host-docs", "dependencies": {"fast-glob": "1.0.0"}}),
        encoding="utf-8",
    )
    (site / "package-lock.json").write_text(json.dumps({
        "name": "host-docs", "lockfileVersion": 3,
        "packages": {
            "": {"dependencies": {"fast-glob": "1.0.0"}},
            "node_modules/fast-glob": {"version": "1.0.0", "integrity": "sha512-host"},
        },
    }), encoding="utf-8")
    target = make_skill(repository, "docs", "docs-audit")

    def fake_ci(staging: Path):
        package = json.loads((staging / "package.json").read_text())
        name = min(package["dependencies"])
        module = staging / "node_modules" / name
        module.mkdir(parents=True)
        (module / "index.js").write_text("export default {};\n", encoding="utf-8")
        return subprocess.CompletedProcess([], 0, "", "")

    monkeypatch.setattr(eval_runtime, "_run_locked_npm_ci", fake_ci)
    run = eval_runtime.materialize_eval_run(
        fixture_root=fixture, repository_root=repository, target_skill=target,
        skill_dependencies=[], prompt="audit", runtime_isolation=RUNTIME_ISOLATION,
        runtime_root=tmp_path / "runtime", model_available=True,
    )

    assert not (run.canonical_root / "docs/site/node_modules").exists()
    assert run.dependency_evidence["status"] == "PASS"
    assert len(run.dependency_evidence["sites"]) == 2
    assert all(len(site["lock_sha256"]) == 64 for site in run.dependency_evidence["sites"])
    assert all(
        site["install_command"] == "npm ci --ignore-scripts --no-audit --no-fund"
        for site in run.dependency_evidence["sites"]
    )
    without = eval_runtime.open_context(run, "without_skill")
    first_module = without.workspace_root / "docs/site/node_modules/fast-glob/index.js"
    assert first_module.read_text() == "export default {};\n"
    assert (without.workspace_root / "node_modules/root-dep/index.js").is_file()
    config = (without.codex_home / "config.toml").read_text(encoding="utf-8")
    assert '"node_modules" = "read"' in config
    assert '"docs/site/node_modules" = "read"' in config
    assert eval_runtime._dependency_probe_sites(without) == [
        {"path": ".", "package": "root-dep"},
        {"path": "docs/site", "package": "fast-glob"},
    ]
    assert "node_modules" not in subprocess.check_output(
        ["git", "status", "--porcelain", "--untracked-files=all"],
        cwd=without.git_root, text=True,
    )
    assert eval_runtime.evaluate_context_preflight(
        run, without, "without_skill", passing_probe,
    ).checks["dependencies"] is True
    first_module.write_text("tampered\n", encoding="utf-8")
    assert eval_runtime.verify_context_dependencies(without)["status"] == "BLOCKED"
    first_root = without.outer_root
    eval_runtime.close_context(run, without, evidence_locked=True)
    with_skill = eval_runtime.open_context(run, "with_skill")
    assert not first_root.exists()
    assert (with_skill.workspace_root / "docs/site/node_modules/fast-glob/index.js").is_file()
    run.cleanup()


def test_locked_dependency_install_failure_blocks_preflight(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch,
) -> None:
    repository = tmp_path / "repo"
    fixture = tmp_path / "fixture"
    site = fixture / "docs/site"
    site.mkdir(parents=True)
    (site / "package.json").write_text('{"name":"host-docs"}', encoding="utf-8")
    (site / "package-lock.json").write_text(
        '{"name":"host-docs","lockfileVersion":3,"packages":{"":{}}}',
        encoding="utf-8",
    )
    target = make_skill(repository, "docs", "docs-audit")
    monkeypatch.setattr(
        eval_runtime, "_run_locked_npm_ci",
        lambda _path: subprocess.CompletedProcess([], 1, "", "locked install failed"),
    )
    run = eval_runtime.materialize_eval_run(
        fixture_root=fixture, repository_root=repository, target_skill=target,
        skill_dependencies=[], prompt="audit", runtime_isolation=RUNTIME_ISOLATION,
        runtime_root=tmp_path / "runtime", model_available=True,
    )
    context = eval_runtime.open_context(run, "without_skill")

    preflight = eval_runtime.evaluate_context_preflight(
        run, context, "without_skill", passing_probe,
    )

    assert preflight.status == "BLOCKED"
    assert preflight.checks["dependencies"] is False
    assert any("locked dependency" in blocker for blocker in preflight.blockers)
    run.cleanup()


def test_manifest_is_stable_and_detects_content_changes(tmp_path: Path) -> None:
    root = tmp_path / "fixture"
    root.mkdir()
    (root / "a.txt").write_text("alpha", encoding="utf-8")
    (root / "b.txt").write_text("beta", encoding="utf-8")

    first = eval_runtime.fixture_manifest(root)
    first_hash = eval_runtime.manifest_hash(first)
    assert first == eval_runtime.fixture_manifest(root)
    assert first_hash == eval_runtime.manifest_hash(first)

    (root / "b.txt").write_text("changed", encoding="utf-8")
    second = eval_runtime.fixture_manifest(root)
    assert second != first
    assert eval_runtime.manifest_hash(second) != first_hash


def test_materializer_creates_independent_git_home_and_exact_skill_overlay(
    tmp_path: Path,
) -> None:
    repository = tmp_path / "repo"
    fixture = tmp_path / "fixture"
    fixture.mkdir()
    (fixture / "input.md").write_text("host input", encoding="utf-8")
    target = make_skill(repository, "qa", "bug-analyzer", "# Target protocol\n")
    dependency = make_skill(repository, "qa", "qa-agent", "# Dependency protocol\n")

    materialized = eval_runtime.materialize_eval_run(
        fixture_root=fixture,
        repository_root=repository,
        target_skill=target,
        skill_dependencies=[dependency],
        prompt="请分析这份错误报告。",
        runtime_isolation=RUNTIME_ISOLATION,
        runtime_root=tmp_path / "runtime",
        model_available=True,
    )
    try:
        without = eval_runtime.open_context(materialized, "without_skill")
        without_outer = without.outer_root
        expected_git_bin = eval_runtime._bundled_git_bin()
        expected_prefix = [str(expected_git_bin)] if expected_git_bin else []
        assert without.env["PATH"].split(os.pathsep)[:len(expected_prefix) + 2] == [
            *expected_prefix, "/usr/bin", "/bin",
        ]
        assert without.env["TMPDIR"] == str(without.home / "tmp")
        assert without.env["GIT_BINARY"] == str(
            (expected_git_bin / "git") if expected_git_bin else Path("/usr/bin/git")
        )
        assert Path(without.env["TMPDIR"]).is_dir()
        assert "GITHUB_BASE_SHA" not in without.env
        assert (without.git_root / ".git").is_dir()
        assert without.skill_sources == ()
        assert not (without.workspace_root / ".agents/skills").exists()
        without_config = (without.codex_home / "config.toml").read_text(encoding="utf-8")
        assert "developer_instructions" not in without_config
        assert "[shell_environment_policy.set]" in without_config
        assert "TMPDIR" in without_config
        preflight = eval_runtime.evaluate_context_preflight(
            materialized, without, "without_skill", passing_probe,
        )
        assert preflight.status == "PASS"
        eval_runtime.close_context(materialized, without, evidence_locked=True)

        with_skill = eval_runtime.open_context(materialized, "with_skill")
        assert not without_outer.exists()
        assert (with_skill.git_root / ".git").is_dir()
        assert with_skill.skill_sources == (
            "agents/qa/skills/bug-analyzer",
            "agents/qa/skills/qa-agent",
        )
        assert (with_skill.workspace_root / ".agents/skills/bug-analyzer/SKILL.md").is_file()
        assert (with_skill.workspace_root / ".agents/skills/qa-agent/SKILL.md").is_file()
        with_config = (with_skill.codex_home / "config.toml").read_text(encoding="utf-8")
        assert "developer_instructions" in with_config
        assert "`.agents/skills/bug-analyzer`" in with_config
        assert "# Target protocol" in with_config
        assert "# Dependency protocol" not in with_config
        assert eval_runtime.evaluate_context_preflight(
            materialized, with_skill, "with_skill", passing_probe,
        ).status == "PASS"
        eval_runtime.close_context(materialized, with_skill, evidence_locked=True)
    finally:
        materialized.cleanup()


def test_materializer_builds_identical_declared_git_topology_in_both_lanes(
    tmp_path: Path,
) -> None:
    repository = tmp_path / "repo"
    fixture = tmp_path / "fixture"
    (fixture / "src").mkdir(parents=True)
    (fixture / "src/facts.txt").write_text("after\n", encoding="utf-8")
    (fixture / "change.patch").write_text(
        "diff --git a/src/facts.txt b/src/facts.txt\n"
        "--- a/src/facts.txt\n+++ b/src/facts.txt\n"
        "@@ -1 +1 @@\n-before\n+after\n",
        encoding="utf-8",
    )
    target = make_skill(repository, "docs", "docs-audit")
    topology = {
        "base_ref": "old-base",
        "target_ref": "release-head",
        "target_patch": "change.patch",
        "tags": [
            {"name": "v1.0.0", "target": "base", "kind": "lightweight"},
            {"name": "v1.1.0", "target": "target", "kind": "annotated"},
        ],
        "refs": [
            {"name": "refs/heads/release-evidence/v1.1.0", "target": "target"},
            {"name": "refs/release-evidence/v1.1.0", "target": "base"},
        ],
        "absent_refs": ["refs/tags/v2.0.0"],
    }
    run = eval_runtime.materialize_eval_run(
        fixture_root=fixture, repository_root=repository, target_skill=target,
        skill_dependencies=[], prompt="audit", runtime_isolation=RUNTIME_ISOLATION,
        runtime_root=tmp_path / "runtime", model_available=True,
        git_topology=topology,
    )

    def git(context: eval_runtime.IsolatedContext, *args: str) -> str:
        return subprocess.check_output(
            ["git", *args], cwd=context.git_root, text=True,
        ).strip()

    try:
        without = eval_runtime.open_context(run, "without_skill")
        assert git(without, "show", "old-base:src/facts.txt") == "before"
        assert git(without, "show", "release-head:src/facts.txt") == "after"
        assert git(without, "rev-parse", "HEAD") == git(
            without, "rev-parse", "release-head^{commit}",
        )
        assert without.env["GITHUB_BASE_SHA"] == git(
            without, "rev-parse", "old-base^{commit}",
        )
        assert "GITHUB_BASE_SHA" in (
            without.codex_home / "config.toml"
        ).read_text(encoding="utf-8")
        assert git(without, "cat-file", "-t", "v1.0.0") == "commit"
        assert git(without, "cat-file", "-t", "v1.1.0") == "tag"
        assert git(without, "rev-parse", "refs/release-evidence/v1.1.0^{commit}") \
            == git(without, "rev-parse", "old-base^{commit}")
        clone = without.git_topology["fresh_clone"]
        assert clone["custom_refs"]["refs/release-evidence/v1.1.0"] == {
            "source_present": True, "clone_present": False,
        }
        assert clone["tags"]["refs/tags/v1.1.0"]["clone_present"] is True
        assert clone["tags"]["refs/tags/v1.1.0"]["tree_matches"] is True
        assert clone["cleaned"] is True
        history = (
            git(without, "log", "--all", "--format=%an%n%ae%n%s%n%b")
            + "\n" + git(without, "for-each-ref", "refs/tags", "--format=%(contents)")
        ).lower()
        assert not any(marker in history for marker in ("eval", "fixture", "runtime", "test"))
        assert subprocess.run(
            ["git", "rev-parse", "--verify", "refs/tags/v2.0.0"],
            cwd=without.git_root, capture_output=True,
        ).returncode != 0
        assert not (without.workspace_root / "eval_metadata.json").exists()
        without_refs = git(
            without, "for-each-ref", "--format=%(refname) %(objecttype) %(objectname)",
        )
        without_ids = git(
            without, "rev-parse", "old-base^{commit}", "release-head^{commit}",
            "v1.0.0^{commit}", "v1.1.0^{commit}",
        )
        assert eval_runtime.evaluate_context_preflight(
            run, without, "without_skill", passing_probe,
        ).checks["git_topology"] is True
        eval_runtime.close_context(run, without, evidence_locked=True)

        with_skill = eval_runtime.open_context(run, "with_skill")
        assert git(
            with_skill, "for-each-ref", "--format=%(refname) %(objecttype) %(objectname)",
        ) == without_refs
        assert git(
            with_skill, "rev-parse", "old-base^{commit}", "release-head^{commit}",
            "v1.0.0^{commit}", "v1.1.0^{commit}",
        ) == without_ids
        assert ".agents" not in git(with_skill, "status", "--porcelain", "--untracked-files=all")
        assert eval_runtime.evaluate_context_preflight(
            run, with_skill, "with_skill", passing_probe,
        ).checks["git_topology"] is True
    finally:
        run.cleanup()


def test_preflight_blocks_tampered_declared_git_ref(tmp_path: Path) -> None:
    repository = tmp_path / "repo"
    fixture = tmp_path / "fixture"
    fixture.mkdir()
    (fixture / "input.md").write_text("host input", encoding="utf-8")
    target = make_skill(repository, "docs", "docs-audit")
    run = eval_runtime.materialize_eval_run(
        fixture_root=fixture, repository_root=repository, target_skill=target,
        skill_dependencies=[], prompt="audit", runtime_isolation=RUNTIME_ISOLATION,
        runtime_root=tmp_path / "runtime", model_available=True,
        git_topology={"base_ref": "base", "target_ref": "target"},
    )
    try:
        context = eval_runtime.open_context(run, "without_skill")
        subprocess.run(
            ["git", "branch", "-f", "base", "target"], cwd=context.git_root, check=True,
        )
        preflight = eval_runtime.evaluate_context_preflight(
            run, context, "without_skill", passing_probe,
        )
        assert preflight.status == "BLOCKED"
        assert preflight.checks["git_topology"] is False
    finally:
        run.cleanup()


def test_preflight_blocks_annotated_tag_object_rewrite_to_same_commit(
    tmp_path: Path,
) -> None:
    repository = tmp_path / "repo"
    fixture = tmp_path / "fixture"
    fixture.mkdir()
    (fixture / "input.md").write_text("host input", encoding="utf-8")
    target = make_skill(repository, "docs", "docs-audit")
    run = eval_runtime.materialize_eval_run(
        fixture_root=fixture, repository_root=repository, target_skill=target,
        skill_dependencies=[], prompt="audit", runtime_isolation=RUNTIME_ISOLATION,
        runtime_root=tmp_path / "runtime", model_available=True,
        git_topology={
            "base_ref": "base", "target_ref": "target",
            "tags": [{"name": "v1.0.0", "target": "target", "kind": "annotated"}],
        },
    )
    try:
        context = eval_runtime.open_context(run, "without_skill")
        commit = subprocess.check_output(
            ["git", "rev-parse", "v1.0.0^{commit}"], cwd=context.git_root, text=True,
        ).strip()
        subprocess.run([
            "git", "-c", "user.name=Repository Maintainer",
            "-c", "user.email=maintainer@example.invalid", "tag", "-f", "-a",
            "v1.0.0", "-m", "Rewritten release object", commit,
        ], cwd=context.git_root, check=True, capture_output=True)

        preflight = eval_runtime.evaluate_context_preflight(
            run, context, "without_skill", passing_probe,
        )

        assert preflight.status == "BLOCKED"
        assert preflight.checks["git_topology"] is False
    finally:
        run.cleanup()


def test_git_topology_materializes_mixed_patch_states_and_status_evidence(
    tmp_path: Path,
) -> None:
    repository = tmp_path / "repo"
    fixture = tmp_path / "fixture"
    (fixture / "src").mkdir(parents=True)
    (fixture / "docs").mkdir()
    (fixture / "drafts").mkdir()
    (fixture / "src/routes.txt").write_text("new route\n", encoding="utf-8")
    (fixture / "docs/api.md").write_text("new docs\n", encoding="utf-8")
    (fixture / "package.json").write_text('{"version":"2"}\n', encoding="utf-8")
    (fixture / "drafts/audit.md").write_text("draft\n", encoding="utf-8")
    (fixture / "change.patch").write_text(
        "diff --git a/src/routes.txt b/src/routes.txt\n"
        "--- a/src/routes.txt\n+++ b/src/routes.txt\n"
        "@@ -1 +1 @@\n-old route\n+new route\n"
        "diff --git a/docs/api.md b/docs/api.md\n"
        "--- a/docs/api.md\n+++ b/docs/api.md\n"
        "@@ -1 +1 @@\n-old docs\n+new docs\n"
        "diff --git a/package.json b/package.json\n"
        "--- a/package.json\n+++ b/package.json\n"
        "@@ -1 +1 @@\n-{\"version\":\"1\"}\n+{\"version\":\"2\"}\n"
        "diff --git a/drafts/audit.md b/drafts/audit.md\n"
        "new file mode 100644\n--- /dev/null\n+++ b/drafts/audit.md\n"
        "@@ -0,0 +1 @@\n+draft\n",
        encoding="utf-8",
    )
    target = make_skill(repository, "docs", "docs-audit")
    run = eval_runtime.materialize_eval_run(
        fixture_root=fixture, repository_root=repository, target_skill=target,
        skill_dependencies=[], prompt="audit", runtime_isolation=RUNTIME_ISOLATION,
        runtime_root=tmp_path / "runtime", model_available=True,
        git_topology={
            "base_ref": "base", "target_ref": "target",
            "target_patch": "change.patch",
            "target_patch_states": {
                "src/routes.txt": "staged",
                "docs/api.md": "unstaged",
                "package.json": "unstaged",
                "drafts/audit.md": "untracked",
            },
        },
    )
    try:
        context = eval_runtime.open_context(run, "without_skill")
        git = lambda *args: subprocess.check_output(
            ["git", *args], cwd=context.git_root, text=True,
        ).strip()
        assert git("show", "target:src/routes.txt") == "old route"
        status = subprocess.check_output(
            ["git", "status", "--porcelain=v1", "--untracked-files=all"],
            cwd=context.git_root, text=True,
        ).rstrip()
        assert status == (
            " M docs/api.md\n M package.json\nM  src/routes.txt\n?? drafts/audit.md"
        )
        assert context.git_topology["status_porcelain"] == status
        assert eval_runtime.evaluate_context_preflight(
            run, context, "without_skill", passing_probe,
        ).checks["git_topology"] is True
        subprocess.run(
            ["git", "reset", "-q", "HEAD", "--", "src/routes.txt"],
            cwd=context.git_root, check=True,
        )
        assert eval_runtime.evaluate_context_preflight(
            run, context, "without_skill", passing_probe,
        ).checks["git_topology"] is False
    finally:
        run.cleanup()


@pytest.mark.parametrize(
    "topology",
    [
        {"base_ref": "HEAD", "target_ref": "target"},
        {"base_ref": "main", "target_ref": "target"},
        {"base_ref": "base", "target_ref": "main"},
        {"base_ref": "base\nother", "target_ref": "target"},
        {"base_ref": "base", "target_ref": "target", "refs": [{"name": [], "target": "base"}]},
        {"base_ref": "base", "target_ref": "target", "refs": [{"name": "refs/heads/x", "target": []}]},
        {"base_ref": "base", "target_ref": "target", "tags": [{"name": "v1", "target": [], "kind": "lightweight"}]},
        {"base_ref": "base", "target_ref": "target", "tags": [{"name": "v1", "target": "base", "kind": []}]},
        {"base_ref": "base", "target_ref": "target", "absent_refs": [[]]},
        {"base_ref": "base", "target_ref": "target", "refs": [{"name": "refs/heads/base", "target": "target"}]},
        {"base_ref": "base", "target_ref": "target", "absent_refs": ["refs/heads/base"]},
        {"base_ref": "base", "target_ref": "target", "refs": [{"name": "refs/heads/-force", "target": "base"}]},
        {"base_ref": "base", "target_ref": "target", "tags": [{"name": "-force", "target": "base", "kind": "lightweight"}]},
    ],
)
def test_git_topology_validator_rejects_invalid_refs_without_type_error(
    topology: dict,
) -> None:
    errors = eval_runtime.git_topology_errors(topology)
    assert errors


def test_git_topology_rejects_unbounded_custom_ref_namespace() -> None:
    errors = eval_runtime.git_topology_errors({
        "base_ref": "base", "target_ref": "target",
        "refs": [{"name": "refs/arbitrary/escape", "target": "base"}],
    })

    assert errors


def test_git_topology_rejects_head_tag_short_name_collision() -> None:
    errors = eval_runtime.git_topology_errors({
        "base_ref": "base", "target_ref": "target",
        "refs": [{"name": "refs/heads/release/v1", "target": "base"}],
        "tags": [{"name": "release/v1", "target": "target", "kind": "lightweight"}],
    })

    assert any("short name" in error for error in errors)


def test_git_topology_rejects_tag_colliding_with_internal_main() -> None:
    errors = eval_runtime.git_topology_errors({
        "base_ref": "base", "target_ref": "target",
        "tags": [{"name": "main", "target": "target", "kind": "lightweight"}],
    })

    assert any("short name" in error for error in errors)


def test_git_topology_rejects_internal_main_as_absent() -> None:
    errors = eval_runtime.git_topology_errors({
        "base_ref": "base", "target_ref": "target",
        "absent_refs": ["refs/heads/main"],
    })

    assert any("both present and absent" in error for error in errors)


def test_git_topology_rejects_option_like_patch_path() -> None:
    errors = eval_runtime.git_topology_errors({
        "base_ref": "base", "target_ref": "target", "target_patch": "release/-force.patch",
    })

    assert errors


def test_git_topology_rejects_excluded_target_patch(tmp_path: Path) -> None:
    fixture = tmp_path / "fixture"
    patch = fixture / "with_skill/answer.patch"
    patch.parent.mkdir(parents=True)
    patch.write_text("not candidate-visible\n", encoding="utf-8")

    errors = eval_runtime.git_topology_errors({
        "base_ref": "base", "target_ref": "target",
        "target_patch": "with_skill/answer.patch",
    }, fixture)

    assert any("excluded" in error for error in errors)


def test_git_topology_rejects_excluded_base_file_source(tmp_path: Path) -> None:
    fixture = tmp_path / "fixture"
    source = fixture / "with_skill/answer.md"
    source.parent.mkdir(parents=True)
    source.write_text("not candidate-visible\n", encoding="utf-8")

    errors = eval_runtime.git_topology_errors({
        "base_ref": "base", "target_ref": "target",
        "base_files": [{"source": "with_skill/answer.md", "path": "docs/host.md"}],
    }, fixture)

    assert any("source is excluded" in error for error in errors)


def test_git_topology_missing_new_file_reports_error_without_read_failure(
    tmp_path: Path,
) -> None:
    fixture = tmp_path / "fixture"
    fixture.mkdir()
    (fixture / "change.patch").write_text(
        "diff --git a/new.txt b/new.txt\n"
        "new file mode 100644\n--- /dev/null\n+++ b/new.txt\n"
        "@@ -0,0 +1 @@\n+new content\n",
        encoding="utf-8",
    )

    errors = eval_runtime.git_topology_errors(
        {"base_ref": "base", "target_ref": "target", "target_patch": "change.patch"},
        fixture,
    )

    assert any("target files do not exist" in error for error in errors)


@pytest.mark.parametrize(
    "hunk",
    [
        "@@\n-old\n+new\n",
        "@@ -1 +1 @@\n-same\n+same\n",
        "@@ -1 +0,0 @@\n-old\n",
    ],
)
def test_git_topology_rejects_malformed_noop_and_deletion_only_patches(
    tmp_path: Path, hunk: str,
) -> None:
    fixture = tmp_path / "fixture"
    fixture.mkdir()
    (fixture / "facts.txt").write_text("new\n", encoding="utf-8")
    (fixture / "change.patch").write_text(
        "diff --git a/facts.txt b/facts.txt\n"
        "--- a/facts.txt\n+++ b/facts.txt\n" + hunk,
        encoding="utf-8",
    )

    errors = eval_runtime.git_topology_errors(
        {"base_ref": "base", "target_ref": "target", "target_patch": "change.patch"},
        fixture,
    )

    assert any("supported fixture patch" in error for error in errors)


def test_git_topology_rejects_patch_that_does_not_apply_to_current_bytes(
    tmp_path: Path,
) -> None:
    fixture = tmp_path / "fixture"
    fixture.mkdir()
    (fixture / "facts.txt").write_text("actual current\n", encoding="utf-8")
    (fixture / "change.patch").write_text(
        "diff --git a/facts.txt b/facts.txt\n"
        "--- a/facts.txt\n+++ b/facts.txt\n"
        "@@ -1 +1 @@\n-before\n+claimed current\n",
        encoding="utf-8",
    )

    errors = eval_runtime.git_topology_errors(
        {"base_ref": "base", "target_ref": "target", "target_patch": "change.patch"},
        fixture,
    )

    assert any("does not apply to current fixture bytes" in error for error in errors)


def test_runtime_read_roots_skips_missing_platform_tool(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    real_run = eval_runtime.subprocess.run

    monkeypatch.setattr(eval_runtime.shutil, "which", lambda _name: None)

    def reject_missing_tool(command, *args, **kwargs):
        if command[0] == "xcode-select":
            raise FileNotFoundError("xcode-select is unavailable")
        return real_run(command, *args, **kwargs)

    monkeypatch.setattr(eval_runtime.subprocess, "run", reject_missing_tool)

    assert isinstance(eval_runtime._runtime_read_roots(), tuple)


def test_preflight_blocks_unknown_runtime_and_does_not_report_pass(
    tmp_path: Path,
) -> None:
    repository = tmp_path / "repo"
    fixture = tmp_path / "fixture"
    fixture.mkdir()
    (fixture / "input.md").write_text("host input", encoding="utf-8")
    target = make_skill(repository, "qa", "bug-analyzer")
    runtime_isolation = dict(RUNTIME_ISOLATION)
    runtime_isolation["browser"] = "unknown"

    materialized = eval_runtime.materialize_eval_run(
        fixture_root=fixture,
        repository_root=repository,
        target_skill=target,
        skill_dependencies=[],
        prompt="请分析这份错误报告。",
        runtime_isolation=runtime_isolation,
        runtime_root=tmp_path / "runtime",
        model_available=True,
    )
    try:
        context = eval_runtime.open_context(materialized, "without_skill")
        preflight = eval_runtime.evaluate_context_preflight(
            materialized, context, "without_skill", passing_probe,
        )
        eval_runtime.record_preflight(materialized, "without_skill", preflight)
        assert preflight.status == "BLOCKED"
        assert preflight.checks["runtime"] is False
        assert any("browser" in blocker for blocker in preflight.blockers)
        assert json.loads(materialized.preflight_path.read_text())["status"] == "BLOCKED"
    finally:
        materialized.cleanup()


def test_preflight_blocks_model_unavailable_and_fixture_mismatch(tmp_path: Path) -> None:
    repository = tmp_path / "repo"
    fixture = tmp_path / "fixture"
    fixture.mkdir()
    (fixture / "input.md").write_text("host input", encoding="utf-8")
    target = make_skill(repository, "qa", "bug-analyzer")

    materialized = eval_runtime.materialize_eval_run(
        fixture_root=fixture,
        repository_root=repository,
        target_skill=target,
        skill_dependencies=[],
        prompt="请分析这份错误报告。",
        runtime_isolation=RUNTIME_ISOLATION,
        runtime_root=tmp_path / "runtime",
        model_available=False,
    )
    try:
        context = eval_runtime.open_context(materialized, "without_skill")
        (context.workspace_root / "input.md").write_text("tampered", encoding="utf-8")
        preflight = eval_runtime.evaluate_context_preflight(
            materialized, context, "without_skill", passing_probe,
        )
        assert preflight.status == "BLOCKED"
        assert preflight.checks["model"] is False
        assert preflight.checks["fixture"] is False
    finally:
        materialized.cleanup()


def test_preflight_blocks_answer_guidance_and_source_path_in_fixture(tmp_path: Path) -> None:
    repository = tmp_path / "repo"
    fixture = tmp_path / "fixture"
    (fixture / "service").mkdir(parents=True)
    (fixture / "service/README.md").write_text(
        "Expected behavior: dispatcher should return PASS.", encoding="utf-8"
    )
    (fixture / "service/context.txt").write_text(
        f"Read the source at {repository}", encoding="utf-8"
    )
    target = make_skill(repository, "qa", "bug-analyzer")

    materialized = eval_runtime.materialize_eval_run(
        fixture_root=fixture,
        repository_root=repository,
        target_skill=target,
        skill_dependencies=[],
        prompt="请分析服务异常。",
        runtime_isolation=RUNTIME_ISOLATION,
        runtime_root=tmp_path / "runtime",
        model_available=True,
    )
    try:
        context = eval_runtime.open_context(materialized, "without_skill")
        preflight = eval_runtime.evaluate_context_preflight(
            materialized, context, "without_skill", passing_probe,
        )
        assert preflight.status == "BLOCKED"
        assert not (context.workspace_root / "service/README.md").exists()
        assert preflight.checks["exclusions"] is True
        assert preflight.checks["source_isolation"] is False
    finally:
        materialized.cleanup()


def test_preflight_blocks_workspace_nested_under_source_root(tmp_path: Path) -> None:
    repository = tmp_path / "repo"
    fixture = tmp_path / "fixture"
    fixture.mkdir()
    (fixture / "input.md").write_text("host input", encoding="utf-8")
    target = make_skill(repository, "qa", "bug-analyzer")
    materialized = eval_runtime.materialize_eval_run(
        fixture_root=fixture, repository_root=repository, target_skill=target,
        skill_dependencies=[], prompt="请分析服务异常。",
        runtime_isolation=RUNTIME_ISOLATION, runtime_root=tmp_path / "runtime",
        model_available=True,
    )
    try:
        context = eval_runtime.open_context(materialized, "without_skill")
        materialized.repository_root = context.outer_root
        preflight = eval_runtime.evaluate_context_preflight(
            materialized, context, "without_skill", passing_probe,
        )
        assert preflight.checks["source_isolation"] is False
    finally:
        materialized.cleanup()
