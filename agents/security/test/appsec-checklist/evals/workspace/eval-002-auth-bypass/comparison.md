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
- Identity schema: `2`
- target_skill_sha256: `9ac7059a9a39550256d4de1ed82086d7f6b3c81bd069d831f0bf87ce02417c58`
- eval_definition_sha256: `6a82fe3c3414aca61cd232161a32adb38bf8c698919832011992c1d84f8965f5`
- metadata_sha256: `cd24e6f3242be56aca57c51c88f32017b1caf4b9307635625892f26c0b426e5d`
- fixture_sha256: `cc5543f86ff4c8f3552e0e869f4690b7cabc4d7aa6f846231a547e3a3fb6e25c`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `dd30fe689fbcc65952d80f9f7fb0f55e7cc2d55b9002a172d25f15b8b97c4288`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `f088fb8b19565a837c87f47deb48148bf8a1f74fd9bf243974d4975068d68895`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `d316d6849a82751d5c66c424af9993a42c304fe892fdb2411469b461bec624ee`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `security_findings` | PASS | 报告识别了认证绕过和管理员授权缺失，明确指出匿名及普通用户可进入 /admin/users 的 listUsers。 |
| `evidence_and_impact` | PASS | 报告引用 src/app.js:18、src/api/admin-routes.js:6、src/api/admin-users.js:6-7，并说明用户账号资料暴露及后续管理操作风险。 |
| `severity_rationale` | PASS | 报告将问题分为 Critical，并以管理 API 暴露、低攻击前置条件、机密性影响和上线阻断依据进行说明。 |
| `remediation` | PASS | 报告提供认证→admin 角色校验的挂载方案，并给出 401/403/管理员成功访问、处理器不执行及路由覆盖等验证步骤。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f088fb8b19565a837c87f47deb48148bf8a1f74fd9bf243974d4975068d68895; fixture_sha256=cc5543f86ff4c8f3552e0e869f4690b7cabc4d7aa6f846231a547e3a3fb6e25c; output_sha256=a38106f3bf9c2d2f63f3b9422ac687d8722156886701cabc0390ea03ef99a53f; snapshot_sha256=5db86896dc6ff516af78d39ebfe3189068d5cece00853f799f34008bde3d8334
- Behavior: 完成了符合要求的安全报告，识别认证绕过与垂直越权，提供定位证据、影响、严重度依据和可执行修复验证建议。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f088fb8b19565a837c87f47deb48148bf8a1f74fd9bf243974d4975068d68895; fixture_sha256=cc5543f86ff4c8f3552e0e869f4690b7cabc4d7aa6f846231a547e3a3fb6e25c; output_sha256=98161e7e8748d14952ca7507967bd8fe5f3b61fd7601f8fca734e0fcf93ed213; snapshot_sha256=7c5bafe89c50dce98f03162349d85377af7605c885f856ef50bb2c801d6d20c8
- Behavior: Fresh baseline 也识别了核心认证与授权缺陷并交付报告，但分级为高危、报告结构和细节相对简略。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
