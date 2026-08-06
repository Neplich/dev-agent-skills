# Eval Result: eval-002-feature-path-design-handoff

## Evaluation Target

- Agent: `designer`
- Skill: `designer-agent`
- Eval: `eval-002-feature-path-design-handoff`
- Workspace: `workspace/eval-2-feature-path-design-handoff`
- Review context: issue #196 L2-4 router single-table convergence
- Latest run: fresh isolated paired Codex validation and independent judge on 2026-08-07

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt and assertions: current `agents/designer/test/designer-agent/evals/evals.json`
- Fixture documents: same-path PRD and TRD for `chat-interface/messages/history/search`
- With-skill source: current Designer README, `designer-agent/SKILL.md`, eval definition, fixture, and the referenced PM handoff/closeout contract; historical comparison was not read before candidate generation.
- Without-skill source: the same prompt and fixture in an isolated directory, without reading or applying Designer README, `designer-agent/SKILL.md`, with-skill output, assertions, historical comparison, or an old baseline.

## Latest Result

- Behavior result: **FAIL**
- Coverage result: **FULL** (4/4 declared assertions exercised)
Overall result: FAIL

## Assertion Results (Current)

- uses_confirmed_feature_path: **PASS** — the full four-level path and same-path PRD/TRD are preserved.
- mirrors_design_outputs: **FAIL** — ui-ux-spec.md is generated, but visual-system.md is absent.
- no_synonym_top_level: **PASS** — no synonym or truncated design directory is created.
- stops_before_code: **PASS** — the candidate stops at design handoff and routes implementation to engineer-agent.

## With-Skill Behavior (Current)

The candidate correctly preserves the canonical feature path and design-only
boundary, but narrows the request to UI/UX and omits the required visual-system
artifact.

## Fresh Without-Skill Baseline (Current)

The baseline was regenerated before the with-skill root existed, from the same
prompt and clean fixture under an isolated HOME/CODEX_HOME. It produced a
non-canonical design/code-style deliverable; this is comparison evidence only.

## Failures (Current)

- Missing docs/design/chat-interface/messages/history/search/visual-system.md.

## Next Steps (Current)

- Align router behavior with the two-artifact assertion, then rerun.

## Runtime Artifact Policy (Current)

- Runtime lanes and judge evidence remain in independent /tmp workspaces and are not committed.
- Only this durable comparison is updated.

## Historical Result (Superseded: pre-#234 contract)

- Behavior result: PASS
- Coverage result: FULL (4/4 declared assertions exercised)
Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


The current prompt supplies a precise four-level feature path and asks for UI/UX and visual artifacts. It therefore does not exercise the L2-4 “范围已确认但设计类型模糊” fallback; no fallback result is inferred from this fixture.

## Assertion Results

| Assertion | With skill | Without skill | Evidence |
| --- | --- | --- | --- |
| `uses_confirmed_feature_path` | PASS | PASS | Both preserve the full path and use the same-path PRD/TRD as design inputs. |
| `mirrors_design_outputs` | PASS | FAIL | With skill uses canonical `ui-ux-spec.md` and `visual-system.md`; baseline invents `UI_UX_SPEC.md` and `VISUAL_SPEC.md`. |
| `no_synonym_top_level` | PASS | PASS | Neither candidate creates a synonym or truncated top-level directory. |
| `stops_before_code` | PASS | PASS | Both stop at design delivery without code, commands, tests, or patches. |

## With-Skill Behavior

The candidate treats `chat-interface/messages/history/search` as the only
feature path, references its exact PRD/TRD, mirrors the complete path under
`docs/design/`, names both canonical design files, and stops before
implementation. All 4 assertions pass.

## Without-Skill Baseline

The fresh baseline preserves the multi-level path and respects the explicit
no-implementation instruction, so it is strong on facts already stated in the
prompt. It fails the repository artifact-name contract by inventing
`UI_UX_SPEC.md` and `VISUAL_SPEC.md`. The skill's differentiating value in this
case is exact durable naming rather than path preservation.

## Failures

- None in the with-skill candidate.

## Next Steps

- Keep this eval as regression coverage for full feature-path mirroring and canonical design artifact names.
- Do not reinterpret the explicit design layers in this fixture as coverage of the ambiguous-design fallback.

## Runtime Artifacts Policy

Paired runtime evidence is stored only under
`tmp/eval-runs/issue-196-l2-3-4/designer-agent/eval-002-feature-path-design-handoff/`
as `with_skill/candidate-output.md` and
`without_skill/baseline-output.md`. Runtime outputs, transcripts, verdicts,
timing data, and diagnostics must not be committed. This `comparison.md` is the
durable result.
