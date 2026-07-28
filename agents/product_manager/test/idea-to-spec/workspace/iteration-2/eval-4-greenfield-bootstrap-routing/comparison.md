# Eval Result: eval-004-greenfield-bootstrap-routing

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-004-greenfield-bootstrap-routing`
- Test case: greenfield-bootstrap-routing
- Workspace: `workspace/iteration-2/eval-4-greenfield-bootstrap-routing`

## Test Set / Fixture Version

- Evaluation date: `2026-07-28`
- Schema: `evals.json` v1.0
- Fixture: empty-workspace AI chat assistant request; stale root `PRD.md` was excluded through `execution_cleanup`.
- Run: fresh Codex evaluator with a separately isolated, newly generated `without_skill` baseline.

## Latest Result

**PASS** — all 4 assertions passed. The response starts with the empty-workspace context, selects a PM-first `greenfield-bootstrap` lane, explicitly rejects engineering scaffolding, and names durable PM documents as the next step.

## With-Skill Behavior

- Did not reuse the stale root PRD or infer an existing stack.
- Explicitly avoided `npm create vite`, `create-next-app`, and equivalent scaffolds.
- Proposed `project-init`, `DECISIONS.md`, and `PRD.md` only after the first product-positioning decision is confirmed.
- Kept the proposed `feature_path` provisional.

## Without-Skill Baseline

- Source: fresh isolated subagent run using the same prompt and cleaned fixture without the target skill, PM Agent README, internal instructions, or historical comparison.
- The baseline also avoided engineering setup, but immediately produced a broad PRD skeleton and multiple unresolved questions; the with-skill response follows the single-decision and durable-doc gate more strictly.

## Failures

- No assertion failures or baseline blockers.
- PR #163's post-Docs deployment completeness check did not apply because no docs-site bootstrap or confirmed commit occurred.

## Next Steps

- Keep this eval as PM-first empty-workspace routing coverage.
- Re-run when `project-init`, execution cleanup, or Docs completion routing changes.

## Runtime Artifacts Policy

- Responses, verdicts, timing, and diagnostics remain under `tmp/eval-runs/idea-to-spec-v0.3.4/` and are not committed.
