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
- Repository HEAD: `f34c1007244dc48cf04fcd5d073fc5949225f1bd`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `7ed8638f6a80000c952068f188dbfe51d8ede83a52ee0b3635f473bf2d9da41d`
- Skill overlay SHA-256: `4183c2c4191ffb5278feb2ab2a6f8ac1fed136b346aab58bc7438d627c8d7660`
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
| `preserves_state_for_no_surface_change` | PASS | With-skill output correctly identifies the version-stamp patch as metadata-only and says no deployment-integrity recheck is needed; locked patch evidence confirms only last_verified_version changes. |
| `refreshes_shared_state_for_material_change` | NOT_EXERCISED | With-skill output correctly identifies the internal output-path/build-target change and requests a deployment-integrity recheck, but the locked fixture lacks the runtime/deployment evidence needed to perform and refresh the shared audit state. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cb27f98c195c0adaa2bc7ce90eded119c590e29ff34ec55cdd7a71187adb71ba; fixture_sha256=02024e6f0aaa0bcf6615062b3d8a31430a90f2e0a76edad7ce1044c04423eb52; output_sha256=2aee5c2a960fe70e98d5e326c9425071efee942d9157a25b7c834429ba0bb9e1; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly distinguishes metadata-only changes from material build-target changes, preserves the workspace, and appropriately blocks the formal recheck for missing evidence.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cb27f98c195c0adaa2bc7ce90eded119c590e29ff34ec55cdd7a71187adb71ba; fixture_sha256=02024e6f0aaa0bcf6615062b3d8a31430a90f2e0a76edad7ce1044c04423eb52; output_sha256=489ba85c6fc1d9a43e52ce31dc9378e3e94e33776fdc27964fc35459ab4e45d1; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline reaches the same core distinction and recheck recommendation, with less explicit audit-state gating.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide the missing deployment/build audit evidence and confirmation needed to execute the shared integrity check and refresh its state for the internal build-target change.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
