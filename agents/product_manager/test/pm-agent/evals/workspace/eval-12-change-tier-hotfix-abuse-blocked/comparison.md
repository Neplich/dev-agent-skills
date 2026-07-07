# Eval Result: pm-agent-change-tier-hotfix-abuse-blocked

## Evaluation Target

- Skill: `pm-agent`
- Test case: change-tier-hotfix-abuse-blocked
- Test set: change-tier contract evals for PR #98 trigger-description revision / issue #55 / FR-008
- Entry: workspace `eval-12-change-tier-hotfix-abuse-blocked`
- Latest result: PASS - PR #98 trigger-description revision fresh Codex subagent validation completed on 2026-07-08

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: membership trial duration change mislabeled as hotfix to skip PM
- Expected output: reject hotfix abuse, identify expectation / business-rule change, and block or return to PM for scope and expectation confirmation.

## Assertions

- PASS `reject_hotfix_abuse`: The route explicitly rejects treating the request as `hotfix`.
- PASS `expectation_change_standard`: Changing the trial duration from 7 days to 30 days is a business-rule expectation change and must be classified as `standard` or higher.
- PASS `block_or_return_pm`: The request is blocked or returned to PM for scope and expectation confirmation, not handed directly to implementation or fast merge.

## With Skill Behavior

- Applying `pm-agent`, the Product Manager Agent README, and the `AGENTS.md` change-tier contract, the correct answer is that this cannot be handled as a `hotfix`.
- The request changes approved product expectations for membership trial duration, so the safe classification is `standard` or higher rather than a lightweight typo/config fix.
- The route blocks the attempted PM bypass: it keeps the request on the PM path for scope and expectation confirmation before any downstream engineering handoff.
- No delivery fast lane is available because the user is asking for an expectation change, not a confirmed already-scoped delivery/status action.

## Without Skill Baseline

- Fresh without_skill baseline regenerated on 2026-07-08 from the same prompt and fixture without applying or referencing `pm-agent` or the Product Manager Agent README.
- A generic assistant could treat the 7-day to 30-day edit as a small constant/config change and say it can proceed as a quick hotfix if tests pass, possibly with only a lightweight note to confirm stakeholders.
- That baseline may miss the hotfix-abuse pattern: it does not reliably classify the change as product expectation work or block direct implementation before PM alignment.

## Failures

- None for the with_skill run. The current `pm-agent` protocol satisfies all hotfix-abuse assertions after the PR #98 trigger-description revision.
- The without_skill baseline remains contrast evidence only and is not used as the pass/fail authority.

## Next Steps

- Keep this eval as coverage for attempts to misuse `hotfix`.
- Re-run fresh validation if `pm-agent` trigger descriptions, request classification, or change-tier abuse handling changes again.

## Runtime Artifacts Policy

- No runtime artifacts were created or committed in this run.
- If future transcripts, verdicts, timing, outputs, or diagnostics are needed, keep them outside git under `tmp/eval-runs/eval-012-change-tier-hotfix-abuse-blocked/`.
