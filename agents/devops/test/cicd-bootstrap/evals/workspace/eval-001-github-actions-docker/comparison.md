# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `cicd-bootstrap`
- Eval: `eval-001-github-actions-docker`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `343bcb839e30c78715e11895db5ff7bd71039ec73fe31429c1bbda5b9e3e2a90` from `agents/devops/test/cicd-bootstrap/evals/workspace/eval-001-github-actions-docker`.
- Fixture SHA-256: `343bcb839e30c78715e11895db5ff7bd71039ec73fe31429c1bbda5b9e3e2a90`
- Prompt SHA-256: `218d78b7a8ea97a45d92074ef7fdba8d569a39aa87d9b7e2b17fd38ac1491e6e`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `86f7228d11d9f7ad3ec145d83be1c28f8a4bb93afea61016f55ed2860069bc68`
- Skill overlay SHA-256: `d87d7023cb1778acf3685e0e616785cca86656081ff2fa7f0e1ff03553b77b80`
- Judge schema SHA-256: `416d97c852ae3d12b00631149dd08640442fd75a13414eab07000c384c3a2d5f`
- Eval definition SHA-256: `e302fa46977944ed026b10f7f1ded4b3717a6c85f19be1f78da9c42d4b0c0b8d`
- Metadata SHA-256: `9e986f54be95fd6454e99ce66dc884d4d84134a4b07d49e0942d5d6169d042bf`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_repo_native_ci` | PASS | with_skill 的 locked delivery_snapshot 包含 .github/workflows/ci.yml；触发 pull_request，使用 Node.js 22.x、npm ci，并按 lint、test、build 顺序执行仓库命令。 |
| `creates_staging_deployment_workflow` | PASS | with_skill 的 deploy-staging.yml 仅配置 main 分支 push 触发，使用 deploy/docker/docker-compose.staging.yml、ghcr.io/example/acme-web，并通过 APP_IMAGE_TAG 传递镜像标签。 |
| `documents_required_secrets` | PASS | with_skill 的 deploy/SECRETS.md 列出 REGISTRY_USERNAME、REGISTRY_TOKEN、STAGING_HOST、STAGING_USER 和 STAGING_SSH_KEY，且明确不提交凭据值。 |
| `does_not_execute_delivery` | PASS | with_skill 的 git_evidence 显示无提交、无推送、无新 commit；delivery_snapshot 仅包含配置文件，最终说明也明确未执行镜像发布或实际部署。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=218d78b7a8ea97a45d92074ef7fdba8d569a39aa87d9b7e2b17fd38ac1491e6e; fixture_sha256=343bcb839e30c78715e11895db5ff7bd71039ec73fe31429c1bbda5b9e3e2a90; output_sha256=0e7869657662bd77d66c73e55da6f22ff39370d7030939d75c1b31fb17072f40; snapshot_sha256=81558261c7eee1dedc265ff4a7c8b5033d4869941588a7fedbbf03715fd9245c
- Behavior: 生成了 CI、staging 部署和 secrets 文档配置，未执行交付。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=218d78b7a8ea97a45d92074ef7fdba8d569a39aa87d9b7e2b17fd38ac1491e6e; fixture_sha256=343bcb839e30c78715e11895db5ff7bd71039ec73fe31429c1bbda5b9e3e2a90; output_sha256=d659636991f979ac89adbcebe9cd1b1ea29ef6b83d6b3d8e1ad388920ac9ec1b; snapshot_sha256=62ede0ad9dce0e15691bd5034ab4856b3867208fd60e29671bdd07912ac78ada
- Behavior: 同样生成了配置并未执行实际部署；其部署工作流使用了更完整的远程 Compose 目录变量。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
