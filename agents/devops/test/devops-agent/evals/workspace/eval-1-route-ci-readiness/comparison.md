# Eval Result: eval-001-route-ci-readiness

## Evaluation Target

- Agent: `devops`
- Skill: `devops-agent`
- Eval: `eval-001-route-ci-readiness`
- Test case: route-ci-readiness
- Workspace: `workspace/eval-1-route-ci-readiness`
- Review context: PR #204 / issue #196 eval alignment fix round

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture base: repository commit `f808d82`, plus the approved minimal `PM_HANDOFF.md` alignment in this fix round.
- Fixture: confirmed repo-wide PM handoff, existing `deploy/docker/README.md`, missing GitHub Actions PR gate, and later config/runbook concerns.
- Validation date: `2026-08-01 09:57:18 +0800`.
- With-skill source: fresh candidate generated after fully reading `agents/devops/README.md`, `agents/devops/skills/devops-agent/SKILL.md`, the current `evals.json`, `eval_metadata.json`, `PM_HANDOFF.md`, and all fixture files.
- Without-skill source: fresh candidate generated from the same prompt and an independent fixture copy only; it did not read or apply the DevOps Agent README or target skill and did not reuse the with-skill candidate, old comparison, or historical baseline.

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL** (5/5 assertions exercised)
- No assertion was `NOT EXERCISED`.

Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_primary_to_cicd` | PASS | The with-skill candidate accepts the confirmed PM handoff and selects `cicd-bootstrap` as the current primary route because Docker deployment exists and the missing artifact is a GitHub Actions PR gate. |
| `keeps_deployment_context` | PASS | It carries `deploy/docker/README.md` and the existing Docker path into the specialist context and explicitly rejects rebuilding deployment assets from zero. |
| `names_followups` | PASS | It assigns environment/config coverage to later `env-config-auditor` work and rollback documentation to later `incident-playbook-writer` work. |
| `does_not_run_all_skills` | PASS | It separates one current primary route from sequential follow-up checks and does not execute all DevOps specialists together. |
| `does_not_write_workflow` | PASS | It preserves the route-only authorization and explicitly does not add `.github/workflows/` files. |

## With-Skill Behavior

The fresh candidate uses the aligned PM handoff to pass the router entry gate, preserves the confirmed `N/A` repo-wide feature scope, and routes the current CI readiness gap to `cicd-bootstrap`. It keeps the existing `deploy/docker` evidence, names configuration audit and rollback documentation as later checks, and does not execute specialist work or write a workflow.

## Fresh Without-Skill Baseline

The fresh baseline also recognizes CI/CD automation as the immediate owner, preserves the existing Docker deployment, and keeps configuration and rollback concerns as later checks. Because it does not use the repository skill, it describes generic owners rather than the repo-native `cicd-bootstrap`, `env-config-auditor`, and `incident-playbook-writer` routes. The contrast shows the skill adds precise internal routing while preserving the user's authorization boundary.

## Failures

- None.
- The previous fixture/gate conflict is resolved by the approved minimal PM handoff packet.
- No runtime, credential, or external-service blocker occurred.

## Next Steps

- No eval-specific correction is required.
- Retain the PM handoff fixture and the current-route/follow-up separation in future router changes.

## Runtime Artifact Policy

- Fresh paired evidence is stored only under `tmp/eval-runs/pr-204-fix-round-20260801/devops-agent/eval-001-route-ci-readiness/`.
- The runtime directory contains independent `with_fixture/` and `without_fixture/` copies plus `with_skill.md`, `without_skill.md`, and `judge.md`.
- Runtime candidates, fixture copies, verdicts, transcripts, timing, status, diagnostics, and generated outputs are scratch artifacts and are not committed.
- The durable committed result is this `comparison.md` only.
