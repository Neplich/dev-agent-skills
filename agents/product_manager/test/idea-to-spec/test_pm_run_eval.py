import importlib.util
import os
import sys
import tempfile
import unittest
from pathlib import Path


RUN_EVAL_PATH = Path(__file__).resolve().parent / "run_eval.py"


def load_run_eval_module():
    import sys

    run_eval_dir = str(RUN_EVAL_PATH.parent)
    if run_eval_dir not in sys.path:
        sys.path.insert(0, run_eval_dir)

    spec = importlib.util.spec_from_file_location(
        "idea_to_spec_run_eval",
        RUN_EVAL_PATH,
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class RunEvalTests(unittest.TestCase):
    def test_evaluate_assertion_supports_all_of_any_groups(self):
        run_eval = load_run_eval_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            transcript = root / "with_skill/outputs/transcript.md"
            transcript.parent.mkdir(parents=True)
            transcript.write_text(
                "\n".join(
                    [
                        "项目上下文摘要",
                        "- **状态**: empty workspace",
                        "- **建议车道**: `greenfield-discovery`",
                    ]
                )
            )

            result = run_eval.evaluate_assertion(
                root,
                {
                    "id": "pm_first_lane",
                    "description": "Allows localized PM-first lane labels",
                    "all_of_any": [
                        ["Project context:", "项目上下文摘要"],
                        ["Suggested lane", "建议车道"],
                        ["greenfield-bootstrap", "greenfield-discovery"],
                    ],
                },
            )

            self.assertEqual(result["status"], "PASS")

    def test_main_skips_no_deterministic_checks_before_generation(self):
        run_eval = load_run_eval_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            fixture = temp_root / "fixture"
            fixture.mkdir()
            metadata = fixture / "eval_metadata.json"
            metadata.write_text(
                """{
  "eval_id": "eval-001-no-deterministic-checks",
  "eval_name": "no-deterministic-checks",
  "prompt": "Check metadata with no deterministic runner flow."
}
"""
            )

            def fail_generate(_metadata_path):
                raise AssertionError("generate_eval_outputs should not run")

            old_generate = run_eval.generate_eval_outputs
            old_argv = sys.argv
            old_output_dir = os.environ.get("EVAL_RUN_OUTPUT_DIR")
            run_eval.generate_eval_outputs = fail_generate
            os.environ["EVAL_RUN_OUTPUT_DIR"] = str(temp_root / "runs")
            sys.argv = ["run_eval.py", str(metadata)]
            try:
                result = run_eval.main()
            finally:
                run_eval.generate_eval_outputs = old_generate
                sys.argv = old_argv
                if old_output_dir is None:
                    os.environ.pop("EVAL_RUN_OUTPUT_DIR", None)
                else:
                    os.environ["EVAL_RUN_OUTPUT_DIR"] = old_output_dir

            self.assertEqual(result, 0)
            reports = list((temp_root / "runs").rglob("comparison.auto.md"))
            self.assertEqual(len(reports), 1)
            report = reports[0].read_text()
            self.assertIn("[SKIP] This eval has no deterministic outputs", report)
            self.assertIn("fresh subagent validation", report)


if __name__ == "__main__":
    unittest.main()
