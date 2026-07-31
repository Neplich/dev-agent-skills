# Evaluation Comparison: Minimalist Design System

## Evaluation target

- Skill: `visual-design`
- Eval: `eval-001-minimalist`
- Test set / fixture version: `evals.json` schema `1.0` on 2026-07-31;
  `workspace/eval-1-minimalist/eval_metadata.json`
- Fresh run root:
  `tmp/eval-runs/issue-196-l2-3-4/visual-design/eval-001-minimalist/`

## Latest result

- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
- Overall result: FAIL

Coverage is partial because `assertion_3` (“如果需要实现”) was not exercised: the run stopped
at the missing PM handoff / confirmed `feature_path` gate before an implementable visual system
existed.

## Run sources

- With skill:
  `tmp/eval-runs/issue-196-l2-3-4/visual-design/eval-001-minimalist/with_skill/candidate-output.md`
  was generated fresh after reading Designer README, `visual-design/SKILL.md`, the current eval
  definition, and this fixture metadata.
- Without skill:
  `tmp/eval-runs/issue-196-l2-3-4/visual-design/eval-001-minimalist/without_skill/baseline-output.md`
  was regenerated from the original prompt and fixture only, without reading or applying the
  skill, Designer README, with-skill output, or an earlier comparison.
- Fresh judge:
  `tmp/eval-runs/issue-196-l2-3-4/visual-design/eval-001-minimalist/judge.md`.

## With-skill behavior

The skill enforced its entry and feature-path gates. Because the prompt and fixture supply neither
a PM/design handoff nor a confirmed `feature_path`, it returned the request to `pm-agent` and
created no design artifact. It stayed strictly design-only.

Assertion results:

- `assertion_1`: **FAIL** — no canonical `visual-system.md` could be written without inventing a
  feature path.
- `assertion_2`: **PASS** — no token code, CSS/component implementation, task decomposition, or
  test commands were produced.
- `assertion_3`: **NOT EXERCISED** — implementation handoff was not yet applicable.

## Fresh without-skill baseline

The baseline generated a standalone visual note with a coherent color system, type scale, compact
spacing progression, component dimensions, copy guidance, accessibility requirements, and a
generic engineering handoff. It did not know or enforce the repository's PM/feature-path gate and
did not write the canonical path.

## Font-size and spacing internalization observation

On the narrow “font-size/spacing system rationality” dimension, the baseline is stronger than the
blocked with-skill output because it actually derives a 28/20/16/14 role scale and a compact
4-point progression from the professional productivity context. The with-skill run provides no
type/spacing system because the required handoff is absent. This is fixture/gate behavior, not
evidence that the skill internalized the new density-derived rule.

## Failures

- The output assertion requires a document whose path comes from a confirmed `feature_path`, but
  this fixture supplies no handoff or feature path.
- The implementation-handoff assertion is conditional and was not triggered.

## Next steps

- Align the fixture with the current entry gate by adding a confirmed PM/design handoff and
  `feature_path`, or change the assertion set to evaluate the expected blocked route.
- Re-run both fresh candidates after that alignment; do not reinterpret this run as a generated
  design-system pass.

## Runtime artifact policy

Candidates, baselines, and judge diagnostics remain under `tmp/eval-runs/` and are not committed.
Only this durable `comparison.md` is committed.
