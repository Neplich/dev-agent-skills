import json
import os
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INSTALLER = ROOT / "scripts" / "install_codex_skills.py"
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
MIRROR_DIR = ".dev-agent-skills"
MIRROR_MARKER = ".dev-agent-skills-mirror.json"


def run_installer(target: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(INSTALLER), "--target", str(target), *args],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


def write_dev_agent_marketplace_marker(root: Path) -> None:
    (root / ".claude-plugin").mkdir(parents=True, exist_ok=True)
    (root / ".claude-plugin/marketplace.json").write_text(
        json.dumps({"name": "dev-agent-skills"}),
        encoding="utf-8",
    )


def make_minimal_checkout(root: Path) -> None:
    (root / "scripts").mkdir(parents=True)
    shutil.copy2(INSTALLER, root / "scripts" / "install_codex_skills.py")
    (root / ".claude-plugin").mkdir()
    (root / "agents/product_manager/skills/pm-agent").mkdir(parents=True)
    (root / "agents/product_manager/skills/pm-agent/SKILL.md").write_text(
        "---\nname: pm-agent\n---\n",
        encoding="utf-8",
    )
    (root / ".claude-plugin/marketplace.json").write_text(
        json.dumps(
            {
                "name": "dev-agent-skills",
                "plugins": [
                    {
                        "name": "pm-agent",
                        "source": "./agents/product_manager",
                        "skills": ["./skills/pm-agent"],
                    }
                ],
            }
        ),
        encoding="utf-8",
    )


def marketplace_data() -> dict:
    return json.loads(MARKETPLACE.read_text(encoding="utf-8"))


def marketplace_skill_sources() -> list[tuple[str, Path]]:
    sources: list[tuple[str, Path]] = []
    for plugin in marketplace_data()["plugins"]:
        plugin_source = ROOT / plugin["source"]
        for skill_path in plugin["skills"]:
            sources.append((plugin["name"], (plugin_source / skill_path).resolve()))
    return sources


def marketplace_skill_map() -> dict[str, Path]:
    sources = marketplace_skill_sources()
    basename_counts: dict[str, int] = {}
    for _, source in sources:
        basename_counts[source.name] = basename_counts.get(source.name, 0) + 1

    result: dict[str, Path] = {}
    for plugin_name, source in sources:
        install_name = source.name
        if basename_counts[source.name] > 1:
            install_name = f"{plugin_name.removesuffix('-agent')}-{source.name}"
        result[install_name] = source.relative_to(ROOT)
    return result


def marketplace_skill_names() -> list[str]:
    return sorted(marketplace_skill_map())


def router_skill_names() -> list[str]:
    return sorted(plugin["name"] for plugin in marketplace_data()["plugins"])


def skill_source_rel(skill_name: str) -> Path:
    try:
        return marketplace_skill_map()[skill_name]
    except KeyError as exc:
        raise AssertionError(f"unknown skill {skill_name}") from exc


def scanned_skill_entries(skill_root: Path) -> list[str]:
    entries: list[str] = []
    for current, dirs, files in os.walk(skill_root, followlinks=True):
        dirs[:] = [name for name in dirs if not name.startswith(".")]
        if "SKILL.md" in files:
            entries.append(Path(current).relative_to(skill_root).as_posix())
    return sorted(entries)


def assert_relative_mirror_link(target: Path, skill_name: str) -> None:
    link = target / skill_name
    assert link.is_symlink()
    assert os.readlink(link) == (Path(MIRROR_DIR) / skill_source_rel(skill_name)).as_posix()
    assert link.resolve(strict=True) == target / MIRROR_DIR / skill_source_rel(skill_name)


def plugin_manifest_paths(target: Path) -> list[Path]:
    return sorted(
        path
        for path in (target / MIRROR_DIR).rglob("plugin.json")
        if ".claude-plugin" in path.parts or ".codex-plugin" in path.parts
    )


