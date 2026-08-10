# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-011-deployment-three-class-backfill`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `4d8408c1113f0b188f486ff52a1805928dda107a5b4bcef41d15ff086a7d524c` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-011-deployment-three-class-backfill`.
- Fixture SHA-256: `4d8408c1113f0b188f486ff52a1805928dda107a5b4bcef41d15ff086a7d524c`
- Prompt SHA-256: `bed66a02e7102d84cc8988d8318b854a858b57d12888f0168cc60650b6d45cd2`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f24bfeb12dba77a74fcf3f0161749ae4671b83762eac08484e7ae08621d9bacb`
- Skill overlay SHA-256: `5dbb8d8559bfab3926047aa028e19f362490751247c2142101cfd687fff5239e`
- Judge schema SHA-256: `2e68facf61317de81b206f59b17f3e724dc3951afae11b2a8c4aad6ddba91a26`
- Eval definition SHA-256: `75d9816433885deaa537c3684a33cbf77a210bf3435c193880901b7467aafb6d`
- Metadata SHA-256: `e1dbc6626788bdd9110a7a2968862f7b97506d86b4133c4cf183a556eecf36ce`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_three_class_page_tree` | PASS | with_skill 的 delivery_snapshot 直接包含根索引、共享环境页，以及 Development、Docker、Kubernetes/Helm 三类及全部指定子页；根页提供范围、证据状态和导航。 |
| `cross_checks_environment_reference` | PASS | with_skill 的 environment-reference.md 交叉列出 APP_PORT、LOG_LEVEL、DATABASE_URL、LEGACY_TIMEOUT 及 Helm Secret 引用，覆盖类型、必填性/默认值、适用类别、注入方式、敏感性和证据，并明确 LEGACY_TIMEOUT 已废弃；源文件与模板内容相互一致。 |
| `separates_class_specific_contracts` | PASS | 三个类别的锁定页面分别包含前置条件、配置、命令、成功标准、回滚和故障处理，并分别绑定真实源码/Compose/Helm范围；Helm页面覆盖 namespace、Secret、migration hook、rollout/rollback 和 Chart/values/image 子页。 |
| `maps_each_class_atomically` | PASS | delivery_snapshot 中的 change-map 分别映射 scripts/dev/**、Dockerfile、deploy/docker/**、deploy/helm/** 及共享配置范围，并保留 src/product/** 的 custom_owner_field；runner trace 记录了页面读回和映射检查。 |
| `runs_nested_docs_checks` | NOT_EXERCISED | runner_captured_trace 证明在 docs/site 执行 npm run test:docs，首次链接问题修复后 3 项测试全部通过；但没有可证明的 public/internal 构建或递归导航检查，且 audit_handoff 因 target_release_version missing 为 blocked，未完成 docs-agent:docs-audit handoff。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=bed66a02e7102d84cc8988d8318b854a858b57d12888f0168cc60650b6d45cd2; fixture_sha256=4d8408c1113f0b188f486ff52a1805928dda107a5b4bcef41d15ff086a7d524c; output_sha256=cc9bdfa13974a061d2072e117b04f37fdd53cf35f5fd5551c4add323a88b6e03; snapshot_sha256=e63226d7a7801a6acb1aedf507483ca751fdc7843c1baf1347ea777d78d5de18
- Behavior: 完成并交付三类部署文档、环境矩阵和 change-map；主机文档测试最终通过，但审计交接受缺失 release version 和站点构建配置限制。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=bed66a02e7102d84cc8988d8318b854a858b57d12888f0168cc60650b6d45cd2; fixture_sha256=4d8408c1113f0b188f486ff52a1805928dda107a5b4bcef41d15ff086a7d524c; output_sha256=2b0da4aed4aa7310c7a83fcf0cf602ad0f5bd3068bd53b904ed0e16bfade7969; snapshot_sha256=d7b29438e55234c23af0c93a2328be63fb199633986ef0a0312e76acbecb9c87
- Behavior: 也交付了三类页面树和基础导航，但环境参考及各类运行手册明显较简略，未提供 with_skill 的完整参数矩阵、类别边界和逐类运行结构。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 确认 target release version 后完成 docs-agent:docs-audit handoff。
- Next: 若要求 public/internal 覆盖，补充并运行对应站点构建或递归导航检查。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
