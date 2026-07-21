# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-site-bootstrap`
- Eval: `eval-002-repeat-bootstrap-idempotent`
- Review context: issue #155 fresh paired eval

## Test Set / Fixture Version

- Fixture: `issue-122-assets-v2-c5r`
- Scope: 9 materialized targets; all omitted targets are explicitly assumed present and byte-identical to the current 40-file inventory
- Dependency fact under review: the representative `package.json` VitePress declaration is pinned exactly to `1.6.4`
- Actual validation date: `2026-07-22`

## Latest Result

**PASS (3/3 assertions)** — the fresh with-skill repeat classification preserved every representative target, the existing manifest dispositions, and the original `createdAt` with zero content changes.

## Assertions

- `produces_zero_diff`: PASS. All nine materialized targets compared byte-identical to packaged assets; before/after SHA-256 sets matched and `createdAt` remained `2026-07-16T08:00:00+08:00`.
- `reports_skipped_identical`: PASS. The nine representative paths remain persisted as `skipped-identical` in the existing manifest.
- `preserves_existing_state`: PASS. `standards/change-map.yaml`, `.meta/releases.json`, standards pages, templates, package metadata, manifest, and all other fixture content remained unchanged.

## With-Skill Behavior

- Source: fresh issue #155 with-skill lane under `tmp/eval-runs/issue-155/with_skill/eval-002`, using the current target skill and internal inventory rules with the same eval prompt and copied minimal fixture.
- Applied the 40-file inventory and persistent manifest rules while honoring the fixture's explicit omitted-target byte-equivalence assumption.
- Exact comparisons for all nine materialized targets returned equal; manifest read-back preserved all nine `skipped-identical` dispositions and the original timestamp.
- The representative package declares VitePress exactly as `1.6.4` and remained byte-identical to the current packaged asset.
- The fixture intentionally omits scripts, the lockfile, and most of the complete site, so host tests and builds are not applicable. Validation used exact asset comparisons, manifest parsing, and before/after content hashes; no complete-host checks are claimed.

## Fresh Without-Skill Baseline

- Source: a newly spawned independent issue #155 baseline worker using the same prompt and copied fixture, with the target skill, Docs README, internal instructions, old comparisons, and with-skill output prohibited.
- Result: `PARTIAL / NO-OP`. It used the fixture's omitted-target assumption and existing manifest to preserve all content and report zero target changes, but it had no bootstrap runner or complete inventory source and therefore did not claim a real repeat execution.
- No historical baseline was reused. Its no-op evidence is directionally consistent with the three assertions, while the skill supplied the authoritative inventory and persistent-disposition semantics needed for a complete PASS.

## Failures

- No with-skill assertion failures or blocked checks.
- Host docs tests and builds are not applicable to this deliberately minimized fixture because the scripts, lockfile, and full site are not materialized.
- The baseline's missing runner and inventory source limit it to `PARTIAL`; this does not affect the complete with-skill byte and manifest evidence.

## Next Steps

- Retain this PASS. Re-run if the inventory, representative targets, omitted-target assumption, dependency declaration, or manifest disposition rules change.

## Runtime Artifact Policy

- Runtime copies, checksums, and baseline reports remain under `tmp/eval-runs/issue-155/` and are not submitted.
- Only this durable comparison is retained; no runtime output, dependency directory, generated site, transcript, candidate, verdict, timing, or diagnostics are committed.
