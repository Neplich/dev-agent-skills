# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-site-bootstrap`
- Eval: `eval-003-block-bootstrap-conflict`
- Review context: issue #155 fresh paired eval

## Test Set / Fixture Version

- Fixture: `issue-122-assets-conflict-v1`
- Scope: one known host conflict plus representative identical targets; omitted targets follow the fixture's missing-or-identical assumption
- Dependency fact under review: the representative `package.json` VitePress declaration is pinned exactly to `1.6.4`
- Actual validation date: `2026-07-22`

## Latest Result

**PASS (3/3 assertions)** — the fresh with-skill lane identified the complete materialized conflict, preserved the customized host file and partial manifest byte-for-byte, and blocked the overwrite stage pending one of three explicit decisions.

## Assertions

- `blocks_on_complete_conflict_list`: PASS. `docs/site/standards/index.md` is the complete conflict list under the fixture scope; the unresolved overwrite stage remains blocked and the manifest has no success state for that path.
- `does_not_overwrite_conflict`: PASS. The target still matches the pristine host customization and differs from the packaged asset; before/after SHA-256 sets match, with no merge, formatting, normalization, or partial overwrite.
- `offers_explicit_resolution_choices`: PASS. The with-skill result requires the user to choose overwrite, an explicitly reviewed merge, or keep; `kept-as-is` is recorded only after an explicit keep decision.

## With-Skill Behavior

- Source: fresh issue #155 with-skill lane under `tmp/eval-runs/issue-155/with_skill/eval-003`, using the current target skill and conflict protocol with the same eval prompt and copied minimal fixture.
- Classified `package.json` and `.meta/releases.json` as byte-identical and `standards/index.md` as the single known unresolved conflict; the representative package declares VitePress exactly as `1.6.4`.
- Read-back confirmed the customized index and manifest stayed byte-identical to input; the manifest still contains only the two pre-existing `skipped-identical` entries and no state for the conflict.
- The valid outcome is blocked pending overwrite, explicit merge, or keep. A future keep decision would add `kept-as-is`; no such decision was inferred in this run.
- The fixture deliberately omits executable site scripts and most inventory files, so host tests and builds are not applicable. Conflict comparison, manifest parsing, and before/after hashes are the executable evidence; no complete-host checks are claimed.

## Fresh Without-Skill Baseline

- Source: a newly spawned independent issue #155 baseline worker using the same prompt and copied fixture, with the target skill, Docs README, internal instructions, old comparisons, and with-skill output prohibited.
- Result: `BLOCKED`. It preserved the customized conflict and partial manifest, but lacked the full inventory source and could not complete omitted-target classification or bootstrap.
- The baseline identified keep and overwrite as decisions but omitted the required explicit-merge option, so its behavior satisfies conflict preservation but not the full three-choice assertion. No historical baseline was reused.

## Failures

- No with-skill assertion failures.
- The blocked overwrite stage is the expected successful behavior, not an eval failure.
- Host docs tests and builds are not applicable to this deliberately partial conflict fixture.
- The baseline did not provide the full three-option conflict protocol and remained blocked by missing inventory; this comparison does not promote it to PASS.

## Next Steps

- Retain this PASS. A real bootstrap remains paused until the maintainer selects overwrite, an approved explicit merge, or keep for every conflict.

## Runtime Artifact Policy

- Runtime copies, hashes, conflict evidence, and baseline reports remain under `tmp/eval-runs/issue-155/` and are not submitted.
- Only this durable comparison is retained; no runtime transcript, candidate, verdict, timing, diagnostics, dependencies, or generated site output is committed.
