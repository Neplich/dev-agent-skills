# Skill Eval Comparison

## Evaluation Target

- Skill: `manual-gen`
- Eval: `eval-002-local-start-consent`
- Target behavior: enter the local-start branch only after the domain path is unavailable and execute zero startup commands before explicit consent

## Test Set / Fixture Version

- Fixture version: `manual-gen-v0.1.0`
- Environment fixture: no domain environment; local-start consent not yet provided
- Validation status: not executed as of `2026-08-05`

## Latest Result

- Behavior result: `BLOCKED` — no with-skill lane, fresh without-skill baseline, or independent judge has run.
- Coverage result: `PARTIAL` — `enters_local_branch_only_after_domain_gap`, `asks_for_explicit_start_consent`, `runs_zero_start_commands_before_consent`, and `keeps_site_and_capture_zero_write` are all `NOT EXERCISED`.
- Blocking reason: fresh subagent validation and the same-run fresh without-skill baseline are pending.

Overall result: BLOCKED

## With-Skill Behavior

- Not observed. The future lane must stop at the explicit local-start consent question and prove that no startup, capture, or site-write command ran.
- This file does not claim a command transcript or zero-diff manifest that has not been independently checked.

## Fresh Without-Skill Baseline

- Source: pending fresh baseline from the same prompt and pristine fixture, without reading or applying `manual-gen`, the Docs Agent README, or historical lane output.
- Behavior summary: unavailable until that baseline completes; no historical baseline may substitute for this run.

## Failures

- Behavior failures: none recorded because the eval has not run.
- Infrastructure blocker: fresh with-skill, without-skill, and independent review lanes have not been executed.

## Next Steps

- Run both isolated lanes from the same fixture and capture start/end manifests plus executed-command evidence.
- Have an independent fresh reviewer verify the branch order, explicit-consent question, zero startup commands, and zero site writes before updating the two-dimensional result.

## Runtime Artifact Policy

- Lane workspaces, command logs, manifests, candidate outputs, transcripts, verdicts, timing, status, and diagnostics belong only in an isolated `tmp/eval-runs/...` workspace.
- Only this `comparison.md` and `eval_metadata.json` are durable; runtime artifacts must not be committed.
