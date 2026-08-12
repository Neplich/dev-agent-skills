# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `release-notes-gen`
- Eval: `eval-004-conditional-deployment-recheck`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1d05a5ef6eacf2734acacac9c7f138205eacee50a9bb44893b96aa9bb0d64d31` from `agents/docs/test/release-notes-gen/evals/workspace/eval-004-conditional-deployment-recheck`.
- Identity schema: `2`
- target_skill_sha256: `c8459f189e8d92d91e1c7ede8875090bfc1c2e1e04b8f18983b4339e6b65ba34`
- eval_definition_sha256: `34ab52326e403178b3c65c89903f9ce3ed937721059a083b8dcd35f212e12e18`
- metadata_sha256: `026d3644999635bf9397130063cb1f65e3467ff790b1fe892aa83df25be7904c`
- fixture_sha256: `1d05a5ef6eacf2734acacac9c7f138205eacee50a9bb44893b96aa9bb0d64d31`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `f6ca8293d29d78d2f2b85bd613e1f25b3aa93a647c64e21ca6731d5a228a1284`
- Identity migration: **MIGRATED_WITHOUT_MODEL_RERUN**
- Identity migration source commit: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Identity migration audit: `docs/engineer/repository-governance/eval-scenario-isolation/eval-identity-v2-migration-audit.json`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `skips_content_only_recheck` | PASS | with_skill correctly classified editorial.patch as content-only and reported no deployment recheck or invalidation. |
| `rechecks_material_release_surface` | NOT_EXERCISED | with_skill correctly identified the material build-output, navigation, and runtime-entry changes and stated that shared deployment completeness checking must be rerun, but the check could not occur without host/runtime evidence. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5b0a2bb08468867270b5e33622f2c669d7709f2935d65084fe81cdc7c550d3b1; fixture_sha256=1d05a5ef6eacf2734acacac9c7f138205eacee50a9bb44893b96aa9bb0d64d31; output_sha256=f3245a3643626c3ff337ec171f7bbe04d3e4d554a19e83582353e98445a3fd0c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Accurately separated content-only and material release-surface changes, preserved the no-mutation boundary, and stopped at the required confirmation/evidence gate.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5b0a2bb08468867270b5e33622f2c669d7709f2935d65084fe81cdc7c550d3b1; fixture_sha256=1d05a5ef6eacf2734acacac9c7f138205eacee50a9bb44893b96aa9bb0d64d31; output_sha256=58884930a10275412a73793de08c04616f3ac4886db564d941718c314002e965; snapshot_sha256=ffb0533395517b28971efa232d18554a737d589b11ac4f219f2a3262ec72db53
- Behavior: Fresh baseline wrote a review file and identified the path change, but did not demonstrate the shared recheck gate or blocked handoff behavior.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide the missing host/runtime evidence and confirmation inputs, then run the shared deployment completeness check for internal-entry.patch.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
