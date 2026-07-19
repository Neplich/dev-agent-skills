# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-002-audit-stale-doc`

## Test Set / Fixture Version

- Fixture version: issue #117 A2 / 2026-07-19
- Assertions: 4

## Latest Result

**PASS — 4 / 4 assertions passed.** Fresh with-skill 候选先标 `suspect`，再以新增必填 `locale` 和 `invalid_locale` 错误证据确认 `stale`，pre-tag `blocked` 且零盖章。

## Assertion Results

| Assertion | Result | Evidence summary |
| --- | --- | --- |
| `marks_missing_doc_update_suspect` | PASS | required doc 未同批更新时仅标 `suspect` 并送事实层，没有直接等同于 stale。 |
| `confirms_outdated_claim_stale` | PASS | 当前代码要求非空 `locale` 并定义 400 `invalid_locale`，文档遗漏，事实层判 `stale`。 |
| `blocks_stale_release` | PASS | 报告列出同步文档、补齐 release surfaces、重审的待办，结果 `blocked`。 |
| `does_not_stamp_stale_set` | PASS | 页面版本保持 `v1.0.0`，未创建或修改 `.meta/releases.json`。 |

## With-Skill Behavior

- 来源：本轮 fresh session `019f7a73-2dfe-7763-a3a0-e6156e81de1b`，位于 `tmp/eval-runs/117/eval-002-audit-stale-doc/with_skill/`。
- 候选持久化契约路径报告，清楚区分确定性 `suspect` 与事实层 `stale`。

## Without-Skill Baseline

- 来源：本轮独立 fresh session `019f7a77-668b-7f93-b7db-5e4a32d4d4d0`，同一 prompt 与 pristine fixture；未复用历史 baseline。
- baseline 同样识别 stale 和 blocked，但报告位于 `.eval/audit-report.md`，未完整体现版本表面与契约化报告路径。

## Failures

- 无 assertion failure。合成 refs 通过 `.eval/actual-diff.patch` 复现，属于 harness 限制，不是协议缺陷。

## Next Steps

- 保留本结果；suspect/stale 判定规则变化时重跑。

## Runtime Artifact Policy

- 本轮运行期证据仅位于 `tmp/eval-runs/117/`，不提交；durable 产物仅为本 `comparison.md`。
