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
- target_skill_sha256: `a8f87afda76c64d983a7b5f9d6a3f49bd751951e01d3714fb0439b6add7757ba`
- eval_definition_sha256: `5217a2bb49f0b8e0ba081e4029f81b07efd6b07af9fb34ce9773ecbde5d00a5b`
- metadata_sha256: `44155614dff76be09dfa5bcf55f66a5294433bd6eedc45d0d67dd22dcd2225eb`
- fixture_sha256: `4e6c22cd2abded0cbcf31007050064d16e8cb14c8ccdda445c9587853833ba57`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `7c0e897fa2e11e667f833a3bbf2e28e35b1c65790975d953ea93444f623ad66b`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `75e60dc10eb3fef811146cbd4dcc0df487be3bd537e40cef0747bad2cca106cf`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `79bb3dd33873d6df8baf21e6b0c5f2908c29f5d530191b5eb998f51613f0fe2f`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_durable_config_audit` | NOT_EXERCISED | with_skill stopped at the documented missing PM/DevOps handoff gate and did not create a report; the required artifact was therefore not exercised. |
| `compares_code_deploy_and_cicd` | NOT_EXERCISED | with_skill did not reach the audit comparison because the required handoff was missing. |
| `keeps_secrets_and_unknowns_honest` | NOT_EXERCISED | with_skill did not reach secret/Helm/unknown analysis because the required handoff was missing. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=75e60dc10eb3fef811146cbd4dcc0df487be3bd537e40cef0747bad2cca106cf; fixture_sha256=4e6c22cd2abded0cbcf31007050064d16e8cb14c8ccdda445c9587853833ba57; output_sha256=0512c65d8c49ee5aa9e1c16e2d2be28a97ff1749afdbde1898f368113c5307cc; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly stopped at the missing-handoff gate and requested PM classification; no audit delivery occurred.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=75e60dc10eb3fef811146cbd4dcc0df487be3bd537e40cef0747bad2cca106cf; fixture_sha256=4e6c22cd2abded0cbcf31007050064d16e8cb14c8ccdda445c9587853833ba57; output_sha256=9c9f81a2c29521bc3156a6bc59a2ed1189f2f24202209758956240edb49b7cf1; snapshot_sha256=671eb075a9e2124b720bb9234113da6d1a629fc58381e04f30c20fd1f00a0368
- Behavior: Produced a detailed audit with correct variable findings, but delivered it as ENV_CONFIG_AUDIT.md rather than the requested deploy/ENV_AUDIT.md.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide the required PM/DevOps handoff, then rerun the audit to exercise all assertions.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
