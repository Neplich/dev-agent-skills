# Eval Result: eval-003-with-reference

## Evaluation Target

- Agent: `designer`
- Skill: `ui-ux-design`
- Eval: `eval-003-with-reference`
- Test case: Design with Reference Website
- Workspace: `workspace/eval-003-with-reference`

## Test Set or Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: HEAD `a452319`
- Fresh run time: `2026-08-07 00:04:31 +0800`
- Runtime directory: `tmp/eval-runs/issue-198-brd/designer/ui-ux-design/eval-003-with-reference/`
- Fixture: confirmed PM handoff, PRD, and stable Linear reference-pattern record

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL** (2/2 assertions exercised)
Overall result: PASS

## Assertion Results (Current)

- assertion_1: **PASS** — the fresh ui-ux-spec.md extracts Linear navigation, hero, workflow, CTA, and motion patterns with an explicit adaptation boundary.
- assertion_2: **PASS** — the output stops at UI/UX specification and creates no frontend implementation artifacts.

## With-Skill Behavior (Current)

The candidate uses the confirmed PM scope and stable reference record, verifies
the live reference, produces the canonical artifact, and remains in design-only
scope.

## Fresh Without-Skill Baseline (Current)

The baseline was generated before the with-skill root existed, using the same
prompt and fixture in an independent top-level workspace under isolated
HOME/CODEX_HOME. It also meets the broad assertions but is less disciplined
about canonical structure and confirmed-source use.

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


Both assertions were exercised on the reachable reference-backed design path.

## Assertion Results

- `assertion_1`: **PASS** — the candidate extracts restrained navigation, hero hierarchy, progressive workflow sections, product proof, CTA rhythm, purposeful motion, and mobile stacking from the stable reference record.
- `assertion_2`: **PASS** — it stops after the design artifact and does not enter frontend implementation.

## With-Skill Behavior

- Produces `docs/design/productivity-app-landing/ui-ux-spec.md` with reference analysis, user journey, inventory, ASCII layouts, CTA states, and responsive behavior.
- Explicitly forbids copying Linear branding, copy, screenshots, icons, product names, or feature scope.
- Uses PRD, handoff, and the stable reference note only; no BRD is requested or cited, so BRD removal causes no tested behavior difference.

## Fresh Without-Skill Baseline

- This baseline was newly generated in this run from only the same prompt, fixture handoff, PRD, and stable reference note; it did not apply the skill/README or reuse historical output.
- It satisfies the two broad assertions but gives less explicit repository artifact structure, adaptation boundary, and handoff discipline.
- It contains no BRD reference.

## Failures

- None.

## Next Steps

- No skill or fixture correction is required for this case.

## Runtime Artifact Policy

- Runtime candidates, fresh baseline, and judge evidence remain under the ignored runtime directory and are not committed.
- Only this durable `comparison.md` is updated.
