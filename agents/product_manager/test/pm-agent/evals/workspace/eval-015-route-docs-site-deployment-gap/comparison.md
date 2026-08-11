# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-015-route-docs-site-deployment-gap`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `16e3b6cbbbae6769ac6b5ead7bae34214b3dd90e3e6c4d5fad97cfd7d3784013` from `agents/product_manager/test/pm-agent/evals/workspace/eval-015-route-docs-site-deployment-gap`.
- Fixture SHA-256: `16e3b6cbbbae6769ac6b5ead7bae34214b3dd90e3e6c4d5fad97cfd7d3784013`
- Prompt SHA-256: `f6c9996daf9a7bdf78228fb674eccb457f386d1e74abf9925ac4646e4da1c9d4`
- Repository HEAD: `ae451ca624c3dfd1bb8d530c3b416d40910caf82`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `619bfdcdc189ae85f09016655828cc88fc4d95591087522dac73338147eaad17`
- Skill overlay SHA-256: `d250e0c694804c4780185b995ee5f122601fe31dbd177a9a2a0571aa28ed8dec`
- Judge schema SHA-256: `69f2798cad12b0dd0ca3c224e3cfd6cf611a315695684db1b07a23452b52a60e`
- Eval definition SHA-256: `6e2d29edefa67ed434a00461a929405f7c4bccd693a99ad48559b546fe6fab29`
- Metadata SHA-256: `e7a743e88e4c53094e4afe2903a87ebcc467ace2dc58c61ccb0a0dcf64ebf2fd`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_unknown_evidence` | PASS | with_skill 直接核对了 access-note.md、CI workflow、Helm values 和 maintainer-decision.md，并基于已补齐的 CI/环境证据给出 public 范围结论；未错误声称 integrated 或 ready handoff。 |
| `builds_repo_wide_deployment_packet` | PASS | with_skill 输出明确包含 request_type: deployment、feature_path/feature/parent_feature/feature_level: N/A、feature_path_evidence: []，并在 source_documents 与 blockers_risks 中保留了实际文件和授权边界证据。 |
| `routes_devops_ordered_chain` | NOT_EXERCISED | with_skill 仅完成了向 DevOps 的下一步路由，并明确 devops-agent 不可用；锁定证据无法证明 devops-agent:deployment-planner → cicd-bootstrap → env-config-auditor → docs-agent:formal-docs-sync 的后续链条或最终 Docs 同步，因此后续断言未执行。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f6c9996daf9a7bdf78228fb674eccb457f386d1e74abf9925ac4646e4da1c9d4; fixture_sha256=16e3b6cbbbae6769ac6b5ead7bae34214b3dd90e3e6c4d5fad97cfd7d3784013; output_sha256=79b7fc8744e99d36352d14f953ccbeb96b961d56559e8ef44e0768c2254a1f87; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 准确读取并综合 CI、Helm、权限说明和维护者决定，生成受约束的 deployment handoff，并在缺少下游能力时停止。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f6c9996daf9a7bdf78228fb674eccb457f386d1e74abf9925ac4646e4da1c9d4; fixture_sha256=16e3b6cbbbae6769ac6b5ead7bae34214b3dd90e3e6c4d5fad97cfd7d3784013; output_sha256=62a0fa55dc4219e5bedeb323d5e1d3735dba3b2882fd50f331ce770e243c4e7e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了 CI/Helm 与维护者授权边界，但仅给出条件式规划建议，未生成标准 deployment handoff。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 安装或提供 devops-agent 后，按 deployment-planner → cicd-bootstrap → env-config-auditor 顺序继续，并在运维事实落地且验证后交给 docs-agent:formal-docs-sync。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
