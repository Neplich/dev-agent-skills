# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-site-bootstrap`
- Eval: `eval-004-deployment-completeness-trigger`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842` from `agents/docs/test/docs-site-bootstrap/evals/workspace/eval-004-deployment-completeness-trigger`.
- Fixture SHA-256: `4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842`
- Prompt SHA-256: `a857fcf2c722711dbe976f85685cf13e950a1e35983a7408a6a97bb35347ed24`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f74a445a21eabfad3f25cc38a5190833cf5fc52294bb0054a41378fe894ddd82`
- Skill overlay SHA-256: `b193497852920517172f09f5d68ba6d13d4646f7f71948ca300566e66c51cb59`
- Judge schema SHA-256: `84cb88cc9e25dde2fbf0d2a0fb5349bfe630e32b333634cfdb918d30e60002a8`
- Eval definition SHA-256: `f0a0699462419947dfa64649c390cf74a3d370111b9c3ea826e84a8d4dc9f735`
- Metadata SHA-256: `abed400d8529a0bd91cc069fda9057f38aa9e64b1a632698bb6d1e29c26ae6e8`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `classifies_first_bootstrap_integrated` | NOT_EXERCISED | With-skill output explicitly keeps the task read-only, says bootstrap was not executed, and states it will not modify docs/site. It reports no push, image publication, or deployment actions; git evidence shows no changes. |
| `asks_first_bootstrap_choice` | NOT_EXERCISED | No bootstrap or first post-commit deployment decision was required or performed; the candidate correctly identified the request as a read-only connectivity review. |
| `rechecks_rebootstrap_drift` | NOT_EXERCISED | No bootstrap or re-bootstrap occurred, so post-rebootstrap configuration drift and the PM-to-DevOps follow-up choice were not exercised. |
| `preserves_authorization_boundary` | PASS | The with-skill output preserves the read-only boundary, explicitly avoids bootstrap and docs/site changes, and the locked git evidence shows unchanged branch, HEAD, index, worktree, and no new commits. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a857fcf2c722711dbe976f85685cf13e950a1e35983a7408a6a97bb35347ed24; fixture_sha256=4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842; output_sha256=4693f33beb0f1bd46dbf172fc1ffa0bb4191020205f26c816ae5bf02b5221f2a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly performed the requested read-only repository connectivity review, identified build/deployment gaps, and preserved authorization boundaries.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a857fcf2c722711dbe976f85685cf13e950a1e35983a7408a6a97bb35347ed24; fixture_sha256=4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842; output_sha256=1cacc8ce050d2035d3399b19d11435073db5a7f88cb0f993286a706462209b0a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provided a comparable read-only repository review and baseline connectivity conclusions, but did not exercise the bootstrap workflow either.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
