# Eval Result: eval-009-prd-iteration-split-proposal

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec` (`prd-iteration` lane)
- Eval: `eval-009-prd-iteration-split-proposal`
- Workspace: `workspace/eval-009-prd-iteration-split-proposal`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: current uncommitted workspace atop HEAD `82376b4`. It includes the review fixes that make `prd-iteration` derive direct child paths before using `child_features: N/A`, align approved structural changes across Engineer TRD/API/ADR artifacts, hand active implementation plan alignment to `engineer-agent:feature-implementor`, and add the Implemented plan at `docs/engineer/repository-governance/feature-path-contract/IMPLEMENTATION_PLAN.md`. The eval fixture itself remains the confirmed level-1 `notification-center` PRD with no direct child directories, 3 explicit domains, 10 user stories, 8 functional requirements, and a polling-based Engineer TRD.
- Fresh run: `2026-08-03 17:24:15 +0800`
- Runtime directory: `tmp/eval-runs/issue-197-evals-r6/eval-009/`

## Latest Result

- Behavior result: PASS — all 5 assertions passed.
- Coverage result: FULL — 5/5 assertion scenarios were exercised; no `NOT EXERCISED` items.
- Overall result: PASS

## Assertion Results

- `applies_requested_change`: PASS — the with-skill run produced a complete updated PRD in `updated-PRD.md`; FR-02, Delivery Strategy, and AC-2 now specify event publication, subscribed consumers, and a 10-second urgent-delivery criterion. The candidate derives direct children first and keeps `child_features: N/A` only because the fixture contains no direct child paths.
- `detects_l2b_signals`: PASS — the with-skill response explicitly exercises 3 independent domains and 18 combined US/FR rows as two L2b signals, while correctly noting that the document is below 500 lines.
- `presents_split_proposal`: PASS — the proposal contains the three child paths `delivery-strategy`, `subscription-management`, and `channel-configuration`; maps parent-retained and child-bound content; and covers `docs/engineer`, `docs/design`, `docs/qa/e2e`, `docs/devops`, and `docs/security`. Its Engineer impact covers affected TRD/API/ADR artifacts and delegates active plan alignment to `engineer-agent:feature-implementor`.
- `waits_for_confirmation`: PASS — the response states that no split, child-document creation, `git mv`, or mirror move occurs before explicit user confirmation, and classifies an approved structure change as a separate `major` flow.
- `rejection_keeps_current_flow`: PASS — rejection preserves `notification-center` and resumes the normal `1.3.0 -> 1.4.0` bump, changelog, inline validation, and Engineer-owned event-driven alignment flow.

## With-Skill Behavior

The run first reconciled the existing feature tree, found no direct child path, and therefore retained `child_features: N/A`. It then applied the requested event-driven delta to a complete working PRD before assessing structure. The working document keeps the current path and version because the L2b structural decision is still pending. Based on actual fixture evidence, the response proposed a three-child tree, supplied a traceable content map and five-root downstream mirror impact list, reflected the expanded Engineer TRD/API/ADR scope and active-plan ownership, and held all restructuring behind explicit confirmation. It also defined the rejection path back to normal versioning and validation.

## Fresh Without-Skill Baseline

The baseline was newly generated in this run from the same prompt and fixture without applying `idea-to-spec`, the Product Manager README, internal instructions, historical comparison, or prior runtime output. It supplied concrete event-driven replacement content and noticed that the polling TRD would need later alignment, so `applies_requested_change` passed. It did not count L2b signals, propose child paths with content and mirror maps, establish a confirmation gate, or define the rejection path. Baseline result: 1/5 assertions passed.

## Judge Conclusion

The fresh judge compared the current fixture, complete with-skill PRD, with-skill response, newly generated baseline, and all five semantic assertions. The requested content change is present in the candidate itself; both L2b signals are measured; every proposal surface is explicit; and confirmation and rejection semantics are directly exercised. Therefore Behavior is PASS and Coverage is FULL. The baseline contrast shows that generic PRD editing supplies the content delta but not the repository-specific L2b governance behavior.

## Failures

- No with-skill assertion failures, unexercised assertions, or baseline-generation blockers.
- Baseline gaps: `detects_l2b_signals`, `presents_split_proposal`, `waits_for_confirmation`, and `rejection_keeps_current_flow` failed.

## Next Steps

- Keep this eval as regression coverage for applied PRD content, derive-first `child_features` reconciliation, L2b proposal gating, expanded Engineer artifact scope, and active implementation plan ownership.

## Runtime Artifact(s) Policy

- The complete with-skill response and updated PRD, newly generated without-skill baseline, and explicit judge record remain under `tmp/eval-runs/issue-197-evals-r6/eval-009/` and are not committed.
