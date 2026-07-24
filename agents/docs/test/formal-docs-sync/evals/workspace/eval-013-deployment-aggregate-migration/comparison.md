# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-013-deployment-aggregate-migration`
- Review context: issue #161 fresh paired rerun and fresh Codex judge

## Test Set / Fixture Version

- Fixture: legacy aggregate deployment page, inbound links, three-class evidence summary and old change map
- Actual validation date: `2026-07-22`

## Latest Result

**PASS (4/4 assertions)** — the fresh with-skill lane removed the aggregate page, migrated shared/class facts, repaired links/navigation/maps without data loss, and passed `npm run test:docs` with 2/2 tests. The fresh judge independently reran the check.

## With-Skill Behavior

- Moved shared `APP_PORT` facts to the environment authority, repaired Ops/Product inbound links, split maps by class and preserved `exclude`, unknown fields and unrelated entries.
- Limited the migration to evidence retained by the fixture; it did not invent image, Chart, values or exact command child pages from a summary.
- Kept changed pages `unverified` and returned the #117 handoff blocked on a confirmed target version.

## Fresh Without-Skill Baseline

- Source: fresh lane from the same pristine fixture and prompt without the target skill, Agent README, comparisons or with-skill output.
- It also passed 2/2 structural migration tests, but used broader unsupported phrases such as a current Chart, approved workflow and previous Helm revision; with-skill maintained the stricter evidence boundary.

## Failures

- No with-skill assertion failures.
- Runtime provenance used lane transcripts and reports; a separate immutable input manifest was not retained.

## Next Steps

- Keep this PASS; require a new confirmed batch with source-level evidence before adding detailed image/Chart/values pages.

## Runtime Artifact Policy

- Paired lanes, transcripts, reports, generated pages and judge verdict remain under `tmp/eval-runs/issue-161-rerun/` and are not submitted.
- Only this comparison is durable.
