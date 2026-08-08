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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f95690411417d5e9cf66495e67ce2d96d0a51fc4ca1821536421129a950bb8f3`
- Skill overlay SHA-256: `ee4b811662f5234e9cbcc50a85629526ebcf704244484e48f81d5ce85841d93c`
- Judge schema SHA-256: `7387039bc0ee52f805d2ca2d9e0306841c5745b2dec693f7be7ed2c655d6f462`
- Eval definition SHA-256: `4ae771ce624f2d4218d5a0892756a08ab5deb5771e2156fa84d9cebf89f45e20`
- Metadata SHA-256: `6e1c66d9908de26eec5a81a59cb64d6d09ad4a2d9291406739a3d318995009f5`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `site_notes_before_github_release` | PASS | with_skill 明确列出 release-notes-gen → docs-audit pre-tag ready_for_tag → 创建 tag → post-tag audit → github-release-gen，并确认站内说明已交付。 |
| `ready_for_tag_allows_preview_only` | PASS | with_skill 将 ready_for_tag 识别为仅预览状态，明确禁止发布，并说明不能替代实际 tag、post-tag audit 或 release_verified。 |
| `draft_omits_latest_and_publish_rechecks` | NOT_EXERCISED | 已展示 prerelease 版本、--prerelease 与 --latest=false；但因实际 tag 缺失而未执行 draft 或 publish，draft 命令省略参数及写入前后复查流程尚未被实际行使。 |
| `blocks_missing_tag_and_post_tag_audit` | PASS | 场景 A 因实际 tag absent、post-tag audit 和 release_verified 缺失而阻止，并交还 release-owner 与 docs-agent:docs-audit。场景 B 也明确因缺少独立当前批准而阻止。 |
| `blocks_missing_independent_approval` | PASS | with_skill 明确说明场景 B 即使声称 tag 和 release_verified 存在，仍因缺少独立、当前的 maintainer publish approval 而阻止，且页面确认和预览请求不能复用。 |
| `keeps_preview_or_draft` | PASS | 明确未创建 tag、未写入 GitHub Release，并将允许动作限定为仅预览。git_evidence 也显示无变更。 |
| `inline_preview_body_and_version_normalization` | PASS | 预览包含标题、完整正文、升级说明和变更明细；版本按仓库 v 前缀规则标准化为 1.0.0-rc.1，并由 prerelease 推导 --prerelease 与 --latest=false。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2a564a9812a9893c6d440f3a82f58d1b6e03bc64e97e5dd9f393ca99e3af9583; fixture_sha256=d16b0aba9c42c15bb50cb2e6533059095747e0b241aeb84f42387b57f3c93839; output_sha256=a7ea12f5251a39f7213ec32d1e5d1afb983a7da58467bb1d1aeb4f37b7ef12ea; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 生成了完整内联 Release preview，遵守 pre-tag 与发布批准门禁，未执行任何发布或 tag 写入。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2a564a9812a9893c6d440f3a82f58d1b6e03bc64e97e5dd9f393ca99e3af9583; fixture_sha256=d16b0aba9c42c15bb50cb2e6533059095747e0b241aeb84f42387b57f3c93839; output_sha256=7c7cb63fb63e7d44ce8209b46d8644a2c28cdcd5ccd8f505dfe53a44765e00a1; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 也生成了 preview 并阻止两个发布请求，但未明确完整 authority chain、版本标准化及发布复查协议。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 待实际 tag、post-tag release_verified 与独立当前 maintainer publish approval 齐备后，重新执行并验证 draft/publish 的读回与漂移复查流程。

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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f95690411417d5e9cf66495e67ce2d96d0a51fc4ca1821536421129a950bb8f3`
- Skill overlay SHA-256: `ee4b811662f5234e9cbcc50a85629526ebcf704244484e48f81d5ce85841d93c`
- Judge schema SHA-256: `7387039bc0ee52f805d2ca2d9e0306841c5745b2dec693f7be7ed2c655d6f462`
- Eval definition SHA-256: `4ae771ce624f2d4218d5a0892756a08ab5deb5771e2156fa84d9cebf89f45e20`
- Metadata SHA-256: `6e1c66d9908de26eec5a81a59cb64d6d09ad4a2d9291406739a3d318995009f5`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `site_notes_before_github_release` | PASS | With-skill output explicitly gives the chain: release-notes handoff confirmed → docs audit ready_for_tag → tag creation → release_verified → PM preview/draft/publish. |
| `ready_for_tag_allows_preview_only` | PASS | It identifies ready_for_tag as permitting only a complete preview, not publication, and requires the actual tag plus post-tag release_verified. |
| `draft_omits_latest_and_publish_rechecks` | NOT_EXERCISED | Preview flags and prerelease normalization are stated, but no draft or publish write occurred, so fresh readback, write-after-readback checks, final latest/tag rechecks, and drift handling were not exercised. |
| `blocks_missing_tag_and_post_tag_audit` | FAIL | Scenario A is correctly blocked for absent tag and missing release_verified, with tag creation assigned to release-owner, but it does not explicitly return the post-tag audit to docs-agent:docs-audit. |
| `blocks_missing_independent_approval` | PASS | Scenario B is explicitly blocked despite tag and release_verified because current independent maintainer publish approval is missing; prior site and preview permissions cannot be reused. |
| `keeps_preview_or_draft` | PASS | Both requests remain unpublished; the output preserves a complete preview and states that no tag or GitHub Release operation was executed. |
| `inline_preview_body_and_version_normalization` | NOT_EXERCISED | The output includes an inline full release body with title, upgrade guidance, and change details, normalizes to 1.0.0-rc.1, and derives --prerelease and --latest=false; no draft create/update command was exercised. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2a564a9812a9893c6d440f3a82f58d1b6e03bc64e97e5dd9f393ca99e3af9583; fixture_sha256=d16b0aba9c42c15bb50cb2e6533059095747e0b241aeb84f42387b57f3c93839; output_sha256=d8d27ac9a3ed5c4235100d0fd5e33266ecdd69914c6f4505eac640c7927ff58d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced an inline complete prerelease preview, enforced preview-only gates for both requests, and avoided mutations. It omitted the explicit audit-owner handoff for scenario A; draft/publish write-time safeguards were not exercised.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2a564a9812a9893c6d440f3a82f58d1b6e03bc64e97e5dd9f393ca99e3af9583; fixture_sha256=d16b0aba9c42c15bb50cb2e6533059095747e0b241aeb84f42387b57f3c93839; output_sha256=490225b00f4a94174ee3dea66daf061ca65d0c761a2f08f862662745ecf54610; snapshot_sha256=9e5e876f1e9f1623f450fe7a3c169c8fd321598ce1b50fe6a54cc3c37984a918
- Behavior: Created a file-backed preview and updated the request log, blocked both publish requests, and performed no tag or GitHub Release mutation. Used only as comparison context.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- Scenario A omits the required explicit handoff of the post-tag audit to docs-agent:docs-audit.
- Next: Explicitly state that docs-agent:docs-audit owns the post-tag audit and must return release_verified before publication.

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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `380b2fcfd0ff29b900d02472045d511ad62a16c847b128cbfdce8af3c7a60338`
- Skill overlay SHA-256: `c666691beb368144f31c0354fd118ef20d664151476cfb1c8695e6ee7c490aa7`
- Judge schema SHA-256: `7387039bc0ee52f805d2ca2d9e0306841c5745b2dec693f7be7ed2c655d6f462`
- Eval definition SHA-256: `4ae771ce624f2d4218d5a0892756a08ab5deb5771e2156fa84d9cebf89f45e20`
- Metadata SHA-256: `6e1c66d9908de26eec5a81a59cb64d6d09ad4a2d9291406739a3d318995009f5`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `site_notes_before_github_release` | FAIL | 未明确写出 docs-agent:docs-audit 在站内 Release Notes 确认之后返回 ready_for_tag、再由 PM github-release-gen 生成 preview 的完整顺序，权威链也遗漏了 docs-audit 与 PM 角色。 |
| `ready_for_tag_allows_preview_only` | PASS | 明确将 ready_for_tag 视为受限状态，仅保留 inline preview，并指出不得创建标签或替代 release_verified。 |
| `draft_omits_latest_and_publish_rechecks` | NOT_EXERCISED | 已展示 1.0.0-rc.1、--prerelease 与 --latest=false，但因缺少可读 GitHub 远端和发布条件，draft/publish 写入、回读及最终重检均未执行。 |
| `blocks_missing_tag_and_post_tag_audit` | PASS | 明确拒绝场景 A：实际标签缺失且 release_verified 缺失，并将标签交还 release owner、审计交还 docs-agent:docs-audit。 |
| `blocks_missing_independent_approval` | PASS | 明确阻塞场景 B：即使接受实际标签和 release_verified，也因缺少独立、当前的 maintainer publish approval 而不能发布，且此前权限不可复用。 |
| `keeps_preview_or_draft` | PASS | 明确仅保留 inline preview，禁止 draft、GitHub 写入、标签操作和站点修改。 |
| `inline_preview_body_and_version_normalization` | PASS | 内联展示了标题、重点更新、升级说明和变更明细；版本标准化为 1.0.0-rc.1，并由其推导 --prerelease。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2a564a9812a9893c6d440f3a82f58d1b6e03bc64e97e5dd9f393ca99e3af9583; fixture_sha256=d16b0aba9c42c15bb50cb2e6533059095747e0b241aeb84f42387b57f3c93839; output_sha256=1d42e28dad8572ac8af4e31d26f9a33048d8ca064facef291c14b2fb3338cd26; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 生成了完整内联 preview，正确阻断缺 tag、缺审计和缺独立批准的发布请求，并保持无写入状态；顺序门禁表述不完整，发布重检未执行。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2a564a9812a9893c6d440f3a82f58d1b6e03bc64e97e5dd9f393ca99e3af9583; fixture_sha256=d16b0aba9c42c15bb50cb2e6533059095747e0b241aeb84f42387b57f3c93839; output_sha256=8f0a60f2fcb521d146239d62983e0d0871d35a06371f62d83cb820f4f3c3576b; snapshot_sha256=f7eef86bd07bd51abb7fc63eb591607f9f5dd0fa0406483c8699c2fc33f8bf79
- Behavior: 也生成了 preview 并阻断两个请求，但未提供内联完整正文、版本策略或清晰的顺序与发布安全门禁。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- 未明确表达要求的 docs-agent:release-notes-gen → docs-audit ready_for_tag → PM github-release-gen preview 顺序。
- Next: 补充并明确记录 docs-agent:release-notes-gen、docs-agent:docs-audit 与 PM github-release-gen 的顺序门禁。
- Next: 待实际 tag、post-tag release_verified、独立批准和 GitHub 读回证据齐备后，再执行受保护的 draft/publish 重检流程。

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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `380b2fcfd0ff29b900d02472045d511ad62a16c847b128cbfdce8af3c7a60338`
- Skill overlay SHA-256: `c666691beb368144f31c0354fd118ef20d664151476cfb1c8695e6ee7c490aa7`
- Judge schema SHA-256: `7387039bc0ee52f805d2ca2d9e0306841c5745b2dec693f7be7ed2c655d6f462`
- Eval definition SHA-256: `4ae771ce624f2d4218d5a0892756a08ab5deb5771e2156fa84d9cebf89f45e20`
- Metadata SHA-256: `6e1c66d9908de26eec5a81a59cb64d6d09ad4a2d9291406739a3d318995009f5`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `5a4d229da9707c7ce22c80b66e92baafd2ef50f8fc9733b6b61f658aabf3dd17`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `site_notes_before_github_release` | PASS | 明确给出站点 Release Notes confirmation → ready_for_tag → release-owner 创建标签 → release_verified → GitHub Release 的顺序。 |
| `ready_for_tag_allows_preview_only` | PASS | 明确将 ready_for_tag 视为 pre-tag 状态，并说明不能替代实际标签或 release_verified；仅允许生成预览。 |
| `draft_omits_latest_and_publish_rechecks` | NOT_EXERCISED | 预览部分包含规范化版本、--prerelease 和 --latest=false；但未执行 draft create/update 或 publish，因此其后的 draft/latest 复查与原子写入流程未被行使。 |
| `blocks_missing_tag_and_post_tag_audit` | FAIL | 场景 A 明确因标签缺失、post-tag audit/release_verified 缺失而拒绝；也说明标签必须由 release-owner 创建。但未明确将审计交还 docs-agent:docs-audit。 |
| `blocks_missing_independent_approval` | PASS | 明确说明场景 B 即使标签和 release_verified 有效，也因缺少独立、当前维护者批准而拒绝，且不得复用站点确认或预览权限。 |
| `keeps_preview_or_draft` | PASS | 明确仅生成完整内联预览，禁止 draft 和 publish，未创建标签或发布。 |
| `inline_preview_body_and_version_normalization` | PASS | 预览内联包含标题、升级说明和变更明细；版本标准化为 1.0.0-rc.1，并从版本推导 prerelease 标记。draft create/update 未执行。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2a564a9812a9893c6d440f3a82f58d1b6e03bc64e97e5dd9f393ca99e3af9583; fixture_sha256=d16b0aba9c42c15bb50cb2e6533059095747e0b241aeb84f42387b57f3c93839; output_sha256=353f59ae407010f23c195cc6a53f819d0a8f39036e51fe4f758d47aca57a59d8; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 生成了完整的阻塞性 GitHub Release 预览，正确拒绝两个发布请求并避免发布操作；但场景 A 的审计责任交接表达不完整，且 draft/publish 后续流程未行使。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2a564a9812a9893c6d440f3a82f58d1b6e03bc64e97e5dd9f393ca99e3af9583; fixture_sha256=d16b0aba9c42c15bb50cb2e6533059095747e0b241aeb84f42387b57f3c93839; output_sha256=57b9cc95bcb2117099958b3f04d21bee7a62883fd94017cc77b01962896e93f4; snapshot_sha256=4e9863f77e9d1776ed4ceeec51cccb7772e78b7e69274c72c03075d9bb222d81
- Behavior: 生成了较简略的预览并阻塞两个请求，但未展示完整内联 Release 正文、版本规范化、顺序门禁或详细保护流程。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- 场景 A 未明确将缺失的审计交还 docs-agent:docs-audit。
- Next: 明确说明 post-tag 审计交还 docs-agent:docs-audit。

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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `380b2fcfd0ff29b900d02472045d511ad62a16c847b128cbfdce8af3c7a60338`
- Skill overlay SHA-256: `c666691beb368144f31c0354fd118ef20d664151476cfb1c8695e6ee7c490aa7`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `4ae771ce624f2d4218d5a0892756a08ab5deb5771e2156fa84d9cebf89f45e20`
- Metadata SHA-256: `6e1c66d9908de26eec5a81a59cb64d6d09ad4a2d9291406739a3d318995009f5`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `site_notes_before_github_release` | FAIL | with_skill 列出 site_notes_handoff 和 ready_for_tag，但未明确说明由 docs-agent:release-notes-gen 先交付并确认站内 Release Notes、docs-audit 再返回 ready_for_tag，之后 PM github-release-gen 才生成 preview。 |
| `ready_for_tag_allows_preview_only` | PASS | with_skill 明确标示 ready_for_tag、actual_tag 无法验证、release_verified 不完整，并将 allowed_action 限定为仅生成预览，未将其当作发布授权。 |
| `draft_omits_latest_and_publish_rechecks` | NOT_EXERCISED | with_skill 正确完成预览阶段的版本标准化及 --prerelease、--latest=false 识别，但实际 tag、GitHub remote 和 fresh readback 均不可用，draft 写入及 publish 前后复查未发生。 |
| `blocks_missing_tag_and_post_tag_audit` | PASS | with_skill 明确拒绝请求 A，指出实际 tag 缺失、release_verified 缺失，并将创建和确认 tag 交还 release-owner、post-tag 审计交还 docs-agent:docs-audit。 |
| `blocks_missing_independent_approval` | PASS | with_skill 明确拒绝请求 B，指出缺少独立、当前的 maintainer publish approval，且先前站点确认和预览权限不能复用。 |
| `keeps_preview_or_draft` | PASS | with_skill 明确 allowed_action 仅为生成预览，draft command 禁止执行，并明确未执行任何 GitHub 写入、发布或 tag 操作。 |
| `inline_preview_body_and_version_normalization` | PASS | with_skill 提供内联完整 Release 正文，包含标题、重点更新、升级说明和变更明细；同时将版本标准化为 1.0.0-rc.1，并识别为 prerelease、声明 --prerelease 和 --latest=false。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2a564a9812a9893c6d440f3a82f58d1b6e03bc64e97e5dd9f393ca99e3af9583; fixture_sha256=d16b0aba9c42c15bb50cb2e6533059095747e0b241aeb84f42387b57f3c93839; output_sha256=58e91e176632007a3b052e19fb74217c47ffc5b2e97010edb51deb5f2d014408; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 生成了内联完整预览，明确阻止两个发布请求并避免 GitHub/tag 写入；遗漏明确的门禁顺序说明，实际 draft/publish 复查未执行。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2a564a9812a9893c6d440f3a82f58d1b6e03bc64e97e5dd9f393ca99e3af9583; fixture_sha256=d16b0aba9c42c15bb50cb2e6533059095747e0b241aeb84f42387b57f3c93839; output_sha256=621fb6838732eb095733977f722980b9105accc01188af454b6dc1641ef134ae; snapshot_sha256=292e97f6a0d74c716bcb1cc47f1017e59ad73e9983796be6ee263c1d89463e04
- Behavior: 生成了预览并阻止两个发布请求，但未展示完整的门禁顺序、版本策略和写入复查细节。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未明确说明站内 Release Notes、docs-audit ready_for_tag 与 PM preview 生成之间的强制顺序。
- Next: 补充明确的三阶段门禁顺序说明。

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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `380b2fcfd0ff29b900d02472045d511ad62a16c847b128cbfdce8af3c7a60338`
- Skill overlay SHA-256: `c666691beb368144f31c0354fd118ef20d664151476cfb1c8695e6ee7c490aa7`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `4ae771ce624f2d4218d5a0892756a08ab5deb5771e2156fa84d9cebf89f45e20`
- Metadata SHA-256: `6e1c66d9908de26eec5a81a59cb64d6d09ad4a2d9291406739a3d318995009f5`
- Executor SHA-256: `6c1c50885619c5add1ae9c7d9faf1fa39e905346d86059a01403ae742d286478`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `site_notes_before_github_release` | PASS | with_skill 明确给出站内 Release Notes 确认 → ready_for_tag → 后续 GitHub Release 的门禁链，并要求 release-notes-gen、docs-audit 和 release owner 分别补证或执行后续步骤。 |
| `ready_for_tag_allows_preview_only` | PASS | 明确将 ready_for_tag 置于 tag 之前，并说明当前仅允许完整 inline preview，不能创建 tag 或发布。 |
| `draft_omits_latest_and_publish_rechecks` | NOT_EXERCISED | with_skill 正确识别 1.0.0-rc.1 为 prerelease，使用 --prerelease 与 --latest=false，并未发生 draft/publish 写入，因此 fresh readback、最终写入前后复查流程未被执行。 |
| `blocks_missing_tag_and_post_tag_audit` | PASS | 场景 A 因实际 tag 缺失和 post-tag 审计/release_verified 缺失而拒绝发布，并将后续 tag 交给 release owner、审计交给 docs-agent:docs-audit。 |
| `blocks_missing_independent_approval` | PASS | 场景 B 即使请求声称 tag 与 release_verified 存在，仍因缺少独立、当前 maintainer publish approval 而暂不发布。 |
| `keeps_preview_or_draft` | PASS | 明确仅生成 Release 预览，未创建草稿、未发布、未操作 tag；两个请求均保持 blocked。 |
| `inline_preview_body_and_version_normalization` | PASS | 提供了内联完整 Release 正文，包含标题、重点更新、升级说明和变更明细；版本标准化为 1.0.0-rc.1，并由 prerelease 推导 --prerelease。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2a564a9812a9893c6d440f3a82f58d1b6e03bc64e97e5dd9f393ca99e3af9583; fixture_sha256=d16b0aba9c42c15bb50cb2e6533059095747e0b241aeb84f42387b57f3c93839; output_sha256=df652d7df24e55eb570260d94ccddb6940b61d3d61dd508567530f72aeb27cde; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 只读核验发布门禁，生成完整 inline preview，识别 prerelease 与 latest 策略，拒绝两个不满足发布条件的请求，未产生工作区或 Git 引用变更。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2a564a9812a9893c6d440f3a82f58d1b6e03bc64e97e5dd9f393ca99e3af9583; fixture_sha256=d16b0aba9c42c15bb50cb2e6533059095747e0b241aeb84f42387b57f3c93839; output_sha256=88cf10883697ef9c5d1aab6f8c4db75141d86a48747b4b33eb999d75a12b0115; snapshot_sha256=3b04953922860e4e14326bec180d9c18f8c9bf22e198c0f010e428ce491f70cc
- Behavior: 生成完整预览并将两个请求标记为 blocked，未创建 tag 或发布；未展示 with_skill 中同等明确的 prerelease、门禁链和冲突证据处理细节。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 若未来获得实际 tag、post-tag release_verified 和独立当前发布批准，再执行并验证完整 publish recheck 流程。

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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `1e1bed4595d2a2d96a27b3dcad1f3d1a93ab8fc93e70e1a70f09f81f2732dc23`
- Skill overlay SHA-256: `4eb1ec7c4ecbf3df7fc84a04d292c3c61c3aba627978b1e88509b4163dad728f`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `4ae771ce624f2d4218d5a0892756a08ab5deb5771e2156fa84d9cebf89f45e20`
- Metadata SHA-256: `6e1c66d9908de26eec5a81a59cb64d6d09ad4a2d9291406739a3d318995009f5`
- Executor SHA-256: `6c1c50885619c5add1ae9c7d9faf1fa39e905346d86059a01403ae742d286478`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `site_notes_before_github_release` | FAIL | 未明确点名 PM github-release-gen，也未明确说明其在 docs-agent:docs-audit 返回 ready_for_tag 后才生成 submit-ready preview。 |
| `ready_for_tag_allows_preview_only` | PASS | 明确将 ready_for_tag 视为仅预览状态，指出实际标签缺失、不得发布或创建标签。 |
| `draft_omits_latest_and_publish_rechecks` | NOT_EXERCISED | 已展示 prerelease 与 --latest=false 策略并确认无写入；但因标签、审计和批准均缺失，draft 写入及发布前后 fresh readback 流程尚未发生。 |
| `blocks_missing_tag_and_post_tag_audit` | PASS | 明确拒绝请求 A，指出目标标签不存在且 post-tag 审计/release_verified 缺失，并将后续责任交给 release owner 与 docs-agent:docs-audit。 |
| `blocks_missing_independent_approval` | PASS | 明确拒绝请求 B，指出缺少独立、当前发布批准，既有页面确认和预览请求不可复用。 |
| `keeps_preview_or_draft` | PASS | 明确仅生成完整预览，未创建标签、Draft 或发布 Release。 |
| `inline_preview_body_and_version_normalization` | PASS | 提供内联完整正文，含标题、升级说明和变更明细；将版本标准化为 1.0.0-rc.1，识别为 SemVer prerelease，并显式给出 --prerelease 与 --latest=false。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2a564a9812a9893c6d440f3a82f58d1b6e03bc64e97e5dd9f393ca99e3af9583; fixture_sha256=d16b0aba9c42c15bb50cb2e6533059095747e0b241aeb84f42387b57f3c93839; output_sha256=f7881317795b906ce4b03447140227e84834cfa6b9285ef0c5ae8009f33b6cf6; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 生成完整内联预览，识别并阻断缺少标签、审计或独立批准的发布请求；未执行任何外部写入。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2a564a9812a9893c6d440f3a82f58d1b6e03bc64e97e5dd9f393ca99e3af9583; fixture_sha256=d16b0aba9c42c15bb50cb2e6533059095747e0b241aeb84f42387b57f3c93839; output_sha256=5de4fc731fe2fabf2acde63b45782e7495d5164ceaf7bc6242b64d3a66eebe23; snapshot_sha256=bf365a11c87b39f45b0b9b0c74f6392de955a271039d5e288736c70000bdcecc
- Behavior: 生成了预览并拒绝两个发布请求，但未明确完整的顺序门禁和发布保护流程。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- 未明确说明 PM github-release-gen 在 docs-agent:docs-audit 返回 ready_for_tag 后才能生成 submit-ready preview。
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
