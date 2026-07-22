# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-007-feature-database-design`
- Review context: PR #164 fourth-review candidate-scope confirmation repair

## Test Set / Fixture Version

- Fixture: current pristine `workspace/eval-007-feature-database-design` snapshot after the PR #164 fourth-review repair; the confirmed write scope explicitly includes refreshing the stable page to current facts or redirecting it in place, while deletion, movement, and migration remain excluded
- Evidence set: confirmed handoff and candidate scope, Approved PRD, Confirmed TRD/plan, complete closeout, actual diff, passed test record, schema, repository, service, API page, stable database path, change-map entry, and host standards
- Actual validation date: `2026-07-22`
- Isolation: fresh `codex exec` copied the same fixture without historical comparison into independent with-skill and without-skill lanes; a third fresh read-only `codex exec` judge checked both final workspaces, logs, and generated navigation

## Latest Result

**PASS (10/10 assertions)** — the with-skill lane retained the stable `docs/site/database/workspace-access.md` path and mapping while refreshing its confirmed content to current evidence, generated the complete database/schema/domain/entity subtree, preserved every page's visibility, and passed all content, navigation, host-check, and handoff assertions.

## Assertions

- `loads_only_database_design_contracts`: PASS. The lane loaded the host standards/map and only the database/design type modules.
- `passes_design_closeout_gate`: PASS. Approved PRD, Confirmed TRD/plan, complete scope, diff coverage, passed test evidence, and confirmed candidate scope were verified before writing.
- `creates_database_schema_domain_tree`: PASS. Database root, `primary` schema index, Workspace Access domain index, relationship overview, and three entity/table pages exist and are linked.
- `preserves_unapproved_stable_path`: PASS. The stable path and its change-map mapping remain; its content contains only current unique-membership, constrained-role, physical-workspace-FK, logical-user-reference, and invitation facts, with no superseded claims.
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
- The baseline also retained the stable path with current content, produced the database/design subtree, maintained the map, passed the three host commands, and generated correct visibility-filtered navigation.
- The fresh judge rated the baseline 9.0/10: all general delivery assertions passed, while target-module loading was partial because the baseline was forbidden from reading the database/design type modules, and the #117 handoff was partial because it did not explicitly block stamping while waiting for a maintainer-confirmed `target_release_version`.

## Failures

- With-skill: no assertion, host-check, build, navigation, or handoff failure.
- Without-skill: no general delivery failure; target-module loading and the release-context-specific #117 handoff gate were partial.
- Non-blocking: the fixture's supplied required-test record remained passed, and all three required host documentation commands succeeded; Python pytest was not rerun in this validation.
- Non-blocking: dependency vulnerability notices and two unchanged VitePress template placeholder warnings did not fail tests, links, or either build. The with-skill lane removed all target-page link warnings before its final internal build.

## Next Steps

- Keep candidate confirmation, the stable-path/current-fact assertion, and the visibility-target rule together as regression guards: confirmed content refresh must not imply permission to delete, move, or migrate the stable path, and each page must remain available only in allowed navigation targets.

## Runtime Artifact Policy

- Source copy, both isolated lanes, installed dependencies, generated sites, candidate outputs, logs, and fresh judge verdict remain under `tmp/eval-runs/issue-159-review4-zWwkYx/` and are not submitted.
- Only this `comparison.md` is durable; no transcript, candidate output, verdict, timing, diagnostics, dependency directory, or generated site is tracked.
