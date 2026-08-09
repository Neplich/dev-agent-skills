# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `appsec-checklist`
- Eval: `eval-002-auth-bypass`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `cc5543f86ff4c8f3552e0e869f4690b7cabc4d7aa6f846231a547e3a3fb6e25c` from `agents/security/test/appsec-checklist/evals/workspace/eval-002-auth-bypass`.
- Fixture SHA-256: `cc5543f86ff4c8f3552e0e869f4690b7cabc4d7aa6f846231a547e3a3fb6e25c`
- Prompt SHA-256: `f088fb8b19565a837c87f47deb48148bf8a1f74fd9bf243974d4975068d68895`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `812b371fc30792cb2b0cf8d96079b3244c95b93efab7638e085d4e955d6ea42c`
- Skill overlay SHA-256: `33e7e73c99fb4e7a6f2d6ab5104b8298fc067235a29614a6e32ee61035051666`
- Judge schema SHA-256: `dd30fe689fbcc65952d80f9f7fb0f55e7cc2d55b9002a172d25f15b8b97c4288`
- Eval definition SHA-256: `6a82fe3c3414aca61cd232161a32adb38bf8c698919832011992c1d84f8965f5`
- Metadata SHA-256: `3fcfb91e83a24f1f8a67c2d9edff9012dc72e220f47b3bfd6102b0d7601836a9`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `security_findings` | PASS | The locked with_skill report identifies missing authentication and admin-role authorization on /admin/users, with anonymous and member access to user data. |
| `evidence_and_impact` | PASS | The report cites src/app.js:18, src/api/admin-routes.js:4-6, and src/api/admin-users.js:6-8, and explains exposure of account data and release impact. |
| `severity_rationale` | PASS | The report assigns Critical severity and provides rationale based on direct authentication/authorization bypass affecting an administrative endpoint. |
| `remediation` | PASS | The report gives executable middleware changes, route-prefix guidance, 401/403 behavior, handler non-execution checks, and regression tests. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f088fb8b19565a837c87f47deb48148bf8a1f74fd9bf243974d4975068d68895; fixture_sha256=cc5543f86ff4c8f3552e0e869f4690b7cabc4d7aa6f846231a547e3a3fb6e25c; output_sha256=9aa4c1058b16ce7d8e587f4beb1f70e9b8c7660d2429808662a74f4c3bb651f9; snapshot_sha256=c79db78bd22ddb4cb8a68fa848da125510fdf54ed5053d95507119991fbcd875
- Behavior: Produced a complete security checklist with findings, evidence, impact, severity rationale, and actionable remediation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f088fb8b19565a837c87f47deb48148bf8a1f74fd9bf243974d4975068d68895; fixture_sha256=cc5543f86ff4c8f3552e0e869f4690b7cabc4d7aa6f846231a547e3a3fb6e25c; output_sha256=9f3fe493ec5f77f305d95492326a8b170e88603f93e2ec5330183dd0af339770; snapshot_sha256=a7ad8f51c8f7fd2f9ca63cfd3da8bc82e4be89556eeb65d430a594b5e4058a38
- Behavior: Also produced a complete checklist; serves only as comparison context and does not affect with_skill assertion verdicts.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
