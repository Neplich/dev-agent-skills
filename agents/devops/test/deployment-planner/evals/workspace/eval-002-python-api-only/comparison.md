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
- Fixture SHA-256: `259dab4dbfe64941c0c3fdd5c97b56c6b90abb97168eeb7461bd9a7bf8e30888`
- Prompt SHA-256: `000bcbda1f774e89fec492193e606a35b1ac2f41c0b29e0c9ac66b491aa38c8b`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `6b7ee50b1667fd76ae49358cc3af5366a7e75afc33e7c444bb73e4e03310853a`
- Skill overlay SHA-256: `c38a517fc6ad0bdb4f779914676cb1e931bf2429f37f629f86b432a5c6adbb84`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `f6bee599168504aabc5841db04bc20810e822fd2af8545bc98e19f6298c38285`
- Metadata SHA-256: `cd34fc596ce17b79112511df2244a7b68d45546111925715157c8598360bb097`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_confirmed_target_matrix` | PASS | with_skill delivery_snapshot contains only deploy/local, deploy/docker, and deploy/helm assets; no fourth deployment target is present. |
| `keeps_api_only_topology` | PASS | with_skill Compose defines a single api service, and the Docker/Helm documentation explicitly states there are no database, cache, migration, Secret, or other service dependencies. No DATABASE_URL appears. |
| `uses_confirmed_runtime_contract` | PASS | Local start.sh invokes uvicorn app.main:app with default port 8000; Dockerfile CMD uses the same app and port; Helm exposes container/service port 8000 and both probes request /health. The fixture confirms /health exists. |
| `stays_within_deployment_scope` | PASS | with_skill outputs contain deployment assets only; no CI/CD configuration is present, and git evidence shows only untracked deploy/ files with no commits or deployment/publishing actions. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=000bcbda1f774e89fec492193e606a35b1ac2f41c0b29e0c9ac66b491aa38c8b; fixture_sha256=259dab4dbfe64941c0c3fdd5c97b56c6b90abb97168eeb7461bd9a7bf8e30888; output_sha256=c867ffbf480a0430840a0ef3950bd2fa8f061372f538723ee6c5c687d61fa650; snapshot_sha256=8fb75f359de61e3a6776a574fbfef7e683310fea72f651eac777e92e8c0dba75
- Behavior: Produced local, Docker, and Helm deployment assets while preserving the API-only topology and stated scope.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=000bcbda1f774e89fec492193e606a35b1ac2f41c0b29e0c9ac66b491aa38c8b; fixture_sha256=259dab4dbfe64941c0c3fdd5c97b56c6b90abb97168eeb7461bd9a7bf8e30888; output_sha256=bcf741a3d0fee3ec49476e705acc9bb3b2d2d7ef903f9a3cebfcb25fb922f216; snapshot_sha256=8dd1716a41ebccc86fd45f2b8c35fedba389b7b01439dc3a89b700c456c85c8f
- Behavior: Produced Docker and Helm assets, but omitted the confirmed local target.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Fixture SHA-256: `259dab4dbfe64941c0c3fdd5c97b56c6b90abb97168eeb7461bd9a7bf8e30888`
- Prompt SHA-256: `000bcbda1f774e89fec492193e606a35b1ac2f41c0b29e0c9ac66b491aa38c8b`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `6b7ee50b1667fd76ae49358cc3af5366a7e75afc33e7c444bb73e4e03310853a`
- Skill overlay SHA-256: `c38a517fc6ad0bdb4f779914676cb1e931bf2429f37f629f86b432a5c6adbb84`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `f6bee599168504aabc5841db04bc20810e822fd2af8545bc98e19f6298c38285`
- Metadata SHA-256: `cd34fc596ce17b79112511df2244a7b68d45546111925715157c8598360bb097`
- Executor SHA-256: `c5ece8c6632badb84ff79ee67e4bea96a1d1db7e8afd66de87486af43e8fdd16`
- Runtime SHA-256: `5c4532cfa9ada91c16b3ae2d69922296ddc7c2c1c61841e01bc9c804be1b85fe`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_confirmed_target_matrix` | PASS | with_skill 仅生成 deploy/local、deploy/docker 和 deploy/helm 三类资产；未生成其他部署目标。 |
| `keeps_api_only_topology` | PASS | docker-compose.yml 仅定义 api 服务；快照及说明均未引入数据库、Redis、migration、DATABASE_URL 或额外服务。 |
| `uses_confirmed_runtime_contract` | PASS | local/start.sh 使用 uvicorn app.main:app，默认端口 8000；Dockerfile 使用同一入口和端口；Compose 健康检查及 Helm 存活/就绪探针均访问 /health。 |
| `stays_within_deployment_scope` | PASS | with_skill 清单未包含 CI/CD 配置，输出仅描述构建/安装命令；没有实际镜像发布或环境部署的执行证据。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=000bcbda1f774e89fec492193e606a35b1ac2f41c0b29e0c9ac66b491aa38c8b; fixture_sha256=259dab4dbfe64941c0c3fdd5c97b56c6b90abb97168eeb7461bd9a7bf8e30888; snapshot_sha256=d14459621409a3fa9a746db173da0aa1113f87dc75f4074ea74c26db61f52c90
- Behavior: 生成了确认的三类部署资产并保持 API-only 拓扑及运行时契约；未涉及 CI/CD 或实际发布。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=000bcbda1f774e89fec492193e606a35b1ac2f41c0b29e0c9ac66b491aa38c8b; fixture_sha256=259dab4dbfe64941c0c3fdd5c97b56c6b90abb97168eeb7461bd9a7bf8e30888; snapshot_sha256=800df9ae97e9c12a8f727e3bd2f35c81bec1005aaa854e0fb48207e22531b479
- Behavior: 生成了 local、Docker、Helm 部署资产，保持 API-only 拓扑并符合运行时契约；未涉及 CI/CD 或实际发布。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Migration Status

