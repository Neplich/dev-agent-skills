#!/usr/bin/env python3

import importlib.util
import os
import sys
import tempfile
import unittest
from pathlib import Path


RUN_EVAL_PATH = Path(__file__).resolve().parent / "run_eval.py"
RUN_ALL_EVALS_PATH = Path(__file__).resolve().parent / "run_all_evals.py"


def load_run_eval_module():
    spec = importlib.util.spec_from_file_location("qa_run_eval", RUN_EVAL_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules["qa_run_eval"] = module
    spec.loader.exec_module(module)
    return module


def load_run_all_evals_module():
    spec = importlib.util.spec_from_file_location("qa_run_all_evals", RUN_ALL_EVALS_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules["qa_run_all_evals"] = module
    spec.loader.exec_module(module)
    return module


class QaRunEvalTests(unittest.TestCase):
    def test_load_eval_definition_finds_skill_and_assertions(self):
        run_eval = load_run_eval_module()
        metadata = Path(
            "agents/qa/test/qa-agent/evals/workspace/"
            "eval-2-empty-qa-directory-expands-cases/eval_metadata.json"
        )

        loaded = run_eval.load_eval_definition(metadata)

        self.assertEqual(loaded.skill_name, "qa-agent")
        self.assertEqual(loaded.eval_item["name"], "empty-qa-directory-expands-cases")
        self.assertGreaterEqual(len(loaded.eval_item["assertions"]), 1)

    def test_run_all_discovers_metadata_without_output_fields(self):
        run_all = load_run_all_evals_module()
        test_root = Path("agents/qa/test")

        discovered = run_all.find_eval_metadata(test_root)

        self.assertIn(
            test_root
            / "qa-agent/evals/workspace/eval-2-empty-qa-directory-expands-cases/eval_metadata.json",
            discovered,
        )

    def test_candidate_prompt_distinguishes_with_and_without_skill(self):
        run_eval = load_run_eval_module()
        metadata = Path(
            "agents/qa/test/qa-agent/evals/workspace/"
            "eval-2-empty-qa-directory-expands-cases/eval_metadata.json"
        )
        loaded = run_eval.load_eval_definition(metadata)

        with_prompt = run_eval.build_candidate_prompt(loaded, "with_skill")
        without_prompt = run_eval.build_candidate_prompt(loaded, "without_skill")

        self.assertIn("agents/qa/skills/qa-agent/SKILL.md", with_prompt)
        self.assertIn("Read and apply", with_prompt)
        self.assertIn("Do not read or apply", without_prompt)
        self.assertIn("candidate QA output", with_prompt)

    def test_judge_prompt_reads_candidate_output_and_assertions(self):
        run_eval = load_run_eval_module()
        metadata = Path(
            "agents/qa/test/qa-agent/evals/workspace/"
            "eval-2-empty-qa-directory-expands-cases/eval_metadata.json"
        )
        loaded = run_eval.load_eval_definition(metadata)

        prompt = run_eval.build_judge_prompt(
            loaded,
            "with_skill",
            "with_skill/outputs/candidate-output.md",
        )

        self.assertIn("with_skill/outputs/candidate-output.md", prompt)
        self.assertIn("空目录识别", prompt)
        self.assertIn("fresh Codex eval judge", prompt)

    def test_parse_overall_extracts_pass_and_fail(self):
        run_eval = load_run_eval_module()

        self.assertEqual(run_eval.parse_overall("# Verdict\n- Overall: PASS\n"), "PASS")
        self.assertEqual(run_eval.parse_overall("# Verdict\n- Overall: FAIL\n"), "FAIL")
        self.assertEqual(run_eval.parse_overall("no verdict"), "MISSING")

    def test_output_specs_keep_top_level_required_and_nested_or(self):
        run_eval = load_run_eval_module()

        self.assertEqual(
            run_eval.flatten_output_specs(["a.md", "b.md", ["c.md", "d.md"]]),
            [
                ("a.md", ["a.md"]),
                ("b.md", ["b.md"]),
                ("c.md OR d.md", ["c.md", "d.md"]),
            ],
        )

    def test_output_check_uses_runtime_root_for_runner_outputs(self):
        run_eval = load_run_eval_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            skill_root = root / "qa-agent"
            eval_root = skill_root / "evals/workspace/eval-001-runtime-output"
            eval_root.mkdir(parents=True)
            (skill_root / "evals/evals.json").write_text(
                """{
  "schema_version": "1.0",
  "agent": "qa",
  "skill_name": "qa-agent",
  "evals": [
    {
      "id": "eval-001-runtime-output",
      "name": "runtime-output",
      "description": "runtime-output",
      "prompt": "runtime-output",
      "workspace": "workspace/eval-001-runtime-output",
      "expected_output": "runtime-output",
      "assertions": [{"id": "runtime_output", "description": "runtime-output", "text": "runtime-output"}]
    }
  ]
}
"""
            )
            metadata = eval_root / "eval_metadata.json"
            metadata.write_text(
                """{
  "eval_id": "eval-001-runtime-output",
  "eval_name": "runtime-output",
  "workspace_root": "workspace/eval-001-runtime-output",
  "prompt": "runtime-output",
  "fixture_context": [],
  "with_skill_outputs": [
    "with_skill/outputs/report.md"
  ]
}
"""
            )

            old_output_dir = os.environ.get("EVAL_RUN_OUTPUT_DIR")
            os.environ["EVAL_RUN_OUTPUT_DIR"] = str(root / "runs")
            try:
                loaded = run_eval.load_eval_definition(metadata)
                report = loaded.runtime_root / "with_skill/outputs/report.md"
                report.parent.mkdir(parents=True, exist_ok=True)
                report.write_text("runtime report")

                checks = run_eval.check_declared_outputs(loaded)
            finally:
                if old_output_dir is None:
                    os.environ.pop("EVAL_RUN_OUTPUT_DIR", None)
                else:
                    os.environ["EVAL_RUN_OUTPUT_DIR"] = old_output_dir

            self.assertEqual(
                checks,
                [
                    {
                        "field": "with_skill_outputs",
                        "path": "with_skill/outputs/report.md",
                        "ok": True,
                    }
                ],
            )

    def test_render_report_marks_semantic_failures(self):
        run_eval = load_run_eval_module()
        metadata = Path(
            "agents/qa/test/qa-agent/evals/workspace/"
            "eval-2-empty-qa-directory-expands-cases/eval_metadata.json"
        )
        loaded = run_eval.load_eval_definition(metadata)

        report = run_eval.render_report(
            loaded,
            [
                {
                    "label": "with_skill",
                    "candidate_ok": True,
                    "verdict_ok": True,
                    "overall": "PASS",
                    "candidate_path": "with_skill/outputs/candidate-output.md",
                    "verdict_path": "with_skill/outputs/subagent-verdict.md",
                },
                {
                    "label": "without_skill",
                    "candidate_ok": True,
                    "verdict_ok": True,
                    "overall": "FAIL",
                    "candidate_path": "without_skill/outputs/candidate-output.md",
                    "verdict_path": "without_skill/outputs/subagent-verdict.md",
                },
            ],
            [],
        )

        self.assertIn("[PASS] `with_skill` semantic verdict: PASS", report)
        self.assertIn("[FAIL] `without_skill` semantic verdict: FAIL", report)

    def test_runtime_paths_are_isolated_from_eval_fixture(self):
        run_eval = load_run_eval_module()
        metadata = Path(
            "agents/qa/test/qa-agent/evals/workspace/"
            "eval-2-empty-qa-directory-expands-cases/eval_metadata.json"
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            old_output_dir = os.environ.get("EVAL_RUN_OUTPUT_DIR")
            os.environ["EVAL_RUN_OUTPUT_DIR"] = temp_dir
            try:
                loaded = run_eval.load_eval_definition(metadata)
            finally:
                if old_output_dir is None:
                    os.environ.pop("EVAL_RUN_OUTPUT_DIR", None)
                else:
                    os.environ["EVAL_RUN_OUTPUT_DIR"] = old_output_dir

            candidate = run_eval.candidate_path(loaded, "with_skill")
            verdict = run_eval.verdict_path(loaded, "with_skill")

            self.assertIn(temp_dir, str(candidate))
            self.assertIn(temp_dir, str(verdict))
            self.assertNotIn(str(loaded.eval_root), str(candidate))
            self.assertNotIn(str(loaded.eval_root), str(verdict))

    def test_runtime_workspace_applies_execution_cleanup(self):
        run_eval = load_run_eval_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            skill_root = root / "qa-agent"
            eval_root = skill_root / "evals/workspace/eval-001-cleanup"
            eval_root.mkdir(parents=True)
            (skill_root / "evals/evals.json").write_text(
                """{
  "schema_version": "1.0",
  "agent": "qa",
  "skill_name": "qa-agent",
  "evals": [
    {
      "id": "eval-001-cleanup",
      "name": "cleanup",
      "description": "cleanup",
      "prompt": "cleanup",
      "workspace": "workspace/eval-001-cleanup",
      "expected_output": "cleanup",
      "assertions": [{"id": "cleanup", "description": "cleanup", "text": "cleanup"}]
    }
  ]
}
"""
            )
            metadata = eval_root / "eval_metadata.json"
            metadata.write_text(
                """{
  "eval_id": "eval-001-cleanup",
  "eval_name": "cleanup",
  "workspace_root": "workspace/eval-001-cleanup",
  "prompt": "cleanup",
  "fixture_context": ["docs/qa/e2e/account/profile-settings/profile-form/"],
  "with_skill_outputs": ["docs/qa/e2e/account/profile-settings/profile-form/TEST_SUITE.md"],
  "without_skill_outputs": ["docs/qa/e2e/account/profile-settings/profile-form/cases/TC-001-new.md"],
  "execution_cleanup": [
    "docs/qa/e2e/account/profile-settings/profile-form/TEST_SUITE.md",
    "docs/qa/e2e/account/profile-settings/profile-form/cases/TC-*.md",
    "with_skill/outputs"
  ]
}
"""
            )
            e2e_root = eval_root / "docs/qa/e2e/account/profile-settings/profile-form"
            (e2e_root / "cases").mkdir(parents=True)
            (e2e_root / "TEST_SUITE.md").write_text("stale")
            (e2e_root / "cases/TC-001-old.md").write_text("stale")
            (eval_root / "with_skill/outputs").mkdir(parents=True)

            old_output_dir = os.environ.get("EVAL_RUN_OUTPUT_DIR")
            os.environ["EVAL_RUN_OUTPUT_DIR"] = str(root / "runs")
            try:
                loaded = run_eval.load_eval_definition(metadata)
                run_eval.clean_outputs(loaded)
                run_eval.prepare_runtime_workspace(loaded)
            finally:
                if old_output_dir is None:
                    os.environ.pop("EVAL_RUN_OUTPUT_DIR", None)
                else:
                    os.environ["EVAL_RUN_OUTPUT_DIR"] = old_output_dir

            runtime_workspace = loaded.runtime_workspace_root
            runtime_e2e_root = runtime_workspace / "docs/qa/e2e/account/profile-settings/profile-form"
            self.assertFalse((runtime_e2e_root / "TEST_SUITE.md").exists())
            self.assertFalse((runtime_e2e_root / "cases/TC-001-old.md").exists())
            self.assertFalse((runtime_workspace / "with_skill/outputs").exists())
            self.assertTrue((e2e_root / "TEST_SUITE.md").exists())

    def test_main_runs_metadata_without_deterministic_outputs(self):
        run_eval = load_run_eval_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            skill_root = root / "qa-agent"
            eval_root = skill_root / "evals/workspace/eval-001-no-output"
            eval_root.mkdir(parents=True)
            (skill_root / "evals/evals.json").write_text(
                """{
  "schema_version": "1.0",
  "agent": "qa",
  "skill_name": "qa-agent",
  "evals": [
    {
      "id": "eval-001-no-output",
      "name": "no-output",
      "description": "no-output",
      "prompt": "no-output",
      "workspace": "workspace/eval-001-no-output",
      "expected_output": "no-output",
      "assertions": [{"id": "no_output", "description": "no-output", "text": "no-output"}]
    }
  ]
}
"""
            )
            metadata = eval_root / "eval_metadata.json"
            metadata.write_text(
                """{
  "eval_id": "eval-001-no-output",
  "eval_name": "no-output",
  "workspace_root": "workspace/eval-001-no-output",
  "prompt": "no-output",
  "fixture_context": []
}
"""
            )

            old_argv = sys.argv
            old_output_dir = os.environ.get("EVAL_RUN_OUTPUT_DIR")
            os.environ["EVAL_RUN_OUTPUT_DIR"] = str(root / "runs")
            try:
                loaded = run_eval.load_eval_definition(metadata)
                for label, overall in (
                    ("with_skill", "PASS"),
                    ("without_skill", "FAIL"),
                ):
                    candidate = run_eval.candidate_path(loaded, label)
                    verdict = run_eval.verdict_path(loaded, label)
                    candidate.parent.mkdir(parents=True, exist_ok=True)
                    verdict.parent.mkdir(parents=True, exist_ok=True)
                    candidate.write_text("candidate")
                    verdict.write_text(f"# Verdict\n- Overall: {overall}\n")

                sys.argv = ["run_eval.py", str(metadata), "--skip-generate"]
                result = run_eval.main()
            finally:
                sys.argv = old_argv
                if old_output_dir is None:
                    os.environ.pop("EVAL_RUN_OUTPUT_DIR", None)
                else:
                    os.environ["EVAL_RUN_OUTPUT_DIR"] = old_output_dir

            self.assertEqual(result, 0)
            reports = list((root / "runs").rglob("comparison.auto.md"))
            self.assertEqual(len(reports), 1)
            report = reports[0].read_text()
            self.assertNotIn("[SKIP]", report)
            self.assertIn("[PASS] `with_skill` semantic verdict: PASS", report)

    def test_main_fails_when_declared_output_is_missing(self):
        run_eval = load_run_eval_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            skill_root = root / "qa-agent"
            eval_root = skill_root / "evals/workspace/eval-001-output-check"
            eval_root.mkdir(parents=True)
            (skill_root / "evals/evals.json").write_text(
                """{
  "schema_version": "1.0",
  "agent": "qa",
  "skill_name": "qa-agent",
  "evals": [
    {
      "id": "eval-001-output-check",
      "name": "output-check",
      "description": "output-check",
      "prompt": "output-check",
      "workspace": "workspace/eval-001-output-check",
      "expected_output": "output-check",
      "assertions": [{"id": "output_check", "description": "output-check", "text": "output-check"}]
    }
  ]
}
"""
            )
            metadata = eval_root / "eval_metadata.json"
            metadata.write_text(
                """{
  "eval_id": "eval-001-output-check",
  "eval_name": "output-check",
  "workspace_root": "workspace/eval-001-output-check",
  "prompt": "output-check",
  "fixture_context": [],
  "with_skill_outputs": [
    "docs/qa/e2e/account/profile-settings/profile-form/TEST_SUITE.md"
  ]
}
"""
            )

            old_argv = sys.argv
            old_output_dir = os.environ.get("EVAL_RUN_OUTPUT_DIR")
            os.environ["EVAL_RUN_OUTPUT_DIR"] = str(root / "runs")
            try:
                loaded = run_eval.load_eval_definition(metadata)
                for label, overall in (
                    ("with_skill", "PASS"),
                    ("without_skill", "FAIL"),
                ):
                    candidate = run_eval.candidate_path(loaded, label)
                    verdict = run_eval.verdict_path(loaded, label)
                    candidate.parent.mkdir(parents=True, exist_ok=True)
                    verdict.parent.mkdir(parents=True, exist_ok=True)
                    candidate.write_text("candidate")
                    verdict.write_text(f"# Verdict\n- Overall: {overall}\n")

                sys.argv = ["run_eval.py", str(metadata), "--skip-generate"]
                result = run_eval.main()
            finally:
                sys.argv = old_argv
                if old_output_dir is None:
                    os.environ.pop("EVAL_RUN_OUTPUT_DIR", None)
                else:
                    os.environ["EVAL_RUN_OUTPUT_DIR"] = old_output_dir

            self.assertEqual(result, 1)
            reports = list((root / "runs").rglob("comparison.auto.md"))
            self.assertEqual(len(reports), 1)
            report = reports[0].read_text()
            self.assertIn("## Declared Output Checks", report)
            self.assertIn("[FAIL] `with_skill_outputs`", report)


if __name__ == "__main__":
    unittest.main()
