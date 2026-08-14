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
- Identity schema: `2`
- target_skill_sha256: `5c1776fcba11e4a564f6d8bef4826b23a262e7433780174f7756ea89d40a2136`
- eval_definition_sha256: `d5973b25612b7e076dab35db16f38a088f965995470b2ae2a1e956ac49b1959d`
- metadata_sha256: `10861a3430f4e9df517502c7dede98b52c06228662db21b0d8914dd6b558a77c`
- fixture_sha256: `6becbc324dd17ee4f5ba7cdf2d867ad58ae183800d34e6d3eb510323380d49a0`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `d09f4cbeb933e811c934cf8e665fe7675560abe0fc34d7865e0c67a56b1f4b12`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `5a4bc456b36f0fe19e8d15843877f0c9ef8daed9d99b67bdcc85d65720c79c5b`
- Repository HEAD: `2f950c46c67111058957774f796ccf97ae616d36`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `a9c69f3b86e02ca2f703b7da58237c4caab46ae028402c3524fc126377a613bc`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_primary_to_authz` | PASS | with_skill 明确将 `authz-reviewer` 作为第一个步骤，并聚焦 admin 越权、角色和认证边界。 |
| `names_dependency_followup` | PASS | with_skill 将 `dependency-risk-auditor` 列为第二步，专门审查 express 及依赖供应链风险。 |
| `collects_security_context` | PASS | with_skill 指定认证流程、角色矩阵、敏感路由、测试证据、实现代码及 package/锁文件和扫描结果作为下游输入。 |
| `structured_risk_output` | PASS | with_skill 声明交付结构化 security review/risk report，包含风险矩阵、证据、修复建议和上线结论，且不是实现补丁。 |
| `hands_off_remediation` | PASS | with_skill 将应用代码修复交给应用工程团队，将依赖、构建或部署修复交给平台工程团队，语义上对应 engineer-agent/devops-agent remediation handoff。 |
| `evaluates_escalation_to_pm_at_closeout` | NOT_EXERCISED | with_skill 已完成路由规划并等待用户确认后进入审查；closeout 阶段尚未发生，因此无法执行最终的 PM escalation 评估。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5a4bc456b36f0fe19e8d15843877f0c9ef8daed9d99b67bdcc85d65720c79c5b; fixture_sha256=6becbc324dd17ee4f5ba7cdf2d867ad58ae183800d34e6d3eb510323380d49a0; output_sha256=753230d8b14d64b0d110fed79248e7f4eff18cec557102f32456e0fef5a269c3; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确完成安全审查路由：authz-reviewer 主审、dependency-risk-auditor 后续，并给出上下文、结构化产物、remediation handoff 和条件性 PM 交接规则；等待用户确认进入下一步。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5a4bc456b36f0fe19e8d15843877f0c9ef8daed9d99b67bdcc85d65720c79c5b; fixture_sha256=6becbc324dd17ee4f5ba7cdf2d867ad58ae183800d34e6d3eb510323380d49a0; output_sha256=3627f0f2b4c6d177ae76d565124c835b46fe059c009f0c897b1d74c83f3cbbd2; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 给出较完整的通用安全审查计划和证据要求，但未明确使用 authz-reviewer 与 dependency-risk-auditor 路由。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 获得用户确认后执行 authz-reviewer；完成后再进行 dependency-risk-auditor 和 closeout escalation 评估。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
