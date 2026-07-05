# Eval Result: eval-004-greenfield-bootstrap-routing

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-004-greenfield-bootstrap-routing`
- Test case: greenfield-bootstrap-routing
- Workspace: `workspace/iteration-2/eval-4-greenfield-bootstrap-routing`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-05

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: empty-workspace AI chat assistant request; `eval_metadata.json` lists `PRD.md` as execution cleanup for stale runtime output
- Expected output: Phase 0 empty-workspace context summary, PM-first `greenfield-discovery` or `greenfield-bootstrap`, no code scaffold, and PM documentation next step.

## Assertions

- `assertion_1`: empty workspace / docs context first
- `pm_first_lane`: PM-first lane selection
- `pm_first`: no direct engineering scaffold
- `assertion_4`: document-oriented next step

## With Skill

- `idea-to-spec` requires Phase 0 context detection and keeps empty product requests in PM lanes unless the user explicitly opts out.
- Because the user asks for PRD shaping rather than code, the correct lane is `greenfield-bootstrap` or a `greenfield-discovery` first step that may load `project-init` for durable docs.
- `project-init` creates documentation scaffolding only when appropriate and records API / ADR needs as Engineer handoff, not immediate code scaffolding.
- The stale `PRD.md` listed in `execution_cleanup` does not weaken the expected behavior; fresh validation treats cleanup metadata as a signal not to reuse prior runtime output as the answer.

## Without Skill / without_skill Baseline

- The baseline read the eval item and fixture before target skill docs. A generic response could run or recommend `create-next-app`, `npm create vite`, or another scaffold because the layout is concrete.
- It could also accept stale `PRD.md` content without first stating empty-workspace context or PM-first routing.

## Failures

- None. The current `idea-to-spec` and `project-init` contract satisfies all greenfield bootstrap routing assertions.

## Next Steps

- Keep this eval as PM-first coverage for empty-workspace app requests.
- Re-run fresh validation if project-init or stale runtime cleanup behavior changes.

## Runtime Artifacts Policy

- No runtime artifacts were created or committed. Transcripts, verdicts, timing, outputs, and diagnostics must remain outside git.
