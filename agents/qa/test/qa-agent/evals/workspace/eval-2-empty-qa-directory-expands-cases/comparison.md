# Eval Result: eval-002-empty-qa-directory-expands-cases

## Evaluation Target

- Skill: `qa-agent`
- Eval: `eval-002-empty-qa-directory-expands-cases`
- Prompt target: 对已有但无 TC 的 E2E 功能树做路由与执行协议说明。

## Test Set / Fixture Version

- Eval schema: `evals.json` v1.0
- Fixture version: repository commit `778b042`
- Fresh run: `2026-07-30 19:26:38 +0800`
- Runtime directory: `tmp/eval-runs/issue-196-pr-b-20260730-192638/qa/agents/qa/test/qa-agent/evals/workspace/eval-2-empty-qa-directory-expands-cases/`
- `eval_metadata.json` 未声明 `execution_cleanup`。

## Latest Result

- Behavior result: **FAIL**
- Coverage result: **FULL**
- 所有 assertion 场景均已触发；无 `NOT EXERCISED` assertion。
- 变更点检查：候选逐项复述了 specialist 的完整 E2E memory、平台版本、执行入口、subagent、凭据和报告规则，没有保持“router 只保留权威指针”的 PR-B 目标。

Overall result: FAIL

## Assertion Results

- PASS `assertion_1`: 正确识别空功能树不是现有覆盖。
- PASS `assertion_2`: 用户已授权探索，要求读取目标源文件与环境说明。
- PASS `assertion_3`: 要求更新 `TEST_SUITE.md`、`FLOW_INDEX.md` 并记录探索证据。
- PASS `e2e`: 给出独立 TC/script 路径并禁止明文凭据。
- PASS `assertion_5`: 要求基于新增 TC 执行并保留 repo harness > Chrome/browser > Playwright 顺序。
- PASS `version_and_subagent_gate`: 平台版本缺失时 blocked，不写 `unknown`，TC 交给 subagent，报告路径正确。
- PASS `assertion_6`: 选择单一 `exploratory-tester` route，未进入实现修复。

## With-Skill Behavior

候选满足现有七条 assertions，但输出把 specialist 协议完整复制进 router；这违反当前 `qa-agent` 的 `Output Behavior` 指针契约，属于本次行为变更的直接回归，因此 Behavior 判 FAIL。

## Fresh Without-Skill Baseline

本轮 baseline 使用同一 prompt 与 fixture 新生成，未读取 skill、QA README 或历史 baseline。candidate/verdict 均成功；baseline 也复制了大部分 specialist 细节，但遗漏测试命令与完整探索沉淀字段，semantic verdict 为 FAIL。

## Failures

- PR-B router 指针收敛未在该候选中生效，输出仍复述 specialist 门禁细节。

## Next Steps

- 保留 assertions 结果与 router 契约失败的双重事实；后续应让 eval prompt/judge 明确验证“只输出指针”。

## Runtime Artifact Policy

- 两条 candidate、两条 verdict、diagnostics 与 `comparison.auto.md` 均在上述 `tmp/eval-runs/` 目录，返回码均为 0、无 timeout。
- Runtime 产物不提交；durable 结果仅为本文件。
