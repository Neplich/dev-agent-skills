# Eval Result: eval-001-route-mixed-qa-request

## Evaluation Target

- Skill: `qa-agent`
- Eval: `eval-001-route-mixed-qa-request`
- Prompt target: 对登录重构验收请求与 intermittent CI 失败先做单一路由，不执行测试。

## Test Set / Fixture Version

- Eval schema: `evals.json` v1.0
- Fixture version: repository commit `c664869`
- Fresh run: `2026-07-31 08:22:36 +0800`
- Runtime directory: `tmp/eval-runs/issue-196-l2-3-4/qa-agent/eval-001-route-mixed-qa-request/`
- `eval_metadata.json` 未声明 `execution_cleanup`。

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL**
- 所有 assertion 场景均已触发；无 `NOT EXERCISED` assertion。
- router 单表契约已触发：with-skill 依据 `Default Routes` 中含「信号示例」列的单表完成路由；未要求或伪造独立信号列表。

Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Assertion Results

- PASS `assertion_1`: 选择单一主 route `spec-based-tester`，并说明文档化验收是当前最窄 evidence outcome。
- PASS `assertion_2`: 显式列出 PRD、TRD、实现变更、CI 日志、QA 功能树、环境约束与 `npm test -- login`，未假设端口。
- PASS `specialist_gate_pointer`: 声明 `spec-based-tester` 的 E2E memory、platform version、credential、execution entry、PRD/TRD/implementation plan 与 blocked-condition 权威门禁适用；没有展开协议。
- PASS `assertion_4`: 预期 artifact 包含 requirement matrix、execution path、evidence references、结果/覆盖、risk notes 与 follow-up。
- PASS `assertion_5`: 未并行调用多个 specialist，intermittent 失败保持 risk/follow-up，不冒充 confirmed bug。

## With-Skill Behavior

with-skill 候选从单张 `Default Routes` 表选择 `spec-based-tester`，完整传递 fixture 上下文，保留 CI 风险边界并停止在路由阶段。门禁只以权威 specialist 指针声明，没有复制具体执行、凭据或阻塞协议。

## Fresh Without-Skill Baseline

本轮 baseline 使用同一 prompt 与 fixture 于隔离 scratch 重新生成；未读取或应用 `qa-agent` SKILL、QA README、with-skill 候选或旧 comparison，也未复用历史 baseline。它能保留 intermittent 风险边界并提出基本测试范围，但没有在四个 QA specialist 中命名单一主 route，没有 repo-specific specialist 权威门禁指针，artifact 结构也弱于 with-skill。

## Failures

- 无 with-skill assertion 失败。

## Next Steps

- 保持单表路由与 specialist 指针契约；后续 specialist 负责执行其权威门禁与测试协议。

## Runtime Artifact Policy

- 新生成的 with-skill / without-skill candidate 与 verdict 均在上述 `tmp/eval-runs/` 目录。
- Runtime 产物不提交；durable 结果仅为本文件。
