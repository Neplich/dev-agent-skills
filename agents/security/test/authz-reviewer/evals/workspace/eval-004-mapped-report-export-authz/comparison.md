# Eval Result: eval-004-mapped-report-export-authz

## Evaluation Target

- Agent: `security`
- Skill: `authz-reviewer`
- Eval: `eval-004-mapped-report-export-authz`
- Test case: Mapped Report Export Authorization
- Workspace: `workspace/eval-004-mapped-report-export-authz`
- Review context: issue #141 Security→PM 结论升级契约修订后的全量复验
- Latest result: PASS（4/4 assertions PASS）- fresh subagent validation completed on 2026-07-21

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt/fixture: 与 `evals.json` 当前提交一致（#141 未改动本 eval 定义）
- Fresh run: fresh general-purpose subagent 成对运行（with_skill 读取更新后 skill 文档；without_skill 不读任何 skill 文档/共享指令/历史 comparison，baseline 本轮重新生成，未复用历史）。本轮经维护者批准以 Claude fresh subagent 执行；后续轮次按更新后的委派规则由 codex 执行。
- Source head: `docs/issue-141-security-pm-escalation` 分支（#141 Security→PM 结论升级契约修订）
- Validation date: 2026-07-21

## Assertions

- PASS：change-map 反查只读 `docs/site/api/report-export.md`。
- PASS：识别文档声称仅 admin 可导出、代码实际放行 analyst 的矛盾，以代码事实评估越权。
- PASS：识别 unverified，扩大代码核证而非采信文档。
- PASS：断言于第二轮 review 后补充；行为证据来自 2026-07-21 同一轮 fresh subagent validation——with_skill candidate 在该轮已展示此行为（mapped 场景正确升级回 pm-agent）。

## With Skill Behavior

结论克制：不单方面裁定 admin-only 是否为预期，交 owner 确认意图；feature_path 未确认故不落档、不自建顶层目录。closeout 验证（#141 核心）：确认结论改变 `docs/site/` 正式文档事实，candidate 按 `Security Conclusion Escalation to PM` 把结论与证据**回交 pm-agent 分类并提 issue**；未直交 docs-agent、未自建 issue、未修改文档；随后 Safety-Net Closeout 等待用户确认。

## Without Skill Baseline

fresh baseline 同样发现 analyst 越权矛盾（fixture 驱动），但无 change-map 纪律、无 unverified 信任模型、无升级/closeout 语义。

## Failures

无。

## Next Steps

- 无阻塞项。

## Runtime Artifacts Policy

- 运行期证据（candidate、baseline、transcript）仅保留在 session scratchpad，不提交到 git。
- Runtime transcripts、verdicts、timing、output 目录、diagnostics 与生成的 with_skill / without_skill 文件均不得提交。
