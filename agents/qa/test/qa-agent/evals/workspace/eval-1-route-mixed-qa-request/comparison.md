# Eval Result: eval-001-route-mixed-qa-request

## Evaluation Target

- Skill: `qa-agent`
- Eval: `eval-001-route-mixed-qa-request`
- Prompt target: 对登录重构验收请求与 intermittent CI 失败先做单一路由，不执行测试。

## Test Set / Fixture Version

- Eval schema: `evals.json` v1.0
- Fixture version: repository commit `cdfc879` plus current working-tree assertion alignment
- Fresh run: `2026-07-30 19:56:24 +0800`
- Runtime directory: `tmp/eval-runs/issue-196-pr-b-qa-agent-20260730-195624/eval-001-route-mixed-qa-request/`
- `eval_metadata.json` 未声明 `execution_cleanup`。

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL**
- 所有 assertion 场景均已触发；无 `NOT EXERCISED` assertion。
- 变更点检查：with-skill 输出声明所选 specialist 及权威门禁适用，只保留指针，未展开 specialist 协议。

Overall result: PASS

## Assertion Results

- PASS `assertion_1`: 选择单一主 route `spec-based-tester`，并说明文档化验收是当前最窄 evidence outcome。
- PASS `assertion_2`: 显式列出 PRD、TRD、实现变更、CI 日志、环境约束与 `npm test -- login`，未假设端口。
- PASS `specialist_gate_pointer`: 声明 `spec-based-tester` 的 E2E memory、platform version、credential、execution entry、PRD/TRD/implementation plan 与 blocked-condition 权威门禁适用；没有展开协议。
- PASS `assertion_4`: 预期 artifact 包含 requirement matrix、execution path、evidence references、结果/覆盖、risk notes 与 follow-up。
- PASS `assertion_5`: 未并行调用多个 specialist，intermittent 失败保持 risk/follow-up，不冒充 confirmed bug。

## With-Skill Behavior

with-skill 候选选择 `spec-based-tester`，完整传递 fixture 上下文，保留 CI 风险边界并停止在路由阶段。门禁只以权威 specialist 指针声明，没有复制具体执行、凭据或阻塞协议。

## Fresh Without-Skill Baseline

本轮 baseline 使用同一 prompt 与 fixture 于隔离 scratch 重新生成；未读取或应用 `qa-agent` SKILL、QA README，也未复用历史 baseline。它选择 `bug-analyzer`，偏离文档化验收主 outcome，且没有声明 repo-specific specialist 权威门禁指针。

## Failures

- 无 with-skill assertion 失败。

## Next Steps

- 保持 router 指针契约；后续 specialist 负责执行其权威门禁与测试协议。

## Runtime Artifact Policy

- 新生成的 with-skill / without-skill candidate 与 verdict 均在上述 `tmp/eval-runs/` 目录。
- Runtime 产物不提交；durable 结果仅为本文件。
