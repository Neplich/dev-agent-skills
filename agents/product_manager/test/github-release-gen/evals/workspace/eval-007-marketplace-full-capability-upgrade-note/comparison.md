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
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
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
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
