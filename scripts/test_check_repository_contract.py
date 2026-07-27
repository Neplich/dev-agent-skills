import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest


CONTRACT_PATH = Path(__file__).with_name("check_repository_contract.py")
CONTRACT_SPEC = importlib.util.spec_from_file_location(
    "check_repository_contract_under_test",
    CONTRACT_PATH,
)
assert CONTRACT_SPEC is not None
assert CONTRACT_SPEC.loader is not None
contract = importlib.util.module_from_spec(CONTRACT_SPEC)
sys.modules[CONTRACT_SPEC.name] = contract
CONTRACT_SPEC.loader.exec_module(contract)


FEATURE_PATH = "fixture-feature"
PLAN_REL = f"docs/engineer/{FEATURE_PATH}/IMPLEMENTATION_PLAN.md"
ARCHIVE_REL = (
    f"docs/engineer/{FEATURE_PATH}/implementation-plans/archive/"
    "IMPLEMENTATION_PLAN-completed-round.md"
)


def run_git(root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=root,
        check=True,
        text=True,
        capture_output=True,
    )
    return result.stdout.strip()


def write_plan(
    root: Path,
    *,
    status: str | None,
    scope: str = "next-round",
    version: str = "0.2.0",
    previous_archive: str | None = None,
) -> dict[str, str]:
    metadata = {
        "feature": FEATURE_PATH,
        "version": version,
        "date": "2026-07-27",
        "last_updated": "2026-07-27",
        "implementation_scope": scope,
    }
    if status is not None:
        metadata["status"] = status
    if previous_archive is not None:
        metadata["previous_plan_archive"] = previous_archive

    path = root / PLAN_REL
    path.parent.mkdir(parents=True, exist_ok=True)
    frontmatter = "\n".join(f'{key}: "{value}"' for key, value in metadata.items())
    path.write_text(f"---\n{frontmatter}\n---\n\n# Fixture plan\n", encoding="utf-8")
    return metadata


def commit_all(root: Path, message: str) -> None:
    run_git(root, "add", "--all")
    run_git(root, "commit", "-m", message)


def initialize_repo(
    tmp_path: Path,
    *,
    base_status: str | None,
    base_has_plan: bool = True,
) -> Path:
    root = tmp_path / "repo"
    root.mkdir()
    run_git(root, "init", "-b", "main")
    run_git(root, "config", "user.email", "fixture@example.com")
    run_git(root, "config", "user.name", "Fixture User")
    if base_has_plan:
        write_plan(root, status=base_status, scope="completed-round")
    else:
        (root / "README.md").write_text("# Fixture\n", encoding="utf-8")
    commit_all(root, "base")
    run_git(root, "switch", "-c", "fixture-change")
    return root


def validate_changed_plan(
    root: Path,
    metadata: dict[str, str],
) -> list[contract.ContractError]:
    base_ref = contract.implementation_plan_base_ref(root)
    assert base_ref == run_git(root, "merge-base", "HEAD", "main")
    changed_docs = set(contract.changed_files_against(root, base_ref))
    assert PLAN_REL in changed_docs

    errors: list[contract.ContractError] = []
    contract.validate_active_plan_archive_linkage(
        root,
        PLAN_REL,
        FEATURE_PATH,
        metadata,
        base_ref,
        True,
        changed_docs,
        errors,
    )
    return errors


def test_active_plan_status_is_unconditionally_required(tmp_path: Path) -> None:
    root = initialize_repo(tmp_path, base_status=None)

    errors: list[contract.ContractError] = []
    contract.validate_implementation_plan_metadata(root, errors)

    assert any(
        error.message == "frontmatter 'status' must be non-empty"
        for error in errors
    )


