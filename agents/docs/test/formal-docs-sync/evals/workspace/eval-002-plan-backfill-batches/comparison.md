# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-002-plan-backfill-batches`
- Mode / types: `existing-system backfill` / API + Product

## Test Set / Fixture Version

- Fixture version: `issue-164 API information architecture + issue-160 recursive Product information architecture`
- Product evidence: two product domains; Workspace Management contains
  `invitations` as a Level 1 feature, `member-invitations` and
  `invitation-acceptance` as Level 2 features, and three independently tested
  task leaves; Analytics remains a shallow domain with one task leaf.
- API evidence: confirmed Accounts/Billing catalog and an unconfirmed
  Accounts candidate subtree with an existing protected Billing subtree.
- Fresh paired run:
  `tmp/eval-runs/pr-165-multilevel-final-clean-20260723-170550/eval-002/`
- Generation method: both generators received the same core prompt and new
  pristine fixture. Only with-skill received the Docs Agent, common contract,
  and API/Product modules. Neither generator received assertions, this
  comparison, an earlier lane, or the other lane's output.
- Judge method: a new independent `codex exec` judge first read the current 14
  assertions after generation, inspected both actual workspaces, reran Product
  acceptance tests and all host commands, and parsed the generated
  public/internal sidebar trees and local links.
- Actual validation date: `2026-07-23`

## Latest Result

**PASS（with-skill 14/14；fresh without-skill 9/14）** — with-skill generated
the complete two-level Product feature tree, kept every task reachable through
five structurally nested sidebar levels, preserved the read-only Accounts and
Billing surfaces, retained independently complete Product mapping closures,
and blocked #117 pre-tag audit until a maintainer confirms
`target_release_version`.

## Assertions

- `loads_scoped_api_product_contracts`: with-skill PASS；without-skill FAIL。
  Only with-skill loaded and applied the common, API, and Product contracts.
- `prefers_catalog_scope`: both PASS. Both selected Accounts and kept Billing
  out of the candidate batch.
- `presents_batch_before_write`: with-skill PASS；without-skill FAIL。
  With-skill used the Accounts boundary for every candidate node; the baseline
  used the over-broad `src/api/**` boundary for the API root.
- `keeps_unconfirmed_batch_read_only`: both PASS. Neither lane wrote Accounts
  or changed protected API/Billing surfaces.
- `aligns_seed_with_page`: both PASS. Both proposed the complete three-page
  Accounts closure and preserved Billing metadata.
- `handles_missing_catalog_semantically`: both PASS. Both proposed bounded API
  discovery followed by confirmation.
- `creates_complete_product_tree`: both PASS. Both generated the Product root,
  two domain indexes, Invitations, two Level 2 indexes, and four task leaves.
- `keeps_every_task_navigable`: both PASS. Both generated root → domain →
  Level 1 → Level 2 → task sidebar navigation without skipping levels.
- `records_confirmed_non_leaf_scope`: with-skill PASS；without-skill FAIL。
  Only with-skill recorded audience, catalog owner, direct children, adjacent
  capability, and exclusions on every non-leaf node.
- `writes_evidence_backed_task_behavior`: both PASS. Invitation creation,
  pending invitation management, acceptance/recovery, and dashboard states
  match their exact functions and three acceptance tests.
- `updates_product_map_atomically`: both PASS. Each of the five broad/exact
  Product globs independently contains its Product ancestors, applicable task
  leaves, and four authority roots in stable order.
- `links_authorities_without_copying_contracts`: both PASS. All four task pages
  link parent and authority pages without copying contracts.
- `runs_product_host_checks`: with-skill PASS；without-skill FAIL。
  Both lanes passed 76 docs tests and both builds, and their public/internal
  sidebars include all ten Product pages with maximum nesting depth five and
  zero unresolved local links. Only with-skill recorded every command, docs
  site cwd, and final exit status as required by the assertion.
- `blocks_audit_without_confirmed_version`: with-skill PASS；without-skill
  FAIL。Only with-skill explicitly blocked #117 pre-tag work pending a
  maintainer-confirmed target version.

## With-Skill Behavior

- Applied the common eight-step contract and only the scoped API/Product
  modules.
- Generated ten Product pages with an independent `index.md` for every
  non-leaf node and evidence-backed behavior on each task leaf.
- Preserved the seeded per-layer change-map ancestor closures and protected
  Billing/manual entries, while keeping Accounts at zero writes.
- Used the host's arbitrary-depth sidebar generator in both views and kept all
  changed pages `last_verified_version: unverified`.
- Returned the complete #117 affected set but correctly blocked pre-tag audit
  on the missing `target_release_version`.

## Fresh Without-Skill Baseline

- Source: a new pristine fixture copy with the same prompt. It did not read or
  apply the target skill, Agent README, assertions, this comparison, with-skill
  output, or a historical baseline.
- Result: 9/14 PARTIAL. It produced the recursive Product tree and valid
  mappings/pages, but failed scoped skill loading, the exact Accounts root
  proposal boundary, complete non-leaf scope, complete command/cwd/exit
  evidence, and the missing-version audit gate.
- Skill-specific uplift: +5 assertions, or +35.7 percentage points.

## Required Test Reproduction

- The independent judge ran
  `PYTHONDONTWRITEBYTECODE=1 uv run --with pytest python -m pytest tests/acceptance/test_product_tasks.py -q -p no:cacheprovider`
  in both lanes; each returned `3 passed`.
- The judge reran `npm run test:docs`, `npm run build:public`, and
  `npm run build:internal` in both lanes; each returned exit code 0, and each
  docs test run passed 76/76 tests.
- Both generated views contained all ten Product nodes at the expected
  recursive depths, and independent link parsing found zero broken links.

## Failures

- With-skill assertion failures: none.
- Without-skill assertion failures: `loads_scoped_api_product_contracts`,
  `presents_batch_before_write`, `records_confirmed_non_leaf_scope`, and
  `runs_product_host_checks`, and `blocks_audit_without_confirmed_version`.
- Existing VitePress asset and chunk-size warnings were non-blocking; generated
  links and both builds succeeded.

## Next Steps

- Keep the recursive sidebar test and all five mapping closures as regression
  guards for deeper future `feature_path` trees.
- Keep the shallow Analytics domain to prove that recursive support does not
  require every product domain to have the same depth.
- Keep the API read-only candidate and missing-version assertions together with
  the Product hierarchy assertions.

## Runtime Artifact Policy

- Both lanes, dependencies, generated sites, generator events, judge events,
  final outputs, verdict, and diagnostics remain under `tmp/eval-runs/` and are
  not submitted.
- Only this `comparison.md` is durable; no `with_skill/`, `without_skill/`,
  transcript, verdict, timing, diagnostics, generated-site, cache, or run-status
  artifact is committed.
