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
- Repository HEAD: `b385df5d17058a52081357c8a8480fc146c3d989`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `ecf67dca8a2fd53bb0dd6d0a63750ba2716e88dc4af4f77176ea061260d64286`
- Skill overlay SHA-256: `2ed9fef9a54be8009ea156c857682ad7dd82c0e56e3463d3257fe74fe9c977ec`
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
| `blocks_unknown_evidence` | PASS | with_skill 明确标记 entry_basis: blocked，指出 devops-agent 不可用及当前证据缺口，未将状态表述为 integrated 或 ready handoff。 |
| `builds_repo_wide_deployment_packet` | PASS | with_skill 输出 request_type: deployment；feature_path、feature、parent_feature、feature_level 均为 N/A，feature_path_evidence 为空；source_documents 和 blockers_risks 保留了 CI、Helm、维护者授权及真实阻塞证据。 |
| `routes_devops_ordered_chain` | NOT_EXERCISED | with_skill 已将下一步路由至 DevOps 部署范围确认与计划，但 devops-agent 不可用，因此 cicd-bootstrap、env-config-auditor、formal-docs-sync 后续阶段未被执行或验证。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f6c9996daf9a7bdf78228fb674eccb457f386d1e74abf9925ac4646e4da1c9d4; fixture_sha256=16e3b6cbbbae6769ac6b5ead7bae34214b3dd90e3e6c4d5fad97cfd7d3784013; output_sha256=59c72735486ebdac8b0b5636f03fba1ea3004f55a95cfe83b39f81158fc74f31; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别当前 CI、Helm 和维护者授权证据，生成部署类 repo-wide handoff，并在执行边界内保持阻塞状态。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f6c9996daf9a7bdf78228fb674eccb457f386d1e74abf9925ac4646e4da1c9d4; fixture_sha256=16e3b6cbbbae6769ac6b5ead7bae34214b3dd90e3e6c4d5fad97cfd7d3784013; output_sha256=da946b928a6c6edc474f10517157b2d9f2045745bdf4d0dd4447dfbd75925bf2; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 保守识别早期检查缺口，但错误地认为当前没有 CI workflow，未生成部署 handoff。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 安装或提供 devops-agent 后继续 deployment-planner → cicd-bootstrap → env-config-auditor → formal-docs-sync 链路。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
