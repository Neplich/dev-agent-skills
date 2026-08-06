# Eval Result: eval-001-route-design-handoff

## Evaluation Target

- Agent: `designer`
- Skill: `designer-agent`
- Eval: `eval-001-route-design-handoff`
- Workspace: `workspace/eval-1-route-design-handoff`
- Review context: issue #196 L2-4 router single-table convergence
- Latest run: fresh isolated paired Codex validation and independent judge on 2026-08-07

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt and assertions: current `agents/designer/test/designer-agent/evals/evals.json`
- Fixture: `docs/pm/billing-notifications/PRD.md`
- With-skill source: current Designer README, `designer-agent/SKILL.md`, eval definition, fixture, and the referenced PM handoff/closeout contract; historical comparison was not read before candidate generation.
- Without-skill source: the same prompt and fixture in an isolated directory, without reading or applying Designer README, `designer-agent/SKILL.md`, with-skill output, assertions, historical comparison, or an old baseline.

## Latest Result

- Behavior result: **FAIL**
- Coverage result: **FULL** (5/5 declared assertions exercised)
Overall result: FAIL

## Assertion Results (Current)

- routes_ux_first: **PASS** — the current final response routes first to ui-ux-design for flow and interaction work.
- routes_visual_followup: **FAIL** — visual-design is second, but the response omits the required color, typography, and copy-tone scope.
- uses_real_output_filenames: **FAIL** — neither canonical design filename is named.
- stops_before_code: **FAIL** — no code was written, but the response does not explicitly refuse React, tests, scripts, and deployment work.
- hands_off_to_engineer: **PASS** — React implementation is assigned to engineer-agent after design.

## With-Skill Behavior (Current)

The candidate honors the PM gate and selects the two design specialists, but it
does not emit the full router contract: canonical filenames and an explicit
multi-surface engineering refusal are missing.

## Fresh Without-Skill Baseline (Current)

The baseline was regenerated before the with-skill root existed, using the
same prompt and clean fixture in an independent top-level workspace with an
isolated HOME/CODEX_HOME. It implemented a React/Vite page, clearly
differentiating the router boundary, but its behavior does not affect the
with-skill verdict.

## Failures (Current)

- Missing canonical ui-ux-spec.md and visual-system.md filenames.
- Incomplete visual-design scope and no explicit refusal covering all forbidden engineering surfaces.

## Next Steps (Current)

- Fix the router response discipline, then rerun this eval with the same isolation protocol.

## Runtime Artifact Policy (Current)

- Runtime lanes and judge evidence remain in independent /tmp workspaces and are not committed.
- Only this durable comparison is updated.

## Historical Result (Superseded: pre-#234 contract)

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
