# Eval Result: pm-agent-route-bugfix-request

## Evaluation Target

- Skill: `pm-agent`
- Test case: route-bugfix-request
- Test set: PM entry evals for issue #52 / FR-006 scenario 2; PR #98 trigger-description routing check
- Entry: workspace `eval-2-route-bugfix-request`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-08

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: login bug report before expected behavior has been checked
- Expected output: classify as `bug_report`, confirm approved PRD / TRD expected behavior first, then hand off to Engineer/debugger only after implementation deviation is established.

## Assertions

- PASS `request_type_bug_report`: The request is classified as `bug_report` rather than immediate repair work.
- PASS `expectation_first`: The route requires approved PRD / TRD or equivalent expected behavior before implementation diagnosis.
- PASS `debugger_handoff_after_confirmation`: Engineer/debugger handoff is allowed only after the bug is confirmed as an implementation deviation.

## With Skill Behavior

- Fresh subagent applied the current-branch `pm-agent` SKILL.md and Product Manager Agent README.
- The router classifies the token-expiry spinner report as `bug_report` instead of starting a repair.
- It requires approved PRD / TRD or equivalent product expectations, reproduction evidence, and actual behavior before implementation diagnosis.
- It only allows `engineer-agent` / debugger handoff after the spinner behavior is confirmed as an implementation deviation; unclear expectations should not be treated as a `hotfix`.

## Without Skill Baseline

- Fresh without_skill baseline was regenerated on 2026-07-08 from the eval prompt and fixture README only; it did not reuse historical baseline text and did not apply `pm-agent` SKILL.md or the Product Manager Agent README.
- The generic baseline may ask for reproduction details and expected token-expiry behavior, but it is less reliable about explicitly classifying `request_type: bug_report`, preserving `change_tier`, and enforcing the PM expectation-first gate before debugger handoff.

## Failures

- None. The current `pm-agent` protocol satisfies the bug classification and expectation-first assertions.
- No routing regression found from the PR #98 trigger-description changes.

## Next Steps

- Keep this eval as PM entry coverage for bug reports.
- Re-run fresh validation if bug handling, debugger handoff gates, or entry trigger descriptions change.

## Runtime Artifacts Policy

- No runtime artifacts were committed. The validating subagent did not create runtime files.
- If future transcripts, verdicts, timing data, outputs, or diagnostics are generated, keep them under `tmp/eval-runs/pm-agent-20260708/eval-002/` or another isolated scratch path and do not commit them.
