# Eval Result: eval-002-defer-bootstrap-without-spec

## Evaluation Target

- Agent: `engineer`
- Skill: `project-bootstrap`
- Eval: `eval-002-defer-bootstrap-without-spec`
- Test case: defer-bootstrap-without-spec
- Workspace: `workspace/eval-002-defer-bootstrap-without-spec`
- Latest result: PARTIAL - prior skill validation evidence is preserved; without-skill baseline was not generated for this historical comparison.
- Prior validation note: fresh Codex subagent validation completed on 2026-06-02

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Verifies that project-bootstrap handles defer-bootstrap-without-spec and produces the expected role-specific artifact.
- Expected output: 识别到缺少 TRD 或已确认 spec；不要直接脚手架；要求先补 PM/idea-to-spec 文档收敛，或仅在用户明确要求跳过 PM 时才继续 bootstrap。

## Assertions

- `assertion_1`: 缺少规格时不应直接初始化
- `pm`: 回指 PM 路径
- `override`: 保留显式 override 例外

## With Skill

Observed behavior:

- 当前 SKILL.md 的 Non-Negotiable Gate 明确无 TRD/PRD/已确认 spec 且无显式 skip PM 时必须拒绝 scaffold，回指 pm-agent:idea-to-spec，并保留显式 override 例外。

## Without Skill / Baseline
- BLOCKED: No actual without-skill baseline result is recorded for this historical comparison. This file is not treated as a full eval PASS until a baseline result is generated and written here.
- This comparison records whether the skill-specific protocol, routing, evidence, or artifact expectations are preserved.

## Failures

- None found in fresh Codex subagent validation.

## Next Steps

- 保持该 eval 覆盖无 spec 不脚手架。

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be committed.
