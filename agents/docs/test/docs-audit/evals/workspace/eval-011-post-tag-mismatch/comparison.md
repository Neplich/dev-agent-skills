# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-011-post-tag-mismatch`

## Test Set / Fixture Version

- Fixture version: A4 / 2026-07-19
- Assertions: 7

## Latest Result

**PASS — 7 / 7 assertions passed.** 本轮 fresh with-skill agent 以可信 handoff 锚定的提交版记录 blob `bddb69002a60bd4c622b4533407fe840ad06b624` 为权威，识别当前路径副本篡改和 tag tree 漂移，并在一般路径发现 `catalog-status.md` 内容哈希漂移，返回 `blocked`；同时给出两条仅由维护者执行的救济路径，允许满足条件后的 pre-tag 重入，且未操作 tag 或重写 release 内容。

本轮 fresh without-skill baseline 同样通过 7 / 7 assertions，未观察到可识别的语义增益。这不是 baseline 失败，而是 fixture 的 `release-context.md` 已直接给出篡改判断、漂移证据、两条救济和权限边界，当前用例区分度不足。

## With-Skill Behavior

- 来源：当前会话中的 fresh with-skill agent；先读取当前 `docs-audit` skill、内部指令、eval prompt/assertions 与 fixture，严格未读取任何 `comparison.md`。
- 行为摘要：按等价于 `git show 3333333:docs/site/.meta/audit/audit-v1.2.0.md` 的提交版记录读取，拒绝当前篡改副本；保留 tag 名与目标版本均为 `v1.2.0` 的事实，但确认实际 tag tree `555555...5555` 不同于 handoff tree `444444...4444`；逐项重算后发现 `catalog-status.md` 从审计态 `995e20a2...a7e` 漂移为 `bebecd95...de4`，因此阻断旧 `ready_for_tag` 的升级。
- 救济与边界：同时提供“维护者纠正同版本 tag、完整重跑并将旧记录标为 `superseded`”和“放弃该版本、明确确认新版本并完整重跑”两条路径；说明维护者选定路径并记录宿主 tag 状态后可重新进入完整 pre-tag；docs-audit 不创建、删除、移动 tag，也不改写页面盖章或 release surfaces。
- 独立复核：提交版记录 Git blob 实算为 `bddb69002a60bd4c622b4533407fe840ad06b624`；当前副本 blob 为 `85ade00ff124774082442d66168104ef26530286`，两者不同；tagged `catalog-status.md` 的 SHA-256 实算为 `bebecd95f2457acf859e6eb32a556bb4801d3169f8f7e1e5bb87b66c4c1b7de4`，与 manifest 一致且不同于审计态哈希。

## Without-Skill Baseline

- 来源：当前会话中 `fork_turns=none` 的 fresh agent；只读取本例 prompt、assertions 与 fixture，严禁读取 skill、Agent README、任何 comparison 或历史 baseline。
- 行为摘要：同样满足 7 / 7 assertions，抵抗当前副本篡改、识别 catalog-status 漂移、返回 `blocked`、给出两条维护者救济、允许条件式 pre-tag 重入并保持 tag/release 内容只读。
- 对比结论：with-skill 与 without-skill 均为满分，未显示技能带来的可识别语义增益；fixture context 已直接陈述正确结论和完整救济协议。

## Assertion Results

| Assertion | Result | Evidence summary |
| --- | --- | --- |
| `reads_anchored_record_not_tampered_copy` | PASS | 使用 `3333333` 锚定的提交版记录；其 blob 为 `bddb6900...b624`，与当前篡改副本 `85ade00f...286` 不同，未消费伪造字段。 |
| `accepts_correct_tag_name_but_checks_commit` | PASS | 保留 tag 与目标版本均为 `v1.2.0`，同时解析 commit/tree 并确认 tag tree 与 handoff post-stamp tree 不同，未因 tag 名正确放行。 |
| `detects_audited_content_drift` | PASS | 一般路径逐项核对；`catalog-status.md` 从 `995e20a2...a7e` 漂移为 `bebecd95...de4`，其余路径匹配未掩盖冲突。 |
| `invalidates_pre_tag_handoff` | PASS | tag commit 未绑定已审计内容，既有 `ready_for_tag` 不可升级，post-tag 结果为 `blocked`。 |
| `offers_two_maintainer_remedies` | PASS | 同时给出同版本纠正 tag 后完整重跑并 supersede 旧记录，以及放弃版本、确认新版本后完整重跑两条维护者路径。 |
| `allows_pre_tag_reentry_after_selection` | PASS | 说明已判定内容漂移、维护者选定救济且宿主记录 tag 状态后可重新进入完整 pre-tag，tag 曾存在不是永久阻塞。 |
| `does_not_rewrite_or_operate_tag` | PASS | docs-audit 只裁定和记录；不改页面盖章、不重生成 release surfaces，也不自行创建、删除或移动 tag。 |

## Failures

- 无 assertion failure。
- 评测设计限制：without-skill 也满分，说明本例不能证明技能增益；release context 已直接披露权威记录、篡改、内容漂移、救济路径与 tag 操作边界。

## Next Steps

- 后续提高 fixture 区分度：保留提交版/当前副本/tagged bytes 等原始证据，但移除 release context 中对篡改结论、两条救济和重入条件的直接说明，让候选从协议自行推导。
- 当 fixture 或 post-tag 漂移救济协议变化时，重新运行 fresh with-skill / without-skill 配对验证。

## Runtime Artifact Policy

- 本轮证据来自当前会话 fresh agents 的消息内结果；未生成、引用或提交任何 runtime artifact，也未复用历史临时路径或 baseline。
- durable 产物仅为本 `comparison.md`。
