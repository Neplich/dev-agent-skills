# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-008-pre-tag-success`

## Test Set / Fixture Version

- Fixture version: A4 / 2026-07-19
- Assertions: 7

## Latest Result

**PASS — 7 / 7 assertions passed.** 本轮 fresh with-skill agent 将完整影响域和 release surfaces 判为 `verified`，把两张 API 页、Release Notes 页及其 Markdown 索引统一盖章为 `v1.2.0`，并确认四页盖章与成功记录由同一普通 post-stamp commit 引入、可信外部 handoff 锚定提交版记录，最终返回不代表已发布的 `ready_for_tag`。

本轮 fresh without-skill baseline 同样通过 7 / 7 assertions，未观察到可识别的语义增益。这不是 baseline 失败，而是 fixture 的 `release-context.md` 已直接陈述关键协议和预期操作，当前用例区分度不足。

## With-Skill Behavior

- 来源：当前会话中的 fresh with-skill agent；先读取当前 `docs-audit` skill、内部指令、eval prompt/assertions 与 fixture，严格未读取任何 `comparison.md`。
- 行为摘要：分别解析 `base_ref: v1.1.0`、`target_ref: release-head`/`2222222` 与维护者确认的 `target_release_version: v1.2.0`；核对两张 API 页、#116 handoff、Release Notes、索引、只读 releases.json 和 package version；记录四页章前值并统一盖章；把四页和成功记录放入同一普通 commit，通过 commit/tree/record path/blob 的外部 handoff anchor 回读提交版记录；结果为 `ready_for_tag`，明确不表示已发布。

## Without-Skill Baseline

- 来源：当前会话中 `fork_turns=none` 的 fresh agent；只读取本例 prompt、assertions 与 fixture，严禁读取 skill、Agent README、任何 comparison 或历史 baseline。
- 行为摘要：同样满足 7 / 7 assertions，完成四页统一盖章、同 commit 边界、可信外部锚点与 `ready_for_tag` 语义判断。
- 对比结论：with-skill 与 without-skill 均为满分，未显示技能带来的可识别语义增益；主要原因是 fixture context 已直接给出统一盖章集、同 commit 要求、外部 handoff tuple 及状态语义。

## Assertion Results

| Assertion | Result | Evidence summary |
| --- | --- | --- |
| `accepts_confirmed_version_without_tag` | PASS | 分别记录 base、target 与维护者确认的 `v1.2.0`；同名 tag 缺失未阻塞 pre-tag。 |
| `verifies_complete_set_and_surfaces` | PASS | change-map 要求的两张 API 页及 #116 handoff、Release Notes、索引、releases.json、package version 全部对齐并通过事实核验。 |
| `records_pre_stamp_values` | PASS | 四页章前值为 items=`v1.1.0`、status=`unverified`、Release Notes=`unverified`、索引=`v1.1.0`，且未引入 `baseline_verified_version`。 |
| `stamps_complete_set_atomically` | PASS | 两张 API 页、Release Notes 与索引统一更新为 `v1.2.0` 并回读；releases.json 保持只读。 |
| `commits_stamp_and_record_together` | PASS | 四页完整盖章集和成功 `audit-v1.2.0.md` 由同一普通 post-stamp commit 引入，没有拆分或仅锚定工作区。 |
| `persists_stamp_and_content_evidence` | PASS | 提交版记录包含四页章前/章后值和精确字节 SHA-256、其他版本面哈希、audited target commit、`ready_for_tag` 与时间；外部 handoff 持久化 commit SHA、tree、record path 与 blob hash。 |
| `returns_ready_for_tag_not_published` | PASS | pre-tag 结果为 `ready_for_tag`，明确只表示可创建 tag，不表示版本已发布或已完成 post-tag 验证。 |

## Failures

- 无 assertion failure。
- 评测设计限制：without-skill 也满分，说明本例不能证明技能增益；fixture 将关键协议直接写入 release context，使 baseline 可以逐项复述并执行预期行为。

## Next Steps

- 后续提高 fixture 区分度：减少 release context 中对正确流程和结论的直接提示，改为提供更原始的 Git/文件证据，让候选自行推导统一盖章集、commit 边界、可信锚点及阶段状态。
- 当上述 fixture 调整或 pre-tag 协议变化时，重新运行 fresh with-skill / without-skill 配对验证。

## Runtime Artifact Policy

- 本轮证据来自当前会话 fresh agents 的消息内结果；未生成、引用或提交任何 runtime artifact，也未复用历史临时路径或 baseline。
- durable 产物仅为本 `comparison.md`。
