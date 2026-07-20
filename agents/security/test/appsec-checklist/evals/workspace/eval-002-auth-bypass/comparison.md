# Eval Result: eval-002-auth-bypass

## Evaluation Target

- Agent: `security`
- Skill: `appsec-checklist`
- Eval: `eval-002-auth-bypass`
- Test case: Authentication Bypass
- Workspace: `workspace/eval-002-auth-bypass`
- Review context: issue #141 Security→PM 结论升级契约修订后的全量复验
- Latest result: PARTIAL（入口门禁触发，assertions 无法展开）- fresh subagent validation completed on 2026-07-21

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt/fixture: 与 `evals.json` 当前提交一致（#141 未改动本 eval 定义）
- Fresh run: fresh general-purpose subagent 成对运行（with_skill 读取更新后 skill 文档；without_skill 不读任何 skill 文档/共享指令/历史 comparison，baseline 本轮重新生成，未复用历史）。本轮经维护者批准以 Claude fresh subagent 执行；后续轮次按更新后的委派规则由 codex 执行。
- Source head: `docs/issue-141-security-pm-escalation` 分支（#141 Security→PM 结论升级契约修订）
- Validation date: 2026-07-21

## Assertions

- BLOCKED `security_findings`：fixture 缺确认上下文，入口门禁触发，断言无法展开判定
- BLOCKED `evidence_and_impact`：fixture 缺确认上下文，入口门禁触发，断言无法展开判定
- BLOCKED `severity_rationale`：fixture 缺确认上下文，入口门禁触发，断言无法展开判定
- BLOCKED `remediation`：fixture 缺确认上下文，入口门禁触发，断言无法展开判定

## With Skill Behavior

fresh candidate 严格按更新后的 SKILL.md 执行：入口门禁判定缺少 PM handoff packet、已确认 feature_path 与可审查 fixture（workspace 仅含 eval_metadata 与历史 comparison），正确将请求温和退回 `pm-agent` 分类，不执行 认证绕过/授权 审查、不臆造证据。closeout 行为符合 #141 新契约：Security Conclusion Escalation to PM 已评估且**正确不触发**（无 confirmed conclusion），Safety-Net Closeout 引导回 pm-agent 并等待确认。

## Without Skill Baseline

fresh baseline 未读 skill 文档，给出通用认证绕过/授权方法论与优先级建议；无入口门禁、无升级/closeout 语义。

## Failures

断言全部无法判定（fixture 阻塞）。根因与 issue #140 同类：workspace 缺 PM handoff packet / 已确认上下文 / 可审查代码或配置 fixture，fresh candidate 依 PM Handoff Entry Gate 正确退回 pm-agent。属 **fixture/prompt 场景缺陷，非 skill 引导缺陷**，与 #141 closeout 改动无关（同 skill 的 mapped eval 全 PASS）。

## Next Steps

- 按 #143 为本 eval workspace 补齐已确认上下文 fixture（PM handoff packet 或等价确认文档链 + 可审查样本），或调整 prompt/assertion 明确入口前提，修正后重跑。

## Runtime Artifacts Policy

- 运行期证据（candidate、baseline、transcript）仅保留在 session scratchpad，不提交到 git。
- Runtime transcripts、verdicts、timing、output 目录、diagnostics 与生成的 with_skill / without_skill 文件均不得提交。
