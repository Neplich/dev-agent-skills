# Eval Result: eval-017-abandoned-draft-can-be-superseded

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-017-abandoned-draft-can-be-superseded`
- Test case: abandoned-draft-can-be-superseded
- Workspace: `workspace/eval-017-abandoned-draft-can-be-superseded`
- Latest result: PASS - fresh Codex validation completed on 2026-07-27 with
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
