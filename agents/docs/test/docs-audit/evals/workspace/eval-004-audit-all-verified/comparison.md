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
- target_skill_sha256: `a5e0bb043d61dbbb218e7d7efc08374e0d16a4d7aaa3b31817f2038830c90941`
- eval_definition_sha256: `9d29cd503dc3f38e1235bc8d674c667f9fc3bef38d94569b7888bb0dfed80506`
- metadata_sha256: `4c1ab6c77122f43adf1cbc9d6f05aea7b2b047fe1e69ba225e32d03f006dc954`
- fixture_sha256: `085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `a043187f1d82deb6ceb1f6f2a8dbb12db6dd01c71ced16d224de3ae50ca31c3b`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `d7e2242fcdf83209e6c0cb5ec9544aa009e79488a72f81ebd4bf387289fbabec`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `verifies_complete_affected_set` | PASS | Candidate record lists all four affected pages, marks each conclusion verified, and reports no blockers or unresolved gaps. |
| `stamps_all_pages_together` | PASS | Candidate record defines the four-page unified stamp set; locked page snapshots show all four at v1.1.0, with the two stale API markers changed and the already-correct release pages preserved. |
| `verifies_release_metadata_read_only` | PASS | Locked git evidence shows releases.json was read as version evidence and was absent from both candidate and handoff commit diffs; its ownership/read-only role is recorded in the version inventory. |
| `normalizes_mixed_version_forms` | PASS | Candidate inventory records v1-prefixed forms for release sources, an unprefixed package.json version, normalized SemVer values, and equality comparisons; the actual-tag source is explicitly pending as expected pre-tag. |
| `persists_candidate_producer_schema` | PASS | Locked audit file at the fixed path contains the candidate schema, attempt/phase, immutable refs, impact and stamp sets, per-page tree metadata and evidence, hashes, complete version-source locator contracts, canonical digest, two staged inventories, conclusion candidate_verified, and no ready_for_tag or post-commit fields. |
| `anchors_candidate_then_discovers_success` | PASS | Raw trace and git evidence show the candidate commit and second staged gate precede the anchor, the fixed handoff is then created in a separate commit, and that commit is fast-forward integrated with final path/blob/tree/status readback. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c; fixture_sha256=085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897; output_sha256=d23fbddb1b0fadb41ca83dc855b5b051c0144950d762937e77e2d02a35386885; snapshot_sha256=64d8660fef3b70f1ebc22efee42675ef36a292a9ef87f15774c6eca6551805c1
- Behavior: Completed the four-page audit, normalized version sources, updated stale API stamps, persisted a candidate record, created the post-stamp anchor and ready_for_tag handoff, and fast-forward integrated it.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c; fixture_sha256=085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897; output_sha256=135e1399a2da7c75c2345138d801772402f0e89de0a3497baafb70a7aaaf39a1; snapshot_sha256=2a72172fd0245765fd076f4502f6946b183f8471e75ef75bd4d7f5b6e71861dc
- Behavior: Created a separate ad hoc report but stopped because the two API pages remained at v1.0.0 and did not complete the required audit workflow.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
