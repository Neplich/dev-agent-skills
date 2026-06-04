# Eval Result: eval-003-bug-report-conflicts-with-prd

## Evaluation Target

- Agent: `engineer`
- Skill: `debugger`
- Eval: `eval-003-bug-report-conflicts-with-prd`
- Test case: bug-report-conflicts-with-prd
- Workspace: `workspace/eval-003-bug-report-conflicts-with-prd`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-06-04

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Verifies that debugger hands off to PM when a reported bug is
  actually a request to change approved PRD/TRD behavior.
- Expected output: 识别用户期望与 PRD/TRD 冲突，停止修复路径，交回
  `pm-agent:idea-to-spec` 的 `existing-project-update` 路径更新 PRD 或产品决策记录并同步 TRD，不产出修复计划或代码改动。

## With Skill

Current `SKILL.md` satisfies all assertions:

- `detects_prd_conflict`: Step 0 requires reading approved PRD/TRD and stopping
  when the user's requested behavior conflicts with those expected-behavior
  documents.
- `hands_off_to_pm_update`: Step 0 requires handing off to
  `pm-agent:idea-to-spec` using the `existing-project-update` lane when the
  requested behavior conflicts with approved PRD/TRD.
- `blocks_e2e_when_expectation_changes`: Step 0 blocks writing the new
  expectation into `docs/qa/e2e/**` until PM updates the PRD or product decision
  record, TRD is synchronized, and a confirmed
  `docs/engineer/{feature}/IMPLEMENTATION_PLAN.md` exists.
- `does_not_produce_repair_plan`: Step 0 says to stop before repair planning
  for a PRD/TRD conflict; Core Principle and Repair Plan Gate prohibit fixing
  before the repair plan flow is confirmed.
- `allows_explicit_skip_only`: Step 0 allows continuing only when the user
  explicitly asks to skip PRD alignment, and requires recording that override.

## Without Skill / Baseline

- Baseline behavior is diagnostic only.
- This comparison records whether the skill-specific protocol, routing,
  evidence, and artifact expectations are preserved.

## Failures

- None.

## Next Steps

- None for this eval.

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be
  committed.
