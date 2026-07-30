# Eval Result: eval-002-boundary-test-generation

## Evaluation Target

- Skill: `spec-based-tester`
- Eval: `eval-002-boundary-test-generation`
- Prompt target: 对登录表单边界做同路径门禁后的结构化验证。

## Test Set / Fixture Version

- Eval schema: `evals.json` v1.0
- Fixture version: repository commit `cdfc879`
- Fresh run: `2026-07-30 20:02:13 +0800`
- Runtime directory: `tmp/eval-runs/issue-196-pr-b-spec-20260730-200213-eval002/qa/agents/qa/test/spec-based-tester/evals/workspace/eval-2-boundary-test-generation/`
- `eval_metadata.json` 未声明 `execution_cleanup`。

## Latest Result

- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
- `assertion_3` 为 **NOT EXERCISED**：缺 confirmed `IMPLEMENTATION_PLAN.md` 已合法阻塞实际边界执行，不能要求候选越过门禁实跑。

Overall result: FAIL

## Assertion Results

- PASS `assertion_1`: preflight 记录范围、五类输入约束、环境假设、缺 plan、缺 URL 和未执行状态。
- PASS `assertion_2`: 明确先读 suite、flow、case、script，并记录没有历史 `results/` 或 `_reports/` 证据。
- NOT EXERCISED `assertion_3`: 实施计划门禁阻止实际边界执行；候选正确把五类边界保留为 `assumed`。
- PASS `assertion_4`: 每项使用 `assumed` 或 `blocked`，并提供可追踪 evidence references。
- PASS `assertion_5`: 包含 requirement matrix、execution path、evidence references、risk notes 和 handoff decision。
- PASS `assertion_6`: 没有把 assumed/blocked 项当成缺陷，且列出未覆盖风险。
- FAIL `alignment_plan_gate`: 正确发现缺 `IMPLEMENTATION_PLAN.md` 并标记 blocked，但没有把 next owner 指向 `engineer-agent:feature-implementor`；后续建议反而先补 `QA_BASE_URL` 并执行 harness，遗漏必须先补齐 plan 的恢复顺序。

## With-Skill Behavior

候选正确执行了文档与 QA memory preflight，也没有伪造边界结果。核心回归仍是实施计划门禁的 handoff 不完整：识别 blocker 后没有交还权威 owner，且恢复步骤顺序错误。

## Fresh Without-Skill Baseline

同一 prompt/fixture 的全新 baseline 已生成，未读取或应用 skill 与 QA README。candidate 和 fresh judge 均成功；baseline 完全没有识别缺失的 `IMPLEMENTATION_PLAN.md`，只以测试环境和 `QA_BASE_URL` 为 blocker，因而同样不满足 `alignment_plan_gate`，semantic verdict 为 FAIL。

## Failures

- 缺 plan 后没有交还 `engineer-agent:feature-implementor`，恢复步骤错误。

## Next Steps

- 先补齐并确认同路径 `IMPLEMENTATION_PLAN.md`，再恢复 repo harness 或浏览器验证。

## Runtime Artifact Policy

- 两条 candidate、两条 fresh judge verdict、diagnostics 与 `comparison.auto.md` 均在上述 `tmp/eval-runs/`；所有 Codex 调用返回码为 0，且无 timeout。
- Runtime 不提交；durable 结果仅为本文件。
