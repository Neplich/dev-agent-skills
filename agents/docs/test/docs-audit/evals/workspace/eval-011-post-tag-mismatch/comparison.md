# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-011-post-tag-mismatch`

## Test Set / Fixture Version

- Fixture version: A5 / 2026-07-19
- Assertions: 8

## Latest Result

**PASS — fresh with-skill 8 / 8 assertions passed.** 候选以 handoff 锚定的提交版记录为权威并识别当前路径副本篡改；实际 tag 与目标版本均为 `v1.2.0`，且所有已记录页面和版本面哈希都保持匹配，但 tag tree 因新增 `src/catalog/export-v2.py` 而不同于 post-stamp tree。严格 tree inequality 一律 `blocked`，已记录路径哈希匹配不能降级放行；报告同时给出两条仅由维护者执行、且都以实际待发布内容为新 `target_ref` 的完整 pre-tag 重跑路径。

Fresh without-skill baseline 同样为 **8 / 8**。fixture 已直接说明篡改事实、严格树不等、增量文件、两条救济和 tag 操作边界，提示度高，当前用例未显示可识别的技能增益。

## Assertion Results

| Assertion | With skill | Without skill | Evidence summary |
| --- | --- | --- | --- |
| `reads_anchored_record_not_tampered_copy` | PASS | PASS | 使用等价于 `git show 3333333:docs/site/.meta/audit/audit-v1.2.0.md` 的提交版记录；其 blob 实算为 `bddb69002a60bd4c622b4533407fe840ad06b624`，不同于当前篡改副本 `85ade00ff124774082442d66168104ef26530286`。 |
| `accepts_correct_tag_name_but_checks_tree` | PASS | PASS | 保留 actual tag 与目标版本均为 `v1.2.0` 的事实，同时解析 tag commit/tree，确认 actual tree `555555...5555` 不等于 handoff tree `444444...4444`；未因 tag 名正确放行。 |
| `rejects_unaudited_tag_delta` | PASS | PASS | 所有 recorded paths 哈希均匹配，但 name-status 证据为 `A src/catalog/export-v2.py`；严格 tree inequality 直接 `blocked`，不采用已记录路径重算的降级放行。 |
| `normalizes_mixed_version_forms` | PASS | PASS | actual tag、Release Notes/索引、releases.json 的 `v1.2.0` 与 package version `1.2.0` 按来源校验并规范化为 SemVer `1.2.0`；版本一致不覆盖树漂移。 |
| `invalidates_pre_tag_handoff` | PASS | PASS | tag commit 未绑定到已审计的完整 tree，旧 `ready_for_tag` 不可升级，post-tag 结果为 `blocked`。 |
| `offers_two_maintainer_remedies` | PASS | PASS | 同时提供：(a) 宿主删除或移动错误 tag，以同一 `v1.2.0` 和实际待发布内容为新 `target_ref` 完整重跑，并将旧记录标为 `superseded`；(b) 放弃 `v1.2.0`、确认新版本，并以实际待发布内容为新 `target_ref` 完整重跑。 |
| `allows_pre_tag_reentry_after_selection` | PASS | PASS | 维护者选定救济并记录宿主 tag 状态后，可重新进入完整 pre-tag；tag 曾存在不构成永久阻塞。 |
| `does_not_rewrite_or_operate_tag` | PASS | PASS | docs-audit 只裁定、记录漂移与维护者选择；不修改页面盖章，不重生成 release surfaces，也不自行创建、删除或移动 tag。 |

## With-Skill Behavior

- 来源：本会话 A5 fresh with-skill validation；读取当前 `docs-audit` skill、内部指令、Docs README、同一 prompt/assertions 与 pristine fixture，不读取历史 comparison 作为判定依据。
- 结果：8 / 8。提交版记录抵抗当前副本篡改；版本事实规范化一致，但 actual tag tree 与 anchored post-stamp tree 不等，因此立即 `blocked` 并报告 `A src/catalog/export-v2.py`。
- 严格树模型：所有已记录页面及版本面均保持原哈希；这只可作为诊断证据，不能覆盖 tree inequality，新增未审计代码已足以阻塞。
- 救济边界：两条路径都要求以实际待发布内容为新 `target_ref` 完整重跑 pre-tag；同版本路径还要求宿主维护者处理错误 tag 并 supersede 旧记录。docs-audit 不执行 tag 操作。

## Without-Skill Baseline

- 来源：本会话 A5 fresh without-skill validation；只读取同一 prompt/assertions 与 pristine fixture，不读取 skill、Docs README、comparison 或历史 baseline。
- 结果：8 / 8。也能根据 fixture 的直接提示拒绝 unaudited code delta、返回 `blocked`，并给出两条带新 `target_ref` 要求的维护者救济路径。
- 对比结论：当前用例未显示可识别的技能增益；`.eval/release-context.md` 已直接陈述提交版权威性、recorded paths 全匹配、tree inequality、差异文件、救济和权限边界。

## Failures and Limitations

- With-skill 与 baseline 均无 assertion failure。
- 评测设计限制：fixture 提示度高，无法充分区分候选能否在没有结论提示时自行拒绝“仅重算已记录路径”的降级模型。
- fixture 使用合成 commit/tree identity 与 name-status 证据，只验证严格树绑定协议语义。

## Next Steps

- 后续提高区分度时，保留锚定记录、实际 tree 和 name-status 原始证据，减少 release context 对 `blocked` 结论、两条救济与重入条件的直接说明。
- 当严格树绑定、版本规范化或救济协议变化时，重新运行 fresh with-skill / without-skill 配对验证。

## Runtime Artifact Policy

- 本轮只使用当前会话最终有效 fresh 结果，未复用历史 baseline。
- 未创建、引用或提交 `tmp/`、transcript、candidate output、verdict、timing 或其他运行期产物；durable 产物仅为本 `comparison.md`。
