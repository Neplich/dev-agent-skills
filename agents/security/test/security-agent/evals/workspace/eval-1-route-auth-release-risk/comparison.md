# Eval Result: eval-001-route-auth-release-risk

## Evaluation Target

- Agent: `security`
- Skill: `security-agent`
- Eval: `eval-001-route-auth-release-risk`
- Test case: route-auth-release-risk
- Workspace: `workspace/eval-1-route-auth-release-risk`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-06

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: auth-centered release security request with dependency-risk concern.
- Context read before applying the skill: `security-agent/SKILL.md`, Security Agent `README.md`, `evals.json`, workspace `eval_metadata.json`, `docs/security/auth-model.md`, `package.json`, and the `Safety-Net Closeout and Auto-Continue` section in `skill-map.md`.

## Assertions

- PASS `routes_primary_to_authz`: login, roles, admin access, and authorization bypass risk route to `authz-reviewer`.
- PASS `names_dependency_followup`: dependency vulnerability concerns are preserved as a `dependency-risk-auditor` follow-up.
- PASS `collects_security_context`: downstream context includes auth flows, roles/permissions, sensitive routes, test evidence, and dependency manifest.
- PASS `structured_risk_output`: expected output is a structured review, risk matrix, evidence, and remediation guidance.
- PASS `hands_off_remediation`: fixes are handed to `engineer-agent` or `devops-agent`, not implemented by Security.

## With Skill Behavior

`security-agent` satisfies the release-risk route. Its router chooses the narrowest security outcome, so the auth/admin risk gets `authz-reviewer` as the current route while dependency audit remains a named `dependency-risk-auditor` follow-up. The selected downstream context is authentication flow, role and permission matrix, sensitive routes, test evidence, and the dependency manifest.

The skill preserves Security as an evidence-backed risk review role and explicitly hands remediation to `engineer-agent` or `devops-agent` when findings require code, dependency, or deployment changes. The #81 safety-net closeout is compatible with this route: the prompt asks for routing only and does not authorize auto-continue, so Security stops at the route and handoff proposal. If auto-continue were enabled later, it would automate only the next-owner handoff and would not let Security execute another role's workflow or bypass that role's gate.

## Without Skill Baseline

Fresh without_skill baseline generated on 2026-07-06 without reading or applying `security-agent/SKILL.md` or the Security Agent README: a generic response could blend auth review, dependency audit, and fix recommendations into one broad release checklist. It may choose a broad security review as the primary route instead of the narrower auth route, bury the dependency concern in the same checklist, and suggest direct code or package changes instead of keeping Security output as structured risk evidence with remediation handoff.

## Failures

- None found. No #81 regression was observed: the original narrow routing and remediation handoff remain intact, and auto-continue does not expand the Security role boundary.

## Next Steps

- Keep this eval as regression coverage for Security narrow-route selection, remediation handoff, and #81 auto-continue boundary behavior.

## Runtime Artifacts Policy

- No runtime artifacts were created for this validation.
- Runtime transcripts, verdicts, timing, output directories, diagnostics, and generated with_skill / without_skill files must not be committed.
