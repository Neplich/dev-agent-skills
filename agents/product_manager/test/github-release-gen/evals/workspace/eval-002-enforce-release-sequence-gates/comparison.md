# Eval Result: eval-002-enforce-release-sequence-gates

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-release-gen`
- Eval: `eval-002-enforce-release-sequence-gates`
- Test case: `prerelease 的时序门禁与 latest 指针保护`
- Prompt:

> 请读取 `release-package.md`、站内版本说明与 GitHub 维护证据，准备 GitHub Release 预览，并处理 `publish-requests.md` 中的两个发布请求。

- Expected output:

> 在 release-notes-gen ready handoff 和 docs-audit ready_for_tag 后允许完整 preview；目标 v1.0.0-rc.1 按 SemVer 识别为 prerelease，preview 显示 --prerelease --latest=false。draft create/update 省略 latest flag；publish 若有两次写，在最终 draft=false 写前重读 latest 与 tag，未漂移时原子应用 prerelease/latest；每次写后回读目标/latest/tag，漂移时返回 preview 或 tag owner；场景 A 因缺实际 tag 与 release_verified 阻塞，场景 B 虽有实际 tag 和 release_verified 但缺当前维护者独立批准仍阻塞。

## Test Set / Fresh Run

- Eval schema: `evals.json` v1.0。
- Fixture manifest: `7e570eede48dfe2fc6170404d472f674fe0da4b94e3d778f5ba7423f63b33f55`（4 个可见文件；两侧逐字节一致）。
- Repository HEAD: `47adbbc9`。
- Fresh run window: 2026-08-07 00:58–01:14（Asia/Shanghai）。
- Runtime: 3 个独立会话，均为 `gpt-5.6-luna`、`model_reasoning_effort=medium`：fresh without-skill、fresh with-skill、fresh judge。
- Controlled variable: 两个 candidate 使用完全相同的 prompt、fixture manifest、HOME/CODEX_HOME 目录形态与同一份 `auth.json`；唯一变量是 with-skill lane 安装并加载目标 specialist skill。
- Physical isolation: 按 skill 先完成并销毁全部 baseline 随机顶层根，再创建 with-skill 根；32 个 candidate 全部完成并销毁后才创建第三套 judge 根。
- Candidate visibility: lane 中未放入 `eval_metadata.json`、`evals.json`、`expected_output`、assertions、历史 `comparison.md`、README 脚手架或 judge 材料；泄漏扫描为 0 命中。
- External data rule: 实时实体因 GitHub 认证、网络或当时集合缺失而不可得时，相关 assertion 记为 `NOT EXERCISED`，只影响 Coverage，不伪造成 Behavior 的 PASS/FAIL。

## Latest Result

- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
- Overall result: FAIL
- With-skill summary: skill_load_hits=2，transcript 先读取 skill 再读取发布包与证据；未发生 GitHub 写入，快照前后相同。最终生成了 prerelease 预览并阻止 A/B 发布，但遗漏若干明确门禁、路由和写入保护说明。

## Historical Contract Note

- 旧 durable 结果因 issue #234 的 prompt/fixture 泄漏修复或后续 assertion 增强而标记为 `BLOCKED`。本文件已由当前契约下的 fresh paired run 与独立 judge 结论覆盖。
- 本轮没有复用历史 baseline、candidate、verdict 或旧结论；without-skill baseline 仅作行为对照，不参与 with-skill 的 Behavior/Coverage 判定。

## With-Skill Behavior

skill_load_hits=2，transcript 先读取 skill 再读取发布包与证据；未发生 GitHub 写入，快照前后相同。最终生成了 prerelease 预览并阻止 A/B 发布，但遗漏若干明确门禁、路由和写入保护说明。

## Without-Skill Baseline

未加载 skill（skill_load_hits=0）；同样未写入 GitHub，输出包含完整预览和 A/B 阻塞结论，但未提供 prerelease/latest 写入保护细节。

## Assertion Review

| Assertion | With skill | Evidence / reason | Without-skill comparison |
| --- | --- | --- | --- |
| `site_notes_before_github_release` | **FAIL** | with_skill transcript item_2 读取了两个 handoff，但最终 candidate.md 只写“站点门禁：ready_for_tag”，未明确说明 release-notes-gen 确认先于 docs-audit ready_for_tag，且未点名两者的顺序门禁。 | without_skill candidate 仅写“文档交接：ready”和“Docs audit：ready_for_tag”，也未明确两阶段顺序。 |
| `ready_for_tag_allows_preview_only` | **FAIL** | candidate.md 将状态列为 ready_for_tag 并表示本次仅生成预览，但未明确声明 ready_for_tag 不是发布授权、不能替代实际 tag 或 post-tag release_verified；该语义只能从 A 的阻塞结论间接推断。 | without_skill 以“Docs audit：ready_for_tag”描述验证状态，也未说明其不是发布授权。 |
| `draft_omits_latest_and_publish_rechecks` | **NOT EXERCISED** | 预览部分明确给出目标为 SemVer prerelease、PRERELEASE_FLAG=--prerelease、LATEST_FLAG=--latest=false；但 transcript 没有 draft/publish 写入、写后回读、最终 latest/tag 复查或漂移分支，快照也无写入，因此该写入契约无法从本次执行判定。 | without_skill 同样无 draft/publish 写入或回读 trace，且未给出 draft 省略 latest 或最终漂移保护说明。 |
| `blocks_missing_tag_and_post_tag_audit` | **FAIL** | candidate.md 正确指出 A 缺少实际目标 tag 和 post-tag release_verified，但没有按契约把 tag 交还宿主 release owner、把审计交还 docs-agent:docs-audit；最终报告未提供这两个 owner 路由。 | without_skill 正确阻塞 A，但同样没有 owner 路由。 |
| `blocks_missing_independent_approval` | **PASS** | candidate.md 明确说明 B 虽有 tag 和 post-tag 审计仍因缺少“独立、当前的 maintainer publish approval”而拒绝，并明确此前站点确认和预览请求不能复用。 | without_skill 也明确阻塞 B，并指出站点页面确认和预览请求不构成独立维护者批准。 |
| `keeps_preview_or_draft` | **PASS** | candidate.md 明确写“本次仅生成预览，未修改 GitHub Release，也未创建或修改 tag”；with_skill after-snapshot 与 before-snapshot 完全一致，transcript 无发布或写入工具调用。 | without_skill candidate 同样声明只生成预览，且前后快照一致。 |
| `inline_preview_body_and_version_normalization` | **PASS** | candidate.md 提供内联标题、重点更新、其他改进、升级说明和变更明细完整正文；版本为 v1.0.0-rc.1，规范化为 1.0.0-rc.1，明确判断 prerelease 并给出 --prerelease 与 --latest=false。 | without_skill 也提供较完整正文并标记 Pre-release，但未给出规范化版本及显式 prerelease/latest flag。 |

## Failures

- site_notes_before_github_release：最终输出未明确 release-notes-gen → docs-audit → github-release-gen 的顺序。
- ready_for_tag_allows_preview_only：未明确 ready_for_tag 不是发布授权且不能替代实际 tag/release_verified。
- blocks_missing_tag_and_post_tag_audit：未将缺失事项路由给 release owner 与 docs-agent:docs-audit。

## Not Exercised

- draft_omits_latest_and_publish_rechecks：本次按 fixture 要求只生成 preview，未执行 draft/publish 写入、回读或漂移检查。

## Next Steps

- 补充顺序门禁、ready_for_tag 限制和缺失证据的 owner 路由；若要评估写入保护，提供可执行的 draft/publish 场景或相应 trace。

## Runtime Evidence

- With-skill candidate: return code `0`，duration `80.853s`，`skill_load_hits=2`。
- Without-skill candidate: return code `0`，duration `73.01s`，`skill_load_hits=0`。
- Independent judge: return code `0`，duration `101.536s`。
- Judge 已读取两侧最终输出、完整 JSONL 工具 trace、before/after workspace snapshot、fixture manifest 与 session status，并核验读取顺序和零写入边界。
- 所有临时 HOME/CODEX_HOME 与 candidate/judge 随机顶层根均已销毁；持久化证据目录中不存在 `auth.json`。

## Runtime Artifact Policy

- 仓库只持久化本 canonical `comparison.md`。
- Candidate、transcript、judge verdict、timing、status、snapshot 与 diagnostics 仅作为 `/tmp` 运行期证据，不提交到 git。
