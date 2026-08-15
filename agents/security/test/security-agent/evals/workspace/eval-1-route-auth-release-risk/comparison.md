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
- target_skill_sha256: `02e38e560c7190aeb913b7c5d8c7a2d7815e82ab5a7f447a1c96c00f49f9f173`
- eval_definition_sha256: `d5973b25612b7e076dab35db16f38a088f965995470b2ae2a1e956ac49b1959d`
- metadata_sha256: `10861a3430f4e9df517502c7dede98b52c06228662db21b0d8914dd6b558a77c`
- fixture_sha256: `6becbc324dd17ee4f5ba7cdf2d867ad58ae183800d34e6d3eb510323380d49a0`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `d09f4cbeb933e811c934cf8e665fe7675560abe0fc34d7865e0c67a56b1f4b12`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `5a4bc456b36f0fe19e8d15843877f0c9ef8daed9d99b67bdcc85d65720c79c5b`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `fd5b004e70c26dca0a4abf3ce0d7b2fe1350c24120a987bbc6ab7abf7df07079`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_primary_to_authz` | PASS | With-skill output explicitly selects `authz-reviewer` as the priority route for admin cross-tenant/platform authorization risks. |
| `names_dependency_followup` | PASS | It explicitly assigns dependency supply-chain review to `dependency-risk-auditor` after the authorization review. |
| `collects_security_context` | PASS | It lists authentication/session lifecycle, the four-role permission matrix, all three sensitive routes, negative-test evidence, and dependency/lockfile/CVE evidence as required review inputs. |
| `structured_risk_output` | PASS | It specifies a structured security review under `docs/security/auth-model/` containing a risk matrix, evidence, impact, remediation recommendations, and evidence gaps, and says it is not an implementation patch. |
| `hands_off_remediation` | PASS | It assigns application/authentication fixes to `engineer-agent` and dependency/build/deployment fixes to `devops-agent`. |
| `evaluates_escalation_to_pm_at_closeout` | NOT_EXERCISED | The candidate correctly marks PM escalation as not applicable yet and requires a later security conclusion before returning findings to `pm-agent`, but the interactive workflow stops pending confirmation to start `authz-reviewer`; closeout evaluation is therefore not exercised. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5a4bc456b36f0fe19e8d15843877f0c9ef8daed9d99b67bdcc85d65720c79c5b; fixture_sha256=6becbc324dd17ee4f5ba7cdf2d867ad58ae183800d34e6d3eb510323380d49a0; output_sha256=dccd8fe75eff7024a45b5de8da013da1815cbc9351f5ccc9273126624a47a777; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly routes authorization first, names dependency follow-up, identifies required security evidence, defines structured outputs, and assigns remediation ownership. It pauses for user confirmation before downstream execution.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5a4bc456b36f0fe19e8d15843877f0c9ef8daed9d99b67bdcc85d65720c79c5b; fixture_sha256=6becbc324dd17ee4f5ba7cdf2d867ad58ae183800d34e6d3eb510323380d49a0; output_sha256=92ed16a254dfa602e3029c64dc34f9cfba14daafa650e12b5d3ba7e8b6c01f5c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a detailed review sequence and evidence requirements but does not establish the required named routes, remediation handoff, or closeout escalation policy.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Confirm starting `authz-reviewer`, then run the dependency audit and perform closeout escalation evaluation after security conclusions are available.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
