import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


CHECKER_PATH = Path(__file__).resolve().parents[1] / "scripts/check_eval_contract.py"
ARTIFACT_CHECKER_PATH = Path(__file__).resolve().parents[1] / "scripts/check_eval_artifacts.py"
REPOSITORY_CHECKER_PATH = (
    Path(__file__).resolve().parents[1] / "scripts/check_repository_contract.py"
)


def load_checker_module():
    spec = importlib.util.spec_from_file_location("check_eval_contract", CHECKER_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules["check_eval_contract"] = module
    spec.loader.exec_module(module)
    return module


def load_artifact_checker_module():
    spec = importlib.util.spec_from_file_location(
        "check_eval_artifacts",
        ARTIFACT_CHECKER_PATH,
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules["check_eval_artifacts"] = module
    spec.loader.exec_module(module)
    return module


def load_repository_checker_module():
    spec = importlib.util.spec_from_file_location(
        "check_repository_contract",
        REPOSITORY_CHECKER_PATH,
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules["check_repository_contract"] = module
    spec.loader.exec_module(module)
    return module


def init_git_main(root: Path) -> None:
    subprocess.run(["git", "init", "-b", "main"], cwd=root, check=True)
    (root / "README.md").write_text("# Fixture\n")
    subprocess.run(["git", "add", "README.md"], cwd=root, check=True)
    subprocess.run(
        [
            "git",
            "-c",
            "user.name=Test User",
            "-c",
            "user.email=test@example.com",
            "commit",
            "-m",
            "base",
        ],
        cwd=root,
        check=True,
        stdout=subprocess.DEVNULL,
    )
    subprocess.run(["git", "switch", "-c", "feature"], cwd=root, check=True)


class EvalContractTests(unittest.TestCase):
    def write_eval_fixture(self, root: Path, comparison_text: str) -> Path:
        evals_path = root / "agents/engineer/test/debugger/evals/evals.json"
        skill_doc = root / "agents/engineer/skills/debugger/SKILL.md"
        workspace = evals_path.parent / "workspace/eval-001-baseline-evidence"
        workspace.mkdir(parents=True)
        skill_doc.parent.mkdir(parents=True)
        skill_doc.write_text("# Debugger\n")
        (workspace / "comparison.md").write_text(comparison_text)
        (workspace / "eval_metadata.json").write_text(
            json.dumps(
                {
                    "eval_id": "eval-001-baseline-evidence",
                    "eval_name": "baseline-evidence",
                }
            )
        )
        evals_path.write_text(
            json.dumps(
                {
                    "schema_version": "1.0",
                    "agent": "engineer",
                    "skill_name": "debugger",
                    "evals": [
                        {
                            "id": "eval-001-baseline-evidence",
                            "name": "baseline-evidence",
                            "description": "Baseline evidence fixture",
                            "prompt": "Run the eval",
                            "workspace": "workspace/eval-001-baseline-evidence",
                            "expected_output": "A result",
                            "assertions": [
                                {
                                    "id": "has_result",
                                    "description": "Has a result",
                                    "text": "Result is present",
                                }
                            ],
                        }
                    ],
                }
            )
        )
        return evals_path

    def test_all_agent_skill_evals_follow_shared_contract(self):
        checker = load_checker_module()
        errors = checker.validate_all()

        self.assertEqual(
            [error.render(checker.repo_root()) for error in errors],
            [],
        )

    def test_eval_contract_rejects_null_workspace(self):
        checker = load_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            evals_path = root / "agents/engineer/test/debugger/evals/evals.json"
            skill_doc = root / "agents/engineer/skills/debugger/SKILL.md"
            evals_path.parent.mkdir(parents=True)
            skill_doc.parent.mkdir(parents=True)
            skill_doc.write_text("# Debugger\n")
            evals_path.write_text(
                json.dumps(
                    {
                        "schema_version": "1.0",
                        "agent": "engineer",
                        "skill_name": "debugger",
                        "evals": [
                            {
                                "id": "eval-001-null-workspace",
                                "name": "null-workspace",
                                "description": "Invalid null workspace fixture",
                                "prompt": "Run the eval",
                                "workspace": None,
                                "expected_output": "A result",
                                "assertions": [
                                    {
                                        "id": "has_result",
                                        "description": "Has a result",
                                        "text": "Result is present",
                                    }
                                ],
                            }
                        ],
                    }
                )
            )

            errors = checker.validate_file(root, evals_path)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn("workspace must be a non-empty string", rendered)

    def test_eval_contract_rejects_subagent_verdict_metadata_outputs(self):
        checker = load_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            evals_path = root / "agents/engineer/test/debugger/evals/evals.json"
            skill_doc = root / "agents/engineer/skills/debugger/SKILL.md"
            workspace = evals_path.parent / "workspace/eval-001-subagent-verdict"
            workspace.mkdir(parents=True)
            skill_doc.parent.mkdir(parents=True)
            skill_doc.write_text("# Debugger\n")
            (workspace / "comparison.md").write_text("# Comparison\n")
            (workspace / "eval_metadata.json").write_text(
                json.dumps(
                    {
                        "eval_id": "eval-001-subagent-verdict",
                        "eval_name": "subagent-verdict",
                        "validation_method": "fresh_codex_subagent",
                        "with_skill_outputs": [
                            "with_skill/outputs/subagent-verdict.md"
                        ],
                        "without_skill_outputs": [
                            "without_skill/outputs/subagent-verdict.md"
                        ],
                    }
                )
            )
            evals_path.write_text(
                json.dumps(
                    {
                        "schema_version": "1.0",
                        "agent": "engineer",
                        "skill_name": "debugger",
                        "evals": [
                            {
                                "id": "eval-001-subagent-verdict",
                                "name": "subagent-verdict",
                                "description": "Invalid runtime verdict output",
                                "prompt": "Run the eval",
                                "workspace": "workspace/eval-001-subagent-verdict",
                                "expected_output": "A result",
                                "assertions": [
                                    {
                                        "id": "has_result",
                                        "description": "Has a result",
                                        "text": "Result is present",
                                    }
                                ],
                            }
                        ],
                    }
                )
            )

            errors = checker.validate_file(root, evals_path)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn("validation_method must not be committed", rendered)
        self.assertIn("must not reference runtime diagnostic output", rendered)

    def test_eval_contract_rejects_transcript_metadata_assertion_targets(self):
        checker = load_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            evals_path = root / "agents/engineer/test/debugger/evals/evals.json"
            skill_doc = root / "agents/engineer/skills/debugger/SKILL.md"
            workspace = evals_path.parent / "workspace/eval-001-transcript-target"
            workspace.mkdir(parents=True)
            skill_doc.parent.mkdir(parents=True)
            skill_doc.write_text("# Debugger\n")
            (workspace / "comparison.md").write_text("# Comparison\n")
            (workspace / "eval_metadata.json").write_text(
                json.dumps(
                    {
                        "eval_id": "eval-001-transcript-target",
                        "eval_name": "transcript-target",
                        "assertions": [
                            {
                                "id": "has_transcript_text",
                                "description": "Invalid transcript target",
                                "target": "with_skill/outputs/transcript.md",
                                "all_of": ["Result"],
                            }
                        ],
                    }
                )
            )
            evals_path.write_text(
                json.dumps(
                    {
                        "schema_version": "1.0",
                        "agent": "engineer",
                        "skill_name": "debugger",
                        "evals": [
                            {
                                "id": "eval-001-transcript-target",
                                "name": "transcript-target",
                                "description": "Invalid transcript target",
                                "prompt": "Run the eval",
                                "workspace": "workspace/eval-001-transcript-target",
                                "expected_output": "A result",
                                "assertions": [
                                    {
                                        "id": "has_result",
                                        "description": "Has a result",
                                        "text": "Result is present",
                                    }
                                ],
                            }
                        ],
                    }
                )
            )

            errors = checker.validate_file(root, evals_path)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn("must not reference runtime diagnostic output", rendered)
        self.assertIn("with_skill/outputs/transcript.md", rendered)

    def test_eval_contract_allows_fixture_context_diagnostic_names(self):
        checker = load_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            evals_path = root / "agents/engineer/test/debugger/evals/evals.json"
            skill_doc = root / "agents/engineer/skills/debugger/SKILL.md"
            workspace = evals_path.parent / "workspace/eval-001-fixture-transcript"
            workspace.mkdir(parents=True)
            skill_doc.parent.mkdir(parents=True)
            skill_doc.write_text("# Debugger\n")
            (workspace / "comparison.md").write_text("# Comparison\n")
            (workspace / "eval_metadata.json").write_text(
                json.dumps(
                    {
                        "eval_id": "eval-001-fixture-transcript",
                        "eval_name": "fixture-transcript",
                        "fixture_context": [
                            "fixtures/customer-interview/transcript.md",
                            "fixtures/diagnostics/readme.md",
                        ],
                    }
                )
            )
            evals_path.write_text(
                json.dumps(
                    {
                        "schema_version": "1.0",
                        "agent": "engineer",
                        "skill_name": "debugger",
                        "evals": [
                            {
                                "id": "eval-001-fixture-transcript",
                                "name": "fixture-transcript",
                                "description": "Valid fixture transcript input",
                                "prompt": "Run the eval",
                                "workspace": "workspace/eval-001-fixture-transcript",
                                "expected_output": "A result",
                                "assertions": [
                                    {
                                        "id": "has_result",
                                        "description": "Has a result",
                                        "text": "Result is present",
                                    }
                                ],
                            }
                        ],
                    }
                )
            )

            errors = checker.validate_file(root, evals_path)

        self.assertEqual(
            "\n".join(error.render(root) for error in errors),
            "",
        )

    def test_eval_contract_rejects_runtime_artifact_metadata_paths(self):
        checker = load_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            evals_path = root / "agents/engineer/test/debugger/evals/evals.json"
            skill_doc = root / "agents/engineer/skills/debugger/SKILL.md"
            workspace = evals_path.parent / "workspace/eval-001-runtime-artifacts"
            workspace.mkdir(parents=True)
            skill_doc.parent.mkdir(parents=True)
            skill_doc.write_text("# Debugger\n")
            (workspace / "comparison.md").write_text("# Comparison\n")
            (workspace / "eval_metadata.json").write_text(
                json.dumps(
                    {
                        "eval_id": "eval-001-runtime-artifacts",
                        "eval_name": "runtime-artifacts",
                        "with_skill_outputs": [
                            "diagnostics",
                            "with_skill/outputs/candidate-output.md",
                            "with_skill/outputs/run_status.json",
                        ],
                        "run_diagnostics": ["diagnostics"],
                    }
                )
            )
            evals_path.write_text(
                json.dumps(
                    {
                        "schema_version": "1.0",
                        "agent": "engineer",
                        "skill_name": "debugger",
                        "evals": [
                            {
                                "id": "eval-001-runtime-artifacts",
                                "name": "runtime-artifacts",
                                "description": "Invalid runtime artifact outputs",
                                "prompt": "Run the eval",
                                "workspace": "workspace/eval-001-runtime-artifacts",
                                "expected_output": "A result",
                                "assertions": [
                                    {
                                        "id": "has_result",
                                        "description": "Has a result",
                                        "text": "Result is present",
                                    }
                                ],
                            }
                        ],
                    }
                )
            )

            errors = checker.validate_file(root, evals_path)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn("with_skill/outputs/candidate-output.md", rendered)
        self.assertIn("with_skill/outputs/run_status.json", rendered)
        self.assertIn("diagnostics", rendered)

    def test_eval_contract_rejects_runner_diagnostics_with_empty_outputs(self):
        checker = load_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            evals_path = root / "agents/engineer/test/debugger/evals/evals.json"
            skill_doc = root / "agents/engineer/skills/debugger/SKILL.md"
            workspace = evals_path.parent / "workspace/eval-001-empty-outputs"
            workspace.mkdir(parents=True)
            skill_doc.parent.mkdir(parents=True)
            skill_doc.write_text("# Debugger\n")
            (workspace / "comparison.md").write_text("# Comparison\n")
            (workspace / "eval_metadata.json").write_text(
                json.dumps(
                    {
                        "eval_id": "eval-001-empty-outputs",
                        "eval_name": "empty-outputs",
                        "with_skill_outputs": [],
                        "without_skill_outputs": [],
                        "run_diagnostics": ["diagnostics/run.json"],
                    }
                )
            )
            evals_path.write_text(
                json.dumps(
                    {
                        "schema_version": "1.0",
                        "agent": "engineer",
                        "skill_name": "debugger",
                        "evals": [
                            {
                                "id": "eval-001-empty-outputs",
                                "name": "empty-outputs",
                                "description": "Invalid empty output fields",
                                "prompt": "Run the eval",
                                "workspace": "workspace/eval-001-empty-outputs",
                                "expected_output": "A result",
                                "assertions": [
                                    {
                                        "id": "has_result",
                                        "description": "Has a result",
                                        "text": "Result is present",
                                    }
                                ],
                            }
                        ],
                    }
                )
            )

            errors = checker.validate_file(root, evals_path)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn(
            "run_diagnostics requires deterministic runner outputs",
            rendered,
        )
        self.assertNotIn("execution_cleanup requires deterministic runner outputs", rendered)

    def test_eval_contract_allows_execution_cleanup_without_outputs(self):
        checker = load_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            evals_path = root / "agents/engineer/test/debugger/evals/evals.json"
            skill_doc = root / "agents/engineer/skills/debugger/SKILL.md"
            workspace = evals_path.parent / "workspace/eval-001-cleanup-only"
            workspace.mkdir(parents=True)
            skill_doc.parent.mkdir(parents=True)
            skill_doc.write_text("# Debugger\n")
            (workspace / "comparison.md").write_text("# Comparison\n")
            (workspace / "eval_metadata.json").write_text(
                json.dumps(
                    {
                        "eval_id": "eval-001-cleanup-only",
                        "eval_name": "cleanup-only",
                        "execution_cleanup": ["docs/pm/"],
                    }
                )
            )
            evals_path.write_text(
                json.dumps(
                    {
                        "schema_version": "1.0",
                        "agent": "engineer",
                        "skill_name": "debugger",
                        "evals": [
                            {
                                "id": "eval-001-cleanup-only",
                                "name": "cleanup-only",
                                "description": "Valid cleanup-only metadata",
                                "prompt": "Run the eval",
                                "workspace": "workspace/eval-001-cleanup-only",
                                "expected_output": "A result",
                                "assertions": [
                                    {
                                        "id": "has_result",
                                        "description": "Has a result",
                                        "text": "Result is present",
                                    }
                                ],
                            }
                        ],
                    }
                )
            )

            errors = checker.validate_file(root, evals_path)

        self.assertEqual(
            "\n".join(error.render(root) for error in errors),
            "",
        )

    def test_eval_contract_rejects_pass_with_diagnostic_only_baseline(self):
        checker = load_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            evals_path = self.write_eval_fixture(
                root,
                "# Comparison\n\n"
                "- Latest result: PASS - fresh validation passed\n\n"
                "## Without Skill / Baseline\n\n"
                "- Baseline behavior is diagnostic only.\n",
            )

            errors = checker.validate_file(root, evals_path)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn(
            "Latest result PASS cannot be paired with explicit missing or blocked baseline state",
            rendered,
        )
        self.assertIn("baseline is diagnostic-only", rendered)

    def test_eval_contract_rejects_pass_with_remaining_diagnostic_baseline(self):
        checker = load_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            evals_path = self.write_eval_fixture(
                root,
                "# Comparison\n\n"
                "- Latest result: PASS - fresh validation passed\n\n"
                "## Without Skill / Baseline\n\n"
                "- Baseline behavior remains diagnostic: a generic response may miss the guardrail.\n",
            )

            errors = checker.validate_file(root, evals_path)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn(
            "Latest result PASS cannot be paired with explicit missing or blocked baseline state",
            rendered,
        )
        self.assertIn("baseline remains diagnostic-only", rendered)

    def test_eval_contract_rejects_pass_with_blocked_baseline(self):
        checker = load_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            evals_path = self.write_eval_fixture(
                root,
                "# Comparison\n\n"
                "- Latest result: PASS - fresh validation passed\n\n"
                "## Without Skill / Baseline\n\n"
                "- BLOCKED: without-skill baseline was not generated.\n",
            )

            errors = checker.validate_file(root, evals_path)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn(
            "Latest result PASS cannot be paired with explicit missing or blocked baseline state",
            rendered,
        )

    def test_eval_contract_rejects_pass_with_skipped_baseline_sentence(self):
        checker = load_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            evals_path = self.write_eval_fixture(
                root,
                "# Comparison\n\n"
                "- Latest result: PASS - fresh validation passed\n\n"
                "## Without Skill / Baseline\n\n"
                "- Baseline was skipped because the runner was unavailable.\n",
            )

            errors = checker.validate_file(root, evals_path)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn("baseline is blocked or skipped", rendered)

    def test_eval_contract_rejects_pass_with_blocked_baseline_sentence(self):
        checker = load_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            evals_path = self.write_eval_fixture(
                root,
                "# Comparison\n\n"
                "- Latest result: PASS - fresh validation passed\n\n"
                "## Without Skill / Baseline\n\n"
                "- Without-skill baseline is blocked by missing credentials.\n",
            )

            errors = checker.validate_file(root, evals_path)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn("baseline is blocked or skipped", rendered)

    def test_eval_contract_allows_pass_with_actual_baseline(self):
        checker = load_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            evals_path = self.write_eval_fixture(
                root,
                "# Comparison\n\n"
                "- Latest result: PASS - with-skill and without-skill runs passed\n\n"
                "## Without Skill / Baseline\n\n"
                "- PASS. Baseline run `019ef5f3-e0e2-7ef3-adb9-5f89535a79f3` passed "
                "against the same prompt and fixture.\n",
            )

            errors = checker.validate_file(root, evals_path)

        self.assertEqual("\n".join(error.render(root) for error in errors), "")

    def test_eval_contract_allows_pass_with_reviewed_hypothetical_baseline(self):
        checker = load_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            evals_path = self.write_eval_fixture(
                root,
                "# Comparison\n\n"
                "- Latest result: PASS - reviewed comparison retained by maintainer\n\n"
                "## Without Skill / Baseline\n\n"
                "- May skip the required gate in a generic response.\n"
                "- Less consistently preserves the role boundary.\n",
            )

            errors = checker.validate_file(root, evals_path)

        self.assertEqual("\n".join(error.render(root) for error in errors), "")

    def test_eval_contract_allows_partial_with_missing_baseline_reason(self):
        checker = load_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            evals_path = self.write_eval_fixture(
                root,
                "# Comparison\n\n"
                "- Latest result: PARTIAL - with-skill validation passed; baseline not generated\n\n"
                "## Without Skill / Baseline\n\n"
                "- BLOCKED: without-skill baseline was not generated for this historical comparison.\n",
            )

            errors = checker.validate_file(root, evals_path)

        self.assertEqual("\n".join(error.render(root) for error in errors), "")

    def test_artifact_checker_blocks_tmp_eval_runs(self):
        checker = load_artifact_checker_module()

        self.assertTrue(
            checker.is_runtime_artifact(
                "tmp/eval-runs/qa/agents/qa/test/example/comparison.auto.md"
            )
        )

    def test_artifact_checker_scopes_agent_runtime_patterns_to_tests(self):
        checker = load_artifact_checker_module()

        self.assertTrue(
            checker.is_runtime_artifact(
                "agents/qa/test/example/with_skill/outputs/transcript.md"
            )
        )
        self.assertFalse(
            checker.is_runtime_artifact(
                "agents/qa/skills/example/with_skill/README.md"
            )
        )

    def test_repository_contract_rejects_stale_marketplace_metadata_version(self):
        checker = load_repository_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            marketplace = root / ".claude-plugin/marketplace.json"
            skill_doc = root / "agents/engineer/skills/example/SKILL.md"
            changelog = root / "docs/changelog/changelog-v0.1.3.md"
            marketplace.parent.mkdir(parents=True)
            skill_doc.parent.mkdir(parents=True)
            changelog.parent.mkdir(parents=True)
            skill_doc.write_text(
                "---\n"
                "name: example\n"
                "description: Example skill\n"
                "---\n"
            )
            changelog.write_text("# Changelog - v0.1.3\n")
            marketplace.write_text(
                json.dumps(
                    {
                        "name": "dev-agent-skills",
                        "owner": {"name": "Neplich"},
                        "metadata": {"version": "0.1.2"},
                        "plugins": [
                            {
                                "name": "engineer-agent",
                                "source": "./agents/engineer",
                                "skills": ["./skills/example"],
                            }
                        ],
                    }
                )
            )

            errors = []
            checker.validate_marketplace(root, errors)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn("metadata.version must match latest changelog version '0.1.3'", rendered)

    def test_repository_contract_orders_prerelease_changelog_versions(self):
        checker = load_repository_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            marketplace = root / ".claude-plugin/marketplace.json"
            skill_doc = root / "agents/engineer/skills/example/SKILL.md"
            changelog_dir = root / "docs/changelog"
            changelog_index = root / "CHANGELOG.md"
            marketplace.parent.mkdir(parents=True)
            skill_doc.parent.mkdir(parents=True)
            changelog_dir.mkdir(parents=True)
            skill_doc.write_text(
                "---\n"
                "name: example\n"
                "description: Example skill\n"
                "---\n"
            )
            (changelog_dir / "changelog-v1.2.3-rc.2.md").write_text(
                "# Changelog - v1.2.3-rc.2\n"
            )
            (changelog_dir / "changelog-v1.2.3-rc.10.md").write_text(
                "# Changelog - v1.2.3-rc.10\n"
            )
            changelog_index.write_text(
                "# Changelog\n\n"
                "- [v1.2.3-rc.10](./docs/changelog/changelog-v1.2.3-rc.10.md)\n"
            )
            marketplace.write_text(
                json.dumps(
                    {
                        "name": "dev-agent-skills",
                        "owner": {"name": "Neplich"},
                        "metadata": {"version": "1.2.3-rc.10"},
                        "plugins": [
                            {
                                "name": "engineer-agent",
                                "source": "./agents/engineer",
                                "skills": ["./skills/example"],
                            }
                        ],
                    }
                )
            )

            errors = []
            latest_version = checker.latest_changelog_version(root)
            checker.validate_marketplace(root, errors)

        self.assertEqual(latest_version, "1.2.3-rc.10")
        self.assertEqual("\n".join(error.render(root) for error in errors), "")

    def test_repository_contract_rejects_invalid_prerelease_metadata_version(self):
        checker = load_repository_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            marketplace = root / ".claude-plugin/marketplace.json"
            skill_doc = root / "agents/engineer/skills/example/SKILL.md"
            changelog = root / "docs/changelog/changelog-v1.2.3-rc.1.md"
            marketplace.parent.mkdir(parents=True)
            skill_doc.parent.mkdir(parents=True)
            changelog.parent.mkdir(parents=True)
            skill_doc.write_text(
                "---\n"
                "name: example\n"
                "description: Example skill\n"
                "---\n"
            )
            changelog.write_text("# Changelog - v1.2.3-rc.1\n")
            marketplace.write_text(
                json.dumps(
                    {
                        "name": "dev-agent-skills",
                        "owner": {"name": "Neplich"},
                        "metadata": {"version": "1.2.3-rc.01"},
                        "plugins": [
                            {
                                "name": "engineer-agent",
                                "source": "./agents/engineer",
                                "skills": ["./skills/example"],
                            }
                        ],
                    }
                )
            )

            errors = []
            checker.validate_marketplace(root, errors)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn("metadata.version must be SemVer without a leading 'v'", rendered)

    def test_repository_contract_rejects_invalid_prerelease_changelog_filename(self):
        checker = load_repository_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            marketplace = root / ".claude-plugin/marketplace.json"
            skill_doc = root / "agents/engineer/skills/example/SKILL.md"
            changelog = root / "docs/changelog/changelog-v1.2.3-rc..1.md"
            marketplace.parent.mkdir(parents=True)
            skill_doc.parent.mkdir(parents=True)
            changelog.parent.mkdir(parents=True)
            skill_doc.write_text(
                "---\n"
                "name: example\n"
                "description: Example skill\n"
                "---\n"
            )
            changelog.write_text("# Changelog - v1.2.3-rc..1\n")
            marketplace.write_text(
                json.dumps(
                    {
                        "name": "dev-agent-skills",
                        "owner": {"name": "Neplich"},
                        "metadata": {"version": "1.2.3-rc.1"},
                        "plugins": [
                            {
                                "name": "engineer-agent",
                                "source": "./agents/engineer",
                                "skills": ["./skills/example"],
                            }
                        ],
                    }
                )
            )

            errors = []
            checker.validate_marketplace(root, errors)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn(
            "changelog-v1.2.3-rc..1.md: changelog filename must use changelog-v{SemVer}.md",
            rendered,
        )

    def test_repository_contract_rejects_invalid_changelog_filename_alongside_valid_file(self):
        checker = load_repository_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            marketplace = root / ".claude-plugin/marketplace.json"
            skill_doc = root / "agents/engineer/skills/example/SKILL.md"
            changelog_dir = root / "docs/changelog"
            changelog_index = root / "CHANGELOG.md"
            marketplace.parent.mkdir(parents=True)
            skill_doc.parent.mkdir(parents=True)
            changelog_dir.mkdir(parents=True)
            skill_doc.write_text(
                "---\n"
                "name: example\n"
                "description: Example skill\n"
                "---\n"
            )
            (changelog_dir / "changelog-v1.2.3.md").write_text(
                "# Changelog - v1.2.3\n"
            )
            (changelog_dir / "changelog-v1.2.4-rc..1.md").write_text(
                "# Changelog - v1.2.4-rc..1\n"
            )
            (changelog_dir / "changelog-v01.2.4.md").write_text(
                "# Changelog - v01.2.4\n"
            )
            changelog_index.write_text(
                "# Changelog\n\n"
                "- [v1.2.3](./docs/changelog/changelog-v1.2.3.md)\n"
            )
            marketplace.write_text(
                json.dumps(
                    {
                        "name": "dev-agent-skills",
                        "owner": {"name": "Neplich"},
                        "metadata": {"version": "1.2.3"},
                        "plugins": [
                            {
                                "name": "engineer-agent",
                                "source": "./agents/engineer",
                                "skills": ["./skills/example"],
                            }
                        ],
                    }
                )
            )

            errors = []
            checker.validate_marketplace(root, errors)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn(
            "changelog-v1.2.4-rc..1.md: changelog filename must use changelog-v{SemVer}.md",
            rendered,
        )
        self.assertIn(
            "changelog-v01.2.4.md: changelog filename must use changelog-v{SemVer}.md",
            rendered,
        )

    def test_repository_contract_rejects_changelog_version_directory(self):
        checker = load_repository_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            marketplace = root / ".claude-plugin/marketplace.json"
            skill_doc = root / "agents/engineer/skills/example/SKILL.md"
            changelog_dir = root / "docs/changelog"
            changelog = changelog_dir / "changelog-v1.2.3.md"
            changelog_index = root / "CHANGELOG.md"
            marketplace.parent.mkdir(parents=True)
            skill_doc.parent.mkdir(parents=True)
            changelog.mkdir(parents=True)
            skill_doc.write_text(
                "---\n"
                "name: example\n"
                "description: Example skill\n"
                "---\n"
            )
            (changelog / "README.md").write_text("# Not a changelog file\n")
            changelog_index.write_text(
                "# Changelog\n\n"
                "- [v1.2.3](./docs/changelog/changelog-v1.2.3.md)\n"
            )
            marketplace.write_text(
                json.dumps(
                    {
                        "name": "dev-agent-skills",
                        "owner": {"name": "Neplich"},
                        "metadata": {"version": "1.2.3"},
                        "plugins": [
                            {
                                "name": "engineer-agent",
                                "source": "./agents/engineer",
                                "skills": ["./skills/example"],
                            }
                        ],
                    }
                )
            )

            errors = []
            checker.validate_marketplace(root, errors)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn(
            "changelog-v1.2.3.md: changelog entry must be a file",
            rendered,
        )

    def test_repository_contract_rejects_missing_root_changelog_index(self):
        checker = load_repository_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            marketplace = root / ".claude-plugin/marketplace.json"
            skill_doc = root / "agents/engineer/skills/example/SKILL.md"
            changelog = root / "docs/changelog/changelog-v0.1.3.md"
            changelog_index = root / "CHANGELOG.md"
            marketplace.parent.mkdir(parents=True)
            skill_doc.parent.mkdir(parents=True)
            changelog.parent.mkdir(parents=True)
            skill_doc.write_text(
                "---\n"
                "name: example\n"
                "description: Example skill\n"
                "---\n"
            )
            changelog.write_text("# Changelog - v0.1.3\n")
            changelog_index.write_text(
                "# Changelog\n\n"
                "- [v0.1.2](./docs/changelog/changelog-v0.1.2.md)\n"
            )
            marketplace.write_text(
                json.dumps(
                    {
                        "name": "dev-agent-skills",
                        "owner": {"name": "Neplich"},
                        "metadata": {"version": "0.1.3"},
                        "plugins": [
                            {
                                "name": "engineer-agent",
                                "source": "./agents/engineer",
                                "skills": ["./skills/example"],
                            }
                        ],
                    }
                )
            )

            errors = []
            checker.validate_marketplace(root, errors)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn(
            "CHANGELOG.md: must reference docs/changelog/changelog-v0.1.3.md",
            rendered,
        )

    def test_repository_contract_rejects_missing_implementation_plan_base_ref(self):
        checker = load_repository_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            plan = root / "docs/engineer/example/IMPLEMENTATION_PLAN.md"
            plan.parent.mkdir(parents=True)
            plan.write_text(
                "---\n"
                'feature: "example"\n'
                'version: "0.1.0"\n'
                'date: "2026-06-12"\n'
                'last_updated: "2026-06-12"\n'
                "---\n\n"
                "# Example Plan\n"
            )
            subprocess.run(["git", "init", "-b", "feature"], cwd=root, check=True)
            subprocess.run(["git", "add", plan.relative_to(root).as_posix()], cwd=root, check=True)

            errors = []
            checker.validate_implementation_plan_metadata(root, errors)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn("no base ref is available", rendered)

    def test_repository_contract_accepts_nested_implementation_plan_metadata(self):
        checker = load_repository_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            init_git_main(root)
            plan = root / "docs/engineer/chat-interface/history-search/IMPLEMENTATION_PLAN.md"
            prd = root / "docs/pm/chat-interface/history-search/PRD.md"
            trd = root / "docs/engineer/chat-interface/history-search/TRD.md"
            plan.parent.mkdir(parents=True)
            prd.parent.mkdir(parents=True)
            prd.write_text(
                "---\n"
                'feature: "history-search"\n'
                'feature_path: "chat-interface/history-search"\n'
                'parent_feature: "chat-interface"\n'
                'feature_level: "2"\n'
                'version: "1.0.0"\n'
                'date: "2026-06-23"\n'
                'last_updated: "2026-06-23"\n'
                "---\n\n"
                "# History Search PRD\n"
            )
            trd.write_text(
                "---\n"
                'feature: "history-search"\n'
                'feature_path: "chat-interface/history-search"\n'
                'parent_feature: "chat-interface"\n'
                'feature_level: "2"\n'
                'version: "0.1.0"\n'
                'date: "2026-06-23"\n'
                'last_updated: "2026-06-23"\n'
                'related_prd: "docs/pm/chat-interface/history-search/PRD.md"\n'
                "---\n\n"
                "# History Search TRD\n"
            )
            plan.write_text(
                "---\n"
                'feature: "history-search"\n'
                'feature_path: "chat-interface/history-search"\n'
                'parent_feature: "chat-interface"\n'
                'feature_level: "2"\n'
                'version: "0.1.0"\n'
                'date: "2026-06-23"\n'
                'last_updated: "2026-06-23"\n'
                'related_prd: "docs/pm/chat-interface/history-search/PRD.md"\n'
                'related_trd: "docs/engineer/chat-interface/history-search/TRD.md"\n'
                "---\n\n"
                "# History Search Plan\n"
            )
            subprocess.run(["git", "add", plan.relative_to(root).as_posix()], cwd=root, check=True)

            errors = []
            checker.validate_implementation_plan_metadata(root, errors)

        self.assertEqual([], errors)

    def test_repository_contract_rejects_changed_plan_with_missing_related_docs(self):
        checker = load_repository_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            init_git_main(root)
            plan = root / "docs/engineer/chat-interface/history-search/IMPLEMENTATION_PLAN.md"
            plan.parent.mkdir(parents=True)
            plan.write_text(
                "---\n"
                'feature: "history-search"\n'
                'feature_path: "chat-interface/history-search"\n'
                'parent_feature: "chat-interface"\n'
                'feature_level: "2"\n'
                'version: "0.1.0"\n'
                'date: "2026-06-23"\n'
                'last_updated: "2026-06-23"\n'
                'related_prd: "docs/pm/chat-interface/history-search/PRD.md"\n'
                'related_trd: "docs/engineer/chat-interface/history-search/TRD.md"\n'
                "---\n\n"
                "# History Search Plan\n"
            )
            subprocess.run(["git", "add", plan.relative_to(root).as_posix()], cwd=root, check=True)

            errors = []
            checker.validate_implementation_plan_metadata(root, errors)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn("frontmatter 'related_prd' must point to an existing file", rendered)
        self.assertIn("frontmatter 'related_trd' must point to an existing file", rendered)

    def test_repository_contract_rejects_changed_plan_without_feature_path_metadata(self):
        checker = load_repository_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            init_git_main(root)
            plan = root / "docs/engineer/chat-interface/history-search/IMPLEMENTATION_PLAN.md"
            plan.parent.mkdir(parents=True)
            plan.write_text(
                "---\n"
                'feature: "history-search"\n'
                'version: "0.1.0"\n'
                'date: "2026-06-23"\n'
                'last_updated: "2026-06-23"\n'
                "---\n\n"
                "# History Search Plan\n"
            )
            subprocess.run(["git", "add", plan.relative_to(root).as_posix()], cwd=root, check=True)

            errors = []
            checker.validate_implementation_plan_metadata(root, errors)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn("frontmatter 'feature_path' must be non-empty", rendered)
        self.assertIn("frontmatter 'parent_feature' must be non-empty", rendered)
        self.assertIn("frontmatter 'feature_level' must be non-empty", rendered)
        self.assertIn("frontmatter 'related_prd' must be non-empty", rendered)
        self.assertIn("frontmatter 'related_trd' must be non-empty", rendered)

    def test_repository_contract_accepts_deep_implementation_plan_path(self):
        checker = load_repository_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            init_git_main(root)
            plan = root / "docs/engineer/a/b/c/d/IMPLEMENTATION_PLAN.md"
            prd = root / "docs/pm/a/b/c/d/PRD.md"
            trd = root / "docs/engineer/a/b/c/d/TRD.md"
            plan.parent.mkdir(parents=True)
            prd.parent.mkdir(parents=True)
            prd.write_text(
                "---\n"
                'feature: "d"\n'
                'feature_path: "a/b/c/d"\n'
                'parent_feature: "a/b/c"\n'
                'feature_level: "4"\n'
                'version: "1.0.0"\n'
                'date: "2026-06-23"\n'
                'last_updated: "2026-06-23"\n'
                "---\n\n"
                "# Deep PRD\n"
            )
            trd.write_text(
                "---\n"
                'feature: "d"\n'
                'feature_path: "a/b/c/d"\n'
                'parent_feature: "a/b/c"\n'
                'feature_level: "4"\n'
                'version: "0.1.0"\n'
                'date: "2026-06-23"\n'
                'last_updated: "2026-06-23"\n'
                'related_prd: "docs/pm/a/b/c/d/PRD.md"\n'
                "---\n\n"
                "# Deep TRD\n"
            )
            plan.write_text(
                "---\n"
                'feature: "d"\n'
                'feature_path: "a/b/c/d"\n'
                'parent_feature: "a/b/c"\n'
                'feature_level: "4"\n'
                'version: "0.1.0"\n'
                'date: "2026-06-23"\n'
                'last_updated: "2026-06-23"\n'
                'related_prd: "docs/pm/a/b/c/d/PRD.md"\n'
                'related_trd: "docs/engineer/a/b/c/d/TRD.md"\n'
                "---\n\n"
                "# Too Deep Plan\n"
            )
            subprocess.run(["git", "add", plan.relative_to(root).as_posix()], cwd=root, check=True)

            errors = []
            checker.validate_implementation_plan_metadata(root, errors)

        self.assertEqual([], errors)

    def test_repository_contract_rejects_invalid_implementation_plan_path_segments(self):
        checker = load_repository_checker_module()

        invalid_paths = [
            "a/Bad_Segment",
            "foo-",
            "a--b",
        ]
        for feature_path in invalid_paths:
            with self.subTest(feature_path=feature_path):
                with tempfile.TemporaryDirectory() as temp_dir:
                    root = Path(temp_dir)
                    init_git_main(root)
                    plan = root / f"docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md"
                    plan.parent.mkdir(parents=True)
                    parent_feature = (
                        "/".join(feature_path.split("/")[:-1])
                        if "/" in feature_path
                        else "N/A"
                    )
                    feature = feature_path.split("/")[-1].lower().replace("_", "-")
                    plan.write_text(
                        "---\n"
                        f'feature: "{feature}"\n'
                        f'feature_path: "{feature_path}"\n'
                        f'parent_feature: "{parent_feature}"\n'
                        f'feature_level: "{len(feature_path.split("/"))}"\n'
                        'version: "0.1.0"\n'
                        'date: "2026-06-23"\n'
                        'last_updated: "2026-06-23"\n'
                        f'related_prd: "docs/pm/{feature_path}/PRD.md"\n'
                        f'related_trd: "docs/engineer/{feature_path}/TRD.md"\n'
                        "---\n\n"
                        "# Invalid Segment Plan\n"
                    )
                    subprocess.run(
                        ["git", "add", plan.relative_to(root).as_posix()],
                        cwd=root,
                        check=True,
                    )

                    errors = []
                    checker.validate_implementation_plan_metadata(root, errors)

                rendered = "\n".join(error.render(root) for error in errors)
                self.assertIn(
                    "implementation plan path must be docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md with one or more lowercase kebab-case segments",
                    rendered,
                )

    def test_repository_contract_rejects_changed_plan_related_doc_mismatch(self):
        checker = load_repository_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            init_git_main(root)
            plan = root / "docs/engineer/chat-interface/history-search/IMPLEMENTATION_PLAN.md"
            plan.parent.mkdir(parents=True)
            plan.write_text(
                "---\n"
                'feature: "history-search"\n'
                'feature_path: "chat-interface/history-search"\n'
                'parent_feature: "chat-interface"\n'
                'feature_level: "2"\n'
                'version: "0.1.0"\n'
                'date: "2026-06-23"\n'
                'last_updated: "2026-06-23"\n'
                'related_prd: "docs/pm/history-search/PRD.md"\n'
                'related_trd: "docs/engineer/history-search/TRD.md"\n'
                "---\n\n"
                "# History Search Plan\n"
            )
            subprocess.run(["git", "add", plan.relative_to(root).as_posix()], cwd=root, check=True)

            errors = []
            checker.validate_implementation_plan_metadata(root, errors)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn(
            "frontmatter 'related_prd' must be 'docs/pm/chat-interface/history-search/PRD.md'",
            rendered,
        )
        self.assertIn(
            "frontmatter 'related_trd' must be 'docs/engineer/chat-interface/history-search/TRD.md'",
            rendered,
        )

    def test_repository_contract_rejects_changed_plan_with_trd_related_prd_mismatch(self):
        checker = load_repository_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            init_git_main(root)
            prd = root / "docs/pm/chat-interface/history-search/PRD.md"
            trd = root / "docs/engineer/chat-interface/history-search/TRD.md"
            plan = root / "docs/engineer/chat-interface/history-search/IMPLEMENTATION_PLAN.md"
            prd.parent.mkdir(parents=True)
            plan.parent.mkdir(parents=True)
            prd.write_text(
                "---\n"
                'feature: "history-search"\n'
                'feature_path: "chat-interface/history-search"\n'
                'parent_feature: "chat-interface"\n'
                'feature_level: "2"\n'
                'version: "1.0.0"\n'
                'date: "2026-06-23"\n'
                'last_updated: "2026-06-23"\n'
                "---\n\n"
                "# History Search PRD\n"
            )
            trd.write_text(
                "---\n"
                'feature: "history-search"\n'
                'feature_path: "chat-interface/history-search"\n'
                'parent_feature: "chat-interface"\n'
                'feature_level: "2"\n'
                'version: "0.1.0"\n'
                'date: "2026-06-23"\n'
                'last_updated: "2026-06-23"\n'
                'related_prd: "docs/pm/history-search/PRD.md"\n'
                "---\n\n"
                "# History Search TRD\n"
            )
            plan.write_text(
                "---\n"
                'feature: "history-search"\n'
                'feature_path: "chat-interface/history-search"\n'
                'parent_feature: "chat-interface"\n'
                'feature_level: "2"\n'
                'version: "0.1.0"\n'
                'date: "2026-06-23"\n'
                'last_updated: "2026-06-23"\n'
                'related_prd: "docs/pm/chat-interface/history-search/PRD.md"\n'
                'related_trd: "docs/engineer/chat-interface/history-search/TRD.md"\n'
                "---\n\n"
                "# History Search Plan\n"
            )
            subprocess.run(["git", "add", plan.relative_to(root).as_posix()], cwd=root, check=True)

            errors = []
            checker.validate_implementation_plan_metadata(root, errors)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn(
            "frontmatter 'related_prd' must be 'docs/pm/chat-interface/history-search/PRD.md'",
            rendered,
        )

    def test_repository_contract_rejects_placeholder_author(self):
        checker = load_repository_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            prd = root / "docs/pm/example/PRD.md"
            prd.parent.mkdir(parents=True)
            prd.write_text(
                "---\n"
                'title: "Example PRD"\n'
                'author: "AI Assistant"\n'
                "---\n\n"
                "# Example PRD\n"
            )
            subprocess.run(["git", "init", "-b", "feature"], cwd=root, check=True)
            subprocess.run(
                ["git", "add", prd.relative_to(root).as_posix()],
                cwd=root,
                check=True,
            )

            errors = []
            checker.validate_formal_document_author(root, errors)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn("docs/pm/example/PRD.md", rendered)
        self.assertIn(
            "frontmatter 'author' must be a filled, non-placeholder traceable value",
            rendered,
        )

    def test_repository_contract_rejects_embedded_author_placeholder(self):
        checker = load_repository_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            prd = root / "docs/pm/example/PRD.md"
            prd.parent.mkdir(parents=True)
            prd.write_text(
                "---\n"
                'title: "Example PRD"\n'
                'author: "Neplich <agent platform name>"\n'
                "---\n\n"
                "# Example PRD\n"
            )
            subprocess.run(["git", "init", "-b", "feature"], cwd=root, check=True)
            subprocess.run(
                ["git", "add", prd.relative_to(root).as_posix()],
                cwd=root,
                check=True,
            )

            errors = []
            checker.validate_formal_document_author(root, errors)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn("docs/pm/example/PRD.md", rendered)
        self.assertIn(
            "frontmatter 'author' must be a filled, non-placeholder traceable value",
            rendered,
        )

    def test_repository_contract_rejects_single_part_author(self):
        checker = load_repository_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            prd = root / "docs/pm/example/PRD.md"
            prd.parent.mkdir(parents=True)
            prd.write_text(
                "---\n"
                'title: "Example PRD"\n'
                'author: "Codex"\n'
                "---\n\n"
                "# Example PRD\n"
            )
            subprocess.run(["git", "init", "-b", "feature"], cwd=root, check=True)
            subprocess.run(
                ["git", "add", prd.relative_to(root).as_posix()],
                cwd=root,
                check=True,
            )

            errors = []
            checker.validate_formal_document_author(root, errors)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn("docs/pm/example/PRD.md", rendered)
        self.assertIn(
            "frontmatter 'author' must be a filled, non-placeholder traceable value",
            rendered,
        )

    def test_repository_contract_accepts_custom_author_platform(self):
        checker = load_repository_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            prd = root / "docs/pm/example/PRD.md"
            prd.parent.mkdir(parents=True)
            prd.write_text(
                "---\n"
                'title: "Example PRD"\n'
                'author: "Neplich Custom Agent"\n'
                "---\n\n"
                "# Example PRD\n"
            )
            subprocess.run(["git", "init", "-b", "feature"], cwd=root, check=True)
            subprocess.run(
                ["git", "add", prd.relative_to(root).as_posix()],
                cwd=root,
                check=True,
            )

            errors = []
            checker.validate_formal_document_author(root, errors)

        self.assertEqual([], errors)


if __name__ == "__main__":
    unittest.main()
