import json
import unittest
from pathlib import Path


AGENT_ROOT = Path(__file__).resolve().parents[1]


class EngineerEvalContractTests(unittest.TestCase):
    def test_each_engineer_skill_has_eval_definition(self):
        skill_dirs = sorted(path.parent for path in (AGENT_ROOT / "skills").glob("*/SKILL.md"))

        for skill_dir in skill_dirs:
            if skill_dir.name == "engineer-agent":
                continue
            with self.subTest(skill=skill_dir.name):
                evals_path = AGENT_ROOT / "test" / skill_dir.name / "evals/evals.json"
                self.assertTrue(evals_path.exists(), f"Missing {evals_path}")

                payload = json.loads(evals_path.read_text())
                self.assertEqual(payload["skill_name"], skill_dir.name)
                self.assertGreaterEqual(len(payload["evals"]), 1)

    def test_engineer_eval_items_have_actionable_assertions(self):
        for evals_path in sorted((AGENT_ROOT / "test").glob("*/evals/evals.json")):
            payload = json.loads(evals_path.read_text())
            for item in payload["evals"]:
                with self.subTest(evals=str(evals_path), eval=item["name"]):
                    self.assertIn("prompt", item)
                    self.assertIn("expected_output", item)
                    self.assertGreaterEqual(len(item.get("assertions", [])), 1)
                    for assertion in item["assertions"]:
                        self.assertTrue(assertion.get("name"))
                        self.assertTrue(assertion.get("text"))


if __name__ == "__main__":
    unittest.main()
