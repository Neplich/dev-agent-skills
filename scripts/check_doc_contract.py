#!/usr/bin/env python3
"""Validate selected document metadata and local Markdown links."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

from check_repository_contract import (
    ContractError, add_error, markdown_frontmatter_block,
    parse_markdown_frontmatter, repo_root, tracked_files,
)

# Values from idea-to-spec/_internal/_shared/output-conventions.md.
FORMAL_DOCUMENT_STATUSES = ("Draft", "In Review", "Approved", "Superseded", "Deprecated")
FORMAL_DOCUMENT_TYPES = {"PRD", "TRD", "ADR", "API", "TEST_SPEC", "DECISIONS"}
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
ATX_HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$")
LINK_SOURCE_EXCLUSIONS = ("/assets/", "/test/", "/_internal/_generated/")


def validate_formal_document_metadata(root: Path, errors: list[ContractError]) -> None:
    for rel in tracked_files(root):
        if not rel.startswith("docs/") or not rel.endswith(".md"):
            continue
        path = root / rel
        if not path.is_file():
            continue
        content = path.read_text(encoding="utf-8")
        has_header = content.startswith("---\n")
        named_formal = path.stem in FORMAL_DOCUMENT_TYPES
        if not has_header and not named_formal:
            continue
        parsed = parse_markdown_frontmatter(path, content, errors)
        if parsed is None:
            continue
        metadata = {}
        for line in markdown_frontmatter_block(content).splitlines():
            if line.startswith((" ", "\t", "-")) or ":" not in line:
                continue
            key, value = line.split(":", 1)
            metadata[key.strip()] = normalize_frontmatter_scalar(value)
        if not named_formal and metadata.get("type") not in FORMAL_DOCUMENT_TYPES:
            continue
        for field in ("title", "type", "status"):
            if not metadata.get(field):
                add_error(errors, path, f"frontmatter {field!r} must be non-empty")
        status = metadata.get("status", "")
        if status and status not in FORMAL_DOCUMENT_STATUSES:
            add_error(
                errors, path,
                f"frontmatter 'status' must be one of {', '.join(FORMAL_DOCUMENT_STATUSES)};"
                f" got {status!r}",
            )


def validate_all(root: Path | None = None) -> list[ContractError]:
    root = root or repo_root()
    errors: list[ContractError] = []
    validate_formal_document_metadata(root, errors)
    validate_markdown_links(root, errors)
    return errors


def normalize_frontmatter_scalar(value: str) -> str:
    normalized = value.strip()
    if normalized.startswith(("'", '"')):
        quote = normalized[0]
        closing_quote = normalized.find(quote, 1)
        if closing_quote == -1:
            return ""
        return normalized[1:closing_quote].strip()
    normalized = re.split(r"(?:^|\s+)#", normalized, maxsplit=1)[0].strip()
    return "" if normalized in ("|", ">") else normalized


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
