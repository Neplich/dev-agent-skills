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
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f24bfeb12dba77a74fcf3f0161749ae4671b83762eac08484e7ae08621d9bacb`
- Skill overlay SHA-256: `5dbb8d8559bfab3926047aa028e19f362490751247c2142101cfd687fff5239e`
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
| `reports_existing_site_integrated` | PASS | With-skill output reports Atlas public/internal coverage, cites the relevant workflow, Dockerfile, Compose, Helm, and auth files, and states that no builds, tests, deployments, or writes were performed; the locked git evidence is unchanged. |
| `detects_partial_variant_coverage` | PASS | With-skill output enumerates Atlas as public plus internal and Orbit as public-only, explaining that Orbit's internal build script lacks a Docker target, Compose service, Helm host, and authentication configuration. This is a semantic partial-coverage conclusion. |
| `returns_gap_to_pm_read_only` | FAIL | With-skill output identifies pm-agent as the next owner for a repo-wide deployment handoff and confirms no deployment-asset changes or deployment execution, but it recommends this next step instead of asking whether pm-agent should generate it. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1fa72144e806cf52f8fd8fbc5b8cac36763c1b6d96e197c5c1ebe4dd6e004c69; fixture_sha256=af01acec7b20eeddc434bb03589d582f709819c1284ea057c0edd1ee4d701107; output_sha256=e463a84abd1bd656fae35b048db25635c876016b67baa733133adc17a709c4c0; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Accurate read-only comparison of Atlas and Orbit variant coverage with supporting configuration evidence; omits the required confirmation question to pm-agent.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1fa72144e806cf52f8fd8fbc5b8cac36763c1b6d96e197c5c1ebe4dd6e004c69; fixture_sha256=af01acec7b20eeddc434bb03589d582f709819c1284ea057c0edd1ee4d701107; output_sha256=bd9ccdad5bda629ae1f0e15d1f43c0749999e8a9431f48c3e2b262c0cd08db5d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline also identifies Atlas as dual-variant and Orbit as public-only, but provides a less complete handoff and does not address the PM confirmation request.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill lane does not ask the required confirmation about pm-agent generating the repo-wide deployment handoff.
- Next: Ask whether pm-agent should generate the repo-wide deployment handoff.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
