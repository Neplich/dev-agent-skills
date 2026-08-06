# Eval Result: eval-002-playful

## Evaluation Target

- Agent: `designer`
- Skill: `visual-design`
- Eval: `eval-002-playful`
- Test case: Reference-Driven Design System
- Workspace: `workspace/eval-2-reference-design-system`

## Test Set or Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: HEAD `a452319`
- Fresh run time: `2026-08-07 00:04:31 +0800`
- Runtime directory: `tmp/eval-runs/issue-198-brd/designer/visual-design/eval-002-playful/`
- Fixture: confirmed PM handoff with `feature_path: enterprise-analytics-platform`

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL** (2/2 assertions exercised)
Overall result: PASS

## Assertion Results (Current)

- design_system_data: **PASS** — the new visual-system.md contains the reference-driven system, enterprise analytics category, Data-Dense Dashboard pattern, Data-Dense + Minimal Trust direction, colors, typography, UX rules, and anti-patterns derived from the local data helper.
- assertion_2: **PASS** — the document contains no implementation code, install command, or engineering task decomposition and ends at engineer-agent handoff.

## With-Skill Behavior (Current)

The candidate consumes the confirmed handoff, runs the local reference lookup,
reconciles it to the in-product analytics scope, and creates the canonical
visual-system artifact without leaking implementation snippets.

## Fresh Without-Skill Baseline (Current)

The baseline was completed before the with-skill root and its local reference
tree existed. It used the same prompt and clean handoff fixture in an independent
top-level workspace under isolated HOME/CODEX_HOME, and produced a generic
visual system without a real Design System Data lookup.

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


Both eval assertions were exercised on the reachable reference-driven generation path.

## Assertion Results

- `design_system_data`: **PASS** — a fresh helper lookup is reconciled into a Reference-Driven Design System with enterprise analytics category, Data-Dense Dashboard pattern, Data-Dense + Minimal Trust style, colors, typography, UX quality rules, and anti-patterns.
- `assertion_2`: **PASS** — output stops at design handoff without CSS/Tailwind/React/shadcn code, install commands, or engineering tasks.

## With-Skill Behavior

- Records the fresh helper's operations-oriented suggestions, then rejects its landing-page/dark-only mismatch in favor of the confirmed in-product data-dense dashboard scope.
- Targets `docs/design/enterprise-analytics-platform/visual-system.md`, removes raw helper implementation snippets, and hands off to Engineer.
- Uses PM handoff and local design evidence only; no BRD is required or cited, and removal causes no tested behavior difference.

## Fresh Without-Skill Baseline

- This baseline was newly generated in this run from only the same prompt and handoff; it did not apply the Designer README, skill, local references/helper, with-skill output, or old comparison.
- It offers a generic professional analytics direction and accessibility rules but cannot provide a real local database query or reference reconciliation.
- It contains no BRD reference.

## Failures

- None. The first helper attempt was blocked by the default `uv` cache path; rerunning unchanged with `UV_CACHE_DIR=/tmp/issue-198-uv-cache` succeeded.

## Next Steps

- No skill or fixture correction is required for this case.

## Runtime Artifact Policy

- Runtime candidates, fresh baseline, helper diagnostics, and judge evidence remain under the ignored runtime directory and are not committed.
- Only this durable `comparison.md` is updated.
