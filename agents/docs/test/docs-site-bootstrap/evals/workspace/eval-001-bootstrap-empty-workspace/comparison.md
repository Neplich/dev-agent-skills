# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-site-bootstrap`
- Eval: `eval-001-bootstrap-empty-workspace`
- Review context: issue #155 fresh paired eval

## Test Set / Fixture Version

- Fixture: pristine empty host from `workspace/eval-001-bootstrap-empty-workspace`
- Historical asset snapshot: 40-file `assets/docs/site/` inventory
- Current contract: 42 packaged assets and six templates
- Dependency fact under review: the VitePress declaration is pinned exactly to `1.6.4` in both `package.json` and the root and resolved entries of `package-lock.json`
- Actual validation date: `2026-07-22`
- Execution cleanup: isolated lane started without `docs/site/`

## Latest Result

**PASS (6/6 assertions)** — the historical fresh with-skill lane created the complete bounded scaffold for the then-current 40-asset, five-template contract, generated and read back a sorted 40-entry manifest, passed the applicable host checks and both site builds with VitePress 1.6.4, and demonstrated a zero-content-diff repeat classification.

Overall result: BLOCKED

## Current Asset-Set Drift

- The retained PASS above is the historical issue #155 result for the former 40-asset, five-template inventory.
- The current packaged asset set contains 42 assets and six templates after adding `standards/templates/manual-guide.md` and `manual/index.md`.
- This changed inventory has not received fresh with-skill, same-run without-skill baseline, and independent judge validation, so the historical PASS does not establish the current result and no current PASS conclusion is claimed.

## Assertions

- `creates_complete_inventory`: PASS. All 40 packaged assets were copied byte-for-byte; manifest parsing returned 40 sorted `created` entries.
- `delivers_deterministic_scaffold_assets`: PASS. `package.json` has exactly one `new:doc`; the scaffold script and test exist; each of five templates has exactly one `docs-scaffold` block and all five are indexed.
- `validates_seven_frontmatter_fields`: PASS. `npm run test:docs` passed the shared frontmatter checker and all 74 Node tests.
- `writes_only_docs_site`: PASS. The generated scaffold and runtime manifest were confined to the isolated `docs/site/` root; evaluation evidence remained outside the generated host root under the issue scratch directory.
- `requires_explicit_opt_in`: PASS. Execution relied on the prompt's explicit host fixture, fixed `docs/site/` root, full scaffold, and manifest authorization; without that entry basis the skill gate stops before writes.
- `reports_manifest_readback`: PASS. The manifest parsed with 40 valid paths and dispositions, and a second full static-content checksum comparison was zero-diff with the original `createdAt` unchanged.

## With-Skill Behavior

- Source: fresh issue #155 with-skill lane under `tmp/eval-runs/issue-155/with_skill/eval-001`, using the current Docs README, target skill, internal inventory protocol, shared frontmatter contract, eval prompt, and pristine fixture.
- Copied 40/40 static assets exactly, created `.meta/bootstrap-manifest.json` with stable sorted paths, and read every generated static target back against its packaged source.
- Confirmed `vitepress: "1.6.4"` in `package.json`, the lockfile root dependency, and the resolved `node_modules/vitepress` record.
- Ran `npm ci`, `npm run test:docs`, `npm run build:public`, and `npm run build:internal`; all exited `0`, and both build logs identified VitePress 1.6.4.
- Reclassified the complete static inventory and compared checksums after host checks; scaffold content and manifest remained zero-diff. Generated `.generated/**` trees and `node_modules/**` were treated only as runtime evidence.

## Fresh Without-Skill Baseline

- Source: a newly spawned independent issue #155 baseline worker using the same prompt and empty scratch fixture. It was explicitly prohibited from reading the target skill, Docs README, internal instructions, old comparisons, with-skill output, and packaged assets.
- Result: `BLOCKED`. The empty scratch exposed no scaffold source, complete inventory, manifest rules, or runner, so the worker correctly refused to guess and created no `docs/site/` output.
- No historical baseline was reused. The inability to generate the requested scaffold demonstrates the behavioral value of the skill and does not block the valid with-skill result.

## Failures

- No with-skill assertion failures or blocked checks.
- The fresh without-skill lane was blocked by absent implementation sources and satisfied none of the artifact assertions.
- `npm ci` reported 3 audit advisories (2 moderate, 1 high); installation, 74/74 tests, and both required builds still passed, so this is recorded as non-blocking runtime evidence rather than an eval failure.

## Next Steps

- Retain the PASS only as the historical issue #155 result for the 40-asset, five-template contract.
- Run fresh paired validation for the current 42-asset, six-template contract, including a newly generated `without_skill` baseline, before replacing the BLOCKED result.

## Runtime Artifact Policy

- Runtime lanes, manifests, checksums, `node_modules`, generated site trees, and baseline reports remain under `tmp/eval-runs/issue-155/` and are not durable repository artifacts.
- Only this `comparison.md` is retained; no transcript, candidate, verdict, timing, diagnostics, dependency directory, or generated site output is submitted.
