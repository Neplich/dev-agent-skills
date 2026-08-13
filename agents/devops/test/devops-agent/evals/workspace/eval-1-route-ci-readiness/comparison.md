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
- target_skill_sha256: `32901f32eb5b31c7ae31e0ec3b0112e3fe1d219e06d0edd2c1c57630d43202e0`
- eval_definition_sha256: `f7117f9350e70c8fb5cb6272bd6b59ffb1bebf3c95dfcda1ac024612c9eb455c`
- metadata_sha256: `7dd2e52b200852fa05d4eb58b51c5b9cc7af5f7c62ced61947f3e3d4b9b7a2c0`
- fixture_sha256: `01efe0f9d93680399a4e60a121c590987f01c7feeb295910c354e36c32f0a756`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `c7039dc2c9d829f51219a90df8027752cbbdaa32f7d8b6eb4b07c94a61b14320`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `0724714db74641157eee897f7a5f22bd3898815bc5861281390b10275748d63d`
- Repository HEAD: `2f950c46c67111058957774f796ccf97ae616d36`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `df8d1c81654b45ca866c7dc4460562101014a579db40445bcd3bbe134bd8f67e`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_primary_to_cicd` | PASS | The with_skill output names `cicd-bootstrap` as the first-stage route for GitHub Actions PR checks. |
| `keeps_deployment_context` | PASS | It targets existing `deploy/docker` assets and cites `deploy/docker/README.md`. |
| `names_followups` | PASS | It names `env-config-auditor` and `incident-playbook-writer` as follow-ups. |
| `does_not_run_all_skills` | PASS | It distinguishes the primary route from follow-ups and excludes `deployment-planner`. |
| `does_not_write_workflow` | PASS | It states no configuration was modified; locked git evidence confirms no changes. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0724714db74641157eee897f7a5f22bd3898815bc5861281390b10275748d63d; fixture_sha256=01efe0f9d93680399a4e60a121c590987f01c7feeb295910c354e36c32f0a756; output_sha256=05f6fa921dd896d23f4af872830f42e540afd90ca9e8d89e6297b409f0322607; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Selects the correct primary route, preserves deployment context, names follow-ups, scopes execution, and makes no workflow changes.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0724714db74641157eee897f7a5f22bd3898815bc5861281390b10275748d63d; fixture_sha256=01efe0f9d93680399a4e60a121c590987f01c7feeb295910c354e36c32f0a756; output_sha256=ede884ab6ed34a240c8f6cb184f04bdef40f9554275ab79a0cd1ac433ded31f7; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a read-only plan but does not select the required primary route or named follow-ups.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