def test_default_install_creates_hidden_mirror_and_relative_skill_symlinks(tmp_path: Path) -> None:
    target = tmp_path / "skills"

    result = run_installer(target)

    assert result.returncode == 0, result.stderr + result.stdout
    assert "Mirror:" in result.stdout
    assert scanned_skill_entries(target) == marketplace_skill_names()
    assert (target / MIRROR_DIR / "agents").is_dir()
    marker = json.loads((target / MIRROR_DIR / MIRROR_MARKER).read_text(encoding="utf-8"))
    assert marker["schema"] == "dev-agent-skills-codex-mirror"
    assert marker["version"] == 1
    assert marker["source"] == ROOT.resolve().as_posix()
    assert_relative_mirror_link(target, "pm-agent")
    assert_relative_mirror_link(target, "debugger")
    assert_relative_mirror_link(target, "pm-release-notes-generator")
    assert_relative_mirror_link(target, "docs-release-notes-generator")
    assert not (target / "release-notes-generator").exists()
    assert skill_source_rel("pm-release-notes-generator") == Path(
        "agents/product_manager/skills/release-notes-generator"
    )
    assert skill_source_rel("docs-release-notes-generator") == Path(
        "agents/docs/skills/release-notes-generator"
    )
    assert (
        "pm-agent:release-notes-generator is explicitly callable as "
        "pm-release-notes-generator"
    ) in result.stdout
    assert (
        "docs-agent:release-notes-generator is explicitly callable as "
        "docs-release-notes-generator"
    ) in result.stdout
    assert (
        target
        / MIRROR_DIR
        / "agents/product_manager/skills/release-notes-generator/SKILL.md"
    ).is_file()
    assert (
        target / MIRROR_DIR / "agents/docs/skills/release-notes-generator/SKILL.md"
    ).is_file()


