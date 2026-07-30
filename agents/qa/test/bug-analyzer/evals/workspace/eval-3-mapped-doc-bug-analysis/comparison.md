# Eval Result: eval-003-mapped-doc-bug-analysis

## Evaluation Target

- Skill: `bug-analyzer`
- Eval: `eval-003-mapped-doc-bug-analysis`
- Prompt target: 通过 change-map 定位通知重试文档并回到代码核证。

## Test Set / Fixture Version

- Eval schema: `evals.json` v1.0
- Fixture version: repository commit `778b042`
- Fresh run: `2026-07-30 19:26:38 +0800`
- Runtime directory: `tmp/eval-runs/issue-196-pr-b-20260730-192638/qa/agents/qa/test/bug-analyzer/evals/workspace/eval-3-mapped-doc-bug-analysis/`
- `eval_metadata.json` 未声明 `execution_cleanup`。

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL**
- 无 `NOT EXERCISED` assertion。
- 非 E2E 路径变更检查：prompt/assertions 只要求证据化静态分析，没有要求持久化报告路径；`docs/qa/{feature_path}/bug-*.md` 未被覆盖。

Overall result: PASS

## Assertion Results

- PASS `reads_mapped_docs_first`: 通过 change-map 精准读取 `notification-retry.md`，未遍历无关文档。
- PASS `verifies_against_code`: 分别记录文档 3 次与代码 2 次，并以代码事实影响缺陷分类。
- PASS `treats_unverified_as_low_trust`: 识别 `unverified`，文档仅作低信任线索，关键结论由代码支撑。

## With-Skill Behavior

候选形成了清楚的文档声明、代码事实、证据边界和影响说明；静态冲突确认与运行时影响未验证被正确分开。

## Fresh Without-Skill Baseline

同一 prompt/fixture 的全新 baseline 已生成，未读取 skill、QA README 或历史 baseline。candidate/verdict 均成功；baseline 同样满足三条 assertions，semantic verdict 为 PASS。

## Failures

- 无 assertion failure。

## Next Steps

- 若要验证 PR-B 非 E2E 路径，应新增明确要求持久化报告且提供 `feature_path` 的 eval；本次不改 fixture。

## Runtime Artifact Policy

- 两条 candidate、两条 verdict、diagnostics 与 `comparison.auto.md` 均在上述 `tmp/eval-runs/`，返回码均为 0、无 timeout。
- Runtime 不提交；durable 结果仅为本文件。
