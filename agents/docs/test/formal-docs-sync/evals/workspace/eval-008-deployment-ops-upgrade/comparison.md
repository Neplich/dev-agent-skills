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
- Fixture SHA-256: `214f53e3513d921f93697a6af50dd22ab635d80910879e93ccbc5d847195e845`
- Prompt SHA-256: `47aecb4a312eb41566bd1acc858dd108cbb65075c955dc6992e37865198bfec5`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f24bfeb12dba77a74fcf3f0161749ae4671b83762eac08484e7ae08621d9bacb`
- Skill overlay SHA-256: `5dbb8d8559bfab3926047aa028e19f362490751247c2142101cfd687fff5239e`
- Judge schema SHA-256: `f5d562d8581b8e42e3d9fc6fee3e3cf82b682235e3b52ce9b9c4f91a22e1e752`
- Eval definition SHA-256: `7fe3c7ecf4038349101f98fb6f2ef19330f01c150bee2276a165994129650157`
- Metadata SHA-256: `2f78367477eb99dc045585689bae85fd3302b30aa534650ea910cd64f9bdfbbe`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_executed_deployment_evidence` | PASS | 交付页面明确引用 deploy/compose.yaml、deployment-evidence/deployment-results.md 和环境差异；启动、升级、健康检查及回滚内容均与已执行结果一致。 |
| `writes_current_ops_upgrade_rollback` | PASS | Docker 页面记录 Compose 启动/升级、/healthz HTTP 200 成功标准及回滚到 v1.4.1 后复查；image-sources.md 记录 AI_HUB_IMAGE 默认 registry.example/ai-hub:v1.4.2 及 Compose 证据。 |
| `does_not_promote_plan_to_current_state` | PASS | 部署索引明确 Kubernetes/Helm 未支持且迁移仍是未执行计划，未写入已部署或可执行现状。 |
| `writes_current_deployment_tree_atomically` | PASS | 四个部署页面均为 last_verified_version: unverified；Ops 导航、部署索引、Docker 索引和 image-sources 页面及链接均已交付，change-map 覆盖 deploy/compose.yaml 与 deploy/** 并保留 exclude；git evidence 显示未修改 product、design、database 或 Release Notes。 |
| `runs_ops_host_checks_and_handoffs` | NOT_EXERCISED | runner_captured_trace 证明在 docs/site 执行 npm run test:docs，exit 0，76/76 通过，且未执行部署命令；但 audit_handoff 明确因 target_release_version missing 而 blocked，未能证明已完成 docs-agent:docs-audit handoff。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47aecb4a312eb41566bd1acc858dd108cbb65075c955dc6992e37865198bfec5; fixture_sha256=214f53e3513d921f93697a6af50dd22ab635d80910879e93ccbc5d847195e845; output_sha256=3d4d3a611262aa31d0ae4872e8dea6ab2efb03158c50ca3dc63282812a2d6b52; snapshot_sha256=fdffd7e4f5336b8b28041773fce0417328d0496885115c4aed4322605b7dafa7
- Behavior: 交付了基于已执行证据的四页部署文档，完成导航与 change-map 原子更新，并通过 76 项文档测试；审计 handoff 因缺少 release version 被阻塞。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47aecb4a312eb41566bd1acc858dd108cbb65075c955dc6992e37865198bfec5; fixture_sha256=214f53e3513d921f93697a6af50dd22ab635d80910879e93ccbc5d847195e845; output_sha256=89a5e6bb0c0c92923c8cc75bf57ee5b0599980afba7477a66a2c00490bd49282; snapshot_sha256=4ae4eb20880d5d638cfdd155f518ad9ada95ce84047e3476cf02855a498916ca
- Behavior: 新建了四页部署文档并声称测试和构建通过，但保留生成物，未同步现有 Ops 导航或 change-map，整体更新不完整。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 提供 target release version 后完成 docs-agent:docs-audit handoff。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
