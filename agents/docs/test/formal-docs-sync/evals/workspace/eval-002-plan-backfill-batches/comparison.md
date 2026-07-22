# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-002-plan-backfill-batches`
- Mode / type: `existing-system backfill` / API

## Test Set / Fixture Version

- Fixture version: `issue-159 API information architecture review 6`
- Evidence: confirmed Accounts/Billing catalog, Accounts route/schema/contract tests, existing nested Billing API subtree, and seeded Billing change-map entry with `exclude` plus unknown `review_policy`
- Fresh run: `/tmp/eval-runs/issue-159-review6-e3v9ny/`
- Generation method: independent pristine fixture copies without historical comparison; both lanes received the same final eval prompt, and only with-skill read the Docs Agent and current `formal-docs-sync` API contracts
- Actual validation date: `2026-07-22`

## Latest Result

**PASS（with-skill 5/5；fresh without-skill 3/5）** — both lanes proposed
`api/index.md → accounts/index.md → get-account.md` instead of the obsolete
flat Accounts page. With-skill additionally supplied the complete per-node
confirmation matrix and preserved the existing Billing mapping fields while
treating the Accounts pages, ancestor index, and map seed as one atomic
candidate scope. A third fresh Codex judge found no infrastructure blocker.

## Assertions

- `prefers_catalog_scope`: both PASS. Both selected Accounts from the catalog,
  verified the listed evidence paths, preserved owner `identity-team`, and kept
  the existing nested Billing subtree out of batch.
- `presents_batch_before_write`: with-skill PASS; without-skill FAIL.
  With-skill paired every root/domain/leaf node with its parent, path, owner,
  code boundary, evidence, map delta, exclusions, and out-of-batch scope before
  waiting for confirmation. The baseline showed the tree but did not provide
  all required fields for each node.
- `keeps_unconfirmed_batch_read_only`: both PASS. Both stopped before changing
  Accounts pages, the API root, Billing pages, or `change-map.yaml`, and neither
  treated the explicit backfill request as candidate-scope confirmation.
- `aligns_seed_with_page`: with-skill PASS; without-skill FAIL. With-skill's
  Accounts seed covers the API root, Accounts index, and route leaf, keeps the
  page/index/map scope atomic, and explicitly preserves the Billing trigger,
  exclude, and unknown `review_policy`. The baseline omitted `exclude`,
  invented an unsupported Accounts review policy, and did not preserve every
  Billing map field explicitly.
- `handles_missing_catalog_semantically`: both PASS. Both keep discovery
  bounded and wait for confirmation; with-skill explicitly derives a complete
  ancestor-index-to-route-leaf subtree from route prefix/tag, schema, handler
  ownership, and contract-test evidence.

## With-Skill Behavior

- Loaded the Docs Agent entry context, `formal-docs-sync` common contract, and
  only the API type module.
- Proposed the complete Accounts domain/index/route-leaf tree with a directly
  auditable per-node confirmation matrix.
- Preserved all seeded Billing mapping fields and proposed stable, exact
  Accounts `required_docs` for the complete subtree.
- Stopped at candidate-scope confirmation with zero writes, no host checks, no
  second batch, and no premature docs-audit handoff.

## Fresh Without-Skill Baseline

- Source: an independent pristine fixture copy with the same final eval prompt;
  it did not read the target skill, Docs Agent README, historical comparison,
  with-skill output, or other eval outputs.
- Result: 3/5 PASS. It derived the correct nested Accounts tree, respected the
  batch boundary, remained read-only, and handled missing-catalog discovery
  semantically.
- It failed the skill-specific per-node candidate matrix and conservative,
  atomic change-map preservation assertions.

## Failures

- With-skill assertion failures: none.
- Without-skill assertion failures: `presents_batch_before_write` and
  `aligns_seed_with_page`.
- Infrastructure blockers: none. Both lane workspaces remained byte-identical
  to the pristine source fixture, excluding the intentionally omitted durable
  comparison.

## Next Steps

- Keep the existing nested Billing subtree and unknown-field seed in the
  fixture so future API information-architecture regressions remain visible.
- Re-run this paired validation whenever API hierarchy, candidate-scope, or
  change-map atomicity rules change.

## Runtime Artifact Policy

- Both lanes, final responses, fresh judge verdict, session logs, and copied
  fixtures remain under `/tmp/eval-runs/issue-159-review6-e3v9ny/` and are not
  submitted.
- Only this `comparison.md` is durable; no `with_skill/`, `without_skill/`,
  transcript, verdict, timing, run status, diagnostics, dependency, generated
  site, or cache artifact is committed.
