# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `devops-agent`
- Eval: `eval-002-route-docs-site-completeness-chain`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `db76812ee462c1a8d89decf8e6fae581930c1406d7c6f72f3847172ed0bb02f3` from `agents/devops/test/devops-agent/evals/workspace/eval-002-route-docs-site-completeness-chain`.
- Identity schema: `2`
- target_skill_sha256: `32901f32eb5b31c7ae31e0ec3b0112e3fe1d219e06d0edd2c1c57630d43202e0`
- eval_definition_sha256: `dc1b04424607a1675278b8e310c3f7b0da94f3cf1e857f037b9a6a8dbbf9482f`
- metadata_sha256: `2718def12280e05b73752266e8d3b39d6929d0781f7ca1aa2088b55bd4e38e9c`
- fixture_sha256: `db76812ee462c1a8d89decf8e6fae581930c1406d7c6f72f3847172ed0bb02f3`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `fdb2fd9254bbcae4d1c5e9dd4a0df1a9be1ee48991c72d5d1ea96147641ed710`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `520c4aa6ac767af388d73d9adeec0eb6b05a688f692c19decf65da48e498c67e`
- Repository HEAD: `2f950c46c67111058957774f796ccf97ae616d36`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `b95c78069c4a6a805dc918675b58a1f4ba98b532673108e30f6ce81c7e8d2976`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_repo_wide_docs_handoff` | PASS | With-skill output explicitly accepts request_type deployment, feature_path N/A, repo-wide documentation completeness scope, and proceeds without requesting feature-path clarification. |
| `routes_dependency_order` | PASS | With-skill output explicitly lists deployment-planner -> cicd-bootstrap -> env-config-auditor -> docs-agent:formal-docs-sync, including the conditional handoff to Docs after verified facts. |
| `preserves_role_and_authority_boundaries` | PASS | With-skill output states DevOps does not modify formal documentation and explicitly preserves no authorization for commit, push, image publication, or deployment. Locked git evidence shows no changes. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=520c4aa6ac767af388d73d9adeec0eb6b05a688f692c19decf65da48e498c67e; fixture_sha256=db76812ee462c1a8d89decf8e6fae581930c1406d7c6f72f3847172ed0bb02f3; output_sha256=1958fcbe1092b3973529b6da089aecf2d1a383770448b582491fa31015e049da; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly accepts and routes the repo-wide deployment handoff while preserving role and authority boundaries.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=520c4aa6ac767af388d73d9adeec0eb6b05a688f692c19decf65da48e498c67e; fixture_sha256=db76812ee462c1a8d89decf8e6fae581930c1406d7c6f72f3847172ed0bb02f3; output_sha256=69db6f72ceb836e7393a2c4d3217e333c8326da4228548b6816d1ef07fd1e398; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a useful generic staged deployment plan and preserves no-preauthorization, but does not provide the required named conditional specialist chain.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
