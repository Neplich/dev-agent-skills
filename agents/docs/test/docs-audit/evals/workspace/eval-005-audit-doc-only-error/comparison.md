# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-005-audit-doc-only-error`

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
| `includes_doc_only_change` | PASS | FAIL | with_skill 明确写出“变更文件：`docs/site/api/catalog.md`”“影响文档：`docs/site/api/catalog.md`”；without_skill 仅说明实际差异仅修改该文件，未明确将其加入影响域。 |
| `uses_related_code_for_fact_check` | PASS | PASS | 两条 lane 均核对 `src/catalog/routes.txt`，并指出该文件仅定义 `GET /catalog/items`、没有 DELETE；没有因无代码 diff 跳过核验。 |
| `classifies_doc_only_conflict_mismatch` | PASS | FAIL | with_skill 保留 DELETE 文档声明、代码事实、证据和影响，并明确判定为 `mismatch`；without_skill 描述了冲突，但未给出 `mismatch` 分类。 |
| `blocks_despite_no_code_diff` | PASS | FAIL | with_skill 明确结论为 `blocked`、不能进入 `ready_for_tag`，且未盖章；without_skill 仅称“不通过（需修复）”，未明确阻塞或禁止 `ready_for_tag`。 |

未满足断言（with/without 任一 FAIL）：``includes_doc_only_change``、``classifies_doc_only_conflict_mismatch``、``blocks_despite_no_code_diff``



## Assertion Results
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

| Assertion | Result | Evidence summary |
| --- | --- | --- |
| `includes_doc_only_change` | PASS | `catalog.md` 即使没有代码 diff 或 change-map 命中也直接进入影响域。 |
| `uses_related_code_for_fact_check` | PASS | 事实层按页面 `related_code` 核对 `src/catalog/routes.txt`。 |
| `classifies_doc_only_conflict_mismatch` | PASS | 文档 DELETE/204 与代码仅有 GET 的事实、证据和影响均保留，结论 `mismatch`。 |
| `blocks_despite_no_code_diff` | PASS | 结果 `blocked`，页面保持 `v1.0.0`，没有因无代码 diff 放行或盖章。 |

## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 来源：本轮 fresh session `019f7a75-30f1-7de1-9565-f18800886463`，位于 `tmp/eval-runs/117/eval-005-audit-doc-only-error/with_skill/`。
- 候选只新增契约路径报告，不修复页面或生成 release metadata。

## Without-Skill Baseline
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 来源：本轮独立 fresh session `019f7a78-ed50-7d13-aa25-55b5c7407307`，同一 prompt 与 pristine fixture；未复用历史 baseline。
- baseline 同样识别 DELETE 冲突并阻塞，但报告写入 `.eval/pre-tag-audit-report.md`，影响域与协议边界证据较简略。

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 无 assertion failure。合成 refs 使用 `.eval/actual-diff.patch`，属于 harness 限制，不是协议缺陷。

## Next Steps

- 保留本结果；文档-only 影响域规则变化时重跑。

## Runtime Artifact Policy

- 本轮运行期证据仅位于 `tmp/eval-runs/117/`，不提交；durable 产物仅为本 `comparison.md`。
