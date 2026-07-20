# Eval Result: eval-004-feature-path-report

## Evaluation Target

- Agent: `security`
- Skill: `appsec-checklist`
- Eval: `eval-004-feature-path-report`
- Test case: Feature Path Security Report
- Workspace: `workspace/eval-004-feature-path-report`
- Review context: issue #141 Security→PM 结论升级契约修订后的全量复验
- Latest result: PASS（4/4 assertions PASS）- fresh subagent validation completed on 2026-07-21

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt/fixture: 与 `evals.json` 当前提交一致（#141 未改动本 eval 定义）
- Fresh run: fresh general-purpose subagent 成对运行（with_skill 读取更新后 skill 文档；without_skill 不读任何 skill 文档/共享指令/历史 comparison，baseline 本轮重新生成，未复用历史）。本轮经维护者批准以 Claude fresh subagent 执行；后续轮次按更新后的委派规则由 codex 执行。
- Source head: `docs/issue-141-security-pm-escalation` 分支（#141 Security→PM 结论升级契约修订）
- Validation date: 2026-07-21

## Assertions

- PASS：读取同路径 PRD/TRD/IMPLEMENTATION_PLAN 并以其为范围依据。
- PASS：报告落 `docs/security/chat-interface/messages/history/search/appsec-checklist.md`。
- PASS：frontmatter 含完整 feature_path/parent_feature/feature_level。
- PASS：未创建 history-search 等同义顶层目录。

## With Skill Behavior

发现 [CRITICAL] SQL 注入（workspaceId/query 直接插值）、[HIGH] 授权执行缺失与敏感字段暴露。closeout 验证（#141 核心）：确认结论改变 `docs/site/` 正式文档事实，candidate 按 `Security Conclusion Escalation to PM` 把结论与证据**回交 pm-agent 分类并提 issue**；未直交 docs-agent、未自建 issue、未修改文档；随后 Safety-Net Closeout 等待用户确认。

## Without Skill Baseline

fresh baseline 也定位到注入与越权面（fixture 驱动），但无 feature_path 归档纪律、无 frontmatter 契约、无升级/closeout 语义。

## Failures

无。

## Next Steps

- 无阻塞项。

## Runtime Artifacts Policy

- 运行期证据（candidate、baseline、transcript）仅保留在 session scratchpad，不提交到 git。
- Runtime transcripts、verdicts、timing、output 目录、diagnostics 与生成的 with_skill / without_skill 文件均不得提交。
