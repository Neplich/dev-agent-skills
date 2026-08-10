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
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `86f7228d11d9f7ad3ec145d83be1c28f8a4bb93afea61016f55ed2860069bc68`
- Skill overlay SHA-256: `c8eba5ff7fa14d3a9d17d2f0e6e7ee710355737a3424af1c887580cc79ea33c4`
- Judge schema SHA-256: `416d97c852ae3d12b00631149dd08640442fd75a13414eab07000c384c3a2d5f`
- Eval definition SHA-256: `e302fa46977944ed026b10f7f1ded4b3717a6c85f19be1f78da9c42d4b0c0b8d`
- Metadata SHA-256: `9e986f54be95fd6454e99ce66dc884d4d84134a4b07d49e0942d5d6169d042bf`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_repo_native_ci` | PASS | with_skill 的 delivery_snapshot 显示 .github/workflows/ci.yml 在 pull_request 触发，使用 Node.js 22.x，依次运行 npm ci、npm run lint、npm test 和 npm run build。 |
| `creates_staging_deployment_workflow` | PASS | with_skill 的 deploy-staging.yml 仅配置 main 分支 push 触发，使用 deploy/docker/docker-compose.staging.yml、ghcr.io/example/acme-web，并将提交 SHA 作为 APP_IMAGE_TAG 传给 Compose。 |
| `documents_required_secrets` | PASS | with_skill 的 deploy/SECRETS.md 列出 REGISTRY_USERNAME、REGISTRY_TOKEN、STAGING_HOST、STAGING_USER 和 STAGING_SSH_KEY，并明确不写入秘密值。 |
| `does_not_execute_delivery` | PASS | git_evidence 显示无提交、推送或引用变化；runner_captured_trace 仅执行了本地质量检查和文件核对，没有 Docker push、SSH 或实际部署。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=218d78b7a8ea97a45d92074ef7fdba8d569a39aa87d9b7e2b17fd38ac1491e6e; fixture_sha256=343bcb839e30c78715e11895db5ff7bd71039ec73fe31429c1bbda5b9e3e2a90; output_sha256=a9dc719da6b33c9a1f87371ddfd5466639f887a91f97c72bae7bbb5a65b9a94b; snapshot_sha256=51898b4650093a77fe21134bfaf92602eb336f0e2ab704b396439bd853875213
- Behavior: 完整生成并验证了 PR CI、main 分支 staging 部署工作流及秘密名称文档，未执行交付。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=218d78b7a8ea97a45d92074ef7fdba8d569a39aa87d9b7e2b17fd38ac1491e6e; fixture_sha256=343bcb839e30c78715e11895db5ff7bd71039ec73fe31429c1bbda5b9e3e2a90; output_sha256=0ca73fc79b0b392e2198b2cc455c7a3eb9c01db89c4f68317d8dc69b6ba02030; snapshot_sha256=cbe0113584bb965a15d9268869625141abb389b7794667377c41e4fcb378b05d
- Behavior: 同样生成了三项配置并未执行交付；其 CI 增加了 main 分支限制，作为对比上下文。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
