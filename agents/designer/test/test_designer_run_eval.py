import importlib.util
import os
import sys
import tempfile
import unittest
from pathlib import Path


RUN_EVAL_PATH = Path(__file__).resolve().parent / "run_eval.py"


def load_run_eval_module():
    spec = importlib.util.spec_from_file_location(
        "designer_run_eval",
        RUN_EVAL_PATH,
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class DesignerRunEvalTests(unittest.TestCase):
    def test_check_outputs_supports_alternative_output_paths(self):
        run_eval = load_run_eval_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "docs/design").mkdir(parents=True)
            (root / "docs/design/ui-ux-spec.md").write_text("spec")

            results = run_eval.check_outputs(
                root,
                [["missing.md", "docs/design/ui-ux-spec.md"]],
            )

            self.assertEqual(results, [("missing.md OR docs/design/ui-ux-spec.md", True)])

    def test_evaluate_assertion_checks_required_forbidden_and_counts(self):
        run_eval = load_run_eval_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            target = root / "with_skill/outputs/transcript.md"
            target.parent.mkdir(parents=True)
            target.write_text("Designer stops here.\nNext role: `engineer-agent`.\n")

            result = run_eval.evaluate_assertion(
                root,
                {
                    "id": "handoff_boundary",
                    "description": "Stops at design handoff",
                    "target": "with_skill/outputs/transcript.md",
                    "all_of": ["Designer stops here."],
                    "none_of": ["apply_patch", "Run `npm test`"],
                    "count_at_least": [{"text": "engineer-agent", "count": 1}],
                },
            )

            self.assertEqual(result["status"], "PASS")

    def test_main_writes_runtime_report_outside_fixture(self):
        run_eval = load_run_eval_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            fixture = temp_root / "fixture"
            fixture.mkdir()
            metadata = fixture / "eval_metadata.json"
            metadata.write_text(
                """{
  "eval_id": "eval-001-runtime-isolation",
  "eval_name": "runtime-isolation",
  "prompt": "Check runtime isolation.",
  "with_skill_outputs": [],
  "without_skill_outputs": [],
  "assertions": []
}
"""
            )

            old_argv = sys.argv
            old_output_dir = os.environ.get("EVAL_RUN_OUTPUT_DIR")
            os.environ["EVAL_RUN_OUTPUT_DIR"] = str(temp_root / "runs")
            sys.argv = ["run_eval.py", str(metadata)]
            try:
                result = run_eval.main()
            finally:
                sys.argv = old_argv
                if old_output_dir is None:
                    os.environ.pop("EVAL_RUN_OUTPUT_DIR", None)
                else:
                    os.environ["EVAL_RUN_OUTPUT_DIR"] = old_output_dir

            self.assertEqual(result, 0)
            self.assertFalse((fixture / "comparison.auto.md").exists())
            reports = list((temp_root / "runs").rglob("comparison.auto.md"))
            self.assertEqual(len(reports), 1)


if __name__ == "__main__":
    unittest.main()
