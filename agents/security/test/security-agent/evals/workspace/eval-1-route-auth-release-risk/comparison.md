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
- Fixture SHA-256: `6becbc324dd17ee4f5ba7cdf2d867ad58ae183800d34e6d3eb510323380d49a0`
- Prompt SHA-256: `5a4bc456b36f0fe19e8d15843877f0c9ef8daed9d99b67bdcc85d65720c79c5b`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `d757bbaf4b55662bd396a15ca7c9b69a10dbe649b2aac6ce29c97794cc4f00b0`
- Skill overlay SHA-256: `c15cc4705f2e5ab1d2498bb87a228d8af5b54c5d7ed76fb2d1049031187c7404`
- Judge schema SHA-256: `d09f4cbeb933e811c934cf8e665fe7675560abe0fc34d7865e0c67a56b1f4b12`
- Eval definition SHA-256: `86d9cf5b5d192be02693890eee51825a1b00e0750fd5f2d88fdcc91b3fe08ad7`
- Metadata SHA-256: `10861a3430f4e9df517502c7dede98b52c06228662db21b0d8914dd6b558a77c`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_primary_to_authz` | PASS | The with_skill output explicitly selects `authz-reviewer` first for login sessions, role matrix, tenant isolation, sensitive routes, and admin privilege escalation. |
| `names_dependency_followup` | PASS | It explicitly places `dependency-risk-auditor` second for Express and the full dependency tree’s CVE, supply-chain, and maintenance risks. |
| `collects_security_context` | PASS | It identifies login sessions, role matrix, tenant isolation, sensitive routes, dependency manifests, and later code/test/audit outputs as the evidence context. |
| `structured_risk_output` | FAIL | It names report deliverables, but does not state that they are structured reviews containing a risk matrix, evidence, and remediation recommendations, nor explicitly distinguish them from direct patches. |
| `hands_off_remediation` | PASS | It assigns authentication fixes to the application engineering team and dependency/build/deployment fixes to the platform engineering team, which is a semantic remediation handoff. |
| `evaluates_escalation_to_pm_at_closeout` | NOT_EXERCISED | The workflow remains before confirmation and before either review produces a Security-owned conclusion; closeout escalation therefore cannot yet be exercised. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5a4bc456b36f0fe19e8d15843877f0c9ef8daed9d99b67bdcc85d65720c79c5b; fixture_sha256=6becbc324dd17ee4f5ba7cdf2d867ad58ae183800d34e6d3eb510323380d49a0; output_sha256=cf9c6f67b0b236a4339aa08cf59186ceebeefd1f5fdf285c9c1ea4dc313a8eb3; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly routes the security review and dependency follow-up, captures the main security context, and assigns remediation ownership, but omits required structured risk-output details.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5a4bc456b36f0fe19e8d15843877f0c9ef8daed9d99b67bdcc85d65720c79c5b; fixture_sha256=6becbc324dd17ee4f5ba7cdf2d867ad58ae183800d34e6d3eb510323380d49a0; output_sha256=3613d0081baa558d331deaa73efeba6cf801847ee9b8f2af4259aaa97ae88da2; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a broad security review plan and dependency concerns, but does not establish the required named primary and follow-up routes or the closeout handoff policy.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill lane omits the required explicit structured-review output contents and direct-patch distinction.
- Next: After confirmation, run `authz-reviewer`, then `dependency-risk-auditor`; assess PM escalation at closeout once a Security-owned conclusion exists.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
