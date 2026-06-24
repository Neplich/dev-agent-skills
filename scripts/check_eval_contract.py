#!/usr/bin/env python3
"""Validate the shared evals.json contract for all agent skill evals."""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
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
OUTPUT_FIELDS = (
    "with_skill_outputs",
    "without_skill_outputs",
    "baseline_outputs",
    "baseline_output",
    "baseline_skill_outputs",
)
RUNNER_ONLY_FIELDS = (
    "run_diagnostics",
)
RUNTIME_DIAGNOSTIC_DIRS = (
    "diagnostics",
)
RUNTIME_DIAGNOSTIC_FILES = (
    "transcript.md",
    "candidate-output.md",
    "subagent-verdict.md",
    "comparison.auto.md",
    "timing.json",
    "run_status.json",
)
LATEST_PASS_RE = re.compile(r"(?im)^\s*-\s*Latest result:\s*PASS\b")
BASELINE_HEADING_RE = re.compile(
    r"^(#{2,6})\s+(?:Without Skill / Baseline|Without Skill|Baseline)\s*$",
    re.IGNORECASE,
)
HEADING_RE = re.compile(r"^(#{1,6})\s+\S")
WEAK_BASELINE_PATTERNS = (
    (
        re.compile(r"\bBaseline behavior is diagnostic only\.", re.IGNORECASE),
        "baseline is diagnostic-only",
    ),
    (
        re.compile(r"\bBaseline behavior remains diagnostic:", re.IGNORECASE),
        "baseline remains diagnostic-only",
    ),
    (
        re.compile(
            r"^\s*-\s*(?:BLOCKED|SKIPPED)\b"
            r"|\b(?:baseline|without_skill)[^\n.]{0,80}\b"
            r"(?:was|is|were|remains)\s+(?:blocked|skipped)\b"
            r"|\b(?:blocked|skipped)[^\n.]{0,80}\b(?:baseline|without_skill)\b",
            re.IGNORECASE | re.MULTILINE,
        ),
        "baseline is blocked or skipped",
    ),
    (
        re.compile(
            r"\b(?:baseline|without_skill)[^\n.]{0,80}\b(?:not generated|not run)\b"
            r"|\b(?:not generated|not run)[^\n.]{0,80}\b(?:baseline|without_skill)\b",
            re.IGNORECASE,
        ),
        "baseline is not generated or not run",
    ),
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


def has_non_empty_output_paths(metadata: dict[str, Any]) -> bool:
    for field in OUTPUT_FIELDS:
        if field not in metadata:
            continue
        paths = flatten_path_specs(metadata[field])
        if paths is not None and any(path.strip() for path in paths):
            return True
    return False


def is_runtime_diagnostic_path(value: str) -> bool:
    parts = PurePosixPath(value).parts
    return any(part in RUNTIME_DIAGNOSTIC_DIRS for part in parts) or any(
        part in RUNTIME_DIAGNOSTIC_FILES for part in parts
    )


def validate_paths_stay_in_workspace(
    metadata_path: Path,
    workspace_root: Path,
    field: str,
    value: Any,
    errors: list[ContractError],
    *,
    forbid_runtime_diagnostics: bool = False,
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
        if forbid_runtime_diagnostics and is_runtime_diagnostic_path(rel):
            add_error(
                errors,
                metadata_path,
                f"{field} must not reference runtime diagnostic output {rel!r}",
            )


def validate_metadata_assertion_targets(
    metadata_path: Path,
    workspace_root: Path,
    metadata: dict[str, Any],
    errors: list[ContractError],
) -> None:
    assertions = metadata.get("assertions", [])
    if not isinstance(assertions, list):
        return

    for index, assertion in enumerate(assertions):
        if isinstance(assertion, dict) and "target" in assertion:
            validate_paths_stay_in_workspace(
                metadata_path,
                workspace_root,
                f"assertions[{index}].target",
                assertion["target"],
                errors,
                forbid_runtime_diagnostics=True,
            )


def baseline_sections(text: str) -> list[str]:
    lines = text.splitlines()
    sections: list[str] = []
    index = 0

    while index < len(lines):
        match = BASELINE_HEADING_RE.match(lines[index])
        if not match:
            index += 1
            continue

        heading_level = len(match.group(1))
        section_lines = [lines[index]]
        index += 1
        while index < len(lines):
            next_heading = HEADING_RE.match(lines[index])
            if next_heading and len(next_heading.group(1)) <= heading_level:
                break
            section_lines.append(lines[index])
            index += 1
        sections.append("\n".join(section_lines))

    return sections


def validate_comparison(path: Path, errors: list[ContractError]) -> None:
    text = path.read_text()
    if not LATEST_PASS_RE.search(text):
        return

    sections = baseline_sections(text)
    if not sections:
        add_error(errors, path, "Latest result PASS requires a baseline section")
        return

    baseline_text = "\n\n".join(sections)
    for pattern, reason in WEAK_BASELINE_PATTERNS:
        if pattern.search(baseline_text):
            add_error(
                errors,
                path,
                "Latest result PASS cannot be paired with explicit missing or "
                f"blocked baseline state; found {reason}",
            )


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
    else:
        validate_comparison(comparison_path, errors)

    metadata = load_json(metadata_path, errors)
    if metadata is None:
        return

    if metadata.get("eval_id") != eval_id:
        add_error(errors, metadata_path, f"eval_id must match evals.json id {eval_id!r}")

    if "validation_method" in metadata:
        add_error(errors, metadata_path, "validation_method must not be committed in eval metadata")

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
                forbid_runtime_diagnostics=(
                    field in OUTPUT_FIELDS or field == "run_diagnostics"
                ),
            )

    validate_metadata_assertion_targets(metadata_path, workspace_root, metadata, errors)

    if not has_non_empty_output_paths(metadata):
        for field in RUNNER_ONLY_FIELDS:
            if field in metadata:
                add_error(
                    errors,
                    metadata_path,
                    f"{field} requires deterministic runner outputs",
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
        if not non_empty_string(workspace) or not workspace.startswith("workspace/"):
            add_error(
                errors,
                path,
                f"evals[{eval_index}].workspace must be a non-empty string starting with workspace/",
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
