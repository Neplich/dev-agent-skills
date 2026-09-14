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
    def test_formal_status_values_match_authoritative_contract(self):
        checker = load_doc_checker_module()
        source = ROOT / (
            "agents/product_manager/skills/idea-to-spec/_internal/"
            "_shared/output-conventions.md"
        )
        status_line = next(
            line for line in source.read_text().splitlines() if line.startswith("status:") and " | " in line
        )
        self.assertEqual(
            tuple(value.strip() for value in status_line.split(":", 1)[1].split("|")),
            checker.FORMAL_DOCUMENT_STATUSES,
        )

    def test_formal_document_status_validation(self):
        checker = load_doc_checker_module()
        valid = ["Draft", "In Review", '\"Approved\"', "'Superseded'", "Deprecated # old"]
        invalid = ["Implemented", "Archived", "approved", "Unknown", "[Approved]"]
        for status in valid + invalid:
            with self.subTest(status=status), tempfile.TemporaryDirectory() as temp_dir:
                root = Path(temp_dir)
                init_git(root)
                add_tracked_file(
                    root, "docs/design.md",
                    f'---\ntitle: Design\ntype: TRD\nstatus: {status}\n---\n',
                )
                errors = checker.validate_all(root)
                if status in valid:
                    self.assertEqual(errors, [])
                else:
                    self.assertEqual(len(errors), 1)
                    self.assertIn("frontmatter 'status' must be one of", errors[0].render(root))

    def test_standalone_design_and_ordinary_notes_need_only_their_own_content(self):
        checker = load_doc_checker_module()
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            init_git(root)
            add_tracked_file(root, "docs/notes.md", "# Notes\nA useful observation.\n")
            add_tracked_file(
                root, "docs/feature/TRD.md",
                '---\ntitle: Design\ntype: TRD\nstatus: Draft\n---\n# Design\n',
            )
            add_tracked_file(root, "docs/feature/IMPLEMENTATION_PLAN.md", "# Work\nCompleted.\n")
            self.assertEqual(checker.validate_all(root), [])

    def test_named_formal_document_reports_incomplete_metadata(self):
        checker = load_doc_checker_module()
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            init_git(root)
            add_tracked_file(root, "docs/PRD.md", "---\ntype: PRD\n---\n")
            rendered = "\n".join(e.render(root) for e in checker.validate_all(root))
            self.assertIn("frontmatter 'title' must be non-empty", rendered)
            self.assertIn("frontmatter 'status' must be non-empty", rendered)

    def test_direct_skill_descriptions_and_repository_without_formal_docs_are_valid(self):
        checker = load_doc_checker_module()
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            init_git(root)
            add_tracked_file(
                root, "agents/engineer/skills/debugger/SKILL.md",
                '---\nname: debugger\ndescription: Use when the user asks to fix a bug.\n---\n',
            )
            self.assertEqual(checker.validate_all(root), [])


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
