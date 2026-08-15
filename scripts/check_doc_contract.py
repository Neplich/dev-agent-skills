#!/usr/bin/env python3
"""Validate documentation contracts not owned by repository/eval checkers."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

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


IMPLEMENTATION_PLAN_ARCHIVE_RE = re.compile(
    r"^docs/engineer/"
    r"(?:[a-z0-9]+(?:-[a-z0-9]+)*/)+"
    r"archive/IMPLEMENTATION_PLAN-[a-z0-9]+(?:-[a-z0-9]+)*\.md$"
)
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
ATX_HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$")
LINK_SOURCE_EXCLUSIONS = (
    "/archive/",
    "docs/changelog/",
    "/evals/fixtures/",
    "/evals/workspace/",
    "/assets/",
    "/test/",
    "/_internal/_generated/",
)


def is_implementation_plan_artifact_path(rel: str) -> bool:
    return (
        rel.endswith("/IMPLEMENTATION_PLAN.md")
        or IMPLEMENTATION_PLAN_ARCHIVE_RE.fullmatch(rel) is not None
    )


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


def is_active_link_source(rel: str) -> bool:
    if not rel.endswith(".md"):
        return False
    return not any(
        marker in rel if marker.startswith("/") else rel.startswith(marker)
        for marker in LINK_SOURCE_EXCLUSIONS
    )


def markdown_without_code(content: str) -> str:
    kept: list[str] = []
    fence: str | None = None
    for line in content.splitlines():
        stripped = line.lstrip()
        marker = stripped[:3]
        if marker in {"```", "~~~"}:
            fence = None if fence == marker else marker if fence is None else fence
            continue
        if fence is None:
            kept.append(re.sub(r"`[^`\n]*`", "", line))
    return "\n".join(kept)


def github_heading_slugs(content: str) -> set[str]:
    counts: dict[str, int] = {}
    slugs: set[str] = set()
    for line in markdown_without_code(content).splitlines():
        match = ATX_HEADING_RE.match(line)
        if match is None:
            continue
        heading = re.sub(r"<[^>]+>", "", match.group(1)).strip().lower()
        base = re.sub(r"[^\w\- ]", "", heading)
        base = re.sub(r"\s+", "-", base)
        occurrence = counts.get(base, 0)
        slug = base if occurrence == 0 else f"{base}-{occurrence}"
        counts[base] = occurrence + 1
        slugs.add(slug)
    return slugs


def link_destination(raw: str) -> str:
    value = raw.strip()
    if value.startswith("<") and ">" in value:
        return value[1 : value.index(">")]
    return value.split(maxsplit=1)[0]


def validate_markdown_links(root: Path, errors: list[ContractError]) -> None:
    root_resolved = root.resolve()
    for rel in tracked_files(root):
        if not is_active_link_source(rel):
            continue
        source = root / rel
        if not source.exists():
            continue
        content = source.read_text(encoding="utf-8")
        for match in MARKDOWN_LINK_RE.finditer(markdown_without_code(content)):
            destination = unquote(link_destination(match.group(1)))
            if not destination or re.match(
                r"^(?:https?|mailto|tel|data):", destination, re.IGNORECASE
            ):
                continue
            target_text, separator, fragment = destination.partition("#")
            target_text = target_text.split("?", 1)[0]
            if target_text.startswith("/"):
                target = root / target_text.lstrip("/")
            elif target_text:
                target = source.parent / target_text
            else:
                target = source
            try:
                resolved = target.resolve(strict=False)
                resolved.relative_to(root_resolved)
            except ValueError:
                add_error(
                    errors,
                    source,
                    f"local Markdown link escapes repository: {destination!r}",
                )
                continue
            if not resolved.exists():
                add_error(
                    errors,
                    source,
                    f"local Markdown link target does not exist: {destination!r}",
                )
                continue
            if separator and fragment and resolved.is_file():
                anchor = fragment.lower()
                if anchor not in github_heading_slugs(
                    resolved.read_text(encoding="utf-8")
                ):
                    add_error(
                        errors,
                        source,
                        f"local Markdown link anchor does not exist: {destination!r}",
                    )


def validate_all(root: Path | None = None) -> list[ContractError]:
    root = root or repo_root()
    errors: list[ContractError] = []
    validate_required_formal_frontmatter(root, errors)
    validate_prd_related_trd_mirror(root, errors)
    validate_skill_description_trigger_phrases(root, errors)
    validate_markdown_links(root, errors)
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
