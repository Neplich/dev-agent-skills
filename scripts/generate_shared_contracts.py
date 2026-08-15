#!/usr/bin/env python3
"""Generate plugin-local copies of cross-role contracts."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CONTRACT_NAMES = (
    "handoff-contract.md",
    "closeout-contract.md",
    "security-escalation.md",
    "consumption-contract.md",
)
ROUTER_ROOTS = (
    "agents/designer/skills/designer-agent",
    "agents/engineer/skills/engineer-agent",
    "agents/qa/skills/qa-agent",
    "agents/devops/skills/devops-agent",
    "agents/security/skills/security-agent",
    "agents/docs/skills/docs-agent",
)
GENERATED_SUBDIR = Path("_internal/_generated/shared-contracts")


def source_root(root: Path = REPO_ROOT) -> Path:
    return (
        root
        / "agents"
        / "product_manager"
        / "skills"
        / "idea-to-spec"
        / "_internal"
        / "_shared"
    )


def generated_content(name: str, root: Path = REPO_ROOT) -> str:
    source = source_root(root) / name
    relative_source = source.relative_to(root).as_posix()
    body = source.read_text(encoding="utf-8")
    return (
        "<!-- GENERATED FILE: DO NOT EDIT. "
        f"Source: {relative_source}. -->\n\n{body}"
    )


def expected_files(root: Path = REPO_ROOT) -> dict[Path, str]:
    expected: dict[Path, str] = {}
    for router_root in ROUTER_ROOTS:
        target_dir = root / router_root / GENERATED_SUBDIR
        for name in CONTRACT_NAMES:
            expected[target_dir / name] = generated_content(name, root)
    return expected


def freshness_errors(root: Path = REPO_ROOT) -> list[str]:
    expected = expected_files(root)
    errors: list[str] = []

    for path, content in expected.items():
        relative = path.relative_to(root).as_posix()
        if not path.exists():
            errors.append(f"missing generated contract: {relative}")
        elif path.read_text(encoding="utf-8") != content:
            errors.append(f"stale generated contract: {relative}")

    expected_paths = set(expected)
    for router_root in ROUTER_ROOTS:
        target_dir = root / router_root / GENERATED_SUBDIR
        if not target_dir.exists():
            continue
        for path in target_dir.iterdir():
            if path.is_file() and path not in expected_paths:
                relative = path.relative_to(root).as_posix()
                errors.append(f"extra generated contract: {relative}")

    return errors


def generate(root: Path = REPO_ROOT) -> None:
    for path, content in expected_files(root).items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="report missing, extra, or stale generated contracts without writing",
    )
    args = parser.parse_args()

    if args.check:
        errors = freshness_errors()
        if errors:
            for error in errors:
                print(f"ERROR: {error}")
            return 1
        print("Shared contract copies are fresh.")
        return 0

    generate()
    print(f"Generated {len(expected_files())} shared contract copies.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
