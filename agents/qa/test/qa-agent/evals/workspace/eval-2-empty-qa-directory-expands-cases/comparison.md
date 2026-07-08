# Eval Result: eval-002-empty-qa-directory-expands-cases

## Evaluation Target

- Agent: `qa`
- Skill: `qa-agent`
- Eval: `eval-002-empty-qa-directory-expands-cases`
- Test case: empty-qa-directory-expands-cases
- Workspace: `workspace/eval-2-empty-qa-directory-expands-cases`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-08 for PR #98 trigger description routing review.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: existing empty E2E function tree for profile settings plus source files and QA environment notes.
- Context read before applying the skill: `AGENTS.md`, `agents/qa/README.md`, `agents/qa/skills/qa-agent/SKILL.md`, `evals.json`, workspace `eval_metadata.json`, `docs/qa/e2e/account/profile-settings/profile-form/TEST_SUITE.md`, `FLOW_INDEX.md`, `environment/qa-env.md`, `src/routes/profile-settings.md`, `src/pages/ProfileSettingsPage.tsx`, and `src/components/ProfileSettingsForm.tsx`.
- Runtime evidence: fresh subagent artifacts were generated under `tmp/eval-runs/2026-07-08-router-trigger-batch3/eval-002-empty-qa-directory-expands-cases/`.

## Assertions

- PASS `assertion_1`: the route recognizes that the QA function tree exists but has no executable TC and must not be treated as existing coverage.
- PASS `assertion_2`: because the user confirmed a feature-update and authorized exploration, the downstream route should inspect target files and environment notes instead of asking whether exploration is allowed.
- PASS `assertion_3`: exploration must update `TEST_SUITE.md` and `FLOW_INDEX.md` with files explored, discovered route/form/commands, coverage meaning, and assumptions.
- PASS `e2e`: each new E2E case must be stored as `cases/TC-NNN-<short-slug>.md` with a matching `scripts/TC-NNN-<short-slug>.spec.md`, without plaintext secrets.
- PASS `assertion_5`: validation is TC-driven, feature-update scope stays on the changed feature and direct impacts, and execution entry follows repo harness > Chrome plugin / browser connector > Playwright fallback.
- PASS `version_and_subagent_gate`: platform version is required before execution; missing version blocks execution and reports go to `_reports/{platform-version}/test-reports-{test-time}.md` only after a real version is known.
- PASS `assertion_6`: the router selects one narrow QA route and does not expand QA routing into implementation repair or multiple QA specialists.

## With Skill Behavior

`qa-agent` satisfies the empty-directory E2E route after the PR #98 trigger description edits. The with-skill run selected a single primary route, `qa-agent:spec-based-tester`, recognized that `docs/qa/e2e/account/profile-settings/profile-form/` exists but has no executable TC, required targeted exploration of route, page, form, environment, harness, and test-command context, and required updates to `TEST_SUITE.md`, `FLOW_INDEX.md`, independent `cases/TC-NNN-<short-slug>.md`, and matching `scripts/TC-NNN-<short-slug>.spec.md` before TC-driven execution. It preserved the feature-update scope, execution-entry priority, subagent execution rule, and platform-version blocker; missing platform version blocks execution and forbids `unknown` result paths.

## Without Skill Baseline

Fresh baseline generated on 2026-07-08 from the eval prompt and fixture files only, without applying `qa-agent`, the QA Agent README, historical `comparison.md`, or any previous baseline. The baseline recognized a need to inspect code and add tests, but lacked the complete function-tree persistence contract, repo harness > Chrome / browser connector > Playwright execution priority, default subagent execution, report path rules, and `unknown` prohibition.

## Failures

- None found. Missing platform version is the expected execution blocker for this fixture, not a router failure.
- PR #98 did not regress empty-directory expansion, E2E persistence, version-gated execution, or QA route boundaries.

## Next Steps

- Keep this eval as regression coverage for empty E2E function-tree expansion and version-gated execution.

## Runtime Artifacts Policy

- Runtime artifacts were created only under `tmp/eval-runs/2026-07-08-router-trigger-batch3/eval-002-empty-qa-directory-expands-cases/`.
- Generated `with_skill.md`, `without_skill.md`, and `verdict.md` are scratch evidence only and must not be committed.
- Durable committed evidence for this run is this `comparison.md`.
