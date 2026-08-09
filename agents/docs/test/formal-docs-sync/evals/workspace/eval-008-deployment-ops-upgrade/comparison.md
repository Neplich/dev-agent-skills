# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-008-deployment-ops-upgrade`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `214f53e3513d921f93697a6af50dd22ab635d80910879e93ccbc5d847195e845` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-008-deployment-ops-upgrade`.
- Fixture SHA-256: `214f53e3513d921f93697a6af50dd22ab635d80910879e93ccbc5d847195e845`
- Prompt SHA-256: `47aecb4a312eb41566bd1acc858dd108cbb65075c955dc6992e37865198bfec5`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a0fd1ad6b8713d6036307d1b20788b4771cc4b6ba53645fe17625e0dd55bbb5b`
- Skill overlay SHA-256: `73e88fe8c07f988c3353f81f9b058d4f8350c48ee381f924fe8c8201b9f92bb4`
- Judge schema SHA-256: `f5d562d8581b8e42e3d9fc6fee3e3cf82b682235e3b52ce9b9c4f91a22e1e752`
- Eval definition SHA-256: `7fe3c7ecf4038349101f98fb6f2ef19330f01c150bee2276a165994129650157`
- Metadata SHA-256: `2f78367477eb99dc045585689bae85fd3302b30aa534650ea910cd64f9bdfbbe`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_executed_deployment_evidence` | PASS | The delivered pages identify deploy/compose.yaml and deployment-evidence/deployment-results.md as sources, and accurately record the executed Compose results, health response, and environment differences. |
| `writes_current_ops_upgrade_rollback` | PASS | Docker pages record Compose startup and upgrade commands, HTTP 200 /healthz success criteria, rollback to v1.4.1 with post-rollback health verification, and the v1.4.2 AI_HUB_IMAGE default with Compose evidence. |
| `does_not_promote_plan_to_current_state` | PASS | The deployment index explicitly states Kubernetes/Helm migration is planned, unexecuted, and unsupported as a current deployment path. |
| `writes_current_deployment_tree_atomically` | PASS | All four required pages are delivered with unverified front matter; links are present across Ops, deployment, and Docker indexes. The fixture change map contains all four deploy/** mappings and preserves deploy/examples/** exclusion; unrelated sections are untouched in the locked status. |
| `runs_ops_host_checks_and_handoffs` | NOT_EXERCISED | The candidate reports npm run test:docs and an audit handoff, but the locked raw evidence does not independently prove real command execution or a completed docs-agent:docs-audit handoff; the handoff is explicitly blocked pending release context. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47aecb4a312eb41566bd1acc858dd108cbb65075c955dc6992e37865198bfec5; fixture_sha256=214f53e3513d921f93697a6af50dd22ab635d80910879e93ccbc5d847195e845; output_sha256=1b6260557181edb8fb286e5e1c25274097a1085012092e59498e2ea1d0a2a5b2; snapshot_sha256=a78cd5fadae9950ce201fbc6f0c5936c8647c082b40cbff09c0aa33dd3550503
- Behavior: Delivered the requested Docker deployment documentation coherently, preserved the Kubernetes/Helm boundary, and reported the missing release context that blocks audit handoff.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47aecb4a312eb41566bd1acc858dd108cbb65075c955dc6992e37865198bfec5; fixture_sha256=214f53e3513d921f93697a6af50dd22ab635d80910879e93ccbc5d847195e845; output_sha256=afb649dbe205dd9f48a12a3d1c473c9685e73f8f09089570238c7710d7f7f5d6; snapshot_sha256=32aeabcde050854e4febe70c7a3cb2905f15f3142733cf43fbc1a60ee31acc43
- Behavior: Delivered broadly similar deployment pages and checks, but provided less explicit gating and process context; comparison only.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide confirmed release context and independently capture the docs audit handoff and host-check results.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
