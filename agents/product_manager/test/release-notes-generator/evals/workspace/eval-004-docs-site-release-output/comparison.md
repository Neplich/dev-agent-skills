# Skill Eval Comparison

## Evaluation Target

- Agent: `product_manager`
- Skill: `release-notes-generator`
- Eval: `eval-004-docs-site-release-output`
- Test case: 文档站与 GitHub Release 双输出边界

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: `eval-004-docs-site-release-output-r3`
- Fixture snapshot: `src/release/version.txt` 确认 `v1.4.0` 与候选变更；文档站包含 release-notes 索引、仍指向 `v1.3.0` 的 API 页面及 change-map，但不包含 Git 历史、compare、PR、changelog 归档或根索引。
- Eval metadata: `eval_metadata.json` 当前工作树版本；本次执行以 `evals.json` 中 `eval-004-docs-site-release-output` 的 prompt、expected output 与 5 条 assertions 为判定真源。
- Runner: 2026-07-19 fresh Codex subagent validation；with-skill 与 without-skill 使用同一 eval prompt 和同一份净化 fixture。

## Latest Result

**PASS** — fresh with-skill 结果满足 5/5 assertions：PM 保留客户公告、GitHub Release 正文与 issue #120 完成前的 tag-aware/draft/publish 边界；站内 `docs/site/release-notes/v1.4.0.md` 以包含版本、scope、证据、宿主和 required output 的 packet 交给 `docs-agent:release-notes-generator`；版本化 changelog 与根索引仍是独立发布门禁。fresh without-skill baseline 仅满足 1/5，证明新 skill 边界提供了实质行为增益。

## Assertion Results

| Assertion | With skill | Without skill | Evidence summary |
| --- | --- | --- | --- |
| `hands_off_site_release_notes_to_docs` | PASS | FAIL | with-skill 明确不由 PM 写站内页，并输出 `target_skill`、`confirmed_version`、`release_scope`、`evidence`、`target_host`、`required_output`；baseline 反而把站内页列为直接创建步骤。 |
| `retains_pm_github_release_work` | PASS | FAIL | with-skill 明确客户公告和 GitHub Release 正文继续由 PM 负责，且 GitHub Release body、draft/publish、tag-aware preparation 在 #120 前不迁移；baseline 未说明 PM、Docs 或 #120 边界。 |
| `preserves_versioned_changelog_archive` | PASS | FAIL | with-skill 固定要求 `docs/changelog/changelog-v1.4.0.md`，并说明站内页不能替代归档；baseline 不知道仓库契约，另行建议 `changelog/v1.4.0.md`。 |
| `preserves_root_changelog_index` | PASS | PASS | 两侧都要求根 `CHANGELOG.md` 只索引版本归档、不重复完整条目；with-skill 还将其设为发布前硬门禁。 |
| `keeps_existing_release_evidence_contract` | PASS | FAIL | with-skill 要求完整审计 `PREV_TAG..v1.4.0` 与同窗口全部 PR、面向用户说明价值、保留 conventional prefix、真实作者/链接及变更明细，并阻止提前迁移 GitHub Release；baseline 只有一般证据审计，没有目标 tag 范围、前缀、PM/#120 边界。 |

## With-Skill Behavior

- 完整读取 PM Agent README、skill 与两份 reference 后，归一化 `THIS_TAG=v1.4.0`、`VERSION=1.4.0`，没有生成双 `v` 或把目标 tag 审计替换为 `HEAD`。
- 把客户公告、GitHub Release 正文和 tag-aware 发布准备留在 PM specialist；没有执行 GitHub、tag、commit 或发布写操作。
- 把 `docs/site/release-notes/v1.4.0.md` 交给 `docs-agent:release-notes-generator`，handoff 保留确认版本、release scope、已确认/可疑/缺失证据、目标宿主和 required output。
- 将 `docs/changelog/changelog-v1.4.0.md` 与根 `CHANGELOG.md` 索引作为独立契约，并明确站内页不替代版本归档。
- 识别 fixture 缺少 PREV_TAG、compare、PR、贡献者、changelog 和发布授权，正确阻断正文虚构；同时指出 API 页面仍为 `v1.3.0` 且未核验。

## Without-Skill Baseline

- 来源：2026-07-19 本次 fresh 独立 Codex 进程；同一 eval prompt、同一净化 fixture，未读取或应用 skill、Agent README、memory、父仓库文档或外部信息。
- baseline 正确识别证据不足、API 页面版本陈旧，并保留“版本归档 + 根索引”概念，因此 `preserves_root_changelog_index` 通过。
- baseline 未识别 Docs specialist handoff，直接计划创建 `docs/site/release-notes/v1.4.0.md`；未保留 PM 与 #120 前的 GitHub Release 边界。
- baseline 不知道仓库的确定路径，建议新增 `changelog/v1.4.0.md`；也未要求 `PREV_TAG..THIS_TAG`、conventional prefix 或 GitHub Release 不提前迁移等既有契约。

## Failures

- with-skill：无 assertion failure。
- without-skill：`hands_off_site_release_notes_to_docs`、`retains_pm_github_release_work`、`preserves_versioned_changelog_archive`、`keeps_existing_release_evidence_contract` 未满足。
- 基础设施提示：Codex CLI 输出了 model cache schema 警告，但 with-skill 与 without-skill 都成功返回完整最终结果，不影响 assertions 判定。

## Next Steps

- 保留本结果作为 PM specialist 在 #120 完成前的职责回归门禁。
- #120 真正迁移 GitHub Release 能力时，应同步修改该 eval 的 expected output/assertions，并重新执行 fresh with-skill 与 without-skill；在此之前不得把 GitHub Release 边界提前迁出 PM。
- `eval_metadata.json` 的 prompt 应持续与 `evals.json` 真源对齐，避免 runner 选择旧 prompt。

## Runtime Artifact Policy

- 本次 transcript、最终输出和隔离 workspace 仅位于 `tmp/eval-runs/pm-release-notes-eval004-r3.vmKkxP/`，不提交到 git。
- Durable 结果只提交本 `comparison.md`；不提交 `with_skill/`、`without_skill/`、transcript、timing、verdict 或 diagnostics。
