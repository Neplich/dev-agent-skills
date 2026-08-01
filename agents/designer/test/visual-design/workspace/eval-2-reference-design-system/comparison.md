# Evaluation Comparison: Reference-Driven Design System

## Evaluation target

- Skill: `visual-design`
- Eval: `eval-002-playful`
- Test set / fixture version: `evals.json` schema `1.0` on 2026-08-01; fixture includes a confirmed PM handoff with `feature_path: enterprise-analytics-platform`
- Fresh run root: `tmp/eval-runs/pr-204-fix-round-20260801/visual-design/eval-002-playful/`

## Latest result

- Behavior result: **PASS**
- Coverage result: **FULL**
- Overall result: PASS

Both assertions were exercised against the reachable reference-driven generation path.

## Run sources

- With skill: `with_skill/outputs/design-system-search.md`, `with_skill/docs/design/enterprise-analytics-platform/visual-system.md`, and `with_skill/candidate-output.md` under the fresh run root were generated after reading the current Designer README, router, `visual-design` skill, current eval definition, complete fixture, and required local references. The lookup evidence comes from a fresh run of the local Design System Data helper.
- Without skill: `without_skill/outputs/design-notes.md` was regenerated from an independent copy of the original prompt and fixture only, without applying the Designer README, router, `visual-design` skill, prior baseline, with-skill output, or old comparison.
- Fresh judge: `judge.md` under the fresh run root records assertion-level decisions.

## With-skill behavior and assertion evidence

- `design_system_data`: **PASS** — fresh lookup evidence records the Data-Dense Dashboard result, palette, typography, effects, and anti-patterns. The artifact contains `## 1. Reference-Driven Design System`, identifies `Product category: Enterprise Analytics Dashboard`, selects `Recommended pattern: Data-Dense Dashboard` and `Style direction: Data-Dense + Minimal Trust`, cites Design System Data, and defines color, typography, UX-quality, and anti-pattern sections.
- `assertion_2`: **PASS** — the artifact stops at `## Design Handoff`, names `engineer-agent` as the next role, and contains no CSS/Tailwind/React/shadcn code, install command, or engineering task decomposition.

The artifact adapts rather than blindly copies the query: it rejects the helper's landing-page framing for the confirmed in-product scope and combines its data-dense evidence with the local enterprise product pattern. Font roles, spacing, and component dimensions are derived from high-frequency desktop analytics density.

## Fresh without-skill baseline

The fresh baseline provides a clean professional dashboard direction and generic accessibility advice but explicitly lacks a real local database path or query result. It does not produce the repository's canonical artifact or reference-backed product/style rationale. This preserves the intended contrast without reusing historical baseline text.

## Failures

- None.

## Next steps

- No skill or fixture correction is required from this run.
- Preserve the confirmed PM handoff and the requirement for real local lookup evidence in future runs.

## Runtime artifact policy

Candidates, fresh baseline, lookup evidence, independent input copies, and judge diagnostics remain under `tmp/eval-runs/` and are not committed. Only this durable `comparison.md` is committed.
