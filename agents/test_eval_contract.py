import importlib.util
import sys
import unittest
from pathlib import Path


CHECKER_PATH = Path(__file__).resolve().parents[1] / "scripts/check_eval_contract.py"


def load_checker_module():
    spec = importlib.util.spec_from_file_location("check_eval_contract", CHECKER_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules["check_eval_contract"] = module
    spec.loader.exec_module(module)
    return module


class EvalContractTests(unittest.TestCase):
    def test_all_agent_skill_evals_follow_shared_contract(self):
        checker = load_checker_module()
        errors = checker.validate_all()

        self.assertEqual(
            [error.render(checker.repo_root()) for error in errors],
            [],
        )


if __name__ == "__main__":
    unittest.main()
