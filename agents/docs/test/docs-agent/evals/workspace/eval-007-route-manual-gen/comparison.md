# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-agent`
- Eval: `eval-007-route-manual-gen`
- Target behavior: route a screenshot-evidenced illustrated manual request to `manual-gen` without executing its gate

## Test Set / Fixture Version

- Fixture version: `manual-routing-v0.1.0`
- Entry fixture: `manual-handoff.md`
- Validation status: not executed as of `2026-08-05`

## Latest Result

- Behavior result: `BLOCKED` — no with-skill lane, fresh without-skill baseline, or independent judge has run.
- Coverage result: `PARTIAL` — all four routing assertions are `NOT EXERCISED`.
- Blocking reason: fresh subagent validation and the same-run fresh without-skill baseline are pending.

Overall result: BLOCKED

## With-Skill Behavior

- Not observed. The future lane must stop after selecting and pointing to `manual-gen`.

## Fresh Without-Skill Baseline

- Source: pending fresh baseline from the same prompt and pristine fixture without reading or applying docs-agent.
- Behavior summary: unavailable; no historical baseline may substitute.

## Failures

- No behavior failure is recorded because the eval has not run.
- Infrastructure blocker: with-skill, without-skill, and independent review lanes are pending.

## Next Steps

- Run both isolated lanes and have an independent fresh reviewer evaluate every assertion.

## Runtime Artifact Policy

- Candidate outputs, transcripts, manifests, verdicts, timing, status, and diagnostics remain in isolated runtime scratch space and are not committed.
