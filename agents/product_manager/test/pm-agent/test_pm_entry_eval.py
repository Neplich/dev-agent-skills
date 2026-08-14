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
    ROOT / "agents/docs/skills/docs-agent/SKILL.md",
]
SPECIALIST_GATE_SKILLS = [
    ROOT / "agents/engineer/skills/feature-implementor/SKILL.md",
    ROOT / "agents/engineer/skills/debugger/SKILL.md",
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
        "不得绕过",
        "pm-agent",
    ],
}
MISSING_TARGET_CASES = {
    "eval-009-missing-handoff-target-unavailable": [
        "not installed",
        "blocked",
        "不代行",
    ],
}
CHANGE_TIER_CASES = {
    "eval-010-change-tier-hotfix-fast-lane": [
        "`hotfix`",
        "fast lane",
        "verification evidence",
    ],
    "eval-011-change-tier-standard-full-gate": [
        "`standard`",
        "PRD/TRD",
        "而不是 `hotfix`",
    ],
    "eval-012-change-tier-hotfix-abuse-blocked": [
        "`hotfix`",
        "expectation change",
        "`standard`",
    ],
    "eval-013-change-tier-hotfix-e2e-direct-path": [
        "hotfix",
        "directly affected path",
        "QA",
    ],
}
READ_ONLY_DIAGNOSIS_CASE = "eval-020-route-read-only-diagnosis"
INTENT_ENTRY_CASES = {
    "eval-017-scope-guard-unenabled-general",
    "eval-018-scope-guard-explicit-invocation",
    "eval-019-scope-guard-enabled-general",
    "eval-021-explicit-downstream-specialist",
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
        assert workspace.is_dir()
        assert (workspace / "eval_metadata.json").exists()
        comparison = workspace / "comparison.md"
        assert comparison.exists()
        comparison_text = comparison.read_text()
        assert "Overall result:" in comparison_text
        assert set(item["scenario"]) == {
            "persona", "situation", "trigger", "goal", "materials",
            "constraints", "success_criteria",
        }
        assert item["assertions"]


def test_fr006_pm_entry_scenarios_1_to_6_are_defined():
    assert_eval_workspaces_exist(set(FR006_ENTRY_CASES))


def test_fr006_pm_entry_scenarios_7_to_8_are_defined():
    assert_eval_workspaces_exist(set(FR006_GATE_DEFENSE_CASES))


def test_missing_handoff_target_eval_is_defined():
    assert_eval_workspaces_exist(set(MISSING_TARGET_CASES))


def test_change_tier_contract_evals_are_defined():
    assert_eval_workspaces_exist(set(CHANGE_TIER_CASES))


def test_read_only_diagnosis_eval_is_defined():
    assert_eval_workspaces_exist({READ_ONLY_DIAGNOSIS_CASE})


def test_intent_entry_evals_are_defined():
    assert_eval_workspaces_exist(INTENT_ENTRY_CASES)


def test_pm_entry_uses_explicit_invocation_then_rd_intent():
    skill_text = PM_AGENT_SKILL.read_text()

    assert_contains_all(
        skill_text,
        [
            "If the user explicitly names `pm-agent`, a role agent, or a skill",
            "Otherwise, determine whether the request expresses product or engineering",
            "leave it to the current assistant without PM",
            "absence does not decide automatic entry",
        ],
    )

    frontmatter_description = skill_text.split('description: "', 1)[1].split('"', 1)[0]
    assert "Use when the user explicitly names pm-agent" in frontmatter_description
    assert "Do not activate when the user explicitly names a different role agent or skill" in frontmatter_description


def test_router_skills_do_not_require_user_visible_routing_process():
    forbidden = [
        "## Mandatory Routing Decision",
        "one-line routing statement",
        "Make the decision observable",
        "Emit one compact `Routing decision` block",
    ]

    for path in [PM_AGENT_SKILL, *ROLE_ROUTER_SKILLS]:
        skill_text = path.read_text()
        for phrase in forbidden:
            assert phrase not in skill_text


def test_pm_agent_protocol_covers_fr006_entry_routes():
    skill_text = PM_AGENT_SKILL.read_text()

    assert "treat `pm-agent` as the first stop" in skill_text
    assert "Classify the request before selecting a downstream PM skill or role agent" in skill_text

    for required_terms in FR006_ENTRY_CASES.values():
        assert_contains_all(skill_text, required_terms)


def test_pm_agent_protocol_covers_missing_targets_and_change_tier():
    skill_text = PM_AGENT_SKILL.read_text()

    assert_contains_all(
        skill_text,
        [
            "If a handoff target skill or agent is not installed or unavailable",
            "mark that handoff stage as blocked",
            "do not perform the missing agent's responsibilities",
        ],
    )
    assert_contains_all(
        skill_text,
        [
            "assess `change_tier`",
            "`hotfix`",
            "`standard`",
            "`major`",
            "`hotfix` plus `delivery` / `status` requests may use the fast lane",
            "Do not route them to downstream execution as `hotfix`",
        ],
    )


def test_pm_agent_only_assigns_diagnosis_mode_for_explicit_read_only_intent():
    skill_text = PM_AGENT_SKILL.read_text()
    section = skill_text.split("For `bug_report`, add the diagnosis-only", 1)[1]
    section = section.split("## Default Routes", 1)[0]

    assert_contains_all(
        section,
        [
            "explicitly says the investigation must be read-only",
            "mode: diagnosis_only",
            "allowed_mutations: none",
            "must not be assigned `diagnosis_only` automatically",
        ],
    )
    assert_contains_all(section, ["查一下", "为什么挂了"])

    handoff_section = skill_text.split(
        "For an explicit read-only `bug_report`, also carry", 1
    )[1]
    handoff_section = handoff_section.split(
        "If a required field is unresolved", 1
    )[0]
    assert_contains_all(
        handoff_section,
        [
            "code, tests, E2E assets, configuration, databases, external state",
            "commits",
            "pushes",
            "pull requests",
        ],
    )


def test_eval_definitions_cover_gate_defense_language():
    evals = load_evals()

    for eval_id, required_terms in FR006_GATE_DEFENSE_CASES.items():
        item_text = json.dumps(evals[eval_id], ensure_ascii=False)
        assert_contains_all(item_text, required_terms)


def test_eval_definitions_cover_missing_targets_and_change_tier():
    evals = load_evals()

    for eval_id, required_terms in {
        **MISSING_TARGET_CASES,
        **CHANGE_TIER_CASES,
    }.items():
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


def test_engineer_router_preserves_specialist_specific_entry_basis():
    skill_text = (ROOT / "agents/engineer/skills/engineer-agent/SKILL.md").read_text()

    assert_contains_all(
        skill_text,
        [
            "`trd-gen` may proceed from confirmed PM documents",
            "before an Engineer TRD exists",
            "`feature-implementor`",
            "requires same-path PRD, TRD",
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
