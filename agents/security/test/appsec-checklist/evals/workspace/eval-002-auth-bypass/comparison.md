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
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `812b371fc30792cb2b0cf8d96079b3244c95b93efab7638e085d4e955d6ea42c`
- Skill overlay SHA-256: `11d9f677e9ab3fadaeeab596575848debc7e1fb3f4f8054e9e5572a63ccf426b`
- Judge schema SHA-256: `dd30fe689fbcc65952d80f9f7fb0f55e7cc2d55b9002a172d25f15b8b97c4288`
- Eval definition SHA-256: `6a82fe3c3414aca61cd232161a32adb38bf8c698919832011992c1d84f8965f5`
- Metadata SHA-256: `3fcfb91e83a24f1f8a67c2d9edff9012dc72e220f47b3bfd6102b0d7601836a9`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `security_findings` | PASS | PASS：报告识别 `/admin/users` 缺少认证与管理员角色授权，导致匿名及普通用户可访问管理 API。 |
| `evidence_and_impact` | PASS | PASS：报告提供了 `src/app.js:18`、`src/api/admin-routes.js:6`、`src/api/admin-users.js:6-7` 等代码证据，并说明了受影响入口、用户资料暴露及后续管理风险。 |
| `severity_rationale` | PASS | PASS：报告将问题评为 High，并依据无需凭证、涉及账号资料且当前为读取接口而非写入接口进行分级。 |
| `remediation` | PASS | PASS：报告提供了集中挂载认证/授权中间件、避免重复 `/admin` 前缀、返回 401/403，以及覆盖匿名/member/admin 身份的回归验证步骤。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f088fb8b19565a837c87f47deb48148bf8a1f74fd9bf243974d4975068d68895; fixture_sha256=cc5543f86ff4c8f3552e0e869f4690b7cabc4d7aa6f846231a547e3a3fb6e25c; output_sha256=44b9f5d5c55c9988ed1a0a714f379063880a8fc296f62e65e9b13f8b2bca50a4; snapshot_sha256=960ccd2ddba752132e56943af47f899252c8bf9e843a35b5c0a6c91959097808
- Behavior: 产出安全审查报告，准确识别未保护的管理路由，提供证据、影响、严重度和修复验证建议，未修改应用代码。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f088fb8b19565a837c87f47deb48148bf8a1f74fd9bf243974d4975068d68895; fixture_sha256=cc5543f86ff4c8f3552e0e869f4690b7cabc4d7aa6f846231a547e3a3fb6e25c; output_sha256=98be20bc82428e1fc9f1c28aa813e4eaf219da9423212d3f5887dad12bce9064; snapshot_sha256=85716abe7274d6b514e5d1352435c46af4047a93e30d3b851ddaa92c395ce65a
- Behavior: 同样产出内容完整的安全审查报告；作为比较基线，不影响 with_skill assertion verdict。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
