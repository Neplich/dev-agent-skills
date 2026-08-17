# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-015-route-docs-site-deployment-gap`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `16e3b6cbbbae6769ac6b5ead7bae34214b3dd90e3e6c4d5fad97cfd7d3784013` from `agents/product_manager/test/pm-agent/evals/workspace/eval-015-route-docs-site-deployment-gap`.
- Identity schema: `2`
- target_skill_sha256: `e17c69ef6e179644f91ff00df55f141c375753f4668f30aca4e37e8247a60506`
- eval_definition_sha256: `8bc69d85fc3ff063d885b8a2c4d7a9ea83b6dca3de23a034dba15fb34f1ba98e`
- metadata_sha256: `7cd2581ae78239652e35a53401d899646cf1bf57925a7928ae3b61ce61b991b9`
- fixture_sha256: `16e3b6cbbbae6769ac6b5ead7bae34214b3dd90e3e6c4d5fad97cfd7d3784013`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `69f2798cad12b0dd0ca3c224e3cfd6cf611a315695684db1b07a23452b52a60e`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `f6c9996daf9a7bdf78228fb674eccb457f386d1e74abf9925ac4646e4da1c9d4`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `260ef2f905808fdff59ef7a047662603594e4a851b7569ea158bfc0c5228c88d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_unknown_evidence` | PASS | With-skill output reports `partial`, identifies missing CI/CD, runtime, Helm, health-check, ingress, and access-control evidence, and does not treat the site as integrated or ready for deployment. |
| `builds_repo_wide_deployment_packet` | PASS | The locked PM handoff packet uses `request_type: deployment`, sets feature fields to `N/A`, uses `feature_path_evidence: []`, and preserves source documents plus evidence-based blockers. |
| `routes_devops_ordered_chain` | PASS | The output gives the ordered chain `deployment-planner → cicd-bootstrap → env-config-auditor → formal-docs-sync`, identifies DevOps as the next owner, and preserves the no-commit/no-publish/no-deploy boundary pending confirmation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f6c9996daf9a7bdf78228fb674eccb457f386d1e74abf9925ac4646e4da1c9d4; fixture_sha256=16e3b6cbbbae6769ac6b5ead7bae34214b3dd90e3e6c4d5fad97cfd7d3784013; output_sha256=bb23227f324d8622785052dba9228284699a94efcc26218266155c954c565b57; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly identifies partial deployment coverage, builds a repo-wide deployment handoff, and specifies the ordered DevOps-to-Docs chain.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f6c9996daf9a7bdf78228fb674eccb457f386d1e74abf9925ac4646e4da1c9d4; fixture_sha256=16e3b6cbbbae6769ac6b5ead7bae34214b3dd90e3e6c4d5fad97cfd7d3784013; output_sha256=6b11e90417b571f937dc2b12ea5b63dd4439615160d204147c85e85fcadeafc7; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a cautious planning response but does not build the required deployment packet or route the complete ordered chain.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