def test_implemented_base_requires_previous_archive(tmp_path: Path) -> None:
    root = initialize_repo(tmp_path, base_status="Implemented")
    metadata = write_plan(root, status="Draft")
    commit_all(root, "rewrite active plan")

    errors = validate_changed_plan(root, metadata)

    assert [error.message for error in errors] == [
        "frontmatter 'previous_plan_archive' must be non-empty because the active plan "
        "status on the base ref is 'Implemented'; archive that plan before modifying it"
    ]


def test_non_implemented_base_allows_plan_update_without_archive(tmp_path: Path) -> None:
    root = initialize_repo(tmp_path, base_status="Draft")
    metadata = write_plan(root, status="Pending Confirmation")
    commit_all(root, "update draft plan")

    assert validate_changed_plan(root, metadata) == []


def test_implemented_base_allows_valid_previous_archive(tmp_path: Path) -> None:
    root = initialize_repo(tmp_path, base_status="Implemented")
    archive_path = root / ARCHIVE_REL
    archive_path.parent.mkdir(parents=True)
    archive_path.write_text("# Archived fixture plan\n", encoding="utf-8")
    metadata = write_plan(
        root,
        status="Pending Confirmation",
        previous_archive=ARCHIVE_REL,
    )
    commit_all(root, "archive completed plan and add replacement")

    assert validate_changed_plan(root, metadata) == []


def test_new_plan_without_base_file_does_not_require_archive(tmp_path: Path) -> None:
    root = initialize_repo(tmp_path, base_status=None, base_has_plan=False)
    metadata = write_plan(root, status="Pending Confirmation")
    commit_all(root, "add first plan")

    assert validate_changed_plan(root, metadata) == []


def test_closeout_archive_in_same_change_allows_missing_back_link(tmp_path: Path) -> None:
    root = initialize_repo(tmp_path, base_status="Implemented")
    archive_path = root / ARCHIVE_REL
    archive_path.parent.mkdir(parents=True)
    archive_path.write_text("# Archived fixture plan\n", encoding="utf-8")
    metadata = write_plan(
        root,
        status="Implemented",
        scope="completed-round",
        version="0.3.0",
    )
    commit_all(root, "close out plan and add archive")

    assert validate_changed_plan(root, metadata) == []


def test_missing_base_ref_does_not_add_archive_linkage_error(tmp_path: Path) -> None:
    root = tmp_path / "repo"
    root.mkdir()
    run_git(root, "init", "-b", "fixture-change")
    run_git(root, "config", "user.email", "fixture@example.com")
    run_git(root, "config", "user.name", "Fixture User")
    metadata = write_plan(root, status="Pending Confirmation")
    commit_all(root, "add plan without main ref")
    assert contract.implementation_plan_base_ref(root) is None

    errors: list[contract.ContractError] = []
    contract.validate_active_plan_archive_linkage(
        root,
        PLAN_REL,
        FEATURE_PATH,
        metadata,
        None,
        True,
        {PLAN_REL},
        errors,
    )

    assert errors == []


@pytest.mark.parametrize(
    ("previous_archive", "expected_message"),
    [
        (
            f"docs/engineer/{FEATURE_PATH}/not-an-archive.md",
            "must point to an implementation-plans/archive/"
            "IMPLEMENTATION_PLAN-<scope>.md path",
        ),
        (
            "docs/engineer/other-feature/implementation-plans/archive/"
            "IMPLEMENTATION_PLAN-completed-round.md",
            f"must reference an archive on feature_path {FEATURE_PATH!r}",
        ),
        (
            ARCHIVE_REL,
            "must point to an existing archive file",
        ),
    ],
)
def test_previous_archive_is_always_validated(
    tmp_path: Path,
    previous_archive: str,
    expected_message: str,
) -> None:
    root = initialize_repo(tmp_path, base_status="Draft")
    metadata = write_plan(
        root,
        status="Pending Confirmation",
        previous_archive=previous_archive,
    )
    commit_all(root, "add invalid archive linkage")

    errors = validate_changed_plan(root, metadata)

    assert len(errors) == 1
    assert expected_message in errors[0].message
