# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `deployment-planner`
- Eval: `eval-002-python-api-only`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `259dab4dbfe64941c0c3fdd5c97b56c6b90abb97168eeb7461bd9a7bf8e30888` from `agents/devops/test/deployment-planner/evals/workspace/eval-002-python-api-only`.
- Fixture SHA-256: `259dab4dbfe64941c0c3fdd5c97b56c6b90abb97168eeb7461bd9a7bf8e30888`
- Prompt SHA-256: `000bcbda1f774e89fec492193e606a35b1ac2f41c0b29e0c9ac66b491aa38c8b`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `762ea3248d76c5c9e715368b11ab616562bb9bdb0e2bd6a6aad38d47cc80b3af`
- Skill overlay SHA-256: `52ed13d453014671ce8cc7f7f7ce4b4108c3a5cc943fcf3bece1ac66b08625d5`
- Judge schema SHA-256: `6d6cb805f86354c5ca7fe62a901b9a052b0e2f5bc53f163da17451ac99ca29a5`
- Eval definition SHA-256: `f6bee599168504aabc5841db04bc20810e822fd2af8545bc98e19f6298c38285`
- Metadata SHA-256: `cd34fc596ce17b79112511df2244a7b68d45546111925715157c8598360bb097`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_confirmed_target_matrix` | PASS | Locked delivery snapshot contains deploy/local, deploy/docker, and deploy/helm assets only; no additional deployment target category is present. |
| `keeps_api_only_topology` | PASS | Compose defines only the api service. Snapshots contain no database, Redis, migration, DATABASE_URL, or dependent service configuration. |
| `uses_confirmed_runtime_contract` | PASS | Local start.sh, Dockerfile, and the image used by Helm specify uvicorn app.main:app and port 8000; Docker and Helm probes use /health, and local documentation verifies /health. |
| `stays_within_deployment_scope` | PASS | Locked snapshot contains no CI/CD configuration and git evidence shows no commits or external deployment/publication actions; publication is explicitly deferred/documented as handoff only. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=000bcbda1f774e89fec492193e606a35b1ac2f41c0b29e0c9ac66b491aa38c8b; fixture_sha256=259dab4dbfe64941c0c3fdd5c97b56c6b90abb97168eeb7461bd9a7bf8e30888; output_sha256=66117e8af42e170775bdc637cc090568e79efa1bd3a6b4cca8046db8ba26434a; snapshot_sha256=1b62515296e834bf18a03e7fba779dc8d39399e9d875e8149023800065fbc880
- Behavior: Delivered local, Docker, and Helm deployment assets with API-only topology and matching runtime/health-check contract; no CI/CD or actual publication was performed.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=000bcbda1f774e89fec492193e606a35b1ac2f41c0b29e0c9ac66b491aa38c8b; fixture_sha256=259dab4dbfe64941c0c3fdd5c97b56c6b90abb97168eeb7461bd9a7bf8e30888; output_sha256=228ce914bd48a36eb390e5c84715acd4c0a64e6e716c8718513f840d4652cf7c; snapshot_sha256=6682a514cf779307fc10e5fa70a359d2895a7b08da00f02f1ea4a949da8f976c
- Behavior: Delivered local, Docker, and Helm assets with matching runtime contract and API-only Compose topology; no CI/CD or actual publication was performed.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
