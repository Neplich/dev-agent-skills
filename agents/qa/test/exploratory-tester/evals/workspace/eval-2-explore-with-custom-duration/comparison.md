# Eval Result: eval-002-explore-with-custom-duration

## Evaluation Target

- Agent: `qa`
- Skill: `exploratory-tester`
- Eval: `eval-002-explore-with-custom-duration`
- Test case: explore-with-custom-duration
- Workspace: `workspace/eval-2-explore-with-custom-duration`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-06-02

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Verifies that exploratory-tester handles explore-with-custom-duration and produces the expected role-specific artifact.
- Expected output: 5 分钟探索测试报告

## Assertions

- `assertion_1`: 上下文驱动范围
- `assertion_2`: 独立探索确认
- `assertion_3`: 异常分层
- `assertion_4`: 证据输出
- `assertion_5`: 风险交接

## With Skill

Observed behavior:

- 当前 skill 要求 timebox 来自上下文，独立 E2E/探索前复用 docs/qa 记忆并在需要扩充时沉淀 FILE_EXPLORATION.md 和独立用例文件；fixture 明确目标 URL、5 分钟 timebox、SettingsPanel/EmailPreferenceForm/toast 风险，支持按 changed surface、相邻风险、confirmed issue/unconfirmed signal/uncovered area 分层输出。

## Without Skill / Baseline

- Baseline behavior is diagnostic only.
- This comparison records whether the skill-specific protocol, routing, evidence, or artifact expectations are preserved.

## Failures

- None found in fresh Codex subagent validation.

## Next Steps

- 保持该 eval 覆盖用户指定时长和证据分层行为。

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be committed.
