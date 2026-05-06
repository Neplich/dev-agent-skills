import json
import unittest
from pathlib import Path


AGENT_ROOT = Path(__file__).resolve().parents[1]


class SecurityEvalContractTests(unittest.TestCase):
    def test_each_security_skill_has_eval_definition(self):
        skill_dirs = sorted(path.parent for path in (AGENT_ROOT / "skills").glob("*/SKILL.md"))

        for skill_dir in skill_dirs:
            if skill_dir.name == "security-agent":
                continue
            with self.subTest(skill=skill_dir.name):
                evals_path = AGENT_ROOT / "test" / skill_dir.name / "evals/evals.json"
                self.assertTrue(evals_path.exists(), f"Missing {evals_path}")

                payload = json.loads(evals_path.read_text())
                self.assertGreaterEqual(len(payload["evals"]), 1)

    def test_security_eval_items_point_to_named_workspaces(self):
        for evals_path in sorted((AGENT_ROOT / "test").glob("*/evals/evals.json")):
            payload = json.loads(evals_path.read_text())
            for item in payload["evals"]:
                with self.subTest(evals=str(evals_path), eval=item["id"]):
                    self.assertTrue(item.get("id"))
                    self.assertTrue(item.get("name"))
                    self.assertTrue(item.get("description"))
                    self.assertTrue(item.get("prompt"))
                    self.assertTrue(item.get("workspace", "").startswith("workspace/"))


if __name__ == "__main__":
    unittest.main()
