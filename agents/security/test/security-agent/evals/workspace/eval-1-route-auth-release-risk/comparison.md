# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `security-agent`
- Eval: `eval-001-route-auth-release-risk`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `6becbc324dd17ee4f5ba7cdf2d867ad58ae183800d34e6d3eb510323380d49a0` from `agents/security/test/security-agent/evals/workspace/eval-1-route-auth-release-risk`.
- Identity schema: `2`
- target_skill_sha256: `3fda47276f652c3a8bf71ee145e10142e5e8e52ecaf4fa1602d50b284a2d428a`
- eval_definition_sha256: `d5973b25612b7e076dab35db16f38a088f965995470b2ae2a1e956ac49b1959d`
- metadata_sha256: `10861a3430f4e9df517502c7dede98b52c06228662db21b0d8914dd6b558a77c`
- fixture_sha256: `6becbc324dd17ee4f5ba7cdf2d867ad58ae183800d34e6d3eb510323380d49a0`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `d09f4cbeb933e811c934cf8e665fe7675560abe0fc34d7865e0c67a56b1f4b12`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `5a4bc456b36f0fe19e8d15843877f0c9ef8daed9d99b67bdcc85d65720c79c5b`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `5a1cae404d0abcef05fcdec59cac49a5b24d80a8810e8c341d88e853203b4442`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_primary_to_authz` | FAIL | The with_skill output places `appsec-checklist` first and `authz-reviewer` second, so it does not select `authz-reviewer` as the current primary route. |
| `names_dependency_followup` | PASS | It explicitly routes dependency vulnerability and supply-chain review to `dependency-risk-auditor` as a later stage. |
| `collects_security_context` | PASS | It identifies authentication/session flow, the guest/member/admin/platform-ops role matrix, sensitive routes, related test evidence, and dependency-version evidence as required review inputs or outputs. |
| `structured_risk_output` | PASS | It explicitly requires a structured security review/risk report containing a risk matrix, evidence, impact, and remediation suggestions, rather than an implementation patch. |
| `hands_off_remediation` | PASS | It hands application authorization fixes to `engineer-agent` and dependency/build/deployment fixes to `devops-agent`. |
| `evaluates_escalation_to_pm_at_closeout` | NOT_EXERCISED | The workflow stops before closeout pending confirmation and an unavailable `appsec-checklist`; the output states escalation is not applicable yet but does not exercise the full closeout evaluation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5a4bc456b36f0fe19e8d15843877f0c9ef8daed9d99b67bdcc85d65720c79c5b; fixture_sha256=6becbc324dd17ee4f5ba7cdf2d867ad58ae183800d34e6d3eb510323380d49a0; output_sha256=932f21d1367e02b72f15b7c2f59bea778fa83370ad431aa9fc58c2ce3f98f539; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides named security routes, required review context, structured deliverables, remediation ownership, and a conditional PM escalation note, but orders `appsec-checklist` before the required primary authorization review and stops before closeout.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5a4bc456b36f0fe19e8d15843877f0c9ef8daed9d99b67bdcc85d65720c79c5b; fixture_sha256=6becbc324dd17ee4f5ba7cdf2d867ad58ae183800d34e6d3eb510323380d49a0; output_sha256=35e82060dfb8b7c6517d4711070875cc65899f59a24274ab31f9ec8f65868af3; snapshot_sha256=65aac036b6562a5c68f9ebc5b01774410c41b40b46b7e088773c558412b775f8
- Behavior: Provides a generic security review plan and blockers but does not name the required specialist routes or the PM escalation/role handoff behavior.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The primary route is `appsec-checklist`, not the required `authz-reviewer`.
- Next: Make `authz-reviewer` the primary route, with dependency review as the follow-up.
- Next: Resolve or explicitly hand off the unavailable `appsec-checklist`, then obtain confirmation before continuing to closeout evaluation.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
