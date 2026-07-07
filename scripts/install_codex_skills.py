#!/usr/bin/env python3
"""Install Codex skills by copying them out of the repository tree."""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


PLUGIN_MANIFESTS = (
    ".claude-plugin/plugin.json",
    ".codex-plugin/plugin.json",
)


@dataclass(frozen=True)
class SkillSpec:
    plugin_name: str
    skill_name: str
    source: Path


@dataclass(frozen=True)
class InstallResult:
    skill: SkillSpec
    status: str
    target: Path
    message: str


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def marketplace_path(root: Path) -> Path:
    return root / ".claude-plugin" / "marketplace.json"


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"{path}: invalid JSON: {exc}") from exc
    except OSError as exc:
        raise ValueError(f"{path}: cannot read file: {exc}") from exc


def safe_relative_path(value: Any, field: str) -> Path:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"marketplace field {field} must be a non-empty string")

    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"marketplace field {field} must be a safe relative path: {value}")
    return path


def resolve_relative(base: Path, value: Any, field: str) -> Path:
    return (base / safe_relative_path(value, field)).resolve()


def parse_skill_specs(root: Path) -> list[SkillSpec]:
    data = load_json(marketplace_path(root))
    plugins = data.get("plugins")
    if not isinstance(plugins, list) or not plugins:
        raise ValueError("marketplace must contain a non-empty plugins array")

    specs: list[SkillSpec] = []
    seen: dict[str, Path] = {}

    for plugin_index, plugin in enumerate(plugins):
        if not isinstance(plugin, dict):
            raise ValueError(f"marketplace plugin at index {plugin_index} must be an object")

        plugin_name = plugin.get("name")
        if not isinstance(plugin_name, str) or not plugin_name.strip():
            raise ValueError(f"marketplace plugin at index {plugin_index} must have a name")

        plugin_source = resolve_relative(root, plugin.get("source"), f"plugins[{plugin_index}].source")
        skills = plugin.get("skills")
        if not isinstance(skills, list) or not skills:
            raise ValueError(f"marketplace plugin {plugin_name} must contain skills")

        for skill_index, skill_entry in enumerate(skills):
            skill_source = resolve_relative(
                plugin_source,
                skill_entry,
                f"plugins[{plugin_index}].skills[{skill_index}]",
            )
            skill_name = skill_source.name

            if not (skill_source / "SKILL.md").is_file():
                raise ValueError(f"{skill_source}: missing SKILL.md")
            if skill_name in seen:
                raise ValueError(
                    f"duplicate skill target name {skill_name!r}: {seen[skill_name]} and {skill_source}"
                )

            seen[skill_name] = skill_source
            specs.append(
                SkillSpec(
                    plugin_name=plugin_name,
                    skill_name=skill_name,
                    source=skill_source,
                )
            )

    return specs


def select_skill_specs(specs: list[SkillSpec], routers_only: bool) -> list[SkillSpec]:
    selected = [spec for spec in specs if not routers_only or spec.skill_name == spec.plugin_name]
    if not selected:
        mode = "--routers-only" if routers_only else "all"
        raise ValueError(f"no skills selected for install mode {mode}")
    return selected


def remove_existing(path: Path) -> None:
    if path.is_symlink() or path.is_file():
        path.unlink()
        return
    if path.is_dir():
        shutil.rmtree(path)
        return
    if path.exists():
        raise ValueError(f"{path}: unsupported existing filesystem entry")


