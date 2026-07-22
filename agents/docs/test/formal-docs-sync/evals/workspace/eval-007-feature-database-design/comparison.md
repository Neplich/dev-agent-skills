# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-007-feature-database-design`
- Mode / types: feature delivery / Database + Design

## Test Set / Fixture Version

- Fixture version: `issue-160 design information architecture v1`
- Evidence: Approved PRD, Confirmed TRD, closed plan, actual diff, four passed
  tests, schema, invitation service, membership repository, and audit writer
- Fresh run: `tmp/eval-runs/issue-160-run-a/design/`
- Actual validation date: `2026-07-22`

## Latest Result

**PASS（with-skill 8/8；fresh without-skill 5/8）** — with-skill passed every
page-level closeout gate, generated two Design domains, three component pages,
one cross-component authoritative flow and one boundary page, maintained
reciprocal and API/Database authority links, closed the atomic change-map tree,
and passed host checks. The baseline produced strong content but missed three
skill-specific governance assertions.

## Assertions

- `loads_only_database_design_contracts`: PASS. The lane loaded the standards,
  granularity, change map, Database/Design templates, and only those two type
  modules; API remained a link target.
- `passes_design_closeout_gate`: PASS. All nine changed Design pages, including
  root and compatibility pages, were checked against the same seven-item
  completion evidence chain before writing.
- `synchronizes_database_current_state`: PASS. The authority page records the
  unique workspace-user pair, allowed roles, required timestamp, logical
  references, and absence of physical foreign keys.
- `creates_domain_component_flow_tree`: PASS. Design root, Workspace Access and
  Audit Log indexes, three components, invitation-acceptance flow, authorization
  boundary, and flat-path compatibility entry were created or updated.
- `keeps_reciprocal_and_authority_links`: PASS. All three components link the
  flow, the flow links them back, and Design links API/Database authority pages
  without copying full contracts.
- `keeps_cross_domain_authority_unique`: PASS. Invitation acceptance has one
  authority page under Workspace Access; Audit Log links it without duplication.
- `updates_atomic_map_and_unverified_pages`: PASS. Invitation, repository,
  schema, service, and audit globs include corresponding leaf pages and required
  ancestor indexes while preserving the unrelated manual entry; all 11 changed
  formal pages remain `unverified`.
- `runs_host_checks_and_handoffs_audit`: PASS. The fresh judge reran
  `GITHUB_BASE_SHA=HEAD npm run test:docs`: exit `0`, 74/74 tests, followed by
  a complete #117 affected-set handoff that waits for confirmed release context.

## With-Skill Behavior

- Applied the Design Delivery Closeout Gate to every actual Design write rather
  than only leaf pages.
- Kept the old flat Design URL as a compatibility entry and repaired root/domain
  navigation in the same confirmed scope.
- Preserved one cross-domain authority and reciprocal component-flow links.
- Included the necessary Design root, domain, and Database indexes in the
  page-specific atomic change-map closure.

## Fresh Without-Skill Baseline

- Source: independent pristine copy with the same eval definition, prompt, and
  fixture; it contained no target skill, Docs README, old comparison,
  with-skill output, or historical baseline.
- Result: 5/8 PASS. It produced correct Database facts, hierarchy, links,
  authority boundaries, compatibility entry, and 74/74 host checks.
- Failures: it did not load the Database/Design type modules, reported closeout
  for only 7 of 9 changed Design pages, and omitted required ancestor indexes
  from several change-map entries.

## Failures

- With-skill assertion failures: none.
- Without-skill assertion failures:
  `loads_only_database_design_contracts`, `passes_design_closeout_gate`, and
  `updates_atomic_map_and_unverified_pages`.
- Non-blocking harness note: the synthetic inner repository needed explicit
  `GITHUB_BASE_SHA=HEAD`; the judge independently reran strict affected checks
  and all 74 Node tests successfully.

## Next Steps

- Keep this PASS and retain page-level closeout plus ancestor-index map closure
  as one regression unit.
- A future deterministic assertion may compare the actual changed Design page
  set with the page-gate matrix and mechanically require ancestor indexes for
  every mapped leaf.

## Runtime Artifact Policy

- Both lanes, candidate outputs, installed dependencies, judge verdict, logs,
  and isolated rerun copies remain under `tmp/eval-runs/issue-160-run-a/` or
  ephemeral `/tmp` and are not submitted.
- Only this `comparison.md` is durable; no `with_skill/`, `without_skill/`,
  transcript, candidate output, verdict, timing, run status, diagnostics,
  `node_modules`, generated site, or cache is committed.
