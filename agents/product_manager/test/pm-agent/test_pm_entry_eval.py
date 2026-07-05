import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
PM_AGENT_SKILL = ROOT / "agents/product_manager/skills/pm-agent/SKILL.md"
EVALS_PATH = ROOT / "agents/product_manager/test/pm-agent/evals/evals.json"
ROLE_ROUTER_SKILLS = [
    ROOT / "agents/engineer/skills/engineer-agent/SKILL.md",
    ROOT / "agents/designer/skills/designer-agent/SKILL.md",
    ROOT / "agents/qa/skills/qa-agent/SKILL.md",
    ROOT / "agents/devops/skills/devops-agent/SKILL.md",
    ROOT / "agents/security/skills/security-agent/SKILL.md",
]
SPECIALIST_GATE_SKILLS = [
    ROOT / "agents/engineer/skills/feature-implementor/SKILL.md",
    ROOT / "agents/engineer/skills/debugger/SKILL.md",
    ROOT / "agents/engineer/skills/project-bootstrap/SKILL.md",
    ROOT / "agents/engineer/skills/trd-gen/SKILL.md",
    ROOT / "agents/engineer/skills/test-writer/SKILL.md",
    ROOT / "agents/engineer/skills/codebase-analyzer/SKILL.md",
    ROOT / "agents/engineer/skills/delivery/SKILL.md",
    ROOT / "agents/designer/skills/ui-ux-design/SKILL.md",
    ROOT / "agents/designer/skills/visual-design/SKILL.md",
    ROOT / "agents/qa/skills/spec-based-tester/SKILL.md",
    ROOT / "agents/qa/skills/exploratory-tester/SKILL.md",
    ROOT / "agents/qa/skills/bug-analyzer/SKILL.md",
    ROOT / "agents/qa/skills/regression-suite/SKILL.md",
    ROOT / "agents/devops/skills/deployment-planner/SKILL.md",
    ROOT / "agents/devops/skills/cicd-bootstrap/SKILL.md",
    ROOT / "agents/devops/skills/env-config-auditor/SKILL.md",
    ROOT / "agents/devops/skills/incident-playbook-writer/SKILL.md",
    ROOT / "agents/security/skills/appsec-checklist/SKILL.md",
    ROOT / "agents/security/skills/authz-reviewer/SKILL.md",
    ROOT / "agents/security/skills/dependency-risk-auditor/SKILL.md",
    ROOT / "agents/security/skills/privacy-surface-mapper/SKILL.md",
]


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
FR006_GATE_DEFENSE_CASES = {
    "eval-007-direct-downstream-without-handoff": [
        "PM handoff packet",
        "`pm-agent`",
        "downstream execution",
    ],
    "eval-008-direct-specialist-bypass-gate": [
        "PM handoff entry gate",
        "Direct invocation",
        "`pm-agent`",
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


def assert_eval_workspaces_exist(case_ids: set[str]) -> None:
    evals = load_evals()

    assert case_ids.issubset(evals)

    for eval_id in case_ids:
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


def test_fr006_pm_entry_scenarios_1_to_6_are_defined():
    assert_eval_workspaces_exist(set(FR006_ENTRY_CASES))


def test_fr006_pm_entry_scenarios_7_to_8_are_defined():
    assert_eval_workspaces_exist(set(FR006_GATE_DEFENSE_CASES))


def test_pm_agent_protocol_covers_fr006_entry_routes():
    skill_text = PM_AGENT_SKILL.read_text()

    assert "Treat `pm-agent` as the first stop" in skill_text
    assert "Classify the request before selecting a downstream PM skill or role agent" in skill_text

    for required_terms in FR006_ENTRY_CASES.values():
        assert_contains_all(skill_text, required_terms)


def test_eval_definitions_cover_gate_defense_language():
    evals = load_evals()

    for eval_id, required_terms in FR006_GATE_DEFENSE_CASES.items():
        item_text = json.dumps(evals[eval_id], ensure_ascii=False)
        assert_contains_all(item_text, required_terms)


def test_downstream_role_routers_return_direct_requests_to_pm():
    for path in ROLE_ROUTER_SKILLS:
        skill_text = path.read_text()
        assert "## PM Handoff Entry Gate" in skill_text
        assert_contains_all(
            skill_text,
            [
                "`pm-agent`",
                "handoff",
                "classification",
            ],
        )


def test_specialist_gates_block_direct_bypass():
    for path in SPECIALIST_GATE_SKILLS:
        skill_text = path.read_text()
        assert "## PM Handoff Entry Gate" in skill_text
        assert_contains_all(
            skill_text,
            [
                "`pm-agent`",
                "classification",
            ],
        )

    feature_implementor_text = (
        ROOT / "agents/engineer/skills/feature-implementor/SKILL.md"
    ).read_text()
    assert_contains_all(
        feature_implementor_text,
        [
            "Direct invocation",
            "does not bypass this gate",
        ],
    )
