# Eval Result: eval-002-existing-project-update

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-002-existing-project-update`
- Test case: existing-project-update
- Workspace: `workspace/iteration-1/eval-2-existing-project-update`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-05

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: approved notification-center PRD, DECISIONS, and Engineer TRD covering a polling baseline and event-driven migration direction
- Expected output: recognize `existing-project-update`, summarize delta and blast radius first, prefer `change-impactor` / iteration over full regeneration, and name affected docs.

## Assertions

- `update`: recognize existing update
- `delta_blast_radius`: start with delta and blast radius
- `assertion_3`: prefer iteration over rewrite
- `assertion_4`: name affected feature docs or document types

## With Skill

- `idea-to-spec` selects `existing-project-update` when approved behavior, rollout, or scope changes.
- The shared skill map requires `change-impactor` first when blast radius is unclear, then targeted iteration rather than full regeneration.
- The fixture docs establish the affected paths: `docs/pm/notification-center/PRD.md`, `docs/pm/notification-center/DECISIONS.md`, and `docs/engineer/notification-center/TRD.md`.
- The current docs preserve the hybrid event-driven transition and rejected permanent polling-only option, so the update path can describe delta, impacted docs, and revision order without reopening unrelated decisions.

## Without Skill / without_skill Baseline

- The baseline read the eval item and fixture before target skill docs. A generic response could treat the request as a net-new design or rewrite the PRD/TRD wholesale.
- It may miss the decision-history requirement to revise or retire the prior polling decision instead of silently replacing it.

## Failures

- None. The current `idea-to-spec` and `change-impactor` routing satisfy all update assertions.

## Next Steps

- Keep this eval as existing-project update coverage.
- Re-run fresh validation if change impact, iteration ordering, or document-memory rules change.

## Runtime Artifacts Policy

- No runtime artifacts were created or committed. Transcripts, verdicts, timing, outputs, and diagnostics must remain outside git.
