# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `deployment-planner`
- Eval: `eval-001-nextjs-web-app`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `06f8a5807d1130b7a91a700b2074192e6dfed0933a071ce16642b27aa050360d` from `agents/devops/test/deployment-planner/evals/workspace/eval-001-nextjs-web-app`.
- Fixture SHA-256: `06f8a5807d1130b7a91a700b2074192e6dfed0933a071ce16642b27aa050360d`
- Prompt SHA-256: `cd186dfdcf8b04b4e66f71faf5fd0b7ea6c6616c86ae2015f0fd5d6d730418e8`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `762ea3248d76c5c9e715368b11ab616562bb9bdb0e2bd6a6aad38d47cc80b3af`
- Skill overlay SHA-256: `52ed13d453014671ce8cc7f7f7ce4b4108c3a5cc943fcf3bece1ac66b08625d5`
- Judge schema SHA-256: `8fdd554bf7008e1addc7b92301444335139887034f2813ab539445a1df4b82d6`
- Eval definition SHA-256: `4ab6f3577023497f11197efb5117e95119ab70a437c95770925330f5be6aa5f2`
- Metadata SHA-256: `be29fd9ddbc554b7d8ca7f9912c9d54f61470e99abd7c2e138b60022c4086794`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_local_runtime_assets` | PASS | With-skill snapshot includes deploy/local/.env.example and executable deploy/local/start.sh plus README documenting npm run start, port 3000, DATABASE_URL, and REDIS_URL. |
| `creates_complete_compose_topology` | PASS | With-skill snapshot includes Dockerfile and docker-compose.yml defining app, postgres, and redis services; app healthcheck calls /api/health and dependencies have healthchecks. |
| `creates_application_helm_chart` | PASS | With-skill snapshot includes Chart.yaml, values.yaml, and Deployment template with replicaCount and PostgreSQL/Redis values injected through the Secret. |
| `documents_each_target_without_delivery` | PASS | Local, Docker, Helm, and deploy/README.md document usage and health checks; evidence explicitly states no deployment and no CI/CD rules, with placeholder credentials only. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cd186dfdcf8b04b4e66f71faf5fd0b7ea6c6616c86ae2015f0fd5d6d730418e8; fixture_sha256=06f8a5807d1130b7a91a700b2074192e6dfed0933a071ce16642b27aa050360d; output_sha256=cdb26857568fc97cd812f806d4331ad234b98ba44a8612161ad5938152041370; snapshot_sha256=893888204298be503f0a41a545efdd35638d4069c1b49cf441d6fce4cf1b8bad
- Behavior: Delivered all three deployment targets with executable local startup, complete Compose topology, application-only Helm chart, cross-target documentation, and explicit non-deployment status.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cd186dfdcf8b04b4e66f71faf5fd0b7ea6c6616c86ae2015f0fd5d6d730418e8; fixture_sha256=06f8a5807d1130b7a91a700b2074192e6dfed0933a071ce16642b27aa050360d; output_sha256=34a08a9de7c2660c327965458e3411f495f0710a53b4e5ac8b3fb9cdb1423065; snapshot_sha256=3813549542ec815eecb28561137e3da9f7264ee4e33113b6577940d44ab237b6
- Behavior: Delivered local, Docker, and Helm assets with required topology and documentation, but without the additional executable local startup script and deployment matrix present in the with_skill lane.
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
- Eval: `eval-001-nextjs-web-app`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `06f8a5807d1130b7a91a700b2074192e6dfed0933a071ce16642b27aa050360d` from `agents/devops/test/deployment-planner/evals/workspace/eval-001-nextjs-web-app`.
- Fixture SHA-256: `06f8a5807d1130b7a91a700b2074192e6dfed0933a071ce16642b27aa050360d`
- Prompt SHA-256: `cd186dfdcf8b04b4e66f71faf5fd0b7ea6c6616c86ae2015f0fd5d6d730418e8`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `762ea3248d76c5c9e715368b11ab616562bb9bdb0e2bd6a6aad38d47cc80b3af`
- Skill overlay SHA-256: `52ed13d453014671ce8cc7f7f7ce4b4108c3a5cc943fcf3bece1ac66b08625d5`
- Judge schema SHA-256: `8fdd554bf7008e1addc7b92301444335139887034f2813ab539445a1df4b82d6`
- Eval definition SHA-256: `4ab6f3577023497f11197efb5117e95119ab70a437c95770925330f5be6aa5f2`
- Metadata SHA-256: `be29fd9ddbc554b7d8ca7f9912c9d54f61470e99abd7c2e138b60022c4086794`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_local_runtime_assets` | PASS | with_skill 快照包含 deploy/local/.env.example、README.md 和可执行 start.sh；配置包含 npm run start、端口 3000、DATABASE_URL 与 REDIS_URL。 |
| `creates_complete_compose_topology` | PASS | with_skill 快照包含 Dockerfile 和 Compose，编排 app、postgres、redis；app healthcheck 请求 /api/health。 |
| `creates_application_helm_chart` | PASS | with_skill 快照包含 Chart.yaml、values.yaml 与 Deployment 模板；Deployment 使用 replicaCount，values 提供外部 databaseUrl 和 redisUrl，并且未创建 PostgreSQL/Redis 工作负载。 |
| `documents_each_target_without_delivery` | PASS | local、Docker、Helm 均有 README；PM_HANDOFF 约束均被覆盖。快照显示未新增 CI/CD、凭据均为占位值，最终输出明确说明未执行实际部署。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cd186dfdcf8b04b4e66f71faf5fd0b7ea6c6616c86ae2015f0fd5d6d730418e8; fixture_sha256=06f8a5807d1130b7a91a700b2074192e6dfed0933a071ce16642b27aa050360d; output_sha256=602f31f669b24c8151bce4956f9df102a6951db222e6ba5d1db5808ad709bc1b; snapshot_sha256=164aec1d41af811f735830b335e6f91a50e2b0837354757597d122379e5748db
- Behavior: 交付了符合仓库约束的 local、Docker Compose 和仅应用 Helm 配置，并明确未部署。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cd186dfdcf8b04b4e66f71faf5fd0b7ea6c6616c86ae2015f0fd5d6d730418e8; fixture_sha256=06f8a5807d1130b7a91a700b2074192e6dfed0933a071ce16642b27aa050360d; output_sha256=c1e99a0543531b9e858f515b8660d1329bf91d6de62448ddc86037c878617a55; snapshot_sha256=20396f089a0e38128bf90426aad6aec7ea2f3ad8115fd476a2d81d608f1bb34b
- Behavior: 提供了三类部署资产，但 local 使用 npm run dev 且缺少应用 Compose 健康检查，作为 fresh baseline 对比不满足全部断言。
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
- Eval: `eval-001-nextjs-web-app`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `06f8a5807d1130b7a91a700b2074192e6dfed0933a071ce16642b27aa050360d` from `agents/devops/test/deployment-planner/evals/workspace/eval-001-nextjs-web-app`.
- Fixture SHA-256: `06f8a5807d1130b7a91a700b2074192e6dfed0933a071ce16642b27aa050360d`
- Prompt SHA-256: `cd186dfdcf8b04b4e66f71faf5fd0b7ea6c6616c86ae2015f0fd5d6d730418e8`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `762ea3248d76c5c9e715368b11ab616562bb9bdb0e2bd6a6aad38d47cc80b3af`
- Skill overlay SHA-256: `52ed13d453014671ce8cc7f7f7ce4b4108c3a5cc943fcf3bece1ac66b08625d5`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `4ab6f3577023497f11197efb5117e95119ab70a437c95770925330f5be6aa5f2`
- Metadata SHA-256: `be29fd9ddbc554b7d8ca7f9912c9d54f61470e99abd7c2e138b60022c4086794`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_local_runtime_assets` | PASS | with_skill 的 deploy/local/README.md 与 start.sh 使用 npm run start、3000、DATABASE_URL 和 REDIS_URL；deploy/local/.env.example 也包含两项依赖地址。 |
| `creates_complete_compose_topology` | PASS | with_skill 的 deploy/docker/ 包含 Dockerfile、README.md 和 Compose；Compose 定义 app、postgres、redis，并通过 /api/health 检查 app。 |
| `creates_application_helm_chart` | PASS | with_skill 的 deploy/helm/ 包含 Chart.yaml、values.yaml 和 Deployment 模板；Deployment 使用 replicaCount，并从 values 的 secrets.databaseUrl/secrets.redisUrl 注入外部依赖地址，未部署 PostgreSQL 或 Redis。 |
| `documents_each_target_without_delivery` | PASS | with_skill 为 local、Docker、Helm 提供说明，声明无 CI/CD 配置、使用占位凭据且未执行实际部署；交付快照未显示生产凭据或部署动作。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cd186dfdcf8b04b4e66f71faf5fd0b7ea6c6616c86ae2015f0fd5d6d730418e8; fixture_sha256=06f8a5807d1130b7a91a700b2074192e6dfed0933a071ce16642b27aa050360d; output_sha256=f905734282eb12aca4e6a221a4fa47b751d48a9b21d5e03b69302d736ff7880c; snapshot_sha256=b89d6c129881d79f7962c83d5faf6d7fbdf84c721b93391679f9280b154fe8f2
- Behavior: Delivered complete local, Docker, and Helm configuration assets and explicitly reported that deployment was not performed.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cd186dfdcf8b04b4e66f71faf5fd0b7ea6c6616c86ae2015f0fd5d6d730418e8; fixture_sha256=06f8a5807d1130b7a91a700b2074192e6dfed0933a071ce16642b27aa050360d; output_sha256=768f6e68115e39cbc6f6752e3e15ebdb0bc7909d2b071d28d3cbba0b08124155; snapshot_sha256=3446a997d1d5eff7fde2a11842c05406a70b42b9300c0bc288788005de591d8e
- Behavior: Docker and Helm assets were documented, but the local README used npm run dev and no local startup script was present.
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
- Eval: `eval-001-nextjs-web-app`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `06f8a5807d1130b7a91a700b2074192e6dfed0933a071ce16642b27aa050360d` from `agents/devops/test/deployment-planner/evals/workspace/eval-001-nextjs-web-app`.
- Fixture SHA-256: `06f8a5807d1130b7a91a700b2074192e6dfed0933a071ce16642b27aa050360d`
- Prompt SHA-256: `cd186dfdcf8b04b4e66f71faf5fd0b7ea6c6616c86ae2015f0fd5d6d730418e8`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `6b7ee50b1667fd76ae49358cc3af5366a7e75afc33e7c444bb73e4e03310853a`
- Skill overlay SHA-256: `c38a517fc6ad0bdb4f779914676cb1e931bf2429f37f629f86b432a5c6adbb84`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `4ab6f3577023497f11197efb5117e95119ab70a437c95770925330f5be6aa5f2`
- Metadata SHA-256: `be29fd9ddbc554b7d8ca7f9912c9d54f61470e99abd7c2e138b60022c4086794`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_local_runtime_assets` | PASS | With_skill snapshot contains deploy/local/.env.example with PORT=3000, DATABASE_URL, and REDIS_URL; deploy/local/start.sh validates both URLs and executes npm run start. README documents usage. |
| `creates_complete_compose_topology` | PASS | With_skill snapshot contains deploy/docker/Dockerfile and docker-compose.yml defining app, postgres, and redis. The app healthcheck requests /api/health. |
| `creates_application_helm_chart` | PASS | With_skill snapshot contains deploy/helm/Chart.yaml, values.yaml, and templates/deployment.yaml. Deployment uses .Values.replicaCount and injects external databaseUrl/redisUrl through values-backed Secret references. |
| `documents_each_target_without_delivery` | PASS | With_skill snapshot includes README files for local, Docker, and Helm. Documentation matches the repository constraints, uses placeholders or externally managed secrets, adds no CI/CD, and explicitly states no actual deployment occurred. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cd186dfdcf8b04b4e66f71faf5fd0b7ea6c6616c86ae2015f0fd5d6d730418e8; fixture_sha256=06f8a5807d1130b7a91a700b2074192e6dfed0933a071ce16642b27aa050360d; output_sha256=b22099699ceb60fc41d616eb3e68d757ae685a6a5ffb7c4ec7a3d58a0a07278a; snapshot_sha256=b1afc5aa33bd8f3c654dba147382fb95ed89f499345084dcfe7bee3bff79ee75
- Behavior: Provided complete local, Docker, and Helm deployment assets with startup behavior, dependency topology, health checks, external dependency injection, and usage documentation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cd186dfdcf8b04b4e66f71faf5fd0b7ea6c6616c86ae2015f0fd5d6d730418e8; fixture_sha256=06f8a5807d1130b7a91a700b2074192e6dfed0933a071ce16642b27aa050360d; output_sha256=1b7a470f8695b70e3fa6d80af5c8b275696008abb77f21ed7b8d931cf64a081d; snapshot_sha256=48b7687d8fdec7474857fe4949e9031488da46adef2d11200407039c90b025dd
- Behavior: Provided local, Docker, and Helm assets, but local used a dependency-only Compose file and documented npm run dev rather than supplying the required start script/runtime path.
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

