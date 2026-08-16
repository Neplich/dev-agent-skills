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
- Identity schema: `2`
- target_skill_sha256: `ff61dcd9673d160376da3723849f195022899b8e8a38fe78c67e4488f9065a5f`
- eval_definition_sha256: `4ab6f3577023497f11197efb5117e95119ab70a437c95770925330f5be6aa5f2`
- metadata_sha256: `de5df4ca13d82c9e7bb152be1484594454c0cf0e1976add64d71c7e6648955c1`
- fixture_sha256: `06f8a5807d1130b7a91a700b2074192e6dfed0933a071ce16642b27aa050360d`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `8fdd554bf7008e1addc7b92301444335139887034f2813ab539445a1df4b82d6`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `cd186dfdcf8b04b4e66f71faf5fd0b7ea6c6616c86ae2015f0fd5d6d730418e8`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `aed4a3cdd1170f44446df97f66f60c0f6ae2151f3522fe982eb11ee05d551389`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_local_runtime_assets` | PASS | with_skill 的 delivery_snapshot 包含 deploy/local/.env.example、deploy/local/README.md 和可执行 deploy/local/start.sh；脚本校验 Node.js 22、DATABASE_URL、REDIS_URL，执行 npm run build 后 npm run start，端口配置为 3000。 |
| `creates_complete_compose_topology` | PASS | with_skill 的 deploy/docker/Dockerfile 和 deploy/docker/docker-compose.yml 直接提供应用镜像及 app、postgres、redis 三个服务；Compose 含依赖健康条件，并以 /api/health 作为 app 健康检查。 |
| `creates_application_helm_chart` | PASS | with_skill 的 deploy/helm/Chart.yaml、values.yaml 和 templates/deployment.yaml 构成 Helm chart；Deployment 使用 .Values.replicaCount，values.env 注入外部 PostgreSQL 与 Redis 地址，且未部署数据库或 Redis 服务。 |
| `documents_each_target_without_delivery` | PASS | with_skill 提供 deploy/README.md、各目标 README 和启动命令说明；deploy/README.md 明确不创建 CI/CD，示例仅使用占位凭据，且候选输出明确未执行实际部署。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cd186dfdcf8b04b4e66f71faf5fd0b7ea6c6616c86ae2015f0fd5d6d730418e8; fixture_sha256=06f8a5807d1130b7a91a700b2074192e6dfed0933a071ce16642b27aa050360d; output_sha256=a811e4779fffbbe0d8ca5ac415fa013fb898c219820890c154c17bd4c3cc738d; snapshot_sha256=4603abd9fda52287fb04ddf628bfeed857e6812724f54b661ef02e375b044616
- Behavior: 交付了 local、Docker Compose 和仅应用 Helm 配置，并提供契约一致的说明；未执行部署。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cd186dfdcf8b04b4e66f71faf5fd0b7ea6c6616c86ae2015f0fd5d6d730418e8; fixture_sha256=06f8a5807d1130b7a91a700b2074192e6dfed0933a071ce16642b27aa050360d; output_sha256=63b0a5f0606bc0395cccfef6f2141067c9147649d68527c4c25bc640669d21e0; snapshot_sha256=cadd089ad52e4f59839ffc9abda902244ed71e2557b05662dd59aed11eb0d536
- Behavior: 同样交付了三类配置，结构更精简；可作为 fresh baseline 对照，不影响 with_skill 的断言判定。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
