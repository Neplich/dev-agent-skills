# Eval Result: eval-001-gdpr

## Evaluation Target

- Agent: `security`
- Skill: `privacy-surface-mapper`
- Eval: `eval-001-gdpr`
- Test case: GDPR Compliance Check
- Workspace: `workspace/eval-001-gdpr`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-06-02

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Test privacy mapping for user data collection
- Expected output: Structured privacy surface map that identifies personal data, processing purpose, third-party sharing, user-rights gaps, and compliance risks.

## Assertions

- `data_inventory`: 识别个人数据类型、收集入口和处理目的
- `sharing_and_retention`: 识别第三方共享、存储或保留相关风险
- `user_rights`: 检查访问、删除、导出或同意等用户权利支持情况
- `compliance_gaps`: 给出隐私合规缺口和改进建议

## With Skill

Observed behavior:

- 当前 skill 要求建立个人数据清单、处理目的、legal basis、retention、用户权利和 GDPR/CCPA 缺口，覆盖所有 privacy assertions。

## Without Skill / Baseline

- Baseline behavior is diagnostic only.
- This comparison records whether the skill-specific protocol, routing, evidence, or artifact expectations are preserved.

## Failures

- None found in fresh Codex subagent validation.

## Next Steps

- 无需修改当前 skill 指令。

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be committed.
