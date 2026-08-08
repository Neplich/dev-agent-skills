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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f95690411417d5e9cf66495e67ce2d96d0a51fc4ca1821536421129a950bb8f3`
- Skill overlay SHA-256: `ee4b811662f5234e9cbcc50a85629526ebcf704244484e48f81d5ce85841d93c`
- Judge schema SHA-256: `03a8fb59a79fd1eace9e70a8f76361828e062efb8e2ad27720ecf0844391b693`
- Eval definition SHA-256: `39c658cc52679808b5a56ed0ccb078241d74aac73ea7ef1462e40e6679aac516`
- Metadata SHA-256: `b64763ea1d58b4c3c1d7a3e95d4a1d7bd5f4195151868d0276dd82eda387eb3e`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `title_matches_marketplace_format` | PASS | With-skill preview title is `v1.0.0 - 文件卡片、统一附件模型与失败消息重试`, a nonempty fact-based topic overview. |
| `upgrade_note_first_sentence` | PASS | The first sentence of `## 升级说明` is exactly `无破坏性变更，也没有新增 plugin。7 个 role plugin 均更新到 \`v1.0.0\`。` |
| `claude_section_verbatim` | PASS | The with-skill body contains the required Claude Code marketplace update, all seven manifest role-plugin update commands in the specified membership, `/reload-plugins`, and the no-version-pin explanation directing fixed installs to Codex or Kimi. |
| `codex_section_pinned_install` | PASS | The Codex section uses the required raw tag URL ending in `refs/tags/v1.0.0/.codex/INSTALL.md` and sets `TARGET_TAG=v1.0.0`. |
| `kimi_section_plugin_install` | PASS | The Kimi Code section uses `/plugins install https://github.com/Neplich/dev-agent-skills/releases/tag/v1.0.0`. |
| `plugin_list_derived_from_manifest` | PASS | The seven listed role plugins match the seven entries in the target `.claude-plugin/marketplace.json`: pm-agent, designer-agent, engineer-agent, qa-agent, devops-agent, security-agent, and docs-agent. |
| `closing_sentence_present` | PASS | The upgrade section closes with `更新仓库后重新运行安装器，即可同步全部 7 个 role plugin 的 \`v1.0.0\` 能力。` |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a62a94b930216669961977d81dd33c33ea8ab99e80d1ccbdd52769d4a9afaf75; fixture_sha256=dc5fdc0f377589e2a17429105072ec9f0f122806b4874d8f07072dd9a6c6c26b; output_sha256=d57534b029426881790b05a8495a81c96f23aa5c29f44e3147360604a1ef1119; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a complete inline GitHub Release preview with a compliant title, fact-grounded release body, manifest-derived seven-plugin upgrade instructions, pinned Codex and release-URL Kimi installation paths, and no GitHub write.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a62a94b930216669961977d81dd33c33ea8ab99e80d1ccbdd52769d4a9afaf75; fixture_sha256=dc5fdc0f377589e2a17429105072ec9f0f122806b4874d8f07072dd9a6c6c26b; output_sha256=815268503d58c22248c3909e862ea5dd7edf238c8facffd47ffc48ab5fcd3568; snapshot_sha256=6d3c920c8be0a0d0a9486717864f3d0642e193456e4b9a4abd2456853e8bd3af
- Behavior: Produced a file-backed preview, but used a noncompliant bare-style title and omitted the required detailed Claude, Codex, Kimi, manifest-derived plugin list, and exact upgrade-section requirements; it also asserted documentation checks passed despite the candidate prose reporting the package was missing.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `380b2fcfd0ff29b900d02472045d511ad62a16c847b128cbfdce8af3c7a60338`
- Skill overlay SHA-256: `c666691beb368144f31c0354fd118ef20d664151476cfb1c8695e6ee7c490aa7`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `39c658cc52679808b5a56ed0ccb078241d74aac73ea7ef1462e40e6679aac516`
- Metadata SHA-256: `b64763ea1d58b4c3c1d7a3e95d4a1d7bd5f4195151868d0276dd82eda387eb3e`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `title_matches_marketplace_format` | PASS | With-skill inline preview title is `v1.0.0 - 文件附件与可靠升级`, with a non-empty fact-based overview. |
| `upgrade_note_first_sentence` | PASS | The 升级说明 section begins with the required sentence, using 7 role plugins derived from marketplace.json. |
| `claude_section_verbatim` | PASS | Claude Code section contains marketplace update, all 7 manifest role-plugin update commands, reload command, and explains that `/plugin update` has no version pin and fixed versions require Codex or Kimi. |
| `codex_section_pinned_install` | PASS | Codex section references the v1.0.0 raw-tag INSTALL.md URL and sets `TARGET_TAG=v1.0.0`. |
| `kimi_section_plugin_install` | PASS | Kimi Code section contains `/plugins install https://github.com/Neplich/dev-agent-skills/releases/tag/v1.0.0`. |
| `plugin_list_derived_from_manifest` | PASS | The preview lists exactly the 7 role plugins registered in the target marketplace manifest. |
| `closing_sentence_present` | PASS | Upgrade instructions end with the required sentence stating that all 7 role plugins synchronize to v1.0.0. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a62a94b930216669961977d81dd33c33ea8ab99e80d1ccbdd52769d4a9afaf75; fixture_sha256=dc5fdc0f377589e2a17429105072ec9f0f122806b4874d8f07072dd9a6c6c26b; output_sha256=0cd423c923b70a8968f1536938b4de9631041915190f72263d10f29c9e4eb570; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced an inline-only, non-mutating GitHub Release preview with the required marketplace-derived title, upgrade wording, seven-plugin list, and Claude Code, Codex, and Kimi Code instructions.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a62a94b930216669961977d81dd33c33ea8ab99e80d1ccbdd52769d4a9afaf75; fixture_sha256=dc5fdc0f377589e2a17429105072ec9f0f122806b4874d8f07072dd9a6c6c26b; output_sha256=4ca1b1d0db86f191ef187289a45f38d1c10d536f832b5d2fe73529fcae364989; snapshot_sha256=84c7accab71a828a3fde1f2a2d132de22d39b86200948b1d21f6bd1e6b4297a7
- Behavior: Created an unrelated release preview focused on file-card application changes and omitted the required marketplace upgrade sections and exact installation guidance.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `bfa553ee1e9614c42bec50e00faa33ed1a614260acdb1011ab1116e8b73db2dd`
- Skill overlay SHA-256: `0db0717c5ca83fddc3ecdfe8bf130c8885c13a22148bb9bf0d8e93c491b17294`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `39c658cc52679808b5a56ed0ccb078241d74aac73ea7ef1462e40e6679aac516`
- Metadata SHA-256: `b64763ea1d58b4c3c1d7a3e95d4a1d7bd5f4195151868d0276dd82eda387eb3e`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `title_matches_marketplace_format` | PASS | With_skill output provides the non-empty, fact-related title `v1.0.0 - 文件附件、失败重试与双架构交付` and treats it as preview-only. |
| `upgrade_note_first_sentence` | PASS | The `升级说明` section begins exactly with `无破坏性变更，也没有新增 plugin。7 个 role plugin 均更新到 v1.0.0。`. |
| `claude_section_verbatim` | PASS | The output includes the required marketplace update, all seven specified `/plugin update` commands, `/reload-plugins`, and the no-version-pin/durable-install limitation with Codex/Kimi alternatives. |
| `codex_section_pinned_install` | PASS | The Codex section references the v1.0.0 raw `.codex/INSTALL.md` URL and sets `TARGET_TAG=v1.0.0`. |
| `kimi_section_plugin_install` | PASS | The Kimi Code section includes `/plugins install https://github.com/Neplich/dev-agent-skills/releases/tag/v1.0.0`. |
| `plugin_list_derived_from_manifest` | PASS | The output states there are 7 role plugins and lists the same seven manifest members used in the Claude commands: pm, designer, engineer, qa, devops, security, and docs. |
| `closing_sentence_present` | PASS | The upgrade section ends with `更新仓库后重新运行安装器，即可同步全部 7 个 role plugin 的 v1.0.0 能力。`. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a62a94b930216669961977d81dd33c33ea8ab99e80d1ccbdd52769d4a9afaf75; fixture_sha256=dc5fdc0f377589e2a17429105072ec9f0f122806b4874d8f07072dd9a6c6c26b; output_sha256=6511ebff6fbc30c678015a4b804c61f52272442d67d920fd8a0186de81a6399f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a complete semantically compliant preview in the candidate output, including manifest-derived plugin instructions and pinned Codex/Kimi paths, without mutating the workspace or creating a draft.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a62a94b930216669961977d81dd33c33ea8ab99e80d1ccbdd52769d4a9afaf75; fixture_sha256=dc5fdc0f377589e2a17429105072ec9f0f122806b4874d8f07072dd9a6c6c26b; output_sha256=7d664e3fceb20c73b8f4fa74612538876fea91317866ce5068f1ade4f5b37741; snapshot_sha256=05dde696fadba4fc8bc59278108947759d0cc2378490025bb3cb5ab9ac09a05d
- Behavior: Created an untracked preview file, but its content was a generic English release draft and did not provide the required structured upgrade instructions.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `bfa553ee1e9614c42bec50e00faa33ed1a614260acdb1011ab1116e8b73db2dd`
- Skill overlay SHA-256: `0db0717c5ca83fddc3ecdfe8bf130c8885c13a22148bb9bf0d8e93c491b17294`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `39c658cc52679808b5a56ed0ccb078241d74aac73ea7ef1462e40e6679aac516`
- Metadata SHA-256: `b64763ea1d58b4c3c1d7a3e95d4a1d7bd5f4195151868d0276dd82eda387eb3e`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `title_matches_marketplace_format` | PASS | With-skill title is `v1.0.0 - 文件卡片、失败重试与统一附件模型`, a non-empty fact-based summary. |
| `upgrade_note_first_sentence` | PASS | The upgrade section begins with the required sentence and uses 7, matching the marketplace manifest. |
| `claude_section_verbatim` | PASS | Claude Code section includes the marketplace update command, all seven required plugin update commands, reload command, no-version-pin limitation, and Codex/Kimi fixed-version guidance. |
| `codex_section_pinned_install` | PASS | Codex section references the v1.0.0 raw INSTALL.md URL and sets `TARGET_TAG=v1.0.0`. |
| `kimi_section_plugin_install` | PASS | Kimi Code section contains the required v1.0.0 release installation URL. |
| `plugin_list_derived_from_manifest` | PASS | The command list contains exactly the seven role plugins registered in `.claude-plugin/marketplace.json`. |
| `closing_sentence_present` | PASS | Upgrade section ends with the required sentence naming all 7 role plugins and `v1.0.0`. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a62a94b930216669961977d81dd33c33ea8ab99e80d1ccbdd52769d4a9afaf75; fixture_sha256=dc5fdc0f377589e2a17429105072ec9f0f122806b4874d8f07072dd9a6c6c26b; output_sha256=ad335446e57489b86ce0802e186eb7eb2ca69830f007deeb1197166e572347b3; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a semantically compliant GitHub Release preview, preserved preview-only scope, and correctly deferred draft creation pending remote checks and approval.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a62a94b930216669961977d81dd33c33ea8ab99e80d1ccbdd52769d4a9afaf75; fixture_sha256=dc5fdc0f377589e2a17429105072ec9f0f122806b4874d8f07072dd9a6c6c26b; output_sha256=0e42eef76cf7b2a5e47353a776804d8d0a441cc7eb0d59f0227588f32d8e0c50; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a generic release draft with an invalid title format and omitted the required structured upgrade instructions.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `793cabc84dc1947c3d6386a1d060276eea2eb8b4e9de25fdd6c7b7a60fb82cb0`
- Skill overlay SHA-256: `ecc021af86f838c5c915ade1c1e1095fa203f789350af9aa701ad32bae876bb2`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `39c658cc52679808b5a56ed0ccb078241d74aac73ea7ef1462e40e6679aac516`
- Metadata SHA-256: `b64763ea1d58b4c3c1d7a3e95d4a1d7bd5f4195151868d0276dd82eda387eb3e`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `title_matches_marketplace_format` | PASS | With-skill title is `v1.0.0 - 文件卡片、统一附件模型与失败消息重试`, a non-empty fact-based marketplace-format title. |
| `upgrade_note_first_sentence` | PASS | The upgrade section begins exactly with `无破坏性变更，也没有新增 plugin。7 个 role plugin 均更新到 `v1.0.0`。`. |
| `claude_section_verbatim` | FAIL | The required commands and seven plugin entries are present, and pinning is discouraged, but it does not explicitly state that the durable正文 cannot guarantee a fixed `v1.0.0` installation. |
| `codex_section_pinned_install` | PASS | The Codex section references the v1.0.0 raw `.codex/INSTALL.md` URL and sets `TARGET_TAG=v1.0.0`. |
| `kimi_section_plugin_install` | PASS | The Kimi section contains `/plugins install https://github.com/Neplich/dev-agent-skills/releases/tag/v1.0.0`. |
| `plugin_list_derived_from_manifest` | PASS | The with-skill output lists exactly the seven manifest role plugins: pm-agent, designer-agent, engineer-agent, qa-agent, devops-agent, security-agent, and docs-agent. |
| `closing_sentence_present` | PASS | The upgrade section ends with `更新仓库后重新运行安装器，即可同步全部 7 个 role plugin 的 `v1.0.0` 能力。`. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a62a94b930216669961977d81dd33c33ea8ab99e80d1ccbdd52769d4a9afaf75; fixture_sha256=dc5fdc0f377589e2a17429105072ec9f0f122806b4874d8f07072dd9a6c6c26b; output_sha256=09a3235fa470286a2537acd89c5a8feae549fbc582d1e7bc75c60e30390d750c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a fact-grounded, non-publishing preview satisfying six of seven assertions; the Claude section lacks the required explicit durable正文 fixed-version limitation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a62a94b930216669961977d81dd33c33ea8ab99e80d1ccbdd52769d4a9afaf75; fixture_sha256=dc5fdc0f377589e2a17429105072ec9f0f122806b4874d8f07072dd9a6c6c26b; output_sha256=31460eda89734050342d18ce90998ab44329554ba3b59fdf53795a0d81412915; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a generic release preview with an unsuitable title and omitted the required structured client-specific installation sections.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill Claude Code section does not explicitly state that durable正文 cannot guarantee installation pinned to `v1.0.0`.
- Next: Add the explicit durable正文 limitation to the Claude Code section.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `ebd2c00966a7932d251daeeef05573b0145183fe908cf102225636115f85820c`
- Skill overlay SHA-256: `2398a04c1c550bc8e45aa1564f5f42f6e629a29d1c1ed530494ae269f918d169`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `39c658cc52679808b5a56ed0ccb078241d74aac73ea7ef1462e40e6679aac516`
- Metadata SHA-256: `b64763ea1d58b4c3c1d7a3e95d4a1d7bd5f4195151868d0276dd82eda387eb3e`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `title_matches_marketplace_format` | PASS | With-skill preview title is `v1.0.0 - 文件卡片、统一附件模型与失败重试`, with non-empty fact-based overview. |
| `upgrade_note_first_sentence` | PASS | Upgrade section begins with the required no-breaking-change/no-new-plugin statement and 7 plugins updated to `v1.0.0`. |
| `claude_section_verbatim` | PASS | Includes the marketplace update command, all 7 required plugin update commands, reload command, and the no-version-pin limitation with Codex/Kimi guidance. |
| `codex_section_pinned_install` | PASS | Includes the tag-specific raw `.codex/INSTALL.md` URL and `TARGET_TAG=v1.0.0`. |
| `kimi_section_plugin_install` | PASS | Includes `/plugins install https://github.com/Neplich/dev-agent-skills/releases/tag/v1.0.0`. |
| `plugin_list_derived_from_manifest` | PASS | Lists exactly the 7 role plugins registered in the fixture marketplace manifest. |
| `closing_sentence_present` | PASS | Upgrade section ends with the required sentence about rerunning the installer to sync all 7 plugins' `v1.0.0` capabilities. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a62a94b930216669961977d81dd33c33ea8ab99e80d1ccbdd52769d4a9afaf75; fixture_sha256=dc5fdc0f377589e2a17429105072ec9f0f122806b4874d8f07072dd9a6c6c26b; output_sha256=5fba229cdf66824dbe2d8aa15723bbfb3d176c7e8626d706ea652605f0c17733; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a preview-only release draft with the required title, fact-bounded upgrade text, manifest-derived plugin list, and pinned Codex/Kimi installation paths.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a62a94b930216669961977d81dd33c33ea8ab99e80d1ccbdd52769d4a9afaf75; fixture_sha256=dc5fdc0f377589e2a17429105072ec9f0f122806b4874d8f07072dd9a6c6c26b; output_sha256=44b76fa8f418fe9830a89d4d929f61478828d7a202b2aa9dd354f56909b7c818; snapshot_sha256=3e11a8cb851d572b0ed6c082452c6f780c32d0c7962746904d4f39e45ad87f6f
- Behavior: Produced a preview file, but used a nonconforming title and generic upgrade/install content without the required manifest-derived command structure.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
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

