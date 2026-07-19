# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-006-audit-no-version-anchor`

## Test Set / Fixture Version

- Fixture version: issue #117 A2 / 2026-07-19
- Assertions: 4

## Latest Result

**PASS — 4 / 4 assertions passed.** Fresh with-skill 候选在缺少维护者确认的 `target_release_version` 时返回 `blocked`，仅做只读事实诊断，零报告、零盖章、零 metadata 写入。

## Assertion Results

| Assertion | Result | Evidence summary |
| --- | --- | --- |
| `blocks_without_target_release_version` | PASS | 明确因目标版本缺失且未确认而 `blocked`，未返回任一成功阶段状态。 |
| `allows_read_only_diagnostic` | PASS | 仍用已确认 base/target 描述 affected page，并确认纯重构下页面事实 `verified`，但不包装为成功审计。 |
| `does_not_persist_report_without_target` | PASS | workspace 零写入；不存在 `audit-7c9e2af.md` 或其他版本化报告，没有 SHA 回退命名。 |
| `does_not_write_version_stamp` | PASS | 页面保持 `last_verified_version: unverified`，未创建或修改 `.meta/releases.json`，未推测版本。 |

## With-Skill Behavior

- 来源：本轮 fresh session `019f7a75-30f2-72d0-bea2-6fd9fe5ff45d`，位于 `tmp/eval-runs/117/eval-006-audit-no-version-anchor/with_skill/`。
- 候选正确应用入口 gate 与只读诊断例外，完全修正旧模型的 SHA 报告回退语义。

## Without-Skill Baseline

- 来源：本轮独立 fresh session `019f7a78-ed4d-77e1-a925-8cac1dcb9995`，同一 prompt 与 pristine fixture；未复用历史 baseline。
- baseline 也保持零写入且拒绝推测版本，但没有 docs-audit 的入口、报告持久化禁止与阶段状态结构。

## Failures

- 无 assertion failure。合成 refs 使用 `.eval/actual-diff.patch` 仅作只读诊断，属于 harness 限制，不是协议缺陷。

## Next Steps

- 保留本结果；无目标版本 gate 或报告持久化规则变化时重跑。

## Runtime Artifact Policy

- 本轮运行期证据仅位于 `tmp/eval-runs/117/`，不提交；durable 产物仅为本 `comparison.md`。
