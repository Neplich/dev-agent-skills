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
- target_skill_sha256: `3da1a9a1466d6ecd43ed5c082adf803d01b5c2ca25dfee7a882fcc8113f7ce5c`
- eval_definition_sha256: `34ab52326e403178b3c65c89903f9ce3ed937721059a083b8dcd35f212e12e18`
- metadata_sha256: `026d3644999635bf9397130063cb1f65e3467ff790b1fe892aa83df25be7904c`
- fixture_sha256: `1d05a5ef6eacf2734acacac9c7f138205eacee50a9bb44893b96aa9bb0d64d31`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `f6ca8293d29d78d2f2b85bd613e1f25b3aa93a647c64e21ca6731d5a228a1284`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `5b0a2bb08468867270b5e33622f2c669d7709f2935d65084fe81cdc7c550d3b1`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `9d7abf20333b60efc8aeaad2d302ecd422e44bb547e52f5a4d9623347a2b048b`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `skips_content_only_recheck` | PASS | With_skill classifies editorial.patch as wording-only, explicitly says it does not change build targets, navigation, or deployment paths, and reports no host documentation check or deployment-surface write. |
| `rechecks_material_release_surface` | NOT_EXERCISED | With_skill correctly identifies internal-entry.patch as changing the internal build output, Docker COPY source, and navigation, and says deployment completeness must be revalidated; the required shared check could not proceed because version confirmation and the PM handoff were missing. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5b0a2bb08468867270b5e33622f2c669d7709f2935d65084fe81cdc7c550d3b1; fixture_sha256=1d05a5ef6eacf2734acacac9c7f138205eacee50a9bb44893b96aa9bb0d64d31; output_sha256=c11b5e19f01f54340415ccdc7dd1d73c3fb597bbbe049c722b70143a24c9eba2; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly distinguished content-only versus material release-surface changes, preserved deployment surfaces, and stopped at the required entry gate.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5b0a2bb08468867270b5e33622f2c669d7709f2935d65084fe81cdc7c550d3b1; fixture_sha256=1d05a5ef6eacf2734acacac9c7f138205eacee50a9bb44893b96aa9bb0d64d31; output_sha256=6cd0650018d4447bb6ee6817dbe54a9e7f6bd84c946d291bb1c2ae08e6b35213; snapshot_sha256=3ffe430e7edc0db5a60c5cfe755e9c3581fea9f0670a18abf6cb200961cc7e78
- Behavior: Created a closeout file and correctly classified the content-only patch, but incorrectly concluded that the material internal-entry change did not invalidate the deployment conclusion.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Obtain the missing version confirmation and PM handoff, then run the shared deployment-completeness check for internal-entry.patch.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
