# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-011-post-tag-mismatch`

## Test Set / Fixture Version

- Fixture version: issue #117 A2 / 2026-07-19
- Assertions: 4

## Latest Result

**PASS — 4 / 4 assertions passed.** Fresh with-skill 候选保留实际 tag `v1.2.1` 与目标 `v1.2.0` 两项冲突事实，判 post-tag `blocked`，不返回 `release_verified`，只追加审计证据而不重写 release 内容。

## Assertion Results

| Assertion | Result | Evidence summary |
| --- | --- | --- |
| `detects_tag_target_mismatch` | PASS | 报告并列保存 `actual_tag: v1.2.1`、commit `abcdef1` 与 `target_release_version: v1.2.0`，明确 mismatch。 |
| `invalidates_pre_tag_handoff` | PASS | 既有 `ready_for_tag` 仅是 v1.2.0 历史 pre-tag 证据，不能升级为当前 tag 的最终验证，结果 `blocked`。 |
| `does_not_return_release_verified` | PASS | 明确未返回 `release_verified`，并给出提供正确 tag 或针对新版本重跑 pre-tag 的待办。 |
| `does_not_rewrite_release_content` | PASS | workspace diff 只追加审计报告；页面 stamp、Release Notes、索引、releases.json、GitHub Release 和 tag 均未改。 |

## With-Skill Behavior

- 来源：本轮 fresh with-skill，证据位于 `tmp/eval-runs/117/eval-011-post-tag-mismatch/with_skill/`。
- 候选完整记录冲突、影响、宿主责任和复核命令，没有用重生成内容掩盖版本不一致。

## Without-Skill Baseline

- 来源：本轮独立 fresh baseline，使用同一 prompt 与 pristine fixture，证据位于 `tmp/eval-runs/117/eval-011-post-tag-mismatch/without_skill/`；未复用历史 baseline。
- baseline 也识别 tag mismatch、blocked 且零写入，但没有向既有审计记录持久化 post-tag 证据。

## Failures

- 无 assertion failure，无 harness 或协议缺陷。

## Next Steps

- 保留本结果；实际 tag mismatch、pre-tag 失效或 post-tag 写入边界变化时重跑。

## Runtime Artifact Policy

- 本轮运行期证据仅位于 `tmp/eval-runs/117/`，不提交；durable 产物仅为本 `comparison.md`。
