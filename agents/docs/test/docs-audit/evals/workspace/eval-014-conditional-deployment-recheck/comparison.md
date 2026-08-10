# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-014-conditional-deployment-recheck`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `02024e6f0aaa0bcf6615062b3d8a31430a90f2e0a76edad7ce1044c04423eb52` from `agents/docs/test/docs-audit/evals/workspace/eval-014-conditional-deployment-recheck`.
- Fixture SHA-256: `02024e6f0aaa0bcf6615062b3d8a31430a90f2e0a76edad7ce1044c04423eb52`
- Prompt SHA-256: `cb27f98c195c0adaa2bc7ce90eded119c590e29ff34ec55cdd7a71187adb71ba`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5b5823d2c0804ce3dabb1d32490f71697f4ff111cd9371ebf92d1bb1b6ad2188`
- Skill overlay SHA-256: `c7033e85898ff61111eb14edc47b25e717119ee79349d7af461390afc706db78`
- Judge schema SHA-256: `b484eac80dd3c83d19d6e2564672bb72616ee37e54370c5c00059bfaaa781dcf`
- Eval definition SHA-256: `3b49ebce5564e2973a0e2404ae2204baef9f3926736e7959e09be720ea423b90`
- Metadata SHA-256: `2b29c083a590a4eda139a3861e29b83daf406cc100d9a6f0e884225e104c8734`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_state_for_no_surface_change` | PASS | The with_skill output correctly classifies version-stamp.patch as not requiring a deployment-integrity recheck and reports no deployment-configuration mutation. The locked patch changes only last_verified_version. |
| `refreshes_shared_state_for_material_change` | NOT_EXERCISED | The with_skill output correctly identifies internal-build-target.patch as a material build-target/output change and says a shared deployment-integrity review should follow, but the locked evidence shows the audit is blocked pending confirmed target_release_version or handoff evidence; refresh cannot yet occur. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cb27f98c195c0adaa2bc7ce90eded119c590e29ff34ec55cdd7a71187adb71ba; fixture_sha256=02024e6f0aaa0bcf6615062b3d8a31430a90f2e0a76edad7ce1044c04423eb52; output_sha256=765f1ffad1cbd4a5bcb896bca296a8d3908afe67ec5dcf6060101ba6be54fc11; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly preserves the no-recheck decision for a version-only stamp and identifies the internal output-directory change as requiring shared deployment-integrity review; execution of that later review is blocked by missing audit credentials.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cb27f98c195c0adaa2bc7ce90eded119c590e29ff34ec55cdd7a71187adb71ba; fixture_sha256=02024e6f0aaa0bcf6615062b3d8a31430a90f2e0a76edad7ce1044c04423eb52; output_sha256=78457a93b69376b24579f796c61420e0c7ffe3fa1f6c1e84a2996a1b041a89cf; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline reaches the same two patch classifications without the formal audit-blocker explanation.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide confirmed target_release_version and valid audit handoff/base-target evidence, then perform the shared deployment-integrity review for internal-build-target.patch.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
