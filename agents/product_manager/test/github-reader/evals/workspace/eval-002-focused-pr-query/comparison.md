# Eval Result: eval-002-focused-pr-query

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-reader`
- Eval: `eval-002-focused-pr-query`
- Test case: focused-pr-query
- Workspace: `workspace/eval-002-focused-pr-query`
- Latest result: PASS - canonical comparison migration retained current-version result on 2026-06-02

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Verifies that github-reader handles focused-pr-query and produces the expected role-specific artifact.
- Expected output: 聚焦 PR 的输出，列出 awaiting review 的 PR 并按等待时间排序，不需要输出 issue 和 milestone 数据

## Assertions

- `pr`: 聚焦 PR 不冗余
- `assertion_2`: 包含等待时间
- `assertion_3`: 有排序

## With Skill

Observed behavior:

- 保留并迁移 iteration-2 最新 comparison。该结果已基于当前 github-reader skill 版本，覆盖 focused PR 查询、等待时间排序和避免冗余 issue/milestone 输出。

## Without Skill / Baseline

- Baseline behavior is diagnostic only.
- This comparison records whether the skill-specific protocol, routing, evidence, or artifact expectations are preserved.

## Failures

- None recorded in the migrated current-version comparison.

## Next Steps

- 本轮未重新运行；保持 canonical workspace 下的最新 durable comparison。

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be committed.
