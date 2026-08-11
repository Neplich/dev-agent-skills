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
- Fixture SHA-256: `085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897`
- Prompt SHA-256: `f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c`
- Repository HEAD: `fecf485e8e3dcaf191b2b221d9cccbddfdea0b72`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5b11b38c1c44c386fe19122dfb1ce5918b2bfbc4830ad32aa994d8a7e39f35e7`
- Skill overlay SHA-256: `85c4ae0a1d58505c4a23c34e6f9116aed81a09b4b6270e3ce148424084f6c7e0`
- Judge schema SHA-256: `a043187f1d82deb6ceb1f6f2a8dbb12db6dd01c71ced16d224de3ae50ca31c3b`
- Eval definition SHA-256: `9d29cd503dc3f38e1235bc8d674c667f9fc3bef38d94569b7888bb0dfed80506`
- Metadata SHA-256: `4c1ab6c77122f43adf1cbc9d6f05aea7b2b047fe1e69ba225e32d03f006dc954`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `verifies_complete_affected_set` | PASS | Candidate record binds the target-tree impact set, matches both required API docs, lists all four affected pages as verified, and states no unresolved blockers. |
| `stamps_all_pages_together` | PASS | Delivered API blobs show both stale stamps changed to v1.1.0; the Release Notes page and index already contain v1.1.0 and are included in the pre/post candidate inventories with successful stamp readback. |
| `verifies_release_metadata_read_only` | PASS | The candidate inventory records docs/site/.meta/releases.json as a read-only git-file source with matching v1.1.0 metadata, and git evidence shows no metadata modification. |
| `normalizes_mixed_version_forms` | PASS | The version inventory records v1.1.0 and 1.1.0 in their required source forms, normalizes both to 1.1.0, and reports equality across confirmation, package, metadata, index, and release-page sources. |
| `persists_candidate_producer_schema` | PASS | The locked candidate blob contains the required candidate schema, immutable refs, impact and page evidence, locator contracts, hashes, canonical inventory digest, prior lineage digest, staged inventories, commands, and candidate_verified conclusion without ready_for_tag or post-commit claims. |
| `anchors_candidate_then_discovers_success` | PASS | Raw git evidence shows the candidate commit, then anchor commit, then handoff commit; the delivered handoff blob contains ready_for_tag discovery data, anchor and candidate identities, post-commit confirmation, and the integrated branch ends at the handoff commit with a clean tree. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c; fixture_sha256=085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897; output_sha256=c6362057354108a70fa0e7b494c86213374f4568cea3e4109741999093c5088b; snapshot_sha256=0d7290de94efa6bca38ccb04254d0d6ade252e9511ec1c286e572ccf74f93984
- Behavior: Completed the full pre-tag audit transaction: verified all affected pages, stamped the stale API pages, persisted the candidate, created and confirmed anchor and handoff commits, fast-forwarded integration, and returned ready_for_tag.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c; fixture_sha256=085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897; output_sha256=d7e30e3ad6096fdb5a69073876bc5810f8553e49a41f1ecbb0006f090e38a580; snapshot_sha256=39b518e6ffd56bffb43b339ed320250cf25cbc25154aa7cdb65c02cfa9f8a90c
- Behavior: Produced a standalone conditional audit report, correctly identified stale API verification stamps and read-only metadata, but did not perform the required stamping, candidate persistence, anchor, handoff, or integration workflow.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
