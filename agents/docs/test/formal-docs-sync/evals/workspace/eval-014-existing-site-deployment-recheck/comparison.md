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
- Fixture SHA-256: `af01acec7b20eeddc434bb03589d582f709819c1284ea057c0edd1ee4d701107`
- Prompt SHA-256: `1fa72144e806cf52f8fd8fbc5b8cac36763c1b6d96e197c5c1ebe4dd6e004c69`
- Repository HEAD: `f2aa9b2c49be68550ec45538c221425607f428ce`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `dd975083d3977d90b71b3396dff2498ef2b7e8d49c50fab50b5462a26f3248ee`
- Skill overlay SHA-256: `9667198915198da0404e03a7d4c962d38742b19c5de4de5f0cf1473f02db2bf1`
- Judge schema SHA-256: `4b8356273a26d14ecc55ebfe7a9a2e541bdc3539a06437a0f30fb3a0dc7cbd4b`
- Eval definition SHA-256: `db9d705a02de2df76d9e1b62334995eac21d110dc172ed350d92306793043708`
- Metadata SHA-256: `88632df23697500a0c7c41e94fb02d6159ef73b07b033169b66f45a2a56cdd01`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reports_existing_site_integrated` | PASS | With-skill output reports Atlas public/internal build, Docker, Compose, domain, authentication, and network evidence, and states the review was read-only with no deployment execution. |
| `detects_partial_variant_coverage` | PASS | With-skill output explicitly distinguishes Orbit public as actually published and Orbit internal as only having an unconnected build script, lacking CI, Docker target, Compose service, Helm host, authentication, and network isolation. |
| `returns_gap_to_pm_read_only` | FAIL | With-skill output documents read-only behavior and no deployment-asset changes, but does not ask whether pm-agent should generate a repo-wide deployment handoff. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1fa72144e806cf52f8fd8fbc5b8cac36763c1b6d96e197c5c1ebe4dd6e004c69; fixture_sha256=af01acec7b20eeddc434bb03589d582f709819c1284ea057c0edd1ee4d701107; output_sha256=114a9bba68f505b75d505d7fc1808ca3bf71ec273df2e7f28bb2ab29b71cb9e0; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Accurately audited existing variant coverage and preserved read-only behavior, but omitted the required PM handoff question.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1fa72144e806cf52f8fd8fbc5b8cac36763c1b6d96e197c5c1ebe4dd6e004c69; fixture_sha256=af01acec7b20eeddc434bb03589d582f709819c1284ea057c0edd1ee4d701107; output_sha256=af76c8ad6661ad8749cd0f4ecf61a53dc53b480be569679decab7f685c889d37; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provided a broadly accurate read-only comparison, including Atlas dual coverage and Orbit public-only coverage, but also omitted the PM handoff question.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill lane omitted the required user-visible question about pm-agent generating a repo-wide deployment handoff.
- Next: Ask whether pm-agent should generate the repo-wide deployment handoff.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
