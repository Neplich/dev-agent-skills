# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-003-audit-pure-refactor`

## Test Set / Fixture Version

- Fixture version: issue #117 A2 / 2026-07-19
- Assertions: 4

## Latest Result

**PASS — 4 / 4 assertions passed.** Fresh with-skill 候选将纯实现重构命中的页面从 `suspect` 经事实核对转为 `verified`，不要求无意义文档编辑；因完整 release-version surfaces 缺失，整体仍 `blocked` 且不盖章。

## Assertion Results

| Assertion | Result | Evidence summary |
| --- | --- | --- |
| `sends_refactor_suspect_to_fact_layer` | PASS | change-map 命中且文档未同批更新时先标 `suspect`，继续事实核对。 |
| `classifies_accurate_refactor_verified` | PASS | GET 路径、limit、200、400、鉴权、流式和文件行为逐项与代码一致，页面 `verified`。 |
| `does_not_force_noop_doc_edit` | PASS | 报告明确实现重构未改变 API，无需为同 diff 编辑准确文档。 |
| `does_not_block_for_unchanged_accurate_doc` | PASS | 页面未因“未修改”判 stale；整体只因 #116 handoff、Release Notes、索引、metadata 和宿主版本事实缺失而 blocked。 |

## With-Skill Behavior

- 来源：本轮 fresh session `019f7a73-2dfe-7161-b291-285f043ab1c7`，位于 `tmp/eval-runs/117/eval-003-audit-pure-refactor/with_skill/`。
- 候选只新增审计报告，未改页面、代码或 release metadata，未返回 `ready_for_tag`。

## Without-Skill Baseline

- 来源：本轮独立 fresh session `019f7a77-670e-7572-bc70-e597b5a8bcaa`，同一 prompt 与 pristine fixture；未复用历史 baseline。
- baseline 同样识别纯重构与版本表面缺口，并保持零写入，但没有持久化契约化审计报告。

## Failures

- 无 assertion failure。合成 refs 使用 `.eval/actual-diff.patch`，是 harness 限制而非协议缺陷。

## Next Steps

- 保留本结果；纯重构放行语义或 release-surface gate 变化时重跑。

## Runtime Artifact Policy

- 本轮运行期证据仅位于 `tmp/eval-runs/117/`，不提交；durable 产物仅为本 `comparison.md`。
