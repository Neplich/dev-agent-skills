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
- Repository HEAD: `f34c1007244dc48cf04fcd5d073fc5949225f1bd`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `7ed8638f6a80000c952068f188dbfe51d8ede83a52ee0b3635f473bf2d9da41d`
- Skill overlay SHA-256: `4183c2c4191ffb5278feb2ab2a6f8ac1fed136b346aab58bc7438d627c8d7660`
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
| `verifies_complete_affected_set` | PASS | Candidate record lists both change-map required API docs, all four affected pages, and each page has final_status: verified with no blockers. |
| `stamps_all_pages_together` | PASS | Final integrated tree contains all four pages stamped v1.1.0; staged/committed evidence shows the API marker updates and confirms the complete unified set read back. |
| `verifies_release_metadata_read_only` | PASS | The release metadata is included in the version inventory and raw Git/result diffs show it was unchanged; fixture evidence identifies it as read-only. |
| `normalizes_mixed_version_forms` | PASS | Candidate inventory records v-prefixed forms for release surfaces, an unprefixed package.json version, normalized SemVer values, and equal comparisons. |
| `persists_candidate_producer_schema` | PASS | Locked candidate blob at the fixed path contains the required schema, immutable refs, impact/page evidence, hashes, inventories, canonicalization digest, staged gates, readback, and candidate_verified conclusion without forbidden success fields. |
| `anchors_candidate_then_discovers_success` | PASS | Raw trace and Git evidence show final staged gate, anchor commit, handoff-only commit, fast-forward integration, committed discovery record, and ready_for_tag returned only after readback. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c; fixture_sha256=085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897; output_sha256=e1ebe0f125b93ab3314c960a1c94877cf323a0bd558b91c38b5cceb79b31821d; snapshot_sha256=718adb200d44f5716a054dc6c58fed27287727aab856d64e3016c03df999b7a3
- Behavior: Completed the pre-tag audit, persisted the candidate and discovery handoff records, stamped the unified page set, and integrated via fast-forward to ready_for_tag.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c; fixture_sha256=085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897; output_sha256=2d78de53caf001e61bf954c3ee102fa491869cfd3c97757a4d186cf5a089263d; snapshot_sha256=a18a2d05eb2e7e4c34eab605d8492deeeef361f4185a1d8a40e975fc286046a7
- Behavior: Produced only a prose report, left documentation markers unchanged, and reported a publication blocker without the required audit artifacts or workflow.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
