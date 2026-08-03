# Eval Result: eval-009-prd-iteration-split-proposal

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec` (`prd-iteration` lane)
- Eval: `eval-009-prd-iteration-split-proposal`
- Workspace: `workspace/eval-009-prd-iteration-split-proposal`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: current workspace atop HEAD `160faaf`; the four level-1 fixture documents have the uncommitted schema correction `parent_feature: "N/A"`. This case contains a confirmed `notification-center` PRD with 3 explicit domains, 10 user stories, 8 functional requirements, and a polling-based Engineer TRD.
- Fresh run: `2026-08-03 15:02:31 +0800`
- Runtime directory: `tmp/eval-runs/issue-197-evals-r3/idea-to-spec/eval-009-prd-iteration-split-proposal/`

## Latest Result

- Behavior result: PASS — all 5 assertions passed.
- Coverage result: FULL — 5/5 assertion scenarios were exercised; no `NOT EXERCISED` items.
- Overall result: PASS

## Assertion Results

- `applies_requested_change`: PASS — the with-skill response first applies the polling-to-event-driven delta to `FR-02`, Delivery Strategy, and the urgent-delivery acceptance criterion in a working draft; it does not reduce the task to structure analysis.
- `detects_l2b_signals`: PASS — it reports 3 independent domains and 18 combined US/FR rows as two triggered L2b signals, while correctly noting that the 69-line PRD does not trigger the `>500` signal.
- `presents_split_proposal`: PASS — it proposes a `notification-center` child tree for delivery strategy, subscription management, and channel configuration; maps every source section or requirement group to the parent or a child; and lists impacts for `docs/engineer`, `docs/design`, `docs/qa/e2e`, `docs/devops`, and `docs/security`.
- `waits_for_confirmation`: PASS — it explicitly waits for user confirmation and states that no split, `git mv`, or child document creation will occur beforehand.
- `rejection_keeps_current_flow`: PASS — it states that rejection preserves the current `notification-center` feature path and continues the normal `1.3.0 -> 1.4.0` bump, changelog, and inline-validation flow.

## With-Skill Behavior

The response recognizes the corrected level-1 metadata (`parent_feature: N/A`), applies the requested product delta before evaluating structure, uses the actual fixture counts to trigger L2b, and produces a confirmation-gated proposal with a complete parent/child content map. It preserves PM/Engineer ownership boundaries, records absent downstream artifacts as `no artifact found`, and does not modify or restructure the fixture while the proposal is pending.

## Fresh Without-Skill Baseline

The baseline was newly generated in this run from the same prompt and fixture without reading or applying the target skill, Product Manager README, internal instructions, or historical comparison. It correctly changes polling to event-driven delivery and notices that the polling-based TRD will need follow-up, but it treats the request as a straightforward single-document revision. It does not evaluate L2b signals, propose a child `feature_path` tree, map source sections, enumerate downstream mirrors, or state the confirmation and rejection behavior.

## Failures

- No assertion failures, unexercised assertions, or baseline-generation blockers.
- No fixture or assertion defect was observed.

## Next Steps

- Keep this eval as regression coverage for the post-change L2b assessment and proposal-confirmation gate.

## Runtime Artifact(s) Policy

- Fresh with-skill response, newly generated without-skill baseline, and judge notes remain under `tmp/eval-runs/issue-197-evals-r3/idea-to-spec/eval-009-prd-iteration-split-proposal/` and are not committed.
