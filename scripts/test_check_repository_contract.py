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
REQUIRED_BACKLINK_ERROR = (
    "frontmatter 'previous_plan_archive' must be non-empty because the base "
    "round for this active plan is already settled and its content has changed; "
    "link the new plan to an archive that faithfully preserves it"
)
FIDELITY_ERROR = (
    "frontmatter 'previous_plan_archive' must reference an archive whose body "
    "faithfully preserves the base active plan"
)


def archive_rel(scope: str) -> str:
    return (
        f"docs/engineer/{FEATURE_PATH}/implementation-plans/archive/"
        f"IMPLEMENTATION_PLAN-{scope}.md"
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
    scope: str | None = "next-round",
    version: str = "0.2.0",
    last_updated: str = "2026-07-27",
    previous_archive: str | None = None,
    body: str = "# Fixture plan\n",
) -> dict[str, str]:
    metadata = {
        "feature": FEATURE_PATH,
        "version": version,
        "date": "2026-07-27",
        "last_updated": last_updated,
    }
    if scope is not None:
        metadata["implementation_scope"] = scope
    if status is not None:
        metadata["status"] = status
    if previous_archive is not None:
        metadata["previous_plan_archive"] = previous_archive

    path = root / PLAN_REL
    path.parent.mkdir(parents=True, exist_ok=True)
    frontmatter = "\n".join(f'{key}: "{value}"' for key, value in metadata.items())
    path.write_text(f"---\n{frontmatter}\n---\n\n{body}", encoding="utf-8")
    return metadata


def write_archive(
    root: Path,
    *,
    scope: str = "completed-round",
    status: str = "Archived",
    archived_at: str = "2026-07-27",
    body: str = "# Archived fixture plan\n",
) -> None:
    archive_path = root / archive_rel(scope)
    archive_path.parent.mkdir(parents=True, exist_ok=True)
    superseded_reason = (
        'superseded_reason: "The round was abandoned."\n'
        if status == "Superseded"
        else ""
    )
    archive_path.write_text(
        "---\n"
        f'implementation_scope: "{scope}"\n'
        f'status: "{status}"\n'
        f'archived_at: "{archived_at}"\n'
        f"{superseded_reason}"
        "---\n\n"
        f"{body}",
        encoding="utf-8",
    )


def commit_all(root: Path, message: str) -> None:
    run_git(root, "add", "--all")
    run_git(root, "commit", "-m", message)


