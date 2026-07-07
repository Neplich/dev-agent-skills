import json
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INSTALLER = ROOT / "scripts" / "install_codex_skills.py"
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
MIRROR_DIR = ".dev-agent-skills"


def run_installer(target: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(INSTALLER), "--target", str(target), *args],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


def marketplace_data() -> dict:
    return json.loads(MARKETPLACE.read_text(encoding="utf-8"))


def marketplace_skill_names() -> list[str]:
    names: list[str] = []
    for plugin in marketplace_data()["plugins"]:
        plugin_source = ROOT / plugin["source"]
        for skill_path in plugin["skills"]:
            names.append((plugin_source / skill_path).resolve().name)
    return sorted(names)


def router_skill_names() -> list[str]:
    return sorted(plugin["name"] for plugin in marketplace_data()["plugins"])


def skill_source_rel(skill_name: str) -> Path:
    for plugin in marketplace_data()["plugins"]:
        plugin_source = (ROOT / plugin["source"]).resolve()
        for skill_path in plugin["skills"]:
            source = (plugin_source / skill_path).resolve()
            if source.name == skill_name:
                return source.relative_to(ROOT)
    raise AssertionError(f"unknown skill {skill_name}")


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
    assert_relative_mirror_link(target, "pm-agent")
    assert_relative_mirror_link(target, "debugger")


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
    assert skill_file.read_text(encoding="utf-8").startswith("---")


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
    checkout_target = ROOT / skill_source_rel("debugger")
    (target / "debugger").symlink_to(checkout_target, target_is_directory=True)

    result = run_installer(target)

    assert result.returncode == 0, result.stderr + result.stdout
    assert "migrated: debugger" in result.stdout
    assert_relative_mirror_link(target, "debugger")
    assert is_under(target / "debugger", target / MIRROR_DIR)


def test_owned_legacy_aggregate_symlink_is_removed_before_install(tmp_path: Path) -> None:
    target = tmp_path / "skills"
    target.mkdir(parents=True)
    (target / "dev-agent-skills").symlink_to(ROOT, target_is_directory=True)

    result = run_installer(target)

    assert result.returncode == 0, result.stderr + result.stdout
    assert "Removed legacy aggregate entries:" in result.stdout
    assert not (target / "dev-agent-skills").exists()
    assert_relative_mirror_link(target, "pm-agent")


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
