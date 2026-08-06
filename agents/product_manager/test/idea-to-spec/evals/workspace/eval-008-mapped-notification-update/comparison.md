# Eval Result: eval-008-mapped-notification-update

## Latest Fresh Evaluation — 2026-08-07

- Model: `gpt-5.6-luna`, `model_reasoning_effort="medium"`
- Fixture: HEAD `47adbbc9`; fresh paired manifests matched exactly.
- Behavior result: PASS — 3/3 assertions passed.
- Coverage result: FULL — all 3 assertion scenarios were exercised.
Overall result: PASS

### Assertion Results

- `reads_mapped_docs_first`: PASS — the trace read the mapped notifications page before `channels.txt` and did not traverse unrelated site pages.
- `verifies_against_code`: PASS — code showed email only and the response preserved the webhook documentation conflict.
- `treats_unverified_as_low_trust`: PASS — the unverified page was treated as low trust and checked against code.

### With-Skill / Baseline Comparison

The with-skill response stayed read-only and formed the SMS-channel update scope from mapped docs plus code truth. The baseline edited the documentation directly; it is comparison evidence only.

### Failures / Next Steps

- No with-skill assertion failures and no coverage gaps.

### Runtime Artifact Policy

- Fresh evidence remains under `/private/tmp/pm-spec-fresh-evidence.GpQ6yO/eval-008-mapped-notification-update/` and is not committed.

---

The sections below are historical records from earlier runs.

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-008-mapped-notification-update`
- Workspace: `workspace/eval-008-mapped-notification-update`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: HEAD `a452319`; notification source, change map, `unverified` API page, and email-only code fact.
- Fresh run: `2026-08-03 11:58:20 +0800`
- Runtime directory: `tmp/eval-runs/issue-198-brd/pm/eval-008-mapped-notification-update/`

## Latest Result

- Behavior result: PASS — all 3 assertions passed.
- Coverage result: FULL — 3/3 assertion scenarios were exercised; no `NOT EXERCISED` items.
Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Assertion Results

- `reads_mapped_docs_first`: PASS — maps `src/notifications/` to and reads only `docs/site/api/notifications.md`.
- `verifies_against_code`: PASS — treats `channels.txt` email-only state as ground truth and reports webhook drift.
- `treats_unverified_as_low_trust`: PASS — explicitly gives the unverified page the lowest trust and rechecks all key facts in code.

## With-Skill Behavior

The response preserves the mapped-document-first and code-ground-truth protocol, structures the email/webhook discrepancy, and frames SMS as an `existing-project-update` whose stable product facts belong in PRD/DECISIONS. No BRD stage or artifact appears.

## Fresh Without-Skill Baseline

The baseline was newly generated in this run from the same prompt and fixture, without reading or applying the target skill, Product Manager README, internal instructions, or historical comparison. Strong fixture cues led it to the correct factual discrepancy, but it did not establish the same precise consumption order, trust model, or single-decision update protocol.

## Failures

- No assertion failures or baseline blockers.
- BRD removal caused no evidence-consumption regression.

## Next Steps

- Keep this eval as coverage for change-map consumption and code verification feeding directly into PRD/DECISIONS scope.

## Runtime Artifact Policy

- Fresh responses and judge notes remain under `tmp/eval-runs/issue-198-brd/pm/eval-008-mapped-notification-update/` and are not committed.
