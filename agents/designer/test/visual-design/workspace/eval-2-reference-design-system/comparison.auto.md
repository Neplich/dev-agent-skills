# Eval 2: reference-driven-design-system

## Prompt

Create a visual design system for an enterprise analytics platform. Target users are operations leaders and analysts. The output should use local Design System Data to choose product pattern, style direction, color system, typography, UX quality rules, and anti-patterns. Stop at design handoff and do not produce implementation code.

## Expected Assertions

- `with_skill_uses_local_design_system_data`: With skill records a real Design System Data query output from the local database
- `with_skill_uses_reference_driven_system`: With skill output includes reference-backed product, style, color, typography, UX, and anti-pattern reasoning
- `with_skill_stops_at_handoff`: With skill output remains design-only and routes implementation to Engineer
- `without_skill_stays_generic`: Baseline output lacks reference-driven design system reasoning

## Output Presence Check

### With Skill

- [PASS] `with_skill/outputs/design-system-search.md`
- [PASS] `with_skill/docs/design/enterprise-analytics-platform/visual-system.md`

### Without Skill

- [PASS] `without_skill/outputs/design-notes.md`

## Assertion Checks

- [PASS] `with_skill_uses_local_design_system_data`: With skill records a real Design System Data query output from the local database
  - All checks passed
- [PASS] `with_skill_uses_reference_driven_system`: With skill output includes reference-backed product, style, color, typography, UX, and anti-pattern reasoning
  - All checks passed
- [PASS] `with_skill_stops_at_handoff`: With skill output remains design-only and routes implementation to Engineer
  - All checks passed
- [PASS] `without_skill_stays_generic`: Baseline output lacks reference-driven design system reasoning
  - All checks passed

## Notes

- Fill in qualitative comparison after reviewing transcripts and design docs.
