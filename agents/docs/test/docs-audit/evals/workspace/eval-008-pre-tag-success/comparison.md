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
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `c716eb0f2d2753ceb3a2258e2367701a57faeef420e346b4fa18dc3a1677c0e3`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `d7e2242fcdf83209e6c0cb5ec9544aa009e79488a72f81ebd4bf387289fbabec`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_confirmed_version_without_tag` | PASS | Candidate record and handoff record retain the confirmed version, base/target refs, and pending-absent actual tag; final output says the tag was not created. |
| `verifies_complete_set_and_surfaces` | PASS | Candidate record lists both change-map API pages, all four affected pages, per-page verified results, release-note handoff, metadata, and package version evidence. |
| `normalizes_mixed_version_forms` | PASS | Version inventory records required raw forms, selectors, extractors, normalized values, and equality across confirmation, package.json, notes, index, and metadata. |
| `records_pre_stamp_values` | PASS | Candidate record directly records the four pre-stamp values: v1.1.0, unverified, v1.1.0, and unverified, with no baseline_verified_version field. |
| `stamps_complete_set_atomically` | PASS | Delivery snapshots show all four authorized pages changed only from their prior values to v1.2.0, readback passed, and releases.json was not changed. |
| `builds_isolated_candidate_transaction` | NOT_EXERCISED | The trace shows the intended isolated worktree/branch flow and delivery evidence shows candidate commits, but the locked raw evidence does not fully prove index initialization and preservation throughout all candidate checks. |
| `candidate_record_has_no_ready_result` | FAIL | The candidate record has the required schema, page hashes, version inventory, digests, staged inventories, readback, and candidate_verified conclusion, but it also contains target/base commit and target_tree identity fields, which the assertion forbids. |
| `validates_two_complete_staged_gates` | PASS | Candidate record and commit evidence contain pre- and post-candidate inventories with raw modes/types/statuses, ordinary blobs, single-line stamp changes, fixed paths, and no unauthorized delta; final commit evidence also shows the expected handoff addition. |
| `confirms_anchor_commit_before_discovery` | PASS | The handoff records anchor commit/tree and post-commit confirmation; commit evidence shows the anchor was created before the handoff and final tree/blob readback was performed. |
| `persists_fixed_discovery_handoff` | FAIL | The delivered handoff includes schema, attempt, phase, version, refs, ready_for_tag, result time, inventory digest, anchor, candidate path/blob, confirmation, lineage, and digest, but omits the required handoff-path preimage and a current entry for the handoff blob without self-reference. |
| `returns_ready_only_after_integration` | PASS | Git evidence shows fast-forward integration from target_ref to the final commit, unchanged branch name, clean final status/index/worktree, and final output exposes the handoff for pm-agent:github-release-gen. |
| `returns_ready_for_tag_not_published` | FAIL | The output returns ready_for_tag and says the tag was not created or published, but it does not explicitly state that the status does not mean release verified. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c716eb0f2d2753ceb3a2258e2367701a57faeef420e346b4fa18dc3a1677c0e3; fixture_sha256=188f1d4d85d9c539fa3ce7acd636673ee316e8a8c7f692533cb806966484f84f; output_sha256=f716a4a427fc71b2f2c55dd4d612502c11c83a837348c88ed24c1191b63fdaa2; snapshot_sha256=0f2c33a1e171108fb586729ab7f78dd027e5dc7f1e711486289af339fc498127
- Behavior: Performed the pre-tag audit, stamped and integrated the four-page set, and exposed ready_for_tag, but delivered a nonconforming candidate record and incomplete handoff metadata.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c716eb0f2d2753ceb3a2258e2367701a57faeef420e346b4fa18dc3a1677c0e3; fixture_sha256=188f1d4d85d9c539fa3ce7acd636673ee316e8a8c7f692533cb806966484f84f; output_sha256=25d3ad05dbf10dd7264c8c644a2d8ed7b4c9c4c08a2ffe5212ec67846dff1698; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline incorrectly blocked pre-tag on metadata, evidence-patch, and scope concerns; it made no repository changes.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- candidate_record_has_no_ready_result
- persists_fixed_discovery_handoff
- returns_ready_for_tag_not_published
- Next: Remove forbidden commit/tree identity fields from the candidate record while retaining required page hashes.
- Next: Add the handoff path preimage and non-self-referential handoff current entry/digest.
- Next: Explicitly state that ready_for_tag permits tag creation only and does not mean publication or release verification.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
