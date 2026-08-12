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
- target_skill_sha256: `5b11b38c1c44c386fe19122dfb1ce5918b2bfbc4830ad32aa994d8a7e39f35e7`
- eval_definition_sha256: `f4b575228474dd8bb2a93bb17a067f25252f9c293e1f78393d445c449385e8d2`
- metadata_sha256: `12f75879efa3cacf943ae19595239a747563947015e4033eed4ea7f4a51a5b47`
- fixture_sha256: `43a1d01505e6c9e0f71431fdaeb75fea6b1939424f6c22775d15a970f4b73518`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `f64d4542aa97d4b9bcd4bc655a5e70fec7d827a5ea9e9f63067fde8d7b819748`
- Identity migration: **MIGRATED_WITHOUT_MODEL_RERUN**
- Identity migration source commit: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Identity migration audit: `docs/engineer/repository-governance/eval-scenario-isolation/eval-identity-v2-migration-audit.json`
- Repository HEAD: `fecf485e8e3dcaf191b2b221d9cccbddfdea0b72`
- Repository worktree state: **DIRTY**
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `selects_pre_tag_authority_safely` | PASS | With-skill evidence resolves refs/release-evidence/v1.2.0 and its commit/tree, reads the handoff and audit, and reports a default-refspec clone without the custom ref that reconstructs evidence from the tag tree. |
| `proves_released_tree_binding` | PASS | It resolves the tag commit and tree, compares the tag tree with the package/evidence tree, and compares committed paths/blob identities in the independent clone without relying on matching commit identity. |
| `verifies_version_surfaces_from_release` | PASS | It verifies the release-note page, index, releases.json, and package.json from Git release content, including normalization of v1.2.0 versus 1.2.0, and does not treat the workspace as success evidence. |
| `requires_durable_post_tag_evidence` | PASS | It identifies missing durable post-tag persistence, reports blocked/not_persisted for both scenarios, and does not upgrade content consistency to release_verified. |
| `preserves_upstream_release_artifacts` | PASS | Git evidence shows unchanged HEAD/branch, empty ref delta, no new commits, no diffs, and no reflog changes; the output reports no ref, tag, or release-record mutation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47c14febb101f8d485b3785bf3ac63c5d627ee1f25999068d61918f6bfa13143; fixture_sha256=43a1d01505e6c9e0f71431fdaeb75fea6b1939424f6c22775d15a970f4b73518; output_sha256=0b892a826700c2b7ef22a8b203af1ef0ef7464c1ec9e4a1607571ab7ab688444; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly performs independent current-repository and fresh-clone release verification, identifies evidence/schema gaps, and remains blocked without durable post-tag persistence.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47c14febb101f8d485b3785bf3ac63c5d627ee1f25999068d61918f6bfa13143; fixture_sha256=43a1d01505e6c9e0f71431fdaeb75fea6b1939424f6c22775d15a970f4b73518; output_sha256=8875d369c12390aac64268c9bafc83e5b003d9cd2f6394d1091656b091cab0cc; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a useful basic tag/content comparison and notes the clone lacks the custom ref, but does not establish the complete blocked post-tag audit requirements.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
