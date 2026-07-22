# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-002-plan-backfill-batches`
- Mode / types: `existing-system backfill` / API + Product

## Test Set / Fixture Version

- Fixture version: `issue-164 API information architecture + issue-160 Product information architecture union`
- Evidence: confirmed Accounts/Billing API catalog, two-domain Product catalog,
  implementation and acceptance tests, plus seeded unrelated change-map entries
  with `exclude` and unknown fields
- Fresh paired run:
  `tmp/eval-runs/pr-165-rebase-20260722-225436/eval-002/`
- Generation method: both generators received the same eval prompt and pristine
  fixture. Only with-skill received the common contract and scoped API/Product
  modules; a fresh independent `codex exec` judge applied all 14 assertions to
  both completed lanes.
- Actual validation date: `2026-07-22`

## Latest Result

**PASS（with-skill 14/14；fresh without-skill 9/14）** — with-skill preserved
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
  With-skill presented an explicit parent/child tree with per-node owner, glob,
  evidence, mapping and exclusions; the baseline omitted the strict tree and
  parent expression.
- `keeps_unconfirmed_batch_read_only`: both PASS. Neither lane wrote Accounts
  pages or mappings, and both preserved the existing API root and Billing pages.
- `aligns_seed_with_page`: both PASS. Both aligned the proposed Accounts seed
  with the three-page candidate closure and preserved Billing map metadata.
- `handles_missing_catalog_semantically`: both PASS. Both proposed bounded API
  discovery and a maintainer confirmation gate rather than repository-wide
  generation.
- `creates_complete_product_tree`: both PASS. Both generated the seven-page
  Product tree without collapsing the two invitation tasks.
- `keeps_every_task_navigable`: both PASS. All task leaves remain reachable
  through the confirmed root/domain/feature hierarchy.
- `records_confirmed_non_leaf_scope`: with-skill PASS；without-skill FAIL。
  The baseline omitted required audience, catalog-owner, adjacent-capability or
  exclusion facts from non-leaf Product pages.
- `writes_evidence_backed_task_behavior`: both PASS. Permissions, limits,
  feedback, recovery, empty state and retry behavior match the fixture evidence.
- `updates_product_map_atomically`: with-skill PASS；without-skill FAIL。
  With-skill stably sorted both globs and `required_docs`, preserved seeded
  unknown fields, and used the confirmed source naming; the baseline did not.
- `links_authorities_without_copying_contracts`: both PASS. Task pages link
  parent and cross-type authorities without duplicating their contracts.
- `runs_product_host_checks`: both PASS. Both lanes passed 74/74 docs tests and
  kept all seven Product pages `unverified` while producing the #117 handoff.
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
- Result: 9/14 PARTIAL. It preserved Billing, kept Accounts read-only, generated
  seven Product pages and passed host checks, but failed scoped contract loading,
  the strict API proposal tree, complete non-leaf Product scope, stable atomic
  mapping and the missing-version audit gate.
- Skill-specific uplift: +5 assertions, or +35.7 percentage points.

## Failures

- With-skill assertion failures: none.
- Without-skill assertion failures: `loads_scoped_api_product_contracts`,
  `presents_batch_before_write`, `records_confirmed_non_leaf_scope`,
  `updates_product_map_atomically`, and
  `blocks_audit_without_confirmed_version`.
- Judge infrastructure required the available Python 3.12 for fixture behavior
  assertions because the system Python 3.9 cannot parse `str | None`; this did
  not affect either lane's result.

## Next Steps

- Keep the API proposal/read-only assertions and Product hierarchy/mapping
  assertions together as the merged regression unit.
- Keep seeded Billing and unrelated map entries so preservation of exclusions
  and unknown fields remains observable.

## Runtime Artifact Policy

- Both lanes, candidate outputs, dependencies, judge verdict, logs and disposable
  rerun copies remain under `tmp/eval-runs/` or `/tmp` and are not submitted.
- Only this `comparison.md` is durable; no `with_skill/`, `without_skill/`,
  transcript, verdict, timing, diagnostics, dependency, generated-site or cache
  artifact is committed.
