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
- Source lock SHA-256: `c58f04d32c2ca3a22aec96f7ee027af648da5971453d2a5553d7ab2cd9272551`
- Prompt SHA-256: `5a4bc456b36f0fe19e8d15843877f0c9ef8daed9d99b67bdcc85d65720c79c5b`
- Repository HEAD: `60a4b3602dc07f3f6683a8873529bbdba6f8d27d`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `5a1cae404d0abcef05fcdec59cac49a5b24d80a8810e8c341d88e853203b4442`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_primary_to_authz` | PASS | With-skill output selects `authz-reviewer` first because the concern is admin cross-tenant/platform privilege escalation. |
| `names_dependency_followup` | PASS | With-skill output explicitly sequences `dependency-risk-auditor` after the authorization review. |
| `collects_security_context` | PASS | The proposed reports cover authentication flow, role matrix/boundaries, sensitive routes, test evidence, and dependency/version/CVE evidence; the candidate also identifies the dependency inventory as `express: latest`. |
| `structured_risk_output` | PASS | The output names structured review and risk-report artifacts containing risk matrix, evidence, impact, and remediation recommendations, with no implementation patch delivered. |
| `hands_off_remediation` | PASS | The output assigns authorization findings to `engineer-agent` and dependency/build findings to `devops-agent`. |
| `evaluates_escalation_to_pm_at_closeout` | NOT_EXERCISED | Routing has not produced a verified Security conclusion; the candidate correctly records `pm_escalation: not_applicable_yet` and awaits confirmation to start the next stage, so closeout escalation evaluation is not exercised. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5a4bc456b36f0fe19e8d15843877f0c9ef8daed9d99b67bdcc85d65720c79c5b; fixture_sha256=6becbc324dd17ee4f5ba7cdf2d867ad58ae183800d34e6d3eb510323380d49a0; output_sha256=02ceaa963461b6346fe4f4ae8ca2b38f37257acecdb15191c6db428dda4d9993; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly routes authorization first, dependency review second, preserves the required security context, defines structured artifacts, and assigns remediation owners.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5a4bc456b36f0fe19e8d15843877f0c9ef8daed9d99b67bdcc85d65720c79c5b; fixture_sha256=6becbc324dd17ee4f5ba7cdf2d867ad58ae183800d34e6d3eb510323380d49a0; output_sha256=185503f6a2c99438a1f3fe128882387b8b4182cfe48f33db8d8a470fa57c3829; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a detailed security plan and evidence checklist but does not demonstrate the required specialist routing or explicit PM closeout/escalation boundary.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Obtain confirmation and run the `authz-reviewer` stage; evaluate PM escalation at Security closeout once a confirmed conclusion exists.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
