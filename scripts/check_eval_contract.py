#!/usr/bin/env python3
"""Validate the shared evals.json contract for all agent skill evals."""

from __future__ import annotations

import json
import hashlib
import re
import subprocess
import sys
import tempfile
from collections import Counter
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.eval_runtime import git_topology_errors  # noqa: E402


SCHEMA_VERSION = "1.0"
VALID_AGENTS = {"designer", "devops", "docs", "engineer", "product_manager", "qa", "security"}
EVAL_ID_RE = re.compile(r"^eval-\d{3}-[a-z0-9]+(?:-[a-z0-9]+)*$")
ASSERTION_ID_RE = re.compile(r"^[a-z][a-z0-9_]*$")
PATH_LIST_FIELDS = ("fixture_context", "with_skill_outputs", "without_skill_outputs",
                    "baseline_outputs", "baseline_output", "baseline_skill_outputs",
                    "execution_cleanup", "run_diagnostics")
OUTPUT_FIELDS = PATH_LIST_FIELDS[1:6]
RUNNER_ONLY_FIELDS = ("run_diagnostics",)
RUNTIME_DIAGNOSTIC_DIRS = ("diagnostics",)
RUNTIME_DIAGNOSTIC_FILES = ("transcript.md", "candidate-output.md", "subagent-verdict.md",
                            "comparison.auto.md", "timing.json", "run_status.json")
MANUAL_ONLY_SKILLS = {
    ("docs", "manual-gen"): "agents/docs/test/manual-gen/comparison.md",
}
SCENARIO_STRING_FIELDS = ("persona", "situation", "trigger", "goal")
SCENARIO_LIST_FIELDS = ("materials", "constraints", "success_criteria")
RUNTIME_SURFACES = ("processes", "ports", "database", "browser", "login_state", "downloads")
PROMPT_FORBIDDEN_PATTERNS = (
    re.compile(r"用户说\s*[：:]"),
    re.compile(r"\b(?:with_skill|without_skill)\b", re.I),
    re.compile(r"\bassertions?\b", re.I),
    re.compile(r"\bexpected[_ ]output\b", re.I),
    re.compile(r"\bfixture\b", re.I),
    re.compile(r"\beval_metadata\.json\b|\bevals\.json\b", re.I),
    re.compile(r"agents/[a-z0-9_-]+/skills/[a-z0-9_-]+", re.I),
    re.compile(r"\bgpt-[a-z0-9.-]+\b|\breasoning_effort\b", re.I),
    re.compile(r"\bchange_tier\b|\bfeature_path\b", re.I),
    re.compile(r"(?:门禁|gate)\s*(?:视为|已通过|passed)", re.I),
    re.compile(r"\bStep\s*\d+\b.*(?:门禁|gate)", re.I),
)
README_ANSWER_PATTERNS = (
    re.compile(r"\bExpected behavior\s*:", re.I),
    re.compile(r"\bdispatcher should\b", re.I),
    re.compile(r"\bfixture verifies\b", re.I),
    re.compile(r"\beval(?:uation)? workspace\b", re.I),
    re.compile(r"\bthe eval (?:expects|asks)\b", re.I),
    re.compile(r"\bregression target\b", re.I),
)
SKILL_PATH_RE = re.compile(r"agents/([a-z0-9_-]+)/skills/([a-z0-9_-]+)")
INTERNAL_DOC_RE = re.compile(
    r"(?:agents/[a-z0-9_-]+/skills/[a-z0-9_-]+/)?(_internal/[a-zA-Z0-9_./-]+\.md)"
)
FIXTURE_FRONTMATTER_RE = re.compile(
    r"(?im)^\s*(?:author\s*:\s*[\"']?(?:PM|Eval) Fixture|generated_by\s*:\s*[\"']?fixture)[\"']?\s*$"
)
INITIAL_FIXTURE_RE = re.compile(
    r"(?im)^\s*(?:[-*]\s*)?(?:changes?\s*:\s*)?[\"']?Initial fixture[\"']?\s*$"
)
MIGRATION_INVENTORY = Path(
    "docs/engineer/repository-governance/eval-scenario-isolation/"
    "migration-inventory.json"
)
FROZEN_AGENT_COUNTS = {"designer": 11, "devops": 15, "docs": 46, "engineer": 38,
                       "product_manager": 50, "qa": 15, "security": 18}
