# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-010-post-tag-match`

## Test Set / Fixture Version

- Fixture version: issue #117 A2 / 2026-07-19
- Assertions: 4

## Latest Result

**PASS — 4 / 4 assertions passed.** Fresh with-skill 候选读取仍有效的 pre-tag 记录，确认实际 tag 与所有版本表面均为 `v1.2.0`，仅追加 post-tag 证据并返回 `release_verified`。

## Assertion Results

| Assertion | Result | Evidence summary |
| --- | --- | --- |
| `reads_valid_pre_tag_record` | PASS | 读取 base、target、目标版本、两页盖章前值、统一盖章、事实证据与 `ready_for_tag`，确认记录仍有效。 |
| `matches_actual_tag_and_surfaces` | PASS | 实际 tag、#116 handoff、Release Notes、索引、releases.json 和 package version 均精确匹配 `v1.2.0`。 |
| `returns_release_verified` | PASS | 无 blocker 时 post-tag 结果为 `release_verified`，没有退回 `ready_for_tag`。 |
| `does_not_regenerate_or_restamp` | PASS | 只修改既有审计报告；页面、Release Notes、索引、metadata、宿主版本和 tag 均未改。 |

## With-Skill Behavior

- 来源：本轮 fresh with-skill，证据位于 `tmp/eval-runs/117/eval-010-post-tag-match/with_skill/`。
- workspace diff 仅为 `audit-v1.2.0.md` 的 post-tag 追加段，包含实际 tag、全部核对表面、结果和复核命令。

## Without-Skill Baseline

- 来源：本轮独立 fresh baseline，使用同一 prompt 与 pristine fixture，证据位于 `tmp/eval-runs/117/eval-010-post-tag-match/without_skill/`；未复用历史 baseline。
- baseline 也确认所有版本事实匹配且零越界写入，但没有把 post-tag 证据持久化回既有审计记录，也未显式输出契约状态名 `release_verified`。

## Failures

- 无 assertion failure，无 harness 或协议缺陷。

## Next Steps

- 保留本结果；post-tag 持久化或 `release_verified` 条件变化时重跑。

## Runtime Artifact Policy

- 本轮运行期证据仅位于 `tmp/eval-runs/117/`，不提交；durable 产物仅为本 `comparison.md`。
