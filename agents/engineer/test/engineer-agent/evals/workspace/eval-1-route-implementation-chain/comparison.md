# Eval Result: eval-001-route-implementation-chain

## Evaluation Target

- Agent: `engineer`
- Skill: `engineer-agent`
- Eval: `eval-001-route-implementation-chain`
- Test case: route-implementation-chain
- Workspace: `workspace/eval-1-route-implementation-chain`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: existing billing webhook service with a TRD and route-only implementation, test, QA E2E handoff, and delivery request.
- Fixture version: current HEAD `a452319`.
- Fresh run time: `2026-08-03 11:58:13 +0800`.
- Runtime directory: `tmp/eval-runs/issue-198-brd/engineer/20260803-115813/engineer-agent/eval-001-route-implementation-chain/`.
- With-skill source: current Engineer README, current `engineer-agent` SKILL, eval definition, and fixture README, metadata, TRD, and code notes.
- Without-skill source: the same prompt and fixture, freshly regenerated this run without applying the target README/SKILL, with-skill output, historical comparison, or any prior baseline.

## Latest Result

- Behavior result: PASS
- Coverage result: FULL
Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


All 6 assertions were exercised and passed. Removing BRD from the planning-input wording did not change the engineering route, implementation-plan gate, QA E2E handoff, or delivery order.

## Assertion Results

- PASS `starts_with_codebase_context`: starts with `codebase-analyzer` for repository structure, stack, constraints, and existing patterns.
- PASS `routes_implementation_to_feature_implementor`: assigns implementation to `feature-implementor` after the confirmed PRD/TRD/implementation-scope entry gate and requires the implementation plan before code.
- PASS `routes_tests_to_test_writer`: keeps automated coverage in a distinct `test-writer` stage.
- PASS `routes_qa_e2e_handoff`: after implementation and deterministic tests, requires the PRD/TRD/confirmed-plan QA E2E handoff package, changed files, verification commands, risks, and suggested feature directory.
- PASS `routes_delivery_last`: leaves `delivery` after implementation, tests, and the QA handoff check.
- PASS `does_not_execute_directly`: performs route-only work and does not modify code, run tests, or create delivery artifacts.

## With-Skill Behavior

The fresh route starts with `codebase-analyzer`, preserves the specialist entry-basis check, then routes confirmed work through `feature-implementor`, `test-writer`, the QA E2E handoff check, and `delivery`. It identifies `docs/engineer/billing-webhook/IMPLEMENTATION_PLAN.md` as the pre-code gate and carries the complete QA package requirements. BRD is neither requested nor treated as a missing prerequisite; PRD, product decisions, TRD, and current implementation scope retain their existing responsibilities.

## Fresh Without-Skill Baseline

The without-skill baseline was newly generated in this run from the same prompt and fixture. It gives a generic inspect-implement-test-PR sequence and obeys the no-execution request, but it does not select the repository's named specialists, require a confirmed durable implementation plan, or include the QA E2E handoff package. Baseline assertion result: 1/6.

## Failures

- None.

## Next Steps

- Keep this eval as regression coverage for route-only implementation chains after BRD contract removal.

## Runtime Artifact Policy

- Fresh runtime evidence is under `tmp/eval-runs/issue-198-brd/engineer/20260803-115813/engineer-agent/eval-001-route-implementation-chain/`.
- `with_skill.md`, `without_skill.md`, and `verdict.md` are ignored scratch evidence and must not be committed.
- This `comparison.md` is the only durable result for this case.
