# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-008-deployment-ops-upgrade`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `214f53e3513d921f93697a6af50dd22ab635d80910879e93ccbc5d847195e845` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-008-deployment-ops-upgrade`.
- Identity schema: `2`
- target_skill_sha256: `dd975083d3977d90b71b3396dff2498ef2b7e8d49c50fab50b5462a26f3248ee`
- eval_definition_sha256: `7fe3c7ecf4038349101f98fb6f2ef19330f01c150bee2276a165994129650157`
- metadata_sha256: `2f78367477eb99dc045585689bae85fd3302b30aa534650ea910cd64f9bdfbbe`
- fixture_sha256: `214f53e3513d921f93697a6af50dd22ab635d80910879e93ccbc5d847195e845`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `f5d562d8581b8e42e3d9fc6fee3e3cf82b682235e3b52ce9b9c4f91a22e1e752`
- Identity migration: **MIGRATED_WITHOUT_MODEL_RERUN**
- Identity migration source commit: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Identity migration audit: `docs/engineer/repository-governance/eval-scenario-isolation/eval-identity-v2-migration-audit.json`
- Repository HEAD: `f2aa9b2c49be68550ec45538c221425607f428ce`
- Repository worktree state: **DIRTY**
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_executed_deployment_evidence` | PASS | 交付页面直接绑定了 Compose、执行结果、环境变量和交接证据；文档中的启动、升级、健康检查及回滚事实与原始执行记录一致。 |
| `writes_current_ops_upgrade_rollback` | PASS | Docker 页面记录了 Compose 启动、升级命令、/healthz HTTP 200 成功标准、回滚至 v1.4.1 及回滚后的健康检查；镜像来源页记录了 AI_HUB_IMAGE 默认值和 Compose 证据。 |
| `does_not_promote_plan_to_current_state` | PASS | 部署根页明确将 Kubernetes/Helm 标为 unsupported，并说明迁移仅为未执行计划，没有把计划写成当前支持或已部署状态。 |
| `writes_current_deployment_tree_atomically` | FAIL | 四个部署页面已交付且新页面为 unverified，change-map 已覆盖四页并保留 exclude；但 with_skill 交付未修改 Ops 索引，现有 Ops 链接仍为 ./deployment/，未完成要求的 Ops 导航原子更新。 |
| `runs_ops_host_checks_and_handoffs` | NOT_EXERCISED | runner trace 证明在 docs/site 执行 npm run test:docs 并以 exit 0 通过 76 项测试，且交付记录了构建结果和 blocked audit_handoff；但原始工具事件无法证明实际完成了 docs-agent:docs-audit handoff，且该后续步骤受缺少 release 版本上下文限制。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47aecb4a312eb41566bd1acc858dd108cbb65075c955dc6992e37865198bfec5; fixture_sha256=214f53e3513d921f93697a6af50dd22ab635d80910879e93ccbc5d847195e845; output_sha256=0569210e51db2a5e6f6db7bfceaf133a73d16459b46f9ec0d7272eed64c072b2; snapshot_sha256=102e60d9308c160cfc1977c4ccd93bc4c7524b34b603c4f8f8ac3b20062830b1
- Behavior: 准确基于已执行部署证据生成四个部署页面，正确排除未执行的 Kubernetes/Helm 计划，并通过 docs 主机检查；但遗漏了 Ops 索引更新，且审计 handoff 未被原始事件证明。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47aecb4a312eb41566bd1acc858dd108cbb65075c955dc6992e37865198bfec5; fixture_sha256=214f53e3513d921f93697a6af50dd22ab635d80910879e93ccbc5d847195e845; output_sha256=f927dd1052724768bb240700b45f2a6708033866c03ae82962efbccc425c71c1; snapshot_sha256=b7f12f1e6661948729d3f6734cbdc6f36dd19ba22d0adca7d7aa7627b7095013
- Behavior: 完成了 Ops 索引链接更新并声称检查通过，但其交付证据显示未形成完整的四页文件快照，且包含被工具拒绝的清理命令，整体证据和交付完整性弱于 with_skill。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未完成确认范围中要求的 Ops 索引原子更新。
- Next: 补齐 Ops 索引到 deployment/index.md 的链接，并在同一原子批次中复核四页、导航和 change-map。
- Next: 在具备所需 release 上下文后，明确记录并完成 docs-agent:docs-audit handoff。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
