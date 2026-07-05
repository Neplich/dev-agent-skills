# Eval Result: eval-001-route-auth-release-risk

## Evaluation Target

- Agent: `security`
- Skill: `security-agent`
- Eval: `eval-001-route-auth-release-risk`
- Test case: route-auth-release-risk
- Workspace: `workspace/eval-1-route-auth-release-risk`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-05

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: auth-centered release security request with dependency-risk concern.
- Context read before applying the skill: `evals.json`, workspace `eval_metadata.json`, `docs/security/auth-model.md`, and `package.json`.

## Assertions

- PASS `routes_primary_to_authz`: login, roles, admin access, and authorization bypass risk route to `authz-reviewer`.
- PASS `names_dependency_followup`: dependency vulnerability concerns are preserved as a `dependency-risk-auditor` follow-up.
- PASS `collects_security_context`: downstream context includes auth flows, roles/permissions, sensitive routes, test evidence, and dependency manifest.
- PASS `structured_risk_output`: expected output is a structured review, risk matrix, evidence, and remediation guidance.
- PASS `hands_off_remediation`: fixes are handed to `engineer-agent` or `devops-agent`, not implemented by Security.

## With Skill Behavior

`security-agent` satisfies the release-risk route. Its router chooses the narrowest security outcome, so the auth/admin risk gets `authz-reviewer` as the current route while dependency audit remains a named follow-up. The skill preserves Security as an evidence-backed risk review role and explicitly hands remediation to Engineer or DevOps when findings require changes.

## Without Skill Baseline

Without the router skill and Security README, a generic response could blend auth review, dependency audit, and fix recommendations into one broad release checklist. It may also suggest code changes directly instead of keeping Security output as structured risk evidence with remediation handoff.

## Failures

- None found.

## Next Steps

- Keep this eval as regression coverage for Security narrow-route selection and remediation handoff.

## Runtime Artifacts Policy

- No runtime artifacts were created for this validation.
- Runtime transcripts, verdicts, timing, output directories, diagnostics, and generated with_skill / without_skill files must not be committed.
