import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHECKER_PATH = ROOT / "scripts/check_doc_contract.py"
SCRIPTS_DIR = ROOT / "scripts"


def load_doc_checker_module():
    if str(SCRIPTS_DIR) not in sys.path:
        sys.path.insert(0, str(SCRIPTS_DIR))
    spec = importlib.util.spec_from_file_location("check_doc_contract", CHECKER_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules["check_doc_contract"] = module
    spec.loader.exec_module(module)
    return module


def init_git(root: Path) -> None:
    subprocess.run(
        ["git", "init", "-b", "main"],
        cwd=root,
        check=True,
        stdout=subprocess.DEVNULL,
    )


def add_tracked_file(root: Path, rel: str, content: str) -> Path:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)
    subprocess.run(["git", "add", rel], cwd=root, check=True)
    return path


class DocContractTests(unittest.TestCase):
    def test_doc_contract_rejects_missing_required_formal_metadata(self):
        checker = load_doc_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            init_git(root)
            add_tracked_file(
                root,
                "docs/pm/example/FEATURE_CATALOG.md",
                "---\n"
                'feature: "example"\n'
                'version: "0.1.0"\n'
                "---\n\n"
                "# Feature Catalog\n",
            )

            errors = checker.validate_all(root)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn("frontmatter 'date' must be non-empty", rendered)
        self.assertIn("frontmatter 'last_updated' must be non-empty", rendered)

    def test_doc_contract_rejects_non_pm_description_trigger_phrase(self):
        checker = load_doc_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            init_git(root)
            skill_doc = root / "agents/engineer/skills/debugger/SKILL.md"
            skill_doc.parent.mkdir(parents=True, exist_ok=True)
            skill_doc.write_text(
                "---\n"
                "name: debugger\n"
                "description: \"Use when the user asks to debug a failure.\"\n"
                "visibility: internal\n"
                "---\n\n"
                "# Debugger\n"
            )

            errors = checker.validate_all(root)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn(
            "frontmatter 'description' must not contain user-trigger phrase pattern 'Use when the user'",
            rendered,
        )

    def test_doc_contract_accepts_formal_docs_and_internal_description(self):
        checker = load_doc_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            init_git(root)
            add_tracked_file(
                root,
                "docs/pm/example/PRD.md",
                "---\n"
                'feature: "example"\n'
                'version: "0.1.0"\n'
                'date: "2026-07-06"\n'
                'last_updated: "2026-07-06"\n'
                "---\n\n"
                "# Example PRD\n",
            )
            add_tracked_file(
                root,
                "docs/engineer/example/TRD.md",
                "---\n"
                'feature: "example"\n'
                'version: "0.1.0"\n'
                'date: "2026-07-06"\n'
                'last_updated: "2026-07-06"\n'
                'related_prd: "docs/pm/example/PRD.md"\n'
                "---\n\n"
                "# Example TRD\n",
            )

            pm_agent = root / "agents/product_manager/skills/pm-agent/SKILL.md"
            pm_agent.parent.mkdir(parents=True, exist_ok=True)
            pm_agent.write_text(
                "---\n"
                "name: pm-agent\n"
                "description: \"Use when the user asks for product work.\"\n"
                "---\n\n"
                "# PM Agent\n"
            )
            debugger = root / "agents/engineer/skills/debugger/SKILL.md"
            debugger.parent.mkdir(parents=True, exist_ok=True)
            debugger.write_text(
                "---\n"
                "name: debugger\n"
                "description: \"Internal engineering specialist invoked by engineer-agent after pm-agent handoff.\"\n"
                "visibility: internal\n"
                "---\n\n"
                "# Debugger\n"
            )

            errors = checker.validate_all(root)

        self.assertEqual([], errors)


if __name__ == "__main__":
    unittest.main()
