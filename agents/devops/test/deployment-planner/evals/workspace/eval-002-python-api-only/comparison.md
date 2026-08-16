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
- target_skill_sha256: `ff61dcd9673d160376da3723849f195022899b8e8a38fe78c67e4488f9065a5f`
- eval_definition_sha256: `f6bee599168504aabc5841db04bc20810e822fd2af8545bc98e19f6298c38285`
- metadata_sha256: `d8b9107459aa74bd3dbadef75ae9d69cc322f1ce75809c991658f0479eee3361`
- fixture_sha256: `259dab4dbfe64941c0c3fdd5c97b56c6b90abb97168eeb7461bd9a7bf8e30888`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6d6cb805f86354c5ca7fe62a901b9a052b0e2f5bc53f163da17451ac99ca29a5`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `000bcbda1f774e89fec492193e606a35b1ac2f41c0b29e0c9ac66b491aa38c8b`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `aed4a3cdd1170f44446df97f66f60c0f6ae2151f3522fe982eb11ee05d551389`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_confirmed_target_matrix` | PASS | with_skill 的 delivery_snapshot 提供 deploy/local、deploy/docker 和 deploy/helm 三类资产，未生成其他部署目标。 |
| `keeps_api_only_topology` | PASS | Docker Compose 仅定义 api 服务；快照中的 Helm 和 local 配置未包含数据库、Redis、migration 或 DATABASE_URL。 |
| `uses_confirmed_runtime_contract` | PASS | local/start.sh、Dockerfile 和 Helm Deployment 均使用 app.main:app、默认 8000 端口；Docker healthcheck、Helm probes 及文档均使用 /health。 |
| `stays_within_deployment_scope` | PASS | 锁定交付文件中没有 CI/CD 配置；git_evidence 显示仅新增 deploy/ 文件，未发生提交、发布或环境部署。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=000bcbda1f774e89fec492193e606a35b1ac2f41c0b29e0c9ac66b491aa38c8b; fixture_sha256=259dab4dbfe64941c0c3fdd5c97b56c6b90abb97168eeb7461bd9a7bf8e30888; output_sha256=19a82fa787dbb190b041e7523eb8cbfdfbf20591ffceedbcacc90480d4e603e5; snapshot_sha256=fe04c5229f0244a8b9588adefdf0049a8db5adcd03355e3ac02a7fe737472ad7
- Behavior: 交付了 local、Docker、Helm 部署资产，并明确 CI/CD 与实际发布为范围外事项。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=000bcbda1f774e89fec492193e606a35b1ac2f41c0b29e0c9ac66b491aa38c8b; fixture_sha256=259dab4dbfe64941c0c3fdd5c97b56c6b90abb97168eeb7461bd9a7bf8e30888; output_sha256=cf84978a90f48534a5587be72207ae541cbeb8ee04eb53816c358df9f75d21a5; snapshot_sha256=8a2ff0a9ea150ebb9b2b228e5d76b8ea7ee7dbe8920135ce9e3bfee11f68d15e
- Behavior: 同样交付了 Docker、Compose 和 Helm 资产，覆盖范围符合 API-only 部署要求。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
