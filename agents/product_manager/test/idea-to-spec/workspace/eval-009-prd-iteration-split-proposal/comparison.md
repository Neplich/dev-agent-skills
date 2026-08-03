# Eval Result: eval-009-prd-iteration-split-proposal

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec` (`prd-iteration` lane)
- Eval: `eval-009-prd-iteration-split-proposal`
- Workspace: `workspace/eval-009-prd-iteration-split-proposal`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: final uncommitted workspace atop HEAD `1e3eac4`. The confirmed level-1 `notification-center` PRD includes `child_features: "N/A"`, 3 explicit domains, 10 user stories, 8 functional requirements, and a polling-based Engineer TRD. Current output conventions define `child_features` as PRD-only and require other document types to omit it.
- Fresh run: `2026-08-03 15:56:54 +0800`
- Runtime directory: `tmp/eval-runs/issue-197-selfreview/final/eval-009/`

## Latest Result

- Behavior result: PASS — all 5 assertions passed.
- Coverage result: FULL — 5/5 assertion scenarios were exercised; no `NOT EXERCISED` items.
- Overall result: PASS

## Assertion Results

- `applies_requested_change`: PASS — the with-skill response first applies the event-driven delta to `FR-02`, Delivery Strategy, and AC-2 in a working result and identifies the polling-based TRD as a later Engineer alignment item.
- `detects_l2b_signals`: PASS — it explicitly reports 3 independent domains and 18 combined US/FR rows as two triggered L2b signals.
- `presents_split_proposal`: PASS — it proposes three child `feature_path` values, maps every source section or requirement group to the parent or a child, and lists impacts for `docs/engineer`, `docs/design`, `docs/qa/e2e`, `docs/devops`, and `docs/security`.
- `waits_for_confirmation`: PASS — it explicitly states that no split, `git mv`, child document creation, or downstream mirror move occurs before user confirmation.
- `rejection_keeps_current_flow`: PASS — it states that rejection preserves `notification-center` and resumes the normal `1.3.0 -> 1.4.0` bump, changelog, and inline-validation flow.

## With-Skill Behavior

The response applies the requested product delta before the structure assessment, uses the actual fixture counts, and produces a complete confirmation-gated L2b proposal. It names the parent PRD `child_features` update and `N/A` values for child PRDs without direct children, while explicitly omitting that PRD-only field from the Engineer TRD and other non-PRD documents. It also preserves the Engineer ownership boundary, archived implementation plans, and append-only QA result history. No fixture document or feature path is restructured while confirmation is pending.

## Fresh Without-Skill Baseline

The baseline was newly regenerated after the final skill change in an isolated context from the same prompt and fixture without reading or applying `idea-to-spec`, the Product Manager README, internal instructions, historical comparison, or prior runtime output. It also passed all 5 assertions: it applied the event-driven delta, detected both L2b signals, proposed the same three-child tree with a section map and five-role downstream impact list, waited for confirmation, and preserved the current path on rejection. The with-skill response remains more explicit about PRD-only `child_features`, Engineer ownership, archived plans, and QA history, but those additions do not change assertion coverage.

## Failures

- No with-skill assertion failures, unexercised assertions, or baseline-generation blockers.
- The fresh baseline also had no assertion failure; this fixture therefore demonstrates correct behavior but no assertion-level advantage over baseline in this run.

## Next Steps

- Keep this eval as regression coverage for post-change L2b assessment and the proposal-confirmation gate.
- If baseline discrimination becomes a goal, strengthen an existing assertion around parent `child_features`, archive preservation, or append-only QA history rather than changing this run's result.

## Runtime Artifact(s) Policy

- Fresh with-skill response, newly regenerated without-skill baseline, and self-check notes remain under `tmp/eval-runs/issue-197-selfreview/final/eval-009/` and are not committed.
