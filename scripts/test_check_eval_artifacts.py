import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts import check_eval_artifacts


def test_new_runtime_directories_are_blocked_in_agent_test_trees() -> None:
    for path in (
        "agents/qa/test/example/snapshots/files.json",
        "agents/qa/test/example/preflight/result.json",
        "agents/qa/test/example/judge/package.json",
        "agents/qa/test/example/judge-package.json",
        "agents/qa/test/example/workspace-snapshot.json",
    ):
        assert check_eval_artifacts.is_runtime_artifact(path), path


def test_runtime_names_remain_allowed_in_skill_business_assets() -> None:
    assert not check_eval_artifacts.is_runtime_artifact(
        "agents/qa/skills/example/references/snapshots/README.md"
    )
