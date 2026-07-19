# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-010-post-tag-match`

## Test Set / Fixture Version

- Fixture version: A5 / 2026-07-19
- Assertions: 6

## Latest Result

**PASS — fresh with-skill 6 / 6 assertions passed.** 候选从可信 handoff 锚定的 post-stamp commit 读取并校验提交版记录，解析实际 tag commit/tree；虽然 commit identity 不同，但实际 tag tree 与 handoff tree 完全相等，因此仅按严格 tree equality 建立内容绑定。实际 tag/Release Notes/索引/releases.json 的 `v1.2.0` 与 package version `1.2.0` 规范化为同一 SemVer，最终返回 `release_verified`，且不重新生成或盖章内容。

Fresh without-skill baseline 同样为 **6 / 6**。fixture 已直接披露 handoff tuple、相同 tree、混合版本事实和快路径预期，提示度高，当前用例未表现可识别的技能增益。

## Assertion Results

| Assertion | With skill | Without skill | Evidence summary |
| --- | --- | --- | --- |
| `reads_valid_pre_tag_record` | PASS | PASS | 使用 handoff 的 `3333333`、tree、record path 与 blob 校验提交版记录；fixture 记录 blob 实算为 `38be5ead4d55f0e800444abf16991005a8b2b44f`，所需成功字段齐全。 |
| `resolves_actual_tag_commit` | PASS | PASS | 解析实际 `v1.2.0` 到 commit `9f8e7d6` 及 tree `4444444444444444444444444444444444444444`，未只比较 tag 名或 commit identity。 |
| `binds_tag_commit_by_tree_hash` | PASS | PASS | tag commit 与 post-stamp commit 不同，但 tree 完全相等；仅据 tree equality 命中快路径并建立内容绑定。 |
| `normalizes_mixed_version_forms` | PASS | PASS | actual tag、Release Notes/索引、releases.json 的 `v1.2.0` 与 package version `1.2.0` 先满足来源形态，再规范化为 SemVer `1.2.0`。 |
| `returns_release_verified` | PASS | PASS | 锚定记录、严格树绑定和版本事实均完整一致，post-tag 结果为 `release_verified`。 |
| `does_not_regenerate_or_restamp` | PASS | PASS | 只做最终复核和 post-tag 证据追加，不重新生成 Release Notes、索引、metadata、GitHub Release 内容或文档盖章。 |

## With-Skill Behavior

- 来源：本会话 A5 fresh with-skill validation；读取当前 `docs-audit` skill、内部指令、Docs README、同一 prompt/assertions 与 pristine fixture，不读取历史 comparison 作为判定依据。
- 结果：6 / 6。严格以提交版记录和 handoff tree 为权威；tree 相等而 commit 不同仍可通过，commit identity 相等本身不能放行；版本源规范化后返回 `release_verified`。
- 独立证据复核：提交版记录 blob 为 `38be5ead4d55f0e800444abf16991005a8b2b44f`；记录内四页与 releases.json/package.json 的 SHA-256 均与 fixture 精确字节一致。

## Without-Skill Baseline

- 来源：本会话 A5 fresh without-skill validation；只读取同一 prompt/assertions 与 pristine fixture，不读取 skill、Docs README、comparison 或历史 baseline。
- 结果：6 / 6。也能根据 fixture 明示的 tree equality、handoff tuple、版本值与只读边界返回 `release_verified`。
- 对比结论：当前用例未显示可识别的技能增益；`.eval/release-context.md` 已直接说明 tree-hash 快路径及预期结果。

## Failures and Limitations

- With-skill 与 baseline 均无 assertion failure。
- 评测设计限制：fixture 提示度高，无法充分区分是否能从更原始的 Git 证据独立推导严格树快路径。
- fixture 使用合成 commit/tree identity，只验证协议语义。

## Next Steps

- 后续提高区分度时，只提供可解析的 commit、tree、record 与版本原始事实，减少对“tree 相等即快路径”和结果状态的直接说明。
- 当 post-tag 树绑定或版本规范化协议变化时，重新运行 fresh 配对验证。

## Runtime Artifact Policy

- 本轮只使用当前会话最终有效 fresh 结果，未复用历史 baseline。
- 未创建、引用或提交 `tmp/`、transcript、candidate output、verdict、timing 或其他运行期产物；durable 产物仅为本 `comparison.md`。
