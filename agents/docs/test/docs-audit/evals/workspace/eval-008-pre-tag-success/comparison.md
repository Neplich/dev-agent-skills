# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-008-pre-tag-success`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `188f1d4d85d9c539fa3ce7acd636673ee316e8a8c7f692533cb806966484f84f` from `agents/docs/test/docs-audit/evals/workspace/eval-008-pre-tag-success`.
- Fixture SHA-256: `188f1d4d85d9c539fa3ce7acd636673ee316e8a8c7f692533cb806966484f84f`
- Prompt SHA-256: `c716eb0f2d2753ceb3a2258e2367701a57faeef420e346b4fa18dc3a1677c0e3`
- Repository HEAD: `fecf485e8e3dcaf191b2b221d9cccbddfdea0b72`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5b11b38c1c44c386fe19122dfb1ce5918b2bfbc4830ad32aa994d8a7e39f35e7`
- Skill overlay SHA-256: `85c4ae0a1d58505c4a23c34e6f9116aed81a09b4b6270e3ce148424084f6c7e0`
- Judge schema SHA-256: `4cd14ef8cd033d31b5bb9ce50a786ad0b7d18c7ff4f682d88505eac53b634ecf`
- Eval definition SHA-256: `4d1aa7f3a07c406f7e925f931c91ea28170bd7650629aa75bcd06b4f58bba0c7`
- Metadata SHA-256: `6adbc51a2dc07674edf9fca71addc72bccaccf75ae663c41fbf3725d8c48b107`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_confirmed_version_without_tag` | PASS | With-skill output and candidate record identify base_ref v1.1.0, target_ref release-head, confirmed v1.2.0, and absent tag without blocking pre-tag. |
| `verifies_complete_set_and_surfaces` | PASS | Candidate record lists both change-map API pages and all four formal surfaces as verified, with release handoff and host/version metadata checked. |
| `normalizes_mixed_version_forms` | PASS | Version inventory records required v-prefixed forms, package.json's 1.2.0 form, selectors/extractors, normalized 1.2.0 equality, and absent tag. |
| `records_pre_stamp_values` | PASS | Candidate record records pre-stamp values v1.1.0, unverified, v1.1.0, unverified and shows no baseline_verified_version field. |
| `stamps_complete_set_atomically` | PASS | Locked blobs show all four pages stamped to v1.2.0, with matching hashes and no release-metadata modification. |
| `builds_isolated_candidate_transaction` | PASS | Trace records creation of an isolated worktree/branch and candidate transaction; host state remained clean until integration. |
| `candidate_record_has_no_ready_result` | PASS | Candidate record is candidate_verified and contains schema, inventories, digests, hashes, staged inventories, and readback commands without ready_for_tag or post-commit fields. |
| `validates_two_complete_staged_gates` | PASS | Candidate record and trace document both staged gates, ordinary 100644 blobs, four one-line M changes, fixed candidate A path, and full patch/name-status checks. |
| `confirms_anchor_commit_before_discovery` | PASS | Trace records the post-stamp anchor commit and subsequent handoff creation; integrated evidence confirms the anchor/tree and candidate readbacks. |
| `persists_fixed_discovery_handoff` | PASS | Locked handoff blob contains the fixed path, ready_for_tag phase, refs, result time, inventory digest, anchor commit/tree, candidate path/blob, confirmation, preimage, lineage, and digest; integration readback supplies commit/tree/blob. |
| `returns_ready_only_after_integration` | PASS | Trace and git evidence show release-head fast-forward integration, integrated handoff commit/tree/blob readback, and clean host state before the ready result. |
| `returns_ready_for_tag_not_published` | PASS | Final output explicitly returns ready_for_tag and states it only means tag creation is allowed, not publication or release verification. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c716eb0f2d2753ceb3a2258e2367701a57faeef420e346b4fa18dc3a1677c0e3; fixture_sha256=188f1d4d85d9c539fa3ce7acd636673ee316e8a8c7f692533cb806966484f84f; output_sha256=88ecf7f28156a0b9d0695b287b362984a08dd54de09950f2c9811a74779c8e4a; snapshot_sha256=98ce9faac70fa34898e28537558402841fd5747d33e2f6c9ab26922e5654aec1
- Behavior: Completed the pre-tag audit, isolated candidate transaction, anchor/handoff commits, fast-forward integration, and returned ready_for_tag without claiming publication.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c716eb0f2d2753ceb3a2258e2367701a57faeef420e346b4fa18dc3a1677c0e3; fixture_sha256=188f1d4d85d9c539fa3ce7acd636673ee316e8a8c7f692533cb806966484f84f; output_sha256=07d0683bac034eaee16aa8ac6273ea11f3e5351f88991792135fc1a5e17a3330; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline performed a read-only audit but stopped blocked on metadata and evidence-patch discrepancies, producing no candidate or integration outputs.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
