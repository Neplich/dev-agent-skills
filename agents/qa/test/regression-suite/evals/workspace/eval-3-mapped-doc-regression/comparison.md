# Eval Result: eval-003-mapped-doc-regression

## Evaluation Target

- Skill: `regression-suite`
- Eval: `eval-003-mapped-doc-regression`
- Prompt target: 由 change-map 收敛搜索阈值回归范围并以代码确定实际值。

## Test Set / Fixture Version

- Eval schema: `evals.json` v1.0
- Fixture version: repository commit `778b042`
- Fresh run: `2026-07-30 19:26:38 +0800`
- Runtime directory: `tmp/eval-runs/issue-196-pr-b-20260730-192638/qa/agents/qa/test/regression-suite/evals/workspace/eval-3-mapped-doc-regression/`
- `eval_metadata.json` 未声明 `execution_cleanup`。

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL**
- 无 `NOT EXERCISED` assertion。
- 非 E2E 路径变更检查：prompt 只要求回归范围与阈值判断，没有要求持久化报告；`docs/qa/{feature_path}/regression-verification.md` 未覆盖。

Overall result: PASS

## Assertion Results

- PASS `reads_mapped_docs_first`: change-map 将范围收窄到 `search-query.md`，未遍历其他文档。
- PASS `verifies_against_code`: 代码阈值 3、文档阈值 2 分开记录，并围绕 2/3 边界设计直接路径。
- PASS `treats_unverified_as_low_trust`: `unverified` 文档不作为 pass/release-ready 的独立依据。

## With-Skill Behavior

候选以代码值 3 为事实，同时保留目标预期仍需确认的边界，没有把过时文档直接当回归 oracle。

## Fresh Without-Skill Baseline

同一 prompt/fixture 的全新 baseline 已生成，未读取 skill、QA README 或历史 baseline。candidate/verdict 均成功；baseline 也满足三条 assertions，semantic verdict 为 PASS。

## Failures

- 无 assertion failure。

## Next Steps

- PR-B 非 E2E 路径需独立持久化报告 fixture；本次不改现有 eval。

## Runtime Artifact Policy

- 两条 candidate、两条 verdict、diagnostics 与 `comparison.auto.md` 均在上述 `tmp/eval-runs/`，返回码均为 0、无 timeout。
- Runtime 不提交；durable 结果仅为本文件。
