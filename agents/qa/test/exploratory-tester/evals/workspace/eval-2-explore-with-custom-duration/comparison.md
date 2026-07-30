# Eval Result: eval-002-explore-with-custom-duration

## Evaluation Target

- Skill: `exploratory-tester`
- Eval: `eval-002-explore-with-custom-duration`
- Prompt target: 使用用户给定 5 分钟 timebox 探索 settings 变更面。

## Test Set / Fixture Version

- Eval schema: `evals.json` v1.0
- Fixture version: repository commit `778b042`
- Fresh run: `2026-07-30 19:26:38 +0800`
- Runtime directory: `tmp/eval-runs/issue-196-pr-b-20260730-192638/qa/agents/qa/test/exploratory-tester/evals/workspace/eval-2-explore-with-custom-duration/`
- `eval_metadata.json` 未声明 `execution_cleanup`。

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL**
- 平台版本缺失触发预期 blocker；没有 assertion 因该 blocker 被遗漏。
- 非 E2E 路径变更检查：这是 E2E `feature-update` 场景，未触发 `docs/qa/{feature_path}/exploratory-report.md`。

Overall result: PASS

## Assertion Results

- PASS `assertion_1`: 使用 URL 与 5 分钟建立 charter，记录 changed surface、环境和未验证的实际加载/登录/交互前提。
- PASS `assertion_2`: 完整记录 suite、flow、缺失 cases/scripts/results/reports，确认 `feature-update`，并说明扩充路径。
- PASS `version_entry_and_subagent`: 平台版本缺失时 blocked，列出执行入口顺序、未选择入口原因和 subagent 默认。
- PASS `assertion_3`: confirmed blocker、unconfirmed signals、uncovered areas 分层，未伪造 console/network/page-crash 结果。
- PASS `assertion_4`: 明确实际路径停在只读 preflight，并提供 evidence references；合法 blocked 不要求虚构浏览器步骤。
- PASS `assertion_5`: 风险 notes 与后续 QA/bug-analyzer 条件清楚。

## With-Skill Behavior

候选完整执行了 blocked preflight；没有平台版本时不开始 5 分钟执行是正确行为，不应因缺少实际 UI 证据判为行为失败。

## Fresh Without-Skill Baseline

同一 prompt/fixture 的全新 baseline 已生成，未读取 skill、QA README 或历史 baseline。candidate/verdict 均成功；baseline 缺完整 memory、entry 和 subagent 协议，semantic verdict 为 FAIL。

## Failures

- 无。

## Next Steps

- 提供平台版本后才可开始真实 5 分钟探索；本 eval 保留为 blocked-preflight 回归。

## Runtime Artifact Policy

- 两条 candidate、两条 verdict、diagnostics 与 `comparison.auto.md` 均在上述 `tmp/eval-runs/`，返回码均为 0、无 timeout。
- Runtime 不提交；durable 结果仅为本文件。
