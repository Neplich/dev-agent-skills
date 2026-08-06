# Eval Result: eval-001-legacy-project-catalog

## Latest Fresh Evaluation — 2026-08-07

- Model: `gpt-5.6-luna`, `model_reasoning_effort="medium"`
- Fixture: HEAD `47adbbc9`; baseline and with-skill input manifests matched exactly.
- Isolation: baseline completed and its root was deleted before any with-skill root was created; the judge used a third independent root.
- Behavior result: PASS — 5/5 assertions passed.
- Coverage result: FULL — all 5 assertion scenarios were exercised.
Overall result: PASS

### Assertion Results

- `draft_before_formal_docs`: PASS — produced a visibly pending draft and wrote no formal catalog or PRD.
- `evidence_and_confidence`: PASS — used the actual route/API/service/model/job/test evidence and conservative confidence.
- `business_capability_naming`: PASS — grouped findings into user-facing authentication, order management, and status notification capabilities.
- `open_questions_present`: PASS — recorded unresolved ownership and boundary questions.
- `confirmation_gate`: PASS — stopped at maintainer confirmation before formal docs or handoff.

### With-Skill / Baseline Comparison

The with-skill lane produced an evidence-first, low-confidence draft without durable writes. The baseline wrote `docs/功能目录.md` before confirmation and lacked the same gate discipline.

### Failures / Next Steps

- No with-skill assertion failures and no coverage gaps.

### Runtime Artifact Policy

- Fresh evidence remains under `/private/tmp/pm-spec-fresh-evidence.GpQ6yO/eval-001-legacy-project-catalog/` and is not committed.

---

The sections below are historical records from earlier runs.

## Evaluation Target

- Agent: `product_manager`
- Skill: `feature-catalog`
- Eval: `eval-001-legacy-project-catalog`
- Workspace: `workspace/eval-001-legacy-project-catalog`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: HEAD `a452319`; Node.js commerce backend with no PM docs and shallow-scan evidence for authentication, orders, notifications, model, and tests.
- Fresh run: `2026-08-03 11:58:20 +0800`
- Runtime directory: `tmp/eval-runs/issue-198-brd/pm/eval-001-legacy-project-catalog/`

## Latest Result

- Behavior result: PASS — all 5 assertions passed.
- Coverage result: FULL — 5/5 assertion scenarios were exercised; no `NOT EXERCISED` items.
Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Assertion Results

- `draft_before_formal_docs`: PASS — produces a visibly pending draft and writes no catalog or PRD.
- `evidence_and_confidence`: PASS — each candidate includes actual evidence categories, related paths, and conservative confidence.
- `business_capability_naming`: PASS — names authentication, order management, and order status notifications as business capabilities.
- `open_questions_present`: PASS — records ownership and boundary uncertainty instead of presenting guesses as facts.
- `confirmation_gate`: PASS — stops with one maintainer confirmation request before formal docs or handoff.

## With-Skill Behavior

The response used the documented lightweight scan because no Project Profile exists, grouped evidence by business capability, capped shallow-scan candidates at low confidence, and stopped before writing `docs/pm/FEATURE_CATALOG.md`. After confirmation, the spec handoff is directly to PRD/DECISIONS and later Engineer TRD; no BRD step remains.

## Fresh Without-Skill Baseline

The baseline was newly generated in this run from the same prompt and fixture, without reading or applying the target skill, Product Manager README, internal instructions, or historical comparison. It found the same broad modules but organized them more mechanically, used inconsistent confidence, and lacked the explicit maintainer confirmation gate.

## Failures

- No assertion failures or baseline blockers.
- BRD removal caused the expected handoff-chain difference, not a regression: confirmed catalog entries now proceed directly to PRD/DECISIONS.

## Next Steps

- Keep this eval as coverage for legacy feature discovery and the BRD-free confirmation-to-spec handoff.

## Runtime Artifact Policy

- Fresh responses and judge notes remain under `tmp/eval-runs/issue-198-brd/pm/eval-001-legacy-project-catalog/` and are not committed.
