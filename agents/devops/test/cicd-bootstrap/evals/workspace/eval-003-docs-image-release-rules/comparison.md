# Eval Result: eval-003-docs-image-release-rules

## Evaluation Target

- Agent: `devops`
- Skill: `cicd-bootstrap`
- Eval: `eval-003-docs-image-release-rules`
- Test case: `docs-image-release-rules`
- Workspace: `agents/devops/test/cicd-bootstrap/evals/workspace/eval-003-docs-image-release-rules`

## Latest Result

- Fresh run: `2026-08-07`（issue #238 严格隔离重跑）
- Model: `gpt-5.6-luna`，`model_reasoning_effort=medium`
- Isolation: baseline 使用随机顶层 root；完成后仅保存在内存快照并删除 root，随后才创建 with_skill root；with_skill root 删除后才创建独立 judge root。两条 lane 的原始 prompt、fixture snapshot、`HOME` 与 `CODEX_HOME` 值相同。
- Judge: 独立 fresh `codex exec`，读取实际产物、final、status 与工具轨迹，对照当前 assertions 判定；不采信 lane 自评。
- Behavior result: PASS
- Coverage result: PARTIAL
- Without-skill comparison: PASS（仅作对照，不参与 durable Overall 组合）

Overall result: PASS (partial coverage)

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Eval definition: `agents/devops/test/cicd-bootstrap/evals/evals.json`
- Metadata: `agents/devops/test/cicd-bootstrap/evals/workspace/eval-003-docs-image-release-rules/eval_metadata.json`
- Expected output: Public/Internal 镜像使用宿主不可变版本、架构、registry、触发器和 manifest/digest 验证。
- Fixture: `deployment-handoff.md`

## Assertion Results

| Assertion | with_skill | without_skill | Evidence |
| --- | --- | --- | --- |
| `preserves_host_image_policy` | PASS | PASS | 两条 lane 的 final 均逐一报告 Public/Internal 的不可变标签、registry、linux/amd64 与 linux/arm64、tag 触发和 digest 检查，符合 fixture。 |
| `verifies_each_published_variant` | NOT_EXERCISED | NOT_EXERCISED | fixture 与两条 lane workspace 均未提供拟议 workflow、发布结果或 digest 证据；with_skill final 正确指出无法验证实现，因此该条件分支不可评估。 |
| `keeps_delivery_authority_separate` | PASS | PASS | fixture 明确不授权 push 或 publication；两条 final 均未执行发布，并明确说明当前只能静态审查、不能据此执行 push 或发布。 |

## With-Skill Behavior

- with_skill 正确提取并报告宿主镜像规则，且识别缺少可审查 CI/CD 实现与发布证据；仅发布验证断言因 fixture 缺少前提而未 exercised，因此 Coverage 为 PARTIAL。按 binding_result_model，with_skill_behavior 为 PASS 且 Coverage 为 PARTIAL，durable Overall 为 PASS (partial coverage)。without_skill 仅作对照，结果不改变 durable Overall。
- Workspace changes: 无文件变更。

## Fresh Without-Skill Baseline

- baseline 在本轮重新生成，没有复用历史 baseline，也没有读取 target skill、with_skill 产物或旧 comparison。
- Workspace changes: 无文件变更。
- assertion 结果见上表；baseline 只用于比较 skill 增益，不作为 durable Overall 的独立机器门禁。

## Failures and Coverage Gaps

- with_skill 无 assertion failure。
- NOT EXERCISED: `verifies_each_published_variant`；fixture 未触发对应条件分支。
- 无模型、认证、runner 或外部服务 blocker。

## Historical Result (Old Contract)

- 旧结论为 PASS（3/3）；issue #234 修复 eval 泄漏后，该结论被标为 BLOCKED 等待重跑。
- 该历史结论适用旧 eval 契约；本文件顶部的 2026-08-07 fresh 结果已取代它作为 latest durable 结论。

## Next Steps

- 保留当前行为结果；若要获得 FULL coverage，需要新增能够触发 NOT EXERCISED 条件分支的独立 fixture。

## Runtime Artifact Policy

- 两条 lane、工具轨迹、状态、文件快照、judge verdict 与隔离事件只保存在 `tmp/eval-runs/issue-238-devops-strict-20260806/`，不提交 git。
- durable 结果只保留本 `comparison.md`。
