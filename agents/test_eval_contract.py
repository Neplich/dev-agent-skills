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


class EvalContractTests(unittest.TestCase):
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
