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
- Fixture SHA-256: `69659db940208abe97ba4ab195a49c736d9a7ba7e1e880c287d3bf12132c10a3`
- Prompt SHA-256: `62a386a246bcb0c7c5b2df7096cfd60c5023a6b28473d50af8f99649d1d3480e`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b04f0f833fdfe60f19dba4258110d7f6b0a3d6a6f2afb7034b0d3d883c30f83b`
- Skill overlay SHA-256: `960ab70564adb8fafabb98cb333bec48d92a317614465aaf97d281e6a5484a8c`
- Judge schema SHA-256: `1f2ea17b811fce39b8e906ef0e0a70b6a6223a188a2f4a05f2f0a88c54c6aceb`
- Eval definition SHA-256: `05d8b9eb5ccf6bbc077dad850c79899562c5b4ed9bbb4187abffd82f21410ea3`
- Metadata SHA-256: `af301306a3e584e9c32987cd73e02ac298dcd98f38208af58ca0764e8b5a4154`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_release_audit_entry` | PASS | With-skill output identifies the confirmed v1.4.0 entry, scope, evidence sources, and read-only execution boundary. |
| `evaluates_site_release_notes_gate` | PASS | It rejects the handoff as consumable without pre-tag authority/inventory and routes follow-up to docs-audit. |
| `validates_release_window_basis` | FAIL | It references the signed snapshot and target version, but does not explicitly validate the previous-tag comparison anchor v1.3.0. |
| `rejects_missing_pre_tag_authority` | PASS | It explicitly states that no consumable pre-tag audit authority exists and does not claim pre-tag success. |
| `detects_post_tag_evidence_drift` | PASS | It identifies the mismatch between the candidate/tag-entry tree and the actual v1.4.0 tag tree and blocks readiness. |
| `blocks_github_release_handoff` | PASS | It blocks GitHub Release preparation, provides no preview/draft/publish handoff, and assigns docs-audit follow-up. |
| `preserves_no_mutation_boundaries` | PASS | Git evidence shows no ref, commit, worktree, or index mutations; output also states that no tag or GitHub Release writes occurred. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=62a386a246bcb0c7c5b2df7096cfd60c5023a6b28473d50af8f99649d1d3480e; fixture_sha256=69659db940208abe97ba4ab195a49c736d9a7ba7e1e880c287d3bf12132c10a3; output_sha256=cb591b80a100bb926a6f2670a80d48742ab6461da52e05dfc9ea5565debbb4b4; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly preserves the read-only boundary, detects missing audit authority and tag/tree drift, blocks GitHub Release, and routes the next audit step to docs-audit; it omits the explicit previous-tag anchor check.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=62a386a246bcb0c7c5b2df7096cfd60c5023a6b28473d50af8f99649d1d3480e; fixture_sha256=69659db940208abe97ba4ab195a49c736d9a7ba7e1e880c287d3bf12132c10a3; output_sha256=9cd45fb8769d56c2fa4301a7f764ca81b5a45b13d0ab52acf28d2427dff43c6d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline correctly blocks release because the actual tag differs from the audited candidate and authority is missing, but gives a less precise phase/owner handoff.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- validates_release_window_basis
- Next: Explicitly verify and report the v1.3.0 previous tag and v1.4.0 target comparison anchors from the signed snapshot.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
