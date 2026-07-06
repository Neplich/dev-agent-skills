# Eval Result: pm-agent-change-tier-hotfix-abuse-blocked

## Evaluation Target

- Skill: `pm-agent`
- Test case: change-tier-hotfix-abuse-blocked
- Test set: change-tier contract evals for issue #55 / FR-008
- Entry: workspace `eval-12-change-tier-hotfix-abuse-blocked`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-06

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: membership trial duration change mislabeled as hotfix to skip PM
- Expected output: reject hotfix abuse, identify expectation / business-rule change, and block or return to PM for scope confirmation.

## Assertions

- PASS `reject_hotfix_abuse`: The route explicitly rejects treating the request as `hotfix`.
- PASS `expectation_change_standard`: The trial-duration change is a business-rule expectation change and must be `standard` or higher.
- PASS `block_or_return_pm`: The request is blocked or returned to PM for scope and expectation confirmation, not handed directly to implementation.

## With Skill Behavior

- The `pm-agent` protocol explicitly says new requirements, expectation changes, and unclear scope stay on the PM path and must not be routed as `hotfix`.
- Changing trial duration from 7 days to 30 days is a business-rule expectation change, so the request is `standard` or higher.
- It blocks direct implementation and returns to PM expectation and scope confirmation.
- Issue #81 safety-net behavior remains within boundary: auto-continue cannot turn an attempted PM bypass into implementation permission.

## Without Skill Baseline

- Fresh without_skill baseline regenerated on 2026-07-06 without applying `pm-agent` or the Product Manager Agent README. A generic response could follow the user's hotfix framing and start the value change.
- It may not catch that the request is trying to use `hotfix` as an escape hatch from PM alignment.

## Failures

- None. The current `pm-agent` protocol satisfies all hotfix-abuse assertions.
- No issue #81 regression found; role-boundary priority keeps expectation changes on the PM path.

## Next Steps

- Keep this eval as coverage for attempts to misuse `hotfix`.
- Re-run fresh validation if change-tier abuse handling changes.

## Runtime Artifacts Policy

- No runtime artifacts were created or committed. Transcripts, verdicts, timing, outputs, and diagnostics must remain outside git.
