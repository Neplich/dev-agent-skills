# Eval Result: eval-002-empty-qa-directory-expands-cases

## Evaluation Target

- Agent: `qa`
- Skill: `qa-agent`
- Eval: `eval-002-empty-qa-directory-expands-cases`
- Test case: empty-qa-directory-expands-cases
- Workspace: `workspace/eval-2-empty-qa-directory-expands-cases`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-06

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: existing empty E2E function tree for profile settings plus source files and QA environment notes.
- Context read before applying the skill: `evals.json`, workspace `eval_metadata.json`, `docs/qa/e2e/account/profile-settings/profile-form/TEST_SUITE.md`, `FLOW_INDEX.md`, `environment/qa-env.md`, `src/routes/profile-settings.md`, `src/pages/ProfileSettingsPage.tsx`, and `src/components/ProfileSettingsForm.tsx`.
- #81 context read: `Safety-Net Closeout and Auto-Continue` from `agents/product_manager/skills/idea-to-spec/_internal/_shared/skill-map.md`.

## Assertions

- PASS `assertion_1`: the route recognizes that the QA function tree exists but has no executable TC and must not be treated as existing coverage.
- PASS `assertion_2`: because the user confirmed a feature-update and authorized exploration, the downstream route should inspect target files and environment notes instead of asking whether exploration is allowed.
- PASS `assertion_3`: exploration must update `TEST_SUITE.md` and `FLOW_INDEX.md` with files explored, discovered route/form/commands, coverage meaning, and assumptions.
- PASS `e2e`: each new E2E case must be stored as `cases/TC-NNN-<short-slug>.md` with a matching `scripts/TC-NNN-<short-slug>.spec.md`, without plaintext secrets.
- PASS `assertion_5`: validation is TC-driven, feature-update scope stays on the changed feature and direct impacts, and execution entry follows repo harness > Chrome plugin / browser connector > Playwright fallback.
- PASS `version_and_subagent_gate`: platform version is required before execution; missing version blocks execution and reports go to `_reports/{platform-version}/test-reports-{test-time}.md` only after a real version is known.
- PASS `assertion_6`: the router selects one narrow QA route, with `exploratory-tester` as the best fit for expanding empty E2E coverage before execution.

## With Skill Behavior

`qa-agent` satisfies the empty-directory E2E route. It treats the existing function tree as durable memory, but not as executable coverage, and points to `exploratory-tester` as the narrow route for discovering flows and creating cases. It preserves credential hygiene, per-TC case/script persistence, subagent execution, and platform-version blocking. The fixture's `TEST_SUITE.md` states the platform version is missing, so execution is intentionally blocked until the version is provided; case expansion can still be routed as the preparatory QA work.

#81 closeout behavior is safe for this case: after preparatory QA routing, `qa-agent` may propose the next owner or handoff, but `auto-continue` cannot skip the platform-version gate, execute blocked E2E work, or perform implementation fixes outside the QA role.

## Without Skill Baseline

Fresh baseline generated on 2026-07-06 without reading or applying `qa-agent` skill instructions or the QA Agent README: a generic response might either mark the existing QA directory as sufficient coverage or jump straight to browser execution from source files. It is less likely to create durable per-TC case/script files, preserve function-tree report paths, block missing platform version correctly, or avoid writing credentials into scripts.

## Failures

- None found. Missing platform version is the expected execution blocker for this fixture.
- No #81 regression found: original empty-directory expansion, E2E persistence, and version gates remain intact, and `auto-continue` does not authorize blocked execution.

## Next Steps

- Keep this eval as regression coverage for empty E2E function-tree expansion, version-gated execution, and #81 closeout boundary behavior.

## Runtime Artifacts Policy

- No runtime artifacts were created for this validation.
- Runtime transcripts, verdicts, timing, output directories, diagnostics, and generated with_skill / without_skill files must not be committed.
