# Eval Result: eval-002-existing-project-update

## Latest Fresh Evaluation — 2026-08-07

- Model: `gpt-5.6-luna`, `model_reasoning_effort="medium"`
- Fixture: HEAD `47adbbc9`; fresh paired manifests matched exactly.
- Behavior result: PASS — 4/4 assertions passed.
- Coverage result: FULL — all 4 assertion scenarios were exercised.
Overall result: PASS

### Assertion Results

- `update`: PASS — identified the request as `existing-project-update` against approved PRD/TRD/DECISIONS.
- `delta_blast_radius`: PASS — described the delivery delta and affected behavior/documents first.
- `assertion_3`: PASS — recommended `change-impactor` plus targeted iteration, not regeneration.
- `assertion_4`: PASS — named the notification-center PRD, DECISIONS, and Engineer TRD paths.

### With-Skill / Baseline Comparison

The with-skill response stayed read-only and produced a delta-oriented update sequence. The baseline also produced a useful impact analysis but directly rewrote the three documents; it remained comparison evidence only.

### Failures / Next Steps

- No with-skill assertion failures and no coverage gaps.

### Runtime Artifact Policy

- Fresh evidence remains under `/private/tmp/pm-spec-fresh-evidence.GpQ6yO/eval-002-existing-project-update/` and is not committed.

---

The sections below are historical records from earlier runs.

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
Historical result: BLOCKED
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