# Eval Result: eval-001-nextjs-web-app

## Evaluation Target

- Agent: `devops`
- Skill: `deployment-planner`
- Eval: `eval-001-nextjs-web-app`
- Test case: `nextjs-web-app`
- Workspace: `agents/devops/test/deployment-planner/evals/workspace/eval-001-nextjs-web-app`

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
- Metadata: `agents/devops/test/deployment-planner/evals/workspace/eval-001-nextjs-web-app/eval_metadata.json`
- Expected output: 在 deploy/ 目录下生成三个子目录，每个包含 README.md 和相应的配置文件
- Fixture: `PM_HANDOFF.md`, `package.json`, `app/api/health/route.ts`

## Assertion Results

| Assertion | with_skill | without_skill | Evidence |
| --- | --- | --- | --- |
| `deploy_local_readme_md` | PASS | PASS | 两条 lane 均存在 deploy/local/README.md。 |
| `deploy_local_env_example_database_url_redis_url` | PASS | PASS | 两条 lane 的 deploy/local/.env.example 均包含 DATABASE_URL 和 REDIS_URL。 |
| `deploy_local_start_sh` | PASS | PASS | 两条 lane 的 deploy/local/start.sh 均具有可执行权限（-rwxr-xr-x）。 |
| `deploy_docker_dockerfile` | PASS | PASS | 两条 lane 均存在 deploy/docker/Dockerfile。 |
| `deploy_docker_docker_compose_yml_app_postgres_redis` | PASS | FAIL | with_skill 存在 deploy/docker/docker-compose.yml，且包含 app、postgres、redis；without_skill 仅有 compose.yaml，目标 docker-compose.yml 缺失。 |
| `deploy_helm_chart_yaml` | PASS | FAIL | with_skill 存在 deploy/helm/Chart.yaml；without_skill 的 Chart.yaml 位于 deploy/helm/analytics-web/Chart.yaml，目标路径缺失。 |
| `deploy_helm_values_yaml_replicacount` | PASS | FAIL | with_skill 的 deploy/helm/values.yaml 包含 replicaCount；without_skill 目标路径 deploy/helm/values.yaml 缺失，文件位于嵌套目录。 |
| `deploy_helm_templates_deployment_yaml` | PASS | FAIL | with_skill 存在 deploy/helm/templates/deployment.yaml；without_skill 目标路径缺失，文件位于 deploy/helm/analytics-web/templates/deployment.yaml。 |

