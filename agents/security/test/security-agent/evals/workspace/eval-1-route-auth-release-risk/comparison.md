# Eval Result: eval-001-route-auth-release-risk

## Evaluation Target

- Agent: `security`
- Skill: `security-agent`
- Eval: `eval-001-route-auth-release-risk`
- Test case: route-auth-release-risk
- Workspace: `workspace/eval-1-route-auth-release-risk`
- Review context: PR #98 trigger description routing review
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-08

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: auth-centered release security request with dependency-risk concern.
- Prompt: login and permission-model refactor is preparing for release; the user primarily worries about admin authorization bypass and also wants dependency vulnerability routing.
- Context read before applying the skill: `AGENTS.md`, Security Agent `README.md`, `security-agent/SKILL.md`, `evals.json`, workspace `eval_metadata.json`, `docs/security/auth-model.md`, `package.json`, and `agents/product_manager/skills/idea-to-spec/_internal/_shared/skill-map.md`.
- Validation date: 2026-07-08.

## Assertions

- PASS `routes_primary_to_authz`: login, roles, admin access, and authorization bypass risk route to `authz-reviewer` as the current primary route.
- PASS `names_dependency_followup`: dependency vulnerability concerns are preserved as a `dependency-risk-auditor` follow-up instead of being ignored or folded into the auth review.
- PASS `collects_security_context`: downstream context includes authentication flows, roles/permissions, sensitive routes and access checks, test evidence, and dependency manifests or audit data.
- PASS `structured_risk_output`: expected output is a structured review with risk matrix, evidence, impact, and remediation guidance, not an implementation patch.
- PASS `hands_off_remediation`: fixes are handed to `engineer-agent` or `devops-agent`, not implemented by Security.

## With Skill Behavior

`security-agent` satisfies the release-risk route. The request is release-shaped, but the dominant risk surface is login, roles, admin permissions, and authorization bypass. The router therefore selects the narrowest current route, `authz-reviewer`, while keeping dependency vulnerability review as a named `dependency-risk-auditor` follow-up.

The skill preserves confirmed security context for the downstream reviewer: authentication flow, permission matrix, sensitive routes, test evidence, and dependency manifests. It also keeps Security's role boundary intact by producing evidence-backed risk review output and handing any code, dependency, or deployment remediation to `engineer-agent` or `devops-agent`.

The safety-net closeout remains compatible with this route. The prompt asks for routing only and does not authorize auto-continue, so Security should stop at the route and follow-up proposal. If auto-continue is later enabled, it automates only the next-owner handoff and does not let Security execute another role's workflow or bypass that role's gate.

## Without Skill Baseline

Fresh without_skill baseline generated on 2026-07-08 from only the eval prompt and fixture facts. It did not read, reference, or apply `agents/security/README.md`, `agents/security/skills/security-agent/SKILL.md`, historical `comparison.md`, or any old baseline.

The no-skill baseline could plausibly treat the request as a broad release security checklist, combine auth review and dependency audit into one generic route, and choose a broad AppSec or release-security review as the current route. It would likely mention login, roles, admin access, sensitive routes, tests, and dependencies, but it is less likely to preserve the exact specialist split: `authz-reviewer` now, `dependency-risk-auditor` later. It may also drift into direct package or code-fix recommendations instead of keeping the output as structured risk evidence with remediation handoff.

## Failures

- None found. No PR #98 trigger description routing regression was observed: the Security router still selects the auth/authz specialist as the primary route, preserves dependency audit as a follow-up, and maintains remediation handoff boundaries.

## Next Steps

- Keep this eval as regression coverage for Security narrow-route selection, dependency follow-up routing, structured risk output, and remediation handoff.
- Do not auto-run the routed specialists from this eval result; execution of `authz-reviewer` or `dependency-risk-auditor` requires the normal downstream gates and user confirmation.

## Runtime Artifacts Policy

- Runtime evidence for this validation was written only under `tmp/eval-runs/2026-07-08-router-trigger-batch4-final/eval-001-route-auth-release-risk/`.
- The scratch files `with_skill.md`, `without_skill.md`, and `verdict.md` are runtime artifacts and must not be committed.
- Runtime transcripts, verdicts, timing, output directories, diagnostics, and generated with_skill / without_skill files must not be committed.
