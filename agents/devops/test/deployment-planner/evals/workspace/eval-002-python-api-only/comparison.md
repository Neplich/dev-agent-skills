# Eval Result: eval-002-python-api-only

## Evaluation Target

- Agent: `devops`
- Skill: `deployment-planner`
- Eval: `eval-002-python-api-only`
- Test case: python-api-only
- Workspace: `workspace/eval-002-python-api-only`
- Latest result: PARTIAL - prior skill validation evidence is preserved; without-skill baseline was not generated for this historical comparison.
- Prior validation note: fresh Codex subagent validation completed on 2026-06-02

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Verifies that deployment-planner handles python-api-only and produces the expected role-specific artifact.
- Expected output: 生成简化的部署配置，不包含数据库相关内容

## Assertions

- `deploy_local_env_example_database_url`: deploy/local/.env.example 不包含 DATABASE_URL
- `deploy_docker_docker_compose_yml_app`: deploy/docker/docker-compose.yml 只有 app 服务
- `deploy_local_start_sh`: deploy/local/start.sh 不包含数据库初始化步骤

## With Skill

Observed behavior:

- 当前 skill 的 no database edge case 要求跳过数据库相关配置；FastAPI API-only 场景可生成简化部署配置，不包含 DATABASE_URL，不添加数据库服务，也不写数据库初始化步骤。

## Without Skill / Baseline
- BLOCKED: No actual without-skill baseline result is recorded for this historical comparison. This file is not treated as a full eval PASS until a baseline result is generated and written here.
- This comparison records whether the skill-specific protocol, routing, evidence, or artifact expectations are preserved.

## Failures

- None found in fresh Codex subagent validation.

## Next Steps

- 无需修改当前 skill 指令。

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be committed.
