# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-008-pre-tag-success`

## Test Set / Fixture Version

- Fixture version: issue #117 A2 / 2026-07-19
- Assertions: 5

## Latest Result

**PASS — 5 / 5 assertions passed.** Fresh with-skill 候选在 `v1.2.0` tag 尚不存在时完成 pre-tag 核验，记录两页盖章前值，统一盖章完整集合，只读核对 metadata，并返回不代表已发布的 `ready_for_tag`。

## Assertion Results

| Assertion | Result | Evidence summary |
| --- | --- | --- |
| `accepts_confirmed_version_without_tag` | PASS | 分别记录 base `v1.1.0`、target `release-head` 和维护者确认的 `v1.2.0`，tag 缺失未阻塞。 |
| `verifies_complete_set_and_surfaces` | PASS | 两张 required docs 均 `verified`；#116 handoff、Release Notes、索引、releases.json 和 package version 全部匹配。 |
| `records_pre_stamp_values` | PASS | 报告记录 items 为 `v1.1.0`、status 为 `unverified`，没有新增 `baseline_verified_version`。 |
| `stamps_complete_set_atomically` | PASS | 两页统一更新为 `v1.2.0` 并回读；releases.json 写前写后哈希一致。 |
| `returns_ready_for_tag_not_published` | PASS | 结果为 `ready_for_tag`，明确仅表示可创建 tag，不是已发布或 `release_verified`。 |

## With-Skill Behavior

- 来源：本轮 fresh with-skill，证据位于 `tmp/eval-runs/117/eval-008-pre-tag-success/with_skill/`。
- 候选只写两张受影响 API 页和契约路径 `audit-v1.2.0.md`，没有把 Release Notes/index 纳入统一盖章集合。

## Without-Skill Baseline

- 来源：本轮独立 fresh baseline，使用同一 prompt 与 pristine fixture，证据位于 `tmp/eval-runs/117/eval-008-pre-tag-success/without_skill/`；未复用历史 baseline。
- baseline 也返回成功，但额外改写 Release Notes 与索引的 stamp，并将报告放在 `.eval/pre-tag-audit-report.md`；这显示 skill 对完整影响域边界和报告路径的可观测增益。

## Failures

- 无 assertion failure，无协议缺陷。fixture-authoritative patch 与 release context 足以复现本场景。

## Next Steps

- 保留本结果；pre-tag 统一盖章、#116 handoff 或 `ready_for_tag` 语义变化时重跑。

## Runtime Artifact Policy

- 本轮运行期证据仅位于 `tmp/eval-runs/117/`，不提交；durable 产物仅为本 `comparison.md`。
