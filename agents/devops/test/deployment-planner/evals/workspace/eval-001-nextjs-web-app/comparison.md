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
- target_skill_sha256: `dfa906d01a96634826afcebe44c9732902f0bc2b120c6c7b7232879b93b8e923`
- eval_definition_sha256: `4ab6f3577023497f11197efb5117e95119ab70a437c95770925330f5be6aa5f2`
- metadata_sha256: `de5df4ca13d82c9e7bb152be1484594454c0cf0e1976add64d71c7e6648955c1`
- fixture_sha256: `06f8a5807d1130b7a91a700b2074192e6dfed0933a071ce16642b27aa050360d`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `8fdd554bf7008e1addc7b92301444335139887034f2813ab539445a1df4b82d6`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `cd186dfdcf8b04b4e66f71faf5fd0b7ea6c6616c86ae2015f0fd5d6d730418e8`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `a8511777e6b4f31217e6a6c17f2c1dc2d5abd375ef6253072404dae037d7bae7`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_local_runtime_assets` | FAIL | FAIL：`deploy/local/.env.example` 提供了 `DATABASE_URL` 和 `REDIS_URL`，但 `deploy/local/README.md` 与 `start.sh` 均执行 `npm run dev`，未使用仓库契约要求的 `npm run start`。 |
| `creates_complete_compose_topology` | PASS | PASS：Dockerfile 存在；Compose 定义 `app`、`postgres`、`redis`，并通过 `/api/health` 配置应用健康检查。 |
| `creates_application_helm_chart` | PASS | PASS：Helm Chart、values 和 Deployment 模板均存在；Deployment 使用 `.Values.replicaCount`，并通过 values 中的外部数据库和 Redis 地址注入依赖。 |
| `documents_each_target_without_delivery` | FAIL | FAIL：Docker 和 Helm 说明基本符合契约且未执行部署，但 local README/start.sh 使用 `npm run dev`，与要求的 `npm run start` 不一致；未发现 CI/CD 或生产凭据交付。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cd186dfdcf8b04b4e66f71faf5fd0b7ea6c6616c86ae2015f0fd5d6d730418e8; fixture_sha256=06f8a5807d1130b7a91a700b2074192e6dfed0933a071ce16642b27aa050360d; output_sha256=abbdd47b7c88459bd651dc133daf88fedf9834c2c4375e9fc34fccb0e73643af; snapshot_sha256=7282db80bda8a3d830f4caaeaed333f6253fba7a441db3dc2695ca57453925ec
- Behavior: 交付了 local、Docker Compose 和 Helm 文件；Docker 拓扑及 Helm 应用配置满足要求，但 local 启动命令错误。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cd186dfdcf8b04b4e66f71faf5fd0b7ea6c6616c86ae2015f0fd5d6d730418e8; fixture_sha256=06f8a5807d1130b7a91a700b2074192e6dfed0933a071ce16642b27aa050360d; output_sha256=71493a2f06f788965adde72326c4b8ab1c3bc88cd368a263be53e370d1468b01; snapshot_sha256=4a0f091490ea1a339eb077ce792d5666be5198073e4e86a72b535849b7e1ec9d
- Behavior: 也交付了三类配置；Docker 和 Helm 基本满足要求，但 local README 同样使用 `npm run dev` 且未提供启动脚本。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 的 local 启动说明和脚本使用 `npm run dev`，未满足仓库约束中的 `npm run start`。
- 因此 local 目标说明也不完全与仓库契约一致。
- Next: 将 `deploy/local/README.md` 和 `deploy/local/start.sh` 改为使用 `npm run start`，并确保说明仍覆盖端口 3000、DATABASE_URL 和 REDIS_URL。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
