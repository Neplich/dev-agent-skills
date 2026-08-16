# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-010-post-tag-match`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `43a1d01505e6c9e0f71431fdaeb75fea6b1939424f6c22775d15a970f4b73518` from `agents/docs/test/docs-audit/evals/workspace/eval-010-post-tag-match`.
- Identity schema: `2`
- target_skill_sha256: `a5e0bb043d61dbbb218e7d7efc08374e0d16a4d7aaa3b31817f2038830c90941`
- eval_definition_sha256: `f4b575228474dd8bb2a93bb17a067f25252f9c293e1f78393d445c449385e8d2`
- metadata_sha256: `12f75879efa3cacf943ae19595239a747563947015e4033eed4ea7f4a51a5b47`
- fixture_sha256: `43a1d01505e6c9e0f71431fdaeb75fea6b1939424f6c22775d15a970f4b73518`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `f64d4542aa97d4b9bcd4bc655a5e70fec7d827a5ea9e9f63067fde8d7b819748`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `47c14febb101f8d485b3785bf3ac63c5d627ee1f25999068d61918f6bfa13143`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `d7e2242fcdf83209e6c0cb5ec9544aa009e79488a72f81ebd4bf387289fbabec`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `selects_pre_tag_authority_safely` | PASS | With-skill raw trace resolves refs/release-evidence/v1.2.0 and reads its handoff/audit; it creates a default-refspec clone, verifies the custom ref is absent there, and inspects the clone’s own Git data. |
| `proves_released_tree_binding` | PASS | Raw evidence resolves the tag commit/tree, compares the authority and tag trees, and independently reads handoff/audit and release paths from the clone’s tag tree. |
| `verifies_version_surfaces_from_release` | PASS | The candidate and raw tag/clone reads verify all four version surfaces, normalize v1.2.0 and 1.2.0 consistently, and use tag content rather than the worktree. |
| `requires_durable_post_tag_evidence` | PASS | The with-skill output identifies the absent proposed post-tag ref and missing maintainer decision, reports blocked_record_persistence as not_persisted, and keeps both scenarios blocked. |
| `preserves_upstream_release_artifacts` | PASS | Raw final Git status and refs show no upstream ref/tag changes; the only temporary clone was cleaned up, and the output explicitly preserves the existing authority. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47c14febb101f8d485b3785bf3ac63c5d627ee1f25999068d61918f6bfa13143; fixture_sha256=43a1d01505e6c9e0f71431fdaeb75fea6b1939424f6c22775d15a970f4b73518; output_sha256=cb27af6e263e16ed2e299875f3b1c73cf1fb79038a9d4a8755216298fded5c0e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly performs independent current-repository and fresh-clone checks, verifies tag/tree and version-surface binding, and preserves a blocked result when durable post-tag evidence is unavailable.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47c14febb101f8d485b3785bf3ac63c5d627ee1f25999068d61918f6bfa13143; fixture_sha256=43a1d01505e6c9e0f71431fdaeb75fea6b1939424f6c22775d15a970f4b73518; output_sha256=7e3fcbe9ca42ea4b4df2fa2f8ed9fb2194d7a29997abac27cbfa4e9e7f662e2a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline verifies the tag and release surfaces but treats the review as independently completable and does not identify or enforce the durable post-tag persistence blocker.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Restore write capability, obtain maintainer confirmation for the post-tag result ref, persist the blocked record, and verify it by readback without changing prior authority.
- Next: Rebuild or restore the missing audit foundation and required source/test evidence before rerunning verification.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
