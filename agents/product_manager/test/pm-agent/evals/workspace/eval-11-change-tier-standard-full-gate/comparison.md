# Eval Result: eval-011-change-tier-standard-full-gate

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-011-change-tier-standard-full-gate`
- Test case: change-tier-standard-full-gate
- Workspace: `workspace/eval-11-change-tier-standard-full-gate`
- Review context: issue #141 Security→PM 结论升级契约修订后的全量复验
- Latest result: PASS（3/3 assertions PASS）- fresh subagent validation completed on 2026-07-21

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt/fixture: 与 `evals.json` 当前提交一致（#141 未改动本 eval 定义）
- Fresh run: fresh general-purpose subagent 成对运行（with_skill 读取更新后 skill 文档；without_skill 不读任何 skill 文档/共享指令/历史 comparison，baseline 本轮重新生成，未复用历史）。本轮经维护者批准以 Claude fresh subagent 执行；后续轮次按更新后的委派规则由 codex 执行。
- Source head: `docs/issue-141-security-pm-escalation` 分支（#141 Security→PM 结论升级契约修订）
- Validation date: 2026-07-21

## Assertions

- PASS `classify_standard`
- PASS `require_prd_trd_alignment`
- PASS `request_type_existing_update`

## With Skill Behavior

判 `existing_update`/`standard`，拒绝 hotfix；要求 PRD/TRD 对齐后再下游。

## Without Skill Baseline

fresh baseline 凭通用常识给出合理的分类/流程建议，但未使用 canonical request_type / change_tier 契约词汇，无 handoff packet 结构、无入口门禁与 fast lane 边界语义。

## Failures

无。

## Next Steps

- 无阻塞项。

## Runtime Artifacts Policy

- 运行期证据（candidate、baseline、transcript）仅保留在 session scratchpad，不提交到 git。
- Runtime transcripts、verdicts、timing、output 目录、diagnostics 与生成的 with_skill / without_skill 文件均不得提交。
