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
- Source lock SHA-256: `c58f04d32c2ca3a22aec96f7ee027af648da5971453d2a5553d7ab2cd9272551`
- Prompt SHA-256: `62a386a246bcb0c7c5b2df7096cfd60c5023a6b28473d50af8f99649d1d3480e`
- Repository HEAD: `60a4b3602dc07f3f6683a8873529bbdba6f8d27d`
- Repository worktree state: **CLEAN**
- Skill overlay SHA-256: `9b4662f75faaa400532cbf63de0f9ad91e1c5da618aac4095cd85a9624829d98`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_release_audit_entry` | PASS | With-skill output explicitly confirms the router entry, version, scope, host repository, evidence source, and read-only boundary. |
| `evaluates_site_release_notes_gate` | PASS | It rejects the handoff's ready label as a substitute for authoritative docs-audit evidence, blocks the gate, and identifies docs-audit ownership. |
| `validates_release_window_basis` | NOT_EXERCISED | The output confirms tag existence and references the Git snapshot, but does not explicitly validate the previous-tag/comparison-anchor basis. |
| `rejects_missing_pre_tag_authority` | PASS | It explicitly states that no confirmed pre-tag audit authority exists and refuses to treat the handoff or page state as verified. |
| `detects_post_tag_evidence_drift` | PASS | It identifies the differing release-candidate/tag-entry tree versus actual tag tree and marks the post-tag path blocked. |
| `blocks_github_release_handoff` | PASS | It concludes the chain cannot continue to GitHub Release preparation and directs remediation and re-audit before handoff. |
| `preserves_no_mutation_boundaries` | PASS | The output states that no tag or GitHub Release write occurred; locked git evidence also shows no mutation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=62a386a246bcb0c7c5b2df7096cfd60c5023a6b28473d50af8f99649d1d3480e; fixture_sha256=69659db940208abe97ba4ab195a49c736d9a7ba7e1e880c287d3bf12132c10a3; output_sha256=33ef93bb484d928281b9c9bd315799d3ba6f9d6d946011f6365460b3c75c9ce3; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly blocks the release flow on missing pre-tag authority and tag/tree drift while preserving read-only boundaries.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=62a386a246bcb0c7c5b2df7096cfd60c5023a6b28473d50af8f99649d1d3480e; fixture_sha256=69659db940208abe97ba4ab195a49c736d9a7ba7e1e880c287d3bf12132c10a3; output_sha256=a2278a121c20c55fb6d901083aa300401242348a54fb60a23d10e3fe65bdef1b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Also blocks release, but provides a less structured audit and does not establish the docs-audit routing as clearly.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Explicitly validate and report the previous-tag and comparison-anchor window basis in a rerun.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
