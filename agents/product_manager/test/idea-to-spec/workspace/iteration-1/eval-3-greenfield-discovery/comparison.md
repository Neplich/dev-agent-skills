# Eval Result: eval-003-greenfield-discovery

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-003-greenfield-discovery`
- Test case: greenfield-discovery
- Workspace: `workspace/iteration-1/eval-3-greenfield-discovery`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-05

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: vague team knowledge Q&A idea with minimal notes and no formal docs or technical stack
- Expected output: stay in `greenfield-discovery`, avoid full PRD/TRD generation, use one-decision discovery, and recommend document generation only after direction stabilizes.

## Assertions

- `assertion_1`: no complete document on the first turn
- `assertion_2`: use exploratory single-decision protocol
- `assertion_3`: recommend documentation after the direction stabilizes

## With Skill

- `idea-to-spec` maps vague ideas and near-empty workspaces to `greenfield-discovery`.
- Its non-negotiable protocol blocks immediate full PRD/TRD generation and advances one decision point at a time.
- It keeps the feature path unresolved until problem, users, scope, constraints, and assumptions are stable enough to document.
- It can recommend future PRD / DECISIONS documentation, but only after the discovery direction is confirmed.

## Without Skill / without_skill Baseline

- The baseline read the eval item and fixture before target skill docs. A generic PM response could produce a premature PRD outline or implementation plan from the vague idea.
- It may ask several broad questions at once rather than using a single focused decision point.

## Failures

- None. The current `idea-to-spec` protocol satisfies all greenfield discovery assertions.

## Next Steps

- Keep this eval as first-turn discovery discipline coverage.
- Re-run fresh validation if greenfield lane selection or document timing changes.

## Runtime Artifacts Policy

- No runtime artifacts were created or committed. Transcripts, verdicts, timing, outputs, and diagnostics must remain outside git.
