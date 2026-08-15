# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `privacy-surface-mapper`
- Eval: `eval-002-user-rights`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `2a160ab6ab1065aa7d10a9502c97feefe12d13d5af072b1075181fbf932723d8` from `agents/security/test/privacy-surface-mapper/evals/workspace/eval-002-user-rights`.
- Identity schema: `2`
- target_skill_sha256: `36470092bada7ef550e554a98c281f2fe94c427f5a20542e3fb5f13c69f3b496`
- eval_definition_sha256: `ba5034d1b895bcb95cc9d848045b869189eec2c98d23c0a5d5ce381059a73047`
- metadata_sha256: `747c4437caa882844d7f4c740414dcda7c0dbb14392d11ed34230c9d397ac11a`
- fixture_sha256: `2a160ab6ab1065aa7d10a9502c97feefe12d13d5af072b1075181fbf932723d8`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `46c6f10cb2ee094e0f2d9b8cf0d9d794ebc801a301eb97187a76e961b4e37fd0`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `f954f6fb2beee6f446fdaf1e7380f20a7139675884dad90e43a17db9c8bbe9d0`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `04d179782a25ad87f73775d407c14368f4301d86a871528ca2b66e82792a813b`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `data_inventory` | PASS | The locked report inventories user profiles, orders, behavioral events, and deletion state, and maps them to the relevant endpoints and purposes. |
| `sharing_and_retention` | PASS | The locked report identifies analytics, backups, caches, queues, and other replicas as unverified sharing/retention surfaces, with risks and remediation recommendations. |
| `user_rights` | PASS | The locked report evaluates access, export, deletion, and correction support, including the concrete authorization and completeness failures. |
| `compliance_gaps` | PASS | The locked report provides prioritized privacy/compliance gaps, impacts, release recommendation, and specific remediation actions. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f954f6fb2beee6f446fdaf1e7380f20a7139675884dad90e43a17db9c8bbe9d0; fixture_sha256=2a160ab6ab1065aa7d10a9502c97feefe12d13d5af072b1075181fbf932723d8; output_sha256=4fec90ad5171ffa1d71590300bb972d1db736310884a48b2577d188eec3d0711; snapshot_sha256=b0f2c05bdf064b6de3871991b0de177751e9cc6a0afb19a912b77cec7d0f67a1
- Behavior: Delivered a complete, evidence-based privacy surface report covering inventory, sharing/retention, user rights, compliance gaps, impacts, and remediation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f954f6fb2beee6f446fdaf1e7380f20a7139675884dad90e43a17db9c8bbe9d0; fixture_sha256=2a160ab6ab1065aa7d10a9502c97feefe12d13d5af072b1075181fbf932723d8; output_sha256=19592d4e533b772e691eb1faba88cc94920ed2f24d611e4b12328d0f73d62e47; snapshot_sha256=639e6b256cf553b2976000518a3b8f4d3b8cf58bbb6d4b2eedbfc112270658bb
- Behavior: Produced a solid comparison report covering the principal authorization, export, deletion, retention, and audit gaps, but with less complete inventory and compliance mapping.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
