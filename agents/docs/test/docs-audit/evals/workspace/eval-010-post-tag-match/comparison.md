# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-010-post-tag-match`

## Test Set / Fixture Version

- Fixture version: A4 / 2026-07-19
- Assertions: 5

## Latest Result

**PASS — 5 / 5 assertions passed.** 本轮 fresh with-skill agent 以可信 handoff 锚定的提交版记录为准，校验记录 blob `38be5ead4d55f0e800444abf16991005a8b2b44f`，解析实际 tag commit/tree，并仅因 tag tree 与 post-stamp tree 完全相等而命中 tree-hash 快路径，最终返回 `release_verified`。

本轮 fresh without-skill baseline 同样通过 5 / 5 assertions，未观察到可识别的语义增益。这不是 baseline 失败，而是 fixture 的 `release-context.md` 已直接给出可信 handoff tuple、tree 相等事实和快路径规则，当前用例区分度不足。

## With-Skill Behavior

- 来源：当前会话中的 fresh with-skill agent；先读取当前 `docs-audit` skill、内部指令、eval prompt/assertions 与 fixture，严格未读取任何 `comparison.md`。
- 行为摘要：通过 handoff 的 `3333333`、tree、record path 与 blob hash 消费提交版记录；解析实际 tag `v1.2.0` 指向 commit `9f8e7d6`，确认其 commit identity 不同于 post-stamp commit，但 tree 均为 `4444444444444444444444444444444444444444`；据 tree-only 快路径建立内容绑定，返回 `release_verified`，且不重新生成或盖章 release 内容。
- 独立复核：当前 fixture 中提交版记录的 Git blob 实算为 `38be5ead4d55f0e800444abf16991005a8b2b44f`；记录内六项精确字节 SHA-256 与对应 fixture 文件一致。

## Without-Skill Baseline

- 来源：当前会话中 `fork_turns=none` 的 fresh agent；只读取本例 prompt、assertions 与 fixture，严禁读取 skill、Agent README、任何 comparison 或历史 baseline。
- 行为摘要：同样满足 5 / 5 assertions，校验提交版记录、解析不同 commit 下的相同 tree、命中 tree-only 快路径并返回 `release_verified`。
- 对比结论：with-skill 与 without-skill 均为满分，未显示技能带来的可识别语义增益；fixture context 已明示 tree hash 相等及应采用快路径。

## Assertion Results

| Assertion | Result | Evidence summary |
| --- | --- | --- |
| `reads_valid_pre_tag_record` | PASS | 依据可信 handoff 的 commit/tree/path/blob 消费提交版记录；blob 实算为 `38be5ead...b44f`，所需 target、四页章前/章后值与哈希、其他版本面、`ready_for_tag` 和时间均存在。 |
| `resolves_actual_tag_commit` | PASS | 解析 `v1.2.0` 到 commit `9f8e7d6` 及 tree `444444...4444`，未只比较 tag 名、版本字符串或 commit identity。 |
| `binds_tag_commit_by_tree_hash` | PASS | tag commit 与 `3333333` 不同，但 tag tree 与 handoff post-stamp tree 完全相等；仅据 tree hash 相等命中快路径。 |
| `returns_release_verified` | PASS | 提交版记录有效、内容绑定和版本事实完整一致，post-tag 结果为 `release_verified`。 |
| `does_not_regenerate_or_restamp` | PASS | 只执行最终复核和 post-tag 证据追加语义，不重新生成 Release Notes、索引、metadata、GitHub Release 内容或文档盖章。 |

## Failures

- 无 assertion failure。
- 评测设计限制：without-skill 也满分，说明本例不能证明技能增益；release context 已直接披露可信读取、tree-only 快路径条件与预期结果。

## Next Steps

- 后续提高 fixture 区分度：只提供可解析的原始 commit/tree/record 证据，避免在 release context 中直接说明 tree 相等即命中快路径，让候选自行选择快路径或一般路径。
- 当 fixture 或 post-tag 内容绑定协议变化时，重新运行 fresh with-skill / without-skill 配对验证。

## Runtime Artifact Policy

- 本轮证据来自当前会话 fresh agents 的消息内结果；未生成、引用或提交任何 runtime artifact，也未复用历史临时路径或 baseline。
- durable 产物仅为本 `comparison.md`。
