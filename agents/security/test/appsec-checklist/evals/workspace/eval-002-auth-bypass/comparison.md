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
- target_skill_sha256: `412a68c0dfdb2d720e3447fdc4faf74b408d3de29706093a3a69fb0ca69d983c`
- eval_definition_sha256: `6a82fe3c3414aca61cd232161a32adb38bf8c698919832011992c1d84f8965f5`
- metadata_sha256: `cd24e6f3242be56aca57c51c88f32017b1caf4b9307635625892f26c0b426e5d`
- fixture_sha256: `cc5543f86ff4c8f3552e0e869f4690b7cabc4d7aa6f846231a547e3a3fb6e25c`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `dd30fe689fbcc65952d80f9f7fb0f55e7cc2d55b9002a172d25f15b8b97c4288`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `f088fb8b19565a837c87f47deb48148bf8a1f74fd9bf243974d4975068d68895`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `035cdf3596c1888564523ed3d4e73116a3d2b231b30d91c462fb62cf6da52e05`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `security_findings` | PASS | The delivered report identifies the missing authentication and administrator authorization on `/admin/users`, supported by `src/app.js:18`, `src/api/admin-routes.js:6`, and `src/api/admin-users.js:6-7`. |
| `evidence_and_impact` | PASS | The report explains the route and handler evidence, identifies anonymous and non-admin access to user account data, and describes impact to current and future admin operations. |
| `severity_rationale` | PASS | The report assigns Critical severity and justifies it as an authentication bypass exposing a protected management surface and account data, while treating the missing role check as part of the same finding. |
| `remediation` | PASS | The report provides executable router-boundary middleware guidance, 401/403 behavior, centralized `/admin` protection, integration tests for anonymous/non-admin/admin users, and post-fix security review. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f088fb8b19565a837c87f47deb48148bf8a1f74fd9bf243974d4975068d68895; fixture_sha256=cc5543f86ff4c8f3552e0e869f4690b7cabc4d7aa6f846231a547e3a3fb6e25c; output_sha256=5270708cf3af3e9b98dd44ae0dc993a481ee4b0270b1250594c135e47ce1eebe; snapshot_sha256=de27d23a50225547b30629dc7f6d2dbc0a471f5d2ed6c7def5c94e6e10cf0c74
- Behavior: Produced the required security report, correctly identified the exposed admin route, gave severity reasoning, and supplied concrete remediation and verification steps.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f088fb8b19565a837c87f47deb48148bf8a1f74fd9bf243974d4975068d68895; fixture_sha256=cc5543f86ff4c8f3552e0e869f4690b7cabc4d7aa6f846231a547e3a3fb6e25c; output_sha256=a0ad15d198d840a1befacd200656ae5e98ec6370fac9e8a3d2af45c29ad40de7; snapshot_sha256=7e3fe3c8a76a7c995defd1d0f37a6a01bfdc9db3c6cd05612d4505f441f5de06
- Behavior: Also identified the core access-control issue and produced a report; it is comparison context only and does not affect with_skill assertion verdicts.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
