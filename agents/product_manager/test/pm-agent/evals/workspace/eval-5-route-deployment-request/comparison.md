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
- target_skill_sha256: `cec475406cc49b4c9cebbfe9c62f8f1a19fc3e7ced9282825f8f2930bab1478a`
- eval_definition_sha256: `cad357efac6928bd9cbca7d09df3972a7367fdbfc93dd87da1f5982bf69d7b10`
- metadata_sha256: `d17a05b229136107ac1e50142856979a9ae9f563cdb19b940e4810dadda79e1c`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `42fd42dc7a350eab589db47b48a132e9f478c8e119c1fdbd30b4875075f9f0b5`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `df8dd8d18e0b79f0114ea9e750efb47af7d21bc05b6ea3666cff7d6bae4802fe`
- Repository HEAD: `133a65e3c3b501be88257e9d3a557af4d5ccd242`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `5047311446f87e0c9eb6ef7577938db174e729f8d09b2851971cbb87a063bf63`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `request_type_deployment` | PASS | With-skill locked output explicitly sets `request_type: deployment` for the CI and pre-release-check request. |
| `repo_wide_scope_allowed` | PASS | With-skill locked output uses `feature_path: N/A`, `feature: N/A`, `parent_feature: N/A`, `feature_level: N/A`, and `feature_path_evidence: []` for repository-level CI work. |
| `devops_handoff_packet` | PASS | With-skill locked output records confirmed repository CI/release scope, required outputs, environment and rollback gaps, and risks before identifying the DevOps owner and next action. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=df8dd8d18e0b79f0114ea9e750efb47af7d21bc05b6ea3666cff7d6bae4802fe; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=055cb8f01d95d5aa1d721d4f4c45f2ce508314995050e06567efe4732b2f0a18; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly classified the request, allowed repository-level N/A scope, and produced a DevOps handoff packet; execution stopped at the unavailable downstream agent.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=df8dd8d18e0b79f0114ea9e750efb47af7d21bc05b6ea3666cff7d6bae4802fe; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=acf5289b685e517384701b53c8d579b00529a195fc73e419aa4adcb8b4641bb1; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Performed a repository inspection and reported the empty repository, but did not provide the required deployment classification or handoff packet.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Install or provide devops-agent, then confirm environment, release target, and rollback strategy before executing CI and pre-release checks.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
