# Eval Result: eval-001-route-ci-readiness

## Evaluation Target

- Agent: `devops`
- Skill: `devops-agent`
- Eval: `eval-001-route-ci-readiness`
- Test case: route-ci-readiness
- Workspace: `workspace/eval-1-route-ci-readiness`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-08 for PR #98 trigger description routing review.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: existing `deploy/docker` path with missing GitHub Actions PR gate and later config/runbook concerns.
- Validation date: 2026-07-08.
- Review context: PR #98 trigger description routing review.
- Context read before applying the skill: `AGENTS.md`, `agents/devops/README.md`, `agents/devops/skills/devops-agent/SKILL.md`, `evals.json`, workspace `eval_metadata.json`, `deploy/docker/README.md`, and `agents/product_manager/skills/idea-to-spec/_internal/_shared/skill-map.md`.

## Assertions

- PASS `routes_primary_to_cicd`: the current missing PR gate routes to `cicd-bootstrap`.
- PASS `keeps_deployment_context`: the existing `deploy/docker` context is preserved rather than replaced with greenfield deployment planning.
- PASS `names_followups`: environment coverage remains an `env-config-auditor` follow-up and rollback docs remain an `incident-playbook-writer` follow-up.
- PASS `does_not_run_all_skills`: the route separates the current primary route from later DevOps checks.
- PASS `does_not_write_workflow`: route-only work does not create `.github/workflows` files.

## With Skill Behavior

`devops-agent` satisfies the CI readiness route. The eval provides confirmed route-only DevOps context: the service already has `deploy/docker`, and the missing piece is GitHub Actions PR readiness. The router selects the narrow current owner `cicd-bootstrap`, carries forward `deploy/docker`, and does not restart deployment planning from zero.

The router names `env-config-auditor` for later environment-variable coverage review and `incident-playbook-writer` for later rollback documentation. Those remain explicit follow-ups, not automatic execution. The route-only instruction prevents writing `.github/workflows` files during this eval.

## Without Skill Baseline

Fresh `without_skill` baseline generated on 2026-07-08 from only the eval prompt and fixture facts, without applying `agents/devops/README.md`, `agents/devops/skills/devops-agent/SKILL.md`, historical `comparison.md`, or any old baseline output.

A generic no-skill response would likely recognize GitHub Actions as important and may mention environment-variable review and rollback docs. It is weaker on the skill-specific behavior: it may blur routing with implementation, sketch workflow YAML despite "不要直接写 workflow", restart deployment planning despite existing `deploy/docker`, or bundle CI, config audit, and runbook work into one broad DevOps pass instead of selecting `cicd-bootstrap` now and naming the other two as follow-ups.

## Failures

- None found.
- No PR #98 trigger description routing regression found: CI readiness still routes to `cicd-bootstrap`; config audit and runbook work remain follow-ups; no workflow files are written.

## Next Steps

- Keep this eval as regression coverage for DevOps primary-route selection and follow-up separation.
- Keep the PR #98 trigger description behavior covered by checking that DevOps trigger text still preserves route-only behavior, existing deployment context, and explicit follow-up separation.

## Runtime Artifacts Policy

- Runtime evidence for this validation was written only under `tmp/eval-runs/2026-07-08-router-trigger-batch4-final/eval-001-route-ci-readiness/`:
  - `with_skill.md`
  - `without_skill.md`
  - `verdict.md`
- These files are scratch runtime artifacts and must not be committed.
- Runtime transcripts, verdicts, timing, output directories, diagnostics, and generated with_skill / without_skill files must not be copied into the fixture workspace.
