# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-008-pre-tag-success`

## Test Set / Fixture Version

- Fixture version: A6 / 2026-07-19
- Assertions: 9

## Latest Result

**PASS — fresh with-skill 9 / 9 assertions passed.** 完整影响域、Release Notes/索引、只读 releases.json 与宿主版本事实全部通过；`v1.2.0` 与 `1.2.0` 按来源校验并规范化为同一 SemVer；四页统一盖章、回读、内容哈希、同一普通 post-stamp commit、可信外部 handoff anchor，以及 `target_ref` 到盖章后 commit 的完整差异收敛证据均满足当前协议，结果为不表示已发布的 `ready_for_tag`。

Fresh without-skill baseline 同样为 **9 / 9**。该满分不表示技能无效，而是 fixture 的 release context 与 assertions 对统一盖章集、版本规范化、commit 边界、handoff tuple 和差异收敛结论提示度很高，当前用例未显示可量化的 skill 增益。

## Assertion Results

| Assertion | With skill | Without skill | Evidence summary |
| --- | --- | --- | --- |
| `accepts_confirmed_version_without_tag` | PASS | PASS | 分别记录 `base_ref`、`target_ref` 与维护者确认的 `v1.2.0`；同名 tag 缺失不阻塞 pre-tag。 |
| `verifies_complete_set_and_surfaces` | PASS | PASS | 两张 API 页、#116 handoff、Release Notes、索引、releases.json 与 package version 全部纳入核验，Release Markdown 也先完成事实核验。 |
| `normalizes_mixed_version_forms` | PASS | PASS | 带 `v` 的目标版本/Release Notes/索引/releases.json 与无 `v` 的 package version 均满足来源形态，并规范化为 SemVer `1.2.0` 后判等。 |
| `records_pre_stamp_values` | PASS | PASS | 四页章前值为 items=`v1.1.0`、status=`unverified`、Release Notes=`unverified`、索引=`v1.1.0`，未新增 baseline frontmatter。 |
| `stamps_complete_set_atomically` | PASS | PASS | 两张 API 页、`v1.2.0.md` 与 Markdown 索引统一更新为 `v1.2.0` 并回读；releases.json 保持只读。 |
| `commits_stamp_and_record_together` | PASS | PASS | 完整四页盖章集与成功 `audit-v1.2.0.md` 由同一普通 post-stamp commit 引入，未拆分或仅锚定工作区。 |
| `persists_stamp_and_content_evidence` | PASS | PASS | 提交版记录包含四页章前/章后值与精确字节 SHA-256、其他版本面哈希、audited target、结果时间和 `ready_for_tag`；可信 handoff 锚定 commit/tree/path/blob。 |
| `records_post_stamp_diff_convergence` | PASS | PASS | 完整文件清单只含四张授权盖章页与审计记录；四页逐文件内容差异都只修改 `last_verified_version` 字段行，记录持久化 passed 结论。 |
| `returns_ready_for_tag_not_published` | PASS | PASS | pre-tag 结果为 `ready_for_tag`，且明确只表示可创建 tag，不表示发布完成或 `release_verified`。 |

## With-Skill Behavior

- 来源：本会话 A6 fresh with-skill validation；读取当前 `docs-audit` skill、内部指令、Docs README、同一 prompt/assertions 与 pristine fixture，不读取历史 comparison 作为判定依据。
- 结果：9 / 9。执行完整核验、来源形态与 SemVer 规范化、四页统一盖章与回读，并满足同 commit 成功记录、外部 handoff anchor 和盖章 commit 差异收敛契约。

## Without-Skill Baseline

- 来源：本会话 A6 fresh without-skill validation；只读取同一 prompt/assertions 与 pristine fixture，不读取 skill、Docs README、comparison 或历史 baseline。
- 结果：9 / 9。也能从 fixture 的直接提示复现统一盖章、版本规范化、同 commit 边界、可信外部锚点、完整差异清单及阶段状态。
- 对比结论：当前用例未显示断言级差异；主要限制是 `.eval/release-context.md` 已直接给出 unified stamp set、commit 要求、handoff tuple 和差异收敛成功事实。

## Failures and Limitations

- With-skill 与 baseline 均无 assertion failure。
- 评测设计限制：fixture 提示度高，满分 baseline 降低了用例对技能独立推导能力的区分度。
- fixture 使用合成 refs 与预期 commit/tree identity，只验证只读协议模拟；未实际执行 commit、`git show`、记录持久化或哈希链路。

## Next Steps

- 后续提高区分度时，保留原始版本与文件证据，减少 release context 对统一盖章集、commit 边界、handoff tuple 和收敛结论的直接陈述。
- 当 fixture 或 pre-tag 协议变化时，重新运行 fresh with-skill / without-skill 配对验证。

## Runtime Artifact Policy

- 本轮只使用当前会话最终有效 fresh 结果，未复用历史 baseline。
- 未创建、引用或提交 `tmp/`、transcript、candidate output、verdict、timing 或其他运行期产物；durable 产物仅为本 `comparison.md`。
