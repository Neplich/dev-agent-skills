# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `deployment-planner`
- Eval: `eval-002-python-api-only`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `259dab4dbfe64941c0c3fdd5c97b56c6b90abb97168eeb7461bd9a7bf8e30888` from `agents/devops/test/deployment-planner/evals/workspace/eval-002-python-api-only`.
- Identity schema: `2`
- target_skill_sha256: `dfa906d01a96634826afcebe44c9732902f0bc2b120c6c7b7232879b93b8e923`
- eval_definition_sha256: `f6bee599168504aabc5841db04bc20810e822fd2af8545bc98e19f6298c38285`
- metadata_sha256: `d8b9107459aa74bd3dbadef75ae9d69cc322f1ce75809c991658f0479eee3361`
- fixture_sha256: `259dab4dbfe64941c0c3fdd5c97b56c6b90abb97168eeb7461bd9a7bf8e30888`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6d6cb805f86354c5ca7fe62a901b9a052b0e2f5bc53f163da17451ac99ca29a5`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `000bcbda1f774e89fec492193e606a35b1ac2f41c0b29e0c9ac66b491aa38c8b`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `a8511777e6b4f31217e6a6c17f2c1dc2d5abd375ef6253072404dae037d7bae7`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_confirmed_target_matrix` | PASS | Locked with_skill snapshot contains deploy/local, deploy/docker, and deploy/helm assets, with the matrix explicitly limited to local, Docker/Compose, and Kubernetes/Helm. |
| `keeps_api_only_topology` | PASS | The Compose snapshot defines only one api service. Locked Helm/local files contain no database, Redis, migration, DATABASE_URL, or additional runtime service; ConfigMap/HPA/Ingress are deployment resources, not extra services. |
| `uses_confirmed_runtime_contract` | PASS | Locked files use uvicorn app.main:app, default port 8000, and /health for Docker healthcheck, local startup documentation, and Helm probes/runtime documentation. |
| `stays_within_deployment_scope` | PASS | The locked delivery snapshot contains deployment assets only. The output and raw trace explicitly state that CI/CD configuration, publishing, and actual deployment were not performed. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=000bcbda1f774e89fec492193e606a35b1ac2f41c0b29e0c9ac66b491aa38c8b; fixture_sha256=259dab4dbfe64941c0c3fdd5c97b56c6b90abb97168eeb7461bd9a7bf8e30888; output_sha256=6bf27410e61b06ba26c77c422eaa521020af51aa0f5cfe81b6bc0263e8727adf; snapshot_sha256=7e162a439c6bab7d1d6a8f5c06b71cb52916262952d77b13d0b219bacb341475
- Behavior: Produced local, Docker/Compose, and Helm deployment assets for the API-only service, with explicit runtime and scope documentation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=000bcbda1f774e89fec492193e606a35b1ac2f41c0b29e0c9ac66b491aa38c8b; fixture_sha256=259dab4dbfe64941c0c3fdd5c97b56c6b90abb97168eeb7461bd9a7bf8e30888; output_sha256=e888cb5dcc2dd4e2d6f3bff573facafc17b32c50997e423ceb9a47e01f84ce5d; snapshot_sha256=64c00c18f49b4e3b0241ff14ec071df6822eb1263df8db37898c8d5c666ddec4
- Behavior: Produced Docker/Compose and Helm assets with an API-only topology and matching runtime settings, but without the structured deploy/local handoff layout.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
