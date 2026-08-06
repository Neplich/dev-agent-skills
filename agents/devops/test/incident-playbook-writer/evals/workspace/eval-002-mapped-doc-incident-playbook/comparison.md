# Eval Result: eval-002-mapped-doc-incident-playbook

## Evaluation Target

- Agent: `devops`
- Skill: `incident-playbook-writer`
- Eval: `eval-002-mapped-doc-incident-playbook`
- Test case: `mapped-doc-incident-playbook`
- Workspace: `agents/devops/test/incident-playbook-writer/evals/workspace/eval-002-mapped-doc-incident-playbook`

## Latest Result

- Fresh run: `2026-08-07`（issue #238 严格隔离重跑）
- Model: `gpt-5.6-luna`，`model_reasoning_effort=medium`
- Isolation: baseline 使用随机顶层 root；完成后仅保存在内存快照并删除 root，随后才创建 with_skill root；with_skill root 删除后才创建独立 judge root。两条 lane 的原始 prompt、fixture snapshot、`HOME` 与 `CODEX_HOME` 值相同。
- Judge: 独立 fresh `codex exec`，读取实际产物、final、status 与工具轨迹，对照当前 assertions 判定；不采信 lane 自评。
- Behavior result: FAIL
- Coverage result: PARTIAL
- Without-skill comparison: FAIL（仅作对照，不参与 durable Overall 组合）

Overall result: FAIL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Eval definition: `agents/devops/test/incident-playbook-writer/evals/evals.json`
- Metadata: `agents/devops/test/incident-playbook-writer/evals/workspace/eval-002-mapped-doc-incident-playbook/eval_metadata.json`
- Expected output: 以代码事实确定告警阈值的故障处置步骤，并记录映射文档差异。
- Fixture: `src/runtime/health.rules`, `docs/site/standards/change-map.yaml`, `docs/site/api/runtime-health.md`

## Assertion Results

| Assertion | with_skill | without_skill | Evidence |
| --- | --- | --- | --- |
| `reads_mapped_docs_first` | FAIL | FAIL | with_skill 先读取 change-map、代码，再读取 runtime-health.md；without_skill 先读取 health.rules，再读取文档，均未优先读取 required doc。 |
| `verifies_against_code` | FAIL | FAIL | 两条 lane 都确认代码阈值为 5、文档值为 3；但 with_skill 未说明阈值差异对处置时机的影响，也未产出处置手册。without_skill 同样未明确说明 5 相对 3 会使告警晚两个连续失败触发。 |
| `treats_unverified_as_low_trust` | NOT_EXERCISED | FAIL | with_skill 因缺少 PM/DevOps 交接上下文和 playbook 选择而未进入写入关键告警/回滚步骤的分支，fixture 前提不足，故不判定该断言。without_skill 虽核对了代码，但生成的回滚步骤没有代码或测试证据支撑，也未明确按 unverified 最低信任处理。 |

## With-Skill Behavior

- with_skill 正确识别了代码阈值 5 与文档阈值 3 的冲突，并因缺少必要上下文而阻止写入；但读取顺序不符合断言，且未说明阈值差异对处置时机的影响。覆盖度因关键步骤分支未触发而为 PARTIAL。without_skill 作为对照也未满足读取顺序和最低信任要求。
- Workspace changes: 无文件变更。

## Fresh Without-Skill Baseline

- baseline 在本轮重新生成，没有复用历史 baseline，也没有读取 target skill、with_skill 产物或旧 comparison。
- Workspace changes: modified: `docs/site/api/runtime-health.md`。
- assertion 结果见上表；baseline 只用于比较 skill 增益，不作为 durable Overall 的独立机器门禁。

## Failures and Coverage Gaps

- with_skill failures: `reads_mapped_docs_first`, `verifies_against_code`。
- NOT EXERCISED: `treats_unverified_as_low_trust`；fixture 未触发对应条件分支。
- 无模型、认证、runner 或外部服务 blocker。

## Historical Result (Old Contract)

- 旧结论为 PASS（3/3）；issue #234 修复 eval 泄漏后，该结论被标为 BLOCKED 等待重跑。
- 该历史结论适用旧 eval 契约；本文件顶部的 2026-08-07 fresh 结果已取代它作为 latest durable 结论。

## Next Steps

- 按上表 with_skill failure 的共同根因建立后续修复项；本轮只记录结果，不修改 skill、eval 定义或 fixture。

## Runtime Artifact Policy

- 两条 lane、工具轨迹、状态、文件快照、judge verdict 与隔离事件只保存在 `tmp/eval-runs/issue-238-devops-strict-20260806/`，不提交 git。
- durable 结果只保留本 `comparison.md`。
