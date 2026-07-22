# Eval Comparison: Feature Database + Design Sync

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-007-feature-database-design`
- Mode / types: feature delivery / Database + Design

## Test Set / Fixture Version

- Fixture version: `issue-164 Database information architecture + issue-160 Design information architecture union`
- Evidence: Approved PRD, Confirmed TRD, closed implementation plan, actual
  diff, seven executable fixture tests with complete result rows, schema,
  invitation service, membership repository, audit writer, stable-path seed and
  unrelated manual mapping.
- Fresh paired run:
  `tmp/eval-runs/pr-165-eval007-pass-20260723-024628/eval-007/`
- Generation method: both generators received the same eval prompt and pristine
  fixture. Only with-skill received the current common contract and
  Database/Design type modules. Neither generator received assertions,
  historical comparison, an old baseline or the other lane's output.
- Judge method: a fresh independent `codex exec` read the exact 12 assertions
  after generation, inspected both actual workspaces and event logs, and reran
  the required fixture pytest in each lane.
- Actual validation date: `2026-07-23`

## Latest Result

**PASS（with-skill 12/12；fresh without-skill 6/12）** — with-skill satisfies
all Database/Design hierarchy, current-fact, reciprocal-link, authority,
closeout, atomic mapping, host-check and handoff assertions. The fresh baseline
still fails the target skill's standards-entry loading, pre-write page-level
closeout, stable-path subtree mapping, entity reverse-link, per-glob atomic
closure and docs-audit handoff behaviors.

## Assertions

- `loads_only_database_design_contracts`: with-skill PASS；without-skill FAIL。
  With-skill read the standards entry, granularity contract, change map and
  Database/Design templates, then loaded only the common, Database and Design
  modules. The baseline did not read the standards entry or type modules.
- `passes_design_closeout_gate`: with-skill PASS；without-skill FAIL。
  With-skill persisted a runtime-only `sync-report.md` before the first formal
  page write, including timestamp, pre-write state and nine Design pages by
  seven gate items; it was not overwritten. The baseline has no equivalent
  pre-write page-level evidence.
- `creates_database_schema_domain_tree`: both PASS. Both generated the Database
  root, Primary boundary, workspace-access data-domain index, relationship page
  and three entity pages with hierarchical navigation.
- `refreshes_confirmed_stable_path`: with-skill PASS；without-skill FAIL。
  Both refreshed the stable page in place with current facts, but only
  with-skill kept it in the broad mapping while adding the complete confirmed
  Database subtree.
- `documents_current_entity_facts`: both PASS. Both accurately documented
  fields, owners, indexes, lifecycle, membership uniqueness/role constraints
  and invitation token/expiry facts.
- `links_relationships_bidirectionally`: with-skill PASS；without-skill FAIL。
  With-skill's relationship page and every entity page link bidirectionally;
  each entity links the data-domain index, relationship page, related entities
  and feature-level Workspace Access API. The invitation entity also links its
  entity-specific API. The baseline omits several entity and feature-API links.
- `distinguishes_physical_and_logical_relations`: both PASS. Both distinguish
  the two CASCADE workspace foreign keys from the service-validated logical
  user reference in prose and Mermaid.
- `creates_domain_component_flow_tree`: both PASS. Both generated the Design
  root, two domains, three components, invitation-acceptance flow,
  authorization boundary and compatible flat entry.
- `keeps_reciprocal_and_authority_links`: both PASS. Components and flow link
  reciprocally, and Design links the invitation API plus the preserved stable
  Database authority without copying either contract.
- `keeps_cross_domain_authority_unique`: both PASS. The cross-domain flow has
  one authoritative page under workspace-access; Audit Log only references it.
- `updates_atomic_map_and_unverified_pages`: with-skill PASS；without-skill
  FAIL。With-skill gives each of the six affected broad/exact invitation,
  repository/schema, service and audit globs the same independently complete,
  stable 19-page closure: leaves/compatibility pages, changed Database and
  Design roots, all ancestor indexes, reciprocal-link pages and authority
  pages. Shared ancestors are repeated, the unrelated manual entry is
  preserved, and all 17 changed formal pages remain `unverified`. Baseline
  mappings contain only partial local subsets.
- `runs_host_checks_and_handoffs_audit`: with-skill PASS；without-skill FAIL。
  Both passed 74/74 docs tests and public/internal builds with correct recursive
  visibility. Only with-skill explicitly handed the complete affected set to
  `docs-agent:docs-audit` and kept pre-tag stamping blocked on an unconfirmed
  `target_release_version`.

## With-Skill Behavior

- Loaded the exact host and type contracts required by the eval and no unrelated
  API, Ops or Product type module.
- Captured the nine-page Design closeout matrix before any formal-page or
  change-map write and kept it runtime-only.
- Refreshed the stable Database page, built the complete nested Database and
  Design trees, and kept current schema/control-flow facts only.
- Applied explicit write/read-back matrices for all entity links, all three
  Design flow participants plus the flow's stable Database authority, and all
  six per-glob 19-page mapping closures.
- Passed `npm run test:docs` (74/74), public build and internal build, then
  produced the #117 docs-audit handoff.

## Fresh Without-Skill Baseline

- Source: a new pristine fixture copy with the same prompt. It did not read or
  apply the target skill, Agent README, old comparison, with-skill output or a
  historical baseline.
- Result: 6/12 PARTIAL. It produced the main Database/Design trees, current
  entity facts, correct relation semantics, main Design authority structure and
  successful host builds, but failed six skill-specific loading, closeout,
  stable mapping, reverse-link, atomic-closure and handoff behaviors.
- Skill-specific uplift: +6 assertions, or +50 percentage points.

## Stability Rationale

The final result is deterministic rather than an accepted lucky generation:

- the common instructions now require reading the host granularity contract,
  so standards loading is an explicit ordered step;
- the Database module requires a pre-write and post-write row for every entity,
  with feature-level API authority mandatory even when an entity-specific API
  also exists;
- the common, Database and Design modules require each affected code glob to
  carry its own full multi-type closure, explicitly including `src/audit/**`
  and allowing shared ancestors to repeat;
- the Design module requires every participating component and flow to link the
  preserved stable Database authority directly; nested entity/domain links are
  additional and cannot replace it;
- the with-skill generator executed concrete read-back checks for the three
  entity link rows, three components plus the flow, and six identical 19-page
  mapping closures before reporting completion.

These steps directly prevent every omission observed in the prior 10/12 and
intermediate 11/12 runs; the final judge verified the files rather than trusting
the generator summary.

## Required Test Reproduction

- The independent judge ran
  `PYTHONDONTWRITEBYTECODE=1 uv run --with pytest python -m pytest tests/test_workspace_access.py -q -p no:cacheprovider`
  in both lanes; each returned `7 passed in 0.00s` and matched all seven rows in
  `.eval/test-results.md`.
- The harness proves the success sequence
  `find_invitation → mark_consumed → upsert_membership → write_audit`; the
  expired branch stops after lookup with no consume, membership or audit write.
- Both generators ran `npm run test:docs`, `npm run build:public` and
  `npm run build:internal`; all commands exited `0`. Internal navigation contains
  all nested Database/Design pages and public navigation excludes them.

## Failures

- With-skill: none.
- Without-skill: standards-entry loading, pre-write page-level closeout,
  stable-path broad mapping expansion, complete entity reverse links,
  per-code-glob atomic closure, and explicit complete-set docs-audit handoff.
- Non-blocking: locked dependencies report two moderate and one high advisory;
  this eval does not modify dependencies. Existing template asset and VitePress
  chunk-size warnings do not fail links, tests or builds.

## Next Steps

- Keep the explicit entity, stable-authority and per-glob closure read-back
  steps together; removing any one would reopen a reproduced omission class.
- Keep the pristine stable page, unrelated manual mapping and fresh paired
  baseline as regression guards for future `formal-docs-sync` changes.

## Runtime Artifact Policy

- Both lanes, dependencies, generated sites, prompts, event logs, final outputs,
  judge verdict and diagnostics remain under `tmp/eval-runs/` and are not
  submitted.
- Only this `comparison.md` is durable; no `with_skill/`, `without_skill/`,
  transcript, verdict, timing, diagnostics, dependency, generated-site or cache
  artifact is committed.
