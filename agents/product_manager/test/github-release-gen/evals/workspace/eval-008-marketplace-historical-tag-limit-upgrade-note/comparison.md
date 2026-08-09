# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-release-gen`
- Eval: `eval-008-marketplace-historical-tag-limit-upgrade-note`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `17e20791a9c9288907fb214989bbc6378e7d64a98732f68a5c493285ff25f933` from `agents/product_manager/test/github-release-gen/evals/workspace/eval-008-marketplace-historical-tag-limit-upgrade-note`.
- Fixture SHA-256: `17e20791a9c9288907fb214989bbc6378e7d64a98732f68a5c493285ff25f933`
- Prompt SHA-256: `734c4a4cb7e543db5091d9f1c4a08014e2d017a93f5c1b82e54e15f916eb8fba`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f95690411417d5e9cf66495e67ce2d96d0a51fc4ca1821536421129a950bb8f3`
- Skill overlay SHA-256: `ee4b811662f5234e9cbcc50a85629526ebcf704244484e48f81d5ce85841d93c`
- Judge schema SHA-256: `df39efd24a07751331d3b8f08b12fab041cb7e732754feb1dfc8bc4a96c5fe1a`
- Eval definition SHA-256: `ca7c0b18d751c17e3675256471abe2e22f05a84c6ec6d780c8a51c53156008f9`
- Metadata SHA-256: `a37c69100d8b09e8a32fd7ae07c266ac1aa0ef65dd08a89916726ecd29694ad7`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `title_matches_marketplace_format` | PASS | 标题为“v0.9.0 - 失败消息重试与统一附件模型兼容”，符合要求。 |
| `upgrade_note_first_sentence_derived` | PASS | 「升级说明」首段以指定句开头，并使用由 manifest 推导的 6 个 role plugin 数量。 |
| `claude_section_omitted_with_platform_limit` | FAIL | 正文包含 `### Claude Code` 小节；该小节按要求应省略。 |
| `codex_section_omitted_without_target_tag_support` | FAIL | 正文包含 `### Codex` 小节；目标 INSTALL.md 不支持 TARGET_TAG，按要求应省略。 |
| `kimi_section_omitted_without_plugin_json` | FAIL | 正文包含 `### Kimi Code` 小节；目标 tag 无 plugin.json，按要求应省略。 |
| `closing_sentence_derived` | PASS | 收尾句包含 6 个 role plugin 数量，并声明无已验证固定版本安装路径、按 main 更新，未作不当承诺。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=734c4a4cb7e543db5091d9f1c4a08014e2d017a93f5c1b82e54e15f916eb8fba; fixture_sha256=17e20791a9c9288907fb214989bbc6378e7d64a98732f68a5c493285ff25f933; output_sha256=78ceeca5ece40ef6b66fd38b11539fb3b8c001e688253560de30173ee86fb9a4; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 生成了未写入或发布的 Release 预览；标题和升级说明数量推导正确，但错误保留了应省略的 Claude Code、Codex 和 Kimi Code 小节。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=734c4a4cb7e543db5091d9f1c4a08014e2d017a93f5c1b82e54e15f916eb8fba; fixture_sha256=17e20791a9c9288907fb214989bbc6378e7d64a98732f68a5c493285ff25f933; output_sha256=27213037a7e614431148631468ba0bb3dbf8bc8d4f135e4343eb9bdfde3c0b85; snapshot_sha256=7aac4f219319af522179782d1c0588f0eb805963ed386026d5a40ac586f321a5
- Behavior: 生成了文件型 Release 预览并保持仓库未提交；标题未采用要求的 marketplace 格式，且保留并泛化描述了三个宿主小节。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- claude_section_omitted_with_platform_limit
- codex_section_omitted_without_target_tag_support
- kimi_section_omitted_without_plugin_json
- Next: 删除升级说明中的 Claude Code、Codex 和 Kimi Code 小节，并保留平台限制及无固定版本安装路径的声明。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
