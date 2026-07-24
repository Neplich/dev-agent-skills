# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-002-plan-backfill-batches`
- Mode / types: `existing-system backfill` / API + Product

## Test Set / Fixture Version

- Fixture version: `issue-164 API information architecture + issue-160 Product information architecture union`
- Evidence: confirmed Accounts/Billing API catalog, two-domain Product catalog,
  implementation and acceptance tests covering allowed roles, limits, duplicate
  invitations, invalid/expired tokens, empty state and retry, plus seeded
  unrelated change-map entries with `exclude` and unknown fields
- Fresh paired run:
  `tmp/eval-runs/pr-165-final-fresh-20260723-1215/eval-002-r3/`
- Generation method: both generators received the same eval prompt and pristine
  fixture. Only with-skill received the common contract and scoped API/Product
  modules. Neither generator received assertions, historical comparison, an old
  baseline or the other lane's output. A fresh independent `codex exec` judge
  applied all 14 assertions after generation and reran Product acceptance tests
  in both completed lanes.
- Actual validation date: `2026-07-23`

## Latest Result

**PASS（with-skill 14/14；fresh without-skill 7/14）** — with-skill preserved
the confirmed Product hierarchy and existing Billing material, kept the
unconfirmed Accounts batch read-only, produced the required parent/child batch
proposal, updated the Product mappings atomically, and blocked #117 audit until
a maintainer confirms `target_release_version`.

## Assertions

- `loads_scoped_api_product_contracts`: with-skill PASS；without-skill FAIL。
  Only with-skill applied the common contract and scoped API/Product modules.
- `prefers_catalog_scope`: both PASS. Both selected Accounts as the first
  catalog-backed API batch and excluded Billing from that proposal.
- `presents_batch_before_write`: with-skill PASS；without-skill FAIL。
  With-skill presented the full three-level candidate tree and per-node parent,
  owner, precise `src/api/accounts/**` glob, evidence, mapping delta, exclusions
  and confirmation gate. The baseline used the over-broad `src/api/**` boundary
  for the API root and omitted its explicit parent field.
- `keeps_unconfirmed_batch_read_only`: both PASS. Neither lane wrote Accounts
  pages or map entries, and both preserved the existing API root, Billing pages
  and Billing map entry while updating only the confirmed Product mappings.
- `aligns_seed_with_page`: both PASS. Both aligned the proposed Accounts seed
  with the three-page candidate closure and preserved Billing map metadata.
- `handles_missing_catalog_semantically`: both PASS. Both proposed bounded API
  discovery and a maintainer confirmation gate rather than repository-wide
  generation.
- `creates_complete_product_tree`: both PASS. Both generated the seven-page
  Product tree without collapsing the two invitation tasks.
- `keeps_every_task_navigable`: with-skill PASS；without-skill FAIL。Both lanes
  keep every task reachable, but the baseline Invitations index repeats task
  permissions and limits instead of remaining a scope-and-navigation index.
- `records_confirmed_non_leaf_scope`: with-skill PASS；without-skill FAIL。
  With-skill recorded audience/roles, both catalog owners, child navigation,
  adjacent capabilities and exclusions on every non-leaf Product page. The
  baseline Product root retained the generic docs owner and its Analytics index
  omitted the applicable audience/roles.
- `writes_evidence_backed_task_behavior`: both PASS. Permissions, limits,
  feedback, recovery, valid/invalid/expired states, dashboard result states and
  retry behavior in both lanes match the final implementation and acceptance
  evidence without claiming real email delivery.
- `updates_product_map_atomically`: with-skill PASS；without-skill FAIL。
  With-skill gives each Product glob its complete, stable Product and linked
  authority closure with exclusions. The baseline omits authority pages and
  exclusions and does not keep the glob/doc lists stably ordered.
- `links_authorities_without_copying_contracts`: both PASS. Task pages link
  parent and cross-type authorities without duplicating their contracts.
- `runs_product_host_checks`: with-skill PASS；without-skill FAIL。Both lanes
  passed 74/74 docs tests and both builds, but only with-skill recorded each
  required command with its `docs/site/` cwd and exit status while keeping all
  seven Product pages `unverified`.
- `blocks_audit_without_confirmed_version`: with-skill PASS；without-skill FAIL。
  Only with-skill explicitly blocked pre-tag audit pending a maintainer-confirmed
  `target_release_version`.

## With-Skill Behavior

- Loaded the common eight-step contract and only the scoped API/Product modules.
- Preserved the existing Billing subtree and map metadata while keeping the
  proposed Accounts batch at zero writes until whole-batch confirmation.
- Generated the full Product tree with evidence-backed task behavior, complete
  non-leaf scope and stable atomic mappings.
- Kept the #117 pre-tag audit handoff blocked instead of inferring a version.

## Fresh Without-Skill Baseline

- Source: a new pristine fixture copy with the same prompt and fixture. It did
  not read or apply the target skill, old comparison, with-skill output or any
  historical baseline.
- Result: 7/14 PARTIAL. It preserved Billing, kept Accounts read-only and
  generated seven Product pages, but failed scoped contract loading, the exact
  API proposal boundary, index-content separation, complete non-leaf Product
  scope, atomic Product/authority mapping, complete host-check reporting and the
  missing-version audit gate.
- Skill-specific uplift: +7 assertions, or +50.0 percentage points.

## Required Test Reproduction

- The independent judge ran
  `PYTHONPATH=. UV_CACHE_DIR=<isolated-cache> uvx --from pytest pytest -q tests/acceptance/test_product_tasks.py`
  in both completed lanes; each returned `2 passed`.
- The judge also reran `npm run test:docs`, `npm run build:public` and
  `npm run build:internal` in both lanes. Each lane passed 74/74 docs tests and
  both builds with exit code 0; all Product and linked authority pages resolved
  in both views without dead links.

## Failures

- With-skill assertion failures: none.
- Without-skill assertion failures: `loads_scoped_api_product_contracts`,
  `presents_batch_before_write`, `keeps_every_task_navigable`,
  `records_confirmed_non_leaf_scope`, `updates_product_map_atomically`,
  `runs_product_host_checks`, and `blocks_audit_without_confirmed_version`.
- The isolated pytest cache downloaded its missing Pygments dependency, then
  both lanes completed with the same command and selector.

## Next Steps

- Keep the API proposal/read-only assertions and Product hierarchy/mapping
  assertions together as the merged regression unit.
- Keep seeded Billing and unrelated map entries so preservation of exclusions
  and unknown fields remains observable.
- Keep the explicit read-only candidate-loading rule so API candidate planning
  uses the API module without gaining write authorization.

## Runtime Artifact Policy

- Both lanes, candidate outputs, dependencies, judge verdict, logs and disposable
  rerun copies remain under `tmp/eval-runs/` or `/tmp` and are not submitted.
- Only this `comparison.md` is durable; no `with_skill/`, `without_skill/`,
  transcript, verdict, timing, diagnostics, dependency, generated-site or cache
  artifact is committed.
