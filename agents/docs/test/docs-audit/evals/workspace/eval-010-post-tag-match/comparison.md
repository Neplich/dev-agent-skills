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
- Fixture SHA-256: `43a1d01505e6c9e0f71431fdaeb75fea6b1939424f6c22775d15a970f4b73518`
- Prompt SHA-256: `47c14febb101f8d485b3785bf3ac63c5d627ee1f25999068d61918f6bfa13143`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5b5823d2c0804ce3dabb1d32490f71697f4ff111cd9371ebf92d1bb1b6ad2188`
- Skill overlay SHA-256: `c7033e85898ff61111eb14edc47b25e717119ee79349d7af461390afc706db78`
- Judge schema SHA-256: `f64d4542aa97d4b9bcd4bc655a5e70fec7d827a5ea9e9f63067fde8d7b819748`
- Eval definition SHA-256: `f4b575228474dd8bb2a93bb17a067f25252f9c293e1f78393d445c449385e8d2`
- Metadata SHA-256: `12f75879efa3cacf943ae19595239a747563947015e4033eed4ea7f4a51a5b47`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `selects_pre_tag_authority_safely` | PASS | With-skill trace resolves refs/release-evidence/v1.2.0 and reads its handoff/audit; the independent clone uses its own Git directory, default refspec, lacks the custom ref, and reads the tag-tree evidence. |
| `proves_released_tree_binding` | PASS | With-skill raw commands resolve the tag commit and tree, compare the pre-tag and tag trees, and inspect committed handoff, audit, and release paths in the clone without requiring identical commit identity. |
| `verifies_version_surfaces_from_release` | PASS | With-skill evidence reads all four release surfaces from the tag and distinguishes v1.2.0 from package.json’s 1.2.0; it does not use the mutable workspace as release proof. |
| `requires_durable_post_tag_evidence` | PASS | With-skill output identifies the absent post-tag record ref and missing maintainer decision, keeps both scenarios blocked, and does not treat matching content as post-tag success. |
| `preserves_upstream_release_artifacts` | PASS | With-skill output and git evidence show no ref, tag, worktree, index, or release-record changes and no regeneration, stamping, or tag operation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47c14febb101f8d485b3785bf3ac63c5d627ee1f25999068d61918f6bfa13143; fixture_sha256=43a1d01505e6c9e0f71431fdaeb75fea6b1939424f6c22775d15a970f4b73518; output_sha256=e3540d757833239a80df2bdcdbc99678be610839917a3c81b0cdb8923d8b2484; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Safely validates the tag and released tree in both the current repository and an isolated default-refspec clone, verifies release version surfaces, and correctly remains blocked for absent durable post-tag evidence.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47c14febb101f8d485b3785bf3ac63c5d627ee1f25999068d61918f6bfa13143; fixture_sha256=43a1d01505e6c9e0f71431fdaeb75fea6b1939424f6c22775d15a970f4b73518; output_sha256=f00a527284c9a574ba7ec26ea8032d5ef78b7fdeef090b97a1a67a5a3f6eb8f4; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Identifies the same tag and clone limitation and preserves repository state, but provides a much thinner comparison account without the with-skill lane’s detailed tree-binding and evidence analysis.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