# Eval Result: eval-007-marketplace-full-capability-upgrade-note

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-release-gen`
- Eval: `eval-007-marketplace-full-capability-upgrade-note`
- Test case: `marketplace 当前 tag 能力齐全的标题强格式与升级说明正向分支`
- Prompt:

> 请根据 `release-package.md`、`docs/site/release-notes/v1.0.0.md` 和 `github-evidence.md` 准备 GitHub Release 预览。本仓库是 dev-agent-skills marketplace 宿主，目标 tag 的插件内容见 `.claude-plugin/marketplace.json`、`.codex/INSTALL.md` 与 `.kimi-plugin/plugin.json`。

- Expected output:

> 标题为 `v1.0.0 - {主题概述}` 强格式；正文四节中「升级说明」按固定结构呈现：简述句（无破坏性变更，也没有新增 plugin。7 个 role plugin 均更新到 `v1.0.0`。）、### Claude Code 小节（9 行指令 + 无版本 pin 限制说明）、### Codex 小节（引用目标 tag 的 .codex/INSTALL.md 并设 TARGET_TAG=v1.0.0）、### Kimi Code 小节（/plugins install 目标 release URL）与收尾句（更新仓库后重新运行安装器，即可同步全部 7 个 role plugin 的 `v1.0.0` 能力。）；plugin 指令列表按目标版本 marketplace.json 推导。

## Test Set / Fresh Run

- Eval schema: `evals.json` v1.0。
- Fixture manifest: `edc8f94a65adc55e0678ac62eedc62d16f0ef2ba75af261ea8c90725c12656ab`（6 个可见文件；两侧逐字节一致）。
- Repository HEAD: `47adbbc9`。
- Fresh run window: 2026-08-07 00:58–01:14（Asia/Shanghai）。
- Runtime: 3 个独立会话，均为 `gpt-5.6-luna`、`model_reasoning_effort=medium`：fresh without-skill、fresh with-skill、fresh judge。
- Controlled variable: 两个 candidate 使用完全相同的 prompt、fixture manifest、HOME/CODEX_HOME 目录形态与同一份 `auth.json`；唯一变量是 with-skill lane 安装并加载目标 specialist skill。
- Physical isolation: 按 skill 先完成并销毁全部 baseline 随机顶层根，再创建 with-skill 根；32 个 candidate 全部完成并销毁后才创建第三套 judge 根。
- Candidate visibility: lane 中未放入 `eval_metadata.json`、`evals.json`、`expected_output`、assertions、历史 `comparison.md`、README 脚手架或 judge 材料；泄漏扫描为 0 命中。
- External data rule: 实时实体因 GitHub 认证、网络或当时集合缺失而不可得时，相关 assertion 记为 `NOT EXERCISED`，只影响 Coverage，不伪造成 Behavior 的 PASS/FAIL。

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL**
- Overall result: PASS
- With-skill summary: with_skill 实际加载 github-release-gen（status.json skill_load_hits=2；transcript item_1/item_2 读取技能及其 references），按正确顺序读取发布证据和三个宿主元数据，未执行写入；candidate 输出满足全部 7 条断言。

## Historical Contract Note

- 旧 durable 结果因 issue #234 的 prompt/fixture 泄漏修复或后续 assertion 增强而标记为 `BLOCKED`。本文件已由当前契约下的 fresh paired run 与独立 judge 结论覆盖。
- 本轮没有复用历史 baseline、candidate、verdict 或旧结论；without-skill baseline 仅作行为对照，不参与 with-skill 的 Behavior/Coverage 判定。

## With-Skill Behavior

with_skill 实际加载 github-release-gen（status.json skill_load_hits=2；transcript item_1/item_2 读取技能及其 references），按正确顺序读取发布证据和三个宿主元数据，未执行写入；candidate 输出满足全部 7 条断言。

## Without-Skill Baseline

without_skill 未加载目标 skill（skill_load_hits=0），仅作对照：输出使用裸版本标题、非固定升级结构且未给出完整指令列表。

## Assertion Review

| Assertion | With skill | Evidence / reason | Without-skill comparison |
| --- | --- | --- | --- |
| `title_matches_marketplace_format` | **PASS** | with_skill candidate 的 Title 为 `v1.0.0 - 文件卡片、统一附件契约与失败消息重试`，符合 `v{VERSION} - {主题概述}`，且概述对应发布事实。trace item_1/item_2 显示先读取 github-release-gen 及 release-outline；未发现脚手架泄漏。 | without_skill candidate 仅输出 `# Dev Agent Skills v1.0.0`，不符合 marketplace 强格式。 |
| `upgrade_note_first_sentence` | **PASS** | candidate 的「升级说明」首段精确为「无破坏性变更，也没有新增 plugin。7 个 role plugin 均更新到 `v1.0.0`。」；trace item_7 通过 marketplace 一致性检查确认 7 个 plugins。 | without_skill 只在后文笼统写“没有新增 plugin，marketplace 保持 7 个 role plugins”，未按要求首句固定呈现。 |
| `claude_section_verbatim` | **PASS** | candidate 含 `### Claude Code`，先给出无版本 pin 限制及固定版本需用 Codex/Kimi 的说明，随后完整列出 marketplace update、7 个指定 role 的 update 和 reload-plugins，共 9 行指令，成员与顺序均匹配 marketplace.json。 | without_skill 仅用安装方式概述，没有完整的 9 行固定指令，也未给出所需的明确 durable 正文限制说明。 |
| `codex_section_pinned_install` | **PASS** | candidate 含 `### Codex`，引用 `https://raw.githubusercontent.com/Neplich/dev-agent-skills/refs/tags/v1.0.0/.codex/INSTALL.md` 并明确 setting `TARGET_TAG=v1.0.0`；fixture-manifest 与 trace item_2 证明目标 `.codex/INSTALL.md` 已读取。 | without_skill 使用 GitHub blob URL 的泛化安装描述，不符合要求的 raw tag URL 结构。 |
| `kimi_section_plugin_install` | **PASS** | candidate 含 `### Kimi Code`，指令精确为 `/plugins install https://github.com/Neplich/dev-agent-skills/releases/tag/v1.0.0`；目标 `.kimi-plugin/plugin.json` 在 fixture-manifest 和 trace item_2 中有证据。 | without_skill 仅概述使用 `/plugins install`，未给出精确 release URL 指令。 |
| `plugin_list_derived_from_manifest` | **PASS** | candidate 的 Claude Code 列表正好包含 pm-agent、designer-agent、engineer-agent、qa-agent、devops-agent、security-agent、docs-agent 7 个成员；trace item_7 输出 `marketplace ... 7 plugins`，与 `.claude-plugin/marketplace.json` 一致。 | without_skill 未列出 7 个 role plugin 的完整指令列表。 |
| `closing_sentence_present` | **PASS** | candidate 的升级说明以「更新仓库后重新运行安装器，即可同步全部 7 个 role plugin 的 `v1.0.0` 能力。」收尾，文本精确匹配要求。 | without_skill 没有该固定收尾句。 |

## Failures

- 无 with-skill assertion failure。

## Not Exercised

- 无；本轮覆盖全部 assertions。

## Next Steps

- 保留当前回归覆盖；目标 skill、fixture 或 assertion 契约变化时重新执行 fresh paired validation。

## Runtime Evidence

- With-skill candidate: return code `0`，duration `120.418s`，`skill_load_hits=2`。
- Without-skill candidate: return code `0`，duration `107.237s`，`skill_load_hits=0`。
- Independent judge: return code `0`，duration `83.485s`。
- Judge 已读取两侧最终输出、完整 JSONL 工具 trace、before/after workspace snapshot、fixture manifest 与 session status，并核验读取顺序和零写入边界。
- 所有临时 HOME/CODEX_HOME 与 candidate/judge 随机顶层根均已销毁；持久化证据目录中不存在 `auth.json`。

## Runtime Artifact Policy

- 仓库只持久化本 canonical `comparison.md`。
- Candidate、transcript、judge verdict、timing、status、snapshot 与 diagnostics 仅作为 `/tmp` 运行期证据，不提交到 git。
