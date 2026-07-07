# Eval Result: pm-agent-missing-handoff-target-unavailable

## Evaluation Target

- Skill: `pm-agent`
- Test case: missing-handoff-target-unavailable
- Test set: PM entry evals for issue #52 / #62 missing target coverage, refreshed after PR #98 trigger description revisions
- Entry: workspace `eval-9-missing-handoff-target-unavailable`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-08 after PR #98 trigger description revisions

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: confirmed design handoff with missing `designer-agent`
- Expected output: mark handoff blocked, name missing capability, and do not perform Designer responsibilities inside PM.
- Validation run: fresh Codex subagent, 2026-07-08, using the same eval prompt and fixture.

## Assertions

- PASS `detect_missing_target`: The route detects that `designer-agent` or the required design capability is unavailable.
- PASS `mark_handoff_blocked`: The handoff stage is marked `blocked` with the missing plugin / capability named.
- PASS `do_not_perform_missing_role`: PM does not produce Designer visual specifications or design deliverables itself.

## With Skill Behavior

- Fresh with_skill validation applied `pm-agent` and the Product Manager Agent README on 2026-07-08.
- The `pm-agent` missing handoff target rule detects unavailable downstream agents or skills.
- It names the missing `designer-agent` capability, marks that handoff stage as `blocked`, and records the blocker.
- It does not substitute for Designer by producing visual specifications or design deliverables; the Designer boundary evidence keeps visual-system output owned by `designer-agent`.
- The PR #98 trigger description revisions do not weaken the missing-target handoff behavior.

## Without Skill Baseline

- Fresh without_skill baseline regenerated on 2026-07-08 from the same eval prompt and fixture without applying or citing `pm-agent` or the Product Manager Agent README.
- A generic assistant can infer that a missing `designer-agent` should be installed or enabled before the design handoff continues, but it has no durable PM handoff protocol to require a `blocked` stage marker.
- It may offer interim design guidance or a lightweight visual-spec outline despite the unavailable target, so it is less reliable on the `do_not_perform_missing_role` boundary than the with_skill path.

## Failures

- None. The current missing-target rule satisfies all assertions.
- No PR #98 regression found; unavailable handoff targets remain hard blockers and PM does not perform missing Designer responsibilities.

## Next Steps

- Keep this eval as coverage for unavailable cross-agent handoff targets.
- Re-run fresh validation if plugin availability handling changes.

## Runtime Artifacts Policy

- No runtime artifacts were created or committed. Transcripts, verdicts, timing, outputs, and diagnostics must remain outside git.
