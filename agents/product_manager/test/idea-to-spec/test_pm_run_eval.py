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

    def test_main_reports_baseline_failures_without_failing(self):
        run_eval = load_run_eval_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            fixture = temp_root / "fixture"
            fixture.mkdir()
            metadata = fixture / "eval_metadata.json"
            metadata.write_text(
                """{
  "eval_id": "eval-001-baseline-report-only",
  "eval_name": "baseline-report-only",
  "prompt": "Check baseline report-only behavior.",
  "with_skill_outputs": [
    "with_skill/outputs/PRD.md"
  ],
  "without_skill_outputs": [
    "without_skill/outputs/notes.md"
  ],
  "baseline_outputs": [
    "baseline/outputs/summary.md"
  ],
  "assertions": [
    {
      "id": "baseline_target_is_report_only",
      "description": "Baseline target failures are report-only",
      "target": "without_skill/outputs/notes.md",
      "all_of": ["baseline detail"]
    }
  ]
}
"""
            )

            old_argv = sys.argv
            old_output_dir = os.environ.get("EVAL_RUN_OUTPUT_DIR")
            os.environ["EVAL_RUN_OUTPUT_DIR"] = str(temp_root / "runs")
            try:
                runtime_root = run_eval.eval_runtime_root(metadata, "product_manager")
                report = runtime_root / "with_skill/outputs/PRD.md"
                report.parent.mkdir(parents=True)
                report.write_text("with skill PRD")

                sys.argv = ["run_eval.py", str(metadata), "--skip-generate"]
                result = run_eval.main()
            finally:
                sys.argv = old_argv
                if old_output_dir is None:
                    os.environ.pop("EVAL_RUN_OUTPUT_DIR", None)
                else:
                    os.environ["EVAL_RUN_OUTPUT_DIR"] = old_output_dir

            self.assertEqual(result, 0)
            reports = list((temp_root / "runs").rglob("comparison.auto.md"))
            self.assertEqual(len(reports), 1)
            rendered = reports[0].read_text()
            self.assertIn("[FAIL] `without_skill_outputs", rendered)
            self.assertIn("[FAIL] `baseline_outputs", rendered)
            self.assertIn("[FAIL] `baseline_target_is_report_only`", rendered)

    def test_main_fails_when_mixed_target_assertion_fails(self):
        run_eval = load_run_eval_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            fixture = temp_root / "fixture"
            fixture.mkdir()
            metadata = fixture / "eval_metadata.json"
            metadata.write_text(
                """{
  "eval_id": "eval-001-mixed-target-gates",
  "eval_name": "mixed-target-gates",
  "prompt": "Check mixed target gating behavior.",
  "with_skill_outputs": [
    "with_skill/outputs/PRD.md"
  ],
  "assertions": [
    {
      "id": "mixed_target_still_gates",
      "description": "Mixed with_skill and baseline targets remain gated",
      "target": [
        "with_skill/outputs/PRD.md",
        "without_skill/outputs/notes.md"
      ],
      "all_of": ["required with-skill detail"]
    }
  ]
}
"""
            )

            old_argv = sys.argv
            old_output_dir = os.environ.get("EVAL_RUN_OUTPUT_DIR")
            os.environ["EVAL_RUN_OUTPUT_DIR"] = str(temp_root / "runs")
            try:
                runtime_root = run_eval.eval_runtime_root(metadata, "product_manager")
                with_skill = runtime_root / "with_skill/outputs/PRD.md"
                baseline = runtime_root / "without_skill/outputs/notes.md"
                with_skill.parent.mkdir(parents=True)
                baseline.parent.mkdir(parents=True)
                with_skill.write_text("with skill PRD")
                baseline.write_text("baseline notes")

                sys.argv = ["run_eval.py", str(metadata), "--skip-generate"]
                result = run_eval.main()
            finally:
                sys.argv = old_argv
                if old_output_dir is None:
                    os.environ.pop("EVAL_RUN_OUTPUT_DIR", None)
                else:
                    os.environ["EVAL_RUN_OUTPUT_DIR"] = old_output_dir

            self.assertEqual(result, 1)
            reports = list((temp_root / "runs").rglob("comparison.auto.md"))
            self.assertEqual(len(reports), 1)
            rendered = reports[0].read_text()
            self.assertIn("[FAIL] `mixed_target_still_gates`", rendered)


if __name__ == "__main__":
    unittest.main()
