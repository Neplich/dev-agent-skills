# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-005-integration-release-chain`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `69659db940208abe97ba4ab195a49c736d9a7ba7e1e880c287d3bf12132c10a3` from `agents/docs/test/docs-agent/evals/workspace/eval-005-integration-release-chain`.
- Identity schema: `2`
- target_skill_sha256: `023cc6d8aa109db6ff7dcd662df567ae4f0c79dddb66dfe7bcf6f1eb91d20f39`
- eval_definition_sha256: `05d8b9eb5ccf6bbc077dad850c79899562c5b4ed9bbb4187abffd82f21410ea3`
- metadata_sha256: `af301306a3e584e9c32987cd73e02ac298dcd98f38208af58ca0764e8b5a4154`
- fixture_sha256: `69659db940208abe97ba4ab195a49c736d9a7ba7e1e880c287d3bf12132c10a3`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `1f2ea17b811fce39b8e906ef0e0a70b6a6223a188a2f4a05f2f0a88c54c6aceb`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `62a386a246bcb0c7c5b2df7096cfd60c5023a6b28473d50af8f99649d1d3480e`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `9b4662f75faaa400532cbf63de0f9ad91e1c5da618aac4095cd85a9624829d98`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_release_audit_entry` | PASS | With_skill identifies the docs-audit route, maintainer-confirmed v1.4.0, scope, host, evidence source, and output requirements. |
| `evaluates_site_release_notes_gate` | PASS | It blocks the handoff because no consumable pre-tag authority exists and names the documentation audit owner as the next responsible party, despite the handoff being marked ready. |
| `validates_release_window_basis` | PASS | It refuses to treat the signed snapshot text as sufficient when the referenced Git objects cannot be parsed locally, and does not guess replacement anchors. |
| `rejects_missing_pre_tag_authority` | PASS | It explicitly states that no verifiable pre-tag authority exists and refuses to return ready_for_tag or release_verified. |
| `detects_post_tag_evidence_drift` | FAIL | The signed snapshot directly records v1.4.0 and release-evidence trees differing from the candidate/tag-entry trees, but the with_skill output does not identify this post-tag object drift; it only cites unavailable refs and objects. |
| `blocks_github_release_handoff` | PASS | It concludes the audit is blocked, prohibits progression to GitHub Release preparation, and names the release preparation owner as dependent on ready_for_tag, an actual tag, and release_verified evidence. |
| `preserves_no_mutation_boundaries` | PASS | The output states that no tag or GitHub Release writes were performed; locked git evidence shows no ref delta, commits, or worktree changes. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=62a386a246bcb0c7c5b2df7096cfd60c5023a6b28473d50af8f99649d1d3480e; fixture_sha256=69659db940208abe97ba4ab195a49c736d9a7ba7e1e880c287d3bf12132c10a3; output_sha256=4f2772f7df5b199ff01807a12ce86399b5d374d8aac1aad84f518b279a4e846c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly accepts the audit entry, rejects unsupported pre/post-tag progression, blocks GitHub Release handoff, and preserves read-only boundaries, but misses the explicit post-tag tree-drift finding.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=62a386a246bcb0c7c5b2df7096cfd60c5023a6b28473d50af8f99649d1d3480e; fixture_sha256=69659db940208abe97ba4ab195a49c736d9a7ba7e1e880c287d3bf12132c10a3; output_sha256=6a6b75e2ebf6f1f76dfa183b81b65b2ce7e626608cadc7bb2fe85b5a3b05167e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline also blocks release progression and preserves no-mutation boundaries, but explicitly identifies the tag/tree mismatch and inconsistent release-note metadata.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill lane does not explicitly detect or report the signed snapshot's post-tag tree drift: v1.4.0 and release-evidence point to 490d0b..., while release-candidate, tag-entry, and evidence-expected point to 7c8b9b....
- Next: Require the with_skill output to explicitly compare the signed snapshot's post-tag tag and persisted evidence trees with the expected candidate trees and report the mismatch as blocked.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