## With-Skill Behavior

- with_skill 实际产物满足全部 8 项断言，覆盖完整，因此 durable Overall 为 PASS。without_skill 作为对照在 4 项路径/文件断言上失败，但不影响 durable Overall。
- Workspace changes: added: `deploy/docker/.dockerignore`, `deploy/docker/.env.example`, `deploy/docker/Dockerfile`, `deploy/docker/README.md`, `deploy/docker/docker-compose.yml`, `deploy/helm/Chart.yaml`, `deploy/helm/README.md`, `deploy/helm/templates/_helpers.tpl`, `deploy/helm/templates/configmap.yaml`, `deploy/helm/templates/deployment.yaml`, `deploy/helm/templates/hpa.yaml`, `deploy/helm/templates/ingress.yaml`, `deploy/helm/templates/secret.yaml`, `deploy/helm/templates/service.yaml`, `deploy/helm/values.yaml`, `deploy/local/.env.example`, `deploy/local/README.md`, `deploy/local/start.sh`。

## Fresh Without-Skill Baseline

- baseline 在本轮重新生成，没有复用历史 baseline，也没有读取 target skill、with_skill 产物或旧 comparison。
- Workspace changes: added: `deploy/README.md`, `deploy/docker/Dockerfile`, `deploy/docker/README.md`, `deploy/docker/compose.yaml`, `deploy/helm/analytics-web/Chart.yaml`, `deploy/helm/analytics-web/README.md`, `deploy/helm/analytics-web/templates/_helpers.tpl`, `deploy/helm/analytics-web/templates/deployment.yaml`, `deploy/helm/analytics-web/templates/ingress.yaml`, `deploy/helm/analytics-web/templates/service.yaml`, `deploy/helm/analytics-web/values.yaml`, `deploy/local/.env.example`, `deploy/local/.gitignore`, `deploy/local/README.md`, `deploy/local/start.sh`。
- assertion 结果见上表；baseline 只用于比较 skill 增益，不作为 durable Overall 的独立机器门禁。

## Failures and Coverage Gaps

- with_skill 无 assertion failure。
- 所有当前 assertions 均已实际覆盖。
- 无模型、认证、runner 或外部服务 blocker。

## Historical Result (Old Contract)

- 旧结论为 PASS（8/8）；issue #234 修复 eval 泄漏后，该结论被标为 BLOCKED 等待重跑。
- 该历史结论适用旧 eval 契约；本文件顶部的 2026-08-07 fresh 结果已取代它作为 latest durable 结论。

## Next Steps

- 保留当前回归用例；后续 skill、fixture 或断言变化时继续执行同等严格的 fresh paired run。

## Runtime Artifact Policy

- 两条 lane、工具轨迹、状态、文件快照、judge verdict 与隔离事件只保存在 `tmp/eval-runs/issue-238-devops-strict-20260806/`，不提交 git。
- durable 结果只保留本 `comparison.md`。
