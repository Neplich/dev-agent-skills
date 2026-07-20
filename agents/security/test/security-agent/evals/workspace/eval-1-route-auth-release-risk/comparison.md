# Eval Result: eval-001-route-auth-release-risk

## Evaluation Target

- Agent: `security`
- Skill: `security-agent`
- Eval: `eval-001-route-auth-release-risk`
- Test case: route-auth-release-risk
- Workspace: `workspace/eval-1-route-auth-release-risk`
- Review context: issue #134 为 `security-agent/SKILL.md` 新增 Security→Docs 收尾指针后的 routing 复验
- Latest result: PARTIAL（4/5 assertions PASS）- fresh Codex subagent validation completed on 2026-07-20

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: auth-centered release security request with dependency-risk concern（fixture 未变化）
- Prompt: login and permission-model refactor is preparing for release; the user primarily worries about admin authorization bypass and also wants dependency vulnerability routing.
- Fresh run: 仓库外隔离 scratch Git 仓库（session scratchpad），fresh `with_skill` 与 fresh `without_skill` 均本轮重新生成，未复用历史 baseline。
- Source head: `8d5700c`（issue #134 分支最小声明版收敛提交）。fresh routing 复验基于 #134 分支的 `security-agent`；其 routing 逻辑（specialist 选择、依赖后续、remediation handoff）在本 PR 全程未变，仅 Security→Docs closeout 指针 bullet 的措辞在后续 commit 精修、不影响 routing assertions，故 Regression 结论对 `8d5700c` 有效
- Validation date: 2026-07-20

## Assertions

- PASS `routes_primary_to_authz`: 登录、角色、admin 越权明确路由到 `authz-reviewer` 作为当前主 route。
- PASS `names_dependency_followup`: 依赖漏洞作为 `dependency-risk-auditor` 后续 route 单列，未被忽略或混入权限审查。
- FAIL `collects_security_context`: 仅给出概括层安全上下文，未完整列出认证流程、角色权限矩阵与测试证据。根因见 Failures，属 eval fixture 缺 PM handoff 导致的入口门禁触发，非 skill 引导缺陷。
- PASS `structured_risk_output`: 预期产物声明为结构化认证/授权与依赖风险报告（含风险等级、证据、影响、修复指导），而非实现补丁。
- PASS `hands_off_remediation`: 代码/依赖修复交 `engineer-agent`，部署/运行配置修复交 `devops-agent`，Security 不代替实施。

## With Skill Behavior

fresh candidate 读取 issue #134 分支的 `security-agent/SKILL.md`、Security README 与 `skill-map.md`（含 `Security-to-Docs Evidence Handoff and Audit Rerun` 子节）。它仍以 `authz-reviewer` 为主 route、`dependency-risk-auditor` 为后续 route，将 remediation 交给 `engineer-agent` / `devops-agent`，并把 Security→Docs 交接正确表述为条件路径（仅当结论/整改改变正式文档事实、对外行为、运维事实或发版就绪时触发）。

由于 fixture 未提供 PM handoff packet 或等价确认上下文，candidate 依 `SKILL.md` 的 PM Handoff Entry Gate 退回 `pm-agent`，在保留候选路由的同时只给出概括层安全上下文。

## Without Skill Baseline

fresh `without_skill` 于 2026-07-20 在仓库外隔离 scratch Git 仓库生成，仅读取 eval prompt 与 fixture 事实，不读取 skill 文档、Agent README、历史 `comparison.md` 或任何旧 baseline。baseline 能识别 admin 越权为 P0、依赖风险为 P1，但未命名 canonical `authz-reviewer` / `dependency-risk-auditor` route，无 PM Handoff Entry Gate、报告路径、remediation handoff 或 Security→Docs 规则。independent judge 确认 baseline 无 skill 文档污染迹象。

## Regression（Security→Docs 契约影响）

Regression PASS。issue #134 新增的 Security→Docs 收尾指针未破坏原有 routing：主 route、依赖后续、remediation handoff 边界均保持，Docs 交接为条件路径，未形成无条件新链路或平行 owner map。

## Failures

- `collects_security_context` FAIL（4/5）。根因：eval fixture/prompt 缺少 PM handoff 场景（无已确认 `feature_path`、正式源文档链、要求的报告类型），`security-agent` 依 PM Handoff Entry Gate 退回 `pm-agent`，只给概括层安全上下文，未完整列出认证流程、角色权限矩阵与测试证据。两轮 fresh subagent validation 稳定复现；independent judge 判定为 fixture/prompt 场景缺陷而非 skill 引导缺陷，且与 issue #134 的 Security→Docs 改动无关（Regression PASS）。跟进见 issue #140。

## Next Steps

- 按 issue #140 为 `eval-001` workspace 补 PM handoff packet fixture（或调整 prompt/assertion 明确入口前提），使场景匹配 `collects_security_context`，期望恢复 5/5。
- Security→Docs 契约的跨 specialist 边界完善（entry basis、readiness-only 路由、direct specialist 挂载、remediation 回流）见 issue #141。
- 不从本 eval 自动执行 routed specialists；`authz-reviewer` / `dependency-risk-auditor` 的执行需正常下游门禁与用户确认。

## Runtime Artifacts Policy

- 运行期证据（candidate、baseline、judge verdict、transcript）仅保留在 session scratchpad 的隔离 scratch 仓库，不提交到 git。
- Runtime transcripts、verdicts、timing、output 目录、diagnostics 与生成的 with_skill / without_skill 文件均不得提交。
