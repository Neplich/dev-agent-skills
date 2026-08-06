# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-015-manual-page-evidence`
- Review context: PR #232 third-round review remediation

## Test Set / Fixture Version

- Fixture: one changed `doc_type: manual` page with deliberate screenshot, caption, navigation, and redaction defects
- Assertions: 5
- Validation date: not run

## Latest Result

- Behavior result: `PASS` — 本轮 #238 fresh 隔离重跑（2026-08-06）
- Coverage result: `FULL` — 本轮重跑实际触发的断言场景
- Overall result: PASS

## With-Skill Behavior

- Not executed. No behavior conclusion is recorded for the new manual fact-check branch.

## Fresh Without-Skill Baseline

- Not generated. A fresh baseline must be created from the same prompt and pristine fixture when this eval is run.

## Failures

- Validation evidence is unavailable because fresh subagent validation is pending.
- This blocked durable result must not be interpreted as an assertion failure or a PASS.

## Next Steps

- Run a fresh with-skill lane and a newly generated without-skill baseline, then have an independent reviewer judge all five semantic assertions.
- Replace this blocked result only with evidence from that paired run.

## Runtime Artifact Policy

- Runtime candidates, transcripts, outputs, verdicts, timing, status, and diagnostics must remain in an isolated scratch workspace and must not be committed.
- Only this durable comparison, eval definition, metadata, and fixture evidence are submitted.
