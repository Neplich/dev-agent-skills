# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-008-pre-tag-success`

## Test Set / Fixture Version

- Fixture version: A3 / 2026-07-19
- Assertions: 6

## Latest Result

**PASS — 6 / 6 assertions passed.** Fresh with-skill 候选在 tag 尚不存在时完成完整 pre-tag 核验，将两页统一盖章为 `v1.2.0` 并回读，把盖章结果及页面/版本面哈希原子持久化后返回不代表已发布的 `ready_for_tag`。

## Assertion Results

| Assertion | Result | Evidence summary |
| --- | --- | --- |
| `accepts_confirmed_version_without_tag` | PASS | 分别记录 base `v1.1.0`、target `release-head`/`2222222` 与维护者确认的 `v1.2.0`，未因同名 tag 缺失阻塞。 |
| `verifies_complete_set_and_surfaces` | PASS | 两张 change-map required docs 均判 `verified`；#116 handoff、Release Notes、索引、releases.json 与 package version 全部对齐 `v1.2.0`。 |
| `records_pre_stamp_values` | PASS | 报告记录 items=`v1.1.0`、status=`unverified`，运行副本未新增 `baseline_verified_version`。 |
| `stamps_complete_set_atomically` | PASS | 两页在完整集合通过后同时更新为 `v1.2.0` 并回读；releases.json 与 pristine fixture 无差异。 |
| `persists_stamp_and_content_evidence` | PASS | 同一报告包含两页清单、章前/章后值、页面与 #116 handoff、Release Notes、索引、metadata、package 的精确字节 SHA-256、target commit、post-stamp HEAD、结果时间和两类 read-back；judge 回算全部哈希匹配。 |
| `returns_ready_for_tag_not_published` | PASS | 结果为 `ready_for_tag`，并明确只表示可以创建 tag，不表示发布或 post-tag `release_verified`。 |

## With-Skill Behavior

- 来源：本轮 fresh with-skill，使用应用 `docs-audit` 与 Docs README 后的同一 prompt 和 pristine 隔离副本；证据位于 `tmp/eval-runs/128-a3-20260719-213128/with_skill/eval-008-pre-tag-success/`。
- 实际变更仅为两张受影响 API 页面统一盖章、创建同版本审计记录及运行期输出；未改写 Release Notes、索引或 metadata。

## Without-Skill Baseline

- 来源：本轮 `fork_turns=none` 的独立 fresh baseline，仅读取本例 prompt/assertions 与 pristine fixture；证据位于 `tmp/eval-runs/128-a3-20260719-213128/without_skill/eval-008-pre-tag-success/`，未复用历史 baseline。
- baseline 也完成 6 / 6 assertions：统一盖章、完整记录断言明确要求的页面与版本面哈希，并保持 metadata 只读；本例未显示行为差距。

## Failures

- 无 assertion failure。fixture 以合成 commit 和文件证据模拟宿主 pre-tag 状态，证据范围已披露。

## Next Steps

- 保留本结果；原子成功回写、内容哈希集合或 `ready_for_tag` 语义变化时重跑。

## Runtime Artifact Policy

- 本轮 `candidate-output.md`、`run-summary.md`、隔离盖章页面与审计报告只保留在 `tmp/eval-runs/128-a3-20260719-213128/`，不提交；durable 产物仅为本 `comparison.md`。
