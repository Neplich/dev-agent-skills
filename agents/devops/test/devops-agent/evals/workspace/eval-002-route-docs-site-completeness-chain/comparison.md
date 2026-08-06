# Eval Result: eval-002-route-docs-site-completeness-chain

## Evaluation Target

- Agent: `devops`
- Skill: `devops-agent`
- Eval: `eval-002-route-docs-site-completeness-chain`
- Test case: `route-docs-site-completeness-chain`
- Workspace: `agents/devops/test/devops-agent/evals/workspace/eval-002-route-docs-site-completeness-chain`

## Latest Result

- Fresh run: `2026-08-07`（issue #238 严格隔离重跑）
- Model: `gpt-5.6-luna`，`model_reasoning_effort=medium`
- Isolation: baseline 使用随机顶层 root；完成后仅保存在内存快照并删除 root，随后才创建 with_skill root；with_skill root 删除后才创建独立 judge root。两条 lane 的原始 prompt、fixture snapshot、`HOME` 与 `CODEX_HOME` 值相同。
- Judge: 独立 fresh `codex exec`，读取实际产物、final、status 与工具轨迹，对照当前 assertions 判定；不采信 lane 自评。
- Behavior result: PASS
- Coverage result: FULL
- Without-skill comparison: FAIL（仅作对照，不参与 durable Overall 组合）

Overall result: PASS

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Eval definition: `agents/devops/test/devops-agent/evals/evals.json`
- Metadata: `agents/devops/test/devops-agent/evals/workspace/eval-002-route-docs-site-completeness-chain/eval_metadata.json`
- Expected output: 按 deployment-planner 到 cicd-bootstrap 到 env-config-auditor 再回 formal-docs-sync 的顺序路由。
- Fixture: `pm-handoff.md`

## Assertion Results

| Assertion | with_skill | without_skill | Evidence |
| --- | --- | --- | --- |
| `accepts_repo_wide_docs_handoff` | PASS | PASS | with_skill 接受 deployment、feature_path=N/A 的 repo-wide handoff，未退回 feature_path 澄清；without_skill 也未退回澄清。 |
| `routes_dependency_order` | PASS | FAIL | with_skill-final 明确给出 deployment-planner → cicd-bootstrap → env-config-auditor → docs-agent:formal-docs-sync；without_skill-final 未给出该依赖顺序。 |
| `preserves_role_and_authority_boundaries` | PASS | PASS | with_skill-final 明确未修改文件并停止于不可验证资产，未执行部署或文档修改；符合 fixture 中未预授权交付的边界。 |

## With-Skill Behavior

- with_skill 三项断言均满足，Coverage 为 FULL，因此 durable Overall 为 PASS。without_skill 缺少所要求的依赖顺序，判为 baseline FAIL；不影响 durable Overall。
- Workspace changes: 无文件变更。

## Fresh Without-Skill Baseline

- baseline 在本轮重新生成，没有复用历史 baseline，也没有读取 target skill、with_skill 产物或旧 comparison。
- Workspace changes: 无文件变更。
- assertion 结果见上表；baseline 只用于比较 skill 增益，不作为 durable Overall 的独立机器门禁。

## Failures and Coverage Gaps

- with_skill 无 assertion failure。
- 所有当前 assertions 均已实际覆盖。
- 无模型、认证、runner 或外部服务 blocker。

## Historical Result (Old Contract)

- 旧结论为 PASS（3/3）；issue #234 修复 eval 泄漏后，该结论被标为 BLOCKED 等待重跑。
- 该历史结论适用旧 eval 契约；本文件顶部的 2026-08-07 fresh 结果已取代它作为 latest durable 结论。

## Next Steps

- 保留当前回归用例；后续 skill、fixture 或断言变化时继续执行同等严格的 fresh paired run。

## Runtime Artifact Policy

- 两条 lane、工具轨迹、状态、文件快照、judge verdict 与隔离事件只保存在 `tmp/eval-runs/issue-238-devops-strict-20260806/`，不提交 git。
- durable 结果只保留本 `comparison.md`。