FROZEN_EVAL_COUNT = 193
FROZEN_SKILL_COUNT = 38
FROZEN_PILOT_COUNT = 7
FROZEN_SOURCE_CONTRACT = {
    "evals_glob": "agents/*/test/*/evals/evals.json",
    "evals_file_count": 38,
    "old_eval_count": 193,
    "identity_key": ["agent", "skill", "old_eval_id"],
    "comparison_stale_marker": "issue-246-stage-0-v1",
    "manual_only_exclusion": "agents/docs/test/manual-gen/comparison.md",
}
RUNNER_AUDIT_FIELDS = {
    "message_source", "candidate_cwd", "home_isolation", "codex_home_isolation",
    "skill_overlay", "fixture_surface", "assertion_expected_output_visibility",
    "runtime_reset", "judge_freshness",
}
AUDIT_STATUSES = {"pass", "fail", "partial", "not_implemented", "not_applicable"}
AUDIT_SURFACES = {
    "designer-runner": ("role_runner", "agents/designer/test/run_eval.py", "compatibility_main"),
    "devops-runner": ("role_runner", "agents/devops/test/run_eval.py", "compatibility_main"),
    "docs-runner": ("role_runner", "agents/docs/test/run_eval.py", "compatibility_main"),
    "product-manager-runner": (
        "role_runner", "agents/product_manager/test/idea-to-spec/run_eval.py", "compatibility_main",
    ),
    "qa-runner": ("role_runner", "agents/qa/test/run_eval.py", "compatibility_main"),
    "pm-transcript-runner": (
        "transcript_runner", "agents/product_manager/test/idea-to-spec/transcript_runner.py",
        "run_selected_eval",
    ),
    "designer-run-all": ("run_all", "agents/designer/test/run_all_evals.py", "run_skill_eval.py"),
    "docs-run-all": ("run_all", "agents/docs/test/run_all_evals.py", "run_skill_eval.py"),
    "qa-run-all": ("run_all", "agents/qa/test/run_all_evals.py", "run_skill_eval.py"),
    "eval-workflow": ("workflow", ".github/workflows/evals.yml", "run_skill_eval.py"),
}
AUDIT_EVIDENCE_ANCHORS = {
    "message_source": "prompt_hash",
    "candidate_cwd": "workspace_root",
    "home_isolation": "context.home",
    "codex_home_isolation": "context.codex_home",
    "skill_overlay": "skill_sources",
    "fixture_surface": "canonical_hash",
    "assertion_expected_output_visibility": 'definition.item["assertions"]',
    "runtime_reset": "runtime_isolation",
    "judge_freshness": 'open_context(materialized, "judge")',
}


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


