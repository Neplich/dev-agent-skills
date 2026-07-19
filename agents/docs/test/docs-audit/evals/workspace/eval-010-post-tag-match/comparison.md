# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-010-post-tag-match`

## Test Set / Fixture Version

- Fixture version: A7 / 2026-07-19
- Assertions: 7
- Fresh pair: current A7 prompt against two pristine copies of the same fixture.

## Latest Result

**PASS — fresh with-skill 7 / 7 assertions passed.** 候选从可信 handoff 锚定 commit 读取并校验提交版 pre-tag record；实际 tag commit 虽不同，但 tree hash 完全相等，版本来源规范化一致，因此仅在独立 post-tag 记录中返回 `release_verified`，不重生成或重盖章。

Fresh without-skill baseline 为 **5 / 7**。它正确使用 tree-hash 快路径、阶段状态和独立记录，但未验证 handoff blob 与 pre-tag record 必填证据，也把 Release Notes/索引/releases.json 的来源核对概括成“documentation”。

## Assertion Results

| Assertion | With skill | Without skill | Evidence summary |
| --- | --- | --- | --- |
| `reads_valid_pre_tag_record` | PASS | FAIL | with-skill 使用 `git show 3333333:...`、校验 blob/path/tree 和必填记录字段；baseline 仅泛称使用 handoff record。 |
| `resolves_actual_tag_commit` | PASS | PASS | 两者均解析 tag commit `9f8e7d6` 与实际 tree。 |
| `binds_tag_commit_by_tree_hash` | PASS | PASS | 两者均在 commit 不同、tree 相等时仅以 tree equality 建立内容绑定。 |
| `normalizes_mixed_version_forms` | PASS | FAIL | baseline 未逐一核对 Release Notes、索引和 releases.json 的来源形态。 |
| `returns_release_verified` | PASS | PASS | 两者均在内容和版本一致时返回 post-tag `release_verified`。 |
| `persists_separate_post_tag_record` | PASS | PASS | 两者均写独立 `audit-v1.2.0-post-tag.md` 并保持 pre-tag record 不变。 |
| `does_not_regenerate_or_restamp` | PASS | PASS | 两者均只复核，不重新生成 release surface 或盖章。 |

## With-Skill Behavior

- 来源：本会话 A7 fresh with-skill candidate；读取当前 skill/内部协议、Docs README、eval 定义和 pristine fixture。
- 结果：7 / 7。提交版 record blob 实算为 `38be5ead4d55f0e800444abf16991005a8b2b44f`，记录中的四页与 releases.json/package.json SHA-256 也与 fixture 精确字节一致。

## Without-Skill Baseline

- 来源：本会话 A7 全新 baseline；相同 prompt、独立 pristine fixture，不读取或应用 skill、Docs README、历史 comparison 或 baseline。
- 结果：5 / 7。高层结论正确，但缺 anchored record 消费门禁和逐来源版本证据。
- 对比结论：本例显示 2 条断言的 skill 增益，集中在提交版记录可信性与版本面完整性。

## Failures and Limitations

- With-skill 无失败；baseline 失败 2 条。
- fixture 使用合成 commit/tree；没有真实 tag peel 操作。
- eval-001～007 不在 A7 两阶段收敛协议变更及本轮指定验证范围内，其 prompt、assertions 与 fixture 未被本任务修改，因此未重跑也未更新其 comparison。

## Next Steps

- 后续接入 Git harness 时，直接验证 tag peel、tree equality、`git show` blob 与独立 post-tag record 写入。

## Runtime Artifact Policy

- fresh candidates 与 judge 诊断仅位于 gitignored `tmp/eval-runs/docs-audit-a7.*`，未写入 fixture、未加入 git、不得提交。
- Durable 结果仅为本 `comparison.md`；未复用历史 baseline。