def initialize_repo(
    tmp_path: Path,
    *,
    base_status: str | None,
    base_has_plan: bool = True,
    base_has_archive: bool = False,
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
    if base_has_archive:
        write_archive(root)
    commit_all(root, "base")
    run_git(root, "switch", "-c", "fixture-change")
    return root


def initialize_repo_with_prior_link(
    tmp_path: Path,
    *,
    base_status: str,
) -> tuple[Path, str]:
    root = initialize_repo(tmp_path, base_status="Draft")
    run_git(root, "switch", "main")
    prior_archive = archive_rel("older-round")
    write_archive(root, scope="older-round")
    write_plan(
        root,
        status=base_status,
        scope="current-round",
        previous_archive=prior_archive,
    )
    commit_all(root, "add active plan with prior archive link")
    run_git(root, "switch", "-C", "fixture-change")
    return root, prior_archive


def validate_changed_plan(
    root: Path,
    metadata: dict[str, str],
) -> list[contract.ContractError]:
    base_ref = contract.implementation_plan_base_ref(root)
    assert base_ref == run_git(root, "merge-base", "HEAD", "main")
    changed_docs = set(contract.changed_files_against(root, base_ref))
    assert PLAN_REL in changed_docs
    parsed = contract.parse_markdown_frontmatter(
        root / PLAN_REL,
        (root / PLAN_REL).read_text(encoding="utf-8"),
        errors=None,
    )
    assert parsed is not None

    errors: list[contract.ContractError] = []
    contract.validate_active_plan_archive_linkage(
        root,
        PLAN_REL,
        FEATURE_PATH,
        metadata,
        parsed[1],
        base_ref,
        True,
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


def test_active_plan_status_rejects_noncanonical_value(tmp_path: Path) -> None:
    root = initialize_repo(tmp_path, base_status="Implementd")

    errors: list[contract.ContractError] = []
    contract.validate_implementation_plan_metadata(root, errors)

    assert any(
        error.message
        == (
            "frontmatter 'status' must be one of: 'Draft', 'Historical', "
            "'Implemented', 'Legacy', 'Pending Confirmation'"
        )
        for error in errors
    )


def test_implemented_base_with_changed_body_requires_previous_archive(
    tmp_path: Path,
) -> None:
    root = initialize_repo(tmp_path, base_status="Implemented")
    metadata = write_plan(
        root,
        status="Implemented",
        scope="completed-round",
        body="# Replacement plan\n",
    )
    commit_all(root, "rewrite active plan")

    errors = validate_changed_plan(root, metadata)

    assert [error.message for error in errors] == [REQUIRED_BACKLINK_ERROR]


def test_draft_base_with_changed_body_allows_continued_update_without_archive(
    tmp_path: Path,
) -> None:
    root = initialize_repo(tmp_path, base_status="Draft")
    metadata = write_plan(
        root,
        status="Pending Confirmation",
        body="# Expanded fixture plan\n",
    )
    commit_all(root, "update draft plan")

    assert validate_changed_plan(root, metadata) == []


def test_faithful_previous_archive_with_any_scope_is_allowed(tmp_path: Path) -> None:
    root = initialize_repo(tmp_path, base_status="Implemented")
    faithful_archive = archive_rel("descriptive-label-only")
    write_archive(
        root,
        scope="descriptive-label-only",
        body="# Fixture plan\n",
    )
    metadata = write_plan(
        root,
        status="Pending Confirmation",
        previous_archive=faithful_archive,
        body="# Replacement plan\n",
    )
    commit_all(root, "archive completed plan and add replacement")

    assert validate_changed_plan(root, metadata) == []


def test_legacy_implemented_base_allows_faithful_archive_with_any_scope(
    tmp_path: Path,
) -> None:
    root = initialize_repo(tmp_path, base_status="Draft")
    run_git(root, "switch", "main")
    write_plan(root, status="Implemented", scope=None)
    commit_all(root, "add legacy implemented plan without scope")
    run_git(root, "switch", "-C", "fixture-change")
    legacy_archive = archive_rel("legacy-round")
    write_archive(root, scope="legacy-round", body="# Fixture plan\n")
    metadata = write_plan(
        root,
        status="Pending Confirmation",
        scope="replacement-round",
        previous_archive=legacy_archive,
        body="# Replacement plan\n",
    )
    commit_all(root, "faithfully archive legacy plan and add replacement")

    assert validate_changed_plan(root, metadata) == []


def test_legacy_implemented_base_rejects_unfaithful_archive(
    tmp_path: Path,
) -> None:
    root = initialize_repo(tmp_path, base_status="Draft")
    run_git(root, "switch", "main")
    write_plan(root, status="Implemented", scope=None)
    commit_all(root, "add legacy implemented plan without scope")
    run_git(root, "switch", "-C", "fixture-change")
    legacy_archive = archive_rel("legacy-round")
    write_archive(root, scope="legacy-round", body="# Unrelated plan\n")
    metadata = write_plan(
        root,
        status="Pending Confirmation",
        scope="replacement-round",
        previous_archive=legacy_archive,
        body="# Replacement plan\n",
    )
    commit_all(root, "forge archive for legacy plan")

    errors = validate_changed_plan(root, metadata)

    assert [error.message for error in errors] == [
        "frontmatter 'previous_plan_archive' must reference an archive whose "
        "body faithfully preserves the base active plan"
    ]


def test_matching_scope_archive_rejects_unfaithful_base_body(
    tmp_path: Path,
) -> None:
    root = initialize_repo(tmp_path, base_status="Implemented")
    write_archive(root, body="# Unrelated plan\n")
    metadata = write_plan(
        root,
        status="Pending Confirmation",
        previous_archive=ARCHIVE_REL,
        body="# Replacement plan\n",
    )
    commit_all(root, "forge matching-scope archive")

    errors = validate_changed_plan(root, metadata)

    assert [error.message for error in errors] == [
        "frontmatter 'previous_plan_archive' must reference an archive whose "
        "body faithfully preserves the base active plan"
    ]


def test_different_scope_archive_is_rejected_only_when_body_is_unfaithful(
    tmp_path: Path,
) -> None:
    root = initialize_repo(tmp_path, base_status="Implemented")
    older_archive = archive_rel("older-round")
    write_archive(root, scope="older-round")
    metadata = write_plan(
        root,
        status="Pending Confirmation",
        previous_archive=older_archive,
    )
    commit_all(root, "link replacement to older archive")

    errors = validate_changed_plan(root, metadata)

    assert [error.message for error in errors] == [FIDELITY_ERROR]


def test_unchanged_active_plan_keeps_link_to_prior_round(tmp_path: Path) -> None:
    root, prior_archive = initialize_repo_with_prior_link(
        tmp_path,
        base_status="Implemented",
    )
    metadata = write_plan(
        root,
        status="Implemented",
        scope="current-round",
        previous_archive=prior_archive,
    )
    parsed = contract.parse_markdown_frontmatter(
        root / PLAN_REL,
        (root / PLAN_REL).read_text(encoding="utf-8"),
        errors=None,
    )
    assert parsed is not None

    errors: list[contract.ContractError] = []
    contract.validate_active_plan_archive_linkage(
        root,
        PLAN_REL,
        FEATURE_PATH,
        metadata,
        parsed[1],
        contract.implementation_plan_base_ref(root),
        False,
        errors,
    )

    assert errors == []


def test_implemented_plan_frontmatter_update_keeps_prior_round_link(
    tmp_path: Path,
) -> None:
    root, prior_archive = initialize_repo_with_prior_link(
        tmp_path,
        base_status="Implemented",
    )
    metadata = write_plan(
        root,
        status="Implemented",
        scope="current-round",
        previous_archive=prior_archive,
        last_updated="2026-07-28",
    )
    commit_all(root, "update implemented plan metadata")

    assert validate_changed_plan(root, metadata) == []


def test_implemented_plan_status_regression_cannot_reuse_prior_round_link(
    tmp_path: Path,
) -> None:
    root, prior_archive = initialize_repo_with_prior_link(
        tmp_path,
        base_status="Implemented",
    )
    metadata = write_plan(
        root,
        status="Draft",
        scope="current-round",
        previous_archive=prior_archive,
    )
    commit_all(root, "regress implemented plan status")

    errors = validate_changed_plan(root, metadata)

    assert [error.message for error in errors] == [FIDELITY_ERROR]


def test_draft_continuation_keeps_link_to_prior_round(tmp_path: Path) -> None:
    root, prior_archive = initialize_repo_with_prior_link(
        tmp_path,
        base_status="Draft",
    )
    metadata = write_plan(
        root,
        status="Pending Confirmation",
        scope="current-round",
        previous_archive=prior_archive,
        body="# Expanded current round\n",
    )
    commit_all(root, "continue draft with prior archive link")

    assert validate_changed_plan(root, metadata) == []


def test_new_plan_without_base_file_does_not_require_archive(tmp_path: Path) -> None:
    root = initialize_repo(tmp_path, base_status=None, base_has_plan=False)
    metadata = write_plan(root, status="Pending Confirmation")
    commit_all(root, "add first plan")

    assert validate_changed_plan(root, metadata) == []


def test_new_plan_without_base_file_requires_back_link_when_archive_history_exists(
    tmp_path: Path,
) -> None:
    root = initialize_repo(
        tmp_path,
        base_status=None,
        base_has_plan=False,
        base_has_archive=True,
    )
    metadata = write_plan(root, status="Pending Confirmation")
    commit_all(root, "add next plan without archive link")

    errors = validate_changed_plan(root, metadata)

    assert [error.message for error in errors] == [
        "frontmatter 'previous_plan_archive' must be non-empty because this "
        "feature_path already has archived plan history; a new active plan must "
        "link to the previous archive"
    ]


def test_new_plan_cannot_hide_base_archive_history_by_deleting_archives(
    tmp_path: Path,
) -> None:
    root = initialize_repo(tmp_path, base_status=None, base_has_plan=False)
    run_git(root, "switch", "main")
    write_archive(root)
    commit_all(root, "add historical archive")
    run_git(root, "switch", "-C", "fixture-change")
    (root / ARCHIVE_REL).unlink()
    metadata = write_plan(root, status="Pending Confirmation")
    commit_all(root, "delete archive history and add an unlinked active plan")

    errors = validate_changed_plan(root, metadata)

    assert [error.message for error in errors] == [
        "frontmatter 'previous_plan_archive' must be non-empty because this "
        "feature_path already has archived plan history; a new active plan must "
        "link to the previous archive"
    ]


def test_new_plan_and_matching_archive_in_same_change_requires_back_link(
    tmp_path: Path,
) -> None:
    root = initialize_repo(tmp_path, base_status=None, base_has_plan=False)
    write_archive(root)
    metadata = write_plan(
        root,
        status="Implemented",
        scope="completed-round",
    )
    commit_all(root, "add plan and matching archive")

    errors = validate_changed_plan(root, metadata)

    assert [error.message for error in errors] == [
        "frontmatter 'previous_plan_archive' must be non-empty because this "
        "feature_path already has archived plan history; a new active plan must "
        "link to the previous archive"
    ]


def test_scope_less_unfinished_base_is_settled_by_faithful_archive(
    tmp_path: Path,
) -> None:
    root = initialize_repo(tmp_path, base_status="Draft")
    run_git(root, "switch", "main")
    write_plan(root, status="Pending Confirmation", scope=None)
    write_archive(
        root,
        scope="legacy-pending-round",
        status="Superseded",
        body="# Fixture plan\n",
    )
    commit_all(root, "add archived legacy pending plan without scope")
    run_git(root, "switch", "-C", "fixture-change")
    metadata = write_plan(
        root,
        status="Pending Confirmation",
        scope="replacement-round",
        body="# Replacement plan\n",
    )
    commit_all(root, "supersede legacy pending plan and add replacement")

    errors = validate_changed_plan(root, metadata)

    assert [error.message for error in errors] == [REQUIRED_BACKLINK_ERROR]


def test_new_plan_without_base_file_rejects_link_to_older_archive(
    tmp_path: Path,
) -> None:
    root = initialize_repo(tmp_path, base_status=None, base_has_plan=False)
    run_git(root, "switch", "main")
    older_archive = archive_rel("older-round")
    write_archive(root, scope="older-round", archived_at="2026-07-25")
    write_archive(root, scope="newer-round", archived_at="2026-07-26")
    commit_all(root, "add two historical archives")
    run_git(root, "switch", "-C", "fixture-change")
    metadata = write_plan(
        root,
        status="Pending Confirmation",
        previous_archive=older_archive,
    )
    commit_all(root, "link new plan to older archive")

    errors = validate_changed_plan(root, metadata)

    assert [error.message for error in errors] == [
        "frontmatter 'previous_plan_archive' must reference the most recent "
        "archive for this feature_path ('newer-round'), not an older archive"
    ]


def test_new_plan_without_base_file_allows_link_to_latest_archive(
    tmp_path: Path,
) -> None:
    root = initialize_repo(tmp_path, base_status=None, base_has_plan=False)
    run_git(root, "switch", "main")
    write_archive(root, scope="older-round", archived_at="2026-07-25")
    newer_archive = archive_rel("newer-round")
    write_archive(root, scope="newer-round", archived_at="2026-07-26")
    commit_all(root, "add two historical archives")
    run_git(root, "switch", "-C", "fixture-change")
    metadata = write_plan(
        root,
        status="Pending Confirmation",
        previous_archive=newer_archive,
    )
    commit_all(root, "link new plan to latest archive")

    assert validate_changed_plan(root, metadata) == []


@pytest.mark.parametrize("linked_scope", ["first-latest-round", "second-latest-round"])
def test_new_plan_allows_link_to_any_archive_tied_for_latest_date(
    tmp_path: Path,
    linked_scope: str,
) -> None:
    root = initialize_repo(tmp_path, base_status=None, base_has_plan=False)
    run_git(root, "switch", "main")
    write_archive(root, scope="first-latest-round", archived_at="2026-07-27")
    write_archive(root, scope="second-latest-round", archived_at="2026-07-27")
    commit_all(root, "add two archives on the latest date")
    run_git(root, "switch", "-C", "fixture-change")
    metadata = write_plan(
        root,
        status="Pending Confirmation",
        previous_archive=archive_rel(linked_scope),
    )
    commit_all(root, f"link new plan to {linked_scope}")

    assert validate_changed_plan(root, metadata) == []


def test_new_plan_without_base_file_allows_link_to_same_change_latest_archive(
    tmp_path: Path,
) -> None:
    root = initialize_repo(tmp_path, base_status=None, base_has_plan=False)
    run_git(root, "switch", "main")
    write_archive(root, scope="older-round", archived_at="2026-07-25")
    commit_all(root, "add historical archive")
    run_git(root, "switch", "-C", "fixture-change")
    current_archive = archive_rel("current-round")
    write_archive(root, scope="current-round", archived_at="2026-07-27")
    metadata = write_plan(
        root,
        status="Pending Confirmation",
        previous_archive=current_archive,
    )
    commit_all(root, "add current archive and linked plan")

    assert validate_changed_plan(root, metadata) == []


def test_new_plan_without_base_file_rejects_edited_stale_archive(
    tmp_path: Path,
) -> None:
    root = initialize_repo(tmp_path, base_status=None, base_has_plan=False)
    run_git(root, "switch", "main")
    stale_archive = archive_rel("stale-round")
    write_archive(root, scope="stale-round", archived_at="2026-07-25")
    write_archive(root, scope="latest-round", archived_at="2026-07-27")
    commit_all(root, "add stale and latest archives")
    run_git(root, "switch", "-C", "fixture-change")
    write_archive(
        root,
        scope="stale-round",
        archived_at="2026-07-25",
        body="# Edited stale archive\n",
    )
    metadata = write_plan(
        root,
        status="Pending Confirmation",
        previous_archive=stale_archive,
    )
    commit_all(root, "edit stale archive and link new plan to it")

    errors = validate_changed_plan(root, metadata)

    assert [error.message for error in errors] == [
        "frontmatter 'previous_plan_archive' must reference the most recent "
        "archive for this feature_path ('latest-round'), not an older archive"
    ]


def test_new_plan_without_base_file_allows_link_to_only_archive(
    tmp_path: Path,
) -> None:
    root = initialize_repo(
        tmp_path,
        base_status=None,
        base_has_plan=False,
        base_has_archive=True,
    )
    metadata = write_plan(
        root,
        status="Pending Confirmation",
        previous_archive=ARCHIVE_REL,
    )
    commit_all(root, "link new plan to only archive")

    assert validate_changed_plan(root, metadata) == []


@pytest.mark.parametrize(
    "regressed_status",
    ["Draft", "Historical", "Legacy", "Pending Confirmation"],
)
def test_implemented_base_with_unchanged_body_rejects_status_regression(
    tmp_path: Path,
    regressed_status: str,
) -> None:
    root = initialize_repo(tmp_path, base_status="Implemented")
    metadata = write_plan(
        root,
        status=regressed_status,
        scope="completed-round",
    )
    commit_all(root, f"regress implemented plan status to {regressed_status}")

    errors = validate_changed_plan(root, metadata)

    assert [error.message for error in errors] == [REQUIRED_BACKLINK_ERROR]


def test_draft_closeout_with_faithful_archive_allows_status_only_progression(
    tmp_path: Path,
) -> None:
    root = initialize_repo(tmp_path, base_status="Draft")
    write_archive(root, body="# Fixture plan\n")
    metadata = write_plan(
        root,
        status="Implemented",
        scope="completed-round",
    )
    commit_all(root, "close out draft with faithful archive")

    assert validate_changed_plan(root, metadata) == []


def test_previously_archived_draft_allows_status_only_progression(
    tmp_path: Path,
) -> None:
    root = initialize_repo(tmp_path, base_status="Draft")
    run_git(root, "switch", "main")
    write_archive(root, body="# Fixture plan\n")
    commit_all(root, "archive draft before status progression")
    run_git(root, "switch", "-C", "fixture-change")
    metadata = write_plan(
        root,
        status="Implemented",
        scope="completed-round",
    )
    commit_all(root, "advance archived draft status without changing its body")

    assert validate_changed_plan(root, metadata) == []


def test_implemented_base_with_unchanged_body_allows_frontmatter_only_update(
    tmp_path: Path,
) -> None:
    root = initialize_repo(tmp_path, base_status="Implemented")
    metadata = write_plan(
        root,
        status="Implemented",
        scope="completed-round",
        last_updated="2026-07-28",
    )
    commit_all(root, "update closeout metadata")

    assert validate_changed_plan(root, metadata) == []


def test_implemented_base_rejects_replacing_unchanged_back_link(
    tmp_path: Path,
) -> None:
    root, prior_archive = initialize_repo_with_prior_link(
        tmp_path,
        base_status="Implemented",
    )
    unrelated_archive = archive_rel("unrelated-round")
    write_archive(
        root,
        scope="unrelated-round",
        body="# Unrelated archived plan\n",
    )
    metadata = write_plan(
        root,
        status="Implemented",
        scope="current-round",
        previous_archive=unrelated_archive,
    )
    commit_all(root, f"replace backlink {prior_archive} with unrelated archive")

    errors = validate_changed_plan(root, metadata)

    assert [error.message for error in errors] == [FIDELITY_ERROR]


def test_superseding_draft_and_replacing_body_requires_previous_archive(
    tmp_path: Path,
) -> None:
    root = initialize_repo(tmp_path, base_status="Draft")
    run_git(root, "switch", "main")
    write_archive(root, status="Superseded", body="# Fixture plan\n")
    commit_all(root, "archive draft before replacement")
    run_git(root, "switch", "-C", "fixture-change")
    metadata = write_plan(
        root,
        status="Pending Confirmation",
        scope="replacement-round",
        body="# Replacement plan\n",
    )
    commit_all(root, "supersede draft and add replacement")

    errors = validate_changed_plan(root, metadata)

    assert [error.message for error in errors] == [REQUIRED_BACKLINK_ERROR]


def test_previously_archived_draft_base_requires_back_link_when_body_changes(
    tmp_path: Path,
) -> None:
    root = initialize_repo(tmp_path, base_status="Draft")
    run_git(root, "switch", "main")
    write_archive(
        root,
        scope="previously-settled-draft",
        status="Superseded",
        body="# Fixture plan\n",
    )
    commit_all(root, "archive draft in an earlier change")
    run_git(root, "switch", "-C", "fixture-change")
    metadata = write_plan(
        root,
        status="Pending Confirmation",
        scope="replacement-round",
        body="# Replacement plan\n",
    )
    commit_all(root, "replace previously archived draft")

    errors = validate_changed_plan(root, metadata)

    assert [error.message for error in errors] == [REQUIRED_BACKLINK_ERROR]


def test_rewriting_previously_archived_draft_and_archive_cannot_bypass_back_link(
    tmp_path: Path,
) -> None:
    root = initialize_repo(tmp_path, base_status="Draft")
    run_git(root, "switch", "main")
    archive_scope = "previously-settled-draft"
    original_body = "# Original settled plan\n"
    write_plan(
        root,
        status="Draft",
        scope=archive_scope,
        body=original_body,
    )
    write_archive(
        root,
        scope=archive_scope,
        status="Superseded",
        body=original_body,
    )
    commit_all(root, "archive draft before the feature change")
    run_git(root, "switch", "-C", "fixture-change")

    forged_body = "# Forged replacement plan\n"
    write_archive(
        root,
        scope=archive_scope,
        status="Superseded",
        body=forged_body,
    )
    metadata = write_plan(
        root,
        status="Draft",
        scope=archive_scope,
        body=forged_body,
    )
    commit_all(root, "rewrite active plan and its historical archive")

    errors = validate_changed_plan(root, metadata)

    assert [error.message for error in errors] == [REQUIRED_BACKLINK_ERROR]


def test_faithful_archive_does_not_allow_unrelated_active_body_rewrite(
    tmp_path: Path,
) -> None:
    root = initialize_repo(tmp_path, base_status="Draft")
    run_git(root, "switch", "main")
    write_archive(root, status="Superseded", body="# Fixture plan\n")
    commit_all(root, "archive draft before unrelated rewrite")
    run_git(root, "switch", "-C", "fixture-change")
    metadata = write_plan(
        root,
        status="Draft",
        scope="completed-round",
        body="# Unrelated replacement plan\n",
    )
    commit_all(root, "rewrite active body beside faithful archive")

    errors = validate_changed_plan(root, metadata)

    assert [error.message for error in errors] == [REQUIRED_BACKLINK_ERROR]


def test_draft_continuation_matching_unrelated_archive_body_remains_unsettled(
    tmp_path: Path,
) -> None:
    root = initialize_repo(tmp_path, base_status="Draft")
    coincidental_body = "# Coincidental next-round body\n"
    write_archive(
        root,
        scope="unrelated-history",
        body=coincidental_body,
    )
    metadata = write_plan(
        root,
        status="Pending Confirmation",
        body=coincidental_body,
    )
    commit_all(root, "continue draft with body matching unrelated history")

    assert validate_changed_plan(root, metadata) == []


def test_faithful_archive_with_extended_active_body_still_requires_back_link(
    tmp_path: Path,
) -> None:
    root = initialize_repo(tmp_path, base_status="Draft")
    run_git(root, "switch", "main")
    write_archive(root, status="Superseded", body="# Fixture plan\n")
    commit_all(root, "archive draft before closeout extension")
    run_git(root, "switch", "-C", "fixture-change")
    metadata = write_plan(
        root,
        status="Draft",
        scope="completed-round",
        body="# Fixture plan\n\n## Closeout\n\nThis round was superseded.\n",
    )
    commit_all(root, "supersede draft with closeout note")

    errors = validate_changed_plan(root, metadata)

    assert [error.message for error in errors] == [REQUIRED_BACKLINK_ERROR]


@pytest.mark.parametrize(
    "source_archive_rel",
    [
        (
            "docs/engineer/agents/qa-agent/e2e-case-memory/"
            "implementation-plans/archive/IMPLEMENTATION_PLAN-e2e-case-memory.md"
        ),
        (
            "docs/engineer/agents/pm-agent/skills/changelog-generator/"
            "implementation-plans/archive/"
            "IMPLEMENTATION_PLAN-changelog-generator-docs-test-ci-semantics.md"
        ),
    ],
)
def test_backfilled_real_archive_body_settles_matching_draft_base(
    tmp_path: Path,
    source_archive_rel: str,
) -> None:
    source_archive = Path(__file__).parents[1] / source_archive_rel
    source_body = contract.parsed_markdown_body(source_archive)
    assert source_body is not None

    root = initialize_repo(tmp_path, base_status="Draft")
    run_git(root, "switch", "main")
    write_plan(
        root,
        status="Draft",
        scope="backfilled-history",
        body=source_body,
    )
    write_archive(
        root,
        scope="backfilled-history",
        body=source_body,
    )
    commit_all(root, f"backfill archive from {source_archive.name}")
    run_git(root, "switch", "-C", "fixture-change")
    metadata = write_plan(
        root,
        status="Pending Confirmation",
        scope="next-round",
        body="# Replacement plan\n",
    )
    commit_all(root, "replace draft backed by real historical archive body")

    errors = validate_changed_plan(root, metadata)

    assert [error.message for error in errors] == [REQUIRED_BACKLINK_ERROR]


def test_matching_rewritten_active_and_archive_bodies_cannot_bypass_back_link(
    tmp_path: Path,
) -> None:
    root = initialize_repo(tmp_path, base_status="Implemented")
    forged_body = "# Forged replacement plan\n"
    write_archive(root, body=forged_body)
    metadata = write_plan(
        root,
        status="Implemented",
        scope="completed-round",
        body=forged_body,
    )
    commit_all(root, "rewrite active plan and archive with matching new body")

    errors = validate_changed_plan(root, metadata)

    assert [error.message for error in errors] == [REQUIRED_BACKLINK_ERROR]


def test_missing_base_ref_does_not_add_archive_linkage_error(tmp_path: Path) -> None:
    root = tmp_path / "repo"
    root.mkdir()
    run_git(root, "init", "-b", "fixture-change")
    run_git(root, "config", "user.email", "fixture@example.com")
    run_git(root, "config", "user.name", "Fixture User")
    metadata = write_plan(root, status="Pending Confirmation")
    commit_all(root, "add plan without main ref")
    assert contract.implementation_plan_base_ref(root) is None
    parsed = contract.parse_markdown_frontmatter(
        root / PLAN_REL,
        (root / PLAN_REL).read_text(encoding="utf-8"),
        errors=None,
    )
    assert parsed is not None

    errors: list[contract.ContractError] = []
    contract.validate_active_plan_archive_linkage(
        root,
        PLAN_REL,
        FEATURE_PATH,
        metadata,
        parsed[1],
        None,
        True,
        errors,
    )

    assert errors == []


def test_archive_files_at_ref_returns_empty_for_missing_tree_or_invalid_ref(
    tmp_path: Path,
) -> None:
    root = initialize_repo(tmp_path, base_status="Draft")

    assert contract.archive_files_at_ref(root, "main", "missing-feature") == []
    assert contract.archive_files_at_ref(root, "missing-ref", FEATURE_PATH) == []


def test_invalid_base_plan_frontmatter_blocks_archive_linkage_validation(
    tmp_path: Path,
) -> None:
    root = initialize_repo(tmp_path, base_status="Draft")
    run_git(root, "switch", "main")
    (root / PLAN_REL).write_text("# Base plan without frontmatter\n", encoding="utf-8")
    commit_all(root, "make base plan frontmatter invalid")
    run_git(root, "switch", "-C", "fixture-change")
    metadata = write_plan(root, status="Pending Confirmation")
    commit_all(root, "replace invalid base plan")

    errors = validate_changed_plan(root, metadata)

    assert [error.message for error in errors] == [
        "cannot validate active plan archive linkage because the base plan "
        "frontmatter is invalid"
    ]


def test_previous_archive_path_must_be_a_file(tmp_path: Path) -> None:
    root = initialize_repo(tmp_path, base_status="Implemented")
    (root / ARCHIVE_REL).mkdir(parents=True)
    metadata = write_plan(
        root,
        status="Pending Confirmation",
        previous_archive=ARCHIVE_REL,
    )
    commit_all(root, "link replacement to archive directory")

    errors = validate_changed_plan(root, metadata)

    assert [error.message for error in errors] == [
        "frontmatter 'previous_plan_archive' must point to an existing archive file"
    ]


def test_previous_archive_without_frontmatter_reports_fidelity_error(
    tmp_path: Path,
) -> None:
    root = initialize_repo(tmp_path, base_status="Implemented")
    archive_path = root / ARCHIVE_REL
    archive_path.parent.mkdir(parents=True)
    archive_path.write_text("", encoding="utf-8")
    metadata = write_plan(
        root,
        status="Pending Confirmation",
        previous_archive=ARCHIVE_REL,
        body="# Replacement plan\n",
    )
    commit_all(root, "link replacement to empty archive")

    errors = validate_changed_plan(root, metadata)

    assert [error.message for error in errors] == [FIDELITY_ERROR]


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
