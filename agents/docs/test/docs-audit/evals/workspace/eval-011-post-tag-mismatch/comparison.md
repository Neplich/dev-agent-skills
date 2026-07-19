# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-011-post-tag-mismatch`

## Test Set / Fixture Version

- Fixture version: A3 / 2026-07-19
- Assertions: 5

## Latest Result

**PASS — 5 / 5 assertions passed.** Fresh with-skill 候选没有因实际 tag 名 `v1.2.0` 正确而放行；一般路径识别 `catalog-status.md` 内容哈希漂移，返回 `blocked` 并要求完整重跑 pre-tag。

## Assertion Results

| Assertion | Result | Evidence summary |
| --- | --- | --- |
| `accepts_correct_tag_name_but_checks_commit` | PASS | 保留 tag 与目标版本均为 `v1.2.0` 的事实，同时解析 commit `abcdef1` 并确认其不同于 post-stamp HEAD 且 tree 不同。 |
| `detects_audited_content_drift` | PASS | 逐项检查六条记录路径；`catalog-status.md` 从记录的 `995e20a2...a7e` 漂移为 tag commit 的 `bebecd95...de4`，其他五项匹配没有掩盖冲突。 |
| `invalidates_pre_tag_handoff` | PASS | 明确 tag commit 未绑定已审计内容，旧 `ready_for_tag` 不可升级，结果为 `blocked`。 |
| `does_not_return_release_verified` | PASS | 未返回 `release_verified`，要求针对当前 tag 内容完整重跑 pre-tag，而非只重新确认 tag 名。 |
| `does_not_rewrite_release_content` | PASS | 实际内容差异仅为既有报告追加失败证据；页面 stamp、Release Notes、索引、metadata、tag 与其他 release 内容未改。 |

## With-Skill Behavior

- 来源：本轮 fresh with-skill，使用应用 `docs-audit` 与 Docs README 后的同一 prompt 和 pristine 隔离副本；证据位于 `tmp/eval-runs/128-a3-20260719-213128/with_skill/eval-011-post-tag-mismatch/`。
- judge 回算 `.eval/tag-commit-catalog-status.md` 与 manifest 哈希一致，并确认追加段保留 pre-tag/actual 两值、blocker 和完整重跑要求。

## Without-Skill Baseline

- 来源：本轮 `fork_turns=none` 的独立 fresh baseline，仅读取本例 prompt/assertions 与 pristine fixture；证据位于 `tmp/eval-runs/128-a3-20260719-213128/without_skill/eval-011-post-tag-mismatch/`，未复用历史 baseline。
- baseline 同样满足 5 / 5 assertions，识别同一内容漂移、追加失败证据并保持 release 内容不变；本例未显示行为差距。

## Failures

- 无 assertion failure。tag commit 内容由 fixture manifest 与保留的 exact tagged bytes 表示，属于已披露的合成 Git harness。

## Next Steps

- 保留本结果；tag 内容绑定、漂移处理或 pre-tag 失效规则变化时重跑。

## Runtime Artifact Policy

- 本轮追加后的隔离报告、`candidate-output.md` 与 `run-summary.md` 只保留在 `tmp/eval-runs/128-a3-20260719-213128/`，不提交；durable 产物仅为本 `comparison.md`。
