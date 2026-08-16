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
- target_skill_sha256: `ed93e443692bf05e76aaa38c8a5b8faff57190219ed48b9335316584424e6eb9`
- eval_definition_sha256: `8bc69d85fc3ff063d885b8a2c4d7a9ea83b6dca3de23a034dba15fb34f1ba98e`
- metadata_sha256: `7cd2581ae78239652e35a53401d899646cf1bf57925a7928ae3b61ce61b991b9`
- fixture_sha256: `16e3b6cbbbae6769ac6b5ead7bae34214b3dd90e3e6c4d5fad97cfd7d3784013`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `69f2798cad12b0dd0ca3c224e3cfd6cf611a315695684db1b07a23452b52a60e`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `f6c9996daf9a7bdf78228fb674eccb457f386d1e74abf9925ac4646e4da1c9d4`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `f0e82f7ac41a59994ff88c345ca6ca77118629bc2985dc7df715d389b37ade9e`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_unknown_evidence` | PASS | with_skill 报告部署完整性为 partial，明确缺少镜像、运行时工作负载、Service/Ingress、健康检查及访问控制证据，并列入 blockers_risks；未声称 integrated 或已完成交接。 |
| `builds_repo_wide_deployment_packet` | PASS | with_skill 输出包含 request_type: deployment、所有 feature 字段为 N/A、feature_path_evidence: []，并在 source_documents 与 blockers_risks 中保留了 access-note、CI、Helm 和维护者授权证据。 |
| `routes_devops_ordered_chain` | NOT_EXERCISED | with_skill 明确列出 deployment-planner → cicd-bootstrap → env-config-auditor → docs-agent:formal-docs-sync，并要求用户确认后继续；没有后续 DevOps 执行或已落地事实可供 Docs 同步，因此最终同步步骤未被实际行使。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f6c9996daf9a7bdf78228fb674eccb457f386d1e74abf9925ac4646e4da1c9d4; fixture_sha256=16e3b6cbbbae6769ac6b5ead7bae34214b3dd90e3e6c4d5fad97cfd7d3784013; output_sha256=64c114f531c63e3ac3fc292127cd93321378f24f2bb8beb91115aa20bccaae34; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别部署状态仅为 partial，保留未知项，生成完整的 repo-wide DevOps 交接包并提出有序后续链路。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f6c9996daf9a7bdf78228fb674eccb457f386d1e74abf9925ac4646e4da1c9d4; fixture_sha256=16e3b6cbbbae6769ac6b5ead7bae34214b3dd90e3e6c4d5fad97cfd7d3784013; output_sha256=434bdeaded6d6c4c03f3b9a0d6697ea55d8be3c92ce257fec6c90133bce9d887; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 将审查范围过早判定为已完成并直接交给文档负责人，未保留 CI/运行时证据缺口，也未生成规范化交接包。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 获得用户确认后进入 deployment-planner，并按顺序完成后续 DevOps 审计；仅将已落地且验证的运维事实交给 Docs。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
