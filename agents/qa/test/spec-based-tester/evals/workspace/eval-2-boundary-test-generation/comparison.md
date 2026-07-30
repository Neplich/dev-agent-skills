# Eval Result: eval-002-boundary-test-generation

## Evaluation Target

- Skill: `spec-based-tester`
- Eval: `eval-002-boundary-test-generation`
- Prompt target: 对登录表单边界做同路径门禁后的结构化验证。

## Test Set / Fixture Version

- Eval schema: `evals.json` v1.0
- Fixture version: repository commit `778b042`
- Fresh run: `2026-07-30 19:26:38 +0800`
- Runtime directory: `tmp/eval-runs/issue-196-pr-b-20260730-192638/qa/agents/qa/test/spec-based-tester/evals/workspace/eval-2-boundary-test-generation/`
- `eval_metadata.json` 未声明 `execution_cleanup`。

## Latest Result

- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
- `assertion_3` 为 **NOT EXERCISED**：缺 confirmed `IMPLEMENTATION_PLAN.md` 已合法阻塞实际边界执行，不能要求候选越过门禁实跑。
- 非 E2E 路径变更检查：该 fixture 是 E2E `feature-update`，未触发 `docs/qa/{feature_path}/spec-validation.md`。

Overall result: FAIL

## Assertion Results

- PASS `assertion_1`: preflight 记录范围、输入约束、环境假设、缺 plan、缺 URL、缺历史结果等 blocker。
- PASS `assertion_2`: 先读 suite、flow、case、script，并显式记录 results/reports 缺失。
- NOT EXERCISED `assertion_3`: 计划门禁阻止实际边界执行；候选正确把五类边界保留为 assumed。
- PASS `assertion_4`: 每项使用 pass/assumed/blocked 且有 evidence reference。
- PASS `assertion_5`: 包含 requirement matrix、execution path、evidence、risk、handoff。
- PASS `assertion_6`: 不把 assumed/blocked 当 bug，列出未覆盖风险。
- FAIL `alignment_plan_gate`: 正确发现缺 `IMPLEMENTATION_PLAN.md`，但没有把 next owner 指向 `engineer-agent:feature-implementor`；下一步反而建议补 URL 后直接执行，遗漏 plan 必须先补齐的顺序。

## With-Skill Behavior

候选正确停止执行并诚实标记 assumed/blocked；核心失败是缺 plan 后的 next-owner 与恢复顺序错误。

## Fresh Without-Skill Baseline

同一 prompt/fixture 的全新 baseline 已生成，未读取 skill、QA README 或历史 baseline。candidate/verdict 均成功；baseline 完全遗漏 plan gate，semantic verdict 为 FAIL。

## Failures

- 缺 plan 没有交还 `engineer-agent:feature-implementor`，恢复步骤错误。

## Next Steps

- 先确认同路径 implementation plan，再谈 harness 或 URL 执行。

## Runtime Artifact Policy

- 两条 candidate、两条 verdict、diagnostics 与 `comparison.auto.md` 均在上述 `tmp/eval-runs/`，返回码均为 0、无 timeout。
- Runtime 不提交；durable 结果仅为本文件。
