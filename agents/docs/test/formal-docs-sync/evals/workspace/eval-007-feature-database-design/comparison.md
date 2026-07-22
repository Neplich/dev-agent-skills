# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-007-feature-database-design`
- Review context: PR #164 fifth-review pristine stable-page fixture repair

## Test Set / Fixture Version

- Fixture: current pristine `workspace/eval-007-feature-database-design` snapshot after the PR #164 fifth-review repair; the stable page starts at verified `v0.9.0` with stale duplicate-membership, arbitrary-role, and physical-user-FK claims, while the confirmed write scope requires an in-place current-fact refresh or redirect and still excludes deletion, movement, and migration
- Evidence set: confirmed handoff and candidate scope, Approved PRD, Confirmed TRD/plan, complete closeout, actual diff, passed test record, schema, repository, service, API page, stable database path, change-map entry, and host standards
- Actual validation date: `2026-07-22`
- Isolation: fresh `codex exec` copied the same fixture without historical comparison into independent with-skill and without-skill lanes; a third fresh read-only `codex exec` judge checked both final workspaces, logs, and generated navigation

## Latest Result

**PASS (10/10 assertions; 10.0/10)** — the with-skill lane retained the stable `docs/site/database/workspace-access.md` path and mapping while actually replacing the pristine `v0.9.0` stale facts with current evidence, generated the complete database/schema/domain/entity subtree, preserved every page's visibility, and passed all content, navigation, host-check, and handoff assertions.

## Assertions

- `loads_only_database_design_contracts`: PASS. The lane loaded the host standards/map and only the database/design type modules.
- `passes_design_closeout_gate`: PASS. Approved PRD, Confirmed TRD/plan, complete scope, diff coverage, passed test evidence, and confirmed candidate scope were verified before writing.
- `creates_database_schema_domain_tree`: PASS. Database root, `primary` schema index, Workspace Access domain index, relationship overview, and three entity/table pages exist and are linked.
- `refreshes_confirmed_stable_path`: PASS. The pristine stable page started with `last_verified_version: v0.9.0` and stale duplicate-membership, arbitrary-role, and physical-user-FK claims. The lane produced an actual content diff, kept the path and change-map mapping, changed the page to `unverified`, and replaced those claims with current unique-membership, constrained-role, physical-workspace-FK, logical-user-reference, and invitation facts.
- `documents_current_entity_facts`: PASS. Fields, checks, unique constraints, expiry, indexes, ownership, and lifecycle match current schema and access evidence.
- `links_relationships_bidirectionally`: PASS. The Mermaid overview links all entity pages; every entity links its domain, relationship page, related entities, and API page.
- `distinguishes_physical_and_logical_relations`: PASS. Both `workspace_id` cascade foreign keys are physical, while `user_id` is explicitly a service-validated logical reference without a foreign key.
- `synchronizes_delivered_design`: PASS. The design page documents workspace/user validation before repository upsert and excludes inherited or future roles.
- `updates_atomic_map_and_unverified_pages`: PASS. The stable page plus new subtree are merged in stable path order, the unrelated manual entry is preserved, and all changed pages remain `unverified`.
- `runs_host_checks_and_handoffs_audit`: PASS. Required commands passed; internal navigation contains every nested and stable internal database/design page, public navigation excludes them, no visibility was changed to satisfy checks, and the #117 handoff is complete.

## With-Skill Behavior

- Applied the database/schema/data-domain/entity hierarchy, conditional relationship-page contract, stable-path migration safeguard, current-fact replacement rule, and physical/logical relation rules.
- Preserved the stable path and mapping without preserving stale content; retained the existing trigger, exclusion, and unrelated mapping fields.
- Ran `npm run test:docs` (74/74), `npm run build:public`, and `npm run build:internal`; all exited `0`.
- Verified navigation by target: public contains only `public`/`both`, while internal contains `public`/`internal`/`both`; page visibility remained unchanged.

## Fresh Without-Skill Baseline

- Source: freshly regenerated from the same prompt and identical pristine fixture; it did not read the target skill, Docs Agent README, internal/shared skill instructions, historical comparison, or with-skill output.
- The baseline retained and actually refreshed the stable path from the same stale `v0.9.0` fixture, produced the database/design subtree, maintained the map, passed the three host commands, generated correct visibility-filtered navigation, and completed the #117 handoff. It no longer receives the stable-page assertion for merely leaving an already-current file untouched.
- The fresh judge rated the baseline 9.5/10: all general delivery assertions passed, including `refreshes_confirmed_stable_path`; only target-module loading was partial because the baseline was forbidden from reading the formal-docs-sync database/design type modules.

## Failures

- With-skill: no assertion, host-check, build, navigation, or handoff failure.
- Without-skill: no general delivery failure; target-module loading was partial by baseline design.
- Non-blocking: with-skill first encountered missing installed dependencies, then completed deterministic `npm ci` and passed all three required host commands; the baseline also passed all three commands. The fixture's supplied required-test record remained passed, and Python pytest was not rerun in this validation.
- Non-blocking: dependency vulnerability notices and unchanged VitePress resource/asset warnings did not fail tests, links, or either build.

## Next Steps

- Keep the pristine stable page in its verified pre-sync state, and keep candidate confirmation, the stable-path/current-fact assertion, and the visibility-target rule together as regression guards: a no-op must fail the content refresh assertion, confirmed refresh must not imply permission to delete, move, or migrate the path, and each page must remain available only in allowed navigation targets.

## Runtime Artifact Policy

- Source copy, both isolated lanes, installed dependencies, generated sites, candidate outputs, final responses, prompts, and fresh judge verdict remain under `tmp/eval-runs/issue-159-review5-EWIuF7/` and are not submitted.
- Only this `comparison.md` is durable; no transcript, candidate output, verdict, timing, diagnostics, dependency directory, or generated site is tracked.
