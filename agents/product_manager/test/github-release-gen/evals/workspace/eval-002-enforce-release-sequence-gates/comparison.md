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
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
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
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
