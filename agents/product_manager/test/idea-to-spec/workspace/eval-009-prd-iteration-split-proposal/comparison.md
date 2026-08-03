# Eval Result: eval-009-prd-iteration-split-proposal

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec` (`prd-iteration` lane)
- Eval: `eval-009-prd-iteration-split-proposal`
- Workspace: `workspace/eval-009-prd-iteration-split-proposal`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: current uncommitted workspace atop HEAD `65ec8f7`, including the tightened `applies_requested_change` assertion and current L2b, role-boundary, reparenting, `_legacy`, and `child_features` fixes. The confirmed level-1 `notification-center` PRD has 3 explicit domains, 10 user stories, 8 functional requirements, and a polling-based Engineer TRD.
- Fresh run: `2026-08-03 16:57:47 +0800`
- Runtime directory: `tmp/eval-runs/issue-197-evals-r5/eval-009/`

## Latest Result

- Behavior result: PASS — all 5 assertions passed.
- Coverage result: FULL — 5/5 assertion scenarios were exercised; no `NOT EXERCISED` items.
- Overall result: PASS

## Assertion Results

- `applies_requested_change`: PASS — the with-skill run produced a complete updated PRD at `with_skill/updated-PRD.md`; FR-02, Delivery Strategy, and AC-2 are actually event-driven rather than a verbal change plan. The fixture PRD remains untouched because the candidate is isolated runtime output.
- `detects_l2b_signals`: PASS — the response explicitly identifies 3 independent domains and 18 combined US/FR rows as two triggered L2b signals; it also records that the document is below 500 lines.
- `presents_split_proposal`: PASS — the proposal contains three child `feature_path` values, maps all parent and child content, and lists mirror impacts for `docs/engineer`, `docs/design`, `docs/qa/e2e`, `docs/devops`, and `docs/security`.
- `waits_for_confirmation`: PASS — the response states that no split, `git mv`, child-document creation, or downstream mirror move occurs before explicit user confirmation.
- `rejection_keeps_current_flow`: PASS — rejection preserves `notification-center` and resumes the normal `1.3.0 -> 1.4.0` bump, changelog, inline validation, and Engineer-owned TRD alignment flow.

## With-Skill Behavior

The run applied the requested event-driven delta before assessing structure and emitted the complete updated PRD content in the isolated runtime directory. Because the L2b proposal is not yet approved, that working document keeps the current `feature_path`, `child_features: N/A`, and version rather than representing the structural choice as settled. The response then used the actual fixture counts, proposed `delivery-strategy`, `subscription-management`, and `channel-configuration` child paths, preserved PM/Engineer ownership boundaries, and held all restructuring behind confirmation. Its rejection path explicitly completes the current single-path versioning and validation flow.

## Fresh Without-Skill Baseline

The baseline was newly generated in this run from the same prompt and fixture without reading or applying `idea-to-spec`, the Product Manager README, internal instructions, historical comparison, or prior runtime output. It produced updated PRD content for the event-driven delta and noted the polling TRD mismatch, so `applies_requested_change` passed. It did not count L2b signals, propose a child tree with content and mirror maps, establish the confirmation gate, or state the rejection path; the remaining 4 assertions failed. Baseline result: 1/5 assertions passed.

## Judge Conclusion

The fresh judge compared the with-skill output, newly generated baseline, fixture evidence, and all five semantic assertions. Each with-skill assertion has a concrete runtime artifact or response passage as evidence, so Behavior is PASS and Coverage is FULL. The baseline gap shows that generic PRD editing alone does not supply the required L2b governance behavior.

## Failures

- No with-skill assertion failures, unexercised assertions, or baseline-generation blockers.
- Baseline gaps: `detects_l2b_signals`, `presents_split_proposal`, `waits_for_confirmation`, and `rejection_keeps_current_flow` failed.

## Next Steps

- Keep this eval as regression coverage for the tightened actual-PRD-output requirement and the post-change L2b proposal/confirmation gate.

## Runtime Artifact(s) Policy

- The with-skill response and updated PRD, newly generated without-skill baseline, and explicit judge record remain under `tmp/eval-runs/issue-197-evals-r5/eval-009/` and are not committed.
