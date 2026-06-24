# Eval Result: eval-003-feature-path-missing-plan-blocked

## Evaluation Target

- Agent: `qa`
- Skill: `qa-agent`
- Eval: `eval-003-feature-path-missing-plan-blocked`
- Test case: feature-path-missing-plan-blocked
- Workspace: `workspace/eval-3-feature-path-missing-plan-blocked`
- Latest result: PARTIAL - prior skill validation evidence is preserved; without-skill baseline was not generated for this historical comparison.
- Prior validation note: fresh Codex subagent validation on 2026-06-23

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Same-path PRD and TRD for `account/profile/preferences`, an existing QA E2E function-tree directory, and no `docs/engineer/account/profile/preferences/IMPLEMENTATION_PLAN.md`.
- Expected output: QA route decision that blocks E2E acceptance TC creation/update/execution because the confirmed implementation plan is missing.

## Assertions

- `reads_same_feature_path`: use `account/profile/preferences` as the confirmed feature path and read matching PRD/TRD plus QA function-tree memory.
- `blocks_missing_plan`: mark the request blocked and return the missing implementation plan to `engineer-agent:feature-implementor`.
- `no_e2e_mutation_or_execution`: do not create, update, or execute acceptance TC without the plan.
- `keeps_single_route`: choose one narrow QA route and do not enter implementation.

## With Skill

- PASS. Current `qa-agent` instructions consume a confirmed same-path `feature_path` before E2E acceptance work. The fixture provides matching `docs/pm/account/profile/preferences/PRD.md`, `docs/engineer/account/profile/preferences/TRD.md`, and QA function-tree memory under `docs/qa/e2e/account/profile/preferences/`.
- PASS. The QA Feature Path Gate requires `docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md` for existing-feature changes, bug fixes, or code-complete E2E documentation updates before creating, updating, or executing acceptance TC. The fixture intentionally omits `docs/engineer/account/profile/preferences/IMPLEMENTATION_PLAN.md`, so the correct route result is `blocked`.
- PASS. The skill separates owners: missing or mismatched TRD returns to `engineer-agent:trd-gen`, while a missing or mismatched implementation plan returns to `engineer-agent:feature-implementor`. This fixture omits the implementation plan, so the next owner is `engineer-agent:feature-implementor` rather than QA execution.
- PASS. The route remains a single narrow QA route and stops before TC mutation, TC execution, or implementation repair. The QA directory being present is treated as memory to read, not sufficient authorization to run acceptance.

## Without Skill / Baseline
- BLOCKED: No actual without-skill baseline result is recorded for this historical comparison. This file is not treated as a full eval PASS until a baseline result is generated and written here.
- A generic answer may treat the QA directory as sufficient context and start creating or executing TC without the implementation-plan gate.

## Failures

- None.

## Next Steps

- No skill or fixture change is required for this eval. Residual risk: this validation is a direct skill-read judgment against current docs and fixture files; no model transcript was generated.

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be committed.
