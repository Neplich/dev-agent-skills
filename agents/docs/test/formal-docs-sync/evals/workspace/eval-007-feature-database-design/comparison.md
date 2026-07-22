# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-007-feature-database-design`
- Mode / types: feature delivery / Database + Design

## Test Set / Fixture Version

- Fixture version: `issue-164 Database information architecture + issue-160 Design information architecture union`
- Evidence: approved PRD, confirmed TRD, closed implementation plan, actual diff,
  executable fixture tests, schema, invitation service, membership repository,
  audit writer, stable-path seed and unrelated manual mapping
- Fresh paired run:
  `tmp/eval-runs/pr-165-rebase-20260722-232227/eval-007/`
- Generation method: both generators received the same eval prompt and pristine
  fixture. Only with-skill received the common contract and Database/Design type
  modules; a fresh independent `codex exec` judge applied the exact 12 assertion
  semantics without adding stronger per-glob API requirements.
- Actual validation date: `2026-07-22`

## Latest Result

**PASS（with-skill 12/12；fresh without-skill 5/12）** — with-skill passed the
Design closeout gate before writing, refreshed the stable Database path and
complete nested subtree, maintained reciprocal authority links and per-glob
atomic mapping closure, and produced the complete #117 docs-audit handoff.

## Assertions

- `loads_only_database_design_contracts`: with-skill PASS；without-skill FAIL。
  Only with-skill loaded and applied the common, Database and Design modules.
- `passes_design_closeout_gate`: with-skill PASS；without-skill FAIL。
  With-skill's runtime-only `sync-report.md` records the pre-write changed-path
  state and the seven closeout checks for all nine proposed Design pages; the
  baseline has no equivalent evidence.
- `creates_database_schema_domain_tree`: both PASS. Both generated the Database
  root, Primary system, workspace-access domain, relationships and three entity
  pages with hierarchical navigation.
- `refreshes_confirmed_stable_path`: with-skill PASS；without-skill FAIL。
  Both refreshed the stable page's old facts, but only with-skill preserved it
  in the broad seed while appending the complete confirmed nested subtree.
- `documents_current_entity_facts`: both PASS. Both accurately documented
  fields, owners, indexes, lifecycle, membership constraints and invitation
  token/expiry facts.
- `links_relationships_bidirectionally`: with-skill PASS；without-skill FAIL。
  With-skill's relationship and entity pages link both ways and every entity
  links the feature-level Workspace Access API authority; the baseline does not.
- `distinguishes_physical_and_logical_relations`: both PASS. Both distinguish
  the two CASCADE workspace foreign keys from the service-validated logical user
  reference in prose and Mermaid.
- `creates_domain_component_flow_tree`: both PASS. Both generated the Design
  root, two domains, three components, invitation-acceptance flow,
  authorization boundary and compatible flat entry.
- `keeps_reciprocal_and_authority_links`: with-skill PASS；without-skill FAIL。
  Both link components and flow reciprocally, but only with-skill also links the
  required stable Database authority without copying its contract.
- `keeps_cross_domain_authority_unique`: both PASS. The cross-domain flow has
  one authoritative page and Audit Log links to it rather than duplicating it.
- `updates_atomic_map_and_unverified_pages`: with-skill PASS；without-skill FAIL。
  With-skill preserves the manual entry, expands the stable broad seed to the
  full subtree, and gives each invitation, repository/schema and audit glob its
  corresponding leaf or compatibility pages, affected ancestors, reciprocal
  pages and Database authority. The baseline's closures remain incomplete.
- `runs_host_checks_and_handoffs_audit`: with-skill PASS；without-skill FAIL。
  Both report successful docs tests and public/internal builds, but only
  with-skill supplies the explicit `docs-agent:docs-audit` #117 handoff with the
  complete affected set, evidence and version blocker.

## With-Skill Behavior

- Loaded only the common contract plus Database and Design type modules.
- Captured the nine-page Design closeout matrix before any formal-page or
  change-map write and kept the report runtime-only.
- Refreshed the stable Database page, built the full schema/domain/entity tree,
  and generated the confirmed Design domain/component/flow hierarchy.
- Preserved reciprocal links, unique cross-domain authority and complete atomic
  mappings while retaining unrelated manual-map fields.
- Passed 74/74 docs tests plus public/internal builds and prepared the complete
  #117 handoff, blocked only on an unconfirmed `target_release_version`.

## Fresh Without-Skill Baseline

- Source: a new pristine fixture copy with the same prompt and fixture. It did
  not read or apply the target skill, old comparison, with-skill output or any
  historical baseline.
- Result: 5/12 PARTIAL. It produced accurate entity facts, the main Database and
  Design trees, physical/logical relation semantics and unique flow authority,
  but failed seven contract-specific closeout, linking, mapping and handoff
  assertions.
- Skill-specific uplift: +7 assertions, or +58.3 percentage points.

## Required Test Reproduction

- Both generators ran `npm run test:docs`: exit `0`, Node `74 passed, 0 failed`.
- Both generators ran and passed `npm run build:public` and
  `npm run build:internal`; generated internal routes include all nested Database
  pages and public navigation excludes internal Database/Design pages.
- The independent judge performed read-only route, sidebar, link, frontmatter,
  mapping, timestamp and handoff checks. The judge did not rerun build commands
  that would modify `.generated`.
- Generator-side pytest reproduction was unavailable because pytest could not
  be installed in the isolated environment; the confirmed fixture test evidence
  remained an input fact and this was not an assertion failure.

## Failures

- With-skill assertion failures: none.
- Without-skill assertion failures: `loads_only_database_design_contracts`,
  `passes_design_closeout_gate`, `refreshes_confirmed_stable_path`,
  `links_relationships_bidirectionally`,
  `keeps_reciprocal_and_authority_links`,
  `updates_atomic_map_and_unverified_pages`, and
  `runs_host_checks_and_handoffs_audit`.

## Next Steps

- Keep the stable-path expansion, per-glob mapping closure and pre-write Design
  closeout evidence together as the merged Database/Design regression unit.
- Keep the unrelated manual mapping and broad `src/workspace_access/**` seed so
  unknown-field preservation and full subtree expansion remain observable.

## Runtime Artifact Policy

- Both lanes, dependencies, candidate outputs, judge verdict, logs and temporary
  test/build products remain under `tmp/eval-runs/` or `/tmp` and are not
  submitted.
- Only this `comparison.md` is durable; no `with_skill/`, `without_skill/`,
  transcript, verdict, timing, diagnostics, dependency, generated-site or cache
  artifact is committed.
