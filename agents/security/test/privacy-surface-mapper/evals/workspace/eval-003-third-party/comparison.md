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
- target_skill_sha256: `36470092bada7ef550e554a98c281f2fe94c427f5a20542e3fb5f13c69f3b496`
- eval_definition_sha256: `fde37322a972618cf8b85d5463c8e7a856c7547f8c15123669fd15297f556852`
- metadata_sha256: `2bb39446486b68c792ab91df36f237757842e6cc3f736b5a421d1cc25cf91455`
- fixture_sha256: `a0f9b5ed56aa92319d126897928b2da5ef1b5b085fbe003f0b4425dde5805c73`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `46c6f10cb2ee094e0f2d9b8cf0d9d794ebc801a301eb97187a76e961b4e37fd0`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `f08db36d8714dffcf75b41015d8dc4b37be4570b39ece9523f67238ebf8ed935`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `04d179782a25ad87f73775d407c14368f4301d86a871528ca2b66e82792a813b`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `data_inventory` | PASS | With-skill delivery snapshot inventories all three vendors, fields, data categories, purposes, and code-triggered sending paths with direct file references. |
| `sharing_and_retention` | PASS | With-skill report identifies sharing recipients, US/unknown regions, configured retention, missing or limited deletion support, and distinguishes configured policy from runtime proof. |
| `user_rights` | PASS | With-skill report evaluates access, deletion, export, correction, consent, and propagation gaps, including the payment deletion API limitation. |
| `compliance_gaps` | PASS | With-skill report provides prioritized compliance risks and concrete recommendations covering consent, minimization, rights propagation, regional transfer evidence, retention, deletion, and follow-up ownership. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f08db36d8714dffcf75b41015d8dc4b37be4570b39ece9523f67238ebf8ed935; fixture_sha256=a0f9b5ed56aa92319d126897928b2da5ef1b5b085fbe003f0b4425dde5805c73; output_sha256=972b8801eb902b8f1e90ac6658596ecfab64aceac7a9af580fdc8975ef01c1aa; snapshot_sha256=5721405a998f34cb0c5b70271637df91afbf8ab3911ebbc1a905c9d336c83c6c
- Behavior: Delivered a complete, evidence-linked privacy processing map and actionable compliance assessment without implementing unrelated fixes.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f08db36d8714dffcf75b41015d8dc4b37be4570b39ece9523f67238ebf8ed935; fixture_sha256=a0f9b5ed56aa92319d126897928b2da5ef1b5b085fbe003f0b4425dde5805c73; output_sha256=d0319b007fdf0d61094c0552b74470891cbe8ec9a300cfc6e4cdbe87b264ae93; snapshot_sha256=fb6708495744d5e5bd995c66cc80bb7e2b7ce1041c9583867560c13b64e96052
- Behavior: Provided a shorter third-party sharing report covering the main findings, useful as a fresh baseline comparison.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
