# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-007-feature-database-design`
- Mode / types: feature delivery / Database + Design

## Test Set / Fixture Version

- Fixture version: `issue-164 Database information architecture + issue-160 Design information architecture union`
- Evidence: approved PRD, confirmed TRD, closed implementation plan, actual diff,
  seven executable fixture tests with complete result rows, schema, invitation
  service, membership repository, audit writer, stable-path seed and unrelated
  manual mapping
- Fresh paired run:
  `tmp/eval-runs/pr-165-review-consumption-20260723-015600/eval-007/`
- Generation method: both generators received the same eval prompt and pristine
  fixture. Only with-skill received the common contract and Database/Design type
  modules; a fresh independent `codex exec` judge applied the exact 12 assertion
  semantics to both generated workspaces.
- Actual validation date: `2026-07-23`

## Latest Result

**PARTIAL（with-skill 10/12；fresh without-skill 8/12）** — with-skill passed the
Design closeout gate before writing, refreshed the stable Database path and
complete nested subtree, and produced the #117 docs-audit handoff. It did not
fully satisfy the entity-to-API reverse-link requirement or the per-code-glob
atomic ancestor mapping closure.

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
- `refreshes_confirmed_stable_path`: both PASS.
  Both refreshed the stable page's old facts, marked it `unverified`, and kept
  its change-map coverage while preserving the path.
- `documents_current_entity_facts`: both PASS. Both accurately documented
  fields, owners, indexes, lifecycle, membership constraints and invitation
  token/expiry facts.
- `links_relationships_bidirectionally`: both FAIL. Both relationship pages and
  entity pages mostly link in both directions, but `workspace-invitations.md`
  omits the required feature-level Workspace Access API link; the baseline also
  omits it from `workspaces.md`.
- `distinguishes_physical_and_logical_relations`: both PASS. Both distinguish
  the two CASCADE workspace foreign keys from the service-validated logical user
  reference in prose and Mermaid.
- `creates_domain_component_flow_tree`: both PASS. Both generated the Design
  root, two domains, three components, invitation-acceptance flow,
  authorization boundary and compatible flat entry.
- `keeps_reciprocal_and_authority_links`: both PASS. Both link components and
  flow reciprocally and link the invitation API plus stable Database authority
  without copying either contract.
- `keeps_cross_domain_authority_unique`: both PASS. The cross-domain flow has
  one authoritative page and Audit Log links to it rather than duplicating it.
- `updates_atomic_map_and_unverified_pages`: both FAIL. With-skill preserves the
  manual entry, stable ordering and `unverified` pages, but the invitation,
  repository, service and audit globs do not each contain the complete Database
  root, Primary root and data-domain ancestor closure. The baseline also leaves
  incomplete closures and unstable ordering.
- `runs_host_checks_and_handoffs_audit`: both PASS. Both actually passed 74/74
  docs tests and public/internal builds, kept internal-only pages out of public
  navigation, and produced a #117 docs-audit handoff.

## With-Skill Behavior

- Loaded only the common contract plus Database and Design type modules.
- Captured the nine-page Design closeout matrix before any formal-page or
  change-map write and kept the report runtime-only.
- Refreshed the stable Database page, built the full schema/domain/entity tree,
  and generated the confirmed Design domain/component/flow hierarchy.
- Preserved unique cross-domain authority and unrelated manual-map fields, but
  left one required entity-to-API reverse link and several per-glob ancestor
  mapping closures incomplete.
- Passed 74/74 docs tests plus public/internal builds, and prepared the complete
  #117 handoff blocked only on an unconfirmed `target_release_version`.

## Fresh Without-Skill Baseline

- Source: a new pristine fixture copy with the same prompt and fixture. It did
  not read or apply the target skill, old comparison, with-skill output or any
  historical baseline.
- Result: 8/12 PARTIAL. It produced accurate entity facts, the main Database and
  Design trees, stable-path refresh, reciprocal flow/authority links, unique
  flow authority, host-check evidence and a #117 handoff, but failed four
  contract-specific loading, closeout, entity-linking and mapping assertions.
- Skill-specific uplift: +2 assertions, or +16.7 percentage points.

## Required Test Reproduction

- Both generators ran `npm run test:docs`: exit `0`, Node `74 passed, 0 failed`.
- Both generators ran and passed `npm run build:public` and
  `npm run build:internal`; generated internal routes include all nested Database
  pages and public navigation excludes internal Database/Design pages.
- The independent judge ran
  `PYTHONDONTWRITEBYTECODE=1 uv run --with pytest python -m pytest tests/test_workspace_access.py -q -p no:cacheprovider`
  in both lanes; each returned `7 passed in 0.01s`, matching all six required
  implementation-plan rows plus the supplemental supported-role row.
- The judge also performed route, sidebar, link, frontmatter, mapping, timestamp
  and handoff checks without rerunning build commands that would overwrite
  `.generated`.
- The updated harness proves the success sequence
  `find_invitation → mark_consumed → upsert_membership → write_audit`; the
  expired branch stops after lookup with zero membership and audit writes.

## Failures

- With-skill assertion failures: `links_relationships_bidirectionally` and
  `updates_atomic_map_and_unverified_pages`.
- Without-skill assertion failures: `loads_only_database_design_contracts`,
  `passes_design_closeout_gate`, `links_relationships_bidirectionally`, and
  `updates_atomic_map_and_unverified_pages`.

## Next Steps

- Keep the complete required-test result table and pre-write Design closeout
  evidence together as the merged Database/Design regression unit.
- In a separately scoped skill/eval change, make every entity page link the
  feature-level Workspace Access API and make each affected exact code glob
  carry the required Database ancestor closure before expecting 12/12.
- Keep the unrelated manual mapping and broad `src/workspace_access/**` seed so
  unknown-field preservation and full subtree expansion remain observable.

## Runtime Artifact Policy

- Both lanes, dependencies, candidate outputs, judge verdict, logs and temporary
  test/build products remain under `tmp/eval-runs/` or `/tmp` and are not
  submitted.
- Only this `comparison.md` is durable; no `with_skill/`, `without_skill/`,
  transcript, verdict, timing, diagnostics, dependency, generated-site or cache
  artifact is committed.