def test_duplicate_skill_basename_within_one_plugin_is_rejected(tmp_path: Path) -> None:
    checkout = tmp_path / "checkout"
    make_minimal_checkout(checkout)
    for parent in ("one", "two"):
        skill = checkout / f"agents/product_manager/{parent}/duplicate"
        skill.mkdir(parents=True)
        (skill / "SKILL.md").write_text("---\nname: duplicate\n---\n", encoding="utf-8")

    marketplace_path = checkout / ".claude-plugin/marketplace.json"
    marketplace = json.loads(marketplace_path.read_text(encoding="utf-8"))
    marketplace["plugins"][0]["skills"] = ["./one/duplicate", "./two/duplicate"]
    marketplace_path.write_text(json.dumps(marketplace), encoding="utf-8")

    result = subprocess.run(
        [
            sys.executable,
            str(checkout / "scripts/install_codex_skills.py"),
            "--target",
            str(tmp_path / "skills"),
        ],
        cwd=checkout,
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 1
    assert "duplicate skill target name 'duplicate' in plugin 'pm-agent'" in result.stderr


def test_reinstall_removes_obsolete_managed_unqualified_collision_alias(tmp_path: Path) -> None:
    target = tmp_path / "skills"

    first = run_installer(target)
    assert first.returncode == 0, first.stderr + first.stdout

    obsolete = target / "release-notes-generator"
    obsolete.symlink_to(
        Path(MIRROR_DIR) / "agents/docs/skills/release-notes-generator",
        target_is_directory=True,
    )

    second = run_installer(target)

    assert second.returncode == 0, second.stderr + second.stdout
    assert "Removed obsolete unqualified collision aliases:" in second.stdout
    assert not obsolete.exists()
    assert_relative_mirror_link(target, "pm-release-notes-generator")
    assert_relative_mirror_link(target, "docs-release-notes-generator")


def test_routers_only_links_only_router_skills_but_keeps_full_hidden_mirror(tmp_path: Path) -> None:
    target = tmp_path / "skills"

    result = run_installer(target, "--routers-only")

    assert result.returncode == 0, result.stderr + result.stdout
    assert "WARNING: --routers-only installed only role router skills." in result.stdout
    assert scanned_skill_entries(target) == router_skill_names()
    assert not (target / "debugger").exists()
    assert (target / MIRROR_DIR / skill_source_rel("debugger") / "SKILL.md").is_file()


def test_switching_to_routers_only_removes_previously_managed_specialist_links(tmp_path: Path) -> None:
    target = tmp_path / "skills"

    first = run_installer(target)
    assert first.returncode == 0, first.stderr + first.stdout

    second = run_installer(target, "--routers-only")

    assert second.returncode == 0, second.stderr + second.stdout
    assert "Removed unselected managed skills for --routers-only:" in second.stdout
    assert scanned_skill_entries(target) == router_skill_names()
    assert not (target / "debugger").exists()
    assert (target / MIRROR_DIR / skill_source_rel("debugger") / "SKILL.md").is_file()


def test_idempotent_reinstall_rebuilds_stale_hidden_mirror(tmp_path: Path) -> None:
    target = tmp_path / "skills"

    first = run_installer(target)
    assert first.returncode == 0, first.stderr + first.stdout
    stale = target / MIRROR_DIR / "stale.txt"
    stale.write_text("old", encoding="utf-8")

    second = run_installer(target)

    assert second.returncode == 0, second.stderr + second.stdout
    assert "updated: pm-agent" in second.stdout
    assert not stale.exists()
    assert (target / MIRROR_DIR / MIRROR_MARKER).is_file()
    assert scanned_skill_entries(target) == marketplace_skill_names()


def test_force_rebuilds_mirror_and_replaces_owned_links(tmp_path: Path) -> None:
    target = tmp_path / "skills"

    first = run_installer(target)
    assert first.returncode == 0, first.stderr + first.stdout
    skill_file = target / MIRROR_DIR / skill_source_rel("pm-agent") / "SKILL.md"
    skill_file.write_text("stale", encoding="utf-8")

    second = run_installer(target, "--force")

    assert second.returncode == 0, second.stderr + second.stdout
    assert "replaced: pm-agent" in second.stdout
    assert (target / MIRROR_DIR / MIRROR_MARKER).is_file()
    assert skill_file.read_text(encoding="utf-8").startswith("---")


def test_unowned_hidden_mirror_directory_errors_without_partial_changes(tmp_path: Path) -> None:
    for args in [(), ("--force",)]:
        target = tmp_path / ("skills-force" if args else "skills-default")
        mirror = target / MIRROR_DIR
        mirror.mkdir(parents=True)
        sentinel = mirror / "user-owned.txt"
        sentinel.write_text("keep", encoding="utf-8")

        result = run_installer(target, *args)

        assert result.returncode == 1
        assert "target contains a hidden mirror path that is not owned by this installer" in result.stderr
        assert sentinel.read_text(encoding="utf-8") == "keep"
        assert mirror.is_dir()
        assert not (mirror / MIRROR_MARKER).exists()
        assert not (target / "pm-agent").exists()


def test_unowned_selected_directory_is_skipped_without_force(tmp_path: Path) -> None:
    target = tmp_path / "skills"
    unowned = target / "pm-agent"
    unowned.mkdir(parents=True)
    (unowned / "SKILL.md").write_text("user skill", encoding="utf-8")

    result = run_installer(target)

    assert result.returncode == 0, result.stderr + result.stdout
    assert "skipped: pm-agent" in result.stdout
    assert (unowned / "SKILL.md").read_text(encoding="utf-8") == "user skill"
    assert not unowned.is_symlink()


def test_force_errors_on_unowned_selected_directory_without_partial_changes(tmp_path: Path) -> None:
    target = tmp_path / "skills"
    unowned = target / "pm-agent"
    unowned.mkdir(parents=True)
    (unowned / "SKILL.md").write_text("user skill", encoding="utf-8")

    result = run_installer(target, "--force")

    assert result.returncode == 1
    assert "--force target contains skill names that are not owned by this installer" in result.stderr
    assert (unowned / "SKILL.md").read_text(encoding="utf-8") == "user skill"
    assert not (target / MIRROR_DIR).exists()


def test_force_errors_on_unowned_unselected_directory_without_partial_changes(tmp_path: Path) -> None:
    target = tmp_path / "skills"
    unowned = target / "debugger"
    unowned.mkdir(parents=True)
    (unowned / "SKILL.md").write_text("user debugger", encoding="utf-8")

    result = run_installer(target, "--routers-only", "--force")

    assert result.returncode == 1
    assert "--force target contains skill names that are not owned by this installer" in result.stderr
    assert (unowned / "SKILL.md").read_text(encoding="utf-8") == "user debugger"
    assert not (target / MIRROR_DIR).exists()


def test_checkout_symlink_is_migrated_to_hidden_mirror_symlink(tmp_path: Path) -> None:
    target = tmp_path / "skills"
    target.mkdir(parents=True)
    old_checkout = tmp_path / "old-checkout"
    write_dev_agent_marketplace_marker(old_checkout)
    checkout_target = old_checkout / skill_source_rel("debugger")
    checkout_target.mkdir(parents=True)
    (target / "debugger").symlink_to(checkout_target, target_is_directory=True)

    result = run_installer(target)

    assert result.returncode == 0, result.stderr + result.stdout
    assert "migrated: debugger" in result.stdout
    assert_relative_mirror_link(target, "debugger")
    assert is_under(target / "debugger", target / MIRROR_DIR)


def test_selected_source_checkout_symlink_migrates_without_deleting_checkout(tmp_path: Path) -> None:
    target = tmp_path / "skills"
    target.mkdir(parents=True)
    checkout_target = ROOT / skill_source_rel("debugger")
    (target / "debugger").symlink_to(checkout_target, target_is_directory=True)

    result = run_installer(target)

    assert result.returncode == 0, result.stderr + result.stdout
    assert "migrated: debugger" in result.stdout
    assert_relative_mirror_link(target, "debugger")
    assert is_under(target / "debugger", target / MIRROR_DIR)
    assert checkout_target.is_dir()
    assert (checkout_target / "SKILL.md").is_file()
    assert INSTALLER.is_file()


def test_owned_legacy_aggregate_symlink_is_removed_before_install(tmp_path: Path) -> None:
    target = tmp_path / "skills"
    target.mkdir(parents=True)
    old_checkout = tmp_path / "old-checkout"
    write_dev_agent_marketplace_marker(old_checkout)
    (target / "dev-agent-skills").symlink_to(old_checkout, target_is_directory=True)

    result = run_installer(target)

    assert result.returncode == 0, result.stderr + result.stdout
    assert "Removed legacy aggregate entries:" in result.stdout
    assert not (target / "dev-agent-skills").exists()
    assert_relative_mirror_link(target, "pm-agent")


def test_source_checkout_inside_legacy_aggregate_delete_path_errors_without_deleting(
    tmp_path: Path,
) -> None:
    target = tmp_path / "skills"
    checkout = target / "dev-agent-skills"
    make_minimal_checkout(checkout)
    sentinel = checkout / "local-change.txt"
    sentinel.write_text("keep local checkout", encoding="utf-8")

    result = subprocess.run(
        [
            sys.executable,
            str(checkout / "scripts" / "install_codex_skills.py"),
            "--target",
            str(target),
        ],
        cwd=checkout,
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 1
    assert "安装源 checkout 位于目标删除路径内" in result.stderr
    assert sentinel.read_text(encoding="utf-8") == "keep local checkout"
    assert (checkout / ".claude-plugin/marketplace.json").is_file()
    assert (checkout / "agents/product_manager/skills/pm-agent/SKILL.md").is_file()
    assert not (target / MIRROR_DIR).exists()
    assert not (target / "pm-agent").exists()


def test_mirror_does_not_contain_plugin_manifests(tmp_path: Path) -> None:
    target = tmp_path / "skills"

    result = run_installer(target)

    assert result.returncode == 0, result.stderr + result.stdout
    assert plugin_manifest_paths(target) == []
    assert not list((target / MIRROR_DIR).rglob(".claude-plugin"))
    assert not list((target / MIRROR_DIR).rglob(".codex-plugin"))


def test_dot_prefixed_mirror_is_not_scanned_as_extra_skill_root(tmp_path: Path) -> None:
    target = tmp_path / "skills"

    result = run_installer(target)

    assert result.returncode == 0, result.stderr + result.stdout
    assert ".dev-agent-skills/agents/product_manager/skills/pm-agent" not in scanned_skill_entries(target)
    assert len(scanned_skill_entries(target)) == len(marketplace_skill_names())


def test_shared_skill_map_reference_is_reachable_inside_mirror_without_rewrite(tmp_path: Path) -> None:
    target = tmp_path / "skills"

    result = run_installer(target)

    assert result.returncode == 0, result.stderr + result.stdout
    skill_map = (
        target
        / MIRROR_DIR
        / "agents/product_manager/skills/idea-to-spec/_internal/_shared/skill-map.md"
    )
    assert skill_map.is_file()
    assert "agents/engineer/skills/trd-gen/SKILL.md" in skill_map.read_text(encoding="utf-8")
    assert (target / MIRROR_DIR / "agents/engineer/skills/trd-gen/SKILL.md").is_file()


def is_under(link: Path, parent: Path) -> bool:
    try:
        link.resolve(strict=True).relative_to(parent.resolve(strict=True))
    except ValueError:
        return False
    return True
