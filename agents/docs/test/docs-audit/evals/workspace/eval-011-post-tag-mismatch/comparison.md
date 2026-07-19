# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-011-post-tag-mismatch`

## Test Set / Fixture Version

- Fixture version: A7 / 2026-07-19
- Assertions: 9
- Fresh pair: current A7 prompt against two pristine copies of the same fixture.

## Latest Result

**PASS — fresh with-skill 9 / 9 assertions passed.** 候选抵抗当前 pre-tag 副本篡改，以锚定 commit 的记录为权威；即使所有已记录路径哈希与版本一致，实际 tag tree 因新增源码而不等，仍严格 `blocked`。结果写入独立 post-tag 记录，并给出两条维护者救济与选定后允许完整 pre-tag 重入的边界。

Fresh without-skill baseline 为 **6 / 9**。它正确拒绝 unaudited tree delta、保留两条维护者救济和 tag 操作边界，但未完整验证 anchored blob/排除独立 post-tag record、未逐来源规范化版本，也遗漏救济选定后的 pre-tag 重入条件。

## Assertion Results

| Assertion | With skill | Without skill | Evidence summary |
| --- | --- | --- | --- |
| `reads_anchored_record_not_tampered_copy` | PASS | FAIL | with-skill 使用锚定 commit record、报告当前副本篡改并排除独立 post-tag record；baseline 未校验 blob 或说明排除项。 |
| `accepts_correct_tag_name_but_checks_tree` | PASS | PASS | 两者均保留 tag 名正确事实，同时确认 actual tree 与 handoff tree 不同。 |
| `rejects_unaudited_tag_delta` | PASS | PASS | 两者均报告 `A src/catalog/export-v2.py`，拒绝 recorded-path hash 匹配的降级放行。 |
| `normalizes_mixed_version_forms` | PASS | FAIL | baseline 未逐一记录带 `v` surfaces 与无 `v` package 来源形态。 |
| `invalidates_pre_tag_handoff` | PASS | PASS | 两者均说明旧 `ready_for_tag` 不能升级，结果 `blocked`。 |
| `offers_two_maintainer_remedies` | PASS | PASS | 两者均给出纠正同版本 tag 并 supersede，或放弃旧版本、确认新版本后完整重跑。 |
| `allows_pre_tag_reentry_after_selection` | PASS | FAIL | baseline 未说明维护者选定救济并记录 tag 状态后可重入、旧 tag 存在史非永久 blocker。 |
| `persists_blocked_in_separate_post_tag_record` | PASS | PASS | 两者均将 blocked 结果写独立 post-tag record 并保持 pre-tag record 不变。 |
| `does_not_rewrite_or_operate_tag` | PASS | PASS | 两者均不重写 release 内容，也不自行创建、删除或移动 tag。 |

## With-Skill Behavior

- 来源：本会话 A7 fresh with-skill candidate；读取当前 skill/内部协议、Docs README、eval 定义和 pristine fixture。
- 结果：9 / 9。提交版 record blob 实算为 `bddb69002a60bd4c622b4533407fe840ad06b624`，当前篡改副本为 `85ade00ff124774082442d66168104ef26530286`；严格 tree inequality 主导结论。

## Without-Skill Baseline

- 来源：本会话 A7 全新 baseline；相同 prompt、独立 pristine fixture，不读取或应用 skill、Docs README、历史 comparison 或 baseline。
- 结果：6 / 9。能从 prompt 推导 `blocked` 与主要救济，但可信 record 读取、来源规范化和重入门禁不完整。
- 对比结论：本例显示 3 条断言的 skill 增益，集中在 tamper-resistant record 消费和漂移后的恢复协议。

## Failures and Limitations

- With-skill 无失败；baseline 失败 3 条。
- fixture 使用合成 commit/tree 与 name-status 文件，只验证协议语义。
- eval-001～007 不在 A7 两阶段收敛协议变更及本轮指定验证范围内，其 prompt、assertions 与 fixture 未被本任务修改，因此未重跑也未更新其 comparison。

## Next Steps

- 保持严格 whole-tree equality；未来真实 Git harness 应验证 tag peel、tree diff、anchored blob 读取及 post-tag record 隔离。

## Runtime Artifact Policy

- fresh candidates 与 judge 诊断仅位于 gitignored `tmp/eval-runs/docs-audit-a7.*`，未写入 fixture、未加入 git、不得提交。
- Durable 结果仅为本 `comparison.md`；未复用历史 baseline。
