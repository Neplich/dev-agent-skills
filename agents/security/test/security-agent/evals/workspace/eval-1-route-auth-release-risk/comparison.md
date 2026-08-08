# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `security-agent`
- Eval: `eval-001-route-auth-release-risk`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `6becbc324dd17ee4f5ba7cdf2d867ad58ae183800d34e6d3eb510323380d49a0` from `agents/security/test/security-agent/evals/workspace/eval-1-route-auth-release-risk`.
- Fixture SHA-256: `6becbc324dd17ee4f5ba7cdf2d867ad58ae183800d34e6d3eb510323380d49a0`
- Prompt SHA-256: `5a4bc456b36f0fe19e8d15843877f0c9ef8daed9d99b67bdcc85d65720c79c5b`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `c7bb70655078216ed1473a2f43ea75bd2a651e603db60ff1bdae499fb8fcad0d`
- Skill overlay SHA-256: `3d7c6fcf40c8244a30d0a19185ac32957c7700ee79807e5938bbaf835def210a`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `86d9cf5b5d192be02693890eee51825a1b00e0750fd5f2d88fdcc91b3fe08ad7`
- Metadata SHA-256: `10861a3430f4e9df517502c7dede98b52c06228662db21b0d8914dd6b558a77c`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_primary_to_authz` | PASS | with_skill 明确将权限与认证审查列为最高优先级，并指定负责人 authz-reviewer。 |
| `names_dependency_followup` | PASS | with_skill 明确将依赖与供应链审查列为第二步，并指定 dependency-risk-auditor。 |
| `collects_security_context` | PASS | with_skill 要求读取角色—权限矩阵、登录与 session 流程、敏感 endpoint 鉴权覆盖、越权与 session 测试、package.json 和 lockfile 等依赖材料。 |
| `structured_risk_output` | PASS | with_skill 声明交付审查报告、最终风险矩阵、测试/扫描证据和修复建议，并明确不直接修改实现。 |
| `hands_off_remediation` | FAIL | with_skill 仅提到应用工程团队和平台工程团队，没有明确交给 engineer-agent 或 devops-agent。 |
| `evaluates_escalation_to_pm_at_closeout` | FAIL | with_skill 未说明 closeout 时按 Security Conclusion Escalation to PM 评估 Security 自有确认结论，也未说明路由阶段不触发升级、不得直接交给 docs-agent 或由 Security 自行创建 issue。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5a4bc456b36f0fe19e8d15843877f0c9ef8daed9d99b67bdcc85d65720c79c5b; fixture_sha256=6becbc324dd17ee4f5ba7cdf2d867ad58ae183800d34e6d3eb510323380d49a0; output_sha256=c1672a787ba23c95820b857bcb7f087c2b15c1c75b2f80c25c4995562636220c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 按权限/认证审查、依赖审查、上线门禁复核顺序组织工作，并明确指定 authz-reviewer 与 dependency-risk-auditor；但缺少指定 remediation agent 和 closeout PM escalation 规则。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5a4bc456b36f0fe19e8d15843877f0c9ef8daed9d99b67bdcc85d65720c79c5b; fixture_sha256=6becbc324dd17ee4f5ba7cdf2d867ad58ae183800d34e6d3eb510323380d49a0; output_sha256=a0232eb6da04df54a906cba6e1d427324d857bdd489a0a3fe02c47bbd3eefe83; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提供了详细的安全审查清单和证据要求，但将依赖扫描并行推进，未按要求明确 authz-reviewer 主 route 或 dependency-risk-auditor 后续 route。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- hands_off_remediation 未满足指定 agent 名称要求。
- evaluates_escalation_to_pm_at_closeout 未覆盖 closeout 升级及相关禁止事项。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Migration Status

## Current Result

- Evidence status: **STALE**
- Migration status: **PENDING**
- Blocking reason: this eval has not yet been rerun under the Issue #246 scenario, lane-isolation, and fresh-judge contract.
Overall result: BLOCKED

## Historical Context (Superseded)

The complete pre-migration comparison follows unchanged. It is retained only as historical context and is not current release evidence.

---

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
