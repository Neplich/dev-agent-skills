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
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e850d2052b73e431758456627cb816e0d9a45db383146d1349cf24ca05b2aec1`
- Skill overlay SHA-256: `69cf7483c4142716ecdbb6a031121f60813fdaad8bcb74124bd2f705524d6549`
- Judge schema SHA-256: `6d6cb805f86354c5ca7fe62a901b9a052b0e2f5bc53f163da17451ac99ca29a5`
- Eval definition SHA-256: `f6bee599168504aabc5841db04bc20810e822fd2af8545bc98e19f6298c38285`
- Metadata SHA-256: `cd34fc596ce17b79112511df2244a7b68d45546111925715157c8598360bb097`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_confirmed_target_matrix` | PASS | with_skill delivers only local, Docker/Compose, and Helm assets under deploy/. |
| `keeps_api_only_topology` | PASS | Compose contains one api service; snapshots contain no database, Redis, migration, DATABASE_URL, or dependency service. Empty ConfigMap/Secret templates do not add runtime dependencies. |
| `uses_confirmed_runtime_contract` | PASS | Local start.sh, Dockerfile, Compose healthcheck, and Helm probes consistently use app.main:app, port 8000, and /health. |
| `stays_within_deployment_scope` | PASS | No CI/CD configuration or execution evidence is present; CI/CD is explicitly marked as handoff/blocked, and no image publish or deployment was performed. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=000bcbda1f774e89fec492193e606a35b1ac2f41c0b29e0c9ac66b491aa38c8b; fixture_sha256=259dab4dbfe64941c0c3fdd5c97b56c6b90abb97168eeb7461bd9a7bf8e30888; output_sha256=b9d3dda7eda1aa20ec060b3d25cd7d7f91ded3a440712d356d652288828121c3; snapshot_sha256=95e60eab5f7a98cd5f6a82e96cd5895b2b6853c3b0fb32f9eb318ea40d3b675a
- Behavior: Delivered the three confirmed deployment targets with consistent API-only runtime settings and explicit CI/CD boundary.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=000bcbda1f774e89fec492193e606a35b1ac2f41c0b29e0c9ac66b491aa38c8b; fixture_sha256=259dab4dbfe64941c0c3fdd5c97b56c6b90abb97168eeb7461bd9a7bf8e30888; output_sha256=34ca0b3723625f420d89a9d48302bdc4aee333b4a6483279b94e704a774e04f5; snapshot_sha256=494a440b02a2d61cb721d0400e9b91353ecd8baf6775b7ec6f9877651d524f76
- Behavior: Also delivered the three confirmed targets with a simpler Helm chart and no extra ConfigMap, Secret, or HPA templates.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
