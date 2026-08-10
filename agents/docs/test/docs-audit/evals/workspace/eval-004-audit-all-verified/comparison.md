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
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5b5823d2c0804ce3dabb1d32490f71697f4ff111cd9371ebf92d1bb1b6ad2188`
- Skill overlay SHA-256: `c7033e85898ff61111eb14edc47b25e717119ee79349d7af461390afc706db78`
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
| `verifies_complete_affected_set` | PASS | Candidate record lists all four affected pages, marks each final_status as verified, and reports blockers: []. |
| `stamps_all_pages_together` | PASS | The locked candidate record defines the same four-page unified_stamp_set; final Git evidence shows the two stale API metadata lines updated in the integrated transaction while the release surfaces already held v1.1.0. |
| `verifies_release_metadata_read_only` | PASS | The candidate inventory reads docs/site/.meta/releases.json as a file-backed source and the final diff contains no modification to it. |
| `normalizes_mixed_version_forms` | PASS | The version inventory records prefixed and unprefixed raw forms, normalized identity 1.1.0, and equal comparison results, including package.json and release metadata. |
| `persists_candidate_producer_schema` | PASS | The locked audit-v1.1.0.md snapshot contains the required candidate schema, immutable commits, affected/stamp sets, per-page evidence, hashes, locator inventory, canonical digest, staged inventories, readback, commands, and candidate_conclusion: candidate_verified without post-commit success fields. |
| `anchors_candidate_then_discovers_success` | PASS | Git evidence and locked handoff content show distinct candidate/anchor and integrated handoff commits, anchor and candidate blob/tree identities, fast-forward integration, and final readback before phase_result: ready_for_tag. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c; fixture_sha256=085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897; output_sha256=0cbc9cbd0d9ffd60773b817ea493c2cab702848b15d64a73c65c6de36ce114b6; snapshot_sha256=b1f660485e3b92d2f8cd4611515dc4e0442e7f698c29f67abc4eb4fe5b0aebd8
- Behavior: Completed the pre-tag audit, stamped the required API metadata, persisted the candidate, anchored it, created the discovery handoff, fast-forward integrated it, and returned ready_for_tag.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c; fixture_sha256=085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897; output_sha256=ec76c4ad28b18ea9e6da3eb98f0f1580438ebe91a0220adefd79622edfeae3a0; snapshot_sha256=98a6ecfaf3cc547d75504aaabc0a073f4ed0020b37dce327b74cf0a7c8e8205d
- Behavior: Produced a conditional audit report identifying stale API verification metadata and stopped before stamping or release handoff.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
