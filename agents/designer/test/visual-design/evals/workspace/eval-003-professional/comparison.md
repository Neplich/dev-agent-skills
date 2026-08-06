# Eval Result: eval-003-professional

## Evaluation Target

- Agent: `designer`
- Skill: `visual-design`
- Eval: `eval-003-professional`
- Test case: Professional Design System
- Workspace: `workspace/eval-003-professional`

## Test Set or Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: HEAD `a452319`
- Fresh run time: `2026-08-07 00:04:31 +0800`
- Runtime directory: `tmp/eval-runs/issue-198-brd/designer/visual-design/eval-003-professional/`
- Fixture: confirmed PM handoff and PRD for `enterprise-analytics`

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL** (2/2 assertions exercised)
Overall result: PASS

## Assertion Results (Current)

- assertion_1: **PASS** — the fresh visual-system.md defines WCAG 4.5:1 text and 3:1 UI/large-text thresholds with clear enterprise data hierarchy.
- assertion_2: **PASS** — the new artifact is design documentation only and contains no component code, style-file change, or engineering command.

## With-Skill Behavior (Current)

The candidate consumes the confirmed PM scope, reconciles local design evidence
to a trusted data-dense product system, writes the canonical feature-path
artifact, and stops at design handoff.

## Fresh Without-Skill Baseline (Current)

The baseline ran first from the same prompt, PM handoff, and PRD in an
independent top-level workspace under isolated HOME/CODEX_HOME. It meets the
two broad assertions but lacks the current skill's local reference reasoning
and explicit design-handoff depth.

## Failures (Current)

- None.

## Next Steps (Current)

- No corrective change is indicated by the current assertions.

## Runtime Artifact Policy (Current)

- Runtime lanes and judge evidence remain in independent /tmp workspaces and are not committed.
- Only this durable comparison is updated.

## Historical Result (Superseded: pre-#234 contract)

- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


Both assertions were exercised on the reachable visual-system generation path.

## Assertion Results

- `assertion_1`: **PASS** — the candidate states WCAG 4.5:1 normal-text and 3:1 large-text/UI-boundary thresholds and defines a clear enterprise data hierarchy.
- `assertion_2`: **PASS** — it contains no component code, style-file change, or engineering command.

## With-Skill Behavior

- Reconciles the helper's Enterprise Gateway/Trust & Authority result with the PRD's in-product, data-dense dashboard scope.
- Targets `docs/design/enterprise-analytics/visual-system.md` with accessible colors, authoritative typography, compact spacing, dimensioned tables/charts/filters/alerts, explicit states, and Engineer handoff.
- Reads audience, product goals, and visual tone from PRD and never requests or cites BRD; removal causes no tested behavior difference.

## Fresh Without-Skill Baseline

- This baseline was newly generated in this run from only the same prompt, PM handoff, and PRD; it did not apply the Designer README, skill, local helper/references, with-skill output, or old comparison.
- It independently meets the broad accessibility and design-only assertions but lacks lookup reconciliation, canonical artifact depth, and exact role handoff.
- It contains no BRD reference.

## Failures

- None. The first helper attempt was blocked by the default `uv` cache path; rerunning unchanged with `UV_CACHE_DIR=/tmp/issue-198-uv-cache` succeeded.

## Next Steps

- No skill or fixture correction is required for this case.

## Runtime Artifact Policy

- Runtime candidates, fresh baseline, helper diagnostics, and judge evidence remain under the ignored runtime directory and are not committed.
- Only this durable `comparison.md` is updated.
