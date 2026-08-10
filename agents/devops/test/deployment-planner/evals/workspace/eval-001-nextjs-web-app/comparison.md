# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `deployment-planner`
- Eval: `eval-001-nextjs-web-app`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `06f8a5807d1130b7a91a700b2074192e6dfed0933a071ce16642b27aa050360d` from `agents/devops/test/deployment-planner/evals/workspace/eval-001-nextjs-web-app`.
- Fixture SHA-256: `06f8a5807d1130b7a91a700b2074192e6dfed0933a071ce16642b27aa050360d`
- Prompt SHA-256: `cd186dfdcf8b04b4e66f71faf5fd0b7ea6c6616c86ae2015f0fd5d6d730418e8`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e850d2052b73e431758456627cb816e0d9a45db383146d1349cf24ca05b2aec1`
- Skill overlay SHA-256: `69cf7483c4142716ecdbb6a031121f60813fdaad8bcb74124bd2f705524d6549`
- Judge schema SHA-256: `8fdd554bf7008e1addc7b92301444335139887034f2813ab539445a1df4b82d6`
- Eval definition SHA-256: `4ab6f3577023497f11197efb5117e95119ab70a437c95770925330f5be6aa5f2`
- Metadata SHA-256: `be29fd9ddbc554b7d8ca7f9912c9d54f61470e99abd7c2e138b60022c4086794`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_local_runtime_assets` | PASS | with_skill delivery_snapshot contains deploy/local/.env.example with PORT=3000, DATABASE_URL, REDIS_URL, plus README/start.sh invoking npm run start. |
| `creates_complete_compose_topology` | PASS | with_skill deploy/docker contains Dockerfile and docker-compose.yml defining app, postgres, redis, with app healthcheck targeting /api/health. |
| `creates_application_helm_chart` | PASS | with_skill deploy/helm contains Chart.yaml, values.yaml with replicaCount and database/Redis values, and Deployment templating those values into application secrets; no dependency services are charted. |
| `documents_each_target_without_delivery` | PASS | with_skill has README documentation for local, Docker, and Helm; locked evidence shows only deployment assets, no CI/CD files or production credentials, and explicitly states deployment was not executed. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cd186dfdcf8b04b4e66f71faf5fd0b7ea6c6616c86ae2015f0fd5d6d730418e8; fixture_sha256=06f8a5807d1130b7a91a700b2074192e6dfed0933a071ce16642b27aa050360d; output_sha256=38dbe6741c5cdd99e4bdfeea9a6d78f17be7b4ab5cf7a9055bf20874bb41813e; snapshot_sha256=c75f999cbda6442eb70d832d3749f4a51e2d0970a86559e30e89c310836786d4
- Behavior: Delivered all three requested deployment targets with matching runtime contracts and documentation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cd186dfdcf8b04b4e66f71faf5fd0b7ea6c6616c86ae2015f0fd5d6d730418e8; fixture_sha256=06f8a5807d1130b7a91a700b2074192e6dfed0933a071ce16642b27aa050360d; output_sha256=29062a232cb4a67d2794948dacdf2f4452e6881b3e041addb2317522df61a0db; snapshot_sha256=04c713e1cee89b12b5d0a70eb947ea019a4edfac205e59fa4729c5e02a3795f6
- Behavior: Delivered Docker and Helm assets, but local README uses npm run dev and lacks the with_skill local start script, conflicting with the required npm run start contract.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
