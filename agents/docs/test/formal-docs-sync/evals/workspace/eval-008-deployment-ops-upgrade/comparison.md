# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-008-deployment-ops-upgrade`
- Review context: issue #150 fresh paired eval group A

## Test Set / Fixture Version

- Fixture: pristine `workspace/eval-008-deployment-ops-upgrade` snapshot used by issue #150
- Evidence set: confirmed deployment handoff, TRD surface, Compose configuration, executed deployment results, environment differences, and future-only deployment plan
- Actual validation date: `2026-07-21`

## Latest Result

**PASS (5/5 assertions)** — the with-skill lane synchronized only the current Compose runbook, upgrade, health, and rollback facts, excluded unexecuted Kubernetes/Helm plans, passed host checks, and handed off #117.

## Assertions

- `uses_executed_deployment_evidence`: PASS. Current claims were derived from `deploy/compose.yaml`, recorded command exits/health results, and environment differences rather than the TRD or plan alone.
- `writes_current_ops_upgrade_rollback`: PASS. The page records default image `v1.4.2`, Compose start/upgrade, `/healthz` HTTP 200 success, and rollback to `v1.4.1` followed by the same health check.
- `does_not_promote_plan_to_current_state`: PASS. Kubernetes and Helm are explicitly identified as unexecuted planning and excluded from current support.
- `keeps_ops_scope_atomic_and_unverified`: PASS. The only pristine content delta was the target ops page; the already-correct `deploy/**` map entry was preserved, the page is `unverified`, and product/design/database/Release Notes stayed unchanged.
- `runs_ops_host_checks_and_handoffs`: PASS. `npm run test:docs` exited `0`, 74/74 Node tests passed, and the affected set was handed to `docs-agent:docs-audit` (#117) without executing deployment.

## With-Skill Behavior

- Loaded only the host ops template and ops type module after validating the deployment-verification entry basis and confirmed atomic scope.
- Read-back confirmed the exact current commands, image tags, environment ports, health success criteria, rollback, and future-plan exclusion.
- The #117 handoff remains blocked for pre-tag stamping until a maintainer supplies a confirmed `target_release_version`; refs and runtime image tags were not treated as authorization.
- The runtime Git wrapper isolated exact-tag discovery from the outer worktree while leaving other Git-backed docs checks intact.

## Fresh Without-Skill Baseline

- Source: fresh `without_skill` lane from the same pristine fixture and prompt/assertions; it did not read the target skill, Docs README, internal instructions, old comparison, or with-skill output.
- The baseline produced the correct runbook from the strong executed-evidence fixture, excluded Kubernetes/Helm, preserved scope, and passed host checks.
- It did not fully articulate the #117 handoff's confirmed-version/pre-tag boundary; baseline result: PARTIAL (4/5 assertions).

## Failures

- No with-skill assertion failures.
- `npm ci` reported 3 audit advisories; installation and all required docs checks still exited `0`, so they do not fail this eval.

## Next Steps

- Keep this PASS. Preserve executed-evidence-only ops facts, plan exclusion, unverified pages, and confirmed-version audit gating as one regression set.

## Runtime Artifact Policy

- Both lanes, dependencies, edited fixture copies, test output, and isolation tooling remain under `tmp/eval-runs/issue-150/group-a/` and are not submitted.
- Only this comparison is durable; no runtime document, transcript, candidate, verdict, timing, diagnostics, `node_modules`, or build output is committed.