def validate_metadata(
    evals_path: Path,
    skill_test_dir: Path,
    eval_index: int,
    item: dict[str, Any],
    errors: list[ContractError],
    *,
    strict_new_contract: bool = True,
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

    if strict_new_contract:
        if "prompt" in metadata:
            add_error(errors, metadata_path, "prompt must only be defined in evals.json")

        dependencies = metadata.get("skill_dependencies")
        if not isinstance(dependencies, list):
            add_error(errors, metadata_path, "skill_dependencies must be an array")
        else:
            seen_dependencies: set[str] = set()
            for dependency in dependencies:
                if not isinstance(dependency, str) or not is_safe_relative_path(dependency):
                    add_error(
                        errors,
                        metadata_path,
                        f"skill_dependencies contains unsafe path {dependency!r}",
                    )
                    continue
                if dependency in seen_dependencies:
                    add_error(
                        errors,
                        metadata_path,
                        f"skill_dependencies duplicates {dependency!r}",
                    )
                seen_dependencies.add(dependency)
                parts = PurePosixPath(dependency).parts
                is_skill_dir = len(parts) == 4 and parts[0] == "agents" and parts[2] == "skills"
                is_skill_doc = (
                    len(parts) == 5
                    and parts[0] == "agents"
                    and parts[2] == "skills"
                    and parts[4] == "SKILL.md"
                )
                if not (is_skill_dir or is_skill_doc):
                    add_error(
                        errors,
                        metadata_path,
                        "skill_dependencies entries must use "
                        "agents/{agent}/skills/{skill}[/SKILL.md]",
                    )
                    continue
                dependency_path = evals_path.parents[5] / dependency
                if is_skill_dir:
                    dependency_path /= "SKILL.md"
                if not dependency_path.is_file():
                    add_error(
                        errors,
                        metadata_path,
                        f"skill dependency does not exist: {dependency!r}",
                    )

            skill_root = (
                evals_path.parents[5] / "agents" / evals_path.parents[3].name
                / "skills" / evals_path.parents[1].name
            )
            required = explicit_cross_skill_dependencies(skill_root)
            declared = {value.removesuffix("/SKILL.md") for value in seen_dependencies}
            missing = sorted(required - declared)
            if missing:
                add_error(
                    errors,
                    metadata_path,
                    f"missing explicit cross-skill dependencies: {missing}",
                )

        validate_runtime_isolation(metadata_path, metadata.get("runtime_isolation"), errors)
        for message in git_topology_errors(metadata.get("git_topology"), workspace_root):
            add_error(errors, metadata_path, f"git_topology {message}")

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

    if strict_new_contract:
        validate_candidate_fixture(
            workspace_root, metadata_path, evals_path.parents[1].name, errors,
        )


def explicit_cross_skill_dependencies(skill_root: Path) -> set[str]:
    """Return explicit cross-skill roots from the loaded same-skill instruction graph."""
    target = (skill_root.parents[1].name, skill_root.name)
    pending = [skill_root / "SKILL.md"]
    loaded: set[Path] = set()
    required: set[str] = set()
    while pending:
        path = pending.pop()
        if path in loaded or not path.is_file():
            continue
        loaded.add(path)
        text = path.read_text(encoding="utf-8")
        for agent, skill in SKILL_PATH_RE.findall(text):
            if (agent, skill) != target:
                required.add(f"agents/{agent}/skills/{skill}")
        for relative in INTERNAL_DOC_RE.findall(text):
            candidate = (skill_root / relative).resolve()
            if candidate.is_relative_to(skill_root.resolve()):
                pending.append(candidate)
    return required


def validate_runtime_isolation(
    metadata_path: Path,
    value: Any,
    errors: list[ContractError],
) -> None:
    if not isinstance(value, dict):
        add_error(errors, metadata_path, "runtime_isolation must be an object")
        return
    for surface in RUNTIME_SURFACES:
        state = value.get(surface)
        prefix = f"runtime_isolation.{surface}"
        if state == "not_used":
            continue
        if isinstance(state, dict):
            if state.get("state") not in {"isolated", "reset"}:
                add_error(
                    errors,
                    metadata_path,
                    f"{prefix}.state must be isolated or reset",
                )
            if not non_empty_string(state.get("evidence")):
                add_error(
                    errors,
                    metadata_path,
                    f"{prefix}.evidence must be a non-empty string",
                )
            continue
        add_error(
            errors,
            metadata_path,
            f"{prefix} must be not_used or an isolated/reset evidence object",
        )
    extras = sorted(set(value) - set(RUNTIME_SURFACES))
    if extras:
        add_error(
            errors,
            metadata_path,
            f"runtime_isolation contains unsupported surfaces: {extras}",
        )


def validate_candidate_fixture(
    workspace_root: Path,
    metadata_path: Path,
    skill_name: str,
    errors: list[ContractError],
) -> None:
    for readme in sorted(workspace_root.rglob("README.md")):
        text = readme.read_text(encoding="utf-8")
        if any(pattern.search(text) for pattern in README_ANSWER_PATTERNS):
            add_error(
                errors,
                readme,
                "README contains high-confidence answer guidance",
            )
    for package in sorted(workspace_root.rglob("package.json")):
        text = package.read_text(encoding="utf-8")
        skill_eval = re.compile(
            rf"(?:\b{re.escape(skill_name)}\b.{{0,30}}\beval\b|\beval\b.{{0,30}}\b{re.escape(skill_name)}\b)",
            re.I,
        )
        if re.search(r"\beval(?:uation)? workspace\b", text, re.I) or skill_eval.search(text):
            add_error(errors, package, "package.json contains high-confidence eval marker")
    for document in sorted(workspace_root.rglob("*.md")):
        text = document.read_text(encoding="utf-8")
        frontmatter = text.split("---", 2)[1] if text.startswith("---") and text.count("---") >= 2 else ""
        if FIXTURE_FRONTMATTER_RE.search(frontmatter) or INITIAL_FIXTURE_RE.search(text):
            add_error(errors, document, "document contains high-confidence fixture provenance")


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
    *,
    strict_new_contract: bool = True,
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

    if strict_new_contract:
        validate_scenario(path, eval_index, item.get("scenario"), errors)
        prompt = item.get("prompt")
        if isinstance(prompt, str):
            matches = [
                pattern.pattern for pattern in PROMPT_FORBIDDEN_PATTERNS if pattern.search(prompt)
            ]
            if matches:
                add_error(
                    errors,
                    path,
                    f"evals[{eval_index}].prompt contains forbidden eval scaffolding: {matches}",
                )

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
    validate_metadata(
        path,
        skill_test_dir,
        eval_index,
        item,
        errors,
        strict_new_contract=strict_new_contract,
    )


def validate_scenario(
    path: Path,
    eval_index: int,
    scenario: Any,
    errors: list[ContractError],
) -> None:
    prefix = f"evals[{eval_index}].scenario"
    if not isinstance(scenario, dict):
        add_error(errors, path, f"{prefix} must be an object")
        return
    expected = set(SCENARIO_STRING_FIELDS) | set(SCENARIO_LIST_FIELDS)
    extras = sorted(set(scenario) - expected)
    if extras:
        add_error(errors, path, f"{prefix} contains unsupported fields: {extras}")
    for field in SCENARIO_STRING_FIELDS:
        if not non_empty_string(scenario.get(field)):
            add_error(errors, path, f"{prefix}.{field} must be a non-empty string")
    for field in SCENARIO_LIST_FIELDS:
        value = scenario.get(field)
        if not isinstance(value, list) or not value or not all(
            non_empty_string(item) for item in value
        ):
            add_error(
                errors,
                path,
                f"{prefix}.{field} must be a non-empty array of non-empty strings",
            )


def validate_file(
    root: Path,
    path: Path,
    *,
    complete_identities: set[tuple[str, str, str]] | None = None,
) -> list[ContractError]:
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
        eval_id = item.get("id") if isinstance(item, dict) else None
        strict_new_contract = complete_identities is None or (
            agent,
            skill_name,
            eval_id,
        ) in complete_identities
        validate_eval_item(
            path,
            skill_test_dir,
            eval_index,
            item,
            seen_ids,
            errors,
            strict_new_contract=strict_new_contract,
        )

    return errors


def _safe_inventory_path(root: Path, inventory_path: Path, value: Any) -> Path | None:
    if not isinstance(value, str) or not is_safe_relative_path(value):
        return None
    resolved = (root / value).resolve()
    if resolved != root.resolve() and root.resolve() not in resolved.parents:
        return None
    return resolved


def _comparison_has_fresh_evidence(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    current = re.search(
        r"^##\s*(?:Latest|Current) (?:Result|result)\s*$([\s\S]*?)(?=^##\s|\Z)",
        text,
        re.M,
    )
    current_text = current.group(1) if current else text[:1200]
    if re.search(
        r"(?:Evidence status|Migration status|证据状态|迁移状态)"
        r"[：:]\s*\**(?:STALE|PENDING)\b",
        current_text,
        re.I,
    ):
        return False
    freshness = re.search(
        r"(?:Evidence (?:status|freshness)|证据(?:状态|新鲜度))[：:]\s*\**FRESH\b",
        text,
        re.I,
    )
    preflight = re.search(r"Preflight[^\n]{0,100}\bPASS\b", text, re.I)
    judge = re.search(r"\bfresh\b[^\n]{0,100}\bjudge\b|\bjudge\b[^\n]{0,100}\bfresh\b", text, re.I)
    behavior = re.search(r"Behavior result[：:]\s*\**(?:PASS|FAIL)\b", text, re.I)
    coverage = re.search(r"Coverage result[：:]\s*\**(?:FULL|PARTIAL)\b", text, re.I)
    overall = re.search(
        r"Overall result[：:]\s*\**(?:PASS(?:\s*\(partial coverage\))?|FAIL)\b",
        text,
        re.I,
    )
    return all((freshness, preflight, judge, behavior, coverage, overall))


def _comparison_is_stale_blocked(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    current = re.search(
        r"^##\s*(?:Latest|Current) (?:Result|result)\s*$([\s\S]*?)(?=^##\s|\Z)",
        text,
        re.M,
    )
    current_text = current.group(1) if current else text[:1200]
    return bool(
        re.search(r"\b(?:STALE|PENDING)\b", current_text, re.I)
        and re.search(r"Overall result[：:]\s*\**BLOCKED\b", current_text, re.I)
    )


def current_fixture_hash(definition: Any) -> str:
    from scripts.eval_runtime import copy_canonical_fixture, fixture_manifest, manifest_hash

    with tempfile.TemporaryDirectory(prefix="eval-contract-fixture-") as temp_dir:
        canonical = Path(temp_dir) / "canonical"
        copy_canonical_fixture(
            definition.workspace_root, canonical,
            cleanup_paths=definition.metadata.get("execution_cleanup", []),
        )
        return manifest_hash(fixture_manifest(canonical))


def validate_fresh_comparison_identity(
    root: Path, comparison: Path, agent: str, skill: str, eval_id: str,
    errors: list[ContractError],
) -> None:
    from scripts import run_skill_eval as runner

    try:
        definition = runner.load_eval_definition(root, agent, skill, eval_id)
        identity = runner.source_identity(definition)
        # The full overlay is same-run evidence; dependency content is not a
        # cross-skill historical freshness dependency.
        expected = {
            "Fixture SHA-256": current_fixture_hash(definition),
            "Prompt SHA-256": hashlib.sha256(definition.item["prompt"].encode()).hexdigest(),
            "Eval definition SHA-256": identity["eval_definition_sha256"],
            "Metadata SHA-256": identity["metadata_sha256"],
            "Target skill tree SHA-256": identity["target_skill_sha256"],
            "Judge schema SHA-256": identity["judge_schema_sha256"],
            "Executor SHA-256": identity["executor_sha256"],
            "Runtime SHA-256": identity["runtime_sha256"],
        }
    except (KeyError, OSError, ValueError) as exc:
        add_error(errors, comparison, f"fresh comparison input identity cannot be recomputed: {exc}")
        return
    text = comparison.read_text(encoding="utf-8")
    current = re.search(
        r"^##\s*(?:Latest|Current) (?:Result|result)\s*$([\s\S]*?)(?=^##\s|\Z)",
        text, re.M,
    )
    section = current.group(1) if current else text[:2000]
    stale = [
        label for label, digest in expected.items()
        if not re.search(rf"^- {re.escape(label)}:\s*`{digest}`\s*$", section, re.M)
    ]
    if stale:
        add_error(
            errors, comparison,
            f"fresh comparison input identity is stale: {', '.join(stale)}",
        )


def _complete_inventory_identities(
    root: Path,
) -> set[tuple[str, str, str]] | None:
    path = root / MIGRATION_INVENTORY
    if not path.is_file():
        return None
    try:
        payload = _load_json_unchecked(path)
    except (OSError, json.JSONDecodeError):
        return None
    records = payload.get("old_evals")
    if not isinstance(records, list):
        return None
    complete: set[tuple[str, str, str]] = set()
    for record in records:
        if not isinstance(record, dict) or record.get("migration_status") != "complete":
            continue
        identity = (
            record.get("agent"),
            record.get("skill"),
            record.get("new_eval_id"),
        )
        if all(isinstance(value, str) for value in identity):
            complete.add(identity)
    return complete


def _git_blob(
    root: Path, commit: str, path: str, cache: dict[tuple[str, str], bytes],
) -> bytes | None:
    key = (commit, path)
    if key in cache:
        return cache[key]
    completed = subprocess.run(
        ["git", "show", f"{commit}:{path}"], cwd=root, capture_output=True,
    )
    if completed.returncode != 0:
        return None
    cache[key] = completed.stdout
    return completed.stdout


def validate_frozen_record(
    root: Path, commit: str, record: dict[str, Any],
    cache: dict[tuple[str, str], bytes] | None = None,
) -> list[ContractError]:
    cache = cache if cache is not None else {}
    errors: list[ContractError] = []
    inventory_path = root / MIGRATION_INVENTORY
    index = record.get("old_eval_index")
    pointer = record.get("old_eval_path")
    if not isinstance(index, int) or index < 0 or not isinstance(pointer, str):
        return [ContractError(inventory_path, "frozen old eval index/path is invalid")]
    evals_path, separator, fragment = pointer.partition("#")
    if separator != "#" or fragment != f"/evals/{index}" or not is_safe_relative_path(evals_path):
        errors.append(ContractError(inventory_path, "old_eval_path JSON pointer does not match old_eval_index"))
        return errors
    evals_blob = _git_blob(root, commit, evals_path, cache)
    if evals_blob is None:
        errors.append(ContractError(inventory_path, "old_eval_path is missing from frozen commit"))
    else:
        try:
            items = json.loads(evals_blob).get("evals", [])
            item = items[index]
        except (AttributeError, IndexError, json.JSONDecodeError, TypeError):
            errors.append(ContractError(inventory_path, "old_eval_path cannot be resolved at frozen commit"))
        else:
            if item.get("id") != record.get("old_eval_id"):
                errors.append(ContractError(inventory_path, "old_eval_id does not match frozen JSON pointer"))
            canonical = json.dumps(item, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
            if hashlib.sha256(canonical).hexdigest() != record.get("old_eval_sha256"):
                errors.append(ContractError(inventory_path, "old_eval_sha256 does not match frozen commit"))
    for path_field, hash_field in (
        ("metadata_path", "metadata_sha256_at_freeze"),
        ("comparison_path", "comparison_sha256_before_stale"),
    ):
        relative = record.get(path_field)
        blob = _git_blob(root, commit, relative, cache) if isinstance(relative, str) else None
        if blob is None:
            errors.append(ContractError(inventory_path, f"{path_field} is missing from frozen commit"))
        elif hashlib.sha256(blob).hexdigest() != record.get(hash_field):
            errors.append(ContractError(inventory_path, f"{hash_field} does not match frozen commit"))
    return errors


def validate_runner_audit(
    audit: Any, path: Path, errors: list[ContractError], *, all_evals_complete: bool,
) -> None:
    if not isinstance(audit, dict):
        add_error(errors, path, "runner_audit must be an object")
        return
    fields_contract = audit.get("audit_fields")
    if not isinstance(fields_contract, dict) or set(fields_contract) != RUNNER_AUDIT_FIELDS:
        add_error(errors, path, "runner_audit.audit_fields must define exactly the nine audit fields")
    elif not all(non_empty_string(value) for value in fields_contract.values()):
        add_error(errors, path, "runner_audit.audit_fields descriptions must be non-empty")
    surfaces = audit.get("surfaces")
    if not isinstance(surfaces, list) or len(surfaces) != 10:
        add_error(errors, path, "runner_audit.surfaces must contain exactly 10 entries")
        return
    ids = [surface.get("id") for surface in surfaces if isinstance(surface, dict)]
    if len(ids) != 10 or len(set(ids)) != 10 or not all(non_empty_string(value) for value in ids):
        add_error(errors, path, "runner_audit surface ids must be ten unique non-empty strings")
    expected = {
        (surface_id, kind, relative)
        for surface_id, (kind, relative, _anchor) in AUDIT_SURFACES.items()
    }
    actual = {
        (surface.get("id"), surface.get("kind"), surface.get("path"))
        for surface in surfaces if isinstance(surface, dict)
    }
    if actual != expected:
        add_error(errors, path, "runner_audit surfaces must match the exact runner inventory")
    root = path.parents[len(MIGRATION_INVENTORY.parts) - 1]
    executor_text = "\n".join(
        candidate.read_text(encoding="utf-8")
        for candidate in (root / "scripts/run_skill_eval.py", root / "scripts/eval_runtime.py")
        if candidate.is_file()
    )
    for index, surface in enumerate(surfaces):
        prefix = f"runner_audit.surfaces[{index}]"
        if not isinstance(surface, dict):
            add_error(errors, path, f"{prefix} must be an object")
            continue
        for field in ("kind", "path"):
            if not non_empty_string(surface.get(field)):
                add_error(errors, path, f"{prefix}.{field} must be non-empty")
        surface_path = root / str(surface.get("path", ""))
        if not surface_path.is_file():
            add_error(errors, path, f"{prefix} surface path does not exist")
        if surface.get("audit_status") != "audited":
            add_error(errors, path, f"{prefix} must be audited")
        migration = surface.get("migration_status")
        if migration not in {"pending", "complete"}:
            add_error(errors, path, f"{prefix}.migration_status is invalid")
        fields = surface.get("fields")
        if not isinstance(fields, dict) or set(fields) != RUNNER_AUDIT_FIELDS:
            add_error(errors, path, f"{prefix}.fields must contain exactly the nine audit fields")
            continue
        for name, result in fields.items():
            if not isinstance(result, dict) or set(result) != {"status", "evidence"}:
                add_error(errors, path, f"{prefix}.fields.{name} must contain status and evidence")
                continue
            if result.get("status") not in AUDIT_STATUSES or not non_empty_string(result.get("evidence")):
                add_error(errors, path, f"{prefix}.fields.{name} has invalid status/evidence")
            if migration == "complete" and result.get("status") not in {"pass", "not_applicable"}:
                add_error(errors, path, f"{prefix} is complete but {name} is not passing")
            evidence = str(result.get("evidence", ""))
            if migration == "complete" and (
                "run_skill_eval" not in evidence or AUDIT_EVIDENCE_ANCHORS[name] not in evidence
            ):
                add_error(errors, path, f"{prefix}.fields.{name} complete evidence lacks executor anchor")
            if migration == "complete" and AUDIT_EVIDENCE_ANCHORS[name] not in executor_text:
                add_error(errors, path, f"{prefix}.fields.{name} executor source anchor is missing")
        contract = AUDIT_SURFACES.get(surface.get("id"))
        if migration == "complete" and contract and surface_path.is_file():
            if contract[2] not in surface_path.read_text(encoding="utf-8"):
                add_error(errors, path, f"{prefix} complete surface lacks current source anchor")
        if all_evals_complete and migration != "complete":
            add_error(errors, path, f"{prefix} must be complete after all eval migrations")
    if audit.get("surface_count") != 10 or audit.get("audited_count") != 10:
        add_error(errors, path, "runner_audit count fields must both be 10")


def validate_inventory_freeze_contract(
    root: Path, path: Path, payload: dict[str, Any], errors: list[ContractError],
) -> str | None:
    commit = payload.get("frozen_from_git_commit")
    valid_commit = isinstance(commit, str) and bool(re.fullmatch(r"[0-9a-f]{40}", commit))
    if valid_commit:
        valid_commit = subprocess.run(
            ["git", "cat-file", "-e", f"{commit}^{{commit}}"], cwd=root,
            capture_output=True,
        ).returncode == 0
    if not valid_commit:
        add_error(errors, path, "frozen_from_git_commit must be a real 40-hex commit")
    if payload.get("source_contract") != FROZEN_SOURCE_CONTRACT:
        add_error(errors, path, "source_contract must exactly match the frozen scan contract")
    return commit if valid_commit else None


def validate_migration_inventory(root: Path | None = None) -> list[ContractError]:
    root = (root or repo_root()).resolve()
    path = root / MIGRATION_INVENTORY
    feature_root = path.parent
    errors: list[ContractError] = []
    if not feature_root.exists():
        return errors
    if not path.is_file():
        return [ContractError(path, "Issue #246 migration inventory is missing")]
    payload = load_json(path, errors)
    if payload is None:
        return errors

    required_top = {
        "schema_version",
        "issue",
        "feature",
        "frozen_at",
        "frozen_from_git_commit",
        "source_contract",
        "counts",
        "pilot_seeds",
        "runner_audit",
        "old_evals",
    }
    missing_top = sorted(required_top - set(payload))
    if missing_top:
        add_error(errors, path, f"inventory is missing top-level fields: {missing_top}")
    if payload.get("schema_version") != "1.0":
        add_error(errors, path, "inventory schema_version must be '1.0'")
    if payload.get("issue") != 246:
        add_error(errors, path, "inventory issue must be 246")
    if payload.get("feature") != "eval-scenario-isolation":
        add_error(errors, path, "inventory feature must be 'eval-scenario-isolation'")
    frozen_commit = validate_inventory_freeze_contract(root, path, payload, errors)

    records = payload.get("old_evals")
    if not isinstance(records, list):
        add_error(errors, path, "old_evals must be an array")
        return errors
    if len(records) != FROZEN_EVAL_COUNT:
        add_error(
            errors,
            path,
            f"old_evals must contain exactly {FROZEN_EVAL_COUNT} records",
        )

    required_record = {
        "agent",
        "skill",
        "old_eval_id",
        "old_eval_index",
        "old_eval_path",
        "old_eval_sha256",
        "workspace",
        "metadata_path",
        "metadata_sha256_at_freeze",
        "comparison_path",
        "comparison_sha256_before_stale",
        "disposition",
        "new_eval_id",
        "replacement_refs",
        "reason",
        "pilot",
        "migration_status",
    }
    identities: set[tuple[str, str, str]] = set()
    agent_counts: Counter[str] = Counter()
    skill_counts: Counter[str] = Counter()
    disposition_counts: Counter[str] = Counter()
    status_counts: Counter[str] = Counter()
    pilot_identities: set[tuple[str, str, str]] = set()
    suites: dict[Path, dict[str, Any]] = {}
    frozen_cache: dict[tuple[str, str], bytes] = {}
    for index, record in enumerate(records):
        prefix = f"old_evals[{index}]"
        if not isinstance(record, dict):
            add_error(errors, path, f"{prefix} must be an object")
            continue
        missing = sorted(required_record - set(record))
        if missing:
            add_error(errors, path, f"{prefix} is missing fields: {missing}")
            continue
        if frozen_commit is not None:
            errors.extend(validate_frozen_record(root, frozen_commit, record, frozen_cache))
        agent = record.get("agent")
        skill = record.get("skill")
        old_eval_id = record.get("old_eval_id")
        identity = (agent, skill, old_eval_id)
        if not all(non_empty_string(value) for value in identity):
            add_error(errors, path, f"{prefix} identity fields must be non-empty strings")
            continue
        if identity in identities:
            add_error(errors, path, f"{prefix} duplicates identity {identity}")
        identities.add(identity)
        agent_counts[agent] += 1
        skill_counts[f"{agent}/{skill}"] += 1
        if record.get("pilot") is True:
            pilot_identities.add(identity)
        elif record.get("pilot") is not False:
            add_error(errors, path, f"{prefix}.pilot must be boolean")

        disposition = record.get("disposition")
        if disposition not in {"retained", "merged", "deleted"}:
            add_error(errors, path, f"{prefix}.disposition is invalid")
        else:
            disposition_counts[disposition] += 1
        migration_status = record.get("migration_status")
        if migration_status not in {"pending", "complete"}:
            add_error(errors, path, f"{prefix}.migration_status is invalid")
        else:
            status_counts[migration_status] += 1
        if not non_empty_string(record.get("reason")):
            add_error(errors, path, f"{prefix}.reason must be a non-empty string")
        replacement_refs = record.get("replacement_refs")
        if not isinstance(replacement_refs, list) or not all(
            non_empty_string(item) for item in replacement_refs
        ):
            add_error(errors, path, f"{prefix}.replacement_refs must be an array of strings")
        if disposition in {"merged", "deleted"} and not replacement_refs:
            add_error(errors, path, f"{prefix} merged/deleted record needs replacement_refs")

        evals_value = record.get("old_eval_path")
        evals_rel = evals_value.split("#", 1)[0] if isinstance(evals_value, str) else None
        evals_file = _safe_inventory_path(root, path, evals_rel)
        metadata_file = _safe_inventory_path(root, path, record.get("metadata_path"))
        comparison_file = _safe_inventory_path(root, path, record.get("comparison_path"))
        for label, target in (
            ("old_eval_path", evals_file),
            ("metadata_path", metadata_file),
            ("comparison_path", comparison_file),
        ):
            if target is None or not target.is_file():
                add_error(errors, path, f"{prefix}.{label} must point to an existing file")

        if disposition == "retained":
            new_eval_id = record.get("new_eval_id")
            if not non_empty_string(new_eval_id):
                add_error(errors, path, f"{prefix}.new_eval_id is required for retained evals")
            elif migration_status == "complete" and evals_file and evals_file.is_file():
                suite = suites.setdefault(evals_file, _load_json_unchecked(evals_file))
                current_ids = {item.get("id") for item in suite.get("evals", [])}
                if new_eval_id not in current_ids:
                    add_error(errors, path, f"{prefix}.new_eval_id does not exist in evals.json")
            if migration_status == "complete" and metadata_file and metadata_file.is_file():
                metadata = _load_json_unchecked(metadata_file)
                if metadata.get("eval_id") != new_eval_id:
                    add_error(errors, path, f"{prefix} metadata eval_id does not match new_eval_id")
            if migration_status == "complete" and comparison_file and comparison_file.is_file():
                if not _comparison_has_fresh_evidence(comparison_file):
                    add_error(
                        errors,
                        path,
                        f"{prefix} is complete but comparison lacks fresh preflight/judge evidence",
                    )
                else:
                    validate_fresh_comparison_identity(
                        root, comparison_file, agent, skill, new_eval_id, errors,
                    )
            elif migration_status == "pending" and comparison_file and comparison_file.is_file():
                if not _comparison_is_stale_blocked(comparison_file):
                    add_error(
                        errors,
                        path,
                        f"{prefix} is pending but comparison is not stale/BLOCKED",
                    )

    if dict(agent_counts) != FROZEN_AGENT_COUNTS:
        add_error(errors, path, "computed agent counts do not match the frozen 193 baseline")
    if len(skill_counts) != FROZEN_SKILL_COUNT:
        add_error(errors, path, f"computed skill count must be {FROZEN_SKILL_COUNT}")
    if len(pilot_identities) != FROZEN_PILOT_COUNT:
        add_error(errors, path, f"pilot record count must be {FROZEN_PILOT_COUNT}")

    counts = payload.get("counts")
    if not isinstance(counts, dict):
        add_error(errors, path, "counts must be an object")
    else:
        if counts.get("agents") != dict(agent_counts):
            add_error(errors, path, "counts.agents does not match old_evals")
        if counts.get("skills") != dict(skill_counts):
            add_error(errors, path, "counts.skills does not match old_evals")
        if counts.get("skill_group_count") != len(skill_counts):
            add_error(errors, path, "counts.skill_group_count does not match old_evals")
        if counts.get("old_eval_count") != len(records):
            add_error(errors, path, "counts.old_eval_count does not match old_evals")
        if counts.get("pilot_count") != len(pilot_identities):
            add_error(errors, path, "counts.pilot_count does not match old_evals")
        computed_dispositions = {
            value: disposition_counts[value]
            for value in ("retained", "merged", "deleted")
        }
        computed_statuses = {
            value: status_counts[value] for value in ("pending", "complete")
        }
        if counts.get("dispositions") != computed_dispositions:
            add_error(errors, path, "counts.dispositions does not match old_evals")
        if counts.get("migration_status") != computed_statuses:
            add_error(errors, path, "counts.migration_status does not match old_evals")

    seeds = payload.get("pilot_seeds")
    if not isinstance(seeds, list):
        add_error(errors, path, "pilot_seeds must be an array")
    else:
        seed_identities = {
            (seed.get("agent"), seed.get("skill"), seed.get("old_eval_id"))
            for seed in seeds
            if isinstance(seed, dict)
        }
        if len(seeds) != FROZEN_PILOT_COUNT or seed_identities != pilot_identities:
            add_error(errors, path, "pilot_seeds must exactly match the seven pilot records")

    validate_runner_audit(
        payload.get("runner_audit"), path, errors, all_evals_complete=status_counts["pending"] == 0,
    )

    return errors


def _load_json_unchecked(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    return payload if isinstance(payload, dict) else {}


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
        manual_result = MANUAL_ONLY_SKILLS.get((agent, skill_name))
        if manual_result is not None:
            if expected in eval_path_set:
                errors.append(
                    ContractError(
                        root / expected,
                        f"manual-only skill must not define a conventional eval suite; use {manual_result}",
                    )
                )
            if not (root / manual_result).is_file():
                errors.append(
                    ContractError(
                        skill_doc,
                        f"manual-only skill is missing evaluation result {manual_result}",
                    )
                )
            continue
        if expected not in eval_path_set:
            errors.append(
                ContractError(
                    skill_doc,
                    f"missing eval definition {expected}",
                )
            )

    complete_identities = _complete_inventory_identities(root)
    for path in paths:
        errors.extend(
            validate_file(
                root,
                path,
                complete_identities=complete_identities,
            )
        )

    errors.extend(validate_migration_inventory(root))

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
