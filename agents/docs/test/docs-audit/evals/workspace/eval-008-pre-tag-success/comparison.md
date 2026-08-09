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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8588a4fc6bb55ff6a1ce485f659334cabf6f9624098f4db4f1066bdacc1fc3ec`
- Skill overlay SHA-256: `09c184e9256c59e7718f2b61600ec30436b550d1692a7c65f8b8e6c64fc491f3`
- Judge schema SHA-256: `4cd14ef8cd033d31b5bb9ce50a786ad0b7d18c7ff4f682d88505eac53b634ecf`
- Eval definition SHA-256: `4d1aa7f3a07c406f7e925f931c91ea28170bd7650629aa75bcd06b4f58bba0c7`
- Metadata SHA-256: `6adbc51a2dc07674edf9fca71addc72bccaccf75ae663c41fbf3725d8c48b107`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_confirmed_version_without_tag` | PASS | With-skill output records base_ref, target_ref, confirmed v1.2.0, and absent tag, while identifying a separate metadata contradiction as the blocker. |
| `verifies_complete_set_and_surfaces` | PASS | With-skill output includes both change-map API pages, reports all four affected pages verified, and surfaces the conflicting .meta/releases.json state. |
| `normalizes_mixed_version_forms` | NOT_EXERCISED | The output uses v1.2.0 for the confirmed target and page values but does not provide enough evidence of source-form normalization against package.json and metadata. |
| `records_pre_stamp_values` | PASS | All four pre-stamp values are explicitly recorded: v1.1.0, unverified, unverified, and v1.1.0. |
| `stamps_complete_set_atomically` | NOT_EXERCISED | The candidate correctly reports that unified stamping was not executed because the audit is blocked; later stamping cannot proceed without correcting the surfaced blocker. |
| `builds_isolated_candidate_transaction` | NOT_EXERCISED | No candidate was built, and the locked evidence cannot prove the hidden isolation and captured-state process. |
| `candidate_record_has_no_ready_result` | NOT_EXERCISED | No candidate record exists because the audit stopped before candidate construction. |
| `validates_two_complete_staged_gates` | NOT_EXERCISED | No staged gates were executed because the audit stopped at the precondition blocker. |
| `confirms_anchor_commit_before_discovery` | NOT_EXERCISED | No anchor commit or post-stamp validation was created because stamping did not occur. |
| `persists_fixed_discovery_handoff` | NOT_EXERCISED | No discovery handoff was written because no anchor commit was created. |
| `returns_ready_only_after_integration` | NOT_EXERCISED | Integration and downstream readiness were not reached after the metadata blocker was surfaced. |
| `returns_ready_for_tag_not_published` | NOT_EXERCISED | The correct pre-tag outcome is blocked by the contradictory released/latest metadata, so ready_for_tag was not reachable in this run. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c716eb0f2d2753ceb3a2258e2367701a57faeef420e346b4fa18dc3a1677c0e3; fixture_sha256=188f1d4d85d9c539fa3ce7acd636673ee316e8a8c7f692533cb806966484f84f; output_sha256=8a96fe1aba2b23602273d1cd6e861d642e6dc6530d66d939af60720d41305bca; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly audited the confirmed refs/version, verified the affected documentation surfaces, surfaced the release metadata contradiction, and preserved the workspace without performing downstream mutations.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c716eb0f2d2753ceb3a2258e2367701a57faeef420e346b4fa18dc3a1677c0e3; fixture_sha256=188f1d4d85d9c539fa3ce7acd636673ee316e8a8c7f692533cb806966484f84f; output_sha256=ba68143435d49013938be6175eba28c5597c751d3f112746836ea5d5888dcc7a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline also blocked on release metadata, but reported stale verification markers and an alleged diff-evidence mismatch instead of the with-skill complete-surface verification and bound blocker handling.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Correct the contradictory release metadata, then rerun the complete pre-tag workflow.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
