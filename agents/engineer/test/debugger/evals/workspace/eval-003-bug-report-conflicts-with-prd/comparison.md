# Eval Result: eval-003-bug-report-conflicts-with-prd

## Evaluation Target

- Agent: `engineer`
- Skill: `debugger`
- Eval: `eval-003-bug-report-conflicts-with-prd`
- Test case: bug-report-conflicts-with-prd
- Workspace: `workspace/eval-003-bug-report-conflicts-with-prd`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-06-02

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Verifies that debugger hands off to PM when a reported bug is actually a request to change approved PRD/TRD behavior.
- Expected output: 识别用户期望与 PRD/TRD 冲突，停止修复路径，交回 pm-agent:idea-to-spec existing-project-update 更新 PRD 或产品决策记录并同步 TRD，不产出修复计划或代码改动。

## Assertions

- `detects_prd_conflict`: 识别 PRD 冲突
- `hands_off_to_pm_update`: 交回 PM 更新
- `does_not_produce_repair_plan`: 不进入修复计划
- `allows_explicit_skip_only`: 只有显式跳过才能继续

## With Skill

Observed behavior:

- 当前 SKILL.md 要先按 PRD/TRD 对齐预期；若用户请求与已批准 PRD/TRD 冲突，停止修复并交回 pm-agent:idea-to-spec existing-project-update，同步 TRD 后再继续。

## Without Skill / Baseline

- Baseline behavior is diagnostic only.
- This comparison records whether the skill-specific protocol, routing, evidence, or artifact expectations are preserved.

## Failures

- None found in fresh Codex subagent validation.

## Next Steps

- 保持该 eval 覆盖 bug report 与 PRD/TRD 冲突时的 PM handoff。

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be committed.
