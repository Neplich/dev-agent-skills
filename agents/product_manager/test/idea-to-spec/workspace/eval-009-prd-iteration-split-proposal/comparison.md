# Eval Result: eval-009-prd-iteration-split-proposal

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec` (`prd-iteration` lane)
- Eval: `eval-009-prd-iteration-split-proposal`
- Workspace: `workspace/eval-009-prd-iteration-split-proposal`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: current uncommitted workspace atop HEAD `74c3b26`. The workspace includes the review fixes that exclude `implementation-plans/archive/**` and `_legacy/**` from active overlong/L2b governance evidence, make child-PRD generation reconcile the parent `child_features` index from the complete direct-child set, and synchronize `related_prd` plus other applicable `related_*` path fields during approved Engineer structure changes. This fixture remains the confirmed level-1 `notification-center` PRD with no direct child directories, 3 explicit domains, 10 user stories, 8 functional requirements, and a polling-based Engineer TRD. The case directly exercises derive-first `child_features` reconciliation and the expanded downstream reference-impact proposal; it does not create a child PRD, so the `prd-gen` parent-index write path is present in the evaluated workspace but not independently exercised here.
- Fresh run: `2026-08-03 17:44:54 +0800`
- Runtime directory: `tmp/eval-runs/issue-197-evals-r7/eval-009/`

## Latest Result

- Behavior result: PASS — all 5 assertions passed.
- Coverage result: FULL — 5/5 assertion scenarios were exercised; no `NOT EXERCISED` items.
- Overall result: PASS

## Assertion Results

- `applies_requested_change`: PASS — the with-skill run produced a complete PRD candidate in `updated-PRD.md`; FR-02, Delivery Strategy, and AC-2 now specify event publication, subscribed consumers, removal of polling, and a 10-second urgent-delivery criterion. Direct children were derived from the fixture tree first, and `child_features: N/A` remains only because no direct child path exists.
- `detects_l2b_signals`: PASS — the with-skill response explicitly counted 3 independent domains and 18 combined US/FR rows as two L2b signals, while recording that the document is below 500 lines.
- `presents_split_proposal`: PASS — the response proposed `notification-center/delivery-strategy`, `notification-center/subscription-management`, and `notification-center/channel-configuration`; mapped parent-retained and child-bound content; and listed impacts for `docs/engineer`, `docs/design`, `docs/qa/e2e`, `docs/devops`, and `docs/security`. The Engineer impact explicitly covers TRD/API/ADR metadata, `related_prd`, other applicable `related_*` paths, active-plan ownership, and archive preservation.
- `waits_for_confirmation`: PASS — the response states that no split, child-PRD creation, `git mv`, or downstream mirror move occurs before explicit confirmation, and an approved restructure proceeds separately as `change_tier: major`.
- `rejection_keeps_current_flow`: PASS — rejection preserves `feature_path: notification-center` and resumes the normal `1.3.0 -> 1.4.0` version bump, changelog update, inline validation, and event-driven Engineer alignment without creating a child tree.

## With-Skill Behavior

The run first reconciled the actual feature tree and found no direct children, then applied the requested event-driven delta to a complete PRD candidate before evaluating structure. It measured both fixture-backed L2b signals, proposed a traceable three-child tree, supplied a five-root downstream impact list, and kept all structural actions behind explicit confirmation. The proposal reflects the current review fixes by treating parent indexes as complete derived sets, naming `related_prd` and other applicable `related_*` fields in Engineer alignment, and preserving archived implementation plans as historical rather than active evidence. The candidate remains on the current path and version while the structural decision is pending.

## Fresh Without-Skill Baseline

The baseline was newly generated in this run from the same prompt and fixture without reading or applying `idea-to-spec`, the Product Manager README, internal instructions, the historical comparison, or prior runtime output. It supplied concrete event-driven replacements for FR-02, Delivery Strategy, AC-2, the suggested version bump, and later TRD alignment, so `applies_requested_change` passed. It did not count L2b signals, propose child paths with content and five-root mirror maps, establish a confirmation gate, or define the rejection path. Baseline result: 1/5 assertions passed.

## Judge Conclusion

The fresh judge compared the current fixture, full with-skill PRD candidate, with-skill response, newly generated baseline, and all five assertions. The content delta exists in the candidate itself; the two L2b signals are measured from fixture evidence; the child tree, content map, and downstream impacts are explicit; and both confirmation and rejection semantics are exercised. Therefore Behavior is PASS and Coverage is FULL. The baseline contrast shows that generic PRD editing covers the requested content delta but omits the repository-specific L2b governance behavior.

## Failures

- No with-skill assertion failures, unexercised assertions, or baseline-generation blockers.
- Baseline gaps: `detects_l2b_signals`, `presents_split_proposal`, `waits_for_confirmation`, and `rejection_keeps_current_flow` failed.

## Next Steps

- Keep this eval as regression coverage for applied PRD content, derive-first child indexing, L2b proposal gating, full downstream reference impact, and rejection semantics.
- The `prd-gen` reconcile-first write path and archive/legacy exclusion are represented by the current workspace rules but need their own fixture evidence if direct assertion coverage is required.

## Runtime Artifact(s) Policy

- The complete with-skill response and PRD candidate, newly generated without-skill baseline, and explicit judge record remain under `tmp/eval-runs/issue-197-evals-r7/eval-009/` and are not committed.
