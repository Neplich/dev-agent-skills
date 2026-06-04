# Eval Result: qa-agent-empty-qa-directory-expands-cases

## Evaluation Target

- Agent: `qa`
- Skill: `qa-agent`
- Eval: `eval-002-empty-qa-directory-expands-cases`
- Test case: empty-qa-directory-expands-cases
- Workspace: `workspace/eval-2-empty-qa-directory-expands-cases`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-06-04

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Verifies that qa-agent handles an existing but empty E2E function-tree directory by routing to targeted file exploration, durable case creation, and case-based execution when exploration is already authorized.
- Expected output: QA 路由决策与执行协议，明确空 E2E 功能树目录需要触发目标文件探索、更新 TEST_SUITE.md 和 FLOW_INDEX.md、创建独立 TC 与 script 文件，并要求后续验证基于这些用例执行

## Assertions

- `assertion_1`: 空目录识别
- `assertion_2`: 授权后主动探索
- `assertion_3`: 探索记录沉淀
- `e2e`: E2E 用例创建
- `assertion_5`: 用例驱动执行
- `version_and_subagent_gate`: 版本与 subagent 门禁
- `assertion_6`: 路由边界

## With Skill

- PASS - fresh Codex subagent validation completed on 2026-06-04.
- `qa-agent` requires downstream QA to read the target function-tree `TEST_SUITE.md`, `FLOW_INDEX.md`, `cases/*.md`, `scripts/*.spec.md`, prior `results/`, and `_reports/` before exploring. This satisfies the empty-directory assertion because the fixture path is `docs/qa/e2e/account/profile-settings/profile-form/` and no reusable TC exists there.
- Because the prompt already confirms `feature-update`, a new feature update, and authorization to explore, the skill routes the downstream worker to targeted project-file exploration rather than asking again. The relevant fixture files are `src/routes/profile-settings.md`, `src/pages/ProfileSettingsPage.tsx`, `src/components/ProfileSettingsForm.tsx`, and `environment/qa-env.md`.
- Missing coverage is handled durably: the skill requires adding or updating `cases/`, `scripts/`, and `FLOW_INDEX.md` in the same function-tree directory and avoiding duplicate synonym TC. This covers independent `cases/TC-NNN-<short-slug>.md` files and matching `scripts/TC-NNN-<short-slug>.spec.md` snippets.
- The credential rule is satisfied because the skill requires committed QA docs to reference account IDs only and to follow `e2e-credential-store.md` for `.qa/e2e/accounts.local.json`; this matches the fixture credential ref `platform.profile-settings.qa_user` and forbids plaintext secrets in TC, scripts, results, or reports.
- The execution protocol is satisfied: `feature-update` covers the changed feature and direct impact paths only, execution entry order is repo harness > Chrome plugin / browser connector > Playwright fallback, and every E2E TC is executed through a subagent by default while the main agent owns scope confirmation and the final report.
- The platform version gate is satisfied. The fixture explicitly marks platform version missing, and the skill requires `blocked` until the version is provided, never `unknown`; final reporting must follow `e2e-test-report.md` at the feature `_reports/{platform-version}/test-reports-{test-time}.md` path once execution is unblocked.
- The route boundary is satisfied because the skill selects one narrow QA route and keeps QA focused on evidence, case creation, execution protocol, blockers, and handoff instead of implementing fixes.

## Baseline

- Often skips durable test-case memory or creates a one-off checklist.
- Less consistently writes reusable case files before execution.
- Does not consistently name the Chrome plugin / browser connector execution
  path when browser E2E validation is required.

## Failures

- None.

## Next Steps

- No skill or fixture change is required for this eval.

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be committed.
