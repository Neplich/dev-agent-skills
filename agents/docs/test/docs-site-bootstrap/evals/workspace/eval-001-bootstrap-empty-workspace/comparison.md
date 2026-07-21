# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-site-bootstrap`
- Eval: `eval-001-bootstrap-empty-workspace`
- Review context: issue #150 fresh paired eval group A

## Test Set / Fixture Version

- Fixture: pristine empty host from `workspace/eval-001-bootstrap-empty-workspace`
- Asset snapshot: current 40-file `assets/docs/site/` inventory
- Actual validation date: `2026-07-21`
- Execution cleanup: isolated lane started without `docs/site/`

## Latest Result

**PASS (6/6 assertions)** — the fresh with-skill lane created the complete bounded scaffold, generated and read back a 40-entry manifest, passed host checks, and demonstrated a zero-content-diff repeat classification.

## Assertions

- `creates_complete_inventory`: PASS. All 40 packaged assets were copied byte-for-byte; manifest parsing returned 40 sorted `created` entries.
- `delivers_deterministic_scaffold_assets`: PASS. `package.json` has exactly one `new:doc`; the scaffold script and test exist; each of five templates has exactly one `docs-scaffold` block and all five are indexed.
- `validates_seven_frontmatter_fields`: PASS. `npm run test:docs` passed the shared frontmatter checker, including the allowed `doc_type` set and non-empty array requirements.
- `writes_only_docs_site`: PASS. The generated scaffold and runtime manifest were confined to the isolated `docs/site/` root.
- `requires_explicit_opt_in`: PASS. Execution relied on the prompt's explicit repository, fixed root, full scaffold, and manifest authorization; the skill gate would stop before writes without that basis.
- `reports_manifest_readback`: PASS. The manifest was parsed successfully and a checksum dry-run found no file-content delta on repeat classification; only directory timestamps were observable.

## With-Skill Behavior

- Read the Docs Agent boundary, bootstrap skill, internal 40-file inventory, manifest protocol, and shared frontmatter contract only after the explicit opt-in gate passed.
- Copied 40/40 static assets exactly and created `.meta/bootstrap-manifest.json` with stable sorted paths and `createdAt`.
- Ran `npm ci --ignore-scripts`, then `npm run test:docs` in the isolated `docs/site/`; exit status was `0`, with 74/74 Node tests passing.
- The isolated fixture initially inherited the outer worktree's exact tag `v0.3.2`. The final run used a runtime-only Git wrapper that makes only `git describe --exact-match` unavailable while delegating every other Git command, preventing an unrelated ancestor tag from contaminating fixture version checks.

## Fresh Without-Skill Baseline

- Source: fresh `without_skill` lane from the same pristine empty fixture and the same eval prompt/assertions; it did not read the target `SKILL.md`, Docs README, internal instructions, old comparison, or with-skill output.
- The baseline independently found the packaged assets, produced the 40-file scaffold and manifest, and passed the same isolated host checks; it satisfied 6/6 assertions.
- Its artifact result was correct, but it lacked the skill's authoritative explanation of persistent manifest dispositions, conflict-state transitions, and safety-net handoff behavior.

## Failures

- No assertion failures.
- `npm ci` reported 3 audit advisories (2 moderate, 1 high); installation and required docs checks still exited `0`, so this is not a failure of the evaluated bootstrap behavior.

## Next Steps

- Keep this PASS as the issue #150 fresh result. Re-run paired validation whenever the 40-file inventory, frontmatter contract, manifest state machine, or scaffold tests change.

## Runtime Artifact Policy

- Runtime lanes, `node_modules`, manifests, test output, and the isolation wrapper remain under `tmp/eval-runs/issue-150/group-a/` and are not durable repository artifacts.
- Only this `comparison.md` is retained; no transcript, candidate, verdict, timing, diagnostics, build output, or runtime dependency directory is submitted.
