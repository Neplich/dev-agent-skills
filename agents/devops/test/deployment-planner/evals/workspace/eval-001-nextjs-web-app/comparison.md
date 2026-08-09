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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `762ea3248d76c5c9e715368b11ab616562bb9bdb0e2bd6a6aad38d47cc80b3af`
- Skill overlay SHA-256: `52ed13d453014671ce8cc7f7f7ce4b4108c3a5cc943fcf3bece1ac66b08625d5`
- Judge schema SHA-256: `8fdd554bf7008e1addc7b92301444335139887034f2813ab539445a1df4b82d6`
- Eval definition SHA-256: `4ab6f3577023497f11197efb5117e95119ab70a437c95770925330f5be6aa5f2`
- Metadata SHA-256: `be29fd9ddbc554b7d8ca7f9912c9d54f61470e99abd7c2e138b60022c4086794`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_local_runtime_assets` | PASS | With-skill snapshot includes deploy/local/.env.example and executable deploy/local/start.sh plus README documenting npm run start, port 3000, DATABASE_URL, and REDIS_URL. |
| `creates_complete_compose_topology` | PASS | With-skill snapshot includes Dockerfile and docker-compose.yml defining app, postgres, and redis services; app healthcheck calls /api/health and dependencies have healthchecks. |
| `creates_application_helm_chart` | PASS | With-skill snapshot includes Chart.yaml, values.yaml, and Deployment template with replicaCount and PostgreSQL/Redis values injected through the Secret. |
| `documents_each_target_without_delivery` | PASS | Local, Docker, Helm, and deploy/README.md document usage and health checks; evidence explicitly states no deployment and no CI/CD rules, with placeholder credentials only. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cd186dfdcf8b04b4e66f71faf5fd0b7ea6c6616c86ae2015f0fd5d6d730418e8; fixture_sha256=06f8a5807d1130b7a91a700b2074192e6dfed0933a071ce16642b27aa050360d; output_sha256=cdb26857568fc97cd812f806d4331ad234b98ba44a8612161ad5938152041370; snapshot_sha256=893888204298be503f0a41a545efdd35638d4069c1b49cf441d6fce4cf1b8bad
- Behavior: Delivered all three deployment targets with executable local startup, complete Compose topology, application-only Helm chart, cross-target documentation, and explicit non-deployment status.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cd186dfdcf8b04b4e66f71faf5fd0b7ea6c6616c86ae2015f0fd5d6d730418e8; fixture_sha256=06f8a5807d1130b7a91a700b2074192e6dfed0933a071ce16642b27aa050360d; output_sha256=34a08a9de7c2660c327965458e3411f495f0710a53b4e5ac8b3fb9cdb1423065; snapshot_sha256=3813549542ec815eecb28561137e3da9f7264ee4e33113b6577940d44ab237b6
- Behavior: Delivered local, Docker, and Helm assets with required topology and documentation, but without the additional executable local startup script and deployment matrix present in the with_skill lane.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
