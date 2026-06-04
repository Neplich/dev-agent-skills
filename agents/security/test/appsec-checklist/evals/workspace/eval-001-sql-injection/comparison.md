# Eval Result: eval-001-sql-injection

## Evaluation Target

- Agent: `security`
- Skill: `appsec-checklist`
- Eval: `eval-001-sql-injection`
- Test case: SQL Injection Vulnerability
- Workspace: `workspace/eval-001-sql-injection`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-06-02

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Test detection of SQL injection vulnerability in user search
- Expected output: Structured application security checklist with prioritized findings, affected surfaces, evidence, impact, and remediation guidance.

## Assertions

- `security_findings`: 识别与场景匹配的应用安全风险，例如注入、认证绕过或 XSS
- `evidence_and_impact`: 说明证据、受影响入口和业务或安全影响
- `severity_rationale`: 给出严重度并说明判断依据
- `remediation`: 提供具体、可执行的修复建议或验证步骤

## With Skill

Observed behavior:

- 当前 skill 明确要求检查 raw SQL/SQL injection，输出受影响入口、证据、影响、严重度和参数化查询修复建议，覆盖全部 assertions。

## Without Skill / Baseline

- Baseline behavior is diagnostic only.
- This comparison records whether the skill-specific protocol, routing, evidence, or artifact expectations are preserved.

## Failures

- None found in fresh Codex subagent validation.

## Next Steps

- 无需修改当前 skill 指令。

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be committed.
