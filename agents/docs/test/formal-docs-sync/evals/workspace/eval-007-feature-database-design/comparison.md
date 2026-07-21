# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-007-feature-database-design`
- Review context: issue #150 fresh paired eval group A

## Test Set / Fixture Version

- Fixture: pristine `workspace/eval-007-feature-database-design` snapshot used by issue #150
- Evidence set: confirmed feature handoff, Approved PRD, Confirmed TRD/plan, closeout, actual diff, passed test record, schema, repository, service, and tests
- Actual validation date: `2026-07-21`

## Latest Result

**PASS (6/6 assertions)** — the with-skill lane passed all seven design-closeout checks, atomically synchronized database/design current state and their shared map entry, passed host checks, and handed off #117.

## Assertions

- `loads_only_database_design_contracts`: PASS. This eval loaded the standards entry, change map, database/design host templates, and only the database/design type modules.
- `passes_design_closeout_gate`: PASS. Approved PRD, Confirmed TRD, confirmed plan, all-complete scope, full diff coverage, all required tests passed, and maintainer-confirmed candidate scope were checked before writes.
- `synchronizes_database_current_state`: PASS. The page records the unique workspace-user pair, three allowed roles, required timestamp, and application-validated logical references without inventing foreign keys.
- `synchronizes_delivered_design`: PASS. The page shows workspace then user validation before repository upsert and explicitly excludes inherited roles.
- `updates_atomic_map_and_unverified_pages`: PASS. The two pages and `src/workspace_access/**` required-doc list were updated/read back as one scope, stably ordered, and both pages remain `unverified`.
- `runs_host_checks_and_handoffs_audit`: PASS. `npm run test:docs` exited `0` with 74/74 Node tests passing, followed by a complete-set `docs-agent:docs-audit` (#117) handoff.

## With-Skill Behavior

- Applied database and design evidence contracts without loading API, ops, or product rules for this eval.
- Pristine comparison shows exactly three intended content deltas: the database page, design page, and shared change-map entry; all unrelated docs and manual map fields remained unchanged.
- The #117 handoff is ready for content audit but pre-tag stamping remains blocked until a maintainer confirms `target_release_version`.
- The runtime Git wrapper isolated the fixture from the outer worktree's exact tag while preserving all other Git-backed affected checks.

## Fresh Without-Skill Baseline

- Source: fresh `without_skill` lane from the same pristine fixture and prompt/assertions; it did not read the target skill, Docs README, internal instructions, old comparison, or with-skill output.
- The strong fixture let the baseline produce correct database/design pages and map, keep both pages unverified, and pass host checks.
- It did not load the type-specific host contracts or explicitly prove all seven design-closeout gates before writing; baseline result: PARTIAL (4/6 assertions).

## Failures

- No with-skill assertion failures.
- Dependency installation reported 3 audit advisories but did not fail installation or host checks; they are outside this eval's assertions.

## Next Steps

- Keep this PASS. Continue treating the seven-item design closeout, atomic page/map update, host checks, and confirmed-version audit gate as one regression unit.

## Runtime Artifact Policy

- Both runtime lanes, installed dependencies, edited pages, test output, and isolation tooling remain under `tmp/eval-runs/issue-150/group-a/`.
- Only this comparison is durable; no runtime output, transcript, candidate, verdict, timing, diagnostics, `node_modules`, or generated site is submitted.
