# Eval Result: eval-001-route-auth-release-risk

## Evaluation Target

- Agent: `security`
- Skill: `security-agent`
- Eval: `eval-001-route-auth-release-risk`
- Test case: route-auth-release-risk
- Workspace: `workspace/eval-1-route-auth-release-risk`
- Review context: issue #140 为 `eval-001` 补齐 PM handoff packet fixture 后的 routing 复验
- Latest result: PASS（5/5 assertions PASS）- fresh subagent validation completed on 2026-07-20

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: auth-centered release security request with dependency-risk concern，本轮新增已确认 PM handoff 场景（`PM_HANDOFF.md` cross-role security packet + 正式源文档 `docs/pm/auth-model/PRD.md`）；fixture 由 codex 按主流程规格实施，主流程独立复核
- Prompt: 前置「pm-agent 已完成入口分类并附 PM handoff packet 路由」入口前提，保留用户原始诉求（登录与权限模型重构上线、admin 越权、依赖漏洞、先路由不写修复）
- Fresh run: 两个互相隔离的 fresh general-purpose subagent，`with_skill` 与 `without_skill` 均本轮重新生成，未复用历史 baseline
- Source head: 基于 `origin/main` `9fcdbb4`（#134 已 squash 合并）新起 `test/issue-140-security-eval-pm-handoff` 分支；本轮仅改动 `eval-001` fixture、prompt 与 metadata，未触碰 `security-agent` skill 行为或 #134 契约
- Validation date: 2026-07-20

## Assertions

- PASS `routes_primary_to_authz`: 登录、角色、admin 越权明确路由到 `authz-reviewer` 作为当前主 route，命中 routing signal 并说明为何不触发 `appsec-checklist` 兜底。
- PASS `names_dependency_followup`: 依赖漏洞作为 `dependency-risk-auditor` 后续 route 单列（`authz-reviewer` → `dependency-risk-auditor`），未忽略或混入权限审查。
- PASS `collects_security_context`: 完整列出下游需读取的认证流程（session token、角色 claim 校验、敏感操作二次校验）、角色权限矩阵（guest/member/admin/platform-ops 边界）、三条敏感路由、越权/过期会话测试证据与 `package.json` 依赖清单。fixture 补齐 PM handoff 后入口 gate 通过、不再退回 PM，本条从历史 PARTIAL 恢复为 PASS。
- PASS `structured_risk_output`: 预期产物声明为结构化认证/授权与依赖风险报告（风险矩阵、证据、影响、修复建议），归档 `docs/security/auth-model/`，而非实现补丁。
- PASS `hands_off_remediation`: 代码/鉴权逻辑修复交 `engineer-agent`，依赖/构建/部署配置修复交 `devops-agent`，Security 停在证据与风险判断。

## With Skill Behavior

fresh candidate 读取 `security-agent/SKILL.md`、Security README、`skill-map.md` 与 workspace fixture。PM Handoff Entry Gate 因 `PM_HANDOFF.md`（`request_type: security`、`change_tier: standard`、`feature_path: auth-model`、已确认 `source_documents`）齐备而通过，直接进行安全路由而非退回 `pm-agent`。它以 `authz-reviewer` 为主 route、`dependency-risk-auditor` 为后续 route，完整展开下游安全上下文清单，将 remediation 交回 `engineer-agent` / `devops-agent`，并把 Security→Docs 交接正确表述为条件路径（当前仅完成路由、无审查结论，故不触发）。

## Without Skill Baseline

fresh `without_skill` 于 2026-07-20 生成，仅读取 prompt 与场景事实 fixture（含 `PM_HANDOFF.md`、`docs/pm/auth-model/PRD.md`），显式不读取 skill 文档、Agent README、`skill-map.md` 或历史 `comparison.md`。baseline 能给出合理的双通道优先级划分（认证授权越权为上线阻断级、依赖扫描并行），并标出 `express: "latest"` 浮动版本的可复现构建风险。但 baseline **未命名 canonical specialist route**（以「通道1/通道2」泛指，而非 `authz-reviewer` / `dependency-risk-auditor`），无 PM Handoff Entry Gate 判定语义、无 Security→Docs 条件式 closeout 规则。诚实披露：baseline 因读取新增 `PM_HANDOFF.md` fixture 而借到了 `engineer-agent` / `devops-agent` handoff 与 `docs/security/auth-model/` 报告路径线索，故这两点上 with/without 差异被缩小；核心差异（canonical specialist routing 与入口 gate 语义）仍仅 with_skill 具备。

## Regression（Security→Docs 契约影响）

Regression PASS。补齐 handoff fixture 未改变 routing 语义：主 route（`authz-reviewer`）、依赖后续（`dependency-risk-auditor`）、remediation handoff 边界均保持，Docs 交接仍为条件路径，未形成无条件新链路或平行 owner map。#134 的 Security→Docs 契约未被本轮改动。

## Failures

无。历史（issue #134 复验）的 `collects_security_context` FAIL 根因是 fixture 缺 PM handoff 场景、触发 PM Handoff Entry Gate 退回 PM；issue #140 补齐已确认 PM handoff packet 与正式源文档后，该 assertion 恢复 PASS，整体 5/5。未改动 PM Handoff Entry Gate 行为、未放宽 `collects_security_context` 语义、未改动 #134 契约。

## Next Steps

- 无阻塞项。fixture 场景与 `collects_security_context` assertion 语义已对齐，复验稳定 5/5。
- Security→Docs 契约的跨 specialist 边界完善（entry basis、readiness-only 路由、direct specialist 挂载、remediation 回流）见 issue #141，独立跟进。
- 不从本 eval 自动执行 routed specialists；`authz-reviewer` / `dependency-risk-auditor` 的执行需正常下游门禁与用户确认。

## Runtime Artifacts Policy

- 运行期证据（candidate、baseline、judge verdict、transcript）仅保留在 session scratchpad，不提交到 git。
- Runtime transcripts、verdicts、timing、output 目录、diagnostics 与生成的 with_skill / without_skill 文件均不得提交。
