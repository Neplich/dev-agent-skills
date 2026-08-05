# Eval Result: eval-001-route-design-handoff

## Evaluation Target

- Agent: `designer`
- Skill: `designer-agent`
- Eval: `eval-001-route-design-handoff`
- Workspace: `workspace/eval-1-route-design-handoff`
- Review context: issue #196 L2-4 router single-table convergence
- Latest run: fresh paired Codex validation on 2026-07-31

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt and assertions: current `agents/designer/test/designer-agent/evals/evals.json`
- Fixture: `docs/pm/billing-notifications/PRD.md`
- With-skill source: current Designer README, `designer-agent/SKILL.md`, eval definition, fixture, and the referenced PM handoff/closeout contract; historical comparison was not read before candidate generation.
- Without-skill source: the same prompt and fixture in an isolated directory, without reading or applying Designer README, `designer-agent/SKILL.md`, with-skill output, assertions, historical comparison, or an old baseline.

## Latest Result

- Behavior result: PASS
- Coverage result: FULL (5/5 declared assertions exercised)
Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


The L2-4 fallback for “范围已确认但设计类型模糊” is present in the current single `Default Routes` table. This fixture asks explicitly for both flow and visual style, so it does not exercise that fallback; no fallback behavior was inferred or counted as dynamic evidence.

## Assertion Results

| Assertion | With skill | Without skill | Evidence |
| --- | --- | --- | --- |
| `routes_ux_first` | PASS | FAIL | With skill explicitly starts with `ui-ux-design`; baseline gives generic design steps without the repository specialist route. |
| `routes_visual_followup` | PASS | FAIL | With skill explicitly follows with `visual-design`; baseline describes visual work but does not name the specialist. |
| `uses_real_output_filenames` | PASS | FAIL | With skill names both canonical files; baseline names no durable design output file. |
| `stops_before_code` | PASS | PASS | Both honor the prompt's explicit no-implementation boundary. |
| `hands_off_to_engineer` | PASS | FAIL | With skill explicitly hands implementation to `engineer-agent`; baseline only stops before implementation. |

## With-Skill Behavior

The candidate preserves `billing-notifications`, routes `ui-ux-design` before
`visual-design`, names `docs/design/billing-notifications/ui-ux-spec.md` and
`docs/design/billing-notifications/visual-system.md`, refuses React, tests,
scripts, and deployment work, and hands implementation to `engineer-agent`.
All 5 assertions pass.

## Without-Skill Baseline

The fresh baseline gives a reasonable generic design sequence and obeys the
explicit request not to implement React. It does not express the repository's
specialist names, canonical artifact filenames, or named Engineer handoff.
This provides useful differentiation on router-specific behavior.

## Failures

- None in the with-skill candidate.

## Next Steps

- Keep this eval as regression coverage for the two-specialist sequence, durable artifact names, design-only boundary, and Engineer handoff.
- Add a separate fixture only if maintainers later choose to dynamically cover the confirmed-scope/ambiguous-design fallback; this run does not fabricate that scenario.

## Runtime Artifacts Policy

Paired runtime evidence is stored only under
`tmp/eval-runs/issue-196-l2-3-4/designer-agent/eval-001-route-design-handoff/`
as `with_skill/candidate-output.md` and
`without_skill/baseline-output.md`. Runtime outputs, transcripts, verdicts,
timing data, and diagnostics must not be committed. This `comparison.md` is the
durable result.
