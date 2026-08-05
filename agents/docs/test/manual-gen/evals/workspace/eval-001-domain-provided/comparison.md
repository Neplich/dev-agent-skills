# Skill Eval Comparison

## Evaluation Target

- Skill: `manual-gen`
- Eval: `eval-001-domain-provided`
- Target behavior: use a maintainer-provided domain to produce one bounded, evidence-backed illustrated manual batch without entering the local-start branch, then keep it unverified and return a blocked audit handoff until the maintainer confirms `target_release_version`

## Test Set / Fixture Version

- Fixture version: `manual-gen-v0.1.1`
- Environment fixture: `https://mermaid.live/`, anonymous access, maintainer-provided domain
- Capture script: `scripts/capture-basic-editing.spec.md`
- Validation status: not executed as of `2026-08-05`

## Latest Result

- Behavior result: `BLOCKED` — no with-skill lane, fresh without-skill baseline, or independent judge has run.
- Coverage result: `PARTIAL` — `uses_provided_domain_without_local_start`, `confirms_one_bounded_batch`, `records_viewport_set_and_readback`, `captures_sanitized_product_evidence`, `writes_evidence_bounded_manual`, and `checks_render_and_handoffs_audit` are all `NOT EXERCISED`.
- Blocking reason: fresh subagent validation and the same-run fresh without-skill baseline are pending.

Overall result: BLOCKED

## With-Skill Behavior

- Not observed. A fresh isolated lane must read and apply `manual-gen`, use the provided domain, keep all generated pages and screenshots in scratch space, and stop the docs-audit handoff as blocked because the prompt has no confirmed release version.
- No screenshot, manual page, change-map delta, viewport evidence, host-check result, or handoff is claimed by this durable file.

## Fresh Without-Skill Baseline

- Source: pending fresh baseline from the same prompt and pristine fixture, without reading or applying `manual-gen`, the Docs Agent README, or historical lane output.
- Behavior summary: unavailable until that baseline completes; no historical baseline may substitute for this run.

## Failures

- Behavior failures: none recorded because the eval has not run.
- Infrastructure blocker: fresh with-skill, without-skill, and independent review lanes have not been executed.

## Next Steps

- Run the with-skill lane and regenerate the without-skill baseline from the same pristine fixture.
- Have an independent fresh reviewer compare both outputs and workspace manifests against every assertion, then replace this blocked result with the evidence-backed two-dimensional result.

## Runtime Artifact Policy

- Browser screenshots, generated manual pages, lane workspaces, outputs, manifests, transcripts, verdicts, timing, status, and diagnostics belong only in an isolated `tmp/eval-runs/...` workspace.
- Only this `comparison.md`, `eval_metadata.json`, and the reusable script specification are durable; runtime artifacts must not be committed.
