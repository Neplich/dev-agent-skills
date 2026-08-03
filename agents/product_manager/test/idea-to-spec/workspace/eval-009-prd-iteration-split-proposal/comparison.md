# Eval Result: eval-009-prd-iteration-split-proposal

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec` (`prd-iteration` lane)
- Eval: `eval-009-prd-iteration-split-proposal`
- Workspace: `workspace/eval-009-prd-iteration-split-proposal`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: current uncommitted workspace atop HEAD `5af2134`. The workspace includes the latest review fixes: reserved namespace parents (`repository-governance` / `agent-collaboration`) need no physical root PRD or parent-index update; approved moves have per-role owners and each owner uses `git mv` only for its own directory; child-PRD creation refreshes the complete parent index and also bumps the parent version, refreshes `last_updated`, and adds changelog; contract PRD/TRD use `related_issues` and include issue #197. The eval fixture remains the confirmed level-1 `notification-center` PRD with no child directory, 3 domains, 10 user stories, 8 functional requirements, and a polling-based Engineer TRD. The case exercises the L2b gate and records the parent-update/per-role-owner constraints in the proposal; it does not create a child PRD or use a reserved namespace, so those positive execution paths are not separate assertions here.
- Fresh run: `2026-08-03 18:05:27 +0800`
- Runtime directory: `tmp/eval-runs/issue-197-evals-r8/eval-009/`

## Latest Result

- Behavior result: PASS — all 5 assertions passed.
- Coverage result: FULL — 5/5 assertion scenarios were exercised; no `NOT EXERCISED` items.
- Overall result: PASS

## Assertion Results

- `applies_requested_change`: PASS — the with-skill run produced a complete PRD candidate in `updated-PRD.md`; FR-02, Delivery Strategy, and AC-2 now specify event publication, subscribed consumers, removal of polling, and a measurable 10-second urgent-delivery path. Direct children were derived from the fixture first, so `child_features: N/A` remains correct.
- `detects_l2b_signals`: PASS — the response explicitly measured 3 independent domains and 18 combined US/FR rows, while noting the candidate is below 500 lines.
- `presents_split_proposal`: PASS — the proposal contains three child `feature_path` values, maps all parent-retained and child-bound content, and lists impacts for `docs/engineer`, `docs/design`, `docs/qa/e2e`, `docs/devops`, and `docs/security`. It also names the current per-role owners, Engineer reference synchronization, archive preservation, QA history preservation, and the complete parent-index/version/date/changelog update required if child PRDs are later created.
- `waits_for_confirmation`: PASS — no split, child document, `git mv`, or mirror move was performed; approval would start a separate `change_tier: major` flow.
- `rejection_keeps_current_flow`: PASS — rejection preserves `feature_path: notification-center` and resumes the normal `1.3.0 -> 1.4.0` bump, changelog, validation, and Engineer TRD alignment on the current path.

## With-Skill Behavior

The run first reconciled the fixture tree, then applied the event-driven product delta to a complete candidate before evaluating structure. It measured both fixture-backed L2b signals, proposed a traceable three-child tree, covered all five downstream mirror roots, assigned later work to the correct role owners, and kept every structural action behind explicit confirmation. The candidate stays at version `1.3.0` while the split decision is pending; rejection follows the ordinary iteration closeout.

## Fresh Without-Skill Baseline

The baseline was newly generated in this run from the same prompt and fixture without reading or applying `idea-to-spec`, Product Manager README, internal instructions, historical comparison, or prior runtime output. It proposed concrete event-driven changes to FR-02, Delivery Strategy, and AC-2 plus a version bump and TRD follow-up, so `applies_requested_change` passed. It did not measure L2b signals, propose the child tree/content map/five-root mirror impact, establish a confirmation gate, or define rejection semantics. Baseline result: 1/5 assertions passed.

## Judge Conclusion

The judge compared the current fixture, full with-skill PRD candidate and response, newly generated baseline, and all five assertions. The requested content delta exists in the candidate; the two L2b signals are directly measurable; the proposal contains the required tree, mapping, mirror impact, and current execution constraints; and both confirmation and rejection paths are explicit. Behavior is PASS and Coverage is FULL. The baseline contrast shows that generic PRD editing handles the content change but omits repository-specific structure governance.

## Failures

- No with-skill assertion failures, unexercised assertions, or baseline-generation blockers.
- Baseline gaps: `detects_l2b_signals`, `presents_split_proposal`, `waits_for_confirmation`, and `rejection_keeps_current_flow` failed.

## Next Steps

- Keep this eval as regression coverage for applied PRD content, L2b proposal gating, full downstream impact, current per-role ownership constraints, and rejection semantics.
- Use separate fixture assertions if direct positive coverage is needed for reserved namespace parents, actual child-PRD parent version/date/changelog updates, or contract `related_issues` metadata.

## Runtime Artifact(s) Policy

- The complete with-skill response and PRD candidate, newly generated baseline, and explicit judge record remain under `tmp/eval-runs/issue-197-evals-r8/eval-009/` and are not committed.
