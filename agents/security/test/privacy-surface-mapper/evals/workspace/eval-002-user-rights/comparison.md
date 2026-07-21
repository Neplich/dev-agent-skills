# Eval Result: eval-002-user-rights

## Evaluation Target

- Agent: `security`
- Skill: `privacy-surface-mapper`
- Eval: `eval-002-user-rights`
- Test case: User Rights Implementation
- Workspace: `workspace/eval-002-user-rights`
- Review context: issue #143
- Latest result: PASS（4/4 assertions）- fresh Codex paired validation completed on 2026-07-21

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt/fixture: issue #143 当前 fixture；包含 `PM_HANDOFF.md`、`docs/pm/user-rights/PRD.md` 与 `src/api/user-rights.js`
- Fresh run: 当前会话中新启动的 fresh Codex validator 在 `tmp/eval-runs/issue-143/batch-c/eval-002-user-rights/` 的隔离副本中成对运行；with-skill 读取当前 specialist SKILL.md、Security README 与共享 closeout 契约，without-skill 仅以同一 prompt/fixture 重新生成 baseline，未读取历史 comparison，未复用历史 baseline
- Source head: `test/issue-143-security-thin-fixtures`
- Validation date: 2026-07-21

## Assertions

- PASS `data_inventory`：识别资料、订单、分析事件和备份，追踪 `/me`、`/data-export` 与删除端点的处理范围和用途
- PASS `sharing_and_retention`：识别分析系统和备份中的副本，并将供应商属性、保留期限、法定保留例外、删除期限未定义列为风险，而未臆造额外第三方
- PASS `user_rights`：确认资料访问仅部分实现；导出信任 `req.query.userId` 可越权且遗漏行为数据；删除仅软删除主库且不传播到分析/备份；更正、状态和同意控制缺失
- PASS `compliance_gaps`：给出会话身份绑定、授权测试、完整安全导出、跨主库/分析/任务/备份删除编排、法定保留与审计状态等可执行整改

## With Skill Behavior

with-skill 输出以 PM handoff 与 `feature_path=user-rights` 为范围，按数据清单、存储/共享、权利实现和整改结构核对端点。它准确指出 `/data-export` 的对象级越权风险、分析数据遗漏和删除传播缺口，同时把未见证据的保留/供应商信息标为未知，不把推测当事实。输出还给出 `docs/security/user-rights/privacy-map.md` 落点以及 Engineer、DevOps 和 PM 的职责边界。

## Without Skill Baseline

本轮 baseline 在独立 `without_skill` 副本中，仅依据同一 prompt 与 fixture 新生成。它也识别资料/订单/分析/备份、导出越权、删除不完整、保留未知和整改方案，4/4 assertions 均满足；但没有完整的隐私地图结构、严重性表达、报告归档和 Security→PM closeout。

## Failures

- with-skill 与 without-skill 均无 assertion failure。
- baseline 已能利用高度显性的代码注释和 PM 风险提示；skill 的增益主要体现在完整权利矩阵、事实/未知边界和跨角色闭环。

## Next Steps

- 本 eval 无需修改 assertions 或 expected_output；后续 fixture 或 skill 行为变化时继续执行新的 fresh Codex paired run，并重新生成 baseline。

## Runtime Artifacts Policy

- 本轮 paired 输出与临时隔离副本仅用于判定，完成后删除 `tmp/eval-runs/issue-143/batch-c`。
- 不提交 with_skill、without_skill、transcript、verdict、timing、output、diagnostics 或其他运行期产物；durable result 仅为本 `comparison.md`。
