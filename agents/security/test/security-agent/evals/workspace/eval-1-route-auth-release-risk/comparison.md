# Eval Result: eval-001-route-auth-release-risk

## Evaluation Target

- Agent: `security`
- Skill: `security-agent`
- Eval: `eval-001-route-auth-release-risk`
- Test case: route-auth-release-risk
- Workspace: `workspace/eval-1-route-auth-release-risk`
- Review context: PR #204 eval alignment fix round fresh paired validation

## Test Set / Fixture Version

- Schema: `evals.json` v1.0; current prompt and fixture
- Validation date: 2026-08-01
- with_skill source: fresh Codex validator，完整读取并应用当前 `agents/security/README.md`、`agents/security/skills/security-agent/SKILL.md` 与共享 handoff/closeout 契约后，读取独立 fixture copy。
- without_skill source: 同一原始 prompt 与另一份独立 fixture copy 的全新 Codex baseline；未读取或应用目标 README/skill，未复用旧 baseline、旧 comparison 或 with_skill 输出。
- Runtime root: `tmp/eval-runs/pr-204-fix-round-20260801/security-agent/eval-001-route-auth-release-risk/`。

## Latest Result

- Behavior result: **PASS**（6/6 assertions PASS）
- Coverage result: **FULL**（6/6 assertions 均被当前场景触发并完成判定）
- Overall result: PASS

## Assertions

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_primary_to_authz` | PASS | with_skill 明确选择 `security-agent:authz-reviewer` 为当前主 route，并以登录/session、角色权限和 admin 越权为核心风险。 |
| `names_dependency_followup` | PASS | with_skill 将 `security-agent:dependency-risk-auditor` 作为独立后续专项，未混入权限审查。 |
| `collects_security_context` | PASS | with_skill 完整列出认证流程、角色权限矩阵、敏感路由、测试证据以及 `package.json` / 锁文件依赖清单。 |
| `structured_risk_output` | PASS | with_skill 要求结构化 review、风险矩阵、证据、影响和修复建议，并明确不直接输出代码或配置补丁。 |
| `hands_off_remediation` | PASS | with_skill 明确应用鉴权 remediation 交 `engineer-agent`，依赖、构建或部署 remediation 交 `devops-agent`。 |
| `evaluates_escalation_to_pm_at_closeout` | PASS | with_skill 明确当前路由阶段无 Security 自有确认结论所以不升级；closeout 按该确认结论评估，触发时回 `pm-agent` 分类和建 issue，且不直交 `docs-agent`、不由 Security 自行创建 issue。 |

## With-Skill Behavior

with_skill 通过 PM handoff 入口门禁并保留 `auth-model` scope，准确选择 authz 主审与 dependency 后续。上一轮遗漏的两处在本轮都完整覆盖：五类下游安全上下文被逐项列出；closeout 明确锚定 Security 自有确认结论，并陈述当前路由不触发、回 PM 分类/建 issue以及禁止直交 Docs/自行建 issue的完整边界。因此本次疑似方差重跑未复现失败。

## Fresh Without-Skill Baseline

fresh baseline 能从 PM handoff 与 PRD 推断先权限后依赖的合理顺序，也包含一般性的权限文档、接口、测试、依赖与整改归属。它没有命名 canonical `authz-reviewer` / `dependency-risk-auditor`，没有 feature 报告路径，也没有 `Security Conclusion Escalation to PM` 的完整 closeout 契约。with_skill 在 specialist 精确路由、归档和升级边界上有明确增益。

## Failures

- 无；上一轮 `collects_security_context` 与 `evaluates_escalation_to_pm_at_closeout` 的候选输出遗漏均未在本轮 fresh run 复现。

## Next Steps

- 无 eval 行为修复项；后续候选继续完整保留安全上下文清单与 Security closeout 升级边界。

## Runtime Artifacts Policy

- 本轮 candidate、fresh baseline、fixture copies 与 judge 仅位于 `tmp/eval-runs/pr-204-fix-round-20260801/security-agent/eval-001-route-auth-release-risk/`，不提交到 git。
- 提交范围仅包含 canonical `comparison.md`；不提交 with_skill / without_skill、transcript、verdict、timing、diagnostics 或其他运行期文件。
