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
- target_skill_sha256: `e17c69ef6e179644f91ff00df55f141c375753f4668f30aca4e37e8247a60506`
- eval_definition_sha256: `cad357efac6928bd9cbca7d09df3972a7367fdbfc93dd87da1f5982bf69d7b10`
- metadata_sha256: `0bdb522f0df207a2778e820083da8ba9d4f3194004ea2be94909f7b00fa189be`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `42fd42dc7a350eab589db47b48a132e9f478c8e119c1fdbd30b4875075f9f0b5`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `df8dd8d18e0b79f0114ea9e750efb47af7d21bc05b6ea3666cff7d6bae4802fe`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `d2535385fc058d23601a81cc3e6475f8a9805aa0738fe404481cd2e9da3b8bb7`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `request_type_deployment` | PASS | With-skill output explicitly sets `request_type: deployment` for repository CI/CD and pre-release readiness work. |
| `repo_wide_scope_allowed` | PASS | With-skill packet uses `feature_path: N/A`, `feature: N/A`, `parent_feature: N/A`, `feature_level: N/A`, and `feature_path_evidence: []` for confirmed repository-level work. |
| `devops_handoff_packet` | NOT_EXERCISED | The output identifies DevOps as downstream owner and records scope, required outputs, and risks, but the handoff is blocked pending user confirmation of environment, release target, and rollback details. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=df8dd8d18e0b79f0114ea9e750efb47af7d21bc05b6ea3666cff7d6bae4802fe; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=8058f15cdab1dc61ff16909f93be5afd3f5acaeb29acae5e4a943fd8138d853a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly classified the request as deployment and produced a repository-level N/A scope packet; handoff remained blocked pending required operational context.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=df8dd8d18e0b79f0114ea9e750efb47af7d21bc05b6ea3666cff7d6bae4802fe; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=c307c5ad8e9440053946e81799161637ef91fd3ca11b32ae11b65e5f2fbc070a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Stopped at the empty repository snapshot without producing deployment classification or a DevOps handoff packet.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide the missing environment, release scope, CI platform, and rollback details, then complete the DevOps handoff.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
