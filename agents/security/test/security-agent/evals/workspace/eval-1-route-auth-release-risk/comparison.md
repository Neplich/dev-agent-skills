# Eval Result: eval-001-route-auth-release-risk

## Evaluation Target

- Agent: `security`
- Skill: `security-agent`
- Eval: `eval-001-route-auth-release-risk`
- Test case: route-auth-release-risk
- Workspace: `workspace/eval-1-route-auth-release-risk`
- Natural user prompt:

> pm-agent 已完成入口分类，相关材料见 workspace `PM_HANDOFF.md` 与 docs/pm/auth-model/PRD.md。用户原始诉求：登录和权限模型重构准备上线，重点担心 admin 越权，同时也想知道依赖有没有漏洞。请处理这次安全审查请求。

- Expected artifact: 安全路由决策，明确 authz-reviewer 是当前主 route，dependency-risk-auditor 是后续，并保持证据型安全输出边界。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-06 23:45:35 至 2026-08-07 00:13:31（Asia/Shanghai）。
- Runtime root: `/tmp/security-fresh-evals-20260806-n3l1anp1/security-agent--eval-001-route-auth-release-risk/`。
- Fixture identity: 两条 lane 的初始 fixture manifest 完全相同，SHA-256 为 `6965ab9a6a192c2aba9c66d23afdeec69aa3d14bba3d238d07694ef892fd279e`。
- Lane isolation: 先完成并销毁全部 `without_skill` 独立顶层临时目录，再创建任何 `with_skill` 目录；每条 lane 使用独立的顶层临时 workspace、`HOME` 与 `CODEX_HOME`，不存在可供另一条 candidate 读取的 sibling lane。
- Controlled variable: 两条 lane 使用逐字相同 prompt 与相同初始 fixture；仅 `with_skill` 的隔离 `CODEX_HOME` 安装并加载目标 skill，`without_skill` 未安装任何目标 skill。
- Evidence isolation: 所有 candidate 会话结束并删除各自临时根后，才将内存中的最终 workspace 快照与 transcript 持久化到 runtime root；candidate transcript 泄漏扫描未命中 `eval_metadata.json`、`evals/evals.json`、`comparison.md`、judge/verdict 或 expected output/assertion 脚手架。
- Judge: candidate 全部结束后，由第三个独立、只读的 fresh Codex 会话依据当前 assertions、两条 candidate 输出、transcript 与最终 workspace 快照判定。

## Latest Result

- Behavior result: **FAIL**（PASS 5 / FAIL 1 / NOT EXERCISED 0）
- Coverage result: **FULL**
Overall result: FAIL

## Historical Contract Note

上一份 durable comparison 基于 issue #234 修复前会向 baseline 泄漏规则的旧契约，因此标记为 `BLOCKED`。本轮使用当前无泄漏 prompt/fixture 重新生成两条 lane，未复用旧 baseline 或旧结论。

## Assertions

| Assertion | With skill | With-skill evidence | Without skill | Baseline evidence |
| --- | --- | --- | --- | --- |
| `routes_primary_to_authz`<br>权限主 route | PASS | transcript 明确将 authz-reviewer 作为 admin、tenant、platform 边界审查主路由，最终报告也记录该路由。 | NOT EXERCISED | 仅有安全报告，没有明确选择 authz-reviewer 作为主 route 的证据。 |
| `names_dependency_followup`<br>依赖后续 route | PASS | transcript 明确将 dependency-risk-auditor 作为依赖与供应链审查链路，且与 authz 审查分开；最终报告记录两者及后续依赖修复。 | NOT EXERCISED | 报告讨论依赖风险，但没有明确 dependency-risk-auditor 后续 route 的证据。 |
| `collects_security_context`<br>安全上下文 | PASS | transcript 读取 PM_HANDOFF 和 PRD，并检查认证/授权实现、角色与租户边界、敏感路由、测试、依赖清单及扫描证据；最终报告也逐项覆盖这些范围。 | NOT EXERCISED | 报告覆盖相关风险面，但没有明确说明下游需要读取这些安全上下文。 |
| `structured_risk_output`<br>结构化风险产物 | PASS | 最终工作区存在 docs/security/auth-model/review.md，包含结论、风险矩阵、证据分析、影响、修复建议和复审门槛，未输出实现补丁。 | PASS | 最终工作区存在 SECURITY-REVIEW.md，内容包含结构化风险矩阵、证据、影响、修复建议和上线门槛。 |
| `hands_off_remediation`<br>修复 handoff | PASS | 最终报告明确将鉴权逻辑交给 engineer-agent，将依赖/构建修复交给 devops-agent。 | PASS | 最终报告明确列出 engineer-agent 与 devops-agent 的 remediation 分工。 |
| `evaluates_escalation_to_pm_at_closeout`<br>closeout 时评估结论升级 | FAIL | 已有 Security 自有的上线阻断结论并完成 closeout，但 transcript、candidate 和 review.md 都未评估 Security Conclusion Escalation to PM，也未说明不升级的条件；仅说回 Security 复审，未提及 PM、docs-agent 或禁止 Security 自行创建 issue。 | NOT EXERCISED | baseline 没有 closeout 时的 Security 结论升级评估证据。 |

## With-Skill Behavior

with-skill 正确完成 authz 主路由、依赖后续审查，并生成结构化报告；但 closeout 未按规则评估 Security 自有结论是否升级 PM。

## Fresh Without-Skill Baseline

baseline 生成了结构化安全报告并列出 remediation，但没有明确路由、下游上下文收集或 closeout 升级评估。

## Failures

- with-skill 未满足 evaluates_escalation_to_pm_at_closeout。

## Not Exercised

- without-skill 的明确主/后续路由选择
- without-skill 的下游安全上下文收集说明
- without-skill 的 closeout 升级评估

## Next Steps

- 补充 closeout：针对本次上线阻断结论明确评估是否触发 Security Conclusion Escalation to PM，并说明触发时回 PM、由 PM 进入 issue lifecycle；不直接交 docs-agent，也不由 Security 自行创建 issue。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` workspace 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
