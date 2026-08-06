# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-003-audit-pure-refactor`

## Test Set / Fixture Version

- Fixture version: docs-audit A2 / 2026-07-19
- Assertions: 4

## Latest Result

- Overall result: PASS
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `PASS` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `sends_refactor_suspect_to_fact_layer` | PASS | FAIL | with_skill 明确写明页面“先列为 `suspect`；复核后确认”；without_skill 直接称“审计结论：通过”，未将未更新页面交给事实层。 |
| `classifies_accurate_refactor_verified` | PASS | FAIL | with_skill 最终明确标为 `verified`，并核对了 GET、limit、200、400 等事实；without_skill 仅称页面“当前内容仍准确”，没有 `verified` 的事实层结论。 |
| `does_not_force_noop_doc_edit` | PASS | PASS | 两条 lane 均明确说明纯实现重构无需更新 API 页面。 |
| `does_not_block_for_unchanged_accurate_doc` | PASS | PASS | 两条 lane 均未将页面判为 `stale`；with_skill 仅因缺少 Git 元数据而不能签发 `ready_for_tag`，without_skill 也未返回 `ready_for_tag` 或盖章。 |

未满足断言（with/without 任一 FAIL）：``sends_refactor_suspect_to_fact_layer``、``classifies_accurate_refactor_verified``



## Assertion Results
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

| Assertion | Result | Evidence summary |
| --- | --- | --- |
| `sends_refactor_suspect_to_fact_layer` | PASS | change-map 命中且文档未同批更新时先标 `suspect`，继续事实核对。 |
| `classifies_accurate_refactor_verified` | PASS | GET 路径、limit、200、400、鉴权、流式和文件行为逐项与代码一致，页面 `verified`。 |
| `does_not_force_noop_doc_edit` | PASS | 报告明确实现重构未改变 API，无需为同 diff 编辑准确文档。 |
| `does_not_block_for_unchanged_accurate_doc` | PASS | 页面未因“未修改”判 stale；整体只因 `docs-agent:release-notes-gen` handoff、Release Notes、索引、metadata 和宿主版本事实缺失而 blocked。 |

## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 来源：本轮 fresh session `019f7a73-2dfe-7161-b291-285f043ab1c7`，位于 `tmp/eval-runs/117/eval-003-audit-pure-refactor/with_skill/`。
- 候选只新增审计报告，未改页面、代码或 release metadata，未返回 `ready_for_tag`。

## Without-Skill Baseline
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 来源：本轮独立 fresh session `019f7a77-670e-7572-bc70-e597b5a8bcaa`，同一 prompt 与 pristine fixture；未复用历史 baseline。
- baseline 同样识别纯重构与版本表面缺口，并保持零写入，但没有持久化契约化审计报告。

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 无 assertion failure。合成 refs 使用 `.eval/actual-diff.patch`，是 harness 限制而非协议缺陷。

## Next Steps

- 保留本结果；纯重构放行语义或 release-surface gate 变化时重跑。

## Runtime Artifact Policy

- 本轮运行期证据仅位于 `tmp/eval-runs/117/`，不提交；durable 产物仅为本 `comparison.md`。
