# Eval Result: eval-002-thin-evidence-suspected-bug

## Evaluation Target

- Skill: `bug-analyzer`
- Eval: `eval-002-thin-evidence-suspected-bug`
- Prompt target: 薄证据用户反馈不得升级为 confirmed bug。

## Test Set / Fixture Version

- Eval schema: `evals.json` v1.0
- Fixture version: repository commit `778b042`
- Fresh run: `2026-07-30 19:26:38 +0800`
- Runtime directory: `tmp/eval-runs/issue-196-pr-b-20260730-192638/qa/agents/qa/test/bug-analyzer/evals/workspace/eval-2-thin-evidence-suspected-bug/`
- `eval_metadata.json` 未声明 `execution_cleanup`。

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL**
- 无 `NOT EXERCISED` assertion。
- 非 E2E 路径变更检查：该场景只允许调查 note/补证清单，不生成正式非 E2E Bug 报告，因此 `docs/qa/{feature_path}/bug-*.md` 分支未触发。

Overall result: PASS

## Assertion Results

- PASS `assertion_1`: 分类为 `suspected / needs more evidence`。
- PASS `assertion_2`: 完整列出 failing scenario、步骤、环境/版本、console/network、截图与 trace 缺口。
- PASS `assertion_3`: 包含 classification、evidence status、confidence、missing evidence、recommended evidence。
- PASS `assertion_4`: 未创建 GitHub issue 或 confirmed bug，只建议本地调查 note。

## With-Skill Behavior

候选保持低置信度与证据门槛，清楚说明当前只能形成调查型分析，未越权生成 confirmed bug。

## Fresh Without-Skill Baseline

同一 prompt/fixture 的全新 baseline 已生成，未读取 skill、QA README 或历史 baseline。candidate/verdict 均成功；baseline 也满足四条 assertions，semantic verdict 为 PASS。

## Failures

- 无。

## Next Steps

- 保留为薄证据边界回归用例；正式非 E2E 输出路径需由另一 fixture 覆盖。

## Runtime Artifact Policy

- 两条 candidate、两条 verdict、diagnostics 与 `comparison.auto.md` 均在上述 `tmp/eval-runs/`，返回码均为 0、无 timeout。
- Runtime 不提交；durable 结果仅为本文件。
