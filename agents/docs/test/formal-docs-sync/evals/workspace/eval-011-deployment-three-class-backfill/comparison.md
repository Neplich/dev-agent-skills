# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-011-deployment-three-class-backfill`
- Review context: issue #161 fresh paired rerun and fresh Codex judge

## Test Set / Fixture Version

- Fixture: issue #161 three-class deployment evidence set after template-consumer and recursive-link corrections
- Actual validation date: `2026-07-22`

## Latest Result

**PASS (5/5 assertions)** — the fresh with-skill lane generated the complete three-class tree, evidence-backed shared environment reference, per-class maps and navigation, and passed `npm run test:docs` with 3/3 tests. The fresh judge independently reran the check.

## With-Skill Behavior

- Cross-checked env examples, settings/tests, Compose, values and actual template consumers; treated `LEGACY_TIMEOUT` and unconsumed values explicitly instead of inventing runtime mappings.
- Kept Development, Docker and Kubernetes/Helm commands, images, rollback and troubleshooting separate; all class indexes link their authoritative child pages.
- Preserved unrelated/unknown map data, left pages `unverified`, and returned the #117 handoff blocked on a confirmed target version.

## Fresh Without-Skill Baseline

- Source: fresh lane from the same corrected pristine fixture and prompt; it did not read the target skill, Agent README, comparisons or with-skill output.
- It passed 3/3 structural tests, but its environment table omitted required contract fields, treated Helm `service.port` as `APP_PORT`, treated an unconsumed value as effective, and omitted the formal #117 handoff.

## Failures

- No with-skill assertion failures.
- Runtime provenance used lane transcripts and reports; a separate immutable input manifest was not retained.

## Next Steps

- Keep this PASS and retain the stricter internal-link test and template-consumer evidence boundary.

## Runtime Artifact Policy

- Paired lanes, transcripts, reports, generated pages and judge verdict remain under `tmp/eval-runs/issue-161-rerun/` and are not submitted.
- Only this comparison is durable.
