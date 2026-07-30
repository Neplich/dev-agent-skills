# Eval Result: eval-001-verify-bug-fix

## Evaluation Target

- Skill: `regression-suite`
- Eval: `eval-001-verify-bug-fix`
- Prompt target: 复用 BUG-001 与修复上下文做定向回归判断。

## Test Set / Fixture Version

- Eval schema: `evals.json` v1.0
- Fixture version: repository commit `778b042`
- Fresh run: `2026-07-30 19:26:38 +0800`
- Runtime directory: `tmp/eval-runs/issue-196-pr-b-20260730-192638/qa/agents/qa/test/regression-suite/evals/workspace/eval-1-verify-bug-fix/`
- `eval_metadata.json` 未声明 `execution_cleanup`。

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL**
- 缺同路径 PRD/TRD/plan 已触发预期 blocker；无 `NOT EXERCISED` assertion。
- 非 E2E 路径变更检查：fixture 是 E2E `feature-update` 回归，未触发 `docs/qa/{feature_path}/regression-verification.md`。

Overall result: PASS

## Assertion Results

- PASS `assertion_1`: 读取 BUG-001、PR-001，复用原始步骤、预期与共享序列化风险。
- PASS `qa`: 使用 suite、flow、case、script；无历史 results/reports 可用时没有伪造其内容。
- PASS `assertion_3`: original failure、fixed behavior 与总状态均为 blocked/not executed。
- PASS `assertion_4`: `feature-update` 只覆盖成功登录、无效凭据、锁定账号与 session/redirect 直接面。
- PASS `alignment_version_archive`: 同路径 PRD/TRD/plan 缺失导致 blocked；平台版本与追加目录明确，不覆盖历史。
- PASS `assertion_5`: release recommendation 为 blocked，run status 与 confidence 分离。

## With-Skill Behavior

候选没有因为 fixture 提供了 bug、fix 和平台版本就越过对齐门禁；blocked 是正确的 assertion 满足方式。

## Fresh Without-Skill Baseline

同一 prompt/fixture 的全新 baseline 已生成，未读取 skill、QA README 或历史 baseline。candidate/verdict 均成功；baseline 缺 PRD/TRD/plan gate，semantic verdict 为 FAIL。

## Failures

- 无。

## Next Steps

- 补齐同路径 PRD/TRD/confirmed plan 后才可执行与归档真实回归证据。

## Runtime Artifact Policy

- 两条 candidate、两条 verdict、diagnostics 与 `comparison.auto.md` 均在上述 `tmp/eval-runs/`，返回码均为 0、无 timeout。
- Runtime 不提交；durable 结果仅为本文件。
