#!/usr/bin/env python3
"""Validate documentation contracts not owned by repository/eval checkers."""

from __future__ import annotations

import re
import sys
from pathlib import Path

from check_repository_contract import (
    ContractError,
    add_error,
    is_legacy_artifact_path,
    parse_markdown_frontmatter,
    repo_root,
    tracked_files,
)


REQUIRED_FORMAL_FRONTMATTER_FIELDS = ("feature", "version", "date", "last_updated")
FORMAL_DOC_PREFIXES = ("docs/pm/", "docs/engineer/")
NON_FORMAL_DOC_NAMES = {"README.md", "README_zh.md", "CHANGELOG.md"}

DESCRIPTION_DENYLIST: tuple[tuple[re.Pattern[str], str], ...] = (
    (re.compile(r"\bTrigger on phrases like\b", re.IGNORECASE), "Trigger on phrases like"),
    (re.compile(r"\bUse this skill when the user\b", re.IGNORECASE), "Use this skill when the user"),
    (re.compile(r"\bUse this skill whenever the user\b", re.IGNORECASE), "Use this skill whenever the user"),
    (re.compile(r"\bUse when the user\b", re.IGNORECASE), "Use when the user"),
    (re.compile("实现这个功能"), "实现这个功能"),
    (re.compile("修 bug", re.IGNORECASE), "修 bug"),
    (re.compile("提 PR", re.IGNORECASE), "提 PR"),
    (re.compile("测一下"), "测一下"),
    (re.compile("写代码"), "写代码"),
)


def is_implementation_plan_artifact_path(rel: str) -> bool:
    return rel.endswith("/IMPLEMENTATION_PLAN.md") or "/implementation-plans/archive/" in rel


def is_formal_pm_or_engineer_document(rel: str) -> bool:
    if not rel.endswith(".md"):
        return False
    if not rel.startswith(FORMAL_DOC_PREFIXES):
        return False
    if is_legacy_artifact_path(rel):
        return False
    if Path(rel).name in NON_FORMAL_DOC_NAMES:
        return False
    # Implementation plan metadata, including archive-specific fields, is owned
    # by check_repository_contract.py. Keep this checker focused on the gap:
    # PRD/TRD plus other formal PM/Engineer docs such as DECISIONS and CI_PLAN.
    return not is_implementation_plan_artifact_path(rel)


def validate_required_formal_frontmatter(
    root: Path,
    errors: list[ContractError],
) -> None:
    for rel in tracked_files(root):
        if not is_formal_pm_or_engineer_document(rel):
            continue

        path = root / rel
        if not path.exists():
            continue

        parsed = parse_markdown_frontmatter(path, path.read_text(), errors)
        if parsed is None:
            continue
        metadata, _ = parsed

        for field in REQUIRED_FORMAL_FRONTMATTER_FIELDS:
            value = metadata.get(field)
            if not isinstance(value, str) or not value.strip():
                add_error(errors, path, f"frontmatter {field!r} must be non-empty")


def validate_prd_related_trd_mirror(
    root: Path,
    errors: list[ContractError],
) -> None:
    # PRD schema and current PRD samples do not define a `related_trd` field.
    # The reverse PRD -> TRD mirror is therefore not machine-checkable without
    # inventing new metadata. Keep this explicitly skipped until the PRD schema
    # adds a canonical `related_trd` contract.
    return


def validate_skill_description_trigger_phrases(
    root: Path,
    errors: list[ContractError],
) -> None:
    """Heuristic guard against non-PM skills reclaiming user entry phrases.

    The denylist is intentionally conservative and should evolve with the
    frontmatter description convention. `pm-agent` remains exempt because it is
    the high-recall public entry for user-side requests.
    """
    for skill_doc in sorted(root.glob("agents/*/skills/*/SKILL.md")):
        parsed = parse_markdown_frontmatter(skill_doc, skill_doc.read_text(), errors)
        if parsed is None:
            continue
        metadata, _ = parsed

        if metadata.get("name") == "pm-agent":
            continue

        description = metadata.get("description", "")
        if not isinstance(description, str):
            continue

        for pattern, label in DESCRIPTION_DENYLIST:
            if pattern.search(description):
                add_error(
                    errors,
                    skill_doc,
                    "frontmatter 'description' must not contain user-trigger "
                    f"phrase pattern {label!r}",
                )


def validate_all(root: Path | None = None) -> list[ContractError]:
    root = root or repo_root()
    errors: list[ContractError] = []
    validate_required_formal_frontmatter(root, errors)
    validate_prd_related_trd_mirror(root, errors)
    validate_skill_description_trigger_phrases(root, errors)
    return errors


def main() -> int:
    root = repo_root()
    errors = validate_all(root)
    if errors:
        print("FAIL: documentation contract violations found", file=sys.stderr)
        for error in errors:
            print(f"- {error.render(root)}", file=sys.stderr)
        return 1

    print("PASS: documentation contract satisfied")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
