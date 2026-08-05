# Eval Result: eval-002-boundary-test-generation

## Evaluation Target

- Skill: `spec-based-tester`
- Eval: `eval-002-boundary-test-generation`
- Prompt target: 对登录表单边界做同路径门禁后的结构化验证。

## Test Set / Fixture Version

- Eval schema: `evals.json` v1.0
- Fixture version: repository commit `2506764`
- Fresh run: `2026-08-03 11:20:59 +0800`
- Runtime directory: `tmp/eval-runs/issue-201-spec-based-tester/eval-002-boundary-test-generation/`
- `eval_metadata.json` 未声明 `execution_cleanup`。

## Latest Result

- Behavior result: **PASS**
- Coverage result: **PARTIAL**
- `assertion_3` 为 **NOT EXERCISED**：缺 confirmed `IMPLEMENTATION_PLAN.md` 已合法阻塞实际边界执行，不能要求候选越过门禁实跑。

Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Assertion Results

- PASS `assertion_1`: preflight 记录范围、五类输入约束、环境假设、缺 plan、缺 URL 和未执行状态。
- PASS `assertion_2`: 明确先读 suite、flow、case、script，并记录没有历史 `results/` 或 `_reports/` 证据。
- NOT EXERCISED `assertion_3`: 实施计划门禁阻止实际边界执行；候选正确把五类边界保留为 `assumed`。
- PASS `assertion_4`: 每项使用 `assumed` 或 `blocked`，并提供可追踪 evidence references。
- PASS `assertion_5`: 包含 requirement matrix、execution path、evidence references、risk notes 和 handoff decision。
- PASS `assertion_6`: 没有把 assumed/blocked 项当成缺陷，且列出未覆盖风险。
- PASS `alignment_plan_gate`: 确认 `login-refresh` 下 PRD/TRD 对齐，识别同路径 `IMPLEMENTATION_PLAN.md` 缺失并标记 blocked；`Blocked items` 明确将 next owner 指向 `engineer-agent:feature-implementor`，恢复顺序为先确认 plan、再核对环境并执行 repo harness。

## With-Skill Behavior

候选正确执行文档与 QA memory preflight，没有伪造边界结果；修复后的 `Blocked items` 模板把缺 plan 的 owner 和恢复顺序接入最终报告。此前失败的 `alignment_plan_gate` 本轮通过，其余此前通过的断言无回归。

## Fresh Without-Skill Baseline

同一 prompt/fixture 的 without-skill baseline 已在本轮重新生成，未读取或应用 skill 与 QA README，且未复用历史 baseline。它只把测试环境和 `QA_BASE_URL` 作为 blocker，没有识别缺失的 `IMPLEMENTATION_PLAN.md`、next owner 或 plan-first 恢复顺序，因此不满足 `alignment_plan_gate`。

## Failures

- 无 behavior failure。

## Next Steps

- 若需覆盖 `assertion_3` 的实际边界执行分支，应在补齐并确认同路径 `IMPLEMENTATION_PLAN.md` 后另行执行；本轮保持 fixture 与门禁原状。

## Runtime Artifact Policy

- 本轮 with-skill 候选、重新生成的 without-skill baseline 与 judge 笔记均在上述 `tmp/eval-runs/`。
- Runtime 不提交；durable 结果仅为本文件。
