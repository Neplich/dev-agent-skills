# Eval Result: eval-005-existing-behavior-change-needs-pm

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-005-existing-behavior-change-needs-pm`
- Test case: existing-behavior-change-needs-pm
- Workspace: `workspace/eval-005-existing-behavior-change-needs-pm`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-06-04

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Verifies that feature-implementor stops before implementation planning when a small existing-feature change would alter approved PRD/TRD behavior or an existing product decision.
- Expected output: 识别这是改变已批准预期，停止创建 IMPLEMENTATION_PLAN.md，交回 pm-agent:idea-to-spec existing-project-update 更新 PRD 或产品决策记录，再同步 TRD。
- Validation input: current `SKILL.md`, Engineer README, `evals.json`, workspace metadata, and this comparison.

## Assertions

- `checks_approved_behavior`: 检查已批准预期
- `stops_before_implementation_plan`: 停止实施计划
- `hands_off_to_pm_existing_update`: 交回 PM existing-project-update
- `blocks_e2e_expected_behavior_change`: 预期未对齐时阻断 E2E
- `does_not_implement_directly`: 不得直接实施

## With Skill

Observed behavior:

- PASS - fresh Codex subagent validation completed on 2026-06-04.
- Current `SKILL.md` requires existing-feature behavior changes to complete the PRD alignment gate before planning, including PRD, TRD, and product decision records when present.
- If a request changes approved product behavior, the skill stops before implementation planning and hands off to `pm-agent:idea-to-spec` using the `existing-project-update` lane.
- If PRD/product decisions need updates, the skill does not create `docs/engineer/notifications/IMPLEMENTATION_PLAN.md`, does not update tests, and does not implement code just because the change is small or single-file.
- After PM alignment, stale or changed technical decisions return through TRD sync before implementation planning.
- Because QA E2E handoff is only after implementation, self-review, and a confirmed implementation plan, this skill blocks turning the unaligned archived-in-active behavior into a new E2E expected result before PRD/product decision update, TRD sync, and plan confirmation.

## Without Skill / Baseline

- Baseline behavior is diagnostic only.
- This comparison records whether the skill-specific protocol, routing, evidence, or artifact expectations are preserved.

## Failures

- None.

## Next Steps

- 保持该 eval 覆盖现有行为变更回 PM。

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be committed.
