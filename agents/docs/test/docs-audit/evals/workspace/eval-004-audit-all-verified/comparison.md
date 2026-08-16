# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-004-audit-all-verified`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897` from `agents/docs/test/docs-audit/evals/workspace/eval-004-audit-all-verified`.
- Identity schema: `2`
- target_skill_sha256: `dafd53371901dfd724f88c70262b157e59494d29da1c613d0ef130564b6ff4f9`
- eval_definition_sha256: `9d29cd503dc3f38e1235bc8d674c667f9fc3bef38d94569b7888bb0dfed80506`
- metadata_sha256: `4c1ab6c77122f43adf1cbc9d6f05aea7b2b047fe1e69ba225e32d03f006dc954`
- fixture_sha256: `085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `a043187f1d82deb6ceb1f6f2a8dbb12db6dd01c71ced16d224de3ae50ca31c3b`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `7e61bd8eca6431729aee1f3be4656be0a4348119eb1218623bafd54cfaead2ab`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `verifies_complete_affected_set` | PASS | The locked candidate record identifies the two change-map-required API pages and all four affected pages as verified, with no unresolved evidence gap. |
| `stamps_all_pages_together` | PASS | Locked delivery snapshots show both API pages stamped to v1.1.0; the release-notes page and index already contain v1.1.0 and remain unchanged, matching the unified-stamp result. |
| `verifies_release_metadata_read_only` | PASS | The candidate record verifies docs/site/.meta/releases.json and explicitly states it was not modified; commit diffs contain no metadata change. |
| `normalizes_mixed_version_forms` | PASS | The candidate record inventories v-prefixed and unprefixed sources, normalizes them to 1.1.0, and records the required source-specific raw forms and equal comparisons. |
| `persists_candidate_producer_schema` | FAIL | The locked candidate record contains the required candidate schema, inventories, locators, hashes, gates, and candidate_verified conclusion, but does not contain the required prior-lineage SHA-256 digest in the candidate record itself. |
| `anchors_candidate_then_discovers_success` | FAIL | Raw Git evidence shows candidate_commit and anchor_commit are the same badd32b commit, contrary to the required distinct post-candidate anchor step; the later handoff commits and fast-forward are present, but the mandated candidate-then-anchor sequence is not satisfied. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c; fixture_sha256=085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897; output_sha256=f69a97f1f40cacff8c528f7829ad451f77f88874e5a29ef174c9f48c086f5f30; snapshot_sha256=d2eb424ce02e2f34d34069a3fbfc62dbd59ca74dca931a12c87b93249fc3f206
- Behavior: Audited the complete affected set, stamped the two stale API pages, preserved release metadata, persisted candidate and handoff artifacts, and integrated by fast-forward, but failed the candidate-schema lineage requirement and distinct anchor sequencing.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c; fixture_sha256=085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897; output_sha256=76ecc0bacd9841e80f45e46a4368f65e7708ffe62deffa6b691f2d819bf478f0; snapshot_sha256=9fdf4fe0a34caa02600862ff2ca9bdab9d0ecc632ed87d474c6cae5f0ce1e309
- Behavior: Produced only a prose audit report, left the stale API stamps unchanged, and did not create the required candidate, anchor, or discovery handoff artifacts.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- persists_candidate_producer_schema: missing required prior-lineage digest in the locked candidate record.
- anchors_candidate_then_discovers_success: candidate and anchor commits are identical, violating the required sequencing.
- Next: Add the prior-lineage digest to the candidate record and rerun validation.
- Next: Create a distinct post-stamp anchor commit after the candidate commit, then regenerate and validate the handoff.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
