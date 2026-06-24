# Eval Result: eval-002-auth-bypass

## Evaluation Target

- Agent: `security`
- Skill: `appsec-checklist`
- Eval: `eval-002-auth-bypass`
- Test case: Authentication Bypass
- Workspace: `workspace/eval-002-auth-bypass`
- Latest result: PARTIAL - prior skill validation evidence is preserved; without-skill baseline was not generated for this historical comparison.
- Prior validation note: fresh Codex subagent validation completed on 2026-06-02

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Test detection of missing authentication on admin endpoint
- Expected output: Structured application security checklist with prioritized findings, affected surfaces, evidence, impact, and remediation guidance.

## Assertions

- `security_findings`: 识别与场景匹配的应用安全风险，例如注入、认证绕过或 XSS
- `evidence_and_impact`: 说明证据、受影响入口和业务或安全影响
- `severity_rationale`: 给出严重度并说明判断依据
- `remediation`: 提供具体、可执行的修复建议或验证步骤

## With Skill

Observed behavior:

- 当前 skill 覆盖认证、session、access control、缺失权限检查和认证绕过，并要求按 Critical/High 等级给出证据、影响和修复建议。

## Without Skill / Baseline
- BLOCKED: No actual without-skill baseline result is recorded for this historical comparison. This file is not treated as a full eval PASS until a baseline result is generated and written here.
- This comparison records whether the skill-specific protocol, routing, evidence, or artifact expectations are preserved.

## Failures

- None found in fresh Codex subagent validation.

## Next Steps

- 无需修改当前 skill 指令。

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be committed.
