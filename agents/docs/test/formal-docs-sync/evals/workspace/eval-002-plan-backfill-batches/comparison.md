# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-002-plan-backfill-batches`
- Mode / type: `existing-system backfill` / API

## Test Set / Fixture Version

- Fixture version: `issue-159 API information architecture review 8 standards refresh`
- Standards refresh: the fixture now uses the current packaged
  `docs/site/standards/doc-granularity.md`,
  `docs/site/standards/templates/api-template.md`, and
  `docs/site/standards/templates/database.md`; catalog, change map, existing
  API pages, routes, schemas, and tests remain the eval's host-scenario data.
- Evidence: confirmed Accounts/Billing catalog, Accounts route/schema/contract
  tests, existing nested Billing API subtree, and seeded Billing change-map
  entry with `exclude` plus unknown `review_policy`.
- Fresh run: `tmp/eval-runs/issue-159-review8-eval002-ELZH4E/`
- Generation method: independent pristine fixture copies without historical
  comparison; both lanes received the same eval prompt and assertions. Only
  with-skill read and applied the Docs Agent, current `formal-docs-sync` API
  contracts, and the refreshed host standards. A third fresh Codex judge read
  both final responses, fixture evidence, and recursive SHA-256 manifests.
- Actual validation date: `2026-07-22`

## Latest Result

**PASS（with-skill 5/5；fresh without-skill 3/5）** — with-skill consumed the
refreshed host standards and proposed the complete
`api/index.md → accounts/index.md → get-account.md` subtree. It supplied every
required per-node confirmation field, treated all three pages and the Accounts
seed as one atomic candidate scope, preserved the existing Billing mapping
fields, and stopped before writes. The fresh judge found no infrastructure
blocker.

## Assertions

- `prefers_catalog_scope`: both PASS. Both selected Accounts from the catalog,
  verified the referenced paths, preserved owner `identity-team`, and kept the
  existing nested Billing subtree out of batch.
- `presents_batch_before_write`: with-skill PASS; without-skill FAIL.
  With-skill paired every root/domain/leaf node with its parent, path, owner,
  code boundary, evidence, map delta, exclusions, and out-of-batch scope before
  waiting for confirmation. The baseline showed the correct tree but did not
  provide a change-map delta and explicit out-of-batch scope for every node.
- `keeps_unconfirmed_batch_read_only`: both PASS. Both stopped before changing
  Accounts pages, the API root, Billing pages, or `change-map.yaml`, and neither
  treated the explicit backfill request as candidate-scope confirmation.
- `aligns_seed_with_page`: with-skill PASS; without-skill FAIL. With-skill's
  Accounts seed covers the API root, Accounts index, and route leaf, keeps the
  page/index/map scope atomic, and explicitly preserves the Billing trigger,
  exclude, and unknown `review_policy`. The baseline correctly preserved
  Billing but invented unsupported
  `review_policy: identity-owner-approval` for Accounts.
- `handles_missing_catalog_semantically`: both PASS. Both keep discovery
  bounded to one top-level route group, form a complete ancestor-index-to-leaf
  subtree from route/schema/handler/test evidence, and wait for confirmation.

## With-Skill Behavior

- Loaded the Docs Agent entry context, `formal-docs-sync` common contract, only
  the API type module, and the fixture's refreshed standards entry,
  granularity rules, API template, and change map.
- Applied the refreshed host rules rather than bypassing them: root/domain
  indexes contain scope and navigation, one route receives one leaf, and the
  complete navigable subtree and map seed remain atomic.
- Proposed a directly auditable per-node confirmation matrix and preserved all
  seeded Billing mapping fields without inventing an Accounts review policy.
- Stopped at candidate-scope confirmation with zero writes, no host checks, no
  second batch, and no premature docs-audit handoff.

## Fresh Without-Skill Baseline

- Source: a second independent pristine fixture copy with the same eval prompt
  and assertions; it did not read the target skill, Docs Agent README,
  internal/shared instructions, historical comparison, with-skill output, or
  other eval outputs.
- Result: 3/5 PASS. It selected the correct nested Accounts tree, respected the
  batch boundary, remained read-only, and handled missing-catalog discovery
  semantically.
- It failed the skill-specific per-node confirmation completeness and proposed
  an Accounts review-policy value unsupported by the fixture evidence.

## Failures

- With-skill assertion failures: none.
- Without-skill assertion failures: `presents_batch_before_write` and
  `aligns_seed_with_page`.
- Infrastructure blockers: none. Recursive SHA-256 manifest comparisons
  confirmed both lane workspaces were byte-identical to the source fixture and
  to each other, excluding the intentionally omitted durable comparison.

## Next Steps

- Keep eval-002's standards copies synchronized with the packaged bootstrap
  assets whenever API/database information-architecture rules change.
- Re-run this paired validation whenever API hierarchy, candidate-scope, host
  standards consumption, or change-map atomicity rules change.

## Runtime Artifact Policy

- Both copied lanes, final responses, fresh judge verdict, and session/runtime
  evidence remain under
  `tmp/eval-runs/issue-159-review8-eval002-ELZH4E/` and are not submitted.
- Only this `comparison.md` is durable; no `with_skill/`, `without_skill/`,
  transcript, verdict, timing, run status, diagnostics, dependency, generated
  site, cache artifact, or other runtime output is committed.
