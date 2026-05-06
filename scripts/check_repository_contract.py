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
BLOCKED_TRACKED_PATTERNS = (
    re.compile(r"(^|/)\.DS_Store$"),
    re.compile(r"(^|/)\.pytest_cache(/|$)"),
    re.compile(r"(^|/)__pycache__(/|$)"),
    re.compile(r"\.pyc$"),
    re.compile(r"^docs/superpowers(/|$)"),
)


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
