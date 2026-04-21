#!/usr/bin/env python3

import importlib.util
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


if __name__ == "__main__":
    unittest.main()
