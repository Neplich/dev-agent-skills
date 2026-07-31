# Evaluation Comparison: Reference-Driven Design System

## Evaluation target

- Skill: `visual-design`
- Eval: `eval-002-playful`
- Test set / fixture version: `evals.json` schema `1.0` on 2026-07-31;
  `workspace/eval-2-reference-design-system/eval_metadata.json`
- Fresh run root:
  `tmp/eval-runs/issue-196-l2-3-4/visual-design/eval-002-playful/`

## Latest result

- Behavior result: **FAIL**
- Coverage result: **FULL**
- Overall result: FAIL

## Run sources

- With skill:
  `tmp/eval-runs/issue-196-l2-3-4/visual-design/eval-002-playful/with_skill/candidate-output.md`
  was generated fresh after reading Designer README, `visual-design/SKILL.md`, current eval
  definitions, and fixture metadata.
- Without skill:
  `tmp/eval-runs/issue-196-l2-3-4/visual-design/eval-002-playful/without_skill/baseline-output.md`
  was regenerated from the same original prompt and fixture only, without the skill, Designer
  README, with output, or old comparison.
- Fresh judge:
  `tmp/eval-runs/issue-196-l2-3-4/visual-design/eval-002-playful/judge.md`.

## With-skill behavior

The skill stopped before reference lookup and document generation because the fixture has no
PM/design handoff and no confirmed `feature_path`. It did not fabricate a synonym directory or
claim a database result. It produced no implementation content.

Assertion results:

- `design_system_data`: **FAIL** — no query record or reference-driven design artifact was
  generated after the entry gate blocked the run.
- `assertion_2`: **PASS** — the output contains no CSS/Tailwind/React/shadcn code, install command,
  or engineering task list.

## Fresh without-skill baseline

The baseline honestly reported that the supplied fixture does not identify a local database path.
It still inferred a professional data-dense dashboard, conservative semantic colors, readable
typography, accessibility rules, and enterprise-specific anti-patterns, then stopped without
implementation. It did not claim a real local query or produce the canonical design artifact.

## Font-size and spacing internalization observation

Neither output exercised a complete font-size/spacing system. The with-skill run was gate-blocked,
and the baseline stayed at typography/density principles without numeric role definitions.
Accordingly, this eval provides no discriminative evidence for the new density-derived
font-size/spacing contract.

## Failures

- The scenario does not provide the handoff and feature path needed to trigger the asserted local
  reference lookup and `visual-system.md` generation.

## Next steps

- Add a confirmed handoff and `feature_path` fixture if this eval is intended to test the
  reference-driven generation path; otherwise align the assertions to the expected gate block.
- Preserve the requirement that a real lookup result—not a fabricated reference—is evaluated.

## Runtime artifact policy

Candidates, baselines, and judge diagnostics remain under `tmp/eval-runs/` and are not committed.
Only this durable `comparison.md` is committed.
