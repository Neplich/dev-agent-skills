# Eval Result: eval-001-route-ci-readiness

## Evaluation Target

- Agent: `devops`
- Skill: `devops-agent`
- Eval: `eval-001-route-ci-readiness`
- Test case: route-ci-readiness
- Workspace: `workspace/eval-1-route-ci-readiness`
- Review context: issue #196 L2-4 router single-source convergence

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: existing `deploy/docker` path with a missing GitHub Actions PR gate and later config/runbook concerns.
- Validation date: 2026-07-31.
- With-skill source: fresh candidate generated after reading `agents/devops/README.md`, `agents/devops/skills/devops-agent/SKILL.md`, `evals.json`, `eval_metadata.json`, and `deploy/docker/README.md`.
- Without-skill source: fresh candidate regenerated from the same prompt and fixture only, without reading or applying the DevOps Agent README, target skill, with-skill candidate, historical comparison, or prior baseline.

## Latest Result

- Behavior result: **FAIL**
- Coverage result: **FULL** (5/5 assertions exercised)
- Overall result: FAIL

The failure is an actual contract/fixture conflict, not a missing live sample: the prompt does not provide the PM handoff required by the current router, while `routes_primary_to_cicd` requires immediate specialist routing.

## Assertions

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_primary_to_cicd` | FAIL | The with-skill result returns the current request to `pm-agent` because no PM handoff packet or equivalent confirmed operational context is present. It names `cicd-bootstrap` only as the route after that gate, not as the current primary route required by the assertion. |
| `keeps_deployment_context` | PASS | It preserves the existing `deploy/docker` evidence and explicitly avoids restarting deployment work from zero. |
| `names_followups` | PASS | It names `env-config-auditor` and `incident-playbook-writer` as later checks. |
| `does_not_run_all_skills` | PASS | It separates the gate/current decision from the proposed primary route and follow-up checks, without executing the full chain. |
| `does_not_write_workflow` | PASS | It explicitly does not add `.github/workflows` files. |

## With-Skill Behavior

The router applies its downstream PM handoff entry gate before specialist routing. It therefore returns the request to `pm-agent`, preserves the existing Docker deployment context, and explains that the confirmed DevOps route would then start with `cicd-bootstrap`, followed by configuration audit and an on-demand incident playbook. It does not write workflow files or expand into all DevOps specialists.

The L2-4 single-table route source is sufficient for the CI/CD, configuration-audit, and rollback signal recognition. This eval does not require or assume a separate Routing Signals list.

## Fresh Without-Skill Baseline

The fresh baseline directly selects `cicd-bootstrap` from the concrete GitHub Actions gap, carries the existing `deploy/docker` context forward, names `env-config-auditor` and `incident-playbook-writer` as follow-ups, and declines to write workflow files. It satisfies all five eval assertions.

For this fixture, the baseline is more aligned with the asserted immediate route because it does not apply the target skill's PM handoff gate. This difference must not be interpreted as stronger governance behavior; it exposes that the current assertion and prompt do not jointly cover the router's entry contract.

## Failures

- With-skill failure: `routes_primary_to_cicd`.
- Root cause: missing PM handoff/equivalent confirmed context in the fixture conflicts with the current downstream entry gate.
- No assertion was marked `NOT EXERCISED`; all five behaviors were observable.
- No runtime, credential, or external-service blocker occurred.

## Next Steps

- Align this eval through the owning contract decision: either add a valid PM handoff/equivalent confirmed operational context to the fixture or change the expected route to the PM entry gate. Do not silently bypass the gate in the candidate.
- Retain the existing checks for current-route/follow-up separation, Docker context preservation, and route-only authorization.

## Runtime Artifact Policy

- Fresh paired evidence is stored only under `tmp/eval-runs/issue-196-l2-3-4/devops-agent/eval-001-route-ci-readiness/`:
  - `with_skill.md`
  - `without_skill.md`
  - `judge.md`
- These scratch files are not committed.
- Runtime transcripts, candidates, verdicts, timing, status, diagnostics, and generated output directories must not be copied into the fixture workspace.
