# Eval Result: eval-003-feature-path-missing-plan-blocked

## Evaluation Target

- Skill: `qa-agent`
- Eval: `eval-003-feature-path-missing-plan-blocked`
- Prompt target: 识别同路径上下文与缺 implementation plan blocker。

## Test Set / Fixture Version

- Eval schema: `evals.json` v1.0
- Fixture version: repository commit `cdfc879` plus current working-tree assertion alignment
- Fresh run: `2026-07-30 19:56:24 +0800`
- Runtime directory: `tmp/eval-runs/issue-196-pr-b-qa-agent-20260730-195624/eval-003-feature-path-missing-plan-blocked/`
- `eval_metadata.json` 未声明 `execution_cleanup`。

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL**
- 所有 assertion 场景均已触发；无 `NOT EXERCISED` assertion。
- 变更点检查：with-skill 输出保留同路径上下文，只声明 specialist 权威门禁适用，没有展开缺计划后的阻塞、交接或执行协议。

Overall result: PASS

## Assertion Results

- PASS `reads_same_feature_path`: 正确保留 `account/profile/preferences` 及同路径 PRD/TRD/QA 功能树。
- PASS `specialist_gate_pointer`: 声明 `spec-based-tester` 的 E2E memory、platform version、credential、execution entry、PRD/TRD/implementation plan 与 blocked-condition 权威门禁适用；没有复述缺计划后的协议。
- PASS `keeps_single_route`: 选择单一 `spec-based-tester` route，未进入实现修复。

## With-Skill Behavior

候选把 `account/profile/preferences` 及同路径文档完整传给单一 `spec-based-tester`，并停止在 router 边界。它没有代替 specialist 裁决 implementation-plan gate，也没有复述缺计划后的交接或执行协议。

## Fresh Without-Skill Baseline

本轮 baseline 使用同一 prompt 与 fixture 新生成，未读取或应用 skill、QA README，也未复用历史 baseline。它识别 feature path 和缺失 plan，但直接裁决 blocked，并复述 Engineer 交接、平台版本、凭据、执行环境与 subagent 协议，违反当前指针断言。

## Failures

- 无 with-skill assertion 失败。

## Next Steps

- 保持 router 只选择 route、传递同路径上下文并声明权威指针；具体门禁判断由 specialist 执行。

## Runtime Artifact Policy

- 新生成的 with-skill / without-skill candidate 与 verdict 均在上述 `tmp/eval-runs/` 目录。
- Runtime 产物不提交；durable 结果仅为本文件。
