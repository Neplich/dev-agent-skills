#!/usr/bin/env python3
"""Validate the shared evals.json contract for all agent skill evals."""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


SCHEMA_VERSION = "1.0"
VALID_AGENTS = {
    "designer",
    "devops",
    "engineer",
    "product_manager",
    "qa",
    "security",
}
EVAL_ID_RE = re.compile(r"^eval-\d{3}-[a-z0-9]+(?:-[a-z0-9]+)*$")
ASSERTION_ID_RE = re.compile(r"^[a-z][a-z0-9_]*$")


@dataclass
class ContractError:
    path: Path
    message: str

    def render(self, root: Path) -> str:
        rel = self.path.relative_to(root).as_posix()
        return f"{rel}: {self.message}"


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def evals_paths(root: Path) -> list[Path]:
    return sorted(root.glob("agents/*/test/*/evals/evals.json"))


def non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def add_error(errors: list[ContractError], path: Path, message: str) -> None:
    errors.append(ContractError(path=path, message=message))


def load_json(path: Path, errors: list[ContractError]) -> dict[str, Any] | None:
    try:
        payload = json.loads(path.read_text())
    except json.JSONDecodeError as exc:
        add_error(errors, path, f"invalid JSON: {exc}")
        return None

    if not isinstance(payload, dict):
        add_error(errors, path, "top-level payload must be an object")
        return None

    return payload


def validate_assertions(
    path: Path,
    eval_index: int,
    assertions: Any,
    errors: list[ContractError],
) -> None:
    if not isinstance(assertions, list) or not assertions:
        add_error(errors, path, f"evals[{eval_index}].assertions must be a non-empty array")
        return

    seen_ids: set[str] = set()
    for assertion_index, assertion in enumerate(assertions):
        prefix = f"evals[{eval_index}].assertions[{assertion_index}]"
        if not isinstance(assertion, dict):
            add_error(errors, path, f"{prefix} must be an object")
            continue

        assertion_id = assertion.get("id")
        if not non_empty_string(assertion_id) or not ASSERTION_ID_RE.fullmatch(assertion_id):
            add_error(errors, path, f"{prefix}.id must be lower snake_case")
        elif assertion_id in seen_ids:
            add_error(errors, path, f"{prefix}.id duplicates {assertion_id!r}")
        else:
            seen_ids.add(assertion_id)

        for field in ("description", "text"):
            if not non_empty_string(assertion.get(field)):
                add_error(errors, path, f"{prefix}.{field} must be a non-empty string")


def validate_eval_item(
    path: Path,
    skill_test_dir: Path,
    eval_index: int,
    item: Any,
    seen_ids: set[str],
    errors: list[ContractError],
) -> None:
    if not isinstance(item, dict):
        add_error(errors, path, f"evals[{eval_index}] must be an object")
        return

    eval_id = item.get("id")
    if not non_empty_string(eval_id) or not EVAL_ID_RE.fullmatch(eval_id):
        add_error(
            errors,
            path,
            f"evals[{eval_index}].id must match eval-NNN-short-slug",
        )
    elif eval_id in seen_ids:
        add_error(errors, path, f"evals[{eval_index}].id duplicates {eval_id!r}")
    else:
        seen_ids.add(eval_id)

    for field in ("name", "description", "prompt", "expected_output"):
        if not non_empty_string(item.get(field)):
            add_error(errors, path, f"evals[{eval_index}].{field} must be a non-empty string")

    if "workspace" not in item:
        add_error(errors, path, f"evals[{eval_index}].workspace must be present")
    else:
        workspace = item["workspace"]
        if workspace is not None:
            if not non_empty_string(workspace) or not workspace.startswith("workspace/"):
                add_error(
                    errors,
                    path,
                    f"evals[{eval_index}].workspace must be null or start with workspace/",
                )
            elif not ((skill_test_dir / workspace).exists() or (path.parent / workspace).exists()):
                add_error(errors, path, f"evals[{eval_index}].workspace does not exist: {workspace}")

    validate_assertions(path, eval_index, item.get("assertions"), errors)


def validate_file(root: Path, path: Path) -> list[ContractError]:
    errors: list[ContractError] = []
    payload = load_json(path, errors)
    if payload is None:
        return errors

    rel_parts = path.relative_to(root).parts
    agent = rel_parts[1]
    skill_name = rel_parts[3]
    skill_test_dir = root / "agents" / agent / "test" / skill_name
    skill_doc = root / "agents" / agent / "skills" / skill_name / "SKILL.md"

    if payload.get("schema_version") != SCHEMA_VERSION:
        add_error(errors, path, f"schema_version must be {SCHEMA_VERSION!r}")

    if payload.get("agent") != agent:
        add_error(errors, path, f"agent must match path agent {agent!r}")

    if agent not in VALID_AGENTS:
        add_error(errors, path, f"agent {agent!r} is not recognized")

    if payload.get("skill_name") != skill_name:
        add_error(errors, path, f"skill_name must match path skill {skill_name!r}")

    if not skill_doc.exists():
        add_error(errors, path, f"missing skill document {skill_doc.relative_to(root).as_posix()}")

    evals = payload.get("evals")
    if not isinstance(evals, list) or not evals:
        add_error(errors, path, "evals must be a non-empty array")
        return errors

    seen_ids: set[str] = set()
    for eval_index, item in enumerate(evals):
        validate_eval_item(path, skill_test_dir, eval_index, item, seen_ids, errors)

    return errors


def validate_all(root: Path | None = None) -> list[ContractError]:
    root = root or repo_root()
    paths = evals_paths(root)
    errors: list[ContractError] = []

    if not paths:
        return [ContractError(root, "no evals.json files found")]

    for path in paths:
        errors.extend(validate_file(root, path))

    return errors


def main() -> int:
    root = repo_root()
    errors = validate_all(root)
    if errors:
        print("FAIL: eval contract violations found", file=sys.stderr)
        for error in errors:
            print(f"- {error.render(root)}", file=sys.stderr)
        return 1

    print("PASS: all agent skill evals satisfy schema v1.0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
