import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


CHECKER_PATH = Path(__file__).resolve().parents[1] / "scripts/check_eval_contract.py"
ARTIFACT_CHECKER_PATH = Path(__file__).resolve().parents[1] / "scripts/check_eval_artifacts.py"


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

    def test_eval_contract_rejects_transcript_metadata_outputs(self):
        checker = load_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            evals_path = root / "agents/engineer/test/debugger/evals/evals.json"
            skill_doc = root / "agents/engineer/skills/debugger/SKILL.md"
            workspace = evals_path.parent / "workspace/eval-001-transcript-output"
            workspace.mkdir(parents=True)
            skill_doc.parent.mkdir(parents=True)
            skill_doc.write_text("# Debugger\n")
            (workspace / "comparison.md").write_text("# Comparison\n")
            (workspace / "eval_metadata.json").write_text(
                json.dumps(
                    {
                        "eval_id": "eval-001-transcript-output",
                        "eval_name": "transcript-output",
                        "with_skill_outputs": [
                            "with_skill/outputs/transcript.md"
                        ],
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
                                "id": "eval-001-transcript-output",
                                "name": "transcript-output",
                                "description": "Invalid transcript output",
                                "prompt": "Run the eval",
                                "workspace": "workspace/eval-001-transcript-output",
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
        self.assertIn(
            "execution_cleanup requires deterministic runner outputs",
            rendered,
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


if __name__ == "__main__":
    unittest.main()
