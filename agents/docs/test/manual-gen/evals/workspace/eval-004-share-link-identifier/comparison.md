# Skill Eval Comparison

## Evaluation Target

- Skill: `manual-gen`
- Eval: `eval-004-share-link-identifier`
- Target behavior: document the real export and share flow while keeping the environment-specific pako payload out of durable text

## Test Set / Fixture Version

- Fixture version: `manual-gen-v0.1.0`
- Environment fixture: `https://mermaid.live/`, anonymous export and share flow
- Capture script: `scripts/capture-export-share.spec.md`
- Validation status: not executed as of `2026-08-05`

## Latest Result

- Behavior result: `BLOCKED` — no with-skill lane, fresh without-skill baseline, or independent judge has run.
- Coverage result: `PARTIAL` — `covers_export_and_share_from_real_ui`, `redacts_share_link_identifier`, `avoids_sensitive_and_side_effect_data`, and `preserves_capture_and_audit_contract` are all `NOT EXERCISED`.
- Blocking reason: fresh subagent validation and the same-run fresh without-skill baseline are pending.

Overall result: BLOCKED

## With-Skill Behavior

- Not observed. The future lane must capture the real flow in scratch space and let the judge inspect all durable text for accidental pako payload disclosure.
- This file contains no share URL, generated payload, screenshot, manual page, or claimed viewport evidence.

## Fresh Without-Skill Baseline

- Source: pending fresh baseline from the same prompt and pristine fixture, without reading or applying `manual-gen`, the Docs Agent README, or historical lane output.
- Behavior summary: unavailable until that baseline completes; no historical baseline may substitute for this run.

## Failures

- Behavior failures: none recorded because the eval has not run.
- Infrastructure blocker: fresh with-skill, without-skill, and independent review lanes have not been executed.

## Next Steps

- Run both isolated lanes against the same live-site snapshot and keep generated share data only in scratch artifacts.
- Have an independent fresh reviewer compare both outputs, scan durable text for the pako payload, and evaluate all capture, privacy, check, and handoff assertions.

## Runtime Artifact Policy

- Screenshots, generated share data, manual pages, lane workspaces, outputs, manifests, transcripts, verdicts, timing, status, and diagnostics belong only in an isolated `tmp/eval-runs/...` workspace.
- Only this `comparison.md`, `eval_metadata.json`, and the reusable script specification are durable; runtime artifacts must not be committed.
