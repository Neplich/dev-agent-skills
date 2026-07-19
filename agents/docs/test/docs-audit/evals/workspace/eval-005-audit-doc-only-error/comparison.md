# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-005-audit-doc-only-error`

## Test Set / Fixture Version

- Fixture version: issue #117 A2 / 2026-07-19
- Assertions: 4

## Latest Result

**PASS — 4 / 4 assertions passed.** Fresh with-skill 候选把纯文档变更直接纳入影响域，按 `related_code` 发现无实现的 DELETE 声明，判 `mismatch`、pre-tag `blocked` 且零盖章。

## Assertion Results

| Assertion | Result | Evidence summary |
| --- | --- | --- |
| `includes_doc_only_change` | PASS | `catalog.md` 即使没有代码 diff 或 change-map 命中也直接进入影响域。 |
| `uses_related_code_for_fact_check` | PASS | 事实层按页面 `related_code` 核对 `src/catalog/routes.txt`。 |
| `classifies_doc_only_conflict_mismatch` | PASS | 文档 DELETE/204 与代码仅有 GET 的事实、证据和影响均保留，结论 `mismatch`。 |
| `blocks_despite_no_code_diff` | PASS | 结果 `blocked`，页面保持 `v1.0.0`，没有因无代码 diff 放行或盖章。 |

## With-Skill Behavior

- 来源：本轮 fresh session `019f7a75-30f1-7de1-9565-f18800886463`，位于 `tmp/eval-runs/117/eval-005-audit-doc-only-error/with_skill/`。
- 候选只新增契约路径报告，不修复页面或生成 release metadata。

## Without-Skill Baseline

- 来源：本轮独立 fresh session `019f7a78-ed50-7d13-aa25-55b5c7407307`，同一 prompt 与 pristine fixture；未复用历史 baseline。
- baseline 同样识别 DELETE 冲突并阻塞，但报告写入 `.eval/pre-tag-audit-report.md`，影响域与协议边界证据较简略。

## Failures

- 无 assertion failure。合成 refs 使用 `.eval/actual-diff.patch`，属于 harness 限制，不是协议缺陷。

## Next Steps

- 保留本结果；文档-only 影响域规则变化时重跑。

## Runtime Artifact Policy

- 本轮运行期证据仅位于 `tmp/eval-runs/117/`，不提交；durable 产物仅为本 `comparison.md`。
