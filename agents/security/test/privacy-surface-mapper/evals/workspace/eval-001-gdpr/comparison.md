# Eval Result: eval-001-gdpr

## Evaluation Target

- Agent: `security`
- Skill: `privacy-surface-mapper`
- Eval: `eval-001-gdpr`
- Test case: GDPR Compliance Check
- Workspace: `workspace/eval-001-gdpr`
- Review context: issue #143
- Latest result: PASS（4/4 assertions）- fresh Codex paired validation completed on 2026-07-21

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt/fixture: issue #143 当前 fixture；包含 `PM_HANDOFF.md`、`docs/pm/data-collection/PRD.md`、`src/registration.js` 与 `config/analytics.json`
- Fresh run: 当前会话中新启动的 fresh Codex validator 在 `tmp/eval-runs/issue-143/batch-c/eval-001-gdpr/` 的隔离副本中成对运行；with-skill 读取当前 specialist SKILL.md、Security README 与共享 closeout 契约，without-skill 仅以同一 prompt/fixture 重新生成 baseline，未读取历史 comparison，未复用历史 baseline
- Source head: `test/issue-143-security-thin-fixtures`
- Validation date: 2026-07-21

## Assertions

- PASS `data_inventory`：逐字段识别注册库存储的姓名、邮箱、注册 IP、User-Agent，以及发送给 ExampleAnalytics 的 userId、邮箱、IP 和 `account_created` 事件，并关联账号创建和产品分析目的
- PASS `sharing_and_retention`：识别 ExampleAnalytics 第三方共享、默认启用、无需同意、保留期限为空，以及数据库/供应商地域、传输、删除传播和保留未证实等风险
- PASS `user_rights`：检查访问、导出/可携带、删除、更正、撤回同意及第三方传播，明确 fixture 中均无实现证据
- PASS `compliance_gaps`：给出同意或合法基础、数据最小化/假名化、保留删除、处理者与跨境信息、全链路用户权利等分级整改建议

## With Skill Behavior

with-skill 输出验证了 PM handoff 和 `feature_path=data-collection`，将代码中的收集/存储入口与配置中的第三方共享逐字段串联，并显式区分已确认事实与地域、合同、传输和删除支持等未知项。报告同时覆盖处理目的、合法基础缺口、保留、用户权利、优先级建议、`docs/security/data-collection/privacy-map.md` 落点及 Engineer/DevOps/PM 协作边界。

## Without Skill Baseline

本轮 baseline 在独立 `without_skill` 副本中，仅依据同一 prompt 与 fixture 新生成。它同样识别数据字段、ExampleAnalytics 共享、默认无同意、无保留期、用户权利缺失及主要整改项，4/4 assertions 均满足；但结构更简略，未说明 Security 报告落点、证据置信边界和跨角色 closeout。

## Failures

- with-skill 与 without-skill 均无 assertion failure。
- 对照显示该 fixture 本身信号较强；skill 的增益主要体现在证据结构、未知项标注、职责边界和可持久化报告形态。

## Next Steps

- 本 eval 无需修改 assertions 或 expected_output；后续 fixture 或 skill 行为变化时继续执行新的 fresh Codex paired run，并重新生成 baseline。

## Runtime Artifacts Policy

- 本轮 paired 输出与临时隔离副本仅用于判定，完成后删除 `tmp/eval-runs/issue-143/batch-c`。
- 不提交 with_skill、without_skill、transcript、verdict、timing、output、diagnostics 或其他运行期产物；durable result 仅为本 `comparison.md`。
