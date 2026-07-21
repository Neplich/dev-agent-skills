# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-001-sync-feature-api`
- Review context: issue #150 fresh paired eval group A

## Test Set / Fixture Version

- Fixture: pristine `workspace/eval-001-sync-feature-api` snapshot used by issue #150
- Evidence set: confirmed PM handoff, Approved PRD, Confirmed TRD and plan, actual diff, route/schema source, and contract test
- Actual validation date: `2026-07-21`

## Latest Result

**PASS (5/5 assertions)** — the with-skill lane synchronized only the mapped Search API page from current implementation evidence, preserved unrelated mappings and pages, and kept the changed page unverified.

## Assertions

- `updates_only_mapped_api_doc`: PASS. The only pristine-fixture content delta was `docs/site/api/search.md`; the database page and every unrelated page remained unchanged.
- `extracts_current_api_facts`: PASS. The page records `GET /api/search`, required `q`, optional `limit` with its default and bounds, and HTTP 400 `invalid_query` from route/schema/test evidence.
- `merges_map_without_deleting_unknown`: PASS. The existing `src/api/**` mapping needed no text delta; `plugins/manual/**`, its trigger, and exclude remain intact.
- `keeps_confirmed_type_scope`: PASS. The execution recognized the five-type skill surface but loaded and applied only the host API template and API type module for this confirmed batch.
- `marks_changed_page_unverified`: PASS. The current-state API page has `last_verified_version: unverified` and no release stamp.

## With-Skill Behavior

- Followed the feature-delivery entry chain, standards entry, change map, confirmed one-page candidate scope, API evidence rules, shared frontmatter contract, read-back, checks, and audit handoff sequence.
- Ran `npm ci --ignore-scripts` and `npm run test:docs` in the isolated `docs/site/`; exit status was `0` and 74/74 Node tests passed.
- Handed the complete affected set to `docs-agent:docs-audit` (#117). Pre-tag audit remains blocked until a maintainer confirms `target_release_version`; no version was inferred.
- A runtime-only Git wrapper suppressed only the outer worktree's unrelated exact-tag discovery and delegated all other Git commands, so the isolated fixture's `latest: null` was checked without ancestor-tag contamination.

## Fresh Without-Skill Baseline

- Source: fresh `without_skill` lane from the same pristine fixture and prompt/assertions; it did not read the target skill, Docs README, internal instructions, old comparison, or with-skill output.
- The baseline updated the correct page with accurate API facts, preserved the manual map entry, kept `unverified`, and passed host checks.
- It did not establish the skill's five-type capability boundary and API-only progressive-loading evidence or the version-confirmation semantics of the #117 handoff; baseline result: PARTIAL (4/5 assertions).

## Failures

- No with-skill assertion failures.
- `npm ci` reported 3 dependency audit advisories, but required host checks exited `0`; advisories are outside this eval's sync assertions.

## Next Steps

- Keep this PASS and retain API-only progressive loading, current-code ground truth, `unverified`, and confirmed-version audit gating as a joint regression.

## Runtime Artifact Policy

- Both lanes, installed dependencies, edited fixture copies, test output, and the isolation wrapper remain under `tmp/eval-runs/issue-150/group-a/`.
- Only this comparison is durable; no runtime page, transcript, candidate, verdict, timing, diagnostics, `node_modules`, or build output is submitted.