## Current Result

- Evidence status: **STALE**
- Migration status: **PENDING**
- Blocking reason: this eval has not yet been rerun under the Issue #246 scenario, lane-isolation, and fresh-judge contract.
Overall result: BLOCKED

## Historical Context (Superseded)

The complete pre-migration comparison follows unchanged. It is retained only as historical context and is not current release evidence.

---

# Eval Result: eval-002-python-api-only

## Evaluation Target

- Agent: `devops`
- Skill: `deployment-planner`
- Eval: `eval-002-python-api-only`
- Test case: `python-api-only`
- Workspace: `agents/devops/test/deployment-planner/evals/workspace/eval-002-python-api-only`

## Latest Result

- Fresh run: `2026-08-07`（issue #238 严格隔离重跑）
- Model: `gpt-5.6-luna`，`model_reasoning_effort=medium`
- Isolation: baseline 使用随机顶层 root；完成后仅保存在内存快照并删除 root，随后才创建 with_skill root；with_skill root 删除后才创建独立 judge root。两条 lane 的原始 prompt、fixture snapshot、`HOME` 与 `CODEX_HOME` 值相同。
- Judge: 独立 fresh `codex exec`，读取实际产物、final、status 与工具轨迹，对照当前 assertions 判定；不采信 lane 自评。
- Behavior result: PASS
- Coverage result: FULL
- Without-skill comparison: FAIL（仅作对照，不参与 durable Overall 组合）

Overall result: PASS

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Eval definition: `agents/devops/test/deployment-planner/evals/evals.json`
- Metadata: `agents/devops/test/deployment-planner/evals/workspace/eval-002-python-api-only/eval_metadata.json`
- Expected output: 生成简化的部署配置，不包含数据库相关内容
- Fixture: `PM_HANDOFF.md`, `pyproject.toml`, `app/main.py`

## Assertion Results

| Assertion | with_skill | without_skill | Evidence |
| --- | --- | --- | --- |
| `deploy_local_env_example_database_url` | PASS | FAIL | with_skill/deploy/local/.env.example exists and contains only APP_HOST and APP_PORT, with no DATABASE_URL. The without_skill lane lacks the expected deploy/local/.env.example artifact. |
| `deploy_docker_docker_compose_yml_app` | PASS | FAIL | with_skill/deploy/docker/docker-compose.yml defines exactly one service, api. The without_skill lane lacks the expected deploy/docker/docker-compose.yml artifact. |
| `deploy_local_start_sh` | PASS | FAIL | with_skill/deploy/local/start.sh only checks Python dependencies and starts uvicorn; it has no database initialization. The without_skill lane lacks the expected deploy/local/start.sh artifact. |

## With-Skill Behavior

- with_skill 三条断言均可核查且全部满足，因此 Coverage 为 FULL、durable Overall 为 PASS。without_skill 缺少断言所要求的文件，按 baseline_policy 判为 FAIL，但不影响 durable Overall。
- Workspace changes: added: `deploy/docker/.env.example`, `deploy/docker/Dockerfile`, `deploy/docker/README.md`, `deploy/docker/docker-compose.yml`, `deploy/helm/Chart.yaml`, `deploy/helm/README.md`, `deploy/helm/templates/_helpers.tpl`, `deploy/helm/templates/deployment.yaml`, `deploy/helm/templates/hpa.yaml`, `deploy/helm/templates/ingress.yaml`, `deploy/helm/templates/service.yaml`, `deploy/helm/values.yaml`, `deploy/local/.env.example`, `deploy/local/README.md`, `deploy/local/start.sh`。

## Fresh Without-Skill Baseline

- baseline 在本轮重新生成，没有复用历史 baseline，也没有读取 target skill、with_skill 产物或旧 comparison。
- Workspace changes: added: `.dockerignore`, `DEPLOYMENT.md`, `Dockerfile`, `compose.yaml`, `helm/status-api/Chart.yaml`, `helm/status-api/templates/NOTES.txt`, `helm/status-api/templates/_helpers.tpl`, `helm/status-api/templates/deployment.yaml`, `helm/status-api/templates/service.yaml`, `helm/status-api/values.yaml`。
- assertion 结果见上表；baseline 只用于比较 skill 增益，不作为 durable Overall 的独立机器门禁。

## Failures and Coverage Gaps

- with_skill 无 assertion failure。
- 所有当前 assertions 均已实际覆盖。
- 无模型、认证、runner 或外部服务 blocker。

## Historical Result (Old Contract)

- 旧结论为 PASS（3/3）；issue #234 修复 eval 泄漏后，该结论被标为 BLOCKED 等待重跑。
- 该历史结论适用旧 eval 契约；本文件顶部的 2026-08-07 fresh 结果已取代它作为 latest durable 结论。

## Next Steps

- 保留当前回归用例；后续 skill、fixture 或断言变化时继续执行同等严格的 fresh paired run。

## Runtime Artifact Policy

- 两条 lane、工具轨迹、状态、文件快照、judge verdict 与隔离事件只保存在 `tmp/eval-runs/issue-238-devops-strict-20260806/`，不提交 git。
- durable 结果只保留本 `comparison.md`。
