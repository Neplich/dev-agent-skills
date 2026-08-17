# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-release-gen`
- Eval: `eval-007-marketplace-full-capability-upgrade-note`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `dc5fdc0f377589e2a17429105072ec9f0f122806b4874d8f07072dd9a6c6c26b` from `agents/product_manager/test/github-release-gen/evals/workspace/eval-007-marketplace-full-capability-upgrade-note`.
- Identity schema: `2`
- target_skill_sha256: `ed7c0a44968df88c4831e9abe2b9be4922e4fa2cd6bcbd8dc6dd7e927ff9c87a`
- eval_definition_sha256: `ddd9a7434f92d092aeb7262a95bca81739e99a684c38e41461345200798e8931`
- metadata_sha256: `b64763ea1d58b4c3c1d7a3e95d4a1d7bd5f4195151868d0276dd82eda387eb3e`
- fixture_sha256: `dc5fdc0f377589e2a17429105072ec9f0f122806b4874d8f07072dd9a6c6c26b`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `03a8fb59a79fd1eace9e70a8f76361828e062efb8e2ad27720ecf0844391b693`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `a62a94b930216669961977d81dd33c33ea8ab99e80d1ccbdd52769d4a9afaf75`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `41bf9818330e1ae365d336932a5653b591537342874ba68ae701f1478bc7b159`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `title_matches_marketplace_format` | PASS | With-skill preview title is `v1.0.0 - 文件卡片、失败重试与统一附件模型`, matching the required format with a factual non-empty summary. |
| `upgrade_note_first_sentence` | PASS | The first substantive sentence under `## 升级说明` exactly states that there are no breaking changes or new plugins and that all 7 role plugins update to `v1.0.0`. |
| `claude_section_verbatim` | PASS | The Claude Code section includes the marketplace update command, all 7 required role-specific update commands, `/reload-plugins`, and the no-version-pin limitation with fixed-version alternatives. |
| `codex_section_pinned_install` | PASS | The Codex section uses the required raw GitHub tag URL and sets `TARGET_TAG=v1.0.0`. |
| `kimi_section_plugin_install` | PASS | The Kimi Code section uses `/plugins install https://github.com/Neplich/dev-agent-skills/releases/tag/v1.0.0`. |
| `plugin_list_derived_from_manifest` | PASS | The preview lists exactly the 7 role plugins registered in the fixture marketplace manifest: pm-agent, designer-agent, engineer-agent, qa-agent, devops-agent, security-agent, and docs-agent. |
| `closing_sentence_present` | PASS | The upgrade section ends with the required sentence about rerunning the installer to sync all 7 role plugins at `v1.0.0`. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a62a94b930216669961977d81dd33c33ea8ab99e80d1ccbdd52769d4a9afaf75; fixture_sha256=dc5fdc0f377589e2a17429105072ec9f0f122806b4874d8f07072dd9a6c6c26b; output_sha256=e5d9968c61f3b21732b04d91bbf2a96fe51947553af353cb52cef991639c2cc1; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a compliant, read-only GitHub Release preview with the required title, upgrade guidance, host-specific installation instructions, manifest-derived plugin list, and closing sentence.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a62a94b930216669961977d81dd33c33ea8ab99e80d1ccbdd52769d4a9afaf75; fixture_sha256=dc5fdc0f377589e2a17429105072ec9f0f122806b4874d8f07072dd9a6c6c26b; output_sha256=f7a3386748df89c913e11d5a0db78f9ab555c8b950606fb280456d038678431f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a fresh baseline preview but used an invalid title format and omitted the required structured host-specific commands and upgrade wording.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
