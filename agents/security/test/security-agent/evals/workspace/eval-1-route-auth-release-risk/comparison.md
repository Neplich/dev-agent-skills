# Eval Result: eval-001-route-auth-release-risk

## Evaluation Target

- Agent: `security`
- Skill: `security-agent`
- Eval: `eval-001-route-auth-release-risk`
- Test case: route-auth-release-risk
- Workspace: `workspace/eval-1-route-auth-release-risk`
- Review context: issue #196 L2-4 router 单表收敛后的全量复验
- Validation date: 2026-07-31

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt/fixture: 与当前 `evals.json`、`PM_HANDOFF.md`、`docs/pm/auth-model/PRD.md`、`docs/security/auth-model.md`、`package.json` 一致。
- with_skill source: fresh Codex candidate；完整读取并应用当前 `agents/security/README.md` 与 `agents/security/skills/security-agent/SKILL.md` 后，仅读取本 eval fixture。
- without_skill source: 同一 prompt 与独立 fixture copy 的 fresh Codex baseline；未读取或应用 Security README、security-agent skill、with_skill、旧 comparison 或 judge，未复用历史 baseline。
- Runner: Codex CLI 0.144.6，`gpt-5.6-sol`。
- Runtime root: `tmp/eval-runs/issue-196-l2-3-4/security-agent/eval-001-route-auth-release-risk/`。

## Latest Result

- Behavior result: **FAIL**（4/6 assertions PASS）
- Coverage result: **FULL**（6/6 assertions 均被当前场景触发并完成判定）
- Overall result: FAIL

## Assertions

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_primary_to_authz` | PASS | with_skill 明确选择 `security-agent:authz-reviewer` 为主审，并以登录、session、角色权限、admin 越权和敏感路由为证据。 |
| `names_dependency_followup` | PASS | with_skill 明确将 `security-agent:dependency-risk-auditor` 作为第二顺序的后续专项，未混入权限审查。 |
| `collects_security_context` | FAIL | with_skill 提及登录/session、角色权限、敏感路由和 `package.json`，但没有明确声明下游必须读取完整的认证流程、角色权限矩阵、敏感路由、测试证据和依赖清单；尤其未形成断言要求的完整上下文输入清单。 |
| `structured_risk_output` | PASS | with_skill 要求结构化风险报告，记录风险等级、证据、影响和修复建议，并明确不输出代码或配置补丁。 |
| `hands_off_remediation` | PASS | with_skill 将应用鉴权整改交 `engineer-agent`，依赖、构建或部署整改交 `devops-agent`。 |
| `evaluates_escalation_to_pm_at_closeout` | FAIL | with_skill 说明安全结论改变发版就绪状态或正式产品事实时回 `pm-agent`，也说明当前尚未执行审查；但没有明确把 closeout 判定锚定为 Security 自有的确认结论，也没有明确声明不得直交 `docs-agent`、不得由 Security 自行创建 issue，未满足该复合断言。 |

## With Skill Behavior

with_skill 通过 PM handoff 入口门禁，保留 `auth-model` feature scope，并正确使用当前单张 Default Routes 表中的语义信号完成路由；本场景不要求也未生成独立 Routing Signals 列表。它把 admin 越权审查精确路由到 `authz-reviewer`，把依赖漏洞保留为 `dependency-risk-auditor` 后续，给出 `docs/security/auth-model/` 下的两份预期报告路径，并保持“安全报告而非实现补丁”的职责边界。

不足在于：候选没有完整枚举下游所需的五类安全上下文，也没有完整陈述 closeout 的 Security 自有确认结论触发条件与禁止路径。因此本轮属于真实行为回归/遗漏，不因 router 单表改造而放宽。

## Without Skill Baseline

fresh baseline 能直接从 PM handoff 与 PRD 推断两段审查顺序：先认证/授权，再依赖供应链；还较完整地列出 session、角色矩阵、敏感路由、测试证据、依赖树、结构化风险报告和 Engineer/DevOps 整改归属。其主要缺口是没有命名 canonical `authz-reviewer` / `dependency-risk-auditor`，没有 Security router 的入口、归档和 closeout 契约。

with_skill 相比 baseline 在 specialist 精确命名、报告路径和 PM 升级方向上更明确；baseline 在一般安全上下文展开上反而更完整。该差异不足以抵消 with_skill 的两项断言失败。

## Failures

- `collects_security_context`：缺少断言要求的完整下游输入清单，尤其没有明确包含认证流程、角色权限矩阵、敏感路由、测试证据和依赖清单五项。
- `evaluates_escalation_to_pm_at_closeout`：未完整说明 closeout 针对 Security 自有确认结论；未明确禁止证据直交 `docs-agent` 和 Security 自行创建 issue。

## Next Steps

- 后续修订候选输出协议时，确保路由结论显式保留完整安全上下文输入清单。
- closeout 表述需完整覆盖 Security 自有确认结论、路由阶段无结论不升级、回 PM 分类/建 issue，以及不直交 Docs、不由 Security 自建 issue。
- 本轮不改 skill 文档或 eval 断言；仅如实记录 issue #196 全量重跑结果。

## Runtime Artifacts Policy

- 本轮 candidate、fresh baseline、prompt、fixture copy 与 judge 仅位于 `tmp/eval-runs/issue-196-l2-3-4/security-agent/eval-001-route-auth-release-risk/`，不提交到 git。
- 提交范围仅包含 canonical `comparison.md`；不提交 with_skill / without_skill、transcript、verdict、timing、diagnostics 或其他运行期文件。
