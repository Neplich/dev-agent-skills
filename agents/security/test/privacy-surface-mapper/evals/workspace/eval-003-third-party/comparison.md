# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `privacy-surface-mapper`
- Eval: `eval-003-third-party`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `a0f9b5ed56aa92319d126897928b2da5ef1b5b085fbe003f0b4425dde5805c73` from `agents/security/test/privacy-surface-mapper/evals/workspace/eval-003-third-party`.
- Identity schema: `2`
- target_skill_sha256: `25bd4dbed66f3625883b2a2072dcd568eef569278521e1eac012e86f61347836`
- eval_definition_sha256: `fde37322a972618cf8b85d5463c8e7a856c7547f8c15123669fd15297f556852`
- metadata_sha256: `1b358949b025cd13ff498cda0a21978c243d4781824a1ceab1947fe97db21069`
- fixture_sha256: `a0f9b5ed56aa92319d126897928b2da5ef1b5b085fbe003f0b4425dde5805c73`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `46c6f10cb2ee094e0f2d9b8cf0d9d794ebc801a301eb97187a76e961b4e37fd0`
- Identity migration: **MIGRATED_WITHOUT_MODEL_RERUN**
- Identity migration source commit: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Identity migration audit: `docs/engineer/repository-governance/eval-scenario-isolation/eval-identity-v2-migration-audit.json`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `data_inventory` | PASS | Delivered privacy map inventories fields, data categories, collection/send entry points, recipients, and purposes with code-linked evidence. |
| `sharing_and_retention` | PASS | Delivered report identifies recipients, US/unknown regions, configured retention, missing Ads retention/deletion evidence, and distinguishes configured policy from runtime proof. |
| `user_rights` | PASS | Delivered report assesses consent, access, deletion, export/portability, correction, and vendor-rights propagation; it does not overclaim ExamplePay’s configured deletion API. |
| `compliance_gaps` | PASS | Delivered report provides prioritized consent, transfer, retention, deletion, rights-workflow, and data-minimization gaps with actionable recommendations. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f08db36d8714dffcf75b41015d8dc4b37be4570b39ece9523f67238ebf8ed935; fixture_sha256=a0f9b5ed56aa92319d126897928b2da5ef1b5b085fbe003f0b4425dde5805c73; output_sha256=f35e241ad05b3d77d19064f277adf84dfab9804474c25fc8607a362596cf610a; snapshot_sha256=3ada52de09d056e2710a0a35359b8e6bacb804eefe03a0cda5277403f3115669
- Behavior: Produced the required Security-owned privacy map with evidence freshness, data inventory, sharing/retention assessment, user-rights status, compliance risks, recommendations, and PM escalation; no integration or formal-site mutation is evidenced.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f08db36d8714dffcf75b41015d8dc4b37be4570b39ece9523f67238ebf8ed935; fixture_sha256=a0f9b5ed56aa92319d126897928b2da5ef1b5b085fbe003f0b4425dde5805c73; output_sha256=f908ed5559b2025e8e26959988fc854921f319ab7ff12c04f63704864c708e15; snapshot_sha256=7361618269c208e63dd59ce9e60cc016c1c0ac9c89aedcfa3523f88d13eb33f4
- Behavior: Produced a broadly correct sharing report and recommendations, but with less explicit evidence-freshness, runtime-evidence qualification, and structured rights/compliance treatment than the with_skill lane.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
