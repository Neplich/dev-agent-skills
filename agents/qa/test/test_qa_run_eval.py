#!/usr/bin/env python3

import importlib.util
import os
import sys
import tempfile
import unittest
from pathlib import Path


RUN_EVAL_PATH = Path(__file__).resolve().parent / "run_eval.py"


def load_run_eval_module():
    spec = importlib.util.spec_from_file_location("qa_run_eval", RUN_EVAL_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules["qa_run_eval"] = module
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
  "fixture_context": ["docs/qa/profile-settings/"],
  "with_skill_outputs": ["with_skill/outputs/subagent-verdict.md"],
  "without_skill_outputs": ["without_skill/outputs/subagent-verdict.md"],
  "execution_cleanup": [
    "docs/qa/profile-settings/TEST_SPEC.md",
    "docs/qa/profile-settings/test-cases/TC-*.md",
    "with_skill/outputs"
  ]
}
"""
            )
            (eval_root / "docs/qa/profile-settings/test-cases").mkdir(parents=True)
            (eval_root / "docs/qa/profile-settings/TEST_SPEC.md").write_text("stale")
            (eval_root / "docs/qa/profile-settings/test-cases/TC-001-old.md").write_text("stale")
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
            self.assertFalse((runtime_workspace / "docs/qa/profile-settings/TEST_SPEC.md").exists())
            self.assertFalse((runtime_workspace / "docs/qa/profile-settings/test-cases/TC-001-old.md").exists())
            self.assertFalse((runtime_workspace / "with_skill/outputs").exists())
            self.assertTrue((eval_root / "docs/qa/profile-settings/TEST_SPEC.md").exists())


if __name__ == "__main__":
    unittest.main()
