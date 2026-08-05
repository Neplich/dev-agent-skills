# Skill Eval Comparison

## Evaluation Target

- Skill: `manual-gen`
- Eval: `eval-005-manual-hierarchy`
- Target behavior: express platform, business, and operation semantics while keeping the operation layer reproducible for its target role

## Test Set / Fixture Version

- Fixture version: `manual-gen-v0.1.0`
- Environment fixture: `https://mermaid.live/`, one bounded anonymous diagram-author task batch
- Capture script: `scripts/capture-hierarchy-task.spec.md`
- Validation status: not executed as of `2026-08-05`

## Latest Result

- Behavior result: `BLOCKED` — no with-skill lane, fresh without-skill baseline, or independent judge has run.
- Coverage result: `PARTIAL` — `presents_platform_layer_semantics`, `presents_business_layer_semantics`, `makes_operation_layer_reproducible`, and `keeps_hierarchy_navigable_and_evidence_backed` are all `NOT EXERCISED`.
- Blocking reason: fresh subagent validation and the same-run fresh without-skill baseline are pending.

Overall result: BLOCKED

## With-Skill Behavior

- Not observed. The future lane must adapt hierarchy labels and paths to host evidence while preserving the three required semantic levels.
- No fixed business module name, directory tree, screenshot, manual page, or navigation result is asserted by this durable file.

## Fresh Without-Skill Baseline

- Source: pending fresh baseline from the same prompt and pristine fixture, without reading or applying `manual-gen`, the Docs Agent README, or historical lane output.
- Behavior summary: unavailable until that baseline completes; no historical baseline may substitute for this run.

## Failures

- Behavior failures: none recorded because the eval has not run.
- Infrastructure blocker: fresh with-skill, without-skill, and independent review lanes have not been executed.

## Next Steps

- Run both isolated lanes from the same pristine fixture and capture their proposed and rendered navigation evidence in scratch space.
- Have an independent fresh reviewer judge the three semantic levels, task reproducibility, evidence boundaries, and bounded scope without comparing fixed directory or module names.

## Runtime Artifact Policy

- Screenshots, generated manuals, rendered sites, lane workspaces, outputs, manifests, transcripts, verdicts, timing, status, and diagnostics belong only in an isolated `tmp/eval-runs/...` workspace.
- Only this `comparison.md`, `eval_metadata.json`, and the reusable script specification are durable; runtime artifacts must not be committed.
