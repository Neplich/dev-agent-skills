# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-005-route-deployment-request`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-5-route-deployment-request`.
- Identity schema: `2`
- target_skill_sha256: `a37bf10fca64a8e15e6213ecdd45b65783814d307c78fd8d8ce6ab45b20effef`
- eval_definition_sha256: `cad357efac6928bd9cbca7d09df3972a7367fdbfc93dd87da1f5982bf69d7b10`
- metadata_sha256: `d17a05b229136107ac1e50142856979a9ae9f563cdb19b940e4810dadda79e1c`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `42fd42dc7a350eab589db47b48a132e9f478c8e119c1fdbd30b4875075f9f0b5`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `df8dd8d18e0b79f0114ea9e750efb47af7d21bc05b6ea3666cff7d6bae4802fe`
- Repository HEAD: `3f5e81c4837ef85284a7d5381575e40267796c92`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `6f4abf80e411dc3e6124c51093f07046c341195b1b2f0e9981a535c9960cb623`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `request_type_deployment` | PASS | With-skill output and trace explicitly classify the request as `request_type: deployment`. |
| `repo_wide_scope_allowed` | PASS | With-skill output records `feature_path: N/A`, `feature: N/A`, `parent_feature: N/A`, `feature_level: N/A`, and `feature_path_evidence: []`. |
| `devops_handoff_packet` | NOT_EXERCISED | The candidate correctly blocked the downstream DevOps handoff because `devops-agent` and required environment, release, rollback, and build/test context were unavailable; no completed handoff packet is exercised. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=df8dd8d18e0b79f0114ea9e750efb47af7d21bc05b6ea3666cff7d6bae4802fe; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=ec193f40460cbf20f80c73e9e1ae02f31d10222757af0e8313b9e50392ad1d76; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly classified the request, allowed repository-wide N/A scope, and stopped at the unavailable DevOps handoff boundary without mutations.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=df8dd8d18e0b79f0114ea9e750efb47af7d21bc05b6ea3666cff7d6bae4802fe; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=66a220a974b5903285a5c97c9aee139ab6ad284f6bededc092f71ef84148e781; snapshot_sha256=f9d5b45620285dd10d5b4ac4a8b7528f206e52d4182e29f6a6d90a7e4e55c08b
- Behavior: Created CI and release-checklist files as a fresh baseline, but did not provide the PM classification or handoff context.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Install or enable the DevOps agent.
- Next: Provide the deployment environment, target, build/test commands, release scope, operational goal, and rollback needs before resuming the handoff.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
