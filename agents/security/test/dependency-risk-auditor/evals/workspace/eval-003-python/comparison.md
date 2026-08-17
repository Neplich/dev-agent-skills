# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `dependency-risk-auditor`
- Eval: `eval-003-python`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `8307ea1325de4c132e54824c9dd507ed174ce29fe901e9f04e5a56bc654490e3` from `agents/security/test/dependency-risk-auditor/evals/workspace/eval-003-python`.
- Identity schema: `2`
- target_skill_sha256: `cd54295a0cbcb90462d5e5533bde1937cc7e871f8f4c9c53d7773ed40ace553e`
- eval_definition_sha256: `b851960b1dd4c6ab11f9c42f685034d6bd0e27ae3c26e4256af19942329ed614`
- metadata_sha256: `ae72aa507a46a167a61a13af949f88d9dacf41d33161383d4a9754e7de06b4d8`
- fixture_sha256: `8307ea1325de4c132e54824c9dd507ed174ce29fe901e9f04e5a56bc654490e3`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `07345508cc5d326f024163cc8715111c4efeeb1bd80f16886d65b16eb2ef9292`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `109b986b4018ed5121d20e83d0f03f39a0aaef687eb5dd7c1936ee4b3a089210`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `dede36cbf22736a6194a488a09a7dab4d5a1092bacb831a4913854fdff85a07a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `dependency_inventory` | PASS | With_skill inventory identifies the Python ecosystem, all three pinned packages, their roles, HTTP/TLS/template scope, stale dependencies, and provenance/lockfile risks. |
| `risk_classification` | PASS | With_skill distinguishes CVEs from stale-version, abandonment-warning, missing-lockfile, and supply-chain/provenance risks, with High/Moderate severity and conditional exploitability. |
| `evidence` | PASS | The delivered audit directly cites requirements.txt versions, package roles, CVE/GHSA identifiers, fixed versions, advisory links, and repository evidence. |
| `upgrade_plan` | PASS | The delivered audit provides preferred upgrades, compatibility bridges, temporary mitigations, release gating, ownership, and verification/testing steps without modifying requirements.txt. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=109b986b4018ed5121d20e83d0f03f39a0aaef687eb5dd7c1936ee4b3a089210; fixture_sha256=8307ea1325de4c132e54824c9dd507ed174ce29fe901e9f04e5a56bc654490e3; output_sha256=bf7a5137129a406f8e881b1e8539838776e91725b3e291821a83da80bb49a8bc; snapshot_sha256=f744253c33cd727a74a312b55f4ca9eea798c349cb66a7480fa6e12b37a39621
- Behavior: Produced a structured dependency security audit covering inventory, classified risks, direct evidence, and actionable upgrades/mitigations; delivered the report without forbidden dependency changes.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=109b986b4018ed5121d20e83d0f03f39a0aaef687eb5dd7c1936ee4b3a089210; fixture_sha256=8307ea1325de4c132e54824c9dd507ed174ce29fe901e9f04e5a56bc654490e3; output_sha256=4bb2da364f3504e392c9ecdd4801a5b097b859d0b647d8d3a201e38f4787b780; snapshot_sha256=d4dae3d71b2e3bfc13b38eb590faf499f92fdd0146db25884c63b5b741ab246f
- Behavior: Produced a broadly similar audit and comparison report, including package risks and upgrade suggestions; used only as fresh-baseline context.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
