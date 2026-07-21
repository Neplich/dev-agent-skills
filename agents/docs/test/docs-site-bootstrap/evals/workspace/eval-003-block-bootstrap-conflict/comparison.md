# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-site-bootstrap`
- Eval: `eval-003-block-bootstrap-conflict`
- Review context: issue #150 fresh paired eval group A

## Test Set / Fixture Version

- Fixture: `issue-122-assets-conflict-v1`
- Scope: one known host conflict plus representative identical targets; omitted targets follow the fixture's missing-or-identical assumption
- Actual validation date: `2026-07-21`

## Latest Result

**PASS (3/3 assertions)** — the with-skill lane found the complete known conflict, preserved the host file and manifest byte-for-byte, and blocked pending an explicit resolution.

## Assertions

- `blocks_on_complete_conflict_list`: PASS. `docs/site/standards/index.md` was the complete materialized conflict list and the unresolved overwrite phase remained blocked; the manifest gained no success state for that path.
- `does_not_overwrite_conflict`: PASS. The target still matches the pristine host customization and differs from the packaged asset; no merge, formatting, normalization, or partial overwrite occurred.
- `offers_explicit_resolution_choices`: PASS. The result offers overwrite, an explicitly reviewed merge, or keep; `kept-as-is` may be recorded only after the user selects keep.

## With-Skill Behavior

- Classified `package.json` and `.meta/releases.json` as identical and `standards/index.md` as the known unresolved conflict, while respecting the fixture's omitted-target scope.
- Read-back confirmed the host-customized index stayed byte-identical to pristine input and the manifest still contains only the two pre-existing `skipped-identical` entries.
- The fixture is deliberately partial and lacks executable site scripts, so host docs tests are not applicable; conflict preservation and manifest checks are the executable evidence for this case.

## Fresh Without-Skill Baseline

- Source: fresh `without_skill` lane from the same pristine fixture and prompt/assertions; it did not read the target skill, Docs README, internal instructions, old comparison, or with-skill output.
- The explicit `known_conflict` fixture field was sufficient for the baseline to preserve the file, block, and offer all three choices; it satisfied 3/3 assertions.
- The skill added authoritative guarantees for complete inventory classification and persistent `kept-as-is` semantics that the baseline did not independently define.

## Failures

- No assertion failures.
- The blocked overwrite is the expected successful behavior, not an eval failure.

## Next Steps

- Keep this PASS. A real bootstrap remains paused until the maintainer selects overwrite, an approved merge, or keep for each conflict.

## Runtime Artifact Policy

- Runtime copies, comparisons, and conflict evidence stay under `tmp/eval-runs/issue-150/group-a/` and are not submitted.
- Only this comparison is durable; no runtime transcript, candidate, verdict, timing, diagnostics, dependencies, or build output is committed.
