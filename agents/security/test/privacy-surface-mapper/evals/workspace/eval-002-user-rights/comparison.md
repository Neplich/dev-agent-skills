# Eval Result: eval-002-user-rights

## Evaluation Target

- Agent: `security`
- Skill: `privacy-surface-mapper`
- Eval: `eval-002-user-rights`
- Test case: User Rights Implementation
- Workspace: `workspace/eval-002-user-rights`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-06-02

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Test checking of user data rights implementation
- Expected output: Structured privacy surface map that identifies personal data, processing purpose, third-party sharing, user-rights gaps, and compliance risks.

## Assertions

- `data_inventory`: 识别个人数据类型、收集入口和处理目的
- `sharing_and_retention`: 识别第三方共享、存储或保留相关风险
- `user_rights`: 检查访问、删除、导出或同意等用户权利支持情况
- `compliance_gaps`: 给出隐私合规缺口和改进建议

## With Skill

Observed behavior:

- 当前 skill 明确检查 access、deletion、rectification、portability/export 等用户权利，并要求给出实现状态、合规缺口和修复建议。

## Without Skill / Baseline

- Baseline behavior is diagnostic only.
- This comparison records whether the skill-specific protocol, routing, evidence, or artifact expectations are preserved.

## Failures

- None found in fresh Codex subagent validation.

## Next Steps

- 无需修改当前 skill 指令。

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be committed.
