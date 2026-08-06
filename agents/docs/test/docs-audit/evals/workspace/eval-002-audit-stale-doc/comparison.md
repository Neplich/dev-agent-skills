# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-002-audit-stale-doc`

## Test Set / Fixture Version

- Fixture version: docs-audit A2 / 2026-07-19
- Assertions: 4

## Latest Result

- Overall result: FAIL
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `FAIL` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `marks_missing_doc_update_suspect` | PASS | FAIL | with_skill 报告明确写明 required page 的确定性状态为 `suspect`，随后事实层判为 `stale`；without_skill 直接判为 stale，未标记 `suspect`。 |
| `confirms_outdated_claim_stale` | PASS | PASS | 两条 lane 均核对 `src/catalog/routes.txt`：新增必填非空 `locale` 与 `400 invalid_locale`，而 `catalog.md` 未声明，均确认文档为 stale。 |
| `blocks_stale_release` | PASS | FAIL | with_skill 报告 frontmatter 为 `phase_result: blocked`，并明确“不可 `ready_for_tag`”；without_skill 仅为 `status: fail`，未形成 pre-tag `blocked` 结果。 |
| `does_not_stamp_stale_set` | PASS | PASS | 两条 lane 的 `catalog.md` 和 `change-map.yaml` 仍为 `last_verified_version: v1.0.0`，且均不存在或更新 `.meta/releases.json`；报告也明确未执行版本戳更新。 |

未满足断言：``marks_missing_doc_update_suspect``、``blocks_stale_release``


**PASS — 4 / 4 assertions passed.** Fresh with-skill 候选先标 `suspect`，再以新增必填 `locale` 和 `invalid_locale` 错误证据确认 `stale`，pre-tag `blocked` 且零盖章。

## Assertion Results
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

| Assertion | Result | Evidence summary |
| --- | --- | --- |
| `marks_missing_doc_update_suspect` | PASS | required doc 未同批更新时仅标 `suspect` 并送事实层，没有直接等同于 stale。 |
| `confirms_outdated_claim_stale` | PASS | 当前代码要求非空 `locale` 并定义 400 `invalid_locale`，文档遗漏，事实层判 `stale`。 |
| `blocks_stale_release` | PASS | 报告列出同步文档、补齐 release surfaces、重审的待办，结果 `blocked`。 |
| `does_not_stamp_stale_set` | PASS | 页面版本保持 `v1.0.0`，未创建或修改 `.meta/releases.json`。 |

## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 来源：本轮 fresh session `019f7a73-2dfe-7763-a3a0-e6156e81de1b`，位于 `tmp/eval-runs/117/eval-002-audit-stale-doc/with_skill/`。
- 候选持久化契约路径报告，清楚区分确定性 `suspect` 与事实层 `stale`。

## Without-Skill Baseline
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 来源：本轮独立 fresh session `019f7a77-668b-7f93-b7db-5e4a32d4d4d0`，同一 prompt 与 pristine fixture；未复用历史 baseline。
- baseline 同样识别 stale 和 blocked，但报告位于 `.eval/audit-report.md`，未完整体现版本表面与契约化报告路径。

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 无 assertion failure。合成 refs 通过 `.eval/actual-diff.patch` 复现，属于 harness 限制，不是协议缺陷。

## Next Steps

- 保留本结果；suspect/stale 判定规则变化时重跑。

## Runtime Artifact Policy

- 本轮运行期证据仅位于 `tmp/eval-runs/117/`，不提交；durable 产物仅为本 `comparison.md`。
