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


def formal_doc_frontmatter(doc_type: str) -> str:
    child_features = 'child_features: "N/A"\n' if doc_type == "PRD" else ""
    return (
        "---\n"
        'title: "Example"\n'
        f"type: {doc_type}\n"
        'feature: "example"\n'
        'feature_path: "example"\n'
        'parent_feature: "N/A"\n'
        'feature_level: "1"\n'
        'version: "0.1.0"\n'
        "status: Draft\n"
        'author: "Tester Codex"\n'
        'date: "2026-07-06"\n'
        'last_updated: "2026-07-06"\n'
        'generated_by: "prd-gen"\n'
        f"{child_features}"
        "changelog:\n"
        '  - version: "0.1.0"\n'
        '    date: "2026-07-06"\n'
        '    changes: "Initial version"\n'
        "---\n\n"
    )


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
        self.assertIn("frontmatter 'title' must be non-empty", rendered)
        self.assertIn(
            "frontmatter 'changelog' must contain at least one entry", rendered
        )

    def test_doc_contract_rejects_inline_comment_title(self):
        checker = load_doc_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            init_git(root)
            add_tracked_file(
                root,
                "docs/engineer/example/TRD.md",
                formal_doc_frontmatter("TRD").replace(
                    'title: "Example"\n', "title: # absent\n"
                ),
            )
            errors = checker.validate_all(root)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn("frontmatter 'title' must be non-empty", rendered)

    def test_doc_contract_rejects_quoted_empty_feature_with_comment(self):
        checker = load_doc_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            init_git(root)
            add_tracked_file(
                root,
                "docs/engineer/example/TRD.md",
                formal_doc_frontmatter("TRD").replace(
                    'feature: "example"\n', 'feature: "" # absent\n'
                ),
            )
            errors = checker.validate_all(root)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn("frontmatter 'feature' must be non-empty", rendered)

    def test_doc_contract_rejects_bare_block_feature(self):
        checker = load_doc_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            init_git(root)
            add_tracked_file(
                root,
                "docs/engineer/example/TRD.md",
                formal_doc_frontmatter("TRD").replace(
                    'feature: "example"\n', "feature: |\n"
                ),
            )
            errors = checker.validate_all(root)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn("frontmatter 'feature' must be non-empty", rendered)

    def test_doc_contract_archive_segment_pm_doc_still_requires_frontmatter(self):
        checker = load_doc_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            init_git(root)
            add_tracked_file(
                root,
                "docs/pm/payments/archive/PRD.md",
                "# Unfrontmattered PRD under archive segment\n",
            )

            errors = checker.validate_all(root)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn("docs/pm/payments/archive/PRD.md", rendered)

    def test_doc_contract_rejects_prd_without_child_features(self):
        checker = load_doc_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            init_git(root)
            add_tracked_file(
                root,
                "docs/pm/example/PRD.md",
                formal_doc_frontmatter("PRD").replace('child_features: "N/A"\n', "")
                + "# Example PRD\n",
            )

            errors = checker.validate_all(root)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn("frontmatter 'child_features' must be non-empty for PRDs", rendered)

    def test_doc_contract_rejects_changelog_entry_without_changes(self):
        checker = load_doc_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            init_git(root)
            add_tracked_file(
                root,
                "docs/engineer/example/TRD.md",
                formal_doc_frontmatter("TRD").replace(
                    '    changes: "Initial version"\n', ""
                )
                + "# Example TRD\n",
            )

            errors = checker.validate_all(root)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn("must have non-empty 'changes'", rendered)

    def test_doc_contract_rejects_wrapped_changelog(self):
        checker = load_doc_checker_module()
        content = (
            "---\nchangelog:\n  wrapper:\n"
            "    - version: 0.1.0\n"
            "      date: 2026-07-06\n"
            "      changes: Initial version\n---\n"
        )
        errors = []

        checker.validate_changelog_entries(Path("TRD.md"), content, errors)

        self.assertIn("must be a flat list", errors[0].message)

    def test_doc_contract_rejects_inline_comment_changelog_value(self):
        checker = load_doc_checker_module()
        content = (
            "---\nchangelog:\n  - version: 0.1.0\n"
            "    date: 2026-07-06\n    changes: # absent\n---\n"
        )
        errors = []

        checker.validate_changelog_entries(Path("TRD.md"), content, errors)

        self.assertIn("must have non-empty 'changes'", errors[0].message)

    def test_doc_contract_accepts_quoted_block_marker_changelog_value(self):
        checker = load_doc_checker_module()
        content = (
            '---\nchangelog:\n  - version: "0.1.0"\n'
            '    date: "2026-07-06"\n    changes: "|"\n---\n'
        )
        errors = []

        checker.validate_changelog_entries(Path("TRD.md"), content, errors)

        self.assertEqual([], errors)

    def test_doc_contract_rejects_quoted_whitespace_changelog_value(self):
        checker = load_doc_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            init_git(root)
            add_tracked_file(
                root,
                "docs/engineer/example/TRD.md",
                formal_doc_frontmatter("TRD").replace(
                    '    changes: "Initial version"\n', '    changes: "   "\n'
                )
                + "# Example TRD\n",
            )

            errors = checker.validate_all(root)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn("must have non-empty 'changes'", rendered)

    def test_doc_contract_rejects_empty_child_features_collection(self):
        checker = load_doc_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            init_git(root)
            add_tracked_file(
                root,
                "docs/pm/example/PRD.md",
                formal_doc_frontmatter("PRD").replace(
                    'child_features: "N/A"\n', "child_features: []\n"
                )
                + "# Example PRD\n",
            )

            errors = checker.validate_all(root)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn("frontmatter 'child_features' must be non-empty for PRDs", rendered)

    def test_doc_contract_rejects_spaced_empty_child_features_collection(self):
        checker = load_doc_checker_module()
        content = "---\nchild_features: [ ]\n---\n"

        self.assertFalse(checker.frontmatter_field_has_value(content, "child_features"))

    def test_doc_contract_rejects_comment_only_child_features(self):
        checker = load_doc_checker_module()
        content = "---\nchild_features:\n  # absent\nchangelog:\n---\n"

        self.assertFalse(checker.frontmatter_field_has_value(content, "child_features"))

    def test_doc_contract_rejects_blank_child_features_list_item(self):
        checker = load_doc_checker_module()
        content = '---\nchild_features:\n  - ""\nchangelog:\n---\n'

        self.assertFalse(checker.frontmatter_field_has_value(content, "child_features"))

    def test_doc_contract_registered_exemption_skips_extended_fields(self):
        checker = load_doc_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            init_git(root)
            add_tracked_file(
                root,
                "docs/pm/repository-ci-governance/CI_PLAN.md",
                "---\n"
                'feature: "repository-ci-governance"\n'
                'version: "0.1.0-draft"\n'
                'date: "2026-05-06"\n'
                'last_updated: "2026-09-01"\n'
                "---\n\n"
                "# Repository CI Governance Plan\n",
            )

            errors = checker.validate_all(root)

        self.assertEqual([], errors)

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
                formal_doc_frontmatter("PRD") + "# Example PRD\n",
            )
            add_tracked_file(
                root,
                "docs/engineer/example/TRD.md",
                formal_doc_frontmatter("TRD").replace(
                    "changelog:\n",
                    'related_prd: "docs/pm/example/PRD.md"\nchangelog:\n',
                )
                + "# Example TRD\n",
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

    def test_markdown_links_reject_missing_target_and_anchor(self):
        checker = load_doc_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            init_git(root)
            add_tracked_file(
                root,
                "docs/guide.md",
                "# Guide\n\n[missing](missing.md)\n[anchor](target.md#missing)\n",
            )
            add_tracked_file(root, "docs/target.md", "# Present\n")

            errors = []
            checker.validate_markdown_links(root, errors)

        rendered = "\n".join(error.render(root) for error in errors)
        self.assertIn("target does not exist", rendered)
        self.assertIn("anchor does not exist", rendered)

    def test_markdown_links_accept_percent_encoded_duplicate_heading(self):
        checker = load_doc_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            init_git(root)
            add_tracked_file(
                root,
                "docs/guide.md",
                "[encoded](target%20file.md#section-1)\n",
            )
            add_tracked_file(
                root,
                "docs/target file.md",
                "# Section\n\n## Section\n",
            )

            errors = []
            checker.validate_markdown_links(root, errors)

        self.assertEqual([], errors)

    def test_markdown_links_reject_repository_escape(self):
        checker = load_doc_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            init_git(root)
            add_tracked_file(root, "docs/guide.md", "[escape](../../outside.md)\n")

            errors = []
            checker.validate_markdown_links(root, errors)

        self.assertEqual(1, len(errors))
        self.assertIn("escapes repository", errors[0].message)

    def test_markdown_links_ignore_code_and_generated_sources(self):
        checker = load_doc_checker_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            init_git(root)
            add_tracked_file(
                root,
                "docs/guide.md",
                "```markdown\n[ignored](missing.md)\n```\n"
                "`[inline](missing.md)`\n",
            )
            add_tracked_file(
                root,
                "agents/qa/skills/qa-agent/_internal/_generated/"
                "shared-contracts/example.md",
                "[ignored](missing.md)\n",
            )

            errors = []
            checker.validate_markdown_links(root, errors)

        self.assertEqual([], errors)


if __name__ == "__main__":
    unittest.main()
