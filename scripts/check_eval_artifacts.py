#!/usr/bin/env python3
"""Fail when committed eval runtime artifacts are present in the worktree."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


BLOCKED_PATTERNS = [
    re.compile(r"(^|/)with_skill/"),
    re.compile(r"(^|/)without_skill/"),
    re.compile(r"(^|/)baseline/"),
    re.compile(r"(^|/)iteration2/"),
    re.compile(r"(^|/)outputs/"),
    re.compile(r"(^|/)diagnostics/"),
    re.compile(r"(^|/)comparison\.auto\.md$"),
    re.compile(r"(^|/)transcript\.md$"),
    re.compile(r"(^|/)candidate-output\.md$"),
    re.compile(r"(^|/)subagent-verdict\.md$"),
    re.compile(r"(^|/)timing\.json$"),
    re.compile(r"(^|/)run_status\.json$"),
]


def tracked_files() -> list[str]:
    result = subprocess.run(
        ["git", "ls-files", "-z", "--", "agents", "tmp/eval-runs"],
        check=True,
        stdout=subprocess.PIPE,
    )
    return [path for path in result.stdout.decode("utf-8").split("\0") if path]


def is_runtime_artifact(path: str) -> bool:
    if path.startswith("tmp/eval-runs/"):
        return True
    if not (path.startswith("agents/") and "/test/" in path):
        return False
    return any(pattern.search(path) for pattern in BLOCKED_PATTERNS)


def main() -> int:
    blocked = [
        path
        for path in tracked_files()
        if Path(path).exists() and is_runtime_artifact(path)
    ]

    if blocked:
        print("FAIL: tracked eval runtime artifacts are present:", file=sys.stderr)
        for path in blocked:
            print(f"- {path}", file=sys.stderr)
        return 1

    print("PASS: no tracked eval runtime artifacts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
