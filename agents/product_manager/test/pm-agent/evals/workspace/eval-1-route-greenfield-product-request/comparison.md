# Eval Result: pm-agent-route-greenfield-product-request

## Evaluation Target

- Skill: `pm-agent`
- Test case: route-greenfield-product-request
- Test set: dispatcher availability evals
- Entry: workspace `eval-1-route-greenfield-product-request`
- Latest result: PASS

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: empty-workspace product idea request

## With Skill

- Routes the empty-workspace product idea to `idea-to-spec`.
- Preserves the PM-first boundary before design or engineering execution.
- Names the expected PM documents and downstream handoff points.

## Without Skill / Baseline

- May jump directly to project scaffolding or implementation planning.
- Less consistently separates PM discovery from engineering execution.

## Failures

- None recorded.

## Next Steps

- Keep this eval for PM dispatcher route coverage.

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, and diagnostics should not be committed.
