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
- target_skill_sha256: `e6fc9956005b4282420c83eedf1949e2502f3d3153bb3a8b79d34af6c3be8ac8`
- eval_definition_sha256: `dc1b04424607a1675278b8e310c3f7b0da94f3cf1e857f037b9a6a8dbbf9482f`
- metadata_sha256: `2718def12280e05b73752266e8d3b39d6929d0781f7ca1aa2088b55bd4e38e9c`
- fixture_sha256: `db76812ee462c1a8d89decf8e6fae581930c1406d7c6f72f3847172ed0bb02f3`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `fdb2fd9254bbcae4d1c5e9dd4a0df1a9be1ee48991c72d5d1ea96147641ed710`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `520c4aa6ac767af388d73d9adeec0eb6b05a688f692c19decf65da48e498c67e`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `1821e70be0fb2a5cfbaf9844feff79040bd9b8955e0caaf7c11bf00eae6cf1c2`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_repo_wide_docs_handoff` | PASS | With-skill output explicitly identifies a repo-wide deployment handoff, preserves request_type deployment and feature_path N/A, and treats missing completeness/Docker/Helm evidence as a reason to verify rather than request feature-path clarification. |
| `routes_dependency_order` | PASS | With-skill output states the complete conditional sequence deployment-planner -> cicd-bootstrap -> env-config-auditor -> formal-docs-sync, with each stage consuming the prior stage's verified results. |
| `preserves_role_and_authority_boundaries` | PASS | With-skill output states that DevOps does not modify formal documentation and that the handoff authorizes neither commit, push, image publication, deployment, tagging, nor release operations. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=520c4aa6ac767af388d73d9adeec0eb6b05a688f692c19decf65da48e498c67e; fixture_sha256=db76812ee462c1a8d89decf8e6fae581930c1406d7c6f72f3847172ed0bb02f3; output_sha256=1fe769727d7551caa287293feace0e3f70df309a508307f29a2054189adeffa2; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly accepts the repo-wide deployment handoff, routes the required conditional dependency chain, and preserves documentation ownership and authorization boundaries.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=520c4aa6ac767af388d73d9adeec0eb6b05a688f692c19decf65da48e498c67e; fixture_sha256=db76812ee462c1a8d89decf8e6fae581930c1406d7c6f72f3847172ed0bb02f3; output_sha256=e80d0fae90e2fbede53c3fdedb2153435e3fd7b579d28da924c65f3f9134493f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a reasonable generic deployment phase plan and preserves authorization boundaries, but does not name the required specialist dependency chain.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
