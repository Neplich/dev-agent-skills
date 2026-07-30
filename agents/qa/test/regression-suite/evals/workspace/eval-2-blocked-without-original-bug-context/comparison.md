# Eval Result: eval-002-blocked-without-original-bug-context

## Evaluation Target

- Skill: `regression-suite`
- Eval: `eval-002-blocked-without-original-bug-context`
- Prompt target: 原始 bug、修复与环境均缺失时给出 blocked 回归结论。

## Test Set / Fixture Version

- Eval schema: `evals.json` v1.0
- Fixture version: repository commit `778b042`
- Fresh run: `2026-07-30 19:26:38 +0800`
- Runtime directory: `tmp/eval-runs/issue-196-pr-b-20260730-192638/qa/agents/qa/test/regression-suite/evals/workspace/eval-2-blocked-without-original-bug-context/`
- `eval_metadata.json` 未声明 `execution_cleanup`。

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL**
- 所有 blocked assertions 均由 fixture 明确触发；无 `NOT EXERCISED`。
- 非 E2E 路径变更检查：没有足够 `feature_path` 或 fix evidence 生成正式报告，`docs/qa/{feature_path}/regression-verification.md` 分支未触发。

Overall result: PASS

## Assertion Results

- PASS `assertion_1`: 先指出原始 bug、失败证据、修复 PR 与环境缺失，不做泛化回归。
- PASS `blocked`: original failure、fixed behavior、adjacent checks、平台版本与对齐均 blocked/not executed。
- PASS `assertion_3`: 所需结构与 confidence 完整。
- PASS `assertion_4`: recommendation 为 blocked，不建议 release ready。
- PASS `no_unknown_or_unscoped_release`: 不使用 `unknown`，不冒充 release 全量，并列出恢复证据。

## With-Skill Behavior

候选把“资料缺失”与“新回归”分开，明确恢复验证所需输入；合法 blocked 满足全部 assertions。

## Fresh Without-Skill Baseline

同一 prompt/fixture 的全新 baseline 已生成，未读取 skill、QA README 或历史 baseline。candidate/verdict 均成功，baseline 也满足全部 assertions，semantic verdict 为 PASS。

## Failures

- 无。

## Next Steps

- 只有补齐原始 bug、修复证据、环境、版本和预期后才重启回归。

## Runtime Artifact Policy

- 两条 candidate、两条 verdict、diagnostics 与 `comparison.auto.md` 均在上述 `tmp/eval-runs/`，返回码均为 0、无 timeout。
- Runtime 不提交；durable 结果仅为本文件。
