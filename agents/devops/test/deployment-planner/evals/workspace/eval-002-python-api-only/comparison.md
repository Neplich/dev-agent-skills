# Eval Result: eval-002-python-api-only

## Evaluation Target

- Agent: `devops`
- Skill: `deployment-planner`
- Eval: `eval-002-python-api-only`
- Workspace: `workspace/eval-002-python-api-only`
- Validation: 2026-07-31 fresh paired Codex subagent validation

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: confirmed API-only handoff, FastAPI manifest, health endpoint, and explicit no-database boundary
- With-skill source: `tmp/eval-runs/issue-196-l2-1-20260731-0008/with_skill/eval-002-python-api-only/`
- Fresh baseline source: `tmp/eval-runs/issue-196-l2-1-20260731-0008/without_skill_fresh2/eval-002-python-api-only/`

## Latest Result

- Behavior result: PASS
- Coverage result: FULL
- All 3 with-skill assertions were exercised and passed.

Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Assertion Results

- PASS `deploy_local_env_example_database_url`: generated local `.env.example` contains only `PORT` and no `DATABASE_URL`.
- PASS `deploy_docker_docker_compose_yml_app`: generated `docker-compose.yml` defines only the `app` service.
- PASS `deploy_local_start_sh`: generated executable `start.sh` contains no database, Redis, migration, or initialization step.

## With-Skill Behavior

- The output generated the confirmed local, Docker, and Helm targets while preserving the API-only boundary across all assets.
- It did not invent a persistence dependency, related environment variable, or initialization step.

## Fresh Without-Skill Baseline

- The valid fresh baseline used the same prompt and pristine fixture without reading or applying the target skill or DevOps Agent README.
- Its prose preserved the no-database semantic boundary, but it satisfied 0/3 exact artifact assertions: local `.env.example` and `start.sh` were absent, and the Compose artifact was named `compose.yaml` with service key `api`, not the asserted `docker-compose.yml` containing only `app`.
- The earlier `tmp/eval-runs/issue-196-l2-1-20260731-0008/without_skill/` run is excluded because its isolation was invalid; none of its output informed this result.

## Failures

- No with-skill assertion failure or validation blocker.
- The valid baseline preserved the broad no-database behavior but missed all three exact generated-artifact contracts.

## Next Steps

- Keep this negative-boundary regression case and its exact artifact checks.

## Runtime Artifact Policy

- Runtime candidates, generated files, transcripts, results, and diagnostics remain under ignored `tmp/eval-runs/` paths and are not copied into the durable fixture.
- Only this durable `comparison.md` is updated.
