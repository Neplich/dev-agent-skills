# Eval Result: eval-001-route-mixed-qa-request

## Evaluation Target

- Agent: `qa`
- Skill: `qa-agent`
- Eval: `eval-001-route-mixed-qa-request`
- Test case: route-mixed-qa-request
- Workspace: `workspace/eval-1-route-mixed-qa-request`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-06-04

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Verifies that qa-agent handles route-mixed-qa-request and produces the expected role-specific artifact.
- Expected output: QA 路由决策，明确选择最窄的下游 QA skill、选择理由、需要读取的上下文和预期 evidence artifact

## Assertions

- `assertion_1`: 路由选择
- `assertion_2`: 上下文传递
- `qa`: QA 用例记忆
- `e2e_execution_protocol`: E2E 执行协议
- `credential_and_report_refs`: 账号与报告 reference
- `alignment_and_plan_gate`: PRD/TRD 与实施计划门禁
- `assertion_4`: 结构化产物
- `assertion_5`: 边界控制

## With Skill

Observed behavior:

- PASS - fresh Codex subagent validation completed on 2026-06-04.
- `qa-agent` requires routing before execution and selecting one narrow downstream QA skill. For this fixture, the main route is `spec-based-tester` because PM asks whether the implemented login refresh can enter documented acceptance. The intermittent CI failure remains a risk note or potential `bug-analyzer` follow-up, not a confirmed bug and not a second simultaneously executed route.
- The skill requires carrying PM/spec context, implementation changes, CI failure information, environment notes, and test commands into the downstream route. The fixture provides `docs/pm/login-refresh/PRD.md`, `docs/engineer/login-refresh/TRD.md`, `implementation/changes.md`, `ci/login-intermittent-failure.log`, and the TRD command/environment constraints, including not assuming a fixed localhost port.
- The E2E protocol is satisfied: the skill uses `docs/qa/e2e/{feature_path}/` with `TEST_SUITE.md`, `FLOW_INDEX.md`, `cases/`, `scripts/`, prior `results/`, and `_reports/`; it requires `feature-update` or `release`, blocks missing platform version instead of using `unknown`, selects execution by repo harness > Chrome plugin / browser connector > Playwright fallback, and runs E2E TC through subagents by default.
- Credential and report references are covered by explicit links to `agents/qa/skills/qa-agent/references/e2e-credential-store.md` and `agents/qa/skills/qa-agent/references/e2e-test-report.md`. The skill requires local `.qa/e2e/accounts.local.json` storage and committed docs referencing account IDs only.
- The PRD/TRD and plan gate is covered for this existing-feature change: the skill requires same-`feature_path` PRD/TRD expectation alignment and a confirmed `docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md` before creating, updating, or executing acceptance TC. If alignment, environment, credentials, feature path, or the implementation plan are missing, the output must report `blocked` and the next owner.
- The expected artifact shape is explicit: route decision, execution path, evidence artifact, E2E scenario/scope/version status, subagent plan, selected execution entry, evidence references, risk notes, and blocker or handoff notes.

## Without Skill / Baseline

- Baseline behavior is diagnostic only.
- This comparison records whether the skill-specific protocol, routing, evidence, or artifact expectations are preserved.

## Failures

- None.

## Next Steps

- No skill or fixture change is required for this eval.

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be committed.
