# Eval Result: eval-003-third-party

## Evaluation Target

- Agent: `security`
- Skill: `privacy-surface-mapper`
- Eval: `eval-003-third-party`
- Test case: Third-Party Data Sharing
- Workspace: `workspace/eval-003-third-party`
- Review context: issue #143
- Latest result: PASS（4/4 assertions）- fresh Codex paired validation completed on 2026-07-21

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt/fixture: issue #143 当前 fixture；包含 `PM_HANDOFF.md`、`docs/pm/third-party-sharing/PRD.md`、`src/integrations/user-events.js` 与 `config/vendors.json`
- Fresh run: 当前会话中新启动的 fresh Codex validator 在 `tmp/eval-runs/issue-143/batch-c/eval-003-third-party/` 的隔离副本中成对运行；with-skill 读取当前 specialist SKILL.md、Security README 与共享 closeout 契约，without-skill 仅以同一 prompt/fixture 重新生成 baseline，未读取历史 comparison，未复用历史 baseline
- Source head: `test/issue-143-security-thin-fixtures`
- Validation date: 2026-07-21

## Assertions

- PASS `data_inventory`：逐供应商识别 ExampleAnalytics 的 userId/邮箱/IP/pageUrl、ExampleAds 的邮箱/最近购买金额、ExamplePay 的支付客户 ID/邮箱/内部用户 ID，并关联分析、广告受众和支付客户同步目的
- PASS `sharing_and_retention`：核对美国地域、730/2555 天保留、广告保留为空、分析删除 API 缺失、广告删除支持未知和支付删除 API 可用但未编排等第三方风险
- PASS `user_rights`：检查访问、导出、更正、删除和同意传播；明确分析无法通过 API 删除、广告未知、支付仅有能力但未接入工作流，且所有供应商均无完整权利传播证据
- PASS `compliance_gaps`：给出广告默认无同意、合法基础/跨境保障、字段最小化、长或未定义保留、供应商清单和可测试权利传播等分级整改建议

## With Skill Behavior

with-skill 输出将代码发送字段与供应商配置逐一交叉核对，形成供应商、字段、目的、地域、保留、删除能力和用户权利的完整映射。它识别了无条件调用与广告默认启用/无需同意，区分 `deletionApi=true` 和“删除流程已实现”，并对未知地域、保留和删除支持保持证据边界。输出也遵守 `docs/security/third-party-sharing/privacy-map.md` 报告落点与 Engineer/DevOps/PM handoff。

## Without Skill Baseline

本轮 baseline 在独立 `without_skill` 副本中，仅依据同一 prompt 与 fixture 新生成。它同样枚举三个供应商及精确字段，覆盖目的、地域、保留、同意、删除/用户权利和整改建议，4/4 assertions 均满足；但未形成正式的数据流/权利矩阵，也缺少报告归档和跨角色 closeout。

## Failures

- with-skill 与 without-skill 均无 assertion failure。
- 对照 fixture 信息明确，baseline 已能覆盖核心风险；skill 的增益主要体现在交叉核证、未知项边界、结构化报告和职责闭环。

## Next Steps

- 本 eval 无需修改 assertions 或 expected_output；后续 fixture 或 skill 行为变化时继续执行新的 fresh Codex paired run，并重新生成 baseline。

## Runtime Artifacts Policy

- 本轮 paired 输出与临时隔离副本仅用于判定，完成后删除 `tmp/eval-runs/issue-143/batch-c`。
- 不提交 with_skill、without_skill、transcript、verdict、timing、output、diagnostics 或其他运行期产物；durable result 仅为本 `comparison.md`。
