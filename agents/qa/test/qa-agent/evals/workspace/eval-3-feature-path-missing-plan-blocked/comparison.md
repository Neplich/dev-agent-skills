# Eval Result: eval-003-feature-path-missing-plan-blocked

## Evaluation Target

- Skill: `qa-agent`
- Eval: `eval-003-feature-path-missing-plan-blocked`
- Prompt target: 识别同路径上下文与缺 implementation plan blocker。

## Test Set / Fixture Version

- Eval schema: `evals.json` v1.0
- Fixture version: repository commit `c664869`
- Fresh run: `2026-07-31 08:22:36 +0800`
- Runtime directory: `tmp/eval-runs/issue-196-l2-3-4/qa-agent/eval-003-feature-path-missing-plan-blocked/`
- `eval_metadata.json` 未声明 `execution_cleanup`。

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL**
- 所有 assertion 场景均已触发；无 `NOT EXERCISED` assertion。
- router 单表契约已触发：with-skill 依据含「信号示例」列的 `Default Routes` 单表选择主 route；未要求或伪造独立信号列表。

Overall result: PASS

## Assertion Results

- PASS `reads_same_feature_path`: 正确保留 `account/profile/preferences` 及同路径 PRD/TRD/QA 功能树。
- PASS `specialist_gate_pointer`: 声明 `spec-based-tester` 的 E2E memory、platform version、credential、execution entry、PRD/TRD/implementation plan 与 blocked-condition 权威门禁适用；没有复述缺计划后的协议。
- PASS `keeps_single_route`: 选择单一 `spec-based-tester` route，未进入实现修复。

## With-Skill Behavior

候选从单张路由表选择 `spec-based-tester`，把 `account/profile/preferences` 及同路径文档完整传递，并识别当前缺少 implementation plan 的门禁结论；它没有复述缺计划后的交接或执行协议。

## Fresh Without-Skill Baseline

本轮 baseline 使用同一 prompt 与 fixture 新生成，未读取或应用 skill、QA README、with-skill 候选或旧 comparison，也未复用历史 baseline。它识别 feature path 和缺失 plan，但没有命名 repo specialist 或声明权威门禁指针，并自行展开 Engineer 补计划和后续 E2E 用例执行步骤。

## Failures

- 无 with-skill assertion 失败。

## Next Steps

- 保持单表路由，只选择 route、传递同路径上下文并声明权威指针；具体后续协议由 specialist 执行。

## Runtime Artifact Policy

- 新生成的 with-skill / without-skill candidate 与 verdict 均在上述 `tmp/eval-runs/` 目录。
- Runtime 产物不提交；durable 结果仅为本文件。
