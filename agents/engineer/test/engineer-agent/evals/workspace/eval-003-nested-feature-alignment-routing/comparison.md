# Eval Result: eval-003-nested-feature-alignment-routing

## Evaluation Target

- Agent: `engineer`
- Skill: `engineer-agent`
- Eval: `eval-003-nested-feature-alignment-routing`
- Test case: nested-feature-alignment-routing
- Workspace: `workspace/eval-003-nested-feature-alignment-routing`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: approved `chat-interface/history-search` PRD/TRD with a small search-ordering change.
- Fresh validation date: 2026-07-31.
- With-skill source: current `agents/engineer/README.md`, current `agents/engineer/skills/engineer-agent/SKILL.md`, eval definition, README, metadata, and same-path PRD/TRD.
- Without-skill source: the same original prompt and fixture only; it was regenerated without reading or applying the skill, Agent README, with-skill output, old comparison, or a previous baseline.

## Latest Result

- Behavior result: PASS
- Coverage result: FULL
- Overall result: PASS

All 5 current assertions were exercised and passed in the with-skill run.

## Assertions

- PASS `resolves_nested_feature_path`: preserves `chat-interface/history-search` and reads the same-path PRD/TRD.
- PASS `does_not_use_sibling_or_parent_only_path`: does not collapse to a sibling or parent-only path.
- PASS `routes_requirement_change_to_pm`: sends approved ordering changes to the PM existing-project-update lane.
- PASS `routes_trd_mismatch_to_trd_gen`: sends missing, stale, or path-mismatched TRDs to `engineer-agent:trd-gen`.
- PASS `does_not_execute_directly`: remains route-only.

## With Skill Behavior

The route resolves the nested feature path from both paths and frontmatter, compares the explicit PRD/TRD sorting contract, routes an expectation change to `pm-agent:idea-to-spec` / `existing-project-update`, and sends technical path or freshness mismatches to `trd-gen`. It does not write a plan, code, or tests.

## Without Skill Baseline

The fresh baseline preserves the exact nested paths, recognizes that the requested ordering needs clarification, and stays route-only. It does not name the PM existing-project-update or `engineer-agent:trd-gen` lanes. Baseline assertion result: 3/5.

## L2-4 Coverage Observation

This scenario validates nested feature alignment rather than the changed frontend/UI, project-bootstrap, or debugger signal groups. No unrelated signal was fabricated, and all current assertions were still exercised.

## Failures

- None.

## Next Steps

- Keep this eval as regression coverage for nested feature-path resolution and same-path alignment.

## Runtime Artifacts Policy

- Fresh runtime evidence is under `tmp/eval-runs/issue-196-l2-3-l2-4/engineer-agent/eval-003-nested-feature-alignment-routing/`.
- `with_skill.md`, `without_skill.md`, and `verdict.md` are scratch evidence and must not be committed.
- This `comparison.md` is the only durable result.
