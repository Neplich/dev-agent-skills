# Eval Result: eval-003-third-party

## Evaluation Target

- Agent: `security`
- Skill: `privacy-surface-mapper`
- Eval: `eval-003-third-party`
- Test case: Third-Party Data Sharing
- Workspace: `workspace/eval-003-third-party`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-06-02

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Test mapping of third-party data sharing
- Expected output: Structured privacy surface map that identifies personal data, processing purpose, third-party sharing, user-rights gaps, and compliance risks.

## Assertions

- `data_inventory`: 识别个人数据类型、收集入口和处理目的
- `sharing_and_retention`: 识别第三方共享、存储或保留相关风险
- `user_rights`: 检查访问、删除、导出或同意等用户权利支持情况
- `compliance_gaps`: 给出隐私合规缺口和改进建议

## With Skill

Observed behavior:

- 当前 skill 覆盖 third-party data sharing、共享目的、legal basis、cross-border transfer、retention 和用户权利检查，满足第三方数据共享场景断言。

## Without Skill / Baseline

- Baseline behavior is diagnostic only.
- This comparison records whether the skill-specific protocol, routing, evidence, or artifact expectations are preserved.

## Failures

- None found in fresh Codex subagent validation.

## Next Steps

- 无需修改当前 skill 指令。

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be committed.
