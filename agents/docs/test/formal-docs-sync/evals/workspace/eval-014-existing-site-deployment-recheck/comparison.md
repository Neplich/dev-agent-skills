# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-014-existing-site-deployment-recheck`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `af01acec7b20eeddc434bb03589d582f709819c1284ea057c0edd1ee4d701107` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-014-existing-site-deployment-recheck`.
- Identity schema: `2`
- target_skill_sha256: `314b02febc2ef94201a8e1bf1080c874c355a0e47e6ac9a01b931425f08bfbd7`
- eval_definition_sha256: `db9d705a02de2df76d9e1b62334995eac21d110dc172ed350d92306793043708`
- metadata_sha256: `88632df23697500a0c7c41e94fb02d6159ef73b07b033169b66f45a2a56cdd01`
- fixture_sha256: `af01acec7b20eeddc434bb03589d582f709819c1284ea057c0edd1ee4d701107`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `4b8356273a26d14ecc55ebfe7a9a2e541bdc3539a06437a0f30fb3a0dc7cbd4b`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `1fa72144e806cf52f8fd8fbc5b8cac36763c1b6d96e197c5c1ebe4dd6e004c69`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `84e19c3e634cfde176d2ff20ba8e9d25a4838db3ed1deb5def94a8d0f1d2ddd9`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reports_existing_site_integrated` | PASS | With-skill output enumerates Atlas Public/Internal build and startup artifacts, cites configuration evidence, reports no deployment execution, and the locked git evidence shows no changes. |
| `detects_partial_variant_coverage` | PASS | With-skill output identifies Orbit Console as Public-only and lists missing Internal Docker, Compose, Helm, authentication, and CI coverage; this is a semantic partial-coverage determination. |
| `returns_gap_to_pm_read_only` | FAIL | With-skill output recommends that pm-agent generate the repo-wide deployment handoff and confirms no deployment-asset changes or deployment execution, but it does not actually ask whether to proceed. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1fa72144e806cf52f8fd8fbc5b8cac36763c1b6d96e197c5c1ebe4dd6e004c69; fixture_sha256=af01acec7b20eeddc434bb03589d582f709819c1284ea057c0edd1ee4d701107; output_sha256=f00f081f772fcfabebdfdd08266d9623029812ccfc07240064bf896b77180f78; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Read-only evidence review accurately distinguishes Atlas Public/Internal coverage from Orbit Public-only coverage and reports no mutations, but does not explicitly ask for confirmation before the pm-agent handoff.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1fa72144e806cf52f8fd8fbc5b8cac36763c1b6d96e197c5c1ebe4dd6e004c69; fixture_sha256=af01acec7b20eeddc434bb03589d582f709819c1284ea057c0edd1ee4d701107; output_sha256=a3701278307073b4e68f69c75487c17af55fe73ce454727e69ef82e8a1e6b2c9; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline also identifies Atlas as having Public/Internal configuration and Orbit as Public-only, with several deployment gaps, but provides less structured handoff handling.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with-skill lane recommends a pm-agent handoff but omits the required user-facing confirmation question.
- Next: Ask the user whether pm-agent should generate the repo-wide deployment handoff.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
