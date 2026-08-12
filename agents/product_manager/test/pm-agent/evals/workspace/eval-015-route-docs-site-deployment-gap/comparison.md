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
- Repository HEAD: `8813f864e743f7c83dc2e51e0b5add79f312e870`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `0616a11ea39f978cac34906ca01c79a336316825183bb1897d900f056d8544f7`
- Skill overlay SHA-256: `4d4a580c5e7c36b9199abb80221829f90c900c96463581d7f87c6d7ccc538bd7`
- Judge schema SHA-256: `69f2798cad12b0dd0ca3c224e3cfd6cf611a315695684db1b07a23452b52a60e`
- Eval definition SHA-256: `8bc69d85fc3ff063d885b8a2c4d7a9ea83b6dca3de23a034dba15fb34f1ba98e`
- Metadata SHA-256: `e7a743e88e4c53094e4afe2903a87ebcc467ace2dc58c61ccb0a0dcf64ebf2fd`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_unknown_evidence` | PASS | with_skill 明确使用 entry_basis: blocked，列出 devops-agent 不可用、未确认 internal 变体及禁止提交/发布/部署等阻塞，没有将状态表述为 ready 或 integrated handoff。 |
| `builds_repo_wide_deployment_packet` | PASS | with_skill 输出包含 request_type: deployment、feature/parent_feature/feature_level/feature_path 为 N/A、feature_path_evidence: []，并在 source_documents 列出四份真实材料、在 blockers_risks 列出环境不可用、授权边界和 internal 变体未确认等证据。 |
| `routes_devops_ordered_chain` | NOT_EXERCISED | with_skill 仅完成了向 devops-agent 的下一步路由，并明确 devops-agent 当前不可用；没有可证明后续 devops-agent:deployment-planner → devops-agent:cicd-bootstrap → devops-agent:env-config-auditor → docs-agent:formal-docs-sync 已执行或完成的锁定证据。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f6c9996daf9a7bdf78228fb674eccb457f386d1e74abf9925ac4646e4da1c9d4; fixture_sha256=16e3b6cbbbae6769ac6b5ead7bae34214b3dd90e3e6c4d5fad97cfd7d3784013; output_sha256=fa32d5b3b29e90ebfbc36a77af39181348c9e9d3c2712eddc98e7391f26456e4; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别受限状态并生成 deployment handoff packet，完成首个 DevOps 路由；后续有序链未执行。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f6c9996daf9a7bdf78228fb674eccb457f386d1e74abf9925ac4646e4da1c9d4; fixture_sha256=16e3b6cbbbae6769ac6b5ead7bae34214b3dd90e3e6c4d5fad97cfd7d3784013; output_sha256=1f43be5befe6e77636122d2a67734006eedf7bae3d6a120fac343acfaf98daaa; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 给出有依据的部署前建议并识别 CI/Helm 不完整，但未生成标准 deployment packet，也未执行规定的角色路由链。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 在 devops-agent 可用且获得后续确认后，继续执行规定的 DevOps 顺序链；仅在运维事实落地并验证后进行 Docs 同步。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
