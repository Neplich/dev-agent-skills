# Eval Result: eval-003-mapped-doc-deployment

## Evaluation Target

- Agent: `devops`
- Skill: `deployment-planner`
- Eval: `eval-003-mapped-doc-deployment`
- Test case: `mapped-doc-deployment`
- Workspace: `agents/devops/test/deployment-planner/evals/workspace/eval-003-mapped-doc-deployment`

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
- Metadata: `agents/devops/test/deployment-planner/evals/workspace/eval-003-mapped-doc-deployment/eval_metadata.json`
- Expected output: 基于映射文档定位、以代码配置确认端口的部署建议和文档差异记录。
- Fixture: `src/runtime/server.conf`, `docs/site/standards/change-map.yaml`, `docs/site/api/runtime-server.md`

## Assertion Results

| Assertion | with_skill | without_skill | Evidence |
| --- | --- | --- | --- |
| `reads_mapped_docs_first` | FAIL | FAIL | with_skill 首个执行命令只读取 skill 与 server.conf，未先读取 change-map 命中的 docs/site/api/runtime-server.md；without_skill 先读 server.conf，之后才读取文档，并进行了无关文件遍历。 |
| `verifies_against_code` | PASS | PASS | 两条 lane 均读取 src/runtime/server.conf，确认 8081；with_skill final 明确指出文档 8080 与代码 8081 不一致，并按 8081 给出容器发布建议。 |
| `treats_unverified_as_low_trust` | PASS | PASS | 关键端口以 src/runtime/server.conf 的 8081 为准，而非盲用文档中的 8080；两条 lane 均识别并处理了该差异。 |
| `omits_unselected_targets` | PASS | PASS | with_skill 仅给出容器化建议，未生成 deploy/local 或 deploy/helm 资产；status 显示无文件变更。without_skill 也未生成这些未选择目标。 |

## With-Skill Behavior

- with_skill 覆盖全部断言，但未遵守命中文档优先读取顺序，因此 durable Overall 为 FAIL。without_skill 仅作对照，亦因读取顺序不符合断言而判 FAIL。
- Workspace changes: 无文件变更。

## Fresh Without-Skill Baseline

- baseline 在本轮重新生成，没有复用历史 baseline，也没有读取 target skill、with_skill 产物或旧 comparison。
- Workspace changes: modified: `docs/site/api/runtime-server.md`。
- assertion 结果见上表；baseline 只用于比较 skill 增益，不作为 durable Overall 的独立机器门禁。

## Failures and Coverage Gaps

- with_skill failures: `reads_mapped_docs_first`。
- 所有当前 assertions 均已实际覆盖。
- 无模型、认证、runner 或外部服务 blocker。

## Historical Result (Old Contract)

- 旧结论为 PASS（4/4）；issue #234 修复 eval 泄漏后，该结论被标为 BLOCKED 等待重跑。
- 该历史结论适用旧 eval 契约；本文件顶部的 2026-08-07 fresh 结果已取代它作为 latest durable 结论。

## Next Steps

- 按上表 with_skill failure 的共同根因建立后续修复项；本轮只记录结果，不修改 skill、eval 定义或 fixture。

## Runtime Artifact Policy

- 两条 lane、工具轨迹、状态、文件快照、judge verdict 与隔离事件只保存在 `tmp/eval-runs/issue-238-devops-strict-20260806/`，不提交 git。
- durable 结果只保留本 `comparison.md`。
