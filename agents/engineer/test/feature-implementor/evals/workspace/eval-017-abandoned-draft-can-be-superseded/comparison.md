# Eval Result: eval-017-abandoned-draft-can-be-superseded

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-017-abandoned-draft-can-be-superseded`
- Test case: abandoned-draft-can-be-superseded
- Workspace: `workspace/eval-017-abandoned-draft-can-be-superseded`
- Evaluation date: 2026-08-07
- Overall result: PASS
- Behavior result: PASS
- Coverage result: FULL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: docs/pm/payment-refund/PRD.md 和 docs/engineer/payment-refund/TRD.md 已确认。现有退款原因码实施计划不再继续，维护者明确要求废弃这一轮并为新的退款审核流程继续工作。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- PASS `reads_unfinished_active_plan`: with_skill transcript item_2 实际读取 active IMPLEMENTATION_PLAN.md，并输出 status: Draft、路径及 implementation_scope: refund-reason-codes。
- PASS `detects_explicit_abandonment`: transcript item_4 明确记录维护者已放弃该轮，并选择 Superseded 分支，而非继续更新 Draft。
- PASS `archives_as_superseded`: 实际归档文件 status 为 Superseded，包含非空 superseded_reason、implementation_scope、archived_at、archive_approved_by、source_plan，并保留原计划 metadata。
- PASS `links_replacement_plan`: 新 active IMPLEMENTATION_PLAN.md 包含 previous_plan_archive，指向同 feature_path 的 Superseded 归档文件。
- PASS `waits_before_coding`: transcript 无代码修改；workspace 仅新增/更新计划文档，最终输出请求确认后再开始实现。

## With Skill Behavior

with_skill 完成了读取、Superseded 归档、回链新计划，并等待确认；实际 workspace 哈希与 output.sha256 一致。

## Without Skill Baseline

without_skill 作为对照将旧计划标记为 Abandoned 并新增独立计划，未满足 Superseded 归档及 previous_plan_archive 回链要求。

## Failures / Findings

- None.
- Root cause: None.

## Next Steps

- 后续修改该 skill、fixture 或 assertions 时，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-017-abandoned-draft-can-be-superseded

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-017-abandoned-draft-can-be-superseded`
- Test case: abandoned-draft-can-be-superseded
- Workspace: `workspace/eval-017-abandoned-draft-can-be-superseded`
- Latest result: PASS - fresh Codex validation completed on 2026-07-27 with
- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。

  5/5 assertions passing for both with-skill and zero-exposure without-skill
  runs.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture files read before skill validation: `README.md`, `eval_metadata.json`,
  `docs/pm/payment-refund/PRD.md`, `docs/engineer/payment-refund/TRD.md`, and
  `docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md`.
- Fixture summary: the active plan is `status: Draft`, and the maintainer
  explicitly abandons the `refund-reason-codes` round before requesting a
  replacement refund-review plan.

## Assertions

- PASS `reads_unfinished_active_plan`: the response reads the fixed active path
  and identifies `status: Draft` and
  `implementation_scope: refund-reason-codes`.
- PASS `detects_explicit_abandonment`: it treats the maintainer's instruction
  as the explicit-abandonment exception instead of applying the default Draft
  continuation path.
- PASS `archives_as_superseded`: it selects a same-feature-path Superseded
  archive, requires a non-empty `superseded_reason`, and preserves
  `implementation_scope`, `archived_at`, `archive_approved_by`, `source_plan`,
  and the original plan metadata.
- PASS `links_replacement_plan`: it requires the replacement active plan at
  `docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md` to set
  `previous_plan_archive` to the Superseded archive.
- PASS `waits_before_coding`: it makes no code change and keeps implementation
  blocked until the replacement plan is confirmed.

## With Skill Behavior

The fresh with-skill validator read the Engineer README, the
`feature-implementor` entry, and its planner, reviewer, coding, and output
instructions before inspecting the complete fixture. It confirmed that PRD and
TRD metadata align, read the active Draft plan, and chose the explicit
abandonment path permitted by the archive gate. The expected handling archives
the existing plan as
`implementation-plans/archive/IMPLEMENTATION_PLAN-refund-reason-codes.md` with
`status: Superseded`, a non-empty reason, required archive metadata, and
preserved original metadata. It then creates the replacement plan at the fixed
active path with `previous_plan_archive` pointing to that archive and waits for
confirmation before coding.

The fixture identifies the approver only as the maintainer, without a
traceable name or account. The validator therefore required a real, non-empty
`archive_approved_by` value before persistence instead of inventing one; this
does not weaken the archive-field assertion.

## Without Skill Baseline

A separate fresh Codex subagent was spawned with no inherited turns. It
received only the eval prompt, the five assertions, and an allowlist of fixture
files; it was explicitly forbidden to read the Engineer README,
`feature-implementor` instructions, `evals.json`, or any historical
`comparison.md`, and it did not modify files.

The baseline independently read `status: Draft` and
`implementation_scope: refund-reason-codes`, recognized explicit abandonment,
selected a Superseded archive with the full required metadata, linked the
replacement active plan through `previous_plan_archive`, and waited before
coding. It passed 5/5 assertions and likewise declined to invent the missing
approver identity.

## Failures

- None.
- The paired run showed no assertion-level difference. The prompt and
  assertions expose the explicit-abandonment boundary and archive fields, so
  this eval confirms protocol correctness but has limited with-skill
  differentiation.

## Next Steps

- Keep the case focused on distinguishing explicit abandonment from the
  default behavior of continuing an unfinished Draft plan.
- If stronger differentiation is needed later, reduce rule-level hints in the
  assertions without removing the fixture evidence needed to audit archive
  metadata and linkage.

## Runtime Artifacts Policy

- The paired validation returned results in agent responses and did not create
  repository runtime files or modify fixture inputs.
- Runtime transcripts, verdicts, timing files, outputs, diagnostics, run status
  files, and `comparison.auto.md` must not be committed.
