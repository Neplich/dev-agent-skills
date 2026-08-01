# Evaluation Comparison: Professional Design System

## Evaluation target

- Skill: `visual-design`
- Eval: `eval-003-professional`
- Test set / fixture version: `evals.json` schema `1.0` on 2026-07-31;
  `evals/workspace/eval-003-professional/eval_metadata.json`, `PM_HANDOFF.md`, and PRD
- Fresh run root:
  `tmp/eval-runs/issue-196-l2-3-4/visual-design/eval-003-professional/`

## Latest result

- Behavior result: **PASS**
- Coverage result: **FULL**
- Overall result: PASS

## Run sources

- With skill:
  `tmp/eval-runs/issue-196-l2-3-4/visual-design/eval-003-professional/with_skill/`
  was generated fresh after reading Designer README, `visual-design/SKILL.md`, its linked local
  design references, the current eval definition, handoff, PRD, and fixture metadata. The local
  Design System Data helper was run and its mismatched lexical suggestions were reconciled against
  the confirmed product context.
- Without skill:
  `tmp/eval-runs/issue-196-l2-3-4/visual-design/eval-003-professional/without_skill/baseline-output.md`
  was regenerated from the original prompt, PM handoff, and PRD only, without reading or applying
  the skill, Designer README, with output, or old comparison.
- Fresh judge:
  `tmp/eval-runs/issue-196-l2-3-4/visual-design/eval-003-professional/judge.md`.

## With-skill behavior

The with-skill artifact defines a restrained enterprise analytics system with explicit WCAG 4.5:1
and 3:1 thresholds, dense-workbench hierarchy, status rules that do not rely on color, and
table/chart/filter/alert coverage. It derives typography, spacing, and component dimensions from
desktop information density and names conditions under which touch-first dimensions must change.
It stops at the Designer-to-Engineer handoff without implementation content.

Assertion results:

- `assertion_1`: **PASS** — WCAG thresholds and enterprise hierarchy are explicit.
- `assertion_2`: **PASS** — there is no component code, style-file change, or engineering command.

## Fresh without-skill baseline

The baseline independently produced an accessible enterprise analytics system. It selected nearly
the same trust palette, type roles, compact spacing progression, and desktop control dimensions,
and tied those values to dense analytical work. It stayed design-only, though it lacked the
canonical feature-scoped artifact structure, detailed state/component coverage, source
reconciliation, and exact Designer handoff wording.

## Font-size and spacing internalization observation

The with-skill and baseline are substantively tied on “font-size/spacing system rationality.” Both
derive a 28/20/16/14/12 hierarchy, 14/20 dense body/control role, 36 px controls, and a
`4, 8, 12, 16, 24, 32` progression from the same high-density desktop context. The skill adds
clearer per-role rationale, compact/default variants, and a platform-change condition, but the
baseline already satisfies the core semantic derivation. Therefore this case has **insufficient
discriminative power** for the L2-3 internalization dimension; the PASS is an assertion result,
not evidence of a meaningful with-skill advantage.

## Failures

None for the current assertions.

## Next steps

- Keep the PASS result, while treating the tied baseline as decision evidence.
- If stronger discrimination is needed, use a fixture whose brand or platform constraints require
  departing from familiar dense-dashboard values and assert the reasoning rather than a particular
  numeric scale.

## Runtime artifact policy

Candidates, baselines, helper output, and judge diagnostics remain under `tmp/eval-runs/` and are
not committed. Only this durable `comparison.md` is committed.
