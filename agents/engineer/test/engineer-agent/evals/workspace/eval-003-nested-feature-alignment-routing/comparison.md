# Eval Result: eval-003-nested-feature-alignment-routing

## Evaluation Target

- Agent: `engineer`
- Skill: `engineer-agent`
- Eval: `eval-003-nested-feature-alignment-routing`
- Test case: nested-feature-alignment-routing
- Workspace: `workspace/eval-003-nested-feature-alignment-routing`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: approved `chat-interface/history-search` PRD/TRD with a small search-ordering change.
- Fresh validation date: 2026-08-01.
- With-skill source: current Engineer README, current `engineer-agent` SKILL, eval definition, metadata, README, and same-path PRD/TRD.
- Without-skill source: the same prompt and fixture, freshly regenerated without reading or applying the target README/SKILL, with-skill output, historical comparison, or prior baseline.

## Latest Result

- Behavior result: PASS
- Coverage result: FULL
Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


All 5 assertions were exercised and passed in the with-skill run.

## Assertions

- PASS `resolves_nested_feature_path`: preserves `chat-interface/history-search` and reads its same-path PRD/TRD.
- PASS `does_not_use_sibling_or_parent_only_path`: does not collapse evidence to a sibling or parent-only path.
- PASS `routes_requirement_change_to_pm`: sends approved sorting changes to the PM `existing-project-update` lane.
- PASS `routes_trd_mismatch_to_trd_gen`: sends missing, stale, or path-mismatched TRDs to `engineer-agent:trd-gen`.
- PASS `does_not_execute_directly`: remains route-only.

## With Skill Behavior

The fresh route resolves the nested path, compares the explicit sorting contract, sends a changed expectation to PM, and sends technical freshness/path mismatches to `trd-gen`. It does not create a plan, edit code, or run tests.

## Without Skill Baseline

The fresh baseline preserves the exact nested paths, recognizes a possible product requirement change, and stays route-only. It does not name the required PM `existing-project-update` or `engineer-agent:trd-gen` routes. Baseline assertion result: 3/5.

## Failures

- None.

## Next Steps

- Keep this eval as regression coverage for nested feature-path resolution and same-path alignment.

## Runtime Artifacts Policy

- Fresh runtime evidence is under `tmp/eval-runs/issue-196-project-bootstrap-removal-20260801-131022/engineer-agent/eval-003-nested-feature-alignment-routing/`.
- `with_skill.md`, `without_skill.md`, and `verdict.md` are scratch evidence and must not be committed.
- This `comparison.md` is the only durable result.
