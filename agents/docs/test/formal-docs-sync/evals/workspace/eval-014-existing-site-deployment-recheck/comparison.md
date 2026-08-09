# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-014-existing-site-deployment-recheck`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `c3d3b07fc792c4084ace3c9b32ba907e4fcd07d875befcf6af84add997421b79` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-014-existing-site-deployment-recheck`.
- Fixture SHA-256: `c3d3b07fc792c4084ace3c9b32ba907e4fcd07d875befcf6af84add997421b79`
- Prompt SHA-256: `1fa72144e806cf52f8fd8fbc5b8cac36763c1b6d96e197c5c1ebe4dd6e004c69`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a0fd1ad6b8713d6036307d1b20788b4771cc4b6ba53645fe17625e0dd55bbb5b`
- Skill overlay SHA-256: `73e88fe8c07f988c3353f81f9b058d4f8350c48ee381f924fe8c8201b9f92bb4`
- Judge schema SHA-256: `4b8356273a26d14ecc55ebfe7a9a2e541bdc3539a06437a0f30fb3a0dc7cbd4b`
- Eval definition SHA-256: `db9d705a02de2df76d9e1b62334995eac21d110dc172ed350d92306793043708`
- Metadata SHA-256: `57de9e366e385164240069213a2870da7cd8d43f7b6ee6621d6856f237ac7e4c`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reports_existing_site_integrated` | PASS | With_skill reports Atlas public/internal builds, Docker targets, Compose services, Helm values, CI matrix, and read-only evidence paths; it also states no deployment or build execution occurred. |
| `detects_partial_variant_coverage` | PASS | With_skill enumerates Orbit public versus internal: internal has a build script but lacks internal Docker target, Compose service, Helm values, and CI matrix, so it cannot be published or deployed and is not complete. |
| `returns_gap_to_pm_read_only` | NOT_EXERCISED | With_skill records that PM handoff evidence is missing and provides a blocked audit handoff while explicitly excluding deployment and documentation changes, but it does not ask the user to confirm PM-agent handoff generation; that later interactive step is not exercised. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1fa72144e806cf52f8fd8fbc5b8cac36763c1b6d96e197c5c1ebe4dd6e004c69; fixture_sha256=c3d3b07fc792c4084ace3c9b32ba907e4fcd07d875befcf6af84add997421b79; output_sha256=097ec79cedfc4ce5299d6c8772dcee00315169159bc5114cda303a191d24d09f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Accurately performs a read-only configuration review, confirms Atlas coverage, detects Orbit's partial internal coverage, and records the PM handoff gap without mutations.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1fa72144e806cf52f8fd8fbc5b8cac36763c1b6d96e197c5c1ebe4dd6e004c69; fixture_sha256=c3d3b07fc792c4084ace3c9b32ba907e4fcd07d875befcf6af84add997421b79; output_sha256=54650a16846996a76a1780ba76b7afa96458131ad3c1e9b323d658e2b307964a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a fresh comparison baseline that identifies Orbit's missing internal release path but is less systematic about the full deployment-chain gaps.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Ask whether pm-agent should generate the repo-wide deployment handoff when confirmation is available.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
