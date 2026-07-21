# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-site-bootstrap`
- Eval: `eval-002-repeat-bootstrap-idempotent`
- Review context: issue #150 fresh paired eval group A

## Test Set / Fixture Version

- Fixture: `issue-122-assets-v2-c5r`
- Scope: 9 materialized targets; all omitted targets are explicitly assumed present and byte-identical to the current 40-file inventory
- Actual validation date: `2026-07-21`

## Latest Result

**PASS (3/3 assertions)** — the with-skill repeat classification preserved the existing manifest and host state with zero file-content changes.

## Assertions

- `produces_zero_diff`: PASS. All materialized targets compared byte-identical to packaged assets; no file was rewritten and `createdAt` remained `2026-07-16T08:00:00+08:00`.
- `reports_skipped_identical`: PASS. The nine representative paths remain persisted as `skipped-identical` in the existing manifest.
- `preserves_existing_state`: PASS. `standards/change-map.yaml`, `.meta/releases.json`, standards pages, templates, and all other fixture content remained unchanged.

## With-Skill Behavior

- Applied the 40-file inventory and manifest persistence rules while honoring the fixture's explicit omitted-target equivalence assumption.
- Byte comparisons for the nine materialized targets all returned equal; manifest read-back showed the original timestamp and dispositions.
- The fixture intentionally omits scripts and most of the complete site, so `npm run test:docs` is not executable for this minimal idempotency case. Validation used exact asset comparisons, manifest parsing, and before/after content checks as required by the fixture scope.

## Fresh Without-Skill Baseline

- Source: fresh `without_skill` lane from the same pristine fixture and prompt/assertions; it did not read the target skill, Docs README, internal instructions, old comparison, or with-skill output.
- The baseline also compared the representative assets and preserved the manifest and host state, satisfying 3/3 assertions.
- It did not independently supply the skill's complete persistent-disposition and future-conflict semantics, but that gap did not change this fixture's idempotency result.

## Failures

- No assertion failures or blocked checks.
- Host docs tests are not applicable to this deliberately minimized fixture because its scripts and full package are not materialized.

## Next Steps

- Keep this PASS. Re-run if the inventory, representative targets, omitted-target assumption, or manifest disposition rules change.

## Runtime Artifact Policy

- Runtime copies and byte-comparison output stay under `tmp/eval-runs/issue-150/group-a/` and are not submitted.
- Only this durable comparison is retained; no runtime output, dependencies, transcript, candidate, verdict, timing, or diagnostics are committed.
