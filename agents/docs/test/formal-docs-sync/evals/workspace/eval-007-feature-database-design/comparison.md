# Eval Comparison: Feature Database + Design Sync

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-007-feature-database-design`
- Mode / types: feature delivery / Database + Design

## Test Set / Fixture Version

- Fixture version: `issue-164 Database information architecture + issue-160 recursive Design information architecture`
- Evidence: Approved PRD, Confirmed TRD, closed implementation plan, actual
  diff, 11 named executable evidence rows / 12 pytest cases, schema, guarded
  invitation creation and consumption, authenticated-user membership
  persistence, real audit writer, stable-path seed, unrelated manual mapping,
  and arbitrary-depth sidebar infrastructure.
- Fresh paired run:
  `tmp/eval-runs/pr-165-multilevel-final-clean-20260723-170550/eval-007/`
- Generation method: both generators received the same prompt and current
  pristine fixture. Only with-skill received the Docs Agent, common contract,
  and Database/Design modules. Neither generator received assertions, this
  comparison, an earlier lane, or the other lane's output. The first
  with-skill attempt stalled on an empty nested-agent receiver before formal
  writes; the scored lane was rebuilt from pristine input with the same core
  prompt and a wrapper clarification that it was already the required fresh
  document-writing subagent.
- Judge method: a new independent `codex exec` judge first read the current 12
  assertions after generation, inspected both actual workspaces, and reran
  fixture pytest, 76 docs tests, both builds, recursive navigation, link, and
  per-glob closure checks.
- Actual validation date: `2026-07-23`

## Latest Result

**PASS（with-skill 12/12；fresh without-skill 6/12）** — with-skill satisfies
all Database/Design hierarchy, current-fact, reciprocal-link, stable authority,
closeout, atomic mapping, recursive navigation, host-check, and #117 handoff
assertions. The arbitrary-depth Design wording and sidebar implementation did
not weaken existing component/flow behavior.

## Assertions

- `loads_only_database_design_contracts`: with-skill PASS；without-skill FAIL。
  Only with-skill loaded the standards entry, granularity, change map, and
  Database/Design modules.
- `passes_design_closeout_gate`: with-skill PASS；without-skill FAIL。
  With-skill captured the nine-page × seven-item matrix before any formal-page
  or map write; the baseline only produced a post-write summary.
- `creates_database_schema_domain_tree`: both PASS. Both generated the full
  Database root/schema/data-domain/relationship/entity tree.
- `refreshes_confirmed_stable_path`: with-skill PASS；without-skill FAIL。
  Both refreshed the stable page, but only with-skill retained it inside the
  broad glob's complete 19-page closure.
- `documents_current_entity_facts`: both PASS. Entity fields, constraints,
  owners, indexes, and lifecycles match schema and code.
- `links_relationships_bidirectionally`: with-skill PASS；without-skill FAIL。
  Only with-skill gave every entity the complete domain/relationship/related
  entity/feature API backlink set.
- `distinguishes_physical_and_logical_relations`: both PASS. Both distinguish
  CASCADE workspace foreign keys from the service-validated logical user
  reference.
- `creates_domain_component_flow_tree`: both PASS. Both generated the Design
  root, two domains, three components, flow, boundary, and compatibility page.
- `keeps_reciprocal_and_authority_links`: both PASS. Component/flow links are
  reciprocal and use stable API/Database authorities.
- `keeps_cross_domain_authority_unique`: both PASS. The shared flow has one
  authority page and Audit Log links to it.
- `updates_atomic_map_and_unverified_pages`: with-skill PASS；without-skill
  FAIL。Only with-skill gives all six participating globs the independently
  complete, stable 19-page closure.
- `runs_host_checks_and_handoffs_audit`: with-skill PASS；without-skill FAIL。
  Both passed host checks and recursive visibility, but only with-skill handed
  the complete set to `docs-agent:docs-audit` and blocked on the missing target
  version.

## With-Skill Behavior

- Loaded the exact common/Database/Design contracts and no unrelated type
  module.
- Preserved pre-write page-level closeout evidence, refreshed the stable
  Database authority, and generated complete nested Database/Design trees.
- Kept entity/relationship and component/flow links reciprocal, with direct
  links to stable API/Database authority pages.
- Applied identical 19-page closures to all six participating broad/exact
  globs and preserved the unrelated manual entry.
- Passed recursive internal navigation at maximum depth four while public
  navigation correctly excluded all internal Database/Design pages.

## Fresh Without-Skill Baseline

- Source: a new pristine fixture copy with the same prompt. It did not read or
  apply the target skill, Agent README, assertions, this comparison, with-skill
  output, or a historical baseline.
- Result: 6/12 PARTIAL. It generated the main page trees and current facts, but
  failed contract loading, pre-write closeout, stable-path subtree mapping,
  entity reverse links, per-glob atomic closure, and the #117 gate.
- Skill-specific uplift: +6 assertions, or +50.0 percentage points.

## Required Test Reproduction

- The judge ran
  `PYTHONDONTWRITEBYTECODE=1 uv run --with pytest python -m pytest tests/test_workspace_access.py -q -p no:cacheprovider`
  in both lanes; each returned `12 passed`.
- It reran `npm run test:docs`, `npm run build:public`, and
  `npm run build:internal`; each lane passed 76/76 docs tests and both builds.
- Internal navigation contained 16 Database/Design routes at maximum depth
  four; public contained zero internal routes. Independent parsing found zero
  broken links.

## Failures

- With-skill assertion failures: none.
- Without-skill assertion failures: `loads_only_database_design_contracts`,
  `passes_design_closeout_gate`, `refreshes_confirmed_stable_path`,
  `links_relationships_bidirectionally`,
  `updates_atomic_map_and_unverified_pages`, and
  `runs_host_checks_and_handoffs_audit`.
- Existing VitePress directory-asset and chunk-size warnings were
  non-blocking; both builds and independent link resolution succeeded.
- The first with-skill infrastructure attempt was not scored: it never reached
  a receiver or formal-page write. Its diagnostic lane remains runtime-only;
  the independent judge verified the final pristine retry and recorded this
  caveat separately from assertion results.

## Next Steps

- Keep arbitrary-depth sidebar generation and its deterministic test shared by
  bootstrap and both hierarchy fixtures.
- Keep the page-level closeout, stable authority, entity backlink, and per-glob
  closure checks together as the Design/Database regression unit.
- Keep the shallow current Design fixture structure; recursive support does not
  require inventing deeper subsystem levels without confirmed ownership
  evidence.

## Runtime Artifact Policy

- Both lanes, dependencies, generated sites, generator events, judge events,
  final outputs, verdict, and diagnostics remain under `tmp/eval-runs/` and are
  not submitted.
- Only this `comparison.md` is durable; no `with_skill/`, `without_skill/`,
  transcript, verdict, timing, diagnostics, generated-site, cache, or run-status
  artifact is committed.
