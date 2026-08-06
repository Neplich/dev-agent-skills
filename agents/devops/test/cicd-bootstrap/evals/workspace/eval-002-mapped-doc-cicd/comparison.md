# Eval Result: eval-002-mapped-doc-cicd

## Evaluation Target

- Agent: `devops`
- Skill: `cicd-bootstrap`
- Eval: `eval-002-mapped-doc-cicd`
- Test case: `mapped-doc-cicd`
- Workspace: `agents/devops/test/cicd-bootstrap/evals/workspace/eval-002-mapped-doc-cicd`

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
- Eval definition: `agents/devops/test/cicd-bootstrap/evals/evals.json`
- Metadata: `agents/devops/test/cicd-bootstrap/evals/workspace/eval-002-mapped-doc-cicd/eval_metadata.json`
- Expected output: 以代码配置确认校验命令的 CI 建议，并报告映射文档与代码差异。
- Fixture: `src/build/pipeline.rules`, `docs/site/standards/change-map.yaml`, `docs/site/api/build-pipeline.md`

## Assertion Results

| Assertion | with_skill | without_skill | Evidence |
| --- | --- | --- | --- |
| `reads_mapped_docs_first` | FAIL | FAIL | 两条 lane 都先读取 src/build/pipeline.rules，之后才读取 change-map 和 required doc，未满足 change-map → required doc → 回代码核验的要求。 |
| `verifies_against_code` | FAIL | FAIL | 两条 lane 最终均使用 verify 并识别文档中的 test 不一致；但未说明错误命令 test 对流水线的影响。with_skill 后续 rg 可视为再次核验代码，但合取要求仍因缺少影响说明而失败。 |
| `treats_unverified_as_low_trust` | FAIL | FAIL | 两条 lane 都读取到 last_verified_version: unverified，但没有明确将文档视为低信任，也没有证明所有关键 CI 步骤均由代码或测试配置核证。 |

## With-Skill Behavior

- with_skill 的三个合取断言均未完整满足，因此 with_skill_behavior 为 FAIL；所有断言均可评估，Coverage 为 FULL。without_skill 仅作对照，其 FAIL 不改变 durable Overall。
- Workspace changes: added: `.github/workflows/ci.yml`；modified: `docs/site/api/build-pipeline.md`。

## Fresh Without-Skill Baseline

- baseline 在本轮重新生成，没有复用历史 baseline，也没有读取 target skill、with_skill 产物或旧 comparison。
- Workspace changes: added: `.github/workflows/validation.yml`；modified: `docs/site/api/build-pipeline.md`。
- assertion 结果见上表；baseline 只用于比较 skill 增益，不作为 durable Overall 的独立机器门禁。

## Failures and Coverage Gaps

- with_skill failures: `reads_mapped_docs_first`, `verifies_against_code`, `treats_unverified_as_low_trust`。
- 所有当前 assertions 均已实际覆盖。
- 无模型、认证、runner 或外部服务 blocker。

## Historical Result (Old Contract)

- 旧结论为 PASS；issue #234 修复 eval 泄漏后，该结论被标为 BLOCKED 等待重跑。
- 该历史结论适用旧 eval 契约；本文件顶部的 2026-08-07 fresh 结果已取代它作为 latest durable 结论。

## Next Steps

- 按上表 with_skill failure 的共同根因建立后续修复项；本轮只记录结果，不修改 skill、eval 定义或 fixture。

## Runtime Artifact Policy

- 两条 lane、工具轨迹、状态、文件快照、judge verdict 与隔离事件只保存在 `tmp/eval-runs/issue-238-devops-strict-20260806/`，不提交 git。
- durable 结果只保留本 `comparison.md`。
