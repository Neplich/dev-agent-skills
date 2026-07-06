# Eval Result: pm-agent-change-tier-standard-full-gate

## Evaluation Target

- Skill: `pm-agent`
- Test case: change-tier-standard-full-gate
- Test set: change-tier contract evals for issue #55 / FR-008
- Entry: workspace `eval-11-change-tier-standard-full-gate`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-06

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: refund approval behavior change mislabeled as small hotfix
- Expected output: classify as `existing_update`, reject `hotfix`, set `standard` or higher, and require PRD/TRD expectation alignment.

## Assertions

- PASS `classify_standard`: The behavior change is `standard` or higher, not `hotfix`.
- PASS `require_prd_trd_alignment`: PRD/TRD or equivalent product expectation alignment is required before downstream implementation.
- PASS `request_type_existing_update`: The request is `existing_update` because it changes approved business behavior.

## With Skill Behavior

- The `pm-agent` change-tier rule rejects `hotfix` when approved product behavior changes.
- Changing refund approval from automatic approval to admin secondary confirmation is an `existing_update` and at least `standard`.
- The request stays on the PM path for PRD/TRD or equivalent expectation alignment before downstream implementation.
- Issue #81 safety-net behavior remains within boundary: closeout may recommend the next PM or Engineer-alignment step, but auto-continue cannot reclassify the behavior change as hotfix or skip gates.

## Without Skill Baseline

- Fresh without_skill baseline regenerated on 2026-07-06 without applying `pm-agent` or the Product Manager Agent README. A generic response could accept the user's "small" framing and skip expectation alignment.
- It may hand off implementation before confirming changed business behavior and downstream document impact.

## Failures

- None. The current change-tier rule satisfies all standard full-gate assertions.
- No issue #81 regression found; auto-continue respects the full PRD/TRD alignment gate for expectation changes.

## Next Steps

- Keep this eval as coverage for behavior changes mislabeled as hotfix.
- Re-run fresh validation if change-tier or existing-update gates change.

## Runtime Artifacts Policy

- No runtime artifacts were created or committed. Transcripts, verdicts, timing, outputs, and diagnostics must remain outside git.
