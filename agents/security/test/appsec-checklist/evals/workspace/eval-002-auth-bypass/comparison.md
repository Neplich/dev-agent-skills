# Eval Result: eval-002-auth-bypass

## Evaluation Target

- Agent: `security`
- Skill: `appsec-checklist`
- Eval: `eval-002-auth-bypass`
- Test case: Authentication Bypass
- Workspace: `workspace/eval-002-auth-bypass`
- Review context: PR #149 review 修复轮，保留 issue #143 上下文
- Latest result: PASS（4/4 assertions）- fresh paired validation completed on 2026-07-21

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt/fixture: PR #149 review 修复后的 fixture；包含 `PM_HANDOFF.md`、`docs/pm/admin-panel/PRD.md`、新增的 `src/app.js` 与既有 `src/api/admin-routes.js`
- Fixture evidence: `src/app.js:14-19` 对照展示 `/account` 使用 `requireAuthenticated`，而 `adminRouter` 通过 `app.use(adminRouter)` 无认证或授权中间件挂载；`src/api/admin-routes.js:6` 内部也直接注册处理器且没有守卫
- Fresh run: `tmp/eval-runs/issue-143-r2`；with_skill 读取当前 Security Agent README 与 `appsec-checklist`，without_skill 基于同一 prompt/fixture 在本轮重新生成，未读取或应用 skill/Agent README、历史 comparison 或 with_skill 输出
- Source head: `test/issue-143-security-thin-fixtures` (`1a91659`，fixture 修复提交前工作树)
- Validation date: 2026-07-21

## Assertions

- PASS `security_findings`：识别 `GET /admin/users` 在应用挂载点和 router 内均缺失身份认证与管理员授权，形成与场景匹配的认证/授权绕过风险
- PASS `evidence_and_impact`：引用 `src/app.js:14-19` 的受保护路由对照、`app.use(adminRouter)` 无守卫挂载及 `src/api/admin-routes.js:6`，并说明匿名或普通用户可进入管理处理器、影响用户账号资料与后续管理能力
- PASS `severity_rationale`：依据可达的无守卫挂载、PRD 的双重校验要求及 appsec-checklist 对认证绕过的分级，将风险判为 Critical，同时保留未提供 `listUsers` 实现的证据边界
- PASS `remediation`：给出挂载层 fail-closed 身份与 admin 角色守卫、401/403 行为，以及验证处理器未执行和 router 全覆盖的集成测试步骤

## With Skill Behavior

本轮候选不再从裸 router 推断挂载状态，而是使用新增 `src/app.js` 建立端到端可达证据，并用 `/account` 的显式认证形成清楚对照。输出按 Critical finding 组织位置、证据、入口、资产、影响、严重度依据、修复代码与验证矩阵；它没有把未提供的 `listUsers` 内部行为当成事实，并保持 Security 报告、Engineer 修复和 Security→PM closeout 边界。

## Without Skill Baseline

本轮 fresh baseline 同样读取新增 `src/app.js`，准确识别无守卫挂载与 router 内缺失校验，给出 High 严重度、可利用路径、影响、挂载层修复和 401/403/handler-not-called 验证，因此满足 4/4 assertions。相比 with_skill，baseline 的风险分级低于 specialist 规则中的 Critical，且未形成完整 checklist、正式 Security 报告落点和 Security→PM closeout，但这些差异不构成本 eval assertion failure。

## Failures

- with_skill 无 assertion failure。
- fresh without_skill baseline 无 assertion failure。
- 未发现基础设施阻塞；新增应用入口已补足 admin router 实际无守卫挂载的关键证据。

## Next Steps

- 当前 eval 无需修改 skill、assertions 或 fixture；后续相关行为或 fixture 再变化时，继续执行同 prompt/fixture 的 fresh paired run，并重新生成 without_skill baseline。

## Runtime Artifacts Policy

- 本轮 paired 输出和临时证据仅位于 `tmp/eval-runs/issue-143-r2`，不提交到 git。
- `with_skill/`、`without_skill/`、transcript、verdict、timing、diagnostics 及其他运行期产物均不得提交；durable 结果仅为本 `comparison.md`。
