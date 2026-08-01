# Eval Result: eval-001-docker-rollback

## Evaluation Target

- Agent: `devops`
- Skill: `incident-playbook-writer`
- Eval: `eval-001-docker-rollback`
- Test case: docker-rollback
- Workspace: `workspace/eval-001-docker-rollback`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: issue #196 L2-3；确认过的 repo-wide PM handoff、Docker Compose、环境变量样例与部署 README
- Expected output: 仅生成用户明确请求且有仓库证据支撑的回滚与故障响应手册

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL**（5/5 assertions exercised）
- Overall result: PASS
- 运行日期：2026-07-31

## Assertions

- PASS `deploy_rollback_md`: 生成 `deploy/ROLLBACK.md`。
- PASS `rollback_md_docker`: 回滚文档包含绑定 fixture 的 Docker Compose 拉取、重建与验证命令。
- PASS `deploy_incident_response_md`: 生成 `deploy/INCIDENT_RESPONSE.md`。
- PASS `incident_response_md`: 覆盖应用不可用、容器异常、健康检查失败、调查、恢复与恢复验证。
- PASS `does_not_generate_unrequested_playbooks`: 只生成明确请求且有证据的 ROLLBACK 与
  INCIDENT_RESPONSE，未生成 TROUBLESHOOTING 或 ON_CALL。

## With Skill

- 来源：当前会话 fresh Codex validator；先读取 DevOps Agent README、skill、同一原始 prompt
  与 fixture，在 baseline 生成前写入并以 SHA-256 锁定。
- 将用户的“故障处理和回滚手册”收敛为 `INCIDENT_RESPONSE.md` 与 `ROLLBACK.md`。
- 两份文档均绑定实际 Compose 配置、不可变 SemVer tag、日志与 `/health` 验证；未把 PM
  handoff 中较宽的四项候选机械展开为四份文件。

## Without Skill / Baseline

- 来源：with-skill 候选锁定后，使用同一原始 prompt 与 fixture fresh 生成；生成时不读取或
  应用 skill、Agent README、with-skill 输出、历史 comparison 或旧 baseline。
- baseline 读取 PM handoff 的四项 `required_output` 后生成了 ROLLBACK、INCIDENT_RESPONSE、
  TROUBLESHOOTING 与 ON_CALL。
- baseline 满足前四项断言，但未满足“不得默认生成未请求 playbook”的新契约断言。

## Failures

- with-skill 无 assertion failure。
- baseline 失败：`does_not_generate_unrequested_playbooks`，额外生成 TROUBLESHOOTING 与
  ON_CALL。

## Next Steps

- 保留当前按请求选择 playbook 的断言；后续如新增用例，可覆盖“用户未选择文件时只确认不生成”
  和“选中文件但证据不足时阻塞该文件”，本轮不扩大范围。

## Runtime Artifacts Policy

- with-skill、fresh without-skill、锁定清单与 judge 只写入
  `tmp/eval-runs/issue-196-l2-3-4/incident-playbook-writer/eval-001-docker-rollback/`。
- 运行期 candidates、verdicts、timing、outputs 与 diagnostics 不提交；只提交本
  `comparison.md`。
