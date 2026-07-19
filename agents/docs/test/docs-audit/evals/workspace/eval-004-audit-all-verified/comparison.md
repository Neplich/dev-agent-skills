# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-004-audit-all-verified`

## Test Set / Fixture Version

- Fixture version: issue #117 A2 / 2026-07-19
- Assertions: 4

## Latest Result

**PASS — 4 / 4 assertions passed.** Fresh with-skill 候选在 tag 尚不存在时验证完整两页影响域与全部版本表面，统一盖章为 `v1.1.0`，只读核对 releases.json，写入版本化报告并返回 `ready_for_tag`。

## Assertion Results

| Assertion | Result | Evidence summary |
| --- | --- | --- |
| `verifies_complete_affected_set` | PASS | 两张 change-map required docs 均进入事实层并判 `verified`，无证据缺口。 |
| `stamps_all_pages_together` | PASS | 两页在完整集合通过后同时由 `v1.0.0` 更新为 `v1.1.0` 并回读确认。 |
| `verifies_release_metadata_read_only` | PASS | `releases.json` 与目标一致且写前写后 SHA-256 相同；没有创建或修改 metadata。 |
| `persists_versioned_report` | PASS | `audit-v1.1.0.md` 记录三项输入、两页盖章前值、证据、复核命令和 `ready_for_tag`，并明确非发布状态。 |

## With-Skill Behavior

- 来源：本轮 fresh session `019f7a75-30f5-7ce0-8939-906e3925c96c`，位于 `tmp/eval-runs/117/eval-004-audit-all-verified/with_skill/`。
- 候选严格执行完整集合统一盖章和 #116 metadata 只读边界。

## Without-Skill Baseline

- 来源：本轮独立 fresh session `019f7a78-ed4e-7fb3-bfd8-15483efb59da`，同一 prompt 与 pristine fixture；未复用历史 baseline。
- baseline 也盖章两张 API 页面并保持 releases.json 不变，但报告写入 `.eval/audit-report.md`，不是 docs-audit 契约路径。

## Failures

- 无 assertion failure。合成 refs 使用 fixture patch 与 release context，属于已披露的 harness 限制，不是协议缺陷。

## Next Steps

- 保留本结果；完整集合盖章或 metadata 责任边界变化时重跑。

## Runtime Artifact Policy

- 本轮运行期证据仅位于 `tmp/eval-runs/117/`，不提交；durable 产物仅为本 `comparison.md`。
