# Eval Result: eval-001-route-mixed-qa-request

## Evaluation Target

- Skill: `qa-agent`
- Eval: `eval-001-route-mixed-qa-request`
- Prompt target: 对登录重构验收请求与 intermittent CI 失败先做单一路由，不执行测试。

## Test Set / Fixture Version

- Eval schema: `evals.json` v1.0
- Fixture version: repository commit `778b042`
- Fresh run: `2026-07-30 19:26:38 +0800`
- Runtime directory: `tmp/eval-runs/issue-196-pr-b-20260730-192638/qa/agents/qa/test/qa-agent/evals/workspace/eval-1-route-mixed-qa-request/`
- `eval_metadata.json` 未声明 `execution_cleanup`。

## Latest Result

- Behavior result: **FAIL**
- Coverage result: **FULL**
- 所有 assertion 场景均已触发；无 `NOT EXERCISED` assertion。
- 变更点检查：with-skill 输出只声明 specialist 的权威门禁指针，未复述完整门禁细节，符合当前 `qa-agent` router 的收敛目标；但这与本 eval 仍要求 router 展开 E2E、凭据/报告和对齐门禁细节的 assertions 发生直接冲突。

Overall result: FAIL

## Assertion Results

- PASS `assertion_1`: 选择单一主 route `spec-based-tester`，并说明其最符合文档化验收 outcome。
- FAIL `assertion_2`: 列出了 PRD、TRD、实现变更和 CI 日志，但没有显式列出环境说明与测试命令。
- FAIL `qa`: 仅列出 `TEST_SUITE.md`、`FLOW_INDEX.md`，完整 `cases/`、`scripts/`、历史 `results/`、`_reports/` 只由 specialist 指针承接，未满足 assertion 的字面展开要求。
- FAIL `e2e_execution_protocol`: 当前 router 正确保留指针，但未按旧 assertion 逐项复述场景、平台版本、`unknown` 禁止、执行入口与 subagent 规则。
- FAIL `credential_and_report_refs`: 当前 router 正确保留 credential/report 指针，但未按旧 assertion 展开两个 reference 与本地凭据路径。
- FAIL `alignment_and_plan_gate`: 当前 router 正确保留 PRD/TRD/plan 指针，但未按旧 assertion 展开各 gap 的 next owner。
- PASS `assertion_4`: 预期 artifact 包含 requirement matrix、evidence references、risk notes 与 defect handoff notes。
- PASS `assertion_5`: 未并行调用多个 specialist，intermittent 失败保持 risk/follow-up，不冒充 confirmed bug。

## With-Skill Behavior

with-skill 候选选择 `spec-based-tester`，保留 CI 风险边界并停止在路由阶段。它体现了 PR-B 的 router 指针收敛，但无法同时满足仍要求复制 specialist 协议的旧 assertions，因此 Behavior 判 FAIL。

## Fresh Without-Skill Baseline

本轮 baseline 使用同一 prompt 与 fixture 于隔离 scratch 重新生成；未读取 `qa-agent` SKILL、QA README 或历史 baseline。它选择 `bug-analyzer`，候选与 verdict 均生成成功，但同样缺少 repo-specific specialist 门禁，semantic verdict 为 FAIL。

## Failures

- Router 新契约与当前 eval 的细节展开 assertions 不一致。
- 上下文传递未显式包含环境说明与测试命令。

## Next Steps

- 后续由维护者决定是把 assertions 收敛为“权威指针存在且不复述”，还是恢复 router 细节；本次 eval 不修改 fixture。

## Runtime Artifact Policy

- 两条 candidate、两条 verdict、diagnostics 与 `comparison.auto.md` 均在上述 `tmp/eval-runs/` 目录，返回码均为 0、无 timeout。
- Runtime 产物不提交；durable 结果仅为本文件。
