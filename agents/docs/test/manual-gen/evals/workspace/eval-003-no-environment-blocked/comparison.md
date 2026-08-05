# Skill Eval Comparison

## Evaluation Target

- Skill: `manual-gen`
- Eval: `eval-003-no-environment-blocked`
- Target behavior: report a truthful blocker when neither environment path is usable and create no fabricated interface evidence

## Test Set / Fixture Version

- Fixture version: `manual-gen-v0.1.1`
- Environment fixture: domain unavailable; local startup explicitly refused; no existing screenshots
- Validation status: not executed as of `2026-08-05`

## Latest Result

- Behavior result: `BLOCKED` — no with-skill lane, fresh without-skill baseline, or independent judge has run.
- Coverage result: `PARTIAL` — `reports_environment_blocker`, `does_not_start_or_capture`, `does_not_invent_interface_evidence`, and `keeps_manual_surfaces_zero_write` are all `NOT EXERCISED`.
- Blocking reason: fresh subagent validation and the same-run fresh without-skill baseline are pending.

Overall result: BLOCKED

## With-Skill Behavior

- Not observed. The future lane must name the unavailable evidence and owner, remain blocked, and make no environment, screenshot, manual, navigation, or change-map mutation.
- No blocked report or zero-diff result is treated as verified until an independent reviewer checks the lane workspace.

## Fresh Without-Skill Baseline

- Source: pending fresh baseline from the same prompt and pristine fixture, without reading or applying `manual-gen`, the Docs Agent README, or historical lane output.
- Behavior summary: unavailable until that baseline completes; no historical baseline may substitute for this run.

## Failures

- Behavior failures: none recorded because the eval has not run.
- Infrastructure blocker: fresh with-skill, without-skill, and independent review lanes have not been executed.

## Next Steps

- Run both isolated lanes and record command evidence plus start/end workspace manifests.
- Have an independent fresh reviewer confirm the blocked semantics, missing-evidence report, zero writes, and absence of fabricated or example imagery before updating this file.

## Runtime Artifact Policy

- Lane workspaces, outputs, manifests, transcripts, verdicts, timing, status, diagnostics, generated pages, and images belong only in an isolated `tmp/eval-runs/...` workspace.
- Only this `comparison.md` and `eval_metadata.json` are durable; runtime artifacts must not be committed.
