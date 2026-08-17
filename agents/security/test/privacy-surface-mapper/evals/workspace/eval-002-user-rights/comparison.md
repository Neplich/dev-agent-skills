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
- target_skill_sha256: `2d9aa34423715a24783169e774af3c68a95cbc320b5fc5af4b5753bd7785f2a0`
- eval_definition_sha256: `ba5034d1b895bcb95cc9d848045b869189eec2c98d23c0a5d5ce381059a73047`
- metadata_sha256: `747c4437caa882844d7f4c740414dcda7c0dbb14392d11ed34230c9d397ac11a`
- fixture_sha256: `2a160ab6ab1065aa7d10a9502c97feefe12d13d5af072b1075181fbf932723d8`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `46c6f10cb2ee094e0f2d9b8cf0d9d794ebc801a301eb97187a76e961b4e37fd0`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `f954f6fb2beee6f446fdaf1e7380f20a7139675884dad90e43a17db9c8bbe9d0`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `2eea2d31331dfff7d98326573b856ca9f269bca068d5f182bf99e8b0d5d75219`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `data_inventory` | PASS | Locked privacy-map.md inventories user profiles, orders, behavioral events, and deletion markers, with purposes and endpoint/data-flow evidence. |
| `sharing_and_retention` | PASS | Locked privacy-map.md identifies unknown retention, absent retention/legal-hold policy, unavailable processor/transfer evidence, and risks from incomplete deletion propagation. |
| `user_rights` | PASS | Locked report evaluates access, export, deletion, rectification, authentication, tracking, and secure delivery; it identifies the IDOR and incomplete rights implementation. |
| `compliance_gaps` | PASS | Locked report provides prioritized privacy/compliance gaps, impacts, remediation recommendations, testing needs, release decision, and ownership handoff. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f954f6fb2beee6f446fdaf1e7380f20a7139675884dad90e43a17db9c8bbe9d0; fixture_sha256=2a160ab6ab1065aa7d10a9502c97feefe12d13d5af072b1075181fbf932723d8; output_sha256=4f1686815c031c0354874ed2e02c4a5fef0e8862ea32de0f297fa15f8b6af614; snapshot_sha256=f4fff6995d67d1a0f1267bce96ae33a88f10531bf94d7ed8c75119eb65d2fbc4
- Behavior: Delivered a substantive privacy surface map and Security-owned report covering data inventory, flows, rights status, retention/sharing uncertainty, risks, compliance gaps, remediation, testing, and ownership.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f954f6fb2beee6f446fdaf1e7380f20a7139675884dad90e43a17db9c8bbe9d0; fixture_sha256=2a160ab6ab1065aa7d10a9502c97feefe12d13d5af072b1075181fbf932723d8; output_sha256=60f5e601c0ee402d8d5b0c6c71223b1d3524d376480603718345e5e1bb3f2066; snapshot_sha256=747c584d699b0109b79425e40cb79a3695b477ac37a195b823fcb9d57b261942
- Behavior: Delivered a shorter security report identifying major authorization, deletion, export, retention, and abuse-control gaps, but with less complete data inventory and privacy-surface mapping.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
