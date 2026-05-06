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
PATH_LIST_FIELDS = (
    "fixture_context",
    "with_skill_outputs",
    "without_skill_outputs",
    "baseline_outputs",
    "baseline_output",
    "baseline_skill_outputs",
    "execution_cleanup",
    "run_diagnostics",
)


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


def skill_paths(root: Path) -> list[Path]:
    return sorted(root.glob("agents/*/skills/*/SKILL.md"))


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


def is_safe_relative_path(value: str) -> bool:
    if not value.strip():
        return False
    path = Path(value)
    return not path.is_absolute() and ".." not in path.parts


def resolve_workspace_root(
    evals_path: Path,
    skill_test_dir: Path,
    workspace: str,
) -> Path:
    direct = skill_test_dir / workspace
    if direct.exists():
        return direct
    return evals_path.parent / workspace


def flatten_path_specs(value: Any) -> list[str] | None:
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        paths: list[str] = []
        for item in value:
            flattened = flatten_path_specs(item)
            if flattened is None:
                return None
            paths.extend(flattened)
        return paths
    return None


def validate_paths_stay_in_workspace(
    metadata_path: Path,
    workspace_root: Path,
    field: str,
    value: Any,
    errors: list[ContractError],
) -> None:
    paths = flatten_path_specs(value)
    if paths is None:
        add_error(errors, metadata_path, f"{field} must be a string or nested array of strings")
        return

    workspace_root = workspace_root.resolve()
    for rel in paths:
        if not is_safe_relative_path(rel):
            add_error(errors, metadata_path, f"{field} contains unsafe path {rel!r}")
            continue
        target = (workspace_root / rel).resolve()
        if target != workspace_root and workspace_root not in target.parents:
            add_error(errors, metadata_path, f"{field} escapes eval workspace: {rel!r}")


def validate_metadata(
    evals_path: Path,
    skill_test_dir: Path,
    eval_index: int,
    item: dict[str, Any],
    errors: list[ContractError],
) -> None:
    eval_id = item.get("id")
    workspace = item.get("workspace")
    if not isinstance(eval_id, str) or not isinstance(workspace, str):
        return

    workspace_root = resolve_workspace_root(evals_path, skill_test_dir, workspace)
    metadata_path = workspace_root / "eval_metadata.json"
    comparison_path = workspace_root / "comparison.md"

    if not metadata_path.exists():
        add_error(errors, evals_path, f"evals[{eval_index}] workspace is missing eval_metadata.json")
        return
    if not comparison_path.exists():
        add_error(errors, evals_path, f"evals[{eval_index}] workspace is missing durable comparison.md")

    metadata = load_json(metadata_path, errors)
    if metadata is None:
        return

    if metadata.get("eval_id") != eval_id:
        add_error(errors, metadata_path, f"eval_id must match evals.json id {eval_id!r}")

    metadata_workspace_root = metadata.get("workspace_root")
    if metadata_workspace_root is not None:
        if not isinstance(metadata_workspace_root, str) or not is_safe_relative_path(metadata_workspace_root):
            add_error(errors, metadata_path, "workspace_root must be a safe relative path")
        else:
            resolved = (evals_path.parents[5] / metadata_workspace_root).resolve()
            if resolved != workspace_root.resolve():
                add_error(errors, metadata_path, "workspace_root must point to the eval workspace")

    for field in PATH_LIST_FIELDS:
        if field in metadata:
            validate_paths_stay_in_workspace(
                metadata_path,
                workspace_root,
                field,
                metadata[field],
                errors,
            )


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
    validate_metadata(path, skill_test_dir, eval_index, item, errors)


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

    eval_path_set = {path.relative_to(root).as_posix() for path in paths}
    for skill_doc in skill_paths(root):
        rel_parts = skill_doc.relative_to(root).parts
        agent = rel_parts[1]
        skill_name = rel_parts[3]
        expected = f"agents/{agent}/test/{skill_name}/evals/evals.json"
        if expected not in eval_path_set:
            errors.append(
                ContractError(
                    skill_doc,
                    f"missing eval definition {expected}",
                )
            )

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
