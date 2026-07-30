# Eval Result: eval-001-nextjs-web-app

## Evaluation Target

- Agent: `devops`
- Skill: `deployment-planner`
- Eval: `eval-001-nextjs-web-app`
- Workspace: `workspace/eval-001-nextjs-web-app`
- Validation: 2026-07-31 fresh paired Codex subagent validation

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: confirmed repo-wide handoff, Next.js manifest, and health endpoint
- With-skill source: `tmp/eval-runs/issue-196-l2-1-20260731-0008/with_skill/eval-001-nextjs-web-app/`
- Fresh baseline source: `tmp/eval-runs/issue-196-l2-1-20260731-0008/without_skill_fresh2/eval-001-nextjs-web-app/`

## Latest Result

- Behavior result: PASS
- Coverage result: FULL
- All 8 with-skill assertions were exercised and passed.

Overall result: PASS

## Assertion Results

- PASS `deploy_local_readme_md`: `generated/deploy/local/README.md` exists.
- PASS `deploy_local_env_example_database_url_redis_url`: local `.env.example` contains both `DATABASE_URL` and `REDIS_URL`.
- PASS `deploy_local_start_sh`: `generated/deploy/local/start.sh` exists and has executable mode `-rwxr-xr-x`.
- PASS `deploy_docker_dockerfile`: `generated/deploy/docker/Dockerfile` exists.
- PASS `deploy_docker_docker_compose_yml_app_postgres_redis`: `docker-compose.yml` defines exactly the required `app`, `postgres`, and `redis` services.
- PASS `deploy_helm_chart_yaml`: `generated/deploy/helm/Chart.yaml` exists.
- PASS `deploy_helm_values_yaml_replicacount`: Helm values define `replicaCount`.
- PASS `deploy_helm_templates_deployment_yaml`: the Helm deployment template exists.

## With-Skill Behavior

- The output derived the explicit local, Docker, and Helm target matrix from the handoff and generated all required artifacts.
- It preserved the handoff boundary: Compose includes PostgreSQL and Redis, while Helm deploys only the application and injects external dependency addresses.

## Fresh Without-Skill Baseline

- The valid fresh baseline used the same prompt and pristine fixture without reading or applying the target skill or DevOps Agent README.
- It satisfied 6/8 exact artifact assertions. It omitted `deploy/local/start.sh` and named the Compose file `compose.yaml` instead of the asserted `docker-compose.yml`, although the alternate Compose file did contain the three required services.
- The earlier `tmp/eval-runs/issue-196-l2-1-20260731-0008/without_skill/` run is excluded because its isolation was invalid; none of its output informed this result.

## Failures

- No with-skill assertion failure or validation blocker.
- The valid baseline missed two exact artifact-contract assertions.

## Next Steps

- Keep this target-matrix and exact-artifact regression case.

## Runtime Artifact Policy

- Runtime candidates, generated files, transcripts, results, and diagnostics remain under ignored `tmp/eval-runs/` paths and are not copied into the durable fixture.
- Only this durable `comparison.md` is updated.
