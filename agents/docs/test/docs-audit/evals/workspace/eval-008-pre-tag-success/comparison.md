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
- target_skill_sha256: `dafd53371901dfd724f88c70262b157e59494d29da1c613d0ef130564b6ff4f9`
- eval_definition_sha256: `4d1aa7f3a07c406f7e925f931c91ea28170bd7650629aa75bcd06b4f58bba0c7`
- metadata_sha256: `6adbc51a2dc07674edf9fca71addc72bccaccf75ae663c41fbf3725d8c48b107`
- fixture_sha256: `188f1d4d85d9c539fa3ce7acd636673ee316e8a8c7f692533cb806966484f84f`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `4cd14ef8cd033d31b5bb9ce50a786ad0b7d18c7ff4f682d88505eac53b634ecf`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `c716eb0f2d2753ceb3a2258e2367701a57faeef420e346b4fa18dc3a1677c0e3`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `7e61bd8eca6431729aee1f3be4656be0a4348119eb1218623bafd54cfaead2ab`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_confirmed_version_without_tag` | PASS | The with_skill output records base_ref v1.1.0, target_ref release-head, maintainer-confirmed v1.2.0, and explicitly says the v1.2.0 tag is absent and acceptable for pre-tag. |
| `verifies_complete_set_and_surfaces` | PASS | Locked trace reads the change map, both API pages, release handoff, Release Notes, index, release metadata, package version, and route facts; the output reports the complete affected set as verified. |
| `normalizes_mixed_version_forms` | PASS | The output states that package.json, Release Notes, index, and .meta/releases.json normalize to the same 1.2.0 identity, with the expected prefixed and unprefixed source forms. |
| `records_pre_stamp_values` | PASS | The output records the four pre-stamp values: catalog-items and index v1.1.0, catalog-status and Release Notes unverified, and states no baseline_verified_version was added. |
| `stamps_complete_set_atomically` | PASS | Locked file-change and staged-diff evidence shows all four authorized pages updated together; the output says the unified stamp was verified and .meta/releases.json was not modified. |
| `builds_isolated_candidate_transaction` | PASS | The trace creates a temporary branch/worktree from release-head, stages the four pages there, and cleanup evidence shows the host branch, index, and worktree restored. |
| `candidate_record_has_no_ready_result` | NOT_EXERCISED | A candidate record file-change event exists, but its locked content is not exposed, so the required complete schema and absence of forbidden fields cannot be proven. |
| `validates_two_complete_staged_gates` | FAIL | The first staged-gate evidence shows the candidate path as untracked rather than an A/M 100644 ordinary blob, and no complete second gate is shown; this contradicts the exercised gate requirement. |
| `confirms_anchor_commit_before_discovery` | NOT_EXERCISED | No anchor commit was created because Git rejected the commit for missing user.name/user.email; the required post-anchor checks were therefore not reached. |
| `persists_fixed_discovery_handoff` | NOT_EXERCISED | No discovery handoff was written because anchor creation failed; the output explicitly says no handoff remained after rollback. |
| `returns_ready_only_after_integration` | NOT_EXERCISED | No fast-forward integration or integrated handoff readback occurred because the anchor stage failed. |
| `returns_ready_for_tag_not_published` | NOT_EXERCISED | The with_skill lane returned blocked after the missing Git identity prevented the later required steps, so the successful ready_for_tag result was not reached. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c716eb0f2d2753ceb3a2258e2367701a57faeef420e346b4fa18dc3a1677c0e3; fixture_sha256=188f1d4d85d9c539fa3ce7acd636673ee316e8a8c7f692533cb806966484f84f; output_sha256=86f6eb667ca9f4ef62d6243f06870c18f6ffa055f0d1b34c87cc201f60e19c99; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Performed the bounded pre-tag audit, verified and staged the four-page stamp in an isolated worktree, then correctly blocked and rolled back when anchor commit creation lacked Git identity; candidate/gating evidence was incomplete.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c716eb0f2d2753ceb3a2258e2367701a57faeef420e346b4fa18dc3a1677c0e3; fixture_sha256=188f1d4d85d9c539fa3ce7acd636673ee316e8a8c7f692533cb806966484f84f; output_sha256=3f616c531a67a34291981518d58c27bd3dfc41b7990de549b524e94362aff901; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline only checked repository state, basic diff, version/tag facts, and reported blockers without executing the documentation-audit transaction.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The candidate record remained untracked during the staged-gate evidence, and the complete two-gate validation was not demonstrated.
- Next: Configure Git user.name and user.email, then rerun the complete pre-tag transaction and its candidate/staged-gate validation.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
