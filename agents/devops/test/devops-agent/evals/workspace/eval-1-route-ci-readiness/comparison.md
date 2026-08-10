# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `devops-agent`
- Eval: `eval-001-route-ci-readiness`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `01efe0f9d93680399a4e60a121c590987f01c7feeb295910c354e36c32f0a756` from `agents/devops/test/devops-agent/evals/workspace/eval-1-route-ci-readiness`.
- Fixture SHA-256: `01efe0f9d93680399a4e60a121c590987f01c7feeb295910c354e36c32f0a756`
- Prompt SHA-256: `0724714db74641157eee897f7a5f22bd3898815bc5861281390b10275748d63d`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `d688e19912770823b0aab741fb33c331e4eee7536315cf3080fbad81ca1e904f`
- Skill overlay SHA-256: `a9b9ac261ea1b814dd735003762f1150235fa2f98b001a6f7886461be4a86198`
- Judge schema SHA-256: `c7039dc2c9d829f51219a90df8027752cbbdaa32f7d8b6eb4b07c94a61b14320`
- Eval definition SHA-256: `bf26d801d111c094ffb06e4f6cd89e1f8a4b7c9a1e7fc76f302a33c493a411f4`
- Metadata SHA-256: `7dd2e52b200852fa05d4eb58b51c5b9cc7af5f7c62ced61947f3e3d4b9b7a2c0`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_primary_to_cicd` | PASS | With-skill output explicitly selects `cicd-bootstrap` as the current priority for GitHub Actions PR checks. |
| `keeps_deployment_context` | PASS | With-skill output preserves and cites `PM_HANDOFF.md` and `deploy/docker/README.md`, recognizing the existing Docker deployment context. |
| `names_followups` | PASS | With-skill output names `env-config-auditor` for environment-variable coverage and `incident-playbook-writer` for rollback documentation. |
| `does_not_run_all_skills` | PASS | With-skill output distinguishes the primary route from follow-up routes, excludes `deployment-planner`, and requests confirmation before implementation. |
| `does_not_write_workflow` | PASS | With-skill output states no file changes are authorized; locked git evidence shows unchanged HEAD, status, and diffs, with no delivery snapshot. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0724714db74641157eee897f7a5f22bd3898815bc5861281390b10275748d63d; fixture_sha256=01efe0f9d93680399a4e60a121c590987f01c7feeb295910c354e36c32f0a756; output_sha256=020d40ed2d68028d80c942566d921eb2c8adb83148871fa8f800ea9ef4f15020; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly routes the GitHub Actions PR-gate gap to `cicd-bootstrap`, preserves deployment context, names the two follow-ups, and stops before implementation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0724714db74641157eee897f7a5f22bd3898815bc5861281390b10275748d63d; fixture_sha256=01efe0f9d93680399a4e60a121c590987f01c7feeb295910c354e36c32f0a756; output_sha256=f03691e184f36eeaf033e3ff98dfcdd2b3e994311a07b7801b21c6db852230be; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a generic phased DevOps plan but does not select the required specialist route names.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
