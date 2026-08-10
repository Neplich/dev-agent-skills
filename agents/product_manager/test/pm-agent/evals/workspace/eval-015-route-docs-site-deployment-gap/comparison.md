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
- Fixture SHA-256: `16e3b6cbbbae6769ac6b5ead7bae34214b3dd90e3e6c4d5fad97cfd7d3784013`
- Prompt SHA-256: `f6c9996daf9a7bdf78228fb674eccb457f386d1e74abf9925ac4646e4da1c9d4`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `1cfd412fc44e8e1667cc3feab76a58474b6382f405680057b41b379032f76e0a`
- Skill overlay SHA-256: `8ddfbafd6ae3cf064836ded5fbaa7bcc8a3ab817df212a0b6c4ff355a78b12af`
- Judge schema SHA-256: `69f2798cad12b0dd0ca3c224e3cfd6cf611a315695684db1b07a23452b52a60e`
- Eval definition SHA-256: `6e2d29edefa67ed434a00461a929405f7c4bccd693a99ad48559b546fe6fab29`
- Metadata SHA-256: `e7a743e88e4c53094e4afe2903a87ebcc467ace2dc58c61ccb0a0dcf64ebf2fd`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_unknown_evidence` | PASS | With-skill output correctly reports partial deployment coverage, identifies missing image/deployment/verification evidence, and does not claim integrated or ready handoff. |
| `builds_repo_wide_deployment_packet` | PASS | With-skill output provides request_type: deployment, N/A feature fields, feature_path_evidence: [], and preserves the four source documents plus concrete blockers/risks. |
| `routes_devops_ordered_chain` | NOT_EXERCISED | With-skill output routes the next action to DevOps, but devops-agent is unavailable, so the downstream ordered specialist chain was not exercised. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f6c9996daf9a7bdf78228fb674eccb457f386d1e74abf9925ac4646e4da1c9d4; fixture_sha256=16e3b6cbbbae6769ac6b5ead7bae34214b3dd90e3e6c4d5fad97cfd7d3784013; output_sha256=382180018be078b45dea4f66fef89af8050d32d3a3613a6b2f0834697818e2ff; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly classifies the deployment as partial, builds a repo-wide deployment packet, and routes the next action to DevOps without mutation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f6c9996daf9a7bdf78228fb674eccb457f386d1e74abf9925ac4646e4da1c9d4; fixture_sha256=16e3b6cbbbae6769ac6b5ead7bae34214b3dd90e3e6c4d5fad97cfd7d3784013; output_sha256=61550374aa131f016a2de214d0d5bdae5abf7c780d8580481b4b4741fa226d67; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a cautious planning response but does not build the required deployment packet or explicit ordered routing chain.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Run the ordered DevOps specialist chain when devops-agent is available.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
