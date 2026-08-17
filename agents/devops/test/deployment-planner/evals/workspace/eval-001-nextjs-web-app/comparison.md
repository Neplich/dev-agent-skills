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
- Source lock SHA-256: `c58f04d32c2ca3a22aec96f7ee027af648da5971453d2a5553d7ab2cd9272551`
- Prompt SHA-256: `cd186dfdcf8b04b4e66f71faf5fd0b7ea6c6616c86ae2015f0fd5d6d730418e8`
- Repository HEAD: `60a4b3602dc07f3f6683a8873529bbdba6f8d27d`
- Repository worktree state: **CLEAN**
- Skill overlay SHA-256: `a8511777e6b4f31217e6a6c17f2c1dc2d5abd375ef6253072404dae037d7bae7`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_local_runtime_assets` | PASS | with_skill 交付了 deploy/local/.env.example、README.md 和 start.sh；包含 DATABASE_URL、REDIS_URL、3000 端口，并由脚本执行 npm run start。 |
| `creates_complete_compose_topology` | PASS | with_skill 的 Compose 直接编排 app、postgres、redis；app 使用 3000 端口，并以 /api/health 作为健康检查。 |
| `creates_application_helm_chart` | PASS | with_skill 提供 Chart.yaml、values.yaml 和 Deployment 模板；Deployment 使用 replicaCount，并通过 env values/Secret 注入 DATABASE_URL 与 REDIS_URL，同时仅部署应用相关资源。 |
| `documents_each_target_without_delivery` | PASS | with_skill 为 local、Docker、Helm 均提供 README；内容使用占位配置、说明外部依赖，未新增 CI/CD 或生产凭据，也未声称已部署。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cd186dfdcf8b04b4e66f71faf5fd0b7ea6c6616c86ae2015f0fd5d6d730418e8; fixture_sha256=06f8a5807d1130b7a91a700b2074192e6dfed0933a071ce16642b27aa050360d; output_sha256=010f346115799d6b080660c7c9f8d7806581f5f6a7f323d391c74b7f3341bd22; snapshot_sha256=563e278cf58623878e1c281d27276fd888ec5f76f39c186fc6740d3c0e30c2c3
- Behavior: 完整交付三类部署资产，并明确未执行实际部署；Local 启动脚本、Compose 拓扑和 Helm 外部依赖注入均符合契约。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cd186dfdcf8b04b4e66f71faf5fd0b7ea6c6616c86ae2015f0fd5d6d730418e8; fixture_sha256=06f8a5807d1130b7a91a700b2074192e6dfed0933a071ce16642b27aa050360d; output_sha256=525ab20de64189aa99d4565500a1ca4b205693cdf81146b336ac1586958bb7c9; snapshot_sha256=ee13f59195c7054b05e83f85dce8cb5578ef8c0bda791ad7ac6c9f2254aec265
- Behavior: 也交付了基本的 local、Docker 和 Helm 配置；相较之下缺少 Local 启动脚本，但 README 提供了 npm run start 的生产式运行说明。该 lane 仅作为比较基线。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
