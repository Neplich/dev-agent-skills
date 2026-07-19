# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-010-post-tag-match`

## Test Set / Fixture Version

- Fixture version: A3 / 2026-07-19
- Assertions: 5

## Latest Result

**PASS — 5 / 5 assertions passed.** Fresh with-skill 候选解析实际 tag commit，在 HEAD 与 tree 快路径均不成立时按记录路径逐项执行内容哈希一般路径，六项全部匹配并返回 `release_verified`。

## Assertion Results

| Assertion | Result | Evidence summary |
| --- | --- | --- |
| `reads_valid_pre_tag_record` | PASS | 严格消费 audited target commit、post-stamp HEAD、两页清单及章前/章后值、六项哈希、`ready_for_tag` 与结果时间，没有从当前文件补造字段。 |
| `resolves_actual_tag_commit` | PASS | 解析 `v1.2.0` 到 `9f8e7d6`，记录其不同于 `3333333` 且 tree 不同，未只比较 tag 名。 |
| `binds_tag_commit_by_content` | PASS | 对两张 API 页面、Release Notes、索引、releases.json 与 package 六条记录路径逐项比对 tag-commit SHA-256，路径集合和哈希全部匹配 pre-tag 记录。 |
| `returns_release_verified` | PASS | 内容绑定及版本事实完整一致，post-tag 结果为 `release_verified`。 |
| `does_not_regenerate_or_restamp` | PASS | 实际内容差异仅为既有审计报告追加 post-tag 证据；页面、notes、索引、metadata 与 stamps 未改。 |

## With-Skill Behavior

- 来源：本轮 fresh with-skill，使用应用 `docs-audit` 与 Docs README 后的同一 prompt 和 pristine 隔离副本；证据位于 `tmp/eval-runs/128-a3-20260719-213128/with_skill/eval-010-post-tag-match/`。
- judge 将 tag manifest 的六个路径/哈希逐项与 pre-tag 记录及追加段核对，全部一致。

## Without-Skill Baseline

- 来源：本轮 `fork_turns=none` 的独立 fresh baseline，仅读取本例 prompt/assertions 与 pristine fixture；证据位于 `tmp/eval-runs/128-a3-20260719-213128/without_skill/eval-010-post-tag-match/`，未复用历史 baseline。
- baseline 同样满足 5 / 5 assertions，走一般内容绑定路径、追加证据并返回 `release_verified`；本例未显示行为差距。

## Failures

- 无 assertion failure。tag commit 内容由 fixture 的 exact-byte SHA-256 manifest 表示，属于已披露的合成 Git harness。

## Next Steps

- 保留本结果；tag peel、快/一般路径选择或记录字段集合变化时重跑。

## Runtime Artifact Policy

- 本轮追加后的隔离报告、`candidate-output.md` 与 `run-summary.md` 只保留在 `tmp/eval-runs/128-a3-20260719-213128/`，不提交；durable 产物仅为本 `comparison.md`。
