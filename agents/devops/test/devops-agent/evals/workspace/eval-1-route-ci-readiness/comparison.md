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
- target_skill_sha256: `a1710c0451d41ab9797a4d66831dae37e5e82aa02c99f954ebc420b99e5a6387`
- eval_definition_sha256: `f7117f9350e70c8fb5cb6272bd6b59ffb1bebf3c95dfcda1ac024612c9eb455c`
- metadata_sha256: `7dd2e52b200852fa05d4eb58b51c5b9cc7af5f7c62ced61947f3e3d4b9b7a2c0`
- fixture_sha256: `01efe0f9d93680399a4e60a121c590987f01c7feeb295910c354e36c32f0a756`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `c7039dc2c9d829f51219a90df8027752cbbdaa32f7d8b6eb4b07c94a61b14320`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `0724714db74641157eee897f7a5f22bd3898815bc5861281390b10275748d63d`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `c5943c0d67e9e26ad4dd0e60253b5aa5e23f43099b3302627e66a7b3dc2bec2e`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_primary_to_cicd` | PASS | With-skill output explicitly selects `cicd-bootstrap` as the current first step for the GitHub Actions PR gate. |
| `keeps_deployment_context` | PASS | With-skill output cites `PM_HANDOFF.md` and `deploy/docker/README.md`, and states the plan is based on the existing `deploy/docker` image contract. |
| `names_followups` | PASS | With-skill output explicitly names `env-config-auditor` for environment-variable coverage and `incident-playbook-writer` for rollback and incident documentation. |
| `does_not_run_all_skills` | PASS | The output distinguishes the primary route from two follow-ups, while raw trace evidence shows routing/read-only inspection rather than execution of all specialist skills. |
| `does_not_write_workflow` | PASS | The output states no configuration was modified; locked git evidence shows unchanged HEAD, empty diffs, no untracked files, and an empty delivery snapshot. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0724714db74641157eee897f7a5f22bd3898815bc5861281390b10275748d63d; fixture_sha256=01efe0f9d93680399a4e60a121c590987f01c7feeb295910c354e36c32f0a756; output_sha256=36456dfc25c6db6b08dc9f1eeb8aaa5a80b7de495f030da7ecc643abb4fb4f38; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly routes the current work to `cicd-bootstrap`, preserves deployment context, names the two follow-ups, separates routing from execution, and respects the no-mutation boundary.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0724714db74641157eee897f7a5f22bd3898815bc5861281390b10275748d63d; fixture_sha256=01efe0f9d93680399a4e60a121c590987f01c7feeb295910c354e36c32f0a756; output_sha256=ca2a45fc2fc9ae4382261737ec205dc19026b3c32f698c4c06208a6da469c008; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a fresh baseline that identifies the PR gate as current work and the environment and rollback items as follow-ups, but does not use the explicit specialist route names.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
