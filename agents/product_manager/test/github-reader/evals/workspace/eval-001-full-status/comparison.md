# Eval Result: eval-001-full-status

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-reader`
- Eval: `eval-001-full-status`
- Test case: full-status
- Workspace: `workspace/eval-001-full-status`
- Latest result: PARTIAL - prior skill validation evidence is preserved; without_skill baseline was not generated for this historical comparison.
- Prior validation note: canonical comparison migration retained current-version result on 2026-06-02

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Verifies that github-reader handles full-status and produces the expected role-specific artifact.
- Expected output: 结构化的项目状态报告，包含 Milestone 进度表、Open Issues 分组、PR 队列（待 review / 草稿 / 近期合并），以及健康摘要

## Assertions

- `milestone`: 包含 Milestone 表格
- `pr`: 包含 PR 队列
- `assertion_3`: 包含健康摘要
- `pr_2`: PR 链接格式正确

## With Skill

Observed behavior:

- 保留并迁移 iteration-2 最新 comparison。该结果已基于当前 github-reader skill 版本，覆盖 full-status 输出中的 milestones、open issues、PR queue 和健康摘要。

## Without Skill / Baseline
- BLOCKED: No actual without_skill baseline result is recorded for this historical comparison. This file is not treated as a full eval PASS until a baseline result is generated and written here.
- This comparison records whether the skill-specific protocol, routing, evidence, or artifact expectations are preserved.

## Failures

- None recorded in the migrated current-version comparison.

## Next Steps

- 本轮未重新运行；保持 canonical workspace 下的最新 durable comparison。

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be committed.
