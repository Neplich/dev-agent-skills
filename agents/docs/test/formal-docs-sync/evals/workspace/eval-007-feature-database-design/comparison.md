# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-007-feature-database-design`
- Review context: issue #159 database/schema/domain/entity information architecture

## Test Set / Fixture Version

- Fixture: current pristine `workspace/eval-007-feature-database-design` snapshot for issue #159
- Evidence set: confirmed handoff and candidate scope, Approved PRD, Confirmed TRD/plan, complete closeout, actual diff, passed tests, schema, repository, service, API page, and host standards
- Actual validation date: `2026-07-22`
- Isolation: fresh `codex exec` copied the same fixture into independent lanes; start manifests matched with a zero-byte diff, and historical comparisons were excluded

## Latest Result

**PASS (9/9 assertions)** — the with-skill lane produced the complete database/schema/domain/entity subtree, relationship overview, bidirectional links, explicit physical-versus-logical relation semantics, delivered design page, and atomic map update.

## Assertions

- `loads_only_database_design_contracts`: PASS. The output applies only the confirmed database/design rules and host entry/map contracts.
- `passes_design_closeout_gate`: PASS. Approved PRD, Confirmed TRD/plan, complete scope, diff coverage, passed tests, and confirmed candidate scope were verified before writing.
- `creates_database_schema_domain_tree`: PASS. Database root, `primary` schema index, Workspace Access domain index, relationship overview, and three entity/table pages exist and are linked.
- `documents_current_entity_facts`: PASS. Fields, checks, unique constraints, expiry, indexes, ownership, and lifecycle match current schema and access evidence.
- `links_relationships_bidirectionally`: PASS. The Mermaid overview links all entity pages; every entity links its domain, relationship page, related entities, and API page.
- `distinguishes_physical_and_logical_relations`: PASS. Both `workspace_id` cascade foreign keys are physical, while `user_id` is explicitly a service-validated logical reference without a foreign key.
- `synchronizes_delivered_design`: PASS. The design page documents workspace/user validation before repository upsert and excludes inherited or future roles.
- `updates_atomic_map_and_unverified_pages`: PASS. The sorted eight-page map entry, preserved manual entry, complete changed set, and `unverified` frontmatter were verified.
- `runs_host_checks_and_handoffs_audit`: PASS. Required commands passed; internal navigation contains every nested page, public navigation excludes internal database/design pages, and the #117 handoff is complete.

## With-Skill Behavior

- Applied the database/schema/data-domain/entity hierarchy, index/leaf separation, bidirectional relation links, and physical/logical relation contract.
- Synchronized the complete subtree and its exact change-map mapping in one batch while preserving unrelated content.
- Ran `npm ci --ignore-scripts`, `npm run test:docs` (74/74), `npm run build:public`, and `npm run build:internal`; all exited `0`.

## Fresh Without-Skill Baseline

- Source: freshly regenerated from the same prompt and identical pristine fixture; it did not read the target skill, Docs Agent README, internal instructions, old comparison, or with-skill output.
- The explicit prompt and fixture encoded enough hierarchy, relationship, closeout, and host-check detail for the baseline to pass all 9 assertions and the same four host commands.
- No behavioral advantage over the baseline was observed in this fixture; this result proves current skill availability but has weak comparative discrimination.

## Failures

- No assertion, runner, network, credential, dependency-install, or build failure.
- `npm audit` reported 3 existing advisories (2 moderate, 1 high), but all required commands exited `0`.
- Builds emitted non-blocking directory-link asset warnings; VitePress rendered successfully, and route, sidebar, and visibility isolation checks passed.

## Next Steps

- Keep this hierarchy and relationship regression. A future eval refinement can reduce prompt-prescribed output or add conflicting/ambiguous evidence that exercises skill-specific gates more strongly.

## Runtime Artifact Policy

- Source copies, both lanes, installed dependencies, generated sites, candidate outputs, logs, run records, and judge verdict remain under `tmp/eval-runs/issue-159-20260722-1915/`.
- Only this comparison is durable; no transcript, runtime output, verdict, timing, diagnostics, `node_modules`, or generated site is submitted.
