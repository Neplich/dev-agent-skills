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
- target_skill_sha256: `ed7c0a44968df88c4831e9abe2b9be4922e4fa2cd6bcbd8dc6dd7e927ff9c87a`
- eval_definition_sha256: `ca7c0b18d751c17e3675256471abe2e22f05a84c6ec6d780c8a51c53156008f9`
- metadata_sha256: `a37c69100d8b09e8a32fd7ae07c266ac1aa0ef65dd08a89916726ecd29694ad7`
- fixture_sha256: `17e20791a9c9288907fb214989bbc6378e7d64a98732f68a5c493285ff25f933`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `df39efd24a07751331d3b8f08b12fab041cb7e732754feb1dfc8bc4a96c5fe1a`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `734c4a4cb7e543db5091d9f1c4a08014e2d017a93f5c1b82e54e15f916eb8fba`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `41bf9818330e1ae365d336932a5653b591537342874ba68ae701f1478bc7b159`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `title_matches_marketplace_format` | PASS | With_skill preview title is `v0.9.0 - 失败消息重试与统一附件模型链路`, matching the required nonempty marketplace format and describing confirmed release facts. |
| `upgrade_note_first_sentence_derived` | PASS | The locked with_skill preview’s `## 升级说明` begins exactly with `无破坏性变更，也没有新增 plugin。6 个 role plugin 均更新到 v0.9.0。`; the count matches the six entries in the fixture marketplace manifest. |
| `claude_section_omitted_with_platform_limit` | PASS | The preview omits a `### Claude Code` section, explains historical-tag rerun limitations and `/plugin update` lack of version pinning, and states that no verified fixed-version installation path exists. |
| `codex_section_omitted_without_target_tag_support` | PASS | The preview omits a `### Codex` section and explicitly attributes the omission to the fixture `.codex/INSTALL.md` lacking `TARGET_TAG` support. |
| `kimi_section_omitted_without_plugin_json` | PASS | The preview omits a `### Kimi Code` section and explicitly attributes the omission to the absent `.kimi-plugin/plugin.json` in the fixture. |
| `closing_sentence_derived` | PASS | The upgrade section ends with a derived count of 6 role plugins, states there is no verified fixed-version installation path, and directs updates through the default `main` branch without promising pinned synchronization. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=734c4a4cb7e543db5091d9f1c4a08014e2d017a93f5c1b82e54e15f916eb8fba; fixture_sha256=17e20791a9c9288907fb214989bbc6378e7d64a98732f68a5c493285ff25f933; output_sha256=9b8bc20114cc8e4f8a476fee3b0a2a6dc46843e8f791eb917cac7f8823a2c43c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a complete inline GitHub Release preview with the required marketplace title, derived six-plugin upgrade wording, evidence-based platform omissions, and safe closing guidance; raw git evidence shows no mutation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=734c4a4cb7e543db5091d9f1c4a08014e2d017a93f5c1b82e54e15f916eb8fba; fixture_sha256=17e20791a9c9288907fb214989bbc6378e7d64a98732f68a5c493285ff25f933; output_sha256=cb8cbfb03597921f83f87fd975415bdaad9315dfbfbf108e405c8e2de96a22e4; snapshot_sha256=64db1c5e1fcf0d4930550743f83a243186f2e74164b3d3e6cde180e91e4c04a0
- Behavior: Produced a file-backed release preview but retained platform sections/instructions that do not satisfy the stricter assertion requirements; this is comparison context only.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
