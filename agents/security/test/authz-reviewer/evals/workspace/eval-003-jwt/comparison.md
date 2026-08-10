# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `authz-reviewer`
- Eval: `eval-003-jwt`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `b22eea37eaa1e0fa82c96957a5790898e68b0e138db6319e88a5574aee2cf1f4` from `agents/security/test/authz-reviewer/evals/workspace/eval-003-jwt`.
- Fixture SHA-256: `b22eea37eaa1e0fa82c96957a5790898e68b0e138db6319e88a5574aee2cf1f4`
- Prompt SHA-256: `da9ecfe298cdea573f5e2d687f97fd893a94d3dc4b95b345575f1d452f32a2ab`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `c5c4e1b3eeeb704a06966dee8397bc4f1df239be6ed5f5799f8d4bd382f23626`
- Skill overlay SHA-256: `5d963f35c675c3748a7ab8200aa22a681cf01b4c9046afa796b21dbaa5d298b4`
- Judge schema SHA-256: `a3c690bb602cdac9c05191ab0581fc35b8fd034dd27825093b3b51de5926404b`
- Eval definition SHA-256: `8f6e801f8a45c6ec677bbcaa4a56de6b68c935402a27b9f24ca631ffe0af8504`
- Metadata SHA-256: `2db8c4dc18a4712e7dcc4d2c4e3e9c1608e8526019fbff1c3fc3e6ded6f9d1c5`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `authorization_model` | PASS | The locked report identifies user/admin roles, protected APIs, the `/api/admin/*` boundary, and the full path from Authorization header through `authenticateJwt` to `canAccessAdminApi`. |
| `access_control_findings` | PASS | The locked report identifies missing signature verification, algorithm allow-listing, `exp` validation, unverified role trust, and malformed-header handling, with severity and concrete impact. |
| `evidence_and_impact` | PASS | Each finding includes source locations in `src/auth/jwt.js`, links the defects to PRD requirements, and explains forgery, expiry, and admin-escalation consequences. |
| `remediation` | PASS | The report provides actionable cryptographic, algorithm, expiry, claim-trust, parsing, integration, and regression-test recommendations, including a release gate. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=da9ecfe298cdea573f5e2d687f97fd893a94d3dc4b95b345575f1d452f32a2ab; fixture_sha256=b22eea37eaa1e0fa82c96957a5790898e68b0e138db6319e88a5574aee2cf1f4; output_sha256=b56e285d1e4e7a1dc47a2f809c4a96c8af95edeca4f0983032061b933e4af09b; snapshot_sha256=6f5e7f5a27f8e41aa55071232880034016f041d9f491bf95a4f933654114256a
- Behavior: Produced a structured, evidence-backed JWT authorization review artifact with role matrix, authorization flow, severity-ranked findings, impact, remediation, regression guidance, and explicit limits on route coverage.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=da9ecfe298cdea573f5e2d687f97fd893a94d3dc4b95b345575f1d452f32a2ab; fixture_sha256=b22eea37eaa1e0fa82c96957a5790898e68b0e138db6319e88a5574aee2cf1f4; output_sha256=c01dc24b60562b537290851199e10f4e33af2749512ac41705948b039a208b41; snapshot_sha256=6ea88cc9d1575e9b661bf41b9f43d40f0c38c599591775ee2889dfce0f533aac
- Behavior: Provided a concise baseline review covering the main JWT, expiry, role-escalation, and malformed-header risks plus high-level validation suggestions, with less structured evidence and coverage detail.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
