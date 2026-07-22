# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-001-sync-feature-api`
- Review context: issue #159 API nested information architecture

## Test Set / Fixture Version

- Fixture: current pristine `workspace/eval-001-sync-feature-api` snapshot for issue #159
- Evidence set: confirmed backfill scope, feature catalog, route prefixes and tags, handlers, schemas, contract tests, existing stable API page, and host standards
- Actual validation date: `2026-07-22`
- Isolation: fresh `codex exec` copied the same fixture into independent lanes; start manifests matched with a zero-byte diff, and historical comparisons were excluded

## Latest Result

**PASS (6/6 assertions)** — the with-skill lane produced a complete nested API subtree for two functional domains, including the two-level Identity/Sessions branch, exact leaf contracts, recursive navigation, and atomic change-map coverage.

## Assertions

- `creates_complete_nested_api_tree`: PASS. The API root, Identity and Billing domain indexes, Sessions child index, two session route leaves, and invoice route leaf all exist.
- `makes_every_route_navigable_and_complete`: PASS. Parent indexes and generated public/internal sidebars reach each leaf; leaf pages contain method, path, auth, request, response, errors, owner, and direct evidence.
- `maps_code_globs_to_exact_subtrees`: PASS. Billing and Sessions code globs map to separate sorted page sets while existing unknown change-map fields remain intact.
- `uses_evidence_based_split_rules`: PASS. Catalog, route prefix/tag, ownership, and tests support the hierarchy; the existing Search page remains byte-identical.
- `keeps_api_batch_atomic_and_unverified`: PASS. Pages, ancestor navigation, and map entries changed as one complete subtree, and changed pages remain `unverified`.
- `passes_nested_host_navigation_checks`: PASS. Locked install, docs tests, public build, internal build, recursive sidebar checks, and the complete #117 handoff all passed.

## With-Skill Behavior

- Loaded the API type contract and applied the repository's index/leaf responsibilities, lower-kebab-case paths, evidence rules, and full-subtree delivery rule.
- Created two functional domains and one nested subfeature instead of flattening every endpoint under `docs/site/api/*.md`.
- Ran `npm ci --ignore-scripts`, `npm run test:docs` (74/74), `npm run build:public`, and `npm run build:internal`; all exited `0`.

## Fresh Without-Skill Baseline

- Source: freshly regenerated from the same prompt and identical pristine fixture; it did not read the target skill, Docs Agent README, internal instructions, old comparison, or with-skill output.
- The explicit prompt, confirmed tree, and detailed host standards were sufficient for the baseline to pass all 6 assertions and the same four host commands.
- No behavioral advantage over the baseline was observed in this fixture; this result proves current skill availability but has weak comparative discrimination.

## Failures

- No assertion, runner, network, credential, dependency-install, or build failure.
- `npm audit` reported 3 existing advisories (2 moderate, 1 high), but all required commands exited `0`.
- Builds emitted non-blocking warnings because the asset copier treats directory-style Markdown links as non-file asset references; VitePress rendered successfully and generated routes/sidebars were verified.

## Next Steps

- Keep this nested-tree regression. A future eval refinement can reduce prompt-prescribed output or introduce ambiguous evidence so skill-specific scope and split decisions become more discriminative.

## Runtime Artifact Policy

- Source copies, both lanes, installed dependencies, generated sites, candidate outputs, logs, run records, and judge verdict remain under `tmp/eval-runs/issue-159-20260722-1915/`.
- Only this comparison is durable; no transcript, runtime output, verdict, timing, diagnostics, `node_modules`, or generated site is submitted.
