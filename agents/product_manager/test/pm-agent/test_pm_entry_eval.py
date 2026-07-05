import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
PM_AGENT_SKILL = ROOT / "agents/product_manager/skills/pm-agent/SKILL.md"
EVALS_PATH = ROOT / "agents/product_manager/test/pm-agent/evals/evals.json"


FR006_ENTRY_CASES = {
    "eval-001-route-greenfield-product-request": [
        "`new_feature`",
        "`idea-to-spec`",
        "Only point the next step to `engineer-agent` after PM requirements are stable",
    ],
    "eval-002-route-bugfix-request": [
        "`bug_report`",
        "approved PRD / TRD expectations",
        "Engineer / debugger",
    ],
    "eval-003-route-test-writing-request": [
        "`validation`",
        "Confirm the test basis",
        "QA / test-writer",
    ],
    "eval-004-route-ui-update-request": [
        "`design`",
        "`existing_update`",
        "Design artifacts go to Designer",
        "frontend implementation waits",
    ],
    "eval-005-route-deployment-request": [
        "`deployment`",
        "DevOps receives",
        "Confirmed non-feature repo-wide downstream handoffs",
    ],
    "eval-006-route-security-request": [
        "`security`",
        "Security receives",
        "risk surface",
    ],
}


def load_evals():
    return {
        item["id"]: item
        for item in json.loads(EVALS_PATH.read_text())["evals"]
    }


def assert_contains_all(haystack: str, needles: list[str]) -> None:
    normalized = haystack.lower()
    missing = [needle for needle in needles if needle.lower() not in normalized]
    assert missing == []


def test_fr006_pm_entry_scenarios_1_to_6_are_defined():
    evals = load_evals()

    assert set(FR006_ENTRY_CASES).issubset(evals)

    for eval_id in FR006_ENTRY_CASES:
        item = evals[eval_id]
        workspace = EVALS_PATH.parent / item["workspace"]
        assert (workspace / "README.md").exists()
        assert (workspace / "eval_metadata.json").exists()
        comparison = workspace / "comparison.md"
        assert comparison.exists()
        comparison_text = comparison.read_text()
        assert "Latest result:" in comparison_text
        assert "Runtime Artifacts Policy" in comparison_text
        assert item["assertions"]


def test_pm_agent_protocol_covers_fr006_entry_routes():
    skill_text = PM_AGENT_SKILL.read_text()

    assert "Treat `pm-agent` as the first stop" in skill_text
    assert "Classify the request before selecting a downstream PM skill or role agent" in skill_text

    for required_terms in FR006_ENTRY_CASES.values():
        assert_contains_all(skill_text, required_terms)
