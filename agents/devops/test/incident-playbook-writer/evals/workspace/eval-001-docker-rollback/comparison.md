# Eval Result: eval-001-docker-rollback

## Evaluation Target

- Agent: `devops`
- Skill: `incident-playbook-writer`
- Eval: `eval-001-docker-rollback`
- Test case: docker-rollback
- Workspace: `workspace/eval-001-docker-rollback`
- Latest result: PARTIAL - prior skill validation evidence is preserved; without-skill baseline was not generated for this historical comparison.
- Prior validation note: fresh Codex subagent validation completed on 2026-06-02

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Verifies that incident-playbook-writer handles docker-rollback and produces the expected role-specific artifact.
- Expected output: 生成运维手册，包含回滚、故障响应、排查指南

## Assertions

- `deploy_rollback_md`: deploy/ROLLBACK.md 存在
- `rollback_md_docker`: ROLLBACK.md 包含 docker 回滚命令
- `deploy_incident_response_md`: deploy/INCIDENT_RESPONSE.md 存在
- `incident_response_md`: INCIDENT_RESPONSE.md 包含常见故障场景
- `deploy_troubleshooting_md`: deploy/TROUBLESHOOTING.md 存在
- `deploy_on_call_md`: deploy/ON_CALL.md 存在

## With Skill

Observed behavior:

- 当前 skill 对 Docker 部署回滚和故障处理有明确产物要求：deploy/ROLLBACK.md、deploy/INCIDENT_RESPONSE.md、deploy/TROUBLESHOOTING.md、deploy/ON_CALL.md，并要求回滚命令、常见故障场景和排查命令绑定实际 Docker 部署方式。

## Without Skill / Baseline
- BLOCKED: No actual without-skill baseline result is recorded for this historical comparison. This file is not treated as a full eval PASS until a baseline result is generated and written here.
- This comparison records whether the skill-specific protocol, routing, evidence, or artifact expectations are preserved.

## Failures

- None found in fresh Codex subagent validation.

## Next Steps

- 无需修改当前 skill 指令。

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be committed.
