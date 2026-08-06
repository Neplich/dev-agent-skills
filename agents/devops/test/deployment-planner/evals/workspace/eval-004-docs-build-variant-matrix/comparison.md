# Eval Result: eval-004-docs-build-variant-matrix

## Evaluation Target

- Agent: `devops`
- Skill: `deployment-planner`
- Eval: `eval-004-docs-build-variant-matrix`
- Test case: `docs-build-variant-matrix`
- Workspace: `agents/devops/test/deployment-planner/evals/workspace/eval-004-docs-build-variant-matrix`

## Latest Result

- Fresh run: `2026-08-07`（issue #238 严格隔离重跑）
- Model: `gpt-5.6-luna`，`model_reasoning_effort=medium`
- Isolation: baseline 使用随机顶层 root；完成后仅保存在内存快照并删除 root，随后才创建 with_skill root；with_skill root 删除后才创建独立 judge root。两条 lane 的原始 prompt、fixture snapshot、`HOME` 与 `CODEX_HOME` 值相同。
- Judge: 独立 fresh `codex exec`，读取实际产物、final、status 与工具轨迹，对照当前 assertions 判定；不采信 lane 自评。
- Behavior result: FAIL
- Coverage result: FULL
- Without-skill comparison: FAIL（仅作对照，不参与 durable Overall 组合）

Overall result: FAIL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Eval definition: `agents/devops/test/deployment-planner/evals/evals.json`
- Metadata: `agents/devops/test/deployment-planner/evals/workspace/eval-004-docs-build-variant-matrix/eval_metadata.json`
- Expected output: 逐一列出 Public、Internal 与 Preview 的 build/image/Compose/Helm/health/runtime 处置。
- Fixture: `evidence.md`

## Assertion Results

| Assertion | with_skill | without_skill | Evidence |
| --- | --- | --- | --- |
| `enumerates_all_docs_variants` | PASS | PASS | with_skill 矩阵明确包含 public、internal、preview；without_skill 结论也逐一覆盖三者。 |
| `covers_deployment_unit_chain` | PASS | FAIL | with_skill 为每个变体提供了 build target、context、static entry、image、Compose、Kubernetes/Helm、health check、runtime entry 列，并对缺失证据标注“未记录”；without_skill 仅列出 Docker/Compose/Helm 覆盖，没有逐变体核对完整链路。 |
| `hands_units_to_cicd` | FAIL | FAIL | with_skill 给出 integrated/deferred/blocked 处置，但未明确将每个确认的镜像单元和变体矩阵交给 cicd-bootstrap；仅泛称后续交给 CI/CD 流程。without_skill 同样未进行该 handoff。 |

## With-Skill Behavior

- with_skill 成功枚举全部变体并建立了逐变体链路矩阵，所有断言均可评估，Coverage 为 FULL；但遗漏了向 cicd-bootstrap 明确移交确认镜像单元和变体矩阵，因此 durable Overall 为 FAIL。without_skill 仅作对照，存在链路覆盖与 handoff 缺口。
- Workspace changes: added: `docs/devops/documentation-site-deployment-variant-matrix.md`。

## Fresh Without-Skill Baseline

- baseline 在本轮重新生成，没有复用历史 baseline，也没有读取 target skill、with_skill 产物或旧 comparison。
- Workspace changes: 无文件变更。
- assertion 结果见上表；baseline 只用于比较 skill 增益，不作为 durable Overall 的独立机器门禁。

## Failures and Coverage Gaps

- with_skill failures: `hands_units_to_cicd`。
- 所有当前 assertions 均已实际覆盖。
- 无模型、认证、runner 或外部服务 blocker。

## Historical Result (Old Contract)

- 旧结论为 PASS（3/3）；issue #234 修复 eval 泄漏后，该结论被标为 BLOCKED 等待重跑。
- 该历史结论适用旧 eval 契约；本文件顶部的 2026-08-07 fresh 结果已取代它作为 latest durable 结论。

## Next Steps

- 按上表 with_skill failure 的共同根因建立后续修复项；本轮只记录结果，不修改 skill、eval 定义或 fixture。

## Runtime Artifact Policy

- 两条 lane、工具轨迹、状态、文件快照、judge verdict 与隔离事件只保存在 `tmp/eval-runs/issue-238-devops-strict-20260806/`，不提交 git。
- durable 结果只保留本 `comparison.md`。
