# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-012-staged-metadata-rollback`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1013313f9177f2e4b64118a15325ba0a4da0ec26b6c32604368f1f754b57e620` from `agents/docs/test/docs-audit/evals/workspace/eval-012-staged-metadata-rollback`.
- Fixture SHA-256: `1013313f9177f2e4b64118a15325ba0a4da0ec26b6c32604368f1f754b57e620`
- Prompt SHA-256: `4c059264a7527dcf6082f43bc5cacdf327f947505e6d5f9721fd10e71b64fdcb`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5b5823d2c0804ce3dabb1d32490f71697f4ff111cd9371ebf92d1bb1b6ad2188`
- Skill overlay SHA-256: `c7033e85898ff61111eb14edc47b25e717119ee79349d7af461390afc706db78`
- Judge schema SHA-256: `73f9308006ffa877e1ed5f74c8eef2e3a2b3222e98dd5485cfd0ba5e210de92a`
- Eval definition SHA-256: `885108a0e0e9ce48751816455b91da0ec400a08bb7d3a722984a36e4221d1938`
- Metadata SHA-256: `86b2ab0ad4bcb3fb98728ca8ff1375ff58d1094876353cbeafc325bf7593eb63`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_non_content_candidate_drift` | PASS | PASS: The output identifies mode changes, file-type changes, deletion, and symlink targets including the out-of-tree target, using staged.raw/summary and object contents. |
| `rejects_every_unauthorized_transformation` | FAIL | FAIL: It blocks the candidate and names the major unauthorized transformations, but does not explicitly cover the release-notes index-to-archive rename as its own transformation. |
| `rechecks_committed_candidate_boundaries` | FAIL | FAIL: It discusses the staged capture and the need to regenerate evidence, but does not state that a later committed candidate and handoff must be rechecked against the same authorization boundary. |
| `rolls_back_only_the_failed_attempt` | FAIL | FAIL: It notes that unrelated host changes remain and that captured state must not be copied into the current worktree, but does not specify isolating/removing only the failed attempt and its draft while restoring the affected authorized host state. |
| `proves_host_state_restoration` | PASS | PASS: It blocks continuation because cleanup cannot be proven, identifies the unchanged ref context and residual index/worktree paths, and requires renewed cleanup and verification rather than claiming success. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4c059264a7527dcf6082f43bc5cacdf327f947505e6d5f9721fd10e71b64fdcb; fixture_sha256=1013313f9177f2e4b64118a15325ba0a4da0ec26b6c32604368f1f754b57e620; output_sha256=94ce86389bb3f1a95c45381b055560d2669e83cbd0949edc8de4d59bc851e0f1; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly blocks the release and detects candidate drift, evidence-integrity failure, and residual host changes, but omits required boundary-recheck and precise rollback conclusions.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4c059264a7527dcf6082f43bc5cacdf327f947505e6d5f9721fd10e71b64fdcb; fixture_sha256=1013313f9177f2e4b64118a15325ba0a4da0ec26b6c32604368f1f754b57e620; output_sha256=89c3782c8e40cf552e401ef0466d8dc975b9dc5a34ddf17bd5b9cc60b03392e7; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline also blocks the release and identifies several drift and cleanup issues, but is comparison context only.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill output omits the committed-candidate/handoff recheck requirement.
- The with_skill output does not fully enumerate the unauthorized transformation classes or prescribe narrowly scoped rollback.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
