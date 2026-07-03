#!/usr/bin/env python3
"""Validate repository-level contracts that are cheap to run locally."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


SKILL_NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LOCK_HASH_RE = re.compile(r"^[0-9a-f]{64}$")
SEMVER_CORE_PATTERN = r"(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)"
SEMVER_PRERELEASE_IDENTIFIER_PATTERN = (
    r"(?:0|[1-9]\d*|\d*[A-Za-z-][0-9A-Za-z-]*)"
)
SEMVER_PRERELEASE_PATTERN = (
    rf"{SEMVER_PRERELEASE_IDENTIFIER_PATTERN}"
    rf"(?:\.{SEMVER_PRERELEASE_IDENTIFIER_PATTERN})*"
)
SEMVER_PATTERN = rf"{SEMVER_CORE_PATTERN}(?:-{SEMVER_PRERELEASE_PATTERN})?"
SEMVER_RE = re.compile(rf"^{SEMVER_PATTERN}$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
CHANGELOG_VERSION_RE = re.compile(rf"^changelog-v({SEMVER_PATTERN})\.md$")
FEATURE_PATH_SEGMENT_PATTERN = r"[a-z0-9]+(?:-[a-z0-9]+)*"
IMPLEMENTATION_PLAN_RE = re.compile(
    rf"^docs/engineer/"
    rf"(?P<feature_path>{FEATURE_PATH_SEGMENT_PATTERN}"
    rf"(?:/{FEATURE_PATH_SEGMENT_PATTERN})*)"
    rf"/IMPLEMENTATION_PLAN\.md$"
)
IMPLEMENTATION_PLAN_ARCHIVE_RE = re.compile(
    rf"^docs/engineer/"
    rf"(?P<feature_path>{FEATURE_PATH_SEGMENT_PATTERN}"
    rf"(?:/{FEATURE_PATH_SEGMENT_PATTERN})*?)"
    rf"/implementation-plans/archive/"
    rf"IMPLEMENTATION_PLAN-(?P<scope>{FEATURE_PATH_SEGMENT_PATTERN})\.md$"
)
ARCHIVE_STATUS_VALUES = {"Archived", "Superseded"}
PM_PRD_RE = re.compile(
    rf"^docs/pm/"
    rf"(?P<feature_path>{FEATURE_PATH_SEGMENT_PATTERN}"
    rf"(?:/{FEATURE_PATH_SEGMENT_PATTERN})*)"
    rf"/PRD\.md$"
)
ENGINEER_TRD_RE = re.compile(
    rf"^docs/engineer/"
    rf"(?P<feature_path>{FEATURE_PATH_SEGMENT_PATTERN}"
    rf"(?:/{FEATURE_PATH_SEGMENT_PATTERN})*)"
    rf"/TRD\.md$"
)
BLOCKED_TRACKED_PATTERNS = (
    re.compile(r"(^|/)\.DS_Store$"),
    re.compile(r"(^|/)\.pytest_cache(/|$)"),
    re.compile(r"(^|/)__pycache__(/|$)"),
    re.compile(r"\.pyc$"),
    re.compile(r"^docs/superpowers(/|$)"),
)
PLACEHOLDER_AUTHOR_VALUES = {"AI Assistant", "TBD", "TODO", "Unknown", "N/A"}
TEMPLATE_PLACEHOLDER_RE = re.compile(r"<[^<>]+>")


@dataclass
class ContractError:
    path: Path
    message: str

    def render(self, root: Path) -> str:
        try:
            rel = self.path.relative_to(root).as_posix()
        except ValueError:
            rel = self.path.as_posix()
        return f"{rel}: {self.message}"


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def add_error(errors: list[ContractError], path: Path, message: str) -> None:
    errors.append(ContractError(path=path, message=message))


def load_json(path: Path, errors: list[ContractError]) -> Any | None:
    try:
        return json.loads(path.read_text())
    except json.JSONDecodeError as exc:
        add_error(errors, path, f"invalid JSON: {exc}")
    except OSError as exc:
        add_error(errors, path, f"cannot read JSON: {exc}")
    return None


def is_safe_relative_path(value: str) -> bool:
    if not value.strip():
        return False
    path = Path(value)
    return not path.is_absolute() and ".." not in path.parts


def validate_claude_symlink(root: Path, errors: list[ContractError]) -> None:
    path = root / "CLAUDE.md"
    if not path.is_symlink():
        add_error(errors, path, "must be a relative symlink to AGENTS.md")
        return

    target = Path(path.readlink())
    if target.is_absolute() or target.as_posix() != "AGENTS.md":
        add_error(errors, path, "must point to AGENTS.md using a relative symlink")


def parse_frontmatter(path: Path, errors: list[ContractError]) -> dict[str, str] | None:
    lines = path.read_text().splitlines()
    if not lines or lines[0].strip() != "---":
        add_error(errors, path, "missing YAML frontmatter")
        return None

    fields: dict[str, str] = {}
    for line_number, line in enumerate(lines[1:], start=2):
        if line.strip() == "---":
            return fields
        if not line.strip():
            continue
        if line.startswith((" ", "\t")) or ":" not in line:
            add_error(errors, path, f"unsupported frontmatter line {line_number}")
            return None
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if not key:
            add_error(errors, path, f"empty frontmatter key on line {line_number}")
            return None
        if (
            len(value) >= 2
            and value[0] == value[-1]
            and value[0] in {'"', "'"}
        ):
            value = value[1:-1]
        fields[key] = value

    add_error(errors, path, "unterminated YAML frontmatter")
    return None


def parse_markdown_frontmatter(
    path: Path,
    content: str,
    errors: list[ContractError] | None = None,
) -> tuple[dict[str, str], str] | None:
    lines = content.splitlines()
    if not lines or lines[0].strip() != "---":
        if errors is not None:
            add_error(errors, path, "missing YAML frontmatter")
        return None

    end_index: int | None = None
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end_index = index
            break

    if end_index is None:
        if errors is not None:
            add_error(errors, path, "unterminated YAML frontmatter")
        return None

    fields: dict[str, str] = {}
    for line in lines[1:end_index]:
        if not line.strip() or line.startswith((" ", "\t", "-")) or ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if not key:
            continue
        if (
            len(value) >= 2
            and value[0] == value[-1]
            and value[0] in {'"', "'"}
        ):
            value = value[1:-1]
        fields[key] = value

    body = "\n".join(lines[end_index + 1 :])
    return fields, body


def validate_skill(root: Path, skill_dir: Path, errors: list[ContractError]) -> None:
    skill_doc = skill_dir / "SKILL.md"
    if not skill_doc.exists():
        add_error(errors, skill_doc, "registered skill is missing SKILL.md")
        return

    metadata = parse_frontmatter(skill_doc, errors)
    if metadata is None:
        return

    for field in ("name", "description"):
        value = metadata.get(field)
        if not isinstance(value, str) or not value.strip():
            add_error(errors, skill_doc, f"frontmatter {field!r} must be non-empty")

    name = metadata.get("name", "")
    if name != skill_dir.name:
        add_error(errors, skill_doc, "frontmatter name must match the skill directory")
    if not SKILL_NAME_RE.fullmatch(name):
        add_error(errors, skill_doc, "frontmatter name must use lowercase letters, digits, and hyphens only")


def prerelease_identifier_key(identifier: str) -> tuple[int, int | str]:
    if identifier.isdigit():
        return 0, int(identifier)
    return 1, identifier


def prerelease_key(prerelease: str) -> tuple[tuple[int, int | str], ...]:
    if not prerelease:
        return ()
    return tuple(
        prerelease_identifier_key(identifier)
        for identifier in prerelease.split(".")
    )


def semver_key(version: str) -> tuple[int, int, int, int, tuple[tuple[int, int | str], ...]]:
    core, _, prerelease = version.partition("-")
    major, minor, patch = (int(part) for part in core.split("."))
    release_rank = 0 if prerelease else 1
    return major, minor, patch, release_rank, prerelease_key(prerelease)


def latest_changelog_version(
    root: Path,
    errors: list[ContractError] | None = None,
) -> str | None:
    versions: list[str] = []
    changelog_dir = root / "docs" / "changelog"
    if not changelog_dir.exists():
        return None

    for path in changelog_dir.iterdir():
        if not path.name.startswith("changelog-v"):
            continue
        match = CHANGELOG_VERSION_RE.fullmatch(path.name)
        if match is None:
            if errors is not None:
                add_error(
                    errors,
                    path,
                    "changelog filename must use changelog-v{SemVer}.md",
                )
            continue
        if not path.is_file():
            if errors is not None:
                add_error(errors, path, "changelog entry must be a file")
            continue
        versions.append(match.group(1))

    if not versions:
        return None
    return max(versions, key=semver_key)


def validate_root_changelog_entry(
    root: Path,
    metadata_version: str,
    errors: list[ContractError],
) -> None:
    path = root / "CHANGELOG.md"
    expected_link = f"docs/changelog/changelog-v{metadata_version}.md"
    try:
        content = path.read_text()
    except OSError as exc:
        add_error(errors, path, f"cannot read changelog index: {exc}")
        return

    if expected_link not in content:
        add_error(
            errors,
            path,
            f"must reference {expected_link} for marketplace metadata.version",
        )


def validate_marketplace(root: Path, errors: list[ContractError]) -> None:
    path = root / ".claude-plugin" / "marketplace.json"
    payload = load_json(path, errors)
    if not isinstance(payload, dict):
        add_error(errors, path, "top-level payload must be an object")
        return

    plugins = payload.get("plugins")
    if not isinstance(plugins, list):
        add_error(errors, path, "plugins must be an array")
        return

    metadata = payload.get("metadata")
    if not isinstance(metadata, dict):
        add_error(errors, path, "metadata must be an object")
    else:
        metadata_version = metadata.get("version")
        metadata_version_valid = (
            isinstance(metadata_version, str)
            and SEMVER_RE.fullmatch(metadata_version) is not None
        )
        if not metadata_version_valid:
            add_error(errors, path, "metadata.version must be SemVer without a leading 'v'")
        latest_version = latest_changelog_version(root, errors)
        if latest_version is None:
            add_error(
                errors,
                path,
                "docs/changelog must contain at least one changelog-v{version}.md file",
            )
        elif metadata_version_valid and metadata_version != latest_version:
            add_error(
                errors,
                path,
                f"metadata.version must match latest changelog version {latest_version!r}",
            )
        elif metadata_version_valid:
            validate_root_changelog_entry(root, metadata_version, errors)

    for index, plugin in enumerate(plugins):
        if not isinstance(plugin, dict):
            add_error(errors, path, f"plugins[{index}] must be an object")
            continue

        source = plugin.get("source")
        if not isinstance(source, str) or not source.strip():
            add_error(errors, path, f"plugins[{index}].source must be a non-empty string")
            continue

        source_path = (root / source).resolve()
        if not source_path.exists():
            add_error(errors, root / source, f"plugins[{index}].source does not exist")
            continue

        skills = plugin.get("skills")
        if not isinstance(skills, list):
            add_error(errors, path, f"plugins[{index}].skills must be an array")
            continue

        for skill_index, skill in enumerate(skills):
            if not isinstance(skill, str) or not skill.strip():
                add_error(errors, path, f"plugins[{index}].skills[{skill_index}] must be a non-empty string")
                continue
            skill_dir = (source_path / skill).resolve()
            if not skill_dir.exists():
                add_error(errors, Path(source) / skill, "registered skill path does not exist")
                continue
            validate_skill(root, skill_dir, errors)


def marketplace_skill_sources(root: Path, errors: list[ContractError]) -> dict[str, str]:
    path = root / ".claude-plugin" / "marketplace.json"
    payload = load_json(path, errors)
    if not isinstance(payload, dict):
        return {}

    plugins = payload.get("plugins")
    if not isinstance(plugins, list):
        return {}

    sources: dict[str, str] = {}
    for plugin in plugins:
        if not isinstance(plugin, dict):
            continue

        source = plugin.get("source")
        skills = plugin.get("skills")
        if not isinstance(source, str) or not isinstance(skills, list):
            continue

        for skill in skills:
            if not isinstance(skill, str):
                continue
            skill_dir = (root / source / skill).resolve()
            try:
                rel = skill_dir.relative_to(root).as_posix()
            except ValueError:
                continue
            sources[skill_dir.name] = rel

    return sources


def tracked_files_under(root: Path, rel_dir: str) -> list[str]:
    result = subprocess.run(
        ["git", "ls-files", "-z", "--", rel_dir],
        cwd=root,
        check=True,
        stdout=subprocess.PIPE,
    )
    return [path for path in result.stdout.decode("utf-8").split("\0") if path]


def compute_tracked_directory_hash(root: Path, rel_dir: str) -> str:
    digest = hashlib.sha256()
    prefix = f"{rel_dir.rstrip('/')}/"

    for rel_path in sorted(tracked_files_under(root, rel_dir)):
        if not rel_path.startswith(prefix):
            continue
        local_rel = rel_path[len(prefix):]
        digest.update(local_rel.encode("utf-8"))
        digest.update(b"\0")
        digest.update((root / rel_path).read_bytes())
        digest.update(b"\0")

    return digest.hexdigest()


def validate_skills_lock(root: Path, errors: list[ContractError]) -> None:
    path = root / "skills-lock.json"
    payload = load_json(path, errors)
    if not isinstance(payload, dict):
        add_error(errors, path, "top-level payload must be an object")
        return

    skills = payload.get("skills")
    if not isinstance(skills, dict):
        add_error(errors, path, "skills must be an object")
        return

    expected_sources = marketplace_skill_sources(root, errors)
    expected_names = set(expected_sources)
    actual_names = set(skills)

    for missing in sorted(expected_names - actual_names):
        add_error(errors, path, f"missing lock entry for skill {missing!r}")

    for extra in sorted(actual_names - expected_names):
        add_error(errors, path, f"lock entry has no marketplace skill {extra!r}")

    for name in sorted(expected_names & actual_names):
        entry = skills[name]
        if not isinstance(entry, dict):
            add_error(errors, path, f"skills[{name!r}] must be an object")
            continue

        source = entry.get("source")
        if not isinstance(source, str) or not is_safe_relative_path(source):
            add_error(errors, path, f"skills[{name!r}].source must be a safe relative path")
        elif source != expected_sources[name]:
            add_error(
                errors,
                path,
                f"skills[{name!r}].source must be {expected_sources[name]!r}",
            )
        elif not (root / source).exists():
            add_error(errors, root / source, f"skills[{name!r}].source does not exist")

        if entry.get("sourceType") != "local":
            add_error(errors, path, f"skills[{name!r}].sourceType must be 'local'")

        computed_hash = entry.get("computedHash")
        if not isinstance(computed_hash, str) or not LOCK_HASH_RE.fullmatch(computed_hash):
            add_error(errors, path, f"skills[{name!r}].computedHash must be a lowercase sha256")
        elif isinstance(source, str) and is_safe_relative_path(source):
            expected_hash = compute_tracked_directory_hash(root, source)
            if computed_hash != expected_hash:
                add_error(errors, path, f"skills[{name!r}].computedHash is stale")


def tracked_files(root: Path) -> list[str]:
    result = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=root,
        check=True,
        stdout=subprocess.PIPE,
    )
    return [path for path in result.stdout.decode("utf-8").split("\0") if path]


def git_output(root: Path, args: list[str]) -> str | None:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=root,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError:
        return None
    return result.stdout.decode("utf-8")


def implementation_plan_base_ref(root: Path) -> str | None:
    for ref in ("origin/main", "main"):
        if git_output(root, ["rev-parse", "--verify", ref]) is None:
            continue
        merge_base = git_output(root, ["merge-base", "HEAD", ref])
        if merge_base:
            return merge_base.strip()
    return None


def changed_files_against(root: Path, base_ref: str) -> list[str]:
    output = git_output(root, ["diff", "--name-only", "-z", base_ref, "--", "docs/engineer"])
    if output is None:
        return []
    return [path for path in output.split("\0") if path]


def content_at_ref(root: Path, ref: str, rel: str) -> str | None:
    return git_output(root, ["show", f"{ref}:{rel}"])


def implementation_plan_feature_path(rel: str) -> str | None:
    match = IMPLEMENTATION_PLAN_RE.fullmatch(rel)
    if match is None:
        return None
    return match.group("feature_path")


def is_legacy_artifact_path(rel: str) -> bool:
    return "/_legacy/" in rel


def expected_parent_feature(feature_path: str) -> str:
    parts = feature_path.split("/")
    if len(parts) == 1:
        return "N/A"
    return "/".join(parts[:-1])


def validate_related_feature_document(
    root: Path,
    source_path: Path,
    rel_doc: str,
    feature_path: str,
    doc_type: str,
    errors: list[ContractError],
) -> None:
    path = root / rel_doc
    if not path.exists():
        add_error(errors, source_path, f"frontmatter {doc_type!r} must point to an existing file")
        return

    parsed = parse_markdown_frontmatter(path, path.read_text(), errors)
    if parsed is None:
        return
    metadata, _ = parsed

    feature_path_fields = ("feature_path", "parent_feature", "feature_level")
    has_feature_path_metadata = any(metadata.get(field) for field in feature_path_fields)
    requires_feature_path_metadata = "/" in feature_path
    if has_feature_path_metadata or requires_feature_path_metadata:
        for field in feature_path_fields:
            value = metadata.get(field)
            if not isinstance(value, str) or not value.strip():
                add_error(errors, path, f"frontmatter {field!r} must be non-empty")

    metadata_feature_path = metadata.get("feature_path", "")
    if metadata_feature_path and metadata_feature_path != feature_path:
        add_error(
            errors,
            path,
            f"frontmatter 'feature_path' must match directory path {feature_path!r}",
        )

    parent_feature = metadata.get("parent_feature", "")
    expected_parent = expected_parent_feature(feature_path)
    if parent_feature and parent_feature != expected_parent:
        add_error(
            errors,
            path,
            f"frontmatter 'parent_feature' must be {expected_parent!r}",
        )

    feature_level = metadata.get("feature_level", "")
    expected_level = str(len(feature_path.split("/")))
    if feature_level and feature_level != expected_level:
        add_error(
            errors,
            path,
            f"frontmatter 'feature_level' must be {expected_level!r}",
        )

    if doc_type == "related_trd":
        expected_related_prd = f"docs/pm/{feature_path}/PRD.md"
        related_prd = metadata.get("related_prd", "")
        if not isinstance(related_prd, str) or not related_prd.strip():
            add_error(errors, path, "frontmatter 'related_prd' must be non-empty")
        elif related_prd != expected_related_prd:
            add_error(
                errors,
                path,
                f"frontmatter 'related_prd' must be {expected_related_prd!r}",
            )


def validate_feature_path_metadata(
    source_path: Path,
    metadata: dict[str, str],
    feature_path: str,
    errors: list[ContractError],
) -> None:
    for field in ("feature_path", "parent_feature", "feature_level"):
        value = metadata.get(field)
        if not isinstance(value, str) or not value.strip():
            add_error(errors, source_path, f"frontmatter {field!r} must be non-empty")

    metadata_feature_path = metadata.get("feature_path", "")
    if metadata_feature_path and metadata_feature_path != feature_path:
        add_error(
            errors,
            source_path,
            f"frontmatter 'feature_path' must match directory path {feature_path!r}",
        )

    parent_feature = metadata.get("parent_feature", "")
    expected_parent = expected_parent_feature(feature_path)
    if parent_feature and parent_feature != expected_parent:
        add_error(
            errors,
            source_path,
            f"frontmatter 'parent_feature' must be {expected_parent!r}",
        )

    feature_level = metadata.get("feature_level", "")
    expected_level = str(len(feature_path.split("/")))
    if feature_level and feature_level != expected_level:
        add_error(
            errors,
            source_path,
            f"frontmatter 'feature_level' must be {expected_level!r}",
        )


def validate_feature_document_metadata(root: Path, errors: list[ContractError]) -> None:
    for rel in tracked_files(root):
        if is_legacy_artifact_path(rel):
            continue

        prd_match = PM_PRD_RE.fullmatch(rel)
        trd_match = ENGINEER_TRD_RE.fullmatch(rel)
        if prd_match is None and trd_match is None:
            continue

        path = root / rel
        parsed = parse_markdown_frontmatter(path, path.read_text(), errors)
        if parsed is None:
            continue
        metadata, _ = parsed

        feature_path = (
            prd_match.group("feature_path")
            if prd_match is not None
            else trd_match.group("feature_path")
        )
        validate_feature_path_metadata(path, metadata, feature_path, errors)

        if trd_match is not None:
            expected_related_prd = f"docs/pm/{feature_path}/PRD.md"
            related_prd = metadata.get("related_prd", "")
            if not isinstance(related_prd, str) or not related_prd.strip():
                add_error(errors, path, "frontmatter 'related_prd' must be non-empty")
            elif related_prd != expected_related_prd:
                add_error(
                    errors,
                    path,
                    f"frontmatter 'related_prd' must be {expected_related_prd!r}",
                )
            elif not (root / related_prd).exists():
                add_error(errors, path, "frontmatter 'related_prd' must point to an existing file")


def validate_implementation_plan_metadata(root: Path, errors: list[ContractError]) -> None:
    implementation_plans = [
        rel
        for rel in tracked_files(root)
        if rel.startswith("docs/engineer/")
        and rel.endswith("/IMPLEMENTATION_PLAN.md")
        and not is_legacy_artifact_path(rel)
        and (root / rel).exists()
    ]

    base_ref = implementation_plan_base_ref(root)
    changed_plans = set(changed_files_against(root, base_ref)) if base_ref else set()

    for rel in implementation_plans:
        path = root / rel
        feature_path = implementation_plan_feature_path(rel)
        if feature_path is None:
            add_error(
                errors,
                path,
                "implementation plan path must be docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md with one or more lowercase kebab-case segments",
            )
            continue

        parsed = parse_markdown_frontmatter(path, path.read_text(), errors)
        if parsed is None:
            continue
        metadata, _ = parsed

        for field in ("feature", "version", "date", "last_updated"):
            value = metadata.get(field)
            if not isinstance(value, str) or not value.strip():
                add_error(errors, path, f"frontmatter {field!r} must be non-empty")

        version = metadata.get("version", "")
        if version and not SEMVER_RE.fullmatch(version):
            add_error(errors, path, "frontmatter 'version' must be SemVer, for example 0.1.0")

        for field in ("date", "last_updated"):
            value = metadata.get(field, "")
            if value and not DATE_RE.fullmatch(value):
                add_error(errors, path, f"frontmatter {field!r} must use YYYY-MM-DD")

        feature_path_fields = ("feature_path", "parent_feature", "feature_level")
        has_feature_path_metadata = any(metadata.get(field) for field in feature_path_fields)
        requires_feature_path_metadata = rel in changed_plans
        if has_feature_path_metadata or requires_feature_path_metadata:
            for field in feature_path_fields:
                value = metadata.get(field)
                if not isinstance(value, str) or not value.strip():
                    add_error(errors, path, f"frontmatter {field!r} must be non-empty")

        metadata_feature_path = metadata.get("feature_path", "")
        if metadata_feature_path and metadata_feature_path != feature_path:
            add_error(
                errors,
                path,
                f"frontmatter 'feature_path' must match directory path {feature_path!r}",
            )

        parent_feature = metadata.get("parent_feature", "")
        expected_parent = expected_parent_feature(feature_path)
        if parent_feature and parent_feature != expected_parent:
            add_error(
                errors,
                path,
                f"frontmatter 'parent_feature' must be {expected_parent!r}",
            )

        feature_level = metadata.get("feature_level", "")
        expected_level = str(len(feature_path.split("/")))
        if feature_level and feature_level != expected_level:
            add_error(
                errors,
                path,
                f"frontmatter 'feature_level' must be {expected_level!r}",
            )

        validate_active_plan_archive_linkage(root, rel, feature_path, metadata, errors)

        if rel in changed_plans:
            for field in ("related_prd", "related_trd"):
                value = metadata.get(field)
                if not isinstance(value, str) or not value.strip():
                    add_error(errors, path, f"frontmatter {field!r} must be non-empty")

            expected_related_prd = f"docs/pm/{feature_path}/PRD.md"
            expected_related_trd = f"docs/engineer/{feature_path}/TRD.md"
            related_prd = metadata.get("related_prd", "")
            related_trd = metadata.get("related_trd", "")
            if related_prd and related_prd != expected_related_prd:
                add_error(
                    errors,
                    path,
                    f"frontmatter 'related_prd' must be {expected_related_prd!r}",
                )
            if related_trd and related_trd != expected_related_trd:
                add_error(
                    errors,
                    path,
                    f"frontmatter 'related_trd' must be {expected_related_trd!r}",
                )
            if related_prd == expected_related_prd:
                validate_related_feature_document(
                    root,
                    path,
                    related_prd,
                    feature_path,
                    "related_prd",
                    errors,
                )
            if related_trd == expected_related_trd:
                validate_related_feature_document(
                    root,
                    path,
                    related_trd,
                    feature_path,
                    "related_trd",
                    errors,
                )

    if base_ref is None:
        add_error(
            errors,
            root / "docs" / "engineer",
            "cannot compare implementation plan metadata because no base ref is available; fetch origin/main or main before running repository contract",
        )
        return

    for rel in changed_files_against(root, base_ref):
        if is_legacy_artifact_path(rel):
            continue
        if not IMPLEMENTATION_PLAN_RE.fullmatch(rel) or not (root / rel).exists():
            continue

        current_path = root / rel
        base_content = content_at_ref(root, base_ref, rel)
        if base_content is None:
            continue

        current_parsed = parse_markdown_frontmatter(current_path, current_path.read_text())
        base_parsed = parse_markdown_frontmatter(current_path, base_content)
        if current_parsed is None or base_parsed is None:
            continue

        current_metadata, current_body = current_parsed
        base_metadata, base_body = base_parsed
        body_changed = current_body != base_body
        version_changed = current_metadata.get("version") != base_metadata.get("version")
        last_updated_changed = current_metadata.get("last_updated") != base_metadata.get("last_updated")

        if body_changed and not version_changed and not last_updated_changed:
            add_error(
                errors,
                current_path,
                "body changed without updating frontmatter 'version' or 'last_updated'",
            )
        if version_changed and not last_updated_changed:
            add_error(
                errors,
                current_path,
                "frontmatter 'version' changed without updating 'last_updated'",
            )


def validate_archive_plan_metadata(
    root: Path,
    rel: str,
    errors: list[ContractError],
) -> None:
    match = IMPLEMENTATION_PLAN_ARCHIVE_RE.fullmatch(rel)
    if match is None:
        return

    path = root / rel
    feature_path = match.group("feature_path")
    scope = match.group("scope")

    parsed = parse_markdown_frontmatter(path, path.read_text(), errors)
    if parsed is None:
        return
    metadata, _ = parsed

    status = metadata.get("status", "")
    for field in ("implementation_scope", "status", "archived_at", "archive_approved_by", "source_plan"):
        value = metadata.get(field)
        if not isinstance(value, str) or not value.strip():
            add_error(errors, path, f"frontmatter {field!r} must be non-empty")

    if status and status not in ARCHIVE_STATUS_VALUES:
        add_error(
            errors,
            path,
            "frontmatter 'status' must be 'Archived' or 'Superseded'",
        )

    if status == "Superseded":
        reason = metadata.get("superseded_reason")
        if not isinstance(reason, str) or not reason.strip():
            add_error(errors, path, "frontmatter 'superseded_reason' must be non-empty for Superseded archives")

    implementation_scope = metadata.get("implementation_scope", "")
    if implementation_scope and implementation_scope != scope:
        add_error(
            errors,
            path,
            f"frontmatter 'implementation_scope' must match archive filename scope {scope!r}",
        )

    archived_at = metadata.get("archived_at", "")
    if archived_at and not DATE_RE.fullmatch(archived_at):
        add_error(errors, path, "frontmatter 'archived_at' must use YYYY-MM-DD")

    expected_source = f"docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md"
    source_plan = metadata.get("source_plan", "")
    if source_plan and source_plan != expected_source:
        add_error(
            errors,
            path,
            f"frontmatter 'source_plan' must be {expected_source!r}",
        )

    feature_path_fields = ("feature_path", "parent_feature", "feature_level")
    if any(field in metadata for field in feature_path_fields):
        validate_feature_path_metadata(path, metadata, feature_path, errors)

    expected_related_prd = f"docs/pm/{feature_path}/PRD.md"
    expected_related_trd = f"docs/engineer/{feature_path}/TRD.md"
    related_prd = metadata.get("related_prd", "")
    related_trd = metadata.get("related_trd", "")
    if "related_prd" in metadata and related_prd != expected_related_prd:
        add_error(
            errors,
            path,
            f"frontmatter 'related_prd' must be {expected_related_prd!r}",
        )
    if "related_trd" in metadata and related_trd != expected_related_trd:
        add_error(
            errors,
            path,
            f"frontmatter 'related_trd' must be {expected_related_trd!r}",
        )


def feature_path_has_plan_archives(root: Path, feature_path: str) -> bool:
    archive_dir = root / "docs" / "engineer" / feature_path / "implementation-plans" / "archive"
    if not archive_dir.is_dir():
        return False
    for candidate in archive_dir.glob("IMPLEMENTATION_PLAN-*.md"):
        candidate_rel = candidate.relative_to(root).as_posix()
        if IMPLEMENTATION_PLAN_ARCHIVE_RE.fullmatch(candidate_rel):
            return True
    return False


def validate_active_plan_archive_linkage(
    root: Path,
    rel: str,
    feature_path: str,
    metadata: dict[str, str],
    errors: list[ContractError],
) -> None:
    path = root / rel
    previous_archive = metadata.get("previous_plan_archive")
    if not isinstance(previous_archive, str) or not previous_archive.strip():
        if feature_path_has_plan_archives(root, feature_path):
            add_error(
                errors,
                path,
                "frontmatter 'previous_plan_archive' must be non-empty when implementation-plans/archive already contains archived plans for this feature_path",
            )
        return

    archive_match = IMPLEMENTATION_PLAN_ARCHIVE_RE.fullmatch(previous_archive)
    if archive_match is None:
        add_error(
            errors,
            path,
            "frontmatter 'previous_plan_archive' must point to an implementation-plans/archive/IMPLEMENTATION_PLAN-<scope>.md path",
        )
        return

    if archive_match.group("feature_path") != feature_path:
        add_error(
            errors,
            path,
            f"frontmatter 'previous_plan_archive' must reference an archive on feature_path {feature_path!r}",
        )
        return

    if not (root / previous_archive).exists():
        add_error(
            errors,
            path,
            "frontmatter 'previous_plan_archive' must point to an existing archive file",
        )


def validate_archive_plans(root: Path, errors: list[ContractError]) -> None:
    for rel in tracked_files(root):
        if is_legacy_artifact_path(rel):
            continue
        if not (root / rel).exists():
            continue
        if IMPLEMENTATION_PLAN_ARCHIVE_RE.fullmatch(rel) is None:
            if (
                rel.startswith("docs/engineer/")
                and "/implementation-plans/archive/" in rel
                and rel.endswith(".md")
            ):
                add_error(
                    errors,
                    root / rel,
                    "implementation-plans/archive only allows IMPLEMENTATION_PLAN-<scope>.md with a lower kebab-case scope",
                )
            continue
        validate_archive_plan_metadata(root, rel, errors)


def validate_legacy_artifact_metadata(root: Path, errors: list[ContractError]) -> None:
    required_fields = ("legacy_of", "legacy_reason", "superseded_by")

    for rel in tracked_files(root):
        if not rel.startswith("docs/") or not rel.endswith(".md"):
            continue
        if not is_legacy_artifact_path(rel):
            continue

        path = root / rel
        parsed = parse_markdown_frontmatter(path, path.read_text(), errors)
        if parsed is None:
            continue
        metadata, _ = parsed

        for field in required_fields:
            value = metadata.get(field)
            if not isinstance(value, str) or not value.strip():
                add_error(errors, path, f"frontmatter {field!r} must be non-empty")


def validate_formal_document_author(root: Path, errors: list[ContractError]) -> None:
    for rel in tracked_files(root):
        if not rel.startswith("docs/") or not rel.endswith(".md"):
            continue

        path = root / rel
        parsed = parse_markdown_frontmatter(path, path.read_text())
        if parsed is None:
            continue

        metadata, _ = parsed
        author = metadata.get("author")
        if isinstance(author, str):
            normalized_author = " ".join(author.split())
        else:
            normalized_author = ""
        if author is not None and (
            not normalized_author
            or len(normalized_author.split()) < 2
            or normalized_author in PLACEHOLDER_AUTHOR_VALUES
            or TEMPLATE_PLACEHOLDER_RE.search(normalized_author)
        ):
            add_error(
                errors,
                path,
                "frontmatter 'author' must be a filled, non-placeholder traceable value",
            )


def validate_tracked_file_policy(root: Path, errors: list[ContractError]) -> None:
    for rel in tracked_files(root):
        if any(pattern.search(rel) for pattern in BLOCKED_TRACKED_PATTERNS):
            add_error(errors, root / rel, "tracked file is blocked by repository policy")


def validate_all(root: Path | None = None) -> list[ContractError]:
    root = root or repo_root()
    errors: list[ContractError] = []
    validate_claude_symlink(root, errors)
    validate_marketplace(root, errors)
    validate_skills_lock(root, errors)
    validate_feature_document_metadata(root, errors)
    validate_implementation_plan_metadata(root, errors)
    validate_archive_plans(root, errors)
    validate_legacy_artifact_metadata(root, errors)
    validate_formal_document_author(root, errors)
    validate_tracked_file_policy(root, errors)
    return errors


def main() -> int:
    root = repo_root()
    errors = validate_all(root)
    if errors:
        print("FAIL: repository contract violations found", file=sys.stderr)
        for error in errors:
            print(f"- {error.render(root)}", file=sys.stderr)
        return 1

    print("PASS: repository contract satisfied")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
