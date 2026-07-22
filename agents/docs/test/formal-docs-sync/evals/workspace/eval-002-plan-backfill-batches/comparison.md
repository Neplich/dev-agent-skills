# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-002-plan-backfill-batches`
- Mode / type: `existing-system backfill` / Product

## Test Set / Fixture Version

- Fixture version: `issue-160 product information architecture v1`
- Evidence: confirmed two-domain catalog, backfill confirmation, current Product implementation, and acceptance tests
- Fresh run: `tmp/eval-runs/issue-160-run-a/product/`
- Actual validation date: `2026-07-22`

## Latest Result

**PASS（with-skill 6/6；fresh without-skill 6/6）** — with-skill generated a
navigable seven-page Product tree for two domains, kept invitations as a
two-level feature with two independent task pages, mapped both code globs,
passed host checks, and prepared the #117 handoff. The baseline also satisfied
all assertions, so this fixture proves availability but no assertion-level
uplift.

## Assertions

- `creates_complete_product_tree`: PASS. Product root, two domain indexes,
  invitations index, and three task pages were generated; invite and accept
  remain separate.
- `keeps_every_task_navigable`: PASS. Every task is reachable from the root and
  each index is limited to scope, roles, relationships, and navigation.
- `writes_evidence_backed_task_behavior`: PASS. Permissions, the three-pending
  limit, duplicate/expired/invalid feedback, recovery actions, dashboard role,
  empty state, and retry all match implementation and acceptance evidence.
- `updates_product_map_atomically`: PASS. Workspace-management and analytics
  globs map to their corresponding complete subtrees and ancestor root.
- `links_authorities_without_copying_contracts`: PASS. Task pages link parent,
  Design, API, Database, and Ops authorities without duplicating contracts or
  creating role-based duplicate trees.
- `runs_product_host_checks`: PASS. The fresh judge reran
  `GITHUB_BASE_SHA=HEAD npm run test:docs`: exit `0`, 74/74 Node tests; all
  pages remain `unverified` and the #117 pre-tag step waits for a maintainer-
  confirmed target version.

## With-Skill Behavior

- Loaded only the Product type module after the common contract.
- Preserved both catalog owners and made roles, adjacent domains, exclusions,
  and reader tasks explicit in non-leaf indexes.
- Stably sorted change-map globs and required docs.
- Kept the page/index/link/map batch atomic and returned a version-context
  blocked #117 pre-tag handoff rather than stamping a version.

## Fresh Without-Skill Baseline

- Source: independent pristine copy with the same eval definition, prompt, and
  fixture; it contained no `.eval-skill`, old comparison, with-skill output, or
  historical baseline.
- Result: 6/6 PASS. Its indexes had weaker role/exclusion detail, its map was
  not stably sorted, and its #117 blocked semantics were less explicit, but
  those differences did not fail the current assertions.
- The baseline final response mentioned generic PM/Docs routing; directory and
  hash evidence showed no access to the target `formal-docs-sync` skill.

## Failures

- With-skill assertion failures: none.
- Without-skill assertion failures: none.
- Non-blocking harness note: plain `npm run test:docs` exited `1` because the
  synthetic inner repository has only one root commit and cannot infer
  `HEAD^1`. The judge independently reran with explicit
  `GITHUB_BASE_SHA=HEAD`; strict affected checks still included working-tree
  and untracked candidate pages and passed 74/74.

## Next Steps

- Keep this PASS. A future differentiation-focused fixture may seed unknown
  change-map fields and unrelated entries, require stable sorting explicitly,
  or introduce evidence that tempts role-duplicated trees or contract copying.
- The eval harness should set an explicit base for single-commit synthetic
  repositories.

## Runtime Artifact Policy

- Both lanes, candidate outputs, installed dependencies, judge verdict, logs,
  and isolated rerun copies remain under `tmp/eval-runs/issue-160-run-a/` or
  ephemeral `/tmp` and are not submitted.
- Only this `comparison.md` is durable; no `with_skill/`, `without_skill/`,
  transcript, candidate output, verdict, timing, run status, diagnostics,
  `node_modules`, generated site, or cache is committed.
