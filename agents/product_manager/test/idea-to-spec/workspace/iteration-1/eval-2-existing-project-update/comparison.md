# Eval Result: eval-002-existing-project-update

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-002-existing-project-update`
- Test case: existing-project-update
- Workspace: `workspace/iteration-1/eval-2-existing-project-update`

## Test Set / Fixture Version

- Evaluation date: `2026-07-28`
- Schema: `evals.json` v1.0
- Fixture: approved notification-center PRD, DECISIONS, and Engineer TRD covering polling plus the confirmed event-driven migration direction.
- Run: fresh Codex evaluator with a separately isolated, newly generated `without_skill` baseline.

## Latest Result

**PASS** — all 4 assertions passed. The response recognizes an `existing-project-update`, explains the delta and blast radius first, prefers `change-impactor` plus targeted iteration, and names every affected document path.

## With-Skill Behavior

- Preserved the confirmed `hybrid transition` and the rejected permanent polling-only option instead of silently reopening decision history.
- Mapped impact to `DECISIONS.md`, PM PRD, Engineer TRD, and later QA coverage.
- Routed Engineer TRD revision to `engineer-agent:trd-gen` and avoided full regeneration.
- Advanced only the fallback user-behavior decision.

## Without-Skill Baseline

- Source: fresh isolated subagent run using the same prompt and fixture without the target skill, PM Agent README, internal instructions, or historical comparison.
- The baseline also identified a targeted update and the three main documents, but did not name `change-impactor`, `prd-iteration`, or the dependency-ordered lifecycle route.

## Failures

- No assertion failures or baseline blockers.
- PR #163's Docs deployment-completeness closeout did not apply to this feature update and caused no regression.

## Next Steps

- Keep this eval as coverage for decision-history preservation and targeted update routing.
- Re-run when impact analysis, iteration ownership, or Docs closeout rules change.

## Runtime Artifacts Policy

- Responses, verdicts, timing, and diagnostics remain under `tmp/eval-runs/idea-to-spec-v0.3.4/` and are not committed.
