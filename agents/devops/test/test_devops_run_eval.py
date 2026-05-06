import importlib.util
import tempfile
import unittest
from pathlib import Path


RUN_EVAL_PATH = Path(__file__).resolve().parent / "run_eval.py"


def load_run_eval_module():
    spec = importlib.util.spec_from_file_location(
        "devops_run_eval",
        RUN_EVAL_PATH,
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class DevopsRunEvalTests(unittest.TestCase):
    def test_check_outputs_marks_missing_and_existing_outputs(self):
        run_eval = load_run_eval_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "deploy").mkdir()
            (root / "deploy/ENV_AUDIT.md").write_text("audit")

            results = run_eval.check_outputs(
                root,
                ["deploy/ENV_AUDIT.md", "with_skill/outputs/transcript.md"],
            )

            self.assertEqual(
                results,
                [
                    ("deploy/ENV_AUDIT.md", True),
                    ("with_skill/outputs/transcript.md", False),
                ],
            )

    def test_evaluate_assertion_reports_missing_required_text(self):
        run_eval = load_run_eval_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            target = root / "deploy/ENV_AUDIT.md"
            target.parent.mkdir()
            target.write_text("# Environment Configuration Audit Report\n")

            result = run_eval.evaluate_assertion(
                root,
                {
                    "id": "report_has_sections",
                    "description": "Report includes sections",
                    "target": "deploy/ENV_AUDIT.md",
                    "all_of": ["# Environment Configuration Audit Report", "## Missing Variables"],
                },
            )

            self.assertEqual(result["status"], "FAIL")
            self.assertIn("Missing required text", result["details"])


if __name__ == "__main__":
    unittest.main()
