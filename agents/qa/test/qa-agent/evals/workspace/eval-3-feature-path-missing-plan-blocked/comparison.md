# Eval Result: eval-003-feature-path-missing-plan-blocked

## Evaluation Target

- Skill: `qa-agent`
- Eval: `eval-003-feature-path-missing-plan-blocked`
- Prompt target: 识别同路径上下文与缺 implementation plan blocker。

## Test Set / Fixture Version

- Eval schema: `evals.json` v1.0
- Fixture version: repository commit `778b042`
- Fresh run: `2026-07-30 19:26:38 +0800`
- Runtime directory: `tmp/eval-runs/issue-196-pr-b-20260730-192638/qa/agents/qa/test/qa-agent/evals/workspace/eval-3-feature-path-missing-plan-blocked/`
- `eval_metadata.json` 未声明 `execution_cleanup`。

## Latest Result

- Behavior result: **FAIL**
- Coverage result: **FULL**
- 所有 assertion 场景均已触发；无 `NOT EXERCISED` assertion。
- 变更点检查：候选直接执行了 specialist 的 implementation-plan gate 并复述详细 E2E 状态，没有仅保留 specialist 门禁指针。

Overall result: FAIL

## Assertion Results

- PASS `reads_same_feature_path`: 正确保留 `account/profile/preferences` 及同路径 PRD/TRD/QA 功能树。
- PASS `blocks_missing_plan`: 缺 `IMPLEMENTATION_PLAN.md` 时 blocked，next owner 为 `engineer-agent:feature-implementor`。
- PASS `no_e2e_mutation_or_execution`: 没有创建、更新或执行验收 TC。
- PASS `keeps_single_route`: 选择单一 `spec-based-tester` route，未进入实现修复。

## With-Skill Behavior

blocked 是正确产品行为，四条 assertions 也全部满足；但 router 自己展开并裁决了 specialist 的详细 plan/E2E 门禁，与当前 `qa-agent` 只保留 gate pointer 的职责边界冲突，因此 Behavior 判 FAIL。

## Fresh Without-Skill Baseline

本轮 baseline 使用同一 prompt 与 fixture 新生成，未读取 skill、QA README 或历史 baseline。candidate/verdict 均成功；baseline 同样识别缺 plan 并 blocked，semantic verdict 为 PASS。

## Failures

- PR-B router 指针收敛未在该候选中生效；输出仍复述 specialist 门禁细节。

## Next Steps

- 后续 eval 应把“router 只选择 route、声明权威指针；specialist 再做详细门禁”设为显式 assertion。

## Runtime Artifact Policy

- 两条 candidate、两条 verdict、diagnostics 与 `comparison.auto.md` 均在上述 `tmp/eval-runs/` 目录，返回码均为 0、无 timeout。
- Runtime 产物不提交；durable 结果仅为本文件。
