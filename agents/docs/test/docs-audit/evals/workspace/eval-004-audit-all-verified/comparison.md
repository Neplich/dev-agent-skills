# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-004-audit-all-verified`

## Test Set / Fixture Version

- Fixture version: A5 / 2026-07-19
- Assertions: 5

## Latest Result

**PASS — fresh with-skill 5 / 5 assertions passed.** 当前 skill、assertions 与 fixture 一致要求：完整影响域事实核验通过后，两张 API 页、Release Notes 页和 Markdown 索引组成四页统一盖章集；带 `v` 的目标版本/Release Notes/索引/releases.json 与无 `v` 的 package version 先按来源校验，再规范化为同一 SemVer；成功记录与完整盖章由同一普通 post-stamp commit 引入并由外部 handoff 锚定，最终返回不表示已发布的 `ready_for_tag`。

Fresh without-skill baseline 为 **3 / 5**；`stamps_all_pages_together` 与 `persists_versioned_report` 未通过。with-skill 对完整统一盖章范围和成功记录边界体现了可观测增益。

## Assertion Results

| Assertion | With skill | Without skill | Evidence summary |
| --- | --- | --- | --- |
| `verifies_complete_affected_set` | PASS | PASS | `src/catalog/routes.txt` 命中 change-map 的两张 required docs；两张 API 页均有当前路由事实支持并可判为 `verified`。 |
| `stamps_all_pages_together` | PASS | FAIL | with-skill 只在完整集合通过后统一更新两张 API 页、`v1.1.0.md` 与 Markdown 索引；baseline 未完整覆盖四页统一盖章集。 |
| `verifies_release_metadata_read_only` | PASS | PASS | 两路均核对 `docs/site/.meta/releases.json` 的 `v1.1.0`，且保持 #116 所属 metadata 只读。 |
| `normalizes_mixed_version_forms` | PASS | PASS | fixture 的目标版本、Release Notes/索引/releases.json 为 `v1.1.0`，`package.json` 为 `1.1.0`；按来源形态校验后均规范化为 SemVer `1.1.0`。 |
| `persists_versioned_report` | PASS | FAIL | with-skill 完整记录四页章前/章后值、精确字节哈希、版本面证据、audited target、结果时间和 `ready_for_tag`，并遵守同 commit 与外部 handoff anchor；baseline 的成功记录未完整满足该契约。 |

## With-Skill Behavior

- 来源：本会话 A5 fresh with-skill validation 的最终有效复跑；读取当前 `docs-audit` skill、内部指令、Docs README、同一 prompt/assertions 与 pristine fixture，不复用历史 baseline。
- 结果：5 / 5。完整影响域和 release surfaces 均通过；四页统一盖章与成功记录处于同一普通 post-stamp commit 边界，可信 handoff 锚定 commit SHA、tree hash、record path 和 blob hash；`releases.json` 保持只读。
- 版本处理：保留各来源要求的原始形态，并将 `v1.1.0` 与 `1.1.0` 规范化为同一 SemVer 后判等。

## Without-Skill Baseline

- 来源：本会话 A5 fresh without-skill validation 的最终有效复跑；只读取同一 prompt/assertions 与 pristine fixture，不读取 skill、Docs README、comparison 或历史 baseline。
- 结果：3 / 5。通过完整影响域、只读 release metadata 与混合版本规范化；未完整覆盖四页统一盖章集，也未形成满足全部字段、同 commit 边界和可信外部锚点要求的成功记录。
- 对比结论：with-skill 补足了 baseline 在统一盖章范围和 durable success record 上的两个协议缺口。

## Failures and Limitations

- With-skill 无 assertion failure。
- Baseline 失败项：`stamps_all_pages_together`、`persists_versioned_report`。
- fixture 使用合成 refs 与预期 handoff identity；验证的是协议语义，不代表对真实宿主仓库创建了 post-stamp commit。

## Next Steps

- 保留本结果；当统一盖章集合、版本规范化表或成功记录/外部 handoff 协议变化时，重新运行 fresh with-skill / without-skill 配对验证。

## Runtime Artifact Policy

- 本文件只记录本会话最终有效 fresh 结论；修正前的 eval-004 结果不作为证据，也未复用历史 baseline。
- 未创建、引用或提交 `tmp/`、transcript、candidate output、verdict、timing 或其他运行期产物；durable 产物仅为本 `comparison.md`。
