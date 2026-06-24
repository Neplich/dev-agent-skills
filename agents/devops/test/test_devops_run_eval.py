import importlib.util
import os
import sys
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

    def test_main_skips_metadata_without_deterministic_checks(self):
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
    "with_skill/outputs/deploy.md"
  ],
  "without_skill_outputs": [
    "without_skill/outputs/deploy-notes.md"
  ],
  "baseline_outputs": [
    "baseline/outputs/summary.md"
  ],
  "assertions": [
    {
      "id": "baseline_target_is_report_only",
      "description": "Baseline target failures are report-only",
      "target": "without_skill/outputs/deploy-notes.md",
      "all_of": ["baseline detail"]
    }
  ]
}
"""
            )
            report = fixture / "with_skill/outputs/deploy.md"
            report.parent.mkdir(parents=True)
            report.write_text("with skill deploy")

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
    "with_skill/outputs/deploy.md"
  ],
  "assertions": [
    {
      "id": "mixed_target_still_gates",
      "description": "Mixed with_skill and baseline targets remain gated",
      "target": [
        "with_skill/outputs/deploy.md",
        "without_skill/outputs/deploy-notes.md"
      ],
      "all_of": ["required with-skill detail"]
    }
  ]
}
"""
            )
            with_skill = fixture / "with_skill/outputs/deploy.md"
            baseline = fixture / "without_skill/outputs/deploy-notes.md"
            with_skill.parent.mkdir(parents=True)
            baseline.parent.mkdir(parents=True)
            with_skill.write_text("with skill deploy")
            baseline.write_text("baseline notes")

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

            self.assertEqual(result, 1)
            reports = list((temp_root / "runs").rglob("comparison.auto.md"))
            self.assertEqual(len(reports), 1)
            rendered = reports[0].read_text()
            self.assertIn("[FAIL] `mixed_target_still_gates`", rendered)


if __name__ == "__main__":
    unittest.main()
