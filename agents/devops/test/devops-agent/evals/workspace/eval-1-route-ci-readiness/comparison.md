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
- Identity schema: `2`
- target_skill_sha256: `e6fc9956005b4282420c83eedf1949e2502f3d3153bb3a8b79d34af6c3be8ac8`
- eval_definition_sha256: `f7117f9350e70c8fb5cb6272bd6b59ffb1bebf3c95dfcda1ac024612c9eb455c`
- metadata_sha256: `7dd2e52b200852fa05d4eb58b51c5b9cc7af5f7c62ced61947f3e3d4b9b7a2c0`
- fixture_sha256: `01efe0f9d93680399a4e60a121c590987f01c7feeb295910c354e36c32f0a756`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `c7039dc2c9d829f51219a90df8027752cbbdaa32f7d8b6eb4b07c94a61b14320`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `0724714db74641157eee897f7a5f22bd3898815bc5861281390b10275748d63d`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `e9c0bd160ee98dcfdd0de591211716a54c99c4c9faa059d278ee1adcee41cdbf`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_primary_to_cicd` | PASS | With-skill output explicitly selects `cicd-bootstrap` first and identifies GitHub Actions PR checks as the current goal. |
| `keeps_deployment_context` | PASS | With-skill output names `PM_HANDOFF.md` and `deploy/docker/README.md`, and states existing Docker deployment assets are the basis. |
| `names_followups` | PASS | With-skill output names `env-config-auditor` for environment configuration auditing and `incident-playbook-writer` for rollback/runbook work. |
| `does_not_run_all_skills` | PASS | With-skill output separates the primary route from follow-ups, excludes `deployment-planner`, and requests confirmation before proceeding to `cicd-bootstrap`. |
| `does_not_write_workflow` | PASS | Locked git evidence shows no changes, and the output explicitly states no workflow/configuration was modified. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0724714db74641157eee897f7a5f22bd3898815bc5861281390b10275748d63d; fixture_sha256=01efe0f9d93680399a4e60a121c590987f01c7feeb295910c354e36c32f0a756; output_sha256=3d76fb1fa7af950ef7816d7d4c08a1a3e08b32ef737385f112c7969369372810; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly routes the current request to `cicd-bootstrap`, preserves deployment context, names follow-up routes, and respects the no-modification boundary.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0724714db74641157eee897f7a5f22bd3898815bc5861281390b10275748d63d; fixture_sha256=01efe0f9d93680399a4e60a121c590987f01c7feeb295910c354e36c32f0a756; output_sha256=f986f16e55d6f1b54cf0fd90186b7c5524e58682f820053f3d190dd14b8c5fac; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a generic DevOps plan without selecting the required named primary route or follow-up routes.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
