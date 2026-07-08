#!/usr/bin/env python3
"""Install Codex skills with a hidden repository mirror and root symlinks."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


REPO_NAME = "dev-agent-skills"
MIRROR_DIR_NAME = ".dev-agent-skills"
MIRROR_MARKER_NAME = ".dev-agent-skills-mirror.json"
LEGACY_AGGREGATE_DIR = "dev-agent-skills"
PLUGIN_DIR_NAMES = {".claude-plugin", ".codex-plugin"}
PLUGIN_MANIFESTS = (
    ".claude-plugin/plugin.json",
    ".codex-plugin/plugin.json",
)
TEST_REFERENCE_RE = re.compile(
    r"(?P<path>(?:agents/[A-Za-z0-9_.-]+/test/[A-Za-z0-9_./-]+|test/[A-Za-z0-9_./-]+))"
)


@dataclass(frozen=True)
class SkillSpec:
    plugin_name: str
    skill_name: str
    source: Path
    source_rel: Path


@dataclass(frozen=True)
class InstallResult:
    skill: SkillSpec
    status: str
    target: Path
    message: str


@dataclass(frozen=True)
class ExistingTarget:
    skill: SkillSpec
    target: Path
    owned: bool


@dataclass(frozen=True)
class PreflightPlan:
    selected_existing: list[ExistingTarget]
    selected_skipped: list[ExistingTarget]
    unselected_remove: list[ExistingTarget]
    unselected_skipped: list[ExistingTarget]
    legacy_remove: list[Path]
    legacy_skipped: list[Path]


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

            try:
                source_rel = skill_source.relative_to(root)
            except ValueError as exc:
                raise ValueError(f"{skill_source}: skill source must be inside repository root") from exc

            seen[skill_name] = skill_source
            specs.append(
                SkillSpec(
                    plugin_name=plugin_name,
                    skill_name=skill_name,
                    source=skill_source,
                    source_rel=source_rel,
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


def removal_guard_path(path: Path) -> Path:
    if path.is_symlink():
        return path.parent.resolve(strict=False) / path.name
    return path.resolve(strict=False)


def validate_removals_do_not_touch_source(root: Path, paths: list[Path]) -> None:
    source = root.resolve(strict=False)
    conflicts: list[Path] = []

    for path in paths:
        target = removal_guard_path(path)
        if target == source or is_relative_to(target, source) or is_relative_to(source, target):
            conflicts.append(path)

    if conflicts:
        raise ValueError(
            "安装源 checkout 位于目标删除路径内，请先把 checkout 移出 target 或换用其他 --target: "
            f"{summarize_paths(conflicts)}"
        )


def marketplace_name(path: Path) -> str | None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None

    name = data.get("name")
    return name if isinstance(name, str) else None


def is_dev_agent_checkout_path(path: Path) -> bool:
    current = path.resolve(strict=False)
    for parent in (current, *current.parents):
        manifest = parent / ".claude-plugin" / "marketplace.json"
        if manifest.is_file() and marketplace_name(manifest) == REPO_NAME:
            return True
    return False


def directory_contains_dev_agent_marketplace(path: Path) -> bool:
    if not path.is_dir() or path.is_symlink():
        return False

    direct = path / ".claude-plugin" / "marketplace.json"
    if direct.is_file() and marketplace_name(direct) == REPO_NAME:
        return True

    try:
        candidates = path.rglob("marketplace.json")
        for candidate in candidates:
            if ".claude-plugin" in candidate.parts and marketplace_name(candidate) == REPO_NAME:
                return True
    except OSError:
        return False

    return False


def mirror_root(target_root: Path) -> Path:
    return target_root / MIRROR_DIR_NAME


def mirror_marker_path(mirror: Path) -> Path:
    return mirror / MIRROR_MARKER_NAME


def write_mirror_marker(root: Path, mirror: Path) -> None:
    marker = {
        "schema": "dev-agent-skills-codex-mirror",
        "version": 1,
        "source": root.resolve().as_posix(),
    }
    mirror_marker_path(mirror).write_text(
        json.dumps(marker, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def is_owned_mirror(path: Path) -> bool:
    return path.is_symlink() or mirror_marker_path(path).is_file()


def is_mirror_symlink(path: Path, target_root: Path) -> bool:
    if not path.is_symlink():
        return False
    return is_relative_to(path.resolve(strict=False), mirror_root(target_root).resolve(strict=False))


def is_checkout_symlink(path: Path) -> bool:
    return path.is_symlink() and is_dev_agent_checkout_path(path.resolve(strict=False))


def is_owned_skill_target(path: Path, target_root: Path) -> bool:
    return is_mirror_symlink(path, target_root) or is_checkout_symlink(path)


def is_owned_legacy_aggregate(path: Path, target_root: Path) -> bool:
    if path.is_symlink():
        return is_mirror_symlink(path, target_root) or is_checkout_symlink(path)
    return directory_contains_dev_agent_marketplace(path)


def summarize_paths(paths: list[Path]) -> str:
    names = ", ".join(path.name for path in paths[:8])
    if len(paths) > 8:
        names = f"{names}, ... ({len(paths)} total)"
    return names


def build_preflight_plan(
    root: Path,
    all_specs: list[SkillSpec],
    selected_specs: list[SkillSpec],
    target_root: Path,
    routers_only: bool,
    force: bool,
) -> PreflightPlan:
    selected_names = {spec.skill_name for spec in selected_specs}
    selected_existing: list[ExistingTarget] = []
    selected_skipped: list[ExistingTarget] = []
    unselected_remove: list[ExistingTarget] = []
    unselected_skipped: list[ExistingTarget] = []
    force_conflicts: list[Path] = []

    for spec in selected_specs:
        target = target_root / spec.skill_name
        if not (target.exists() or target.is_symlink()):
            continue

        owned = is_owned_skill_target(target, target_root)
        existing = ExistingTarget(skill=spec, target=target, owned=owned)
        if owned:
            selected_existing.append(existing)
        elif force:
            force_conflicts.append(target)
        else:
            selected_skipped.append(existing)

    if routers_only:
        for spec in all_specs:
            if spec.skill_name in selected_names:
                continue

            target = target_root / spec.skill_name
            if not (target.exists() or target.is_symlink()):
                continue

            owned = is_owned_skill_target(target, target_root)
            existing = ExistingTarget(skill=spec, target=target, owned=owned)
            if owned:
                unselected_remove.append(existing)
            elif force:
                force_conflicts.append(target)
            else:
                unselected_skipped.append(existing)

    if force_conflicts:
        raise ValueError(
            "--force target contains skill names that are not owned by this installer: "
            f"{summarize_paths(force_conflicts)}. Move or remove those paths manually; "
            "--force will not delete unowned entries."
        )

    mirror = mirror_root(target_root)
    if (mirror.exists() or mirror.is_symlink()) and not is_owned_mirror(mirror):
        raise ValueError(
            "target contains a hidden mirror path that is not owned by this installer: "
            f"{mirror}. Move or remove that path manually; the installer will not delete it."
        )

    legacy = target_root / LEGACY_AGGREGATE_DIR
    legacy_remove: list[Path] = []
    legacy_skipped: list[Path] = []
    if legacy.exists() or legacy.is_symlink():
        if is_owned_legacy_aggregate(legacy, target_root):
            legacy_remove.append(legacy)
        else:
            legacy_skipped.append(legacy)

    planned_removals: list[Path] = []
    if mirror.exists() or mirror.is_symlink():
        planned_removals.append(mirror)
    planned_removals.extend(existing.target for existing in selected_existing)
    planned_removals.extend(existing.target for existing in unselected_remove)
    planned_removals.extend(legacy_remove)
    validate_removals_do_not_touch_source(root, planned_removals)

    return PreflightPlan(
        selected_existing=selected_existing,
        selected_skipped=selected_skipped,
        unselected_remove=unselected_remove,
        unselected_skipped=unselected_skipped,
        legacy_remove=legacy_remove,
        legacy_skipped=legacy_skipped,
    )


def iter_skill_instruction_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for skill_dir in sorted((root / "agents").glob("*/skills/*")):
        skill_file = skill_dir / "SKILL.md"
        if skill_file.is_file():
            files.append(skill_file)

        internal = skill_dir / "_internal"
        if internal.is_dir():
            files.extend(sorted(path for path in internal.rglob("*") if path.is_file()))

    return files


def role_root_for_instruction_file(root: Path, path: Path) -> Path | None:
    try:
        rel = path.relative_to(root)
    except ValueError:
        return None

    parts = rel.parts
    if len(parts) < 4 or parts[0] != "agents" or parts[2] != "skills":
        return None
    return root / "agents" / parts[1]


def find_referenced_test_paths(root: Path) -> list[Path]:
    referenced: set[Path] = set()

    for instruction_file in iter_skill_instruction_files(root):
        try:
            content = instruction_file.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue

        role_root = role_root_for_instruction_file(root, instruction_file)
        for match in TEST_REFERENCE_RE.finditer(content):
            raw = match.group("path").strip("`'\"),.;:")
            candidates: list[Path] = []

            if raw.startswith("agents/"):
                candidates.append(root / raw)
            elif raw.startswith("test/") and role_root is not None:
                candidates.append(role_root / raw)
                candidates.append(root / raw)

            for candidate in candidates:
                if candidate.exists() or candidate.is_symlink():
                    try:
                        referenced.add(candidate.resolve(strict=False).relative_to(root))
                    except ValueError:
                        pass

    return sorted(referenced)


def mirror_ignore(root: Path):
    agents_root = root / "agents"

    def ignore(current: str, names: list[str]) -> set[str]:
        current_path = Path(current)
        ignored = {name for name in names if name in PLUGIN_DIR_NAMES}

        if current_path.parent == agents_root and "test" in names:
            ignored.add("test")

        return ignored

    return ignore


def copy_extra_path(root: Path, mirror: Path, rel_path: Path) -> None:
    source = root / rel_path
    target = mirror / rel_path

    if target.exists() or target.is_symlink():
        remove_existing(target)

    target.parent.mkdir(parents=True, exist_ok=True)
    if source.is_symlink() or source.is_file():
        shutil.copy2(source, target, follow_symlinks=False)
    elif source.is_dir():
        shutil.copytree(source, target, ignore=mirror_ignore(root))


def rebuild_mirror(root: Path, target_root: Path) -> list[Path]:
    mirror = mirror_root(target_root)

    if mirror.exists() or mirror.is_symlink():
        remove_existing(mirror)

    (mirror / "agents").parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(root / "agents", mirror / "agents", ignore=mirror_ignore(root))

    referenced_test_paths = find_referenced_test_paths(root)
    for rel_path in referenced_test_paths:
        copy_extra_path(root, mirror, rel_path)

    write_mirror_marker(root, mirror)

    return referenced_test_paths


def symlink_target_for_skill(target_root: Path, skill: SkillSpec) -> str:
    mirror_skill = mirror_root(target_root) / skill.source_rel
    return os.path.relpath(mirror_skill, start=target_root)


def install_selected_skill(
    skill: SkillSpec,
    target_root: Path,
    plan: PreflightPlan,
    force: bool,
) -> InstallResult:
    target = target_root / skill.skill_name
    skipped = {existing.skill.skill_name: existing for existing in plan.selected_skipped}
    existing = {existing.skill.skill_name: existing for existing in plan.selected_existing}

    if skill.skill_name in skipped:
        return InstallResult(
            skill=skill,
            status="skipped",
            target=target,
            message="target exists but is not owned by this installer; left unchanged",
        )

    existed = skill.skill_name in existing
    was_checkout_symlink = existed and is_checkout_symlink(target)

    if target.exists() or target.is_symlink():
        remove_existing(target)

    target.symlink_to(symlink_target_for_skill(target_root, skill), target_is_directory=True)

    if was_checkout_symlink:
        status = "migrated"
        message = "replaced checkout symlink with mirror symlink"
    elif existed and force:
        status = "replaced"
        message = "replaced managed mirror symlink"
    elif existed:
        status = "updated"
        message = "refreshed managed mirror symlink"
    else:
        status = "installed"
        message = "created mirror symlink"

    return InstallResult(skill=skill, status=status, target=target, message=message)


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
    plan: PreflightPlan,
    referenced_test_paths: list[Path],
) -> None:
    print(f"Target: {target_root}")
    print(f"Mirror: {mirror_root(target_root)}")
    print("Installed skills:")

    for result in results:
        print(
            f"- {result.status}: {result.skill.skill_name} "
            f"({result.skill.plugin_name}) <- {result.skill.source_rel.as_posix()} -> {result.target} "
            f"[{result.message}]"
        )

    counts: dict[str, int] = {}
    for result in results:
        counts[result.status] = counts.get(result.status, 0) + 1

    summary = ", ".join(f"{status}={count}" for status, count in sorted(counts.items()))
    print(f"Summary: {summary}")

    if referenced_test_paths:
        print()
        print("Included referenced test paths in mirror:")
        for rel_path in referenced_test_paths:
            print(f"- {rel_path.as_posix()}")

    if plan.legacy_remove:
        print()
        print("Removed legacy aggregate entries:")
        for path in plan.legacy_remove:
            print(f"- removed: {path}")

    if plan.legacy_skipped:
        print()
        print("WARNING: skipped unowned legacy aggregate entries:")
        for path in plan.legacy_skipped:
            print(f"- skipped: {path}")

    if routers_only:
        print()
        print("WARNING: --routers-only installed only role router skills.")
        print(
            "Specialist skills were not linked at the target root, so pm-agent / "
            "role router orchestration cannot call downstream specialist workflows."
        )
        print("The hidden mirror still contains the full agents tree for shared instructions.")
        print("Use this mode only for minimal entry classification.")

        if plan.unselected_remove:
            print()
            print("Removed unselected managed skills for --routers-only:")
            for existing in plan.unselected_remove:
                print(f"- removed: {existing.skill.skill_name} ({existing.skill.plugin_name}) -> {existing.target}")

        if plan.unselected_skipped:
            print()
            print("WARNING: skipped unowned unselected skill names for --routers-only:")
            for existing in plan.unselected_skipped:
                print(f"- skipped: {existing.skill.skill_name} -> {existing.target}")

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
        description="Install dev-agent-skills for Codex with a hidden mirror and root symlinks."
    )
    parser.add_argument(
        "--target",
        default="~/.agents/skills",
        help="target skill directory (default: ~/.agents/skills)",
    )
    parser.add_argument(
        "--routers-only",
        action="store_true",
        help="link only role router skills at the target root; specialist orchestration will be unavailable",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="rebuild the mirror and replace owned target symlinks; never deletes unowned entries",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    root = repo_root()
    target_root = Path(args.target).expanduser().resolve()

    try:
        all_specs = parse_skill_specs(root)
        specs = select_skill_specs(all_specs, routers_only=args.routers_only)
        plan = build_preflight_plan(
            root,
            all_specs,
            specs,
            target_root,
            routers_only=args.routers_only,
            force=args.force,
        )
        target_root.mkdir(parents=True, exist_ok=True)

        for path in plan.legacy_remove:
            remove_existing(path)
        for existing in plan.unselected_remove:
            remove_existing(existing.target)

        referenced_test_paths = rebuild_mirror(root, target_root)
        results = [
            install_selected_skill(
                skill,
                target_root,
                plan=plan,
                force=args.force,
            )
            for skill in specs
        ]
        manifests = find_namespace_manifests(target_root)
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    render_results(
        results,
        target_root,
        manifests,
        routers_only=args.routers_only,
        plan=plan,
        referenced_test_paths=referenced_test_paths,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
