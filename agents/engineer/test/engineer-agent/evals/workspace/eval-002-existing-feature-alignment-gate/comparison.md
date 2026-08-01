# Eval Result: eval-002-existing-feature-alignment-gate

## Evaluation Target

- Agent: `engineer`
- Skill: `engineer-agent`
- Eval: `eval-002-existing-feature-alignment-gate`
- Test case: existing-feature-alignment-gate
- Workspace: `workspace/eval-002-existing-feature-alignment-gate`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: small existing-feature behavior change request for Notification Center archived items.
- Fresh validation date: 2026-07-31.
- With-skill source: current `agents/engineer/README.md`, current `agents/engineer/skills/engineer-agent/SKILL.md`, eval definition, and workspace metadata.
- Without-skill source: the same original prompt and fixture only; it was regenerated without reading or applying the skill, Agent README, with-skill output, old comparison, or a previous baseline.

## Latest Result

- Behavior result: PASS
- Coverage result: FULL
- Overall result: PASS

All 6 current assertions were exercised and passed in the with-skill run.

## Assertions

- PASS `reads_product_and_engineer_docs`: requires same-feature PRD, TRD, and existing product decision records.
- PASS `classifies_expectation_change`: treats archived items entering active as a possible approved-expectation change.
- PASS `routes_to_existing_project_update`: sends conflicts to `pm-agent:idea-to-spec` through `existing-project-update`.
- PASS `routes_trd_gap_to_trd_gen`: sends missing, stale, or incomplete technical coverage to `engineer-agent:trd-gen` with a gap packet.
- PASS `requires_plan_after_alignment`: keeps the confirmed implementation-plan gate after alignment.
- PASS `does_not_route_directly_to_implementation`: does not accept "small change" as permission to bypass alignment.

## With Skill Behavior

The route requires the PRD, TRD, and present decision records before selecting implementation. It identifies the requested active/archived behavior as a possible expectation change, distinguishes PM conflict from a TRD gap, and leaves `feature-implementor` blocked until same-path alignment and a confirmed implementation plan exist.

## Without Skill Baseline

The fresh baseline recognizes that the behavior may require product confirmation and generically asks for PRD/TRD review. It omits decision records, the named PM existing-project-update lane, the TRD gap packet and specialist, and the mandatory confirmed implementation-plan gate. Baseline assertion result: 1/6.

## L2-4 Coverage Observation

This scenario validates existing-feature alignment. It does not trigger the new frontend/UI or debugger signal wording, and no unrelated signal was invented. That does not reduce coverage of this eval's current assertions.

## Failures

- None.

## Next Steps

- Keep this eval as regression coverage for existing-feature alignment and user attempts to bypass PM/TRD gates.

## Runtime Artifacts Policy

- Fresh runtime evidence is under `tmp/eval-runs/issue-196-l2-3-l2-4/engineer-agent/eval-002-existing-feature-alignment-gate/`.
- `with_skill.md`, `without_skill.md`, and `verdict.md` are scratch evidence and must not be committed.
- This `comparison.md` is the only durable result.
