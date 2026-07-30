# Eval Result: eval-003-mapped-doc-exploration

## Evaluation Target

- Skill: `exploratory-tester`
- Eval: `eval-003-mapped-doc-exploration`
- Prompt target: 以 change-map 缩小结账超时探索范围并由代码核证。

## Test Set / Fixture Version

- Eval schema: `evals.json` v1.0
- Fixture version: repository commit `778b042`
- Fresh run: `2026-07-30 19:26:38 +0800`
- Runtime directory: `tmp/eval-runs/issue-196-pr-b-20260730-192638/qa/agents/qa/test/exploratory-tester/evals/workspace/eval-3-mapped-doc-exploration/`
- `eval_metadata.json` 未声明 `execution_cleanup`。

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL**
- 无 `NOT EXERCISED` assertion。
- 非 E2E 路径变更检查：prompt 只要求探索章程与边界，没有要求持久化报告；`docs/qa/{feature_path}/exploratory-report.md` 未覆盖。

Overall result: PASS

## Assertion Results

- PASS `reads_mapped_docs_first`: 通过 change-map 只读取 checkout session 文档。
- PASS `verifies_against_code`: 明确文档 15 分钟、代码 10 分钟，并以 10 分钟设计边界。
- PASS `treats_unverified_as_low_trust`: `unverified` 文档仅作低信任线索，关键假设回到代码。

## With-Skill Behavior

候选覆盖 9:59、10:00、10:01 等直接边界，并把文档冲突、运行时未验证与推荐下一步清楚分开。

## Fresh Without-Skill Baseline

同一 prompt/fixture 的全新 baseline 已生成，未读取 skill、QA README 或历史 baseline。candidate/verdict 均成功；baseline 也满足三条 assertions，semantic verdict 为 PASS。

## Failures

- 无 assertion failure。

## Next Steps

- PR-B 非 E2E 报告路径需要独立的持久化报告 fixture；本次不改现有 eval。

## Runtime Artifact Policy

- 两条 candidate、两条 verdict、diagnostics 与 `comparison.auto.md` 均在上述 `tmp/eval-runs/`，返回码均为 0、无 timeout。
- Runtime 不提交；durable 结果仅为本文件。
