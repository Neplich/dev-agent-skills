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
- Identity schema: `2`
- target_skill_sha256: `a5e0bb043d61dbbb218e7d7efc08374e0d16a4d7aaa3b31817f2038830c90941`
- eval_definition_sha256: `4d1aa7f3a07c406f7e925f931c91ea28170bd7650629aa75bcd06b4f58bba0c7`
- metadata_sha256: `6adbc51a2dc07674edf9fca71addc72bccaccf75ae663c41fbf3725d8c48b107`
- fixture_sha256: `188f1d4d85d9c539fa3ce7acd636673ee316e8a8c7f692533cb806966484f84f`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `4cd14ef8cd033d31b5bb9ce50a786ad0b7d18c7ff4f682d88505eac53b634ecf`
- Source lock SHA-256: `c58f04d32c2ca3a22aec96f7ee027af648da5971453d2a5553d7ab2cd9272551`
- Prompt SHA-256: `c716eb0f2d2753ceb3a2258e2367701a57faeef420e346b4fa18dc3a1677c0e3`
- Repository HEAD: `60a4b3602dc07f3f6683a8873529bbdba6f8d27d`
- Repository worktree state: **CLEAN**
- Skill overlay SHA-256: `d7e2242fcdf83209e6c0cb5ec9544aa009e79488a72f81ebd4bf387289fbabec`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_confirmed_version_without_tag` | PASS | Candidate record and handoff record v1.2.0, base_ref v1.1.0, target_ref release-head, and actual-tag pending_expected_absent; final output is ready_for_tag. |
| `verifies_complete_set_and_surfaces` | PASS | Candidate record lists both change-map API pages and all four affected surfaces as verified, with release handoff, release notes, index, metadata, and package version inventory entries. |
| `normalizes_mixed_version_forms` | PASS | Inventory records v-prefixed release forms, unprefixed package.json version, normalized SemVer 1.2.0, and equal comparisons. |
| `records_pre_stamp_values` | PASS | Candidate pages record pre-stamp values v1.1.0, unverified, v1.1.0, and unverified; no baseline_verified_version field is present. |
| `stamps_complete_set_atomically` | PASS | Delivered blobs show all four pages stamped v1.2.0, with readback hashes; the workspace manifest preserves the metadata blob. |
| `builds_isolated_candidate_transaction` | PASS | Trace shows a temporary worktree and branch from release-head, while git evidence shows the host main HEAD, branch, index, and worktree remained unchanged during candidate construction. |
| `candidate_record_has_no_ready_result` | PASS | Candidate blob contains candidate_verified, complete page/version/convergence inventories, hashes, digests, selectors/extractors, and commands; it contains no ready_for_tag, success time, containing commit/tree identity, or post-commit confirmation. |
| `validates_two_complete_staged_gates` | NOT_EXERCISED | The trace shows staged-gate-related commands and the candidate inventories describe both pre- and post-candidate deltas, but locked evidence does not fully prove that every required raw metadata and full-patch check was executed identically at both gates. |
| `confirms_anchor_commit_before_discovery` | NOT_EXERCISED | Anchor and handoff blobs are delivered and the trace shows anchor/handoff commits, but locked raw evidence does not fully prove the complete target_ref-to-anchor raw metadata/content gate in the required order. |
| `persists_fixed_discovery_handoff` | PASS | The fixed handoff blob is directly delivered and reachable, with required schema, refs, ready_for_tag result, digest, anchor/candidate identities, confirmation, preimage, lineage, and current entry; trace shows only the handoff path staged and committed. |
| `returns_ready_only_after_integration` | NOT_EXERCISED | Git evidence shows release-head fast-forwarded from target_ref to the handoff commit and the integrated discovery/candidate blobs are readable, but exact captured fingerprint/CAS proof and downstream package delivery are not independently complete in the locked evidence. |
| `returns_ready_for_tag_not_published` | PASS | Final output and handoff state are pre-tag ready_for_tag, explicitly directing creation of the tag next and requiring a later post-tag audit; the tag is still absent. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c716eb0f2d2753ceb3a2258e2367701a57faeef420e346b4fa18dc3a1677c0e3; fixture_sha256=188f1d4d85d9c539fa3ce7acd636673ee316e8a8c7f692533cb806966484f84f; output_sha256=c3b163b8ec77a4de819ac619ff12a555d4950207da41ac08404605016be97217; snapshot_sha256=52afed544dd8b78abd3457312d3fdbc84faf5182ed870e4d214fc23a2748290c
- Behavior: Produces and integrates a pre-tag candidate with verified documentation surfaces, normalized version inventory, four-page stamps, candidate record, anchor, and fixed handoff; returns ready_for_tag while leaving tag publication pending.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c716eb0f2d2753ceb3a2258e2367701a57faeef420e346b4fa18dc3a1677c0e3; fixture_sha256=188f1d4d85d9c539fa3ce7acd636673ee316e8a8c7f692533cb806966484f84f; output_sha256=8f7fcc5230ccf51bcff4037c96c40022ffdf8aa9bf657a4c1cb6b757a5d6cff5; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline stops as blocked on a perceived release-metadata contradiction and does not produce a candidate, stamps, anchor, handoff, or ready result.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Complete or capture the full identical staged-gate and anchor-gate evidence, including raw metadata, type/mode/path, and full binary patch checks.
- Next: Capture immutable worktree/index fingerprints, CAS integration checks, and the external downstream handoff package if those are required for final coverage.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
