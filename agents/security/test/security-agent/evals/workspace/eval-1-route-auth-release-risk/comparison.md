# Eval Result: eval-001-route-auth-release-risk

## Evaluation Target

- Agent: `security`
- Skill: `security-agent`
- Eval: `eval-001-route-auth-release-risk`
- Test case: route-auth-release-risk
- Workspace: `workspace/eval-1-route-auth-release-risk`
- Review context: issue #141 Security→PM 结论升级契约修订后的全量复验
- Latest result: PASS（5/5 assertions PASS）- fresh subagent validation completed on 2026-07-21

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt/fixture: 与 `evals.json` 当前提交一致（#141 未改动本 eval 定义）
- Fresh run: fresh general-purpose subagent 成对运行（with_skill 读取更新后 skill 文档；without_skill 不读任何 skill 文档/共享指令/历史 comparison，baseline 本轮重新生成，未复用历史）。本轮经维护者批准以 Claude fresh subagent 执行；后续轮次按更新后的委派规则由 codex 执行。
- Source head: `docs/issue-141-security-pm-escalation` 分支（#141 Security→PM 结论升级契约修订）
- Validation date: 2026-07-21

## Assertions

- PASS：主 route `authz-reviewer`，命中路由信号并说明不走 `appsec-checklist` 兜底。
- PASS：`dependency-risk-auditor` 明确后续链，不扩链。
- PASS：完整列出认证流程、角色权限矩阵、敏感路由、测试证据与依赖清单（#140 fixture 使入口 gate 通过）。
- PASS：结构化 review 报告归档 `docs/security/auth-model/`，非补丁。
- PASS：代码修复交 `engineer-agent`，依赖/部署交 `devops-agent`。

## With Skill Behavior

入口 gate 凭 #140 的 PM_HANDOFF fixture 通过；路由与上下文清单同前 PASS。**#141 closeout 新行为验证**：candidate 评估 `Security Conclusion Escalation to PM` 并**正确不触发**（路由阶段尚无 confirmed conclusion），表述中不再出现直交 docs-agent 的路径；Safety-Net Closeout 建议下一步并等待确认。

## Without Skill Baseline

fresh baseline 给出通用优先级划分，未命名 canonical route，无入口门禁与升级/closeout 语义（借到 PM_HANDOFF fixture 的 handoff 线索，差异点同前披露）。

## Failures

无。#141 契约修订后 routing 与 closeout 语义均正确（Regression PASS）。

## Next Steps

- 无阻塞项。

## Runtime Artifacts Policy

- 运行期证据（candidate、baseline、transcript）仅保留在 session scratchpad，不提交到 git。
- Runtime transcripts、verdicts、timing、output 目录、diagnostics 与生成的 with_skill / without_skill 文件均不得提交。
