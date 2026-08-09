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
- Fixture SHA-256: `4e6c22cd2abded0cbcf31007050064d16e8cb14c8ccdda445c9587853833ba57`
- Prompt SHA-256: `75e60dc10eb3fef811146cbd4dcc0df487be3bd537e40cef0747bad2cca106cf`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `11f5a69db2a4c2ab81d782a866d9a88090a8560b5e61462d8af4e66c4376601f`
- Skill overlay SHA-256: `ce7aff0f7795c878221dac5c9435b88a48e75e2799c5f15832edbd27f5f6796f`
- Judge schema SHA-256: `7c0e897fa2e11e667f833a3bbf2e28e35b1c65790975d953ea93444f623ad66b`
- Eval definition SHA-256: `5217a2bb49f0b8e0ba081e4029f81b07efd6b07af9fb34ce9773ecbde5d00a5b`
- Metadata SHA-256: `f2d1d6d11daf93046843d6cf276fdc2c30cd77fd3602aa38ebdb9fcc3d6c1a85`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_durable_config_audit` | PASS | Locked delivery snapshot contains deploy/ENV_AUDIT.md with missing-variable findings, coverage matrices, security issues, recommendations, and explicit source references. |
| `compares_code_deploy_and_cicd` | PASS | The report compares src/server.ts, local, Docker, CI/CD, and Helm/runtime status; it accurately identifies REDIS_URL and API_KEY as missing from Docker and CI/CD, and STRIPE_SECRET_KEY as present only in CI/CD among deployment configurations. |
| `keeps_secrets_and_unknowns_honest` | PASS | The report contains no real secret values, records absent Helm/Kubernetes/runtime evidence as unknown, and explicitly states deployment readiness is not verifiable. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=75e60dc10eb3fef811146cbd4dcc0df487be3bd537e40cef0747bad2cca106cf; fixture_sha256=4e6c22cd2abded0cbcf31007050064d16e8cb14c8ccdda445c9587853833ba57; output_sha256=6d5d612c4821fc98aeb2cc5bf2cab117d23839277f81527acdcd9aaa9604c170; snapshot_sha256=b2380611c5bdb80734738e53aa8b551f6d75390d33c1e1d7486ec1ceea4546cb
- Behavior: Delivered the requested durable audit with comprehensive environment coverage, evidence references, honest unknowns, and security caveats.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=75e60dc10eb3fef811146cbd4dcc0df487be3bd537e40cef0747bad2cca106cf; fixture_sha256=4e6c22cd2abded0cbcf31007050064d16e8cb14c8ccdda445c9587853833ba57; output_sha256=efc76c12a923da79260234bb1f15ca9e141d2f73105813f01329aea24331587d; snapshot_sha256=97f12e1805a69ca9084211039bd97a106a3ecd5bd3a0331483db08f53371e481
- Behavior: Delivered an audit outside the requested deploy/ENV_AUDIT.md path and omitted the required coverage/report details.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
