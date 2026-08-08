# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-release-gen`
- Eval: `eval-002-enforce-release-sequence-gates`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `d16b0aba9c42c15bb50cb2e6533059095747e0b241aeb84f42387b57f3c93839` from `agents/product_manager/test/github-release-gen/evals/workspace/eval-002-enforce-release-sequence-gates`.
- Fixture SHA-256: `d16b0aba9c42c15bb50cb2e6533059095747e0b241aeb84f42387b57f3c93839`
- Prompt SHA-256: `2a564a9812a9893c6d440f3a82f58d1b6e03bc64e97e5dd9f393ca99e3af9583`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `793cabc84dc1947c3d6386a1d060276eea2eb8b4e9de25fdd6c7b7a60fb82cb0`
- Skill overlay SHA-256: `ecc021af86f838c5c915ade1c1e1095fa203f789350af9aa701ad32bae876bb2`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `4ae771ce624f2d4218d5a0892756a08ab5deb5771e2156fa84d9cebf89f45e20`
- Metadata SHA-256: `6e1c66d9908de26eec5a81a59cb64d6d09ad4a2d9291406739a3d318995009f5`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `site_notes_before_github_release` | FAIL | with_skill 未明确说明 docs-agent:release-notes-gen 确认站内 Release Notes → docs-audit 返回 ready_for_tag → PM github-release-gen 生成 submit-ready preview 的完整顺序。 |
| `ready_for_tag_allows_preview_only` | FAIL | with_skill 说明 pre-tag 审计和 post-tag/release_verified 的缺失会阻止发布，但未明确将 ready_for_tag 定义为仅 preview/受限 draft 状态，或明确其不能代替实际 tag。 |
| `draft_omits_latest_and_publish_rechecks` | FAIL | with_skill 正确识别 prerelease 并给出 --prerelease --latest=false，但未说明 draft 命令省略 latest 参数，也未覆盖 publish 前后 fresh read、latest/tag 漂移复查及原子最终写入流程。 |
| `blocks_missing_tag_and_post_tag_audit` | PASS | with_skill 对场景 A 因目标 tag absent、post-tag/release_verified 缺失而拒绝发布，并将 tag 交给 release owner、审计交给 docs-agent:docs-audit。 |
| `blocks_missing_independent_approval` | PASS | with_skill 明确即使接受实际 tag 与 release_verified，仍因缺少独立、当前的 maintainer publish approval 而暂停，并指出站点确认和预览请求不可复用。 |
| `keeps_preview_or_draft` | PASS | with_skill 明确 blocked，未执行 GitHub 写入、发布或 tag 操作，并保留 Release preview；同时说明不能创建 draft。 |
| `inline_preview_body_and_version_normalization` | FAIL | with_skill 提供了内联完整正文、标题、升级说明、变更明细，并识别 prerelease、给出发布参数；但未明确 PRERELEASE_FLAG，亦未说明 draft create/update 命令中的显式声明。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2a564a9812a9893c6d440f3a82f58d1b6e03bc64e97e5dd9f393ca99e3af9583; fixture_sha256=d16b0aba9c42c15bb50cb2e6533059095747e0b241aeb84f42387b57f3c93839; output_sha256=c482a827208f1d4ba7cba282ccf3a66e146d6099737e684d231c319824c66f3d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 生成了完整内联预览，正确阻止缺 tag/审计或独立批准的发布请求，并保持无写入状态；但遗漏多个细粒度流程和参数要求。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2a564a9812a9893c6d440f3a82f58d1b6e03bc64e97e5dd9f393ca99e3af9583; fixture_sha256=d16b0aba9c42c15bb50cb2e6533059095747e0b241aeb84f42387b57f3c93839; output_sha256=2ab4f17c068f1448efe6212677148d4ff2d708b9ee68b89f64bd758cbbc4ac61; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 生成了预览并阻止两个发布请求，但未明确完整的顺序门禁、ready_for_tag 限制、发布写入复查或 draft 参数保护。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足顺序门禁的明确表述。
- with_skill 未完整说明 ready_for_tag 的仅预览语义。
- with_skill 未覆盖 draft 参数省略及 publish 前后漂移复查。
- with_skill 未声明 PRERELEASE_FLAG 及其在 draft 命令中的显式使用。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-release-gen`
- Eval: `eval-002-enforce-release-sequence-gates`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `d16b0aba9c42c15bb50cb2e6533059095747e0b241aeb84f42387b57f3c93839` from `agents/product_manager/test/github-release-gen/evals/workspace/eval-002-enforce-release-sequence-gates`.
- Fixture SHA-256: `d16b0aba9c42c15bb50cb2e6533059095747e0b241aeb84f42387b57f3c93839`
- Prompt SHA-256: `2a564a9812a9893c6d440f3a82f58d1b6e03bc64e97e5dd9f393ca99e3af9583`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `ebd2c00966a7932d251daeeef05573b0145183fe908cf102225636115f85820c`
- Skill overlay SHA-256: `2398a04c1c550bc8e45aa1564f5f42f6e629a29d1c1ed530494ae269f918d169`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `4ae771ce624f2d4218d5a0892756a08ab5deb5771e2156fa84d9cebf89f45e20`
- Metadata SHA-256: `6e1c66d9908de26eec5a81a59cb64d6d09ad4a2d9291406739a3d318995009f5`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `site_notes_before_github_release` | FAIL | With-skill output notes a blocked site handoff but does not explicitly state the required ordered handoffs or PM generation gate. |
| `ready_for_tag_allows_preview_only` | FAIL | It does not characterize ready_for_tag as preview/restricted draft-only status or explicitly distinguish it from tag and post-tag release_verified authorization. |
| `draft_omits_latest_and_publish_rechecks` | FAIL | It gives prerelease flags but omits draft command protections, latest-pointer confirmation, fresh reads, atomic final write, and post-write drift checks. |
| `blocks_missing_tag_and_post_tag_audit` | FAIL | Request A is correctly blocked for absent tag and missing release_verified, but the required handoff of tag ownership to the release owner and audit ownership to docs-agent:docs-audit is not stated. |
| `blocks_missing_independent_approval` | PASS | Request B is rejected despite tag and release_verified being present because independent, current maintainer publish approval is missing; prior page confirmation and preview permission are explicitly not substitutes. |
| `keeps_preview_or_draft` | PASS | The output states preview was generated, no draft was created or updated, and no release or tag operation was performed. |
| `inline_preview_body_and_version_normalization` | FAIL | The output includes an inline full preview body and normalized prerelease decision, but does not show draft create/update commands with PRERELEASE_FLAG explicitly declared. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2a564a9812a9893c6d440f3a82f58d1b6e03bc64e97e5dd9f393ca99e3af9583; fixture_sha256=d16b0aba9c42c15bb50cb2e6533059095747e0b241aeb84f42387b57f3c93839; output_sha256=2bbd5d7d76a6c91162903808c47cba2913e3f758756fdc01943beefec009b628; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced an inline complete preview, normalized the prerelease, and correctly blocked publishing; omitted several required handoff and publish-safety procedures.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2a564a9812a9893c6d440f3a82f58d1b6e03bc64e97e5dd9f393ca99e3af9583; fixture_sha256=d16b0aba9c42c15bb50cb2e6533059095747e0b241aeb84f42387b57f3c93839; output_sha256=6f151d9355a2abdb4c81bce7465d324dd90ce0c50b7a3c0153b714ec30998136; snapshot_sha256=d375a4389419a9aad9061470e1b85cc0c5b25db9f7dc7eba7aa000e9810ea28f
- Behavior: Produced a complete preview file and updated publish-requests.md; correctly blocked A and B, but provided little procedural detail.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- With-skill output omits explicit release-note/audit/PM sequencing.
- With-skill output omits ready_for_tag authorization semantics and detailed draft/publish recheck protocol.
- With-skill output omits required ownership handbacks for the missing-tag/audit scenario.
- With-skill output does not provide explicit draft create/update command declarations.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Migration Status

## Current Result

- Evidence status: **STALE**
- Migration status: **PENDING**
- Blocking reason: this eval has not yet been rerun under the Issue #246 scenario, lane-isolation, and fresh-judge contract.
Overall result: BLOCKED

## Historical Context (Superseded)

The complete pre-migration comparison follows unchanged. It is retained only as historical context and is not current release evidence.

---

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
