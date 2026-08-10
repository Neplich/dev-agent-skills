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
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f9c706626daa220552f758703ae64d133ee8d82358801e24309850f00386ef65`
- Skill overlay SHA-256: `f60ca20c88dbcd89128c2e7274062ceecd615c5940f10126a82abf339cb3d52f`
- Judge schema SHA-256: `d09f4cbeb933e811c934cf8e665fe7675560abe0fc34d7865e0c67a56b1f4b12`
- Eval definition SHA-256: `86d9cf5b5d192be02693890eee51825a1b00e0750fd5f2d88fdcc91b3fe08ad7`
- Metadata SHA-256: `10861a3430f4e9df517502c7dede98b52c06228662db21b0d8914dd6b558a77c`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_primary_to_authz` | PASS | With-skill output explicitly selects `authz-reviewer` first for authentication, roles, sensitive routes, and admin cross-tenant risk. |
| `names_dependency_followup` | PASS | With-skill output explicitly schedules `dependency-risk-auditor` after the authorization review. |
| `collects_security_context` | PASS | It names login sessions, the role matrix, sensitive routes, tenant isolation, existing tests, dependency manifests/lockfiles, and dependency trees as review inputs or evidence. |
| `structured_risk_output` | PASS | It specifies structured security reports, permission matrices, evidence, risk levels, and remediation recommendations, and says the output is not an implementation patch. |
| `hands_off_remediation` | PASS | It hands code fixes to `engineer-agent` and dependency/build/deployment fixes to `devops-agent`. |
| `evaluates_escalation_to_pm_at_closeout` | NOT_EXERCISED | The workflow stops before specialist execution and asks for confirmation. It records escalation as not applicable yet and describes PM handoff/no direct Docs handoff or self-filed issue, but no confirmed closeout conclusion exists to exercise the full closeout assertion. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5a4bc456b36f0fe19e8d15843877f0c9ef8daed9d99b67bdcc85d65720c79c5b; fixture_sha256=6becbc324dd17ee4f5ba7cdf2d867ad58ae183800d34e6d3eb510323380d49a0; output_sha256=68d4737dd6e8ff17c963804c8e73bc17c630ed4516db101f4118364575d246a3; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Routes the request through PM security context to `authz-reviewer`, then `dependency-risk-auditor`, with structured evidence and remediation handoffs; pauses for confirmation before execution.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5a4bc456b36f0fe19e8d15843877f0c9ef8daed9d99b67bdcc85d65720c79c5b; fixture_sha256=6becbc324dd17ee4f5ba7cdf2d867ad58ae183800d34e6d3eb510323380d49a0; output_sha256=4b622c800ab60e894fce5f540d2ef81778d1c774c5df635d38418d3df715a1f8; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a useful generic security review sequence and evidence checklist, but does not establish the specialist route/handoff workflow shown by the with-skill lane.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: After user confirmation, execute the `authz-reviewer` step; assess closeout escalation only after a confirmed review conclusion exists.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
