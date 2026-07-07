import json
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INSTALLER = ROOT / "scripts" / "install_codex_skills.py"
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
SUPPORT_DIR = ".dev-agent-skills-support"


def run_installer(target: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(INSTALLER), "--target", str(target), *args],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


def marketplace_skill_names() -> list[str]:
    data = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    names: list[str] = []
    for plugin in data["plugins"]:
        plugin_source = ROOT / plugin["source"]
        for skill_path in plugin["skills"]:
            names.append((plugin_source / skill_path).resolve().name)
    return sorted(names)


def router_skill_names() -> list[str]:
    data = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    return sorted(plugin["name"] for plugin in data["plugins"])


def scanned_skill_entries(skill_root: Path) -> list[str]:
    entries: list[str] = []
    for current, dirs, files in os.walk(skill_root, followlinks=True):
        dirs[:] = [name for name in dirs if not name.startswith(".")]
        if "SKILL.md" in files:
            entries.append(Path(current).relative_to(skill_root).as_posix())
    return sorted(entries)


def test_default_install_hides_support_reference_from_skill_scan(tmp_path: Path) -> None:
    target = tmp_path / "skills"

    result = run_installer(target)

    assert result.returncode == 0, result.stderr + result.stdout
    assert scanned_skill_entries(target) == marketplace_skill_names()
    assert not (target / "pm-agent" / "agents").exists()
    assert (target / "pm-agent" / SUPPORT_DIR).exists()

    skill_map = (
        target
        / "pm-agent"
        / SUPPORT_DIR
        / "agents/product_manager/skills/idea-to-spec/_internal/_shared/skill-map.md"
    )
    assert skill_map.is_file()
    assert f"{SUPPORT_DIR}/agents/product_manager/skills/idea-to-spec/_internal/_shared/skill-map.md" in (
        target / "pm-agent" / "SKILL.md"
    ).read_text(encoding="utf-8")


def test_routers_only_scan_excludes_support_tree_specialists(tmp_path: Path) -> None:
    target = tmp_path / "skills"

    result = run_installer(target, "--routers-only")

    assert result.returncode == 0, result.stderr + result.stdout
    assert "WARNING: --routers-only installed only role router skills." in result.stdout
    assert scanned_skill_entries(target) == router_skill_names()
    assert not (target / "debugger").exists()
    assert (
        target
        / SUPPORT_DIR
        / "agents/engineer/skills/debugger/SKILL.md"
    ).is_file()
