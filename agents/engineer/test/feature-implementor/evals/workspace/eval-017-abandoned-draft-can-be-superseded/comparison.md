# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-017-abandoned-draft-can-be-superseded`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1f669b72548a150607fd615bf909a1c365d5c49a031676d6fa71132017e8642b` from `agents/engineer/test/feature-implementor/evals/workspace/eval-017-abandoned-draft-can-be-superseded`.
- Fixture SHA-256: `1f669b72548a150607fd615bf909a1c365d5c49a031676d6fa71132017e8642b`
- Prompt SHA-256: `3023c99f87e425cf1e709e4a173f62dfa04ac1cedece451c8d3671923093f7ca`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5a3403ec360f8aca06dd1301fa3bfe0f2bd967f54afc7bad9b5691a78697b0ca`
- Skill overlay SHA-256: `5c74cbf7ab5eef845bc8c3f0d81a775b1feca5810a9a615f9b35865026f3e841`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `d59f332d9689221834dd583c1a569fa62e1de4ce2c4c1d7f5aa087aed088bd53`
- Metadata SHA-256: `21a9c9ae11f8c9b8058a429c319a4f2a640a6b07fdf2d71e259bbc158caa4e24`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_unfinished_active_plan` | PASS | With-skill raw diff shows the original plan was Draft with implementation_scope `refund-reason-codes`, and the output identifies the current and archived plan paths. |
| `detects_explicit_abandonment` | PASS | The output and archived plan identify explicit maintainer abandonment/supersession of the unfinished refund reason-code round. |
| `archives_as_superseded` | FAIL | The archive has status `Superseded`, a non-empty `superseded_reason`, `implementation_scope`, and original metadata, but lacks required `archived_at`, `archive_approved_by`, and `source_plan` fields. |
| `links_replacement_plan` | PASS | The replacement plan contains `previous_plan_archive` pointing to the archive, and both plans use feature_path `payment-refund`; the archive is Superseded. |
| `waits_before_coding` | FAIL | No code was modified and implementation is blocked pending TRD completion, but the output does not state that user confirmation is still required before coding. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3023c99f87e425cf1e709e4a173f62dfa04ac1cedece451c8d3671923093f7ca; fixture_sha256=1f669b72548a150607fd615bf909a1c365d5c49a031676d6fa71132017e8642b; output_sha256=731014c63ba572543fe9cc77e423296677c5b171bc58c71be5c2486d7c421b1d; snapshot_sha256=04af1cb114eeb6b1d70ff70399d7bd15510a5c366ab97b81c93e8754d8b2cb44
- Behavior: Created a Superseded archive and linked replacement Draft plan, but omitted required archive metadata and did not explicitly wait for user confirmation before coding.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3023c99f87e425cf1e709e4a173f62dfa04ac1cedece451c8d3671923093f7ca; fixture_sha256=1f669b72548a150607fd615bf909a1c365d5c49a031676d6fa71132017e8642b; output_sha256=30677428babdc786852d112acf37bb5500311d1bfa25c6769f020aec31a01927; snapshot_sha256=25d73571d5f509474c20bb300783df84a2868dab0fcde25480a77493dd0f2b89
- Behavior: Updated the existing plan in place, marked it Superseded, changed scope, and claimed continuation, without creating a compliant archive or replacement-plan link.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The archive omits `archived_at`, `archive_approved_by`, and `source_plan`.
- The output does not explicitly require user confirmation before coding.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge package, verdict, timing, and diagnostics remain under ignored `tmp/eval-runs/` or short-lived CI artifacts and are not committed.
- This durable comparison retains only the reviewable summary and superseded history.

## Historical Context (Superseded)

# Issue #246 Migration Status

## Current Result

- Evidence status: **STALE**
- Migration status: **PENDING**
- Blocking reason: this eval has not yet been rerun under the Issue #246 scenario, lane-isolation, and fresh-judge contract.
Overall result: BLOCKED

## Historical Context (Superseded)

The complete pre-migration comparison follows unchanged. It is retained only as historical context and is not current release evidence.

---

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
