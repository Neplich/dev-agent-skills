# Eval Result: eval-001-docker-rollback

## Evaluation Target

- Agent: `devops`
- Skill: `incident-playbook-writer`
- Eval: `eval-001-docker-rollback`
- Test case: docker-rollback
- Workspace: `workspace/eval-001-docker-rollback`
- Latest result: PASS - 2026-07-26 fresh paired validation completed; with_skill and fresh without_skill both satisfied 6/6 assertions.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: confirmed repo-wide incident handoff and real Docker Compose rollback context
- Expected output: 生成运维手册，包含回滚、故障响应、排查指南

## Assertions

- PASS `deploy_rollback_md`: 生成 `deploy/ROLLBACK.md`。
- PASS `rollback_md_docker`: 回滚文档包含绑定 fixture 的 Docker 命令。
- PASS `deploy_incident_response_md`: 生成 incident response 文档。
- PASS `incident_response_md`: 覆盖常见故障场景。
- PASS `deploy_troubleshooting_md`: 生成 troubleshooting 文档。
- PASS `deploy_on_call_md`: 生成 on-call 文档。

## With Skill

- 满足 6 项断言，并额外覆盖回滚前置条件、中止规则、P1/P2 响应、角色升级、证据保留与 closeout。
- 输入 Compose 配置解析通过。

## Without Skill / Baseline

- 2026-07-26 使用同一 prompt 和 fixture 重新生成 fresh baseline，未读取或应用 incident-playbook-writer skill、Agent README、历史 comparison 或旧 baseline。
- baseline 同样满足 6/6 assertions，但前置条件、响应分级与证据闭环较简略。

## Failures

- 无 assertion failure。
- 未执行真实回滚或故障演练；当前 assertions 对 skill 增益的区分度有限。

## Next Steps

- 保留四份运维文档和真实 Docker 命令覆盖。

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics were generated only in an ignored scratch workspace and are not committed.
