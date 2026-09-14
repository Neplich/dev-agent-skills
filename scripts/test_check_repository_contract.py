import importlib.util
import json
import sys
from pathlib import Path

import pytest

CONTRACT_PATH = Path(__file__).with_name("check_repository_contract.py")
CONTRACT_SPEC = importlib.util.spec_from_file_location(
    "check_repository_contract_under_test", CONTRACT_PATH,
)
assert CONTRACT_SPEC is not None and CONTRACT_SPEC.loader is not None
contract = importlib.util.module_from_spec(CONTRACT_SPEC)
sys.modules[CONTRACT_SPEC.name] = contract
CONTRACT_SPEC.loader.exec_module(contract)


@pytest.mark.parametrize(
    ("relative_path", "length", "should_fail"),
    [
        ("agents/engineer/skills/debugger/SKILL.md", 500, False),
        (".agents/skills/maintain-skills/SKILL.md", 501, True),
    ],
)
def test_skill_description_length_limit_includes_project_skills(
    tmp_path: Path,
    relative_path: str,
    length: int,
    should_fail: bool,
) -> None:
    skill_doc = tmp_path / relative_path
    skill_doc.parent.mkdir(parents=True)
    skill_doc.write_text(
        "---\n"
        f"name: {skill_doc.parent.name}\n"
        f'description: "{"x" * length}"\n'
        "---\n",
        encoding="utf-8",
    )

    errors: list[contract.ContractError] = []
    contract.validate_skill_description_lengths(tmp_path, errors)

    assert bool(errors) is should_fail
    if should_fail:
        assert "exceeds 500 characters: 501" in errors[0].message


def test_plugin_description_must_match_marketplace(tmp_path: Path) -> None:
    marketplace_path = tmp_path / ".claude-plugin/marketplace.json"
    manifest_path = tmp_path / "agents/engineer/.claude-plugin/plugin.json"
    manifest_path.parent.mkdir(parents=True)
    manifest_path.write_text(
        json.dumps(
            {
                "name": "engineer-agent",
                "version": "0.5.1",
                "description": "Stale plugin description",
            }
        ),
        encoding="utf-8",
    )

    errors: list[contract.ContractError] = []
    contract.validate_plugin_manifest(
        manifest_path,
        marketplace_path,
        0,
        "engineer-agent",
        "0.5.1",
        "Current marketplace description",
        errors,
    )

    assert len(errors) == 1
    assert "description must match marketplace" in errors[0].message


def write_kimi_fixture(
    root: Path,
    *,
    manifest: dict | None,
    marketplace_version: str = "0.3.5",
    skill_dir: str = "agents/product_manager/skills/pm-agent",
) -> Path:
    (root / ".claude-plugin").mkdir(parents=True, exist_ok=True)
    (root / ".claude-plugin" / "marketplace.json").write_text(
        json.dumps({"metadata": {"version": marketplace_version}})
    )
    if skill_dir is not None:
        skill_path = root / skill_dir
        skill_path.mkdir(parents=True, exist_ok=True)
        (skill_path / "SKILL.md").write_text("---\nname: pm-agent\n---\n")
    if manifest is not None:
        (root / ".kimi-plugin").mkdir(parents=True, exist_ok=True)
        (root / ".kimi-plugin" / "plugin.json").write_text(json.dumps(manifest))
    return root


def valid_kimi_manifest() -> dict:
    return {
        "name": "dev-agent-skills",
        "version": "0.3.5",
        "skills": ["./agents/product_manager/skills/"],
    }


def test_kimi_plugin_valid_manifest_passes(tmp_path: Path) -> None:
    root = write_kimi_fixture(tmp_path, manifest=valid_kimi_manifest())

    errors: list = []
    contract.validate_kimi_plugin(root, errors)

    assert errors == []


def test_kimi_plugin_missing_manifest_fails(tmp_path: Path) -> None:
    root = write_kimi_fixture(tmp_path, manifest=None)

    errors: list = []
    contract.validate_kimi_plugin(root, errors)

    assert len(errors) == 1
    assert "must exist" in errors[0].message


def test_kimi_plugin_version_must_match_marketplace(tmp_path: Path) -> None:
    manifest = valid_kimi_manifest()
    manifest["version"] = "0.0.1"
    root = write_kimi_fixture(tmp_path, manifest=manifest)

    errors: list = []
    contract.validate_kimi_plugin(root, errors)

    assert len(errors) == 1
    assert "version must match marketplace metadata.version" in errors[0].message


def test_kimi_plugin_name_pattern_enforced(tmp_path: Path) -> None:
    manifest = valid_kimi_manifest()
    manifest["name"] = "Dev-Agent-Skills"
    root = write_kimi_fixture(tmp_path, manifest=manifest)

    errors: list = []
    contract.validate_kimi_plugin(root, errors)

    assert len(errors) == 1
    assert "name must match" in errors[0].message


def test_kimi_plugin_skills_path_must_exist(tmp_path: Path) -> None:
    manifest = valid_kimi_manifest()
    manifest["skills"] = ["./agents/missing/skills/"]
    root = write_kimi_fixture(tmp_path, manifest=manifest)

    errors: list = []
    contract.validate_kimi_plugin(root, errors)

    assert len(errors) == 1
    assert "does not exist" in errors[0].message


def test_kimi_plugin_session_start_skill_must_exist(tmp_path: Path) -> None:
    manifest = valid_kimi_manifest()
    manifest["sessionStart"] = {"skill": "unknown-skill"}
    root = write_kimi_fixture(tmp_path, manifest=manifest)

    errors: list = []
    contract.validate_kimi_plugin(root, errors)

    assert len(errors) == 1
    assert "sessionStart.skill" in errors[0].message


def test_kimi_plugin_single_string_skills_form_accepted(tmp_path: Path) -> None:
    manifest = valid_kimi_manifest()
    manifest["skills"] = "./agents/product_manager/skills/"
    root = write_kimi_fixture(tmp_path, manifest=manifest)

    errors: list = []
    contract.validate_kimi_plugin(root, errors)

    assert errors == []


def test_kimi_plugin_session_start_skill_glob_metachar_rejected(tmp_path: Path) -> None:
    manifest = valid_kimi_manifest()
    manifest["sessionStart"] = {"skill": "[p]m-agent"}
    root = write_kimi_fixture(tmp_path, manifest=manifest)

    errors: list = []
    contract.validate_kimi_plugin(root, errors)

    assert len(errors) == 1
    assert "sessionStart.skill" in errors[0].message


def test_each_skill_accepts_direct_user_trigger_without_role_metadata(tmp_path: Path) -> None:
    for name in ("pm-agent", "debugger", "manual-gen"):
        skill = tmp_path / "agents/example/skills" / name
        skill.mkdir(parents=True)
        (skill / "SKILL.md").write_text(
            f'---\nname: {name}\ndescription: "Use when the user asks for this capability."\n---\n'
        )
        errors = []
        contract.validate_skill(tmp_path, skill, errors)
        assert errors == []


def test_kimi_plugin_accepts_optional_explicit_session_skill(tmp_path: Path) -> None:
    manifest = valid_kimi_manifest()
    manifest["sessionStart"] = {"skill": "pm-agent"}
    write_kimi_fixture(tmp_path, manifest=manifest)
    errors = []
    contract.validate_kimi_plugin(tmp_path, errors)
    assert errors == []
