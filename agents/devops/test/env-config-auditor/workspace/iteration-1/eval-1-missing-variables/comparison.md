# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `env-config-auditor`
- Eval: `eval-001-missing-variables`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `4e6c22cd2abded0cbcf31007050064d16e8cb14c8ccdda445c9587853833ba57` from `agents/devops/test/env-config-auditor/workspace/iteration-1/eval-1-missing-variables`.
- Identity schema: `2`
- target_skill_sha256: `bd10ad28cda2e258647de2487fc41636124b4b1a48dc9f75b2dda06e6bfc2473`
- eval_definition_sha256: `5217a2bb49f0b8e0ba081e4029f81b07efd6b07af9fb34ce9773ecbde5d00a5b`
- metadata_sha256: `44155614dff76be09dfa5bcf55f66a5294433bd6eedc45d0d67dd22dcd2225eb`
- fixture_sha256: `4e6c22cd2abded0cbcf31007050064d16e8cb14c8ccdda445c9587853833ba57`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `7c0e897fa2e11e667f833a3bbf2e28e35b1c65790975d953ea93444f623ad66b`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `75e60dc10eb3fef811146cbd4dcc0df487be3bd537e40cef0747bad2cca106cf`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `204b02cf02ba29acba94a8f2b9d77989cc545ccad0b3e283133a98976ab6ca74`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_durable_config_audit` | FAIL | With-skill output explicitly declines the requested audit and no delivery_snapshot for deploy/ENV_AUDIT.md exists. |
| `compares_code_deploy_and_cicd` | FAIL | With-skill trace stops at the handoff gate and performs no comparison or report generation; the requested Docker/CI and Helm findings are absent. |
| `keeps_secrets_and_unknowns_honest` | FAIL | No secret value is written, but the with-skill lane produces no audit recording Helm as missing/unknown or the incomplete readiness state. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=75e60dc10eb3fef811146cbd4dcc0df487be3bd537e40cef0747bad2cca106cf; fixture_sha256=4e6c22cd2abded0cbcf31007050064d16e8cb14c8ccdda445c9587853833ba57; output_sha256=76ac090df03da6cbebe8f9fb22467860115b8d362820c72c9ad2647e148d79ee; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Stops at a PM/DevOps handoff gate; no audit is performed and no file is delivered.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=75e60dc10eb3fef811146cbd4dcc0df487be3bd537e40cef0747bad2cca106cf; fixture_sha256=4e6c22cd2abded0cbcf31007050064d16e8cb14c8ccdda445c9587853833ba57; output_sha256=5c78cb0dbb5cead6fe5ab40fa67c4201d08a2b1641fd52669170b0ec6f9df437; snapshot_sha256=5fe5f731911d70c22e391db003afde6847a52b8b4ed5800379587889209d7b2f
- Behavior: Creates a durable audit under docs/environment-config-audit.md with a variable matrix, evidence sources, risks, recommendations, and honest runtime limitations.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with-skill lane incorrectly blocks a directly requested repository-level audit on an unavailable handoff packet and delivers no requested artifact or findings.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
