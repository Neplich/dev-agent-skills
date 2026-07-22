# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-002-plan-backfill-batches`
- Mode / type: `existing-system backfill` / Product

## Test Set / Fixture Version

- Fixture version: `issue-160 product information architecture v2`
- Evidence: confirmed two-domain catalog, implementation, acceptance tests, and a seeded unrelated change-map entry with `exclude` plus an unknown field
- Fresh run: `tmp/eval-runs/pr-165-review-fix-20260722-200100/product/`
- Generation method: both generators received the same eval prompt and pristine
  fixture and were expressly prohibited from reading the staged `evals.json` or
  assertions; only with-skill received the target contract. The independent
  judge read the assertions after generation.
- Actual validation date: `2026-07-22`

## Latest Result

**PASS（with-skill 9/9；fresh without-skill 5/9）** — both lanes generated the
confirmed seven-page Product tree, but with-skill additionally preserved the
atomic ancestor mapping and stable ordering, recorded auditable host-check
evidence, and blocked pre-tag audit until a maintainer confirms the target
version. The baseline failed four skill-specific assertions, including three
observable output and handoff behaviors.

## Assertions

- `loads_only_product_contract`: with-skill PASS; without-skill FAIL. Only the
  with-skill lane had and applied the common contract and Product module; no
  other type module was available.
- `creates_complete_product_tree`: both PASS. Product root, two domain indexes,
  invitations index, and three independent task pages were generated.
- `keeps_every_task_navigable`: both PASS. Every task is reachable from the
  root, while indexes remain navigation and scope pages.
- `records_confirmed_non_leaf_scope`: both PASS. Across the non-leaf pages,
  audience, catalog owner, children, adjacent capabilities, and exclusions are
  retained.
- `writes_evidence_backed_task_behavior`: both PASS. Permissions, limits,
  feedback, recovery, empty state, and retry match code and acceptance tests.
- `updates_product_map_atomically`: with-skill PASS; without-skill FAIL.
  With-skill stably sorts globs and `required_docs`, includes Product root and
  necessary ancestor indexes, and preserves the seeded unrelated entry,
  `exclude`, and `review_policy`; the baseline is unsorted and omits the root
  from both mappings.
- `links_authorities_without_copying_contracts`: both PASS. Task pages link the
  parent and cross-type authority entries without duplicating contracts.
- `runs_product_host_checks`: with-skill PASS; without-skill FAIL. Disposable
  copies both passed 74/74 Node tests and all pages remain `unverified`, but the
  baseline did not record cwd and explicit exit status as required evidence.
- `blocks_audit_without_confirmed_version`: with-skill PASS; without-skill FAIL.
  With-skill's #117 handoff contains the affected set, evidence, exclusions,
  and covered batch and states that pre-tag audit cannot begin before a
  maintainer confirms `target_release_version`; the baseline closes as complete
  without that gate.

## With-Skill Behavior

- Loaded the common eight-step contract and only the Product type module.
- Preserved the confirmed domain-feature-task hierarchy and non-leaf scope
  semantics.
- Stably sorted change-map globs and document lists while preserving unknown
  data.
- Kept the pre-tag audit handoff blocked instead of inferring a version.

## Fresh Without-Skill Baseline

- Source: a new pristine fixture copy with the same eval prompt, metadata, and
  seeded map. Its generation prompt expressly prohibited reading the staged
  `evals.json` or assertions, which were applied only by the independent judge
  after generation; it did not contain or read the target skill, old
  comparison, with-skill output, or historical baseline.
- Result: 5/9 PARTIAL. It creates the full tree and accurate task content, but
  fails contract loading, stable and atomic mapping, auditable host-check
  recording, and the missing-version audit gate.
- Skill-specific uplift: +4 assertions, or +44.4 percentage points; three of
  the four gains are observable generated-output or handoff behaviors.

## Failures

- With-skill assertion failures: none.
- Without-skill assertion failures: `loads_only_product_contract`,
  `updates_product_map_atomically`, `runs_product_host_checks`, and
  `blocks_audit_without_confirmed_version`.
- The single-commit fixture required `GITHUB_BASE_SHA=HEAD`; strict affected
  checks still included working-tree and untracked candidate pages.

## Next Steps

- Keep the module-access, confirmed non-leaf scope, stable-map, and blocked
  handoff assertions together as the Product backfill regression unit.
- Keep the seeded unrelated map entry so unknown-field and exclusion
  preservation remain observable.

## Runtime Artifact Policy

- Both lanes, candidate outputs, dependencies, judge verdict, logs, and
  disposable rerun copies remain under `tmp/eval-runs/` or `/tmp` and are not
  submitted.
- Only this `comparison.md` is durable; no `with_skill/`, `without_skill/`,
  transcript, verdict, timing, diagnostics, dependency, generated-site, or
  cache artifact is committed.
