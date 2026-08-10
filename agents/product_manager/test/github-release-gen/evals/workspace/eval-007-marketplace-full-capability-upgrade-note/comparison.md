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
- Fixture SHA-256: `dc5fdc0f377589e2a17429105072ec9f0f122806b4874d8f07072dd9a6c6c26b`
- Prompt SHA-256: `a62a94b930216669961977d81dd33c33ea8ab99e80d1ccbdd52769d4a9afaf75`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `0c9b1305da43afbfc22e6d563651831ce45be05793224d552c008cc393a37b1e`
- Skill overlay SHA-256: `2f0de1beb8d9a238bffa058ef4ccfb94546f593a81b4fc6e5c1f6bcddf8dbe71`
- Judge schema SHA-256: `03a8fb59a79fd1eace9e70a8f76361828e062efb8e2ad27720ecf0844391b693`
- Eval definition SHA-256: `ddd9a7434f92d092aeb7262a95bca81739e99a684c38e41461345200798e8931`
- Metadata SHA-256: `b64763ea1d58b4c3c1d7a3e95d4a1d7bd5f4195151868d0276dd82eda387eb3e`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `title_matches_marketplace_format` | PASS | With-skill preview title is `v1.0.0 - 文件卡片、统一附件模型与失败消息重试`, with a non-empty fact-based topic. |
| `upgrade_note_first_sentence` | PASS | The upgrade section begins with the required sentence: `无破坏性变更，也没有新增 plugin。7 个 role plugin 均更新到 v1.0.0。` |
| `claude_section_verbatim` | PASS | The Claude Code section includes marketplace update, all seven manifest role update commands, reload, no-version-pin behavior, and Codex/Kimi fixed-version guidance. |
| `codex_section_pinned_install` | PASS | The Codex section uses the required raw tag URL and sets `TARGET_TAG=v1.0.0`. |
| `kimi_section_plugin_install` | PASS | The Kimi Code section uses `/plugins install https://github.com/Neplich/dev-agent-skills/releases/tag/v1.0.0`. |
| `plugin_list_derived_from_manifest` | PASS | The command list contains exactly the seven role plugins registered in the marketplace manifest. |
| `closing_sentence_present` | PASS | The upgrade section ends with the required sentence about rerunning the installer and synchronizing all seven role plugins. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a62a94b930216669961977d81dd33c33ea8ab99e80d1ccbdd52769d4a9afaf75; fixture_sha256=dc5fdc0f377589e2a17429105072ec9f0f122806b4874d8f07072dd9a6c6c26b; output_sha256=ccfd59411c0f5f85fdf11b308d4bff78baed8bc296ffdb9b55885e616f65bd76; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced an inline release preview with the required marketplace-derived title, upgrade wording, seven-plugin Claude commands, pinned Codex install, Kimi release install, and closing sentence; no repository or GitHub mutation occurred.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a62a94b930216669961977d81dd33c33ea8ab99e80d1ccbdd52769d4a9afaf75; fixture_sha256=dc5fdc0f377589e2a17429105072ec9f0f122806b4874d8f07072dd9a6c6c26b; output_sha256=ef89a319c345bdccf5afc793698120aab1874432456e20f3fdbd3924261baa29; snapshot_sha256=59467410fb2e11f29b78d1a82696b2b0aac5c8c358e6efd09c12fd3370541125
- Behavior: Produced a file-backed preview, but its title and installation content did not satisfy the required structured marketplace upgrade assertions.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
