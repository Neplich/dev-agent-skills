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
- Identity schema: `2`
- target_skill_sha256: `0c9b1305da43afbfc22e6d563651831ce45be05793224d552c008cc393a37b1e`
- eval_definition_sha256: `ca7c0b18d751c17e3675256471abe2e22f05a84c6ec6d780c8a51c53156008f9`
- metadata_sha256: `a37c69100d8b09e8a32fd7ae07c266ac1aa0ef65dd08a89916726ecd29694ad7`
- fixture_sha256: `17e20791a9c9288907fb214989bbc6378e7d64a98732f68a5c493285ff25f933`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `df39efd24a07751331d3b8f08b12fab041cb7e732754feb1dfc8bc4a96c5fe1a`
- Identity migration: **MIGRATED_WITHOUT_MODEL_RERUN**
- Identity migration source commit: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Identity migration audit: `docs/engineer/repository-governance/eval-scenario-isolation/eval-identity-v2-migration-audit.json`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `title_matches_marketplace_format` | PASS | 标题为 `v0.9.0 - 失败消息重试与统一附件模型兼容`，符合格式且主题具体相关。 |
| `upgrade_note_first_sentence_derived` | PASS | 「升级说明」首句为「无破坏性变更，也没有新增 plugin。6 个 role plugin 均更新到 `v0.9.0`。」数量与 marketplace manifest 的 6 个插件一致。 |
| `claude_section_omitted_with_platform_limit` | PASS | 正文没有 `### Claude Code` 小节，且说明 `/plugin update` 不支持 version pin、无法固定到 `v0.9.0`，并声明无已验证固定版本路径。 |
| `codex_section_omitted_without_target_tag_support` | PASS | 正文没有 `### Codex` 小节，也未臆造 TARGET_TAG 或 INSTALL.md fetch 指令。 |
| `kimi_section_omitted_without_plugin_json` | PASS | 正文没有 `### Kimi Code` 小节，也未生成 `/plugins install` 命令。 |
| `closing_sentence_derived` | PASS | 收尾句包含 6 个 role plugin，声明无已验证固定版本安装路径，并指向默认分支 main 更新，未作不可验证的固定版本承诺。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=734c4a4cb7e543db5091d9f1c4a08014e2d017a93f5c1b82e54e15f916eb8fba; fixture_sha256=17e20791a9c9288907fb214989bbc6378e7d64a98732f68a5c493285ff25f933; output_sha256=2f9c5ae7e44fb25f5e8a237f5d117f024f4b8e37b9086c04a4a57e4a6de681d3; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 生成了符合要求的 GitHub Release 预览，正确处理 manifest 推导和各平台能力限制。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=734c4a4cb7e543db5091d9f1c4a08014e2d017a93f5c1b82e54e15f916eb8fba; fixture_sha256=17e20791a9c9288907fb214989bbc6378e7d64a98732f68a5c493285ff25f933; output_sha256=f18656cc47f2105f5f7aaaf13422d71aff3ef56425f8e546322d2801c5e5b87e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 生成了裸版本号标题，并保留了不应出现的 Claude、Codex、Kimi 安装小节/说明，未满足目标格式。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
