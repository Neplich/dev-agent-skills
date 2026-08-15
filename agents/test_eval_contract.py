import importlib.util
import hashlib
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
    @staticmethod
    def valid_scenario() -> dict:
        return {
            "persona": "support engineer",
            "situation": "a customer-reported failure is under investigation",
            "trigger": "the failure started after a deploy",
            "goal": "identify the evidence-backed cause",
            "materials": ["application logs"],
            "constraints": ["do not modify production"],
            "success_criteria": ["a reviewer can trace the conclusion to evidence"],
        }

    @staticmethod
    def valid_runtime_isolation() -> dict:
        return {
            "processes": "not_used",
            "ports": "not_used",
            "database": "not_used",
            "browser": "not_used",
            "login_state": "not_used",
            "downloads": "not_used",
        }

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
                    "skill_dependencies": [],
                    "runtime_isolation": self.valid_runtime_isolation(),
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
                            "scenario": self.valid_scenario(),
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

    def test_eval_contract_allows_registered_manual_only_skill(self):
        checker = load_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            identity = "".join(
                f"- {key}: `{'a' * 64}`\n" for key in checker.FRESHNESS_KEYS
            )
            self.write_eval_fixture(
                root,
                "## Current Result\n\n- Evidence status: **PENDING**\n"
                "- Identity schema: `2`\n" + identity + "Overall result: BLOCKED\n",
            )
            skill_doc = root / "agents/docs/skills/manual-gen/SKILL.md"
            result_doc = root / "agents/docs/test/manual-gen/comparison.md"
            skill_doc.parent.mkdir(parents=True)
            result_doc.parent.mkdir(parents=True)
            skill_doc.write_text("# Manual Gen\n")
            result_doc.write_text("# Manual evaluation result\n")

            errors = checker.validate_all(root)

        self.assertEqual("\n".join(error.render(root) for error in errors), "")

    def test_eval_contract_requires_manual_only_result(self):
        checker = load_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self.write_eval_fixture(root, "# Comparison\n")
            skill_doc = root / "agents/docs/skills/manual-gen/SKILL.md"
            skill_doc.parent.mkdir(parents=True)
            skill_doc.write_text("# Manual Gen\n")

            errors = checker.validate_all(root)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn(
            "manual-only skill is missing evaluation result agents/docs/test/manual-gen/comparison.md",
            rendered,
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
                        "skill_dependencies": [],
                        "runtime_isolation": self.valid_runtime_isolation(),
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
                                "scenario": self.valid_scenario(),
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
                        "skill_dependencies": [],
                        "runtime_isolation": self.valid_runtime_isolation(),
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
                                "scenario": self.valid_scenario(),
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

    def test_eval_contract_validates_bounded_git_topology(self):
        checker = load_checker_module()
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            evals_path = self.write_eval_fixture(root, "# Comparison\n")
            workspace = evals_path.parent / "workspace/eval-001-baseline-evidence"
            patch = workspace / "release-evidence/change.patch"
            patch.parent.mkdir()
            (workspace / "a").write_text("new\n", encoding="utf-8")
            patch.write_text(
                "diff --git a/a b/a\n--- a/a\n+++ b/a\n@@ -1 +1 @@\n-old\n+new\n",
                encoding="utf-8",
            )
            metadata_path = workspace / "eval_metadata.json"
            metadata = json.loads(metadata_path.read_text())
            metadata["git_topology"] = {
                "base_ref": "v1.0.0",
                "target_ref": "release-head",
                "target_patch": "release-evidence/change.patch",
                "tags": [
                    {"name": "v1.0.0", "target": "base", "kind": "lightweight"},
                ],
                "refs": [
                    {"name": "refs/heads/release-evidence/v1.1.0", "target": "target"},
                ],
                "absent_refs": ["refs/tags/v1.1.0"],
            }
            metadata_path.write_text(json.dumps(metadata))
            valid = checker.validate_file(root, evals_path)

            metadata["git_topology"]["target_patch"] = "../setup.sh"
            metadata["git_topology"]["refs"][0]["name"] = "refs/tags/../escape"
            metadata["git_topology"]["absent_refs"] = ["refs/tags/v1.0.0"]
            metadata["git_topology"]["base_files"] = [
                {"source": "a", "path": "eval_metadata.json"},
            ]
            metadata_path.write_text(json.dumps(metadata))
            invalid = checker.validate_file(root, evals_path)

        self.assertEqual("\n".join(error.render(root) for error in valid), "")
        rendered = "\n".join(error.render(root) for error in invalid)
        self.assertIn("git_topology", rendered)
        self.assertIn("target_patch", rendered)
        self.assertIn("ref name", rendered)
        self.assertIn("both present and absent", rendered)
        self.assertIn("excluded from candidate fixtures", rendered)

    def test_eval_contract_does_not_validate_baseline_semantics(self):
        checker = load_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            evals_path = self.write_eval_fixture(
                root,
                "# Comparison\n\n"
                "- Latest result: PASS - reviewer accepted the comparison conclusion\n\n"
                "## Without Skill / Baseline\n\n"
                "- BLOCKED: without_skill baseline was not generated.\n"
                "- Baseline behavior is diagnostic only.\n"
                "- Baseline was blocked by unavailable runner.\n"
                "- The without_skill run was skipped.\n"
                "- without_skill run was not generated.\n",
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
                "- BLOCKED: without_skill baseline was not generated for this historical comparison.\n",
            )

            errors = checker.validate_file(root, evals_path)

        self.assertEqual("\n".join(error.render(root) for error in errors), "")

    def test_eval_contract_requires_complete_real_user_scenario(self):
        checker = load_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            evals_path = self.write_eval_fixture(root, "# Comparison\n")
            payload = json.loads(evals_path.read_text())
            del payload["evals"][0]["scenario"]["trigger"]
            evals_path.write_text(json.dumps(payload))

            errors = checker.validate_file(root, evals_path)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn("scenario.trigger must be a non-empty string", rendered)

    def test_eval_contract_rejects_prompt_that_leaks_eval_scaffolding(self):
        checker = load_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            evals_path = self.write_eval_fixture(root, "# Comparison\n")
            payload = json.loads(evals_path.read_text())
            payload["evals"][0]["prompt"] = (
                "用户说：请按 assertions 对比 with_skill 和 without_skill。"
            )
            evals_path.write_text(json.dumps(payload, ensure_ascii=False))

            errors = checker.validate_file(root, evals_path)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn("prompt contains forbidden eval scaffolding", rendered)

    def test_eval_contract_rejects_metadata_prompt_and_unknown_runtime(self):
        checker = load_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            evals_path = self.write_eval_fixture(root, "# Comparison\n")
            metadata = evals_path.parent / "workspace/eval-001-baseline-evidence/eval_metadata.json"
            payload = json.loads(metadata.read_text())
            payload["prompt"] = "duplicated prompt"
            payload["skill_dependencies"] = ["../../outside"]
            payload["runtime_isolation"]["browser"] = "unknown"
            metadata.write_text(json.dumps(payload))

            errors = checker.validate_file(root, evals_path)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn("prompt must only be defined in evals.json", rendered)
        self.assertIn("skill_dependencies contains unsafe path", rendered)
        self.assertIn("runtime_isolation.browser", rendered)

    def test_eval_contract_rejects_answer_bearing_nested_readme(self):
        checker = load_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            evals_path = self.write_eval_fixture(root, "# Comparison\n")
            workspace = evals_path.parent / "workspace/eval-001-baseline-evidence"
            (workspace / "service").mkdir()
            readme = workspace / "service/README.md"
            readme.write_text("Expected behavior: dispatcher should return PASS.")

            errors = checker.validate_file(root, evals_path)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn("README contains high-confidence answer guidance", rendered)

    def test_eval_contract_allows_host_facts_in_nested_readme(self):
        checker = load_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            evals_path = self.write_eval_fixture(root, "# Comparison\n")
            workspace = evals_path.parent / "workspace/eval-001-baseline-evidence"
            (workspace / "service").mkdir()
            (workspace / "service/README.md").write_text(
                "The checkout service listens on port 8080 and owns payment requests."
            )

            errors = checker.validate_file(root, evals_path)

        self.assertEqual("\n".join(error.render(root) for error in errors), "")

    def test_eval_contract_rejects_answer_guidance_in_root_readme(self):
        checker = load_checker_module()
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            evals_path = self.write_eval_fixture(root, "# Comparison\n")
            workspace = evals_path.parent / "workspace/eval-001-baseline-evidence"
            (workspace / "README.md").write_text(
                "Expected behavior: return the scored answer.\n", encoding="utf-8",
            )

            errors = checker.validate_file(root, evals_path)

        self.assertIn(
            "README contains high-confidence answer guidance",
            "\n".join(error.render(root) for error in errors),
        )

    def test_eval_contract_rejects_high_confidence_fixture_markers(self):
        checker = load_checker_module()
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            evals_path = self.write_eval_fixture(root, "# Comparison\n")
            workspace = evals_path.parent / "workspace/eval-001-baseline-evidence"
            (workspace / "package.json").write_text(
                json.dumps({"description": "Existing project update eval workspace"})
            )
            (workspace / "PRD.md").write_text(
                '---\nauthor: "PM Fixture"\ngenerated_by: "fixture"\n---\n'
                'changes: "Initial fixture"\n'
            )

            errors = checker.validate_file(root, evals_path)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn("package.json contains high-confidence eval marker", rendered)
        self.assertIn("document contains high-confidence fixture provenance", rendered)

    def test_eval_contract_allows_ordinary_business_evaluation_and_fixture_words(self):
        checker = load_checker_module()
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            evals_path = self.write_eval_fixture(root, "# Comparison\n")
            workspace = evals_path.parent / "workspace/eval-001-baseline-evidence"
            (workspace / "package.json").write_text(
                json.dumps({"description": "Evaluate fixture mounting hardware inventory"})
            )
            (workspace / "facts.md").write_text(
                "The customer evaluation covers production lighting fixtures.\n"
            )

            errors = checker.validate_file(root, evals_path)

        self.assertEqual("\n".join(error.render(root) for error in errors), "")

    def test_eval_contract_requires_explicit_cross_skill_dependency(self):
        checker = load_checker_module()
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            evals_path = root / "agents/qa/test/bug-analyzer/evals/evals.json"
            workspace = evals_path.parent / "workspace/eval-001-baseline-evidence"
            skill_doc = root / "agents/qa/skills/bug-analyzer/SKILL.md"
            workspace.mkdir(parents=True)
            skill_doc.parent.mkdir(parents=True)
            (workspace / "comparison.md").write_text("# Comparison\n")
            (workspace / "eval_metadata.json").write_text(json.dumps({
                "eval_id": "eval-001-baseline-evidence",
                "skill_dependencies": [],
                "runtime_isolation": self.valid_runtime_isolation(),
            }))
            evals_path.write_text(json.dumps({
                "schema_version": "1.0", "agent": "qa", "skill_name": "bug-analyzer",
                "evals": [{
                    "id": "eval-001-baseline-evidence", "name": "baseline-evidence",
                    "description": "Baseline evidence fixture", "scenario": self.valid_scenario(),
                    "prompt": "Run the eval", "workspace": "workspace/eval-001-baseline-evidence",
                    "expected_output": "A result", "assertions": [{
                        "id": "has_result", "description": "Has a result", "text": "Result is present",
                    }],
                }],
            }))
            skill_doc.write_text(
                "Read agents/product_manager/skills/idea-to-spec/_internal/_shared/skill-map.md.\n"
            )
            dependency = root / "agents/product_manager/skills/idea-to-spec/SKILL.md"
            dependency.parent.mkdir(parents=True)
            dependency.write_text("---\nname: idea-to-spec\n---\n")
            metadata = evals_path.parent / "workspace/eval-001-baseline-evidence/eval_metadata.json"

            missing = checker.validate_file(root, evals_path)
            payload = json.loads(metadata.read_text())
            payload["skill_dependencies"] = ["agents/product_manager/skills/idea-to-spec"]
            metadata.write_text(json.dumps(payload))
            covered = checker.validate_file(root, evals_path)

        self.assertIn(
            "missing explicit cross-skill dependencies",
            "\n".join(error.render(root) for error in missing),
        )
        self.assertEqual("\n".join(error.render(root) for error in covered), "")

    def test_issue_246_inventory_matches_frozen_baseline(self):
        checker = load_checker_module()
        errors = checker.validate_migration_inventory(checker.repo_root())

        self.assertEqual(
            "\n".join(error.render(checker.repo_root()) for error in errors),
            "",
        )

    def test_only_pending_frozen_eval_skips_strict_contract_checks(self):
        checker = load_checker_module()
        identity = ("engineer", "debugger", "eval-001-baseline-evidence")

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            evals_path = self.write_eval_fixture(root, "# Comparison\n")
            payload = json.loads(evals_path.read_text())
            del payload["evals"][0]["scenario"]
            evals_path.write_text(json.dumps(payload, ensure_ascii=False))
            workspace = evals_path.parent / "workspace/eval-001-baseline-evidence"
            metadata = workspace / "eval_metadata.json"
            metadata_payload = json.loads(metadata.read_text())
            del metadata_payload["runtime_isolation"]
            metadata.write_text(json.dumps(metadata_payload))
            (workspace / "service").mkdir()
            (workspace / "service/README.md").write_text(
                "Expected behavior: dispatcher should return PASS."
            )

            post_freeze_errors = checker.validate_file(
                root, evals_path, pending_identities=set(),
            )
            pending_frozen_errors = checker.validate_file(
                root, evals_path, pending_identities={identity},
            )

        strict_messages = "\n".join(error.render(root) for error in post_freeze_errors)
        compatibility_messages = "\n".join(
            error.render(root) for error in pending_frozen_errors
        )
        for message in (
            "scenario must be an object",
            "runtime_isolation must be an object",
            "README contains high-confidence answer guidance",
        ):
            self.assertIn(message, strict_messages)
            self.assertNotIn(message, compatibility_messages)

    def test_inventory_recomputes_frozen_pointer_and_hashes_from_commit(self):
        checker = load_checker_module()
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            subprocess.run(["git", "init", "-q", "-b", "main"], cwd=root, check=True)
            evals = root / "agents/qa/test/example/evals/evals.json"
            metadata = root / "agents/qa/test/example/evals/workspace/eval-001/eval_metadata.json"
            comparison = metadata.parent / "comparison.md"
            metadata.parent.mkdir(parents=True)
            item = {"id": "eval-001-example", "prompt": "help"}
            evals.write_text(json.dumps({"evals": [item]}), encoding="utf-8")
            metadata.write_text('{"eval_id":"eval-001-example"}\n', encoding="utf-8")
            comparison.write_text("Overall result: PASS\n", encoding="utf-8")
            subprocess.run(["git", "add", "."], cwd=root, check=True)
            subprocess.run(
                ["git", "-c", "user.name=Test", "-c", "user.email=test@example.com",
                 "commit", "-q", "-m", "freeze"], cwd=root, check=True,
            )
            commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
            sha = lambda data: hashlib.sha256(data).hexdigest()
            record = {
                "old_eval_id": "eval-001-example", "old_eval_index": 0,
                "old_eval_path": "agents/qa/test/example/evals/evals.json#/evals/0",
                "old_eval_sha256": sha(json.dumps(item, sort_keys=True, separators=(",", ":")).encode()),
                "metadata_path": metadata.relative_to(root).as_posix(),
                "metadata_sha256_at_freeze": sha(metadata.read_bytes()),
                "comparison_path": comparison.relative_to(root).as_posix(),
                "comparison_sha256_before_stale": sha(comparison.read_bytes()),
            }

            self.assertEqual([], checker.validate_frozen_record(root, commit, record))
            record["old_eval_sha256"] = "0" * 64
            errors = checker.validate_frozen_record(root, commit, record)

        self.assertIn("old_eval_sha256 does not match frozen commit", errors[0].message)

    def test_inventory_requires_real_frozen_commit_and_exact_source_contract(self):
        checker = load_checker_module()
        path = checker.repo_root() / checker.MIGRATION_INVENTORY
        errors = []

        checker.validate_inventory_freeze_contract(
            checker.repo_root(), path,
            {"frozen_from_git_commit": "", "source_contract": {}}, errors,
        )
        checker.validate_inventory_freeze_contract(
            checker.repo_root(), path,
            {"frozen_from_git_commit": "f" * 40,
             "source_contract": checker.FROZEN_SOURCE_CONTRACT}, errors,
        )

        rendered = "\n".join(error.message for error in errors)
        self.assertIn("frozen_from_git_commit must be a real 40-hex commit", rendered)
        self.assertIn("source_contract must exactly match the frozen scan contract", rendered)

    def test_fresh_comparison_requires_exact_v2_identity_without_legacy_fields(self):
        checker = load_checker_module()
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            evals_path = self.write_eval_fixture(root, "placeholder")
            workspace = evals_path.parent / "workspace/eval-001-baseline-evidence"
            identity = {"identity_schema": 2, **{
                key: hashlib.sha256(key.encode()).hexdigest()
                for key in checker.FRESHNESS_KEYS
            }}
            checker.current_identity_v2 = lambda _definition, **_kwargs: identity
            comparison = workspace / "comparison.md"
            base = (
                "## Current Result\n\n- Evidence status: **FRESH**\n"
                "- Preflight status: **PASS**\n- Judge: fresh judge completed.\n"
                "- Identity schema: `2`\n"
                + "".join(f"- {key}: `{identity[key]}`\n" for key in checker.FRESHNESS_KEYS)
                + "- Behavior result: **PASS**\n- Coverage result: **FULL**\n"
                "Overall result: PASS\n"
            )
            comparison.write_text(base, encoding="utf-8")
            errors = []
            checker.validate_fresh_comparison_identity(
                root, comparison, "engineer", "debugger",
                "eval-001-baseline-evidence", errors,
            )
            self.assertEqual(errors, [])

            comparison.write_text(
                base + f"- Prompt SHA-256: `{'p' * 64}`\n"
                f"- Skill overlay SHA-256: `{'s' * 64}`\n",
                encoding="utf-8",
            )
            audit_errors = []
            checker.validate_fresh_comparison_identity(
                root, comparison, "engineer", "debugger",
                "eval-001-baseline-evidence", audit_errors,
            )
            self.assertEqual(audit_errors, [])

            for label, altered in (
                ("missing schema", base.replace("- Identity schema: `2`\n", "")),
                ("wrong field", base.replace(identity[checker.FRESHNESS_KEYS[0]], "f" * 64)),
                ("legacy field", base + f"- Executor SHA-256: `{'e' * 64}`\n"),
            ):
                with self.subTest(label=label):
                    comparison.write_text(altered, encoding="utf-8")
                    errors = []
                    checker.validate_fresh_comparison_identity(
                        root, comparison, "engineer", "debugger",
                        "eval-001-baseline-evidence", errors,
                    )
                    self.assertTrue(any("fresh comparison input identity is stale" in error.message
                                        for error in errors))

    def test_fresh_comparison_allows_stale_word_in_eval_slug(self):
        checker = load_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            comparison = Path(temp_dir) / "comparison.md"
            comparison.write_text(
                "## Current Result\n\n"
                "- Evidence status: **FRESH**\n"
                "- Preflight status: **PASS**\n"
                "- Judge: fresh judge completed.\n"
                "- Fixture version/source: workspace/eval-002-audit-stale-doc\n"
                "- Behavior result: **PASS**\n"
                "- Coverage result: **FULL**\n"
                "Overall result: PASS\n",
                encoding="utf-8",
            )

            self.assertTrue(checker._comparison_has_fresh_evidence(comparison))

    def test_v2_freshness_check_does_not_query_git(self):
        checker = load_checker_module()
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            evals_path = self.write_eval_fixture(root, "placeholder")
            workspace = evals_path.parent / "workspace/eval-001-baseline-evidence"
            identity = {"identity_schema": 2, **{
                key: hashlib.sha256(key.encode()).hexdigest()
                for key in checker.FRESHNESS_KEYS
            }}
            checker.current_identity_v2 = lambda _definition, **_kwargs: identity
            comparison = workspace / "comparison.md"
            comparison.write_text(
                "## Current Result\n\n- Evidence status: **FRESH**\n"
                "- Identity schema: `2`\n"
                + "".join(f"- {key}: `{identity[key]}`\n" for key in checker.FRESHNESS_KEYS),
                encoding="utf-8",
            )
            original_run = subprocess.run
            subprocess.run = lambda *_args, **_kwargs: (_ for _ in ()).throw(
                AssertionError("freshness checker must not query Git")
            )
            try:
                errors = []
                checker.validate_fresh_comparison_identity(
                    root, comparison, "engineer", "debugger",
                    "eval-001-baseline-evidence", errors,
                )
            finally:
                subprocess.run = original_run
        self.assertEqual(errors, [])

    def test_validate_all_rejects_post_freeze_fresh_stale_digest(self):
        checker = load_checker_module()
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            identity = {key: hashlib.sha256(key.encode()).hexdigest()
                        for key in checker.FRESHNESS_KEYS}
            comparison_text = (
                "## Current Result\n\n- Evidence status: **FRESH**\n"
                "- Preflight status: **PASS**\n- Judge: fresh judge completed.\n"
                "- Identity schema: `2`\n"
                + "".join(f"- {key}: `{value}`\n" for key, value in identity.items())
                + "- Behavior result: **PASS**\n- Coverage result: **FULL**\nOverall result: PASS\n"
            )
            evals_path = self.write_eval_fixture(root, comparison_text)
            current = {"identity_schema": 2, **identity}
            current[checker.FRESHNESS_KEYS[0]] = "f" * 64
            checker.current_identity_v2 = lambda _definition, **_kwargs: current

            errors = checker.validate_all(root)

        self.assertTrue(any("fresh comparison input identity is stale" in error.message
                            for error in errors))

    def test_runner_audit_requires_all_nine_fields_per_surface(self):
        checker = load_checker_module()
        inventory = json.loads((checker.repo_root() / checker.MIGRATION_INVENTORY).read_text())
        audit = inventory["runner_audit"]
        del audit["surfaces"][0]["fields"]["judge_freshness"]
        errors = []

        checker.validate_runner_audit(
            audit, checker.repo_root() / checker.MIGRATION_INVENTORY, errors,
            all_evals_complete=False,
        )

        self.assertIn("must contain exactly the nine audit fields", errors[0].message)

    def test_runner_audit_rejects_missing_surface_path_and_forged_complete_evidence(self):
        checker = load_checker_module()
        inventory = json.loads((checker.repo_root() / checker.MIGRATION_INVENTORY).read_text())
        audit = inventory["runner_audit"]
        audit["surfaces"][0]["path"] = "missing/runner.py"
        forged = audit["surfaces"][1]
        forged["migration_status"] = "complete"
        forged["fields"] = {
            name: {"status": "pass", "evidence": "looks good"}
            for name in checker.RUNNER_AUDIT_FIELDS
        }
        errors = []

        checker.validate_runner_audit(
            audit, checker.repo_root() / checker.MIGRATION_INVENTORY, errors,
            all_evals_complete=False,
        )

        rendered = "\n".join(error.message for error in errors)
        self.assertIn("surfaces must match the exact runner inventory", rendered)
        self.assertIn("surface path does not exist", rendered)
        self.assertIn("complete evidence lacks executor anchor", rendered)

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

    def test_repository_contract_requires_plugin_manifest_name_and_version(self):
        checker = load_repository_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            marketplace = root / ".claude-plugin/marketplace.json"
            plugin_manifest = root / "agents/engineer/.claude-plugin/plugin.json"
            skill_doc = root / "agents/engineer/skills/example/SKILL.md"
            changelog = root / "docs/changelog/changelog-v1.2.3.md"
            changelog_index = root / "CHANGELOG.md"
            marketplace.parent.mkdir(parents=True)
            skill_doc.parent.mkdir(parents=True)
            changelog.parent.mkdir(parents=True)
            plugin_manifest.parent.mkdir(parents=True)
            skill_doc.write_text(
                "---\n"
                "name: example\n"
                "description: Example skill\n"
                "---\n"
            )
            changelog.write_text("# Changelog - v1.2.3\n")
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
            missing_rendered = "\n".join(error.render(root) for error in errors)

            plugin_manifest.write_text(
                json.dumps(
                    {
                        "name": "wrong-agent",
                        "version": "1.2.2",
                    }
                )
            )
            errors = []
            checker.validate_marketplace(root, errors)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn(
            "agents/engineer/.claude-plugin/plugin.json: plugin source must contain .claude-plugin/plugin.json",
            missing_rendered,
        )
        self.assertIn(
            "name must match marketplace plugins[0].name 'engineer-agent'",
            rendered,
        )
        self.assertIn(
            "version must match marketplace metadata.version '1.2.3'",
            rendered,
        )

    def test_repository_contract_same_day_exception_uses_frontmatter_changelog_only(self):
        checker = load_repository_checker_module()

        content = (
            "---\n"
            'feature: "history-search"\n'
            'version: "0.3.5"\n'
            'last_updated: "2026-07-05"\n'
            "release_metadata:\n"
            "  changelog:\n"
            '    - version: "0.3.5"\n'
            '      date: "2026-07-05"\n'
            "release_refs:\n"
            '  - version: "0.3.5"\n'
            '    date: "2026-07-05"\n'
            "changelog:\n"
            '  - version: "0.3.4"\n'
            '    date: "2026-07-05"\n'
            "---\n\n"
            "```yaml\n"
            '- version: "0.3.5"\n'
            '  date: "2026-07-05"\n'
            "```\n"
        )

        self.assertFalse(
            checker.markdown_frontmatter_changelog_has_version_date(
                content,
                "0.3.5",
                "2026-07-05",
            )
        )

        content_with_changelog_entry = content.replace(
            '  - version: "0.3.4"\n',
            '  - version: "0.3.5"\n',
        )
        self.assertTrue(
            checker.markdown_frontmatter_changelog_has_version_date(
                content_with_changelog_entry,
                "0.3.5",
                "2026-07-05",
            )
        )

    def test_repository_contract_orders_prerelease_changelog_versions(self):
        checker = load_repository_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            marketplace = root / ".claude-plugin/marketplace.json"
            plugin_manifest = root / "agents/engineer/.claude-plugin/plugin.json"
            skill_doc = root / "agents/engineer/skills/example/SKILL.md"
            changelog_dir = root / "docs/changelog"
            changelog_index = root / "CHANGELOG.md"
            marketplace.parent.mkdir(parents=True)
            plugin_manifest.parent.mkdir(parents=True)
            skill_doc.parent.mkdir(parents=True)
            changelog_dir.mkdir(parents=True)
            skill_doc.write_text(
                "---\n"
                "name: example\n"
                "description: Example skill\n"
                "---\n"
            )
            plugin_manifest.write_text(
                json.dumps(
                    {
                        "name": "engineer-agent",
                        "version": "1.2.3-rc.10",
                    }
                )
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
                'status: "Pending Confirmation"\n'
                'date: "2026-06-23"\n'
                'last_updated: "2026-06-23"\n'
                'implementation_scope: "initial-rollout"\n'
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
        self.assertIn("frontmatter 'implementation_scope' must be non-empty", rendered)
        self.assertIn("frontmatter 'related_prd' must be non-empty", rendered)
        self.assertIn("frontmatter 'related_trd' must be non-empty", rendered)

    def _write_history_search_plan_fixture(
        self,
        root: Path,
        plan_extra_frontmatter: str = "",
        implementation_scope: str = "initial-rollout",
        status: str = "Pending Confirmation",
        last_updated: str = "2026-06-23",
        body: str = "# History Search Plan\n",
    ) -> Path:
        plan = root / "docs/engineer/chat-interface/history-search/IMPLEMENTATION_PLAN.md"
        prd = root / "docs/pm/chat-interface/history-search/PRD.md"
        trd = root / "docs/engineer/chat-interface/history-search/TRD.md"
        plan.parent.mkdir(parents=True, exist_ok=True)
        prd.parent.mkdir(parents=True, exist_ok=True)
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
            f'status: "{status}"\n'
            'date: "2026-06-23"\n'
            f'last_updated: "{last_updated}"\n'
            f'implementation_scope: "{implementation_scope}"\n'
            'related_prd: "docs/pm/chat-interface/history-search/PRD.md"\n'
            'related_trd: "docs/engineer/chat-interface/history-search/TRD.md"\n'
            f"{plan_extra_frontmatter}"
            "---\n\n"
            f"{body}"
        )
        return plan

    def test_repository_contract_rejects_changed_plan_with_invalid_implementation_scope(self):
        checker = load_repository_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            init_git_main(root)
            plan = self._write_history_search_plan_fixture(
                root, implementation_scope="Bad Scope"
            )
            subprocess.run(["git", "add", plan.relative_to(root).as_posix()], cwd=root, check=True)

            errors = []
            checker.validate_implementation_plan_metadata(root, errors)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn(
            "frontmatter 'implementation_scope' must be a lower kebab-case scope",
            rendered,
        )

    def test_repository_contract_requires_previous_plan_archive_when_base_has_history_only(self):
        checker = load_repository_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            init_git_main(root)
            plan = self._write_history_search_plan_fixture(
                root, implementation_scope="search-filters-v2"
            )
            archive = (
                root
                / "docs/engineer/chat-interface/history-search"
                / "archive/IMPLEMENTATION_PLAN-initial-rollout.md"
            )
            archive.parent.mkdir(parents=True)
            archive.write_text("# Archived Plan\n")
            subprocess.run(["git", "add", plan.relative_to(root).as_posix()], cwd=root, check=True)

            errors = []
            checker.validate_implementation_plan_metadata(root, errors)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn(
            "frontmatter 'previous_plan_archive' must be non-empty because this "
            "feature_path already has archived plan history; a new active plan "
            "must link to the previous archive",
            rendered,
        )

    def test_repository_contract_rejects_frontmatter_only_update_for_implemented_base(self):
        checker = load_repository_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            subprocess.run(["git", "init", "-b", "main"], cwd=root, check=True)
            plan = self._write_history_search_plan_fixture(
                root,
                implementation_scope="initial-rollout",
                status="Implemented",
            )
            subprocess.run(["git", "add", "-A"], cwd=root, check=True)
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
            # Even an administrative-only change must not leave a completed
            # plan at the active entry.
            plan = self._write_history_search_plan_fixture(
                root,
                status="Implemented",
                last_updated="2026-06-24",
            )
            subprocess.run(["git", "add", plan.relative_to(root).as_posix()], cwd=root, check=True)

            errors = []
            checker.validate_implementation_plan_metadata(root, errors)

        self.assertEqual(1, len(errors))
        self.assertIn(
            "active implementation plan status must not be 'Implemented' or 'Archived'",
            errors[0].message,
        )

    def test_repository_contract_rejects_missing_backlink_for_settled_base_plan(self):
        checker = load_repository_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            # An Implemented active plan already exists on the main baseline.
            # Replacing its body must link the new round to a faithful archive.
            subprocess.run(["git", "init", "-b", "main"], cwd=root, check=True)
            plan = self._write_history_search_plan_fixture(
                root,
                implementation_scope="initial-rollout",
                status="Implemented",
            )
            subprocess.run(["git", "add", "-A"], cwd=root, check=True)
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
            plan = self._write_history_search_plan_fixture(
                root,
                implementation_scope="search-filters-v2",
                status="Pending Confirmation",
                body="# History Search Filters V2 Plan\n",
            )
            subprocess.run(["git", "add", plan.relative_to(root).as_posix()], cwd=root, check=True)

            errors = []
            checker.validate_implementation_plan_metadata(root, errors)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn(
            "frontmatter 'previous_plan_archive' must be non-empty because the "
            "base round for this active plan is already settled and its content "
            "has changed; link the new plan to an archive that faithfully preserves it",
            rendered,
        )

    def test_repository_contract_accepts_previous_plan_archive_linkage_when_archive_exists(self):
        checker = load_repository_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            init_git_main(root)
            plan = self._write_history_search_plan_fixture(
                root,
                'previous_plan_archive: "docs/engineer/chat-interface/history-search/'
                'archive/IMPLEMENTATION_PLAN-initial-rollout.md"\n',
                implementation_scope="search-filters-v2",
            )
            archive = (
                root
                / "docs/engineer/chat-interface/history-search"
                / "archive/IMPLEMENTATION_PLAN-initial-rollout.md"
            )
            archive.parent.mkdir(parents=True)
            archive.write_text("# Archived Plan\n")
            subprocess.run(["git", "add", plan.relative_to(root).as_posix()], cwd=root, check=True)

            errors = []
            checker.validate_implementation_plan_metadata(root, errors)

        self.assertEqual([], errors)

    def test_repository_contract_accepts_missing_previous_plan_archive_without_archives(self):
        checker = load_repository_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            init_git_main(root)
            plan = self._write_history_search_plan_fixture(root)
            archive_dir = (
                root
                / "docs/engineer/chat-interface/history-search"
                / "archive"
            )
            archive_dir.mkdir(parents=True)
            subprocess.run(["git", "add", plan.relative_to(root).as_posix()], cwd=root, check=True)

            errors = []
            checker.validate_implementation_plan_metadata(root, errors)

        self.assertEqual([], errors)

    def test_repository_contract_accepts_missing_previous_plan_archive_for_unchanged_plan(self):
        checker = load_repository_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            subprocess.run(["git", "init", "-b", "main"], cwd=root, check=True)
            self._write_history_search_plan_fixture(
                root, implementation_scope="search-filters-v2"
            )
            subprocess.run(["git", "add", "-A"], cwd=root, check=True)
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
            archive = (
                root
                / "docs/engineer/chat-interface/history-search"
                / "archive/IMPLEMENTATION_PLAN-initial-rollout.md"
            )
            archive.parent.mkdir(parents=True)
            archive.write_text("# Archived Plan\n")
            subprocess.run(
                ["git", "add", archive.relative_to(root).as_posix()], cwd=root, check=True
            )

            errors = []
            checker.validate_implementation_plan_metadata(root, errors)

        self.assertEqual([], errors)

    def _write_history_search_archive_fixture(
        self,
        root: Path,
        feature_path_line: str = 'feature_path: "chat-interface/history-search"\n',
        related_prd_line: str = 'related_prd: "docs/pm/chat-interface/history-search/PRD.md"\n',
        parent_feature_line: str = 'parent_feature: "chat-interface"\n',
        feature_level_line: str = 'feature_level: "2"\n',
    ) -> Path:
        archive = (
            root
            / "docs/engineer/chat-interface/history-search"
            / "archive/IMPLEMENTATION_PLAN-initial-rollout.md"
        )
        archive.parent.mkdir(parents=True)
        archive.write_text(
            "---\n"
            'feature: "history-search"\n'
            f"{feature_path_line}"
            f"{parent_feature_line}"
            f"{feature_level_line}"
            'implementation_scope: "initial-rollout"\n'
            'status: "Archived"\n'
            'archived_at: "2026-06-25"\n'
            'archive_approved_by: "Maintainer"\n'
            'source_plan: "docs/engineer/chat-interface/history-search/IMPLEMENTATION_PLAN.md"\n'
            f"{related_prd_line}"
            'related_trd: "docs/engineer/chat-interface/history-search/TRD.md"\n'
            "---\n\n"
            "# Archived History Search Plan\n"
        )
        return archive

    def test_repository_contract_rejects_archive_plan_feature_path_mismatch(self):
        checker = load_repository_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            init_git_main(root)
            archive = self._write_history_search_archive_fixture(
                root, 'feature_path: "billing"\n'
            )
            subprocess.run(
                ["git", "add", archive.relative_to(root).as_posix()], cwd=root, check=True
            )

            errors = []
            checker.validate_archive_plans(root, errors)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn(
            "frontmatter 'feature_path' must match directory path 'chat-interface/history-search'",
            rendered,
        )

    def test_repository_contract_rejects_archive_plan_empty_feature_path(self):
        checker = load_repository_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            init_git_main(root)
            archive = self._write_history_search_archive_fixture(
                root, feature_path_line='feature_path: ""\n'
            )
            subprocess.run(
                ["git", "add", archive.relative_to(root).as_posix()], cwd=root, check=True
            )

            errors = []
            checker.validate_archive_plans(root, errors)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn("frontmatter 'feature_path' must be non-empty", rendered)

    def test_repository_contract_rejects_archive_plan_omitting_feature_metadata(self):
        checker = load_repository_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            init_git_main(root)
            archive = self._write_history_search_archive_fixture(
                root,
                feature_path_line="",
                parent_feature_line="",
                feature_level_line="",
            )
            subprocess.run(
                ["git", "add", archive.relative_to(root).as_posix()], cwd=root, check=True
            )

            errors = []
            checker.validate_archive_plans(root, errors)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn("frontmatter 'feature_path' must be non-empty", rendered)
        self.assertIn("frontmatter 'parent_feature' must be non-empty", rendered)
        self.assertIn("frontmatter 'feature_level' must be non-empty", rendered)

    def test_repository_contract_rejects_archive_plan_empty_related_prd(self):
        checker = load_repository_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            init_git_main(root)
            archive = self._write_history_search_archive_fixture(
                root, related_prd_line='related_prd: ""\n'
            )
            subprocess.run(
                ["git", "add", archive.relative_to(root).as_posix()], cwd=root, check=True
            )

            errors = []
            checker.validate_archive_plans(root, errors)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn(
            "frontmatter 'related_prd' must be 'docs/pm/chat-interface/history-search/PRD.md'",
            rendered,
        )

    def test_repository_contract_accepts_archive_plan_with_consistent_feature_metadata(self):
        checker = load_repository_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            init_git_main(root)
            archive = self._write_history_search_archive_fixture(root)
            subprocess.run(
                ["git", "add", archive.relative_to(root).as_posix()], cwd=root, check=True
            )

            errors = []
            checker.validate_archive_plans(root, errors)

        self.assertEqual([], errors)

    def test_repository_contract_rejects_misnamed_files_in_archive_directory(self):
        checker = load_repository_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            init_git_main(root)
            archive_dir = (
                root
                / "docs/engineer/chat-interface/history-search"
                / "archive"
            )
            archive_dir.mkdir(parents=True)
            underscore = archive_dir / "IMPLEMENTATION_PLAN-full_refund.md"
            underscore.write_text("# Misnamed Archive\n")
            unrelated = archive_dir / "BAD.md"
            unrelated.write_text("# Unrelated File\n")
            subprocess.run(
                [
                    "git",
                    "add",
                    underscore.relative_to(root).as_posix(),
                    unrelated.relative_to(root).as_posix(),
                ],
                cwd=root,
                check=True,
            )

            errors = []
            checker.validate_archive_plans(root, errors)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertEqual(2, len(errors))
        self.assertIn("IMPLEMENTATION_PLAN-full_refund.md", rendered)
        self.assertIn("BAD.md", rendered)
        self.assertIn(
            "archive only allows IMPLEMENTATION_PLAN-<scope>.md with a lower kebab-case scope",
            rendered,
        )

    def test_repository_contract_accepts_archive_named_feature_path_documents(self):
        checker = load_repository_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            init_git_main(root)
            plan = root / "docs/engineer/payments/archive/IMPLEMENTATION_PLAN.md"
            trd = root / "docs/engineer/payments/archive/TRD.md"
            plan.parent.mkdir(parents=True)
            plan.write_text("# Active Plan\n")
            trd.write_text("# TRD\n")
            subprocess.run(
                ["git", "add", plan.relative_to(root).as_posix()], cwd=root, check=True
            )
            subprocess.run(
                ["git", "add", trd.relative_to(root).as_posix()], cwd=root, check=True
            )

            errors = []
            checker.validate_archive_plans(root, errors)

        self.assertEqual([], errors)

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
                'status: "Pending Confirmation"\n'
                'date: "2026-06-23"\n'
                'last_updated: "2026-06-23"\n'
                'implementation_scope: "initial-rollout"\n'
                'related_prd: "docs/pm/a/b/c/d/PRD.md"\n'
                'related_trd: "docs/engineer/a/b/c/d/TRD.md"\n'
                "---\n\n"
                "# Too Deep Plan\n"
            )
            subprocess.run(["git", "add", plan.relative_to(root).as_posix()], cwd=root, check=True)

            errors = []
            checker.validate_implementation_plan_metadata(root, errors)

        self.assertEqual([], errors)

    def test_repository_contract_accepts_governance_and_collaboration_namespaces(self):
        checker = load_repository_checker_module()

        cases = [
            ("repository-governance/feature-path-contract", "repository-governance", "2"),
            ("agent-collaboration/frontend-ui-routing-contract", "agent-collaboration", "2"),
        ]
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            init_git_main(root)

            for feature_path, parent_feature, feature_level in cases:
                feature = feature_path.split("/")[-1]
                prd = root / f"docs/pm/{feature_path}/PRD.md"
                trd = root / f"docs/engineer/{feature_path}/TRD.md"
                plan = root / f"docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md"
                prd.parent.mkdir(parents=True)
                plan.parent.mkdir(parents=True)
                prd.write_text(
                    "---\n"
                    f'feature: "{feature}"\n'
                    f'feature_path: "{feature_path}"\n'
                    f'parent_feature: "{parent_feature}"\n'
                    f'feature_level: "{feature_level}"\n'
                    'version: "0.1.0"\n'
                    'date: "2026-06-25"\n'
                    'last_updated: "2026-06-25"\n'
                    "---\n\n"
                    f"# {feature} PRD\n"
                )
                trd.write_text(
                    "---\n"
                    f'feature: "{feature}"\n'
                    f'feature_path: "{feature_path}"\n'
                    f'parent_feature: "{parent_feature}"\n'
                    f'feature_level: "{feature_level}"\n'
                    'version: "0.1.0"\n'
                    'date: "2026-06-25"\n'
                    'last_updated: "2026-06-25"\n'
                    f'related_prd: "docs/pm/{feature_path}/PRD.md"\n'
                    "---\n\n"
                    f"# {feature} TRD\n"
                )
                plan.write_text(
                    "---\n"
                    f'feature: "{feature}"\n'
                    f'feature_path: "{feature_path}"\n'
                    f'parent_feature: "{parent_feature}"\n'
                    f'feature_level: "{feature_level}"\n'
                    'version: "0.1.0"\n'
                    'status: "Pending Confirmation"\n'
                    'date: "2026-06-25"\n'
                    'last_updated: "2026-06-25"\n'
                    'implementation_scope: "initial-rollout"\n'
                    f'related_prd: "docs/pm/{feature_path}/PRD.md"\n'
                    f'related_trd: "docs/engineer/{feature_path}/TRD.md"\n'
                    "---\n\n"
                    f"# {feature} Plan\n"
                )

            subprocess.run(["git", "add", "docs"], cwd=root, check=True)

            errors = []
            checker.validate_feature_document_metadata(root, errors)
            checker.validate_implementation_plan_metadata(root, errors)

        self.assertEqual([], errors)

    def test_repository_contract_skips_canonical_checks_for_legacy_plans(self):
        checker = load_repository_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            init_git_main(root)
            plan = (
                root
                / "docs/engineer/agents/engineer-agent/skills/feature-implementor/_legacy/old-plan/IMPLEMENTATION_PLAN.md"
            )
            plan.parent.mkdir(parents=True)
            plan.write_text(
                "---\n"
                'feature: "old-plan"\n'
                'version: "0.1.0"\n'
                'date: "2026-06-25"\n'
                'last_updated: "2026-06-25"\n'
                'legacy_of: "agents/engineer-agent/skills/feature-implementor"\n'
                'legacy_reason: "Historical implementation plan superseded by current requirements"\n'
                'superseded_by: "docs/pm/agents/engineer-agent/skills/feature-implementor/PRD.md"\n'
                "---\n\n"
                "# Old Plan\n"
            )
            subprocess.run(["git", "add", plan.relative_to(root).as_posix()], cwd=root, check=True)

            errors = []
            checker.validate_implementation_plan_metadata(root, errors)
            checker.validate_legacy_artifact_metadata(root, errors)

        self.assertEqual([], errors)

    def test_repository_contract_rejects_legacy_artifacts_missing_required_fields(self):
        checker = load_repository_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            init_git_main(root)
            plan = (
                root
                / "docs/engineer/agents/engineer-agent/skills/feature-implementor/_legacy/old-plan/IMPLEMENTATION_PLAN.md"
            )
            plan.parent.mkdir(parents=True)
            plan.write_text(
                "---\n"
                'feature: "old-plan"\n'
                'version: "0.1.0"\n'
                'date: "2026-06-25"\n'
                'last_updated: "2026-06-25"\n'
                'legacy_of: ""\n'
                "---\n\n"
                "# Old Plan\n"
            )
            subprocess.run(["git", "add", plan.relative_to(root).as_posix()], cwd=root, check=True)

            errors = []
            checker.validate_legacy_artifact_metadata(root, errors)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn("frontmatter 'legacy_of' must be non-empty", rendered)
        self.assertIn("frontmatter 'legacy_reason' must be non-empty", rendered)
        self.assertIn("frontmatter 'superseded_by' must be non-empty", rendered)

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

    def test_repository_contract_accepts_feature_document_metadata(self):
        checker = load_repository_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            prd = root / "docs/pm/agents/pm-agent/skills/idea-to-spec/PRD.md"
            trd = root / "docs/engineer/agents/pm-agent/skills/idea-to-spec/TRD.md"
            prd.parent.mkdir(parents=True)
            trd.parent.mkdir(parents=True)
            prd.write_text(
                "---\n"
                'feature: "skill-idea-to-spec"\n'
                'feature_path: "agents/pm-agent/skills/idea-to-spec"\n'
                'parent_feature: "agents/pm-agent/skills"\n'
                'feature_level: "4"\n'
                'version: "1.0.0"\n'
                'date: "2026-06-25"\n'
                'last_updated: "2026-06-25"\n'
                "---\n\n"
                "# idea-to-spec PRD\n"
            )
            trd.write_text(
                "---\n"
                'feature: "skill-idea-to-spec"\n'
                'feature_path: "agents/pm-agent/skills/idea-to-spec"\n'
                'parent_feature: "agents/pm-agent/skills"\n'
                'feature_level: "4"\n'
                'version: "0.1.0"\n'
                'date: "2026-06-25"\n'
                'last_updated: "2026-06-25"\n'
                'related_prd: "docs/pm/agents/pm-agent/skills/idea-to-spec/PRD.md"\n'
                "---\n\n"
                "# idea-to-spec TRD\n"
            )
            subprocess.run(["git", "init", "-b", "feature"], cwd=root, check=True)
            subprocess.run(
                [
                    "git",
                    "add",
                    prd.relative_to(root).as_posix(),
                    trd.relative_to(root).as_posix(),
                ],
                cwd=root,
                check=True,
            )

            errors = []
            checker.validate_feature_document_metadata(root, errors)

        self.assertEqual([], errors)

    def test_repository_contract_rejects_feature_document_metadata_mismatch(self):
        checker = load_repository_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            prd = root / "docs/pm/agents/pm-agent/skills/idea-to-spec/PRD.md"
            trd = root / "docs/engineer/agents/pm-agent/skills/idea-to-spec/TRD.md"
            prd.parent.mkdir(parents=True)
            trd.parent.mkdir(parents=True)
            prd.write_text(
                "---\n"
                'feature: "skill-idea-to-spec"\n'
                'version: "1.0.0"\n'
                'date: "2026-06-25"\n'
                'last_updated: "2026-06-25"\n'
                "---\n\n"
                "# idea-to-spec PRD\n"
            )
            trd.write_text(
                "---\n"
                'feature: "skill-idea-to-spec"\n'
                'feature_path: "agents/pm-agent/skills/idea-to-spec"\n'
                'parent_feature: "agents/pm-agent"\n'
                'feature_level: "3"\n'
                'version: "0.1.0"\n'
                'date: "2026-06-25"\n'
                'last_updated: "2026-06-25"\n'
                'related_prd: "docs/pm/skill-idea-to-spec/PRD.md"\n'
                "---\n\n"
                "# idea-to-spec TRD\n"
            )
            subprocess.run(["git", "init", "-b", "feature"], cwd=root, check=True)
            subprocess.run(
                [
                    "git",
                    "add",
                    prd.relative_to(root).as_posix(),
                    trd.relative_to(root).as_posix(),
                ],
                cwd=root,
                check=True,
            )

            errors = []
            checker.validate_feature_document_metadata(root, errors)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn("frontmatter 'feature_path' must be non-empty", rendered)
        self.assertIn(
            "frontmatter 'parent_feature' must be 'agents/pm-agent/skills'",
            rendered,
        )
        self.assertIn("frontmatter 'feature_level' must be '4'", rendered)
        self.assertIn(
            "frontmatter 'related_prd' must be 'docs/pm/agents/pm-agent/skills/idea-to-spec/PRD.md'",
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
