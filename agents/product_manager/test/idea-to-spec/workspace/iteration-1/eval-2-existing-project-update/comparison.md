# Eval Result: eval-002-existing-project-update

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-002-existing-project-update`
- Workspace: `workspace/iteration-1/eval-2-existing-project-update`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: HEAD `a452319`; approved notification-center PRD, DECISIONS, and Engineer TRD covering polling and the confirmed event-driven migration direction.
- Fresh run: `2026-08-03 11:58:20 +0800`
- Runtime directory: `tmp/eval-runs/issue-198-brd/pm/eval-002-existing-project-update/`

## Latest Result

- Behavior result: PASS — all 4 assertions passed.
- Coverage result: FULL — 4/4 assertion scenarios were exercised; no `NOT EXERCISED` items.
Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Assertion Results

- `update`: PASS — classifies the request as `existing-project-update`.
- `delta_blast_radius`: PASS — states the delivery-model delta, affected behaviors, compatibility, rollback, tests, and documents before updates.
- `assertion_3`: PASS — prefers `change-impactor` and targeted iteration instead of regeneration.
- `assertion_4`: PASS — names the affected DECISIONS, PRD, Engineer TRD, and later QA paths.

## With-Skill Behavior

The response preserved the confirmed hybrid transition and rejected permanent polling-only history, then routed PM changes to targeted PRD/DECISIONS iteration and Engineer-owned TRD changes to `engineer-agent:trd-gen`. The retired BRD layer was absent; business delta and decisions flow directly into PRD and DECISIONS.

## Fresh Without-Skill Baseline

The baseline was newly generated in this run from the same prompt and fixture, without reading or applying the target skill, Product Manager README, internal instructions, or historical comparison. It identified the main documents and preferred incremental edits, but did not consistently apply `change-impactor`, `prd-iteration`, Engineer ownership, or decision-history preservation.

## Failures

- No assertion failures or baseline blockers.
- BRD removal caused no behavioral regression.

## Next Steps

- Keep this eval as coverage for delta-first impact analysis and targeted PRD/DECISIONS updates.

## Runtime Artifact Policy

- Fresh responses and judge notes remain under `tmp/eval-runs/issue-198-brd/pm/eval-002-existing-project-update/` and are not committed.
