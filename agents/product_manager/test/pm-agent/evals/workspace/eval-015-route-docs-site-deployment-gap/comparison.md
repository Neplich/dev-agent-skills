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
- Identity schema: `2`
- target_skill_sha256: `6f8f132bc1f6eba3f9eb10727126ee30960b503351486b4fb6204e20571ffb35`
- eval_definition_sha256: `8bc69d85fc3ff063d885b8a2c4d7a9ea83b6dca3de23a034dba15fb34f1ba98e`
- metadata_sha256: `e7a743e88e4c53094e4afe2903a87ebcc467ace2dc58c61ccb0a0dcf64ebf2fd`
- fixture_sha256: `16e3b6cbbbae6769ac6b5ead7bae34214b3dd90e3e6c4d5fad97cfd7d3784013`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `69f2798cad12b0dd0ca3c224e3cfd6cf611a315695684db1b07a23452b52a60e`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `f6c9996daf9a7bdf78228fb674eccb457f386d1e74abf9925ac4646e4da1c9d4`
- Repository HEAD: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `6c6b79d36b8b3a1bf132fd82bfece3cf6e7b256e3a9a58a0cdb78f4a09e26e69`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_unknown_evidence` | PASS | with_skill 输出以 entry_basis: blocked 明确当前未就绪，列出 CI/Helm 范围不一致、devops-agent 不可用及禁止发布等缺口，并明确不能直接发布。 |
| `builds_repo_wide_deployment_packet` | PASS | with_skill 输出包含 request_type: deployment；feature_path、feature、parent_feature、feature_level 均为 N/A；feature_path_evidence 为空数组；source_documents 和 blockers_risks 保留了真实材料与风险。 |
| `routes_devops_ordered_chain` | NOT_EXERCISED | with_skill 只完成了 DevOps 入口的阻塞式路由，并明确 devops-agent 未安装；锁定证据未显示后续 deployment-planner、cicd-bootstrap、env-config-auditor 或 docs-agent 阶段可执行，因此后续有序链未被行使。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f6c9996daf9a7bdf78228fb674eccb457f386d1e74abf9925ac4646e4da1c9d4; fixture_sha256=16e3b6cbbbae6769ac6b5ead7bae34214b3dd90e3e6c4d5fad97cfd7d3784013; output_sha256=b474f4d6f058d96d1c9c4e4f7c5bd5408bd309c6518db8bd93a222f15f03d7db; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 生成了阻塞状态的 repo-wide deployment handoff，保留证据并停止在不可用的 DevOps 入口。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f6c9996daf9a7bdf78228fb674eccb457f386d1e74abf9925ac4646e4da1c9d4; fixture_sha256=16e3b6cbbbae6769ac6b5ead7bae34214b3dd90e3e6c4d5fad97cfd7d3784013; output_sha256=d361e4b930d606622bd17bd4ebf54c30925212426af68286bdfba20cfdcb031e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提供了基于材料的范围建议，但未生成结构化 deployment handoff，也未形成下游有序路由链。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 安装或提供 devops-agent 后继续执行 deployment-planner → cicd-bootstrap → env-config-auditor → formal-docs-sync。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