def is_relative_to(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
    except ValueError:
        return False
    return True


def is_repo_symlink(path: Path, root: Path) -> bool:
    return path.is_symlink() and is_relative_to(path.resolve(strict=False), root)


def find_unselected_existing_targets(
    all_specs: list[SkillSpec],
    selected_specs: list[SkillSpec],
    target_root: Path,
) -> list[tuple[SkillSpec, Path]]:
    selected_names = {spec.skill_name for spec in selected_specs}
    targets: list[tuple[SkillSpec, Path]] = []

    for spec in all_specs:
        if spec.skill_name in selected_names:
            continue
        target = target_root / spec.skill_name
        if target.exists() or target.is_symlink():
            targets.append((spec, target))

    return targets


def remove_unselected_targets(
    all_specs: list[SkillSpec],
    selected_specs: list[SkillSpec],
    target_root: Path,
    force: bool,
) -> list[tuple[SkillSpec, Path]]:
    existing = find_unselected_existing_targets(all_specs, selected_specs, target_root)
    if not existing:
        return []

    if not force:
        names = ", ".join(spec.skill_name for spec, _target in existing[:8])
        if len(existing) > 8:
            names = f"{names}, ... ({len(existing)} total)"
        raise ValueError(
            "--routers-only target already contains specialist skills managed by this repo: "
            f"{names}. Remove those directories or rerun with --force to delete "
            "unselected managed skills before installing routers-only."
        )

    for _spec, target in existing:
        remove_existing(target)
    return existing


def install_skill(skill: SkillSpec, target_root: Path, force: bool, root: Path) -> InstallResult:
    target = target_root / skill.skill_name
    target_exists = target.exists() or target.is_symlink()
    repo_symlink = is_repo_symlink(target, root)
    if target_exists:
        if not force and not repo_symlink:
            return InstallResult(
                skill=skill,
                status="skipped",
                target=target,
                message="target already exists; use --force to replace it",
            )

        remove_existing(target)

    shutil.copytree(skill.source, target)
    status = "migrated" if repo_symlink else "replaced" if target_exists else "installed"
    message = "replaced repository symlink with copied skill" if repo_symlink else "copied"
    return InstallResult(
        skill=skill,
        status=status,
        target=target,
        message=message,
    )


def find_namespace_manifests(target_root: Path) -> list[Path]:
    manifests: list[Path] = []
    current = target_root.resolve()

    while True:
        for manifest in PLUGIN_MANIFESTS:
            candidate = current / manifest
            if candidate.is_file():
                manifests.append(candidate)

        if current.parent == current:
            break
        current = current.parent

    return manifests


def render_results(
    results: list[InstallResult],
    target_root: Path,
    manifests: list[Path],
    routers_only: bool,
    removed_unselected: list[tuple[SkillSpec, Path]],
) -> None:
    print(f"Target: {target_root}")
    print("Installed skills:")

    for result in results:
        rel_source = result.skill.source
        try:
            rel_source = result.skill.source.relative_to(repo_root())
        except ValueError:
            pass
        print(
            f"- {result.status}: {result.skill.skill_name} "
            f"({result.skill.plugin_name}) <- {rel_source} -> {result.target} "
            f"[{result.message}]"
        )

    counts: dict[str, int] = {}
    for result in results:
        counts[result.status] = counts.get(result.status, 0) + 1

    summary = ", ".join(f"{status}={count}" for status, count in sorted(counts.items()))
    print(f"Summary: {summary}")

    if routers_only:
        print()
        print("WARNING: --routers-only installed only role router skills.")
        print(
            "Specialist skills were not installed, so pm-agent / role router "
            "orchestration cannot call downstream specialist workflows."
        )
        print("Use this mode only for minimal entry classification.")

        if removed_unselected:
            print()
            print("Removed unselected managed skills for --routers-only:")
            for spec, target in removed_unselected:
                print(f"- removed: {spec.skill_name} ({spec.plugin_name}) -> {target}")

    if manifests:
        print()
        print("WARNING: target ancestor chain contains plugin manifests.")
        print("Codex may still apply namespace prefixes for skills installed under this target.")
        for manifest in manifests:
            print(f"- {manifest}")
    else:
        print("Namespace check: no plugin manifest found in target ancestor chain.")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Copy dev-agent-skills Codex skill directories into a skill target."
    )
    parser.add_argument(
        "--target",
        default="~/.agents/skills",
        help="target skill directory (default: ~/.agents/skills)",
    )
    parser.add_argument(
        "--routers-only",
        action="store_true",
        help="install only role router skills; specialist orchestration will be unavailable",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="replace existing target skill directories before copying",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    root = repo_root()
    target_root = Path(args.target).expanduser().resolve()

    try:
        all_specs = parse_skill_specs(root)
        specs = select_skill_specs(all_specs, routers_only=args.routers_only)
        target_root.mkdir(parents=True, exist_ok=True)
        removed_unselected = (
            remove_unselected_targets(all_specs, specs, target_root, force=args.force)
            if args.routers_only
            else []
        )
        results = [install_skill(skill, target_root, force=args.force, root=root) for skill in specs]
        manifests = find_namespace_manifests(target_root)
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    render_results(
        results,
        target_root,
        manifests,
        routers_only=args.routers_only,
        removed_unselected=removed_unselected,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
