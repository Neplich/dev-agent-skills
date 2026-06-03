# Eval Result: eval-001-rbac

## Evaluation Target

- Agent: `security`
- Skill: `authz-reviewer`
- Eval: `eval-001-rbac`
- Test case: Role-Based Access Control
- Workspace: `workspace/eval-001-rbac`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-06-02

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Test review of RBAC implementation in multi-role app
- Expected output: Structured authorization review that identifies access-control risks, affected roles or resources, evidence, severity, and remediation guidance.

## Assertions

- `authorization_model`: 识别角色、资源、权限边界和关键授权路径
- `access_control_findings`: 指出越权、会话、JWT 或权限检查缺陷
- `evidence_and_impact`: 说明证据、影响范围和风险后果
- `remediation`: 提供可执行的授权修复和回归验证建议

## With Skill

Observed behavior:

- 当前 skill 要求提取角色权限、生成 role matrix、检查 protected endpoints 和 RBAC 覆盖，能输出越权风险、证据、影响和修复/回归建议。

## Without Skill / Baseline

- Baseline behavior is diagnostic only.
- This comparison records whether the skill-specific protocol, routing, evidence, or artifact expectations are preserved.

## Failures

- None found in fresh Codex subagent validation.

## Next Steps

- 无需修改当前 skill 指令。

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be committed.
