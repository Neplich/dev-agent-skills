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
- Identity schema: `2`
- target_skill_sha256: `dafd53371901dfd724f88c70262b157e59494d29da1c613d0ef130564b6ff4f9`
- eval_definition_sha256: `3b49ebce5564e2973a0e2404ae2204baef9f3926736e7959e09be720ea423b90`
- metadata_sha256: `2b29c083a590a4eda139a3861e29b83daf406cc100d9a6f0e884225e104c8734`
- fixture_sha256: `02024e6f0aaa0bcf6615062b3d8a31430a90f2e0a76edad7ce1044c04423eb52`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `b484eac80dd3c83d19d6e2564672bb72616ee37e54370c5c00059bfaaa781dcf`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `cb27f98c195c0adaa2bc7ce90eded119c590e29ff34ec55cdd7a71187adb71ba`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `7e61bd8eca6431729aee1f3be4656be0a4348119eb1218623bafd54cfaead2ab`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_state_for_no_surface_change` | PASS | With-skill output correctly identifies version-stamp.patch as changing only last_verified_version and says deployment completeness remains unchanged. |
| `refreshes_shared_state_for_material_change` | NOT_EXERCISED | With-skill output correctly identifies the build-target changes and recommends rechecking deployment completeness, but the actual shared-state refresh cannot be exercised because the required audit handoff, target references, and confirmed target version are absent. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cb27f98c195c0adaa2bc7ce90eded119c590e29ff34ec55cdd7a71187adb71ba; fixture_sha256=02024e6f0aaa0bcf6615062b3d8a31430a90f2e0a76edad7ce1044c04423eb52; output_sha256=7305c790c6c7474cc5d1e87fa559da7bd8b27fb884cb77f9be7a0ec002214a29; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly distinguishes the non-material version stamp from the material internal build-output change, preserves the no-change state, and identifies the required recheck without modifying deployment configuration.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cb27f98c195c0adaa2bc7ce90eded119c590e29ff34ec55cdd7a71187adb71ba; fixture_sha256=02024e6f0aaa0bcf6615062b3d8a31430a90f2e0a76edad7ce1044c04423eb52; output_sha256=9c21d48aa29aaee51d6768b180af43b4d8549c3badd7a31cf15b30b2ba90f59c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline reaches the same patch-level conclusions and reports no deployment mutation, but lacks the structured audit-gate framing present in the with_skill lane.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide the audit handoff, refs, and confirmed target version, then run the shared documentation audit and refresh the deployment completeness state for the material build-target change.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
