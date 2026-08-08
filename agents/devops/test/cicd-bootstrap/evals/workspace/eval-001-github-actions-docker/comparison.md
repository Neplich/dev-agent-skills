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
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
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
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_repo_native_ci` | PASS | with_skill 的 `.github/workflows/ci.yml` 在 pull_request 上使用 Node.js 22.x、`npm ci`，并依次运行 `npm run lint`、`npm test`、`npm run build`。 |
| `creates_staging_deployment_workflow` | PASS | with_skill 的部署工作流仅监听 main 的 push，使用 `ghcr.io/example/acme-web`、现有 `deploy/docker/docker-compose.staging.yml`，并在远端以 `APP_IMAGE_TAG` 传递提交 SHA。 |
| `documents_required_secrets` | PASS | with_skill 的 `deploy/SECRETS.md` 明确列出 REGISTRY_USERNAME、REGISTRY_TOKEN、STAGING_HOST、STAGING_USER、STAGING_SSH_KEY，并明确禁止将凭据写入仓库。 |
| `does_not_execute_delivery` | PASS | with_skill 的 git evidence 显示仅有未跟踪配置文件、无提交或推送；候选输出明确说明未发布镜像或实际部署。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=218d78b7a8ea97a45d92074ef7fdba8d569a39aa87d9b7e2b17fd38ac1491e6e; fixture_sha256=343bcb839e30c78715e11895db5ff7bd71039ec73fe31429c1bbda5b9e3e2a90; output_sha256=c0a1cfca7011fe48a3dc1e01b3736546797cdcce934c6c73271ba06a6e783d4b; snapshot_sha256=f200d754fde1176e26f8c702c3c76aa3023c99bb6568c23622089378caba17b5
- Behavior: 完整生成 CI、staging 部署和 secrets 文档配置，且未执行交付。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=218d78b7a8ea97a45d92074ef7fdba8d569a39aa87d9b7e2b17fd38ac1491e6e; fixture_sha256=343bcb839e30c78715e11895db5ff7bd71039ec73fe31429c1bbda5b9e3e2a90; output_sha256=db406890f532cba45610b6ef1c0d8b5c368b40ef2132e28b3324eeaef91fd4d9; snapshot_sha256=53e9c4aaf358644f0a7b26d76b6fd5866e12242ebac9787095bcbf64b067a262
- Behavior: 也生成了满足主要要求的配置并未执行部署；其 CI 额外监听 main push。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `e302fa46977944ed026b10f7f1ded4b3717a6c85f19be1f78da9c42d4b0c0b8d`
- Metadata SHA-256: `9e986f54be95fd6454e99ce66dc884d4d84134a4b07d49e0942d5d6169d042bf`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_repo_native_ci` | PASS | with_skill 的 delivery_snapshot 直接生成 .github/workflows/ci.yml，触发 pull_request，使用 Node.js 22.x 和 npm ci，随后按仓库脚本执行 lint、test、build。 |
| `creates_staging_deployment_workflow` | PASS | with_skill 的 deploy-staging.yml 仅监听 main 的 push，构建并推送 ghcr.io/example/acme-web:${{ github.sha }}，通过 docker-compose.staging.yml 使用 APP_IMAGE_TAG 部署。 |
| `documents_required_secrets` | PASS | with_skill 的 deploy/SECRETS.md 列出 REGISTRY_USERNAME、REGISTRY_TOKEN、STAGING_HOST、STAGING_USER、STAGING_SSH_KEY，并明确凭据不存入仓库；内容未包含真实凭据。 |
| `does_not_execute_delivery` | NOT_EXERCISED | git_evidence 证明没有提交、推送或引用变更，但锁定证据不足以独立证明整个过程中未构建、推送镜像或连接 staging。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=218d78b7a8ea97a45d92074ef7fdba8d569a39aa87d9b7e2b17fd38ac1491e6e; fixture_sha256=343bcb839e30c78715e11895db5ff7bd71039ec73fe31429c1bbda5b9e3e2a90; output_sha256=f8c24133a5d9abc6cab31052e08683d36a3eddf0473121ca22c7d5a20f54d677; snapshot_sha256=234ea74d7cdf5a1634491acd8c2914340cbc9c63df53dc161a0220c70d80d879
- Behavior: 生成了符合仓库命令、Docker staging 契约和 secrets 要求的配置；未发生可见的 Git 提交或推送。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=218d78b7a8ea97a45d92074ef7fdba8d569a39aa87d9b7e2b17fd38ac1491e6e; fixture_sha256=343bcb839e30c78715e11895db5ff7bd71039ec73fe31429c1bbda5b9e3e2a90; output_sha256=c858f5c15ff38558eb42e33e397e97252bcab82912042157b532a96947afda64; snapshot_sha256=23d491e40b3036235e5f405b4912d0adb37c1875fa201f907939d7bc6400309c
- Behavior: 生成了所需配置并保持仓库未提交，但其交付快照未复用 APP_IMAGE_TAG/Compose 契约的证据不如 with_skill 完整。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 如需完整覆盖 does_not_execute_delivery，应提供构建、镜像推送和 staging 连接未发生的运行时审计证据。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Skill overlay SHA-256: `89e6351b83062ce7859670a14e2ffbb2ebe9ea30f7da2a45f2991e383570b374`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `e302fa46977944ed026b10f7f1ded4b3717a6c85f19be1f78da9c42d4b0c0b8d`
- Metadata SHA-256: `9e986f54be95fd6454e99ce66dc884d4d84134a4b07d49e0942d5d6169d042bf`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_repo_native_ci` | PASS | with_skill 的 .github/workflows/ci.yml 在 pull_request 触发，使用 Node 22.x，按 npm ci、npm run lint、npm test、npm run build 顺序执行。 |
| `creates_staging_deployment_workflow` | PASS | with_skill 的 deploy-staging.yml 仅监听 main 的 push，使用现有 deploy/docker/docker-compose.staging.yml、ghcr.io/example/acme-web 和 APP_IMAGE_TAG=${{ github.sha }}。 |
| `documents_required_secrets` | PASS | deploy/SECRETS.md 列出 REGISTRY_USERNAME、REGISTRY_TOKEN、STAGING_HOST、STAGING_USER、STAGING_SSH_KEY，并明确不保存凭据值。 |
| `does_not_execute_delivery` | PASS | git evidence 显示无提交、无分支或引用变化，仅有未跟踪配置文件；raw evidence 没有镜像发布或 staging 连接，输出也未声称部署成功。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=218d78b7a8ea97a45d92074ef7fdba8d569a39aa87d9b7e2b17fd38ac1491e6e; fixture_sha256=343bcb839e30c78715e11895db5ff7bd71039ec73fe31429c1bbda5b9e3e2a90; output_sha256=5c299a738692c63548296b9ece91eea65568c18077d468ab343fc3b799633086; snapshot_sha256=93aa6728ce1df90535a8d4087ebe593edbe4d4b65351e7ff2823649e4d879522
- Behavior: 生成了符合要求的 CI、staging 部署和 secrets 文档配置，复用 Compose、GHCR 命名和 APP_IMAGE_TAG，并未执行交付；部署采用 Docker over SSH。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=218d78b7a8ea97a45d92074ef7fdba8d569a39aa87d9b7e2b17fd38ac1491e6e; fixture_sha256=343bcb839e30c78715e11895db5ff7bd71039ec73fe31429c1bbda5b9e3e2a90; output_sha256=ca2e467bc7166559d272843fc894a4868b8bf024bb220eb663fc0fa00da6b8fc; snapshot_sha256=0e608abc8c6670a06a11c79f3686465a1e13ebc6b598e99a42d83c66d378bc55
- Behavior: 生成了符合要求的 CI、staging 部署和 secrets 文档配置，且未执行交付；部署采用 SCP/SSH。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `86f7228d11d9f7ad3ec145d83be1c28f8a4bb93afea61016f55ed2860069bc68`
- Skill overlay SHA-256: `89e6351b83062ce7859670a14e2ffbb2ebe9ea30f7da2a45f2991e383570b374`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `e302fa46977944ed026b10f7f1ded4b3717a6c85f19be1f78da9c42d4b0c0b8d`
- Metadata SHA-256: `9e986f54be95fd6454e99ce66dc884d4d84134a4b07d49e0942d5d6169d042bf`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_repo_native_ci` | PASS | with_skill snapshot shows .github/workflows/ci.yml triggered by pull_request, setup-node 22.x, then npm ci, npm run lint, npm test, and npm run build in order. |
| `creates_staging_deployment_workflow` | PASS | with_skill snapshot shows deploy-staging.yml triggered only by push to main, uses the existing deploy/docker/docker-compose.staging.yml, image ghcr.io/example/acme-web, and APP_IMAGE_TAG from the commit SHA. |
| `documents_required_secrets` | PASS | with_skill deploy/SECRETS.md lists REGISTRY_USERNAME, REGISTRY_TOKEN, STAGING_HOST, STAGING_USER, and STAGING_SSH_KEY, and explicitly says not to commit secret values. |
| `does_not_execute_delivery` | PASS | with_skill git evidence shows no commit, ref, branch, or remote changes; only untracked configuration files exist. The output states deployment was not executed, and raw evidence shows no delivery result. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=218d78b7a8ea97a45d92074ef7fdba8d569a39aa87d9b7e2b17fd38ac1491e6e; fixture_sha256=343bcb839e30c78715e11895db5ff7bd71039ec73fe31429c1bbda5b9e3e2a90; output_sha256=2359678a1b8bf962e25f9f2e0af44fe2487e7fcf177658c25e5186fe3af6a3f0; snapshot_sha256=d2d611e880ffdc838568b753e9a8804293f1a379fa7d59de9b8a32b2158c65b3
- Behavior: Generated CI, staging deployment, and secrets documentation consistent with the fixture contract; no deployment or repository delivery mutations were evidenced.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=218d78b7a8ea97a45d92074ef7fdba8d569a39aa87d9b7e2b17fd38ac1491e6e; fixture_sha256=343bcb839e30c78715e11895db5ff7bd71039ec73fe31429c1bbda5b9e3e2a90; output_sha256=9e189720ad3b880a207e0d151728642e7ec7bf01671628dd334bd4e8f96c00f6; snapshot_sha256=865491358070ae6f7379177f608059e353e0794f9d152ddbdc9c72e195433577
- Behavior: Generated the requested files and reported validation, with a different staging path/Compose handling; no repository delivery mutations were evidenced.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `93da25401932361eaed1febe9295456c36da28e8f63a6322a9b6632f928594dc`
- Skill overlay SHA-256: `83d8cb31e47efb4e01e1dd4e2d110f22b10e73a5e448fa73ece38b9d7a75b775`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `e302fa46977944ed026b10f7f1ded4b3717a6c85f19be1f78da9c42d4b0c0b8d`
- Metadata SHA-256: `9e986f54be95fd6454e99ce66dc884d4d84134a4b07d49e0942d5d6169d042bf`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_repo_native_ci` | PASS | with_skill delivery snapshot shows .github/workflows/ci.yml triggered by pull_request, setup-node Node 22, npm ci, then npm run lint, npm test, and npm run build; these match fixture/package.json and PM_HANDOFF.md. |
| `creates_staging_deployment_workflow` | PASS | with_skill snapshot shows deploy-staging.yml triggered only by push to main, builds/pushes ghcr.io/example/acme-web:${{ github.sha }}, and deploys the existing staging Compose configuration with APP_IMAGE_TAG set to the commit SHA. |
| `documents_required_secrets` | PASS | with_skill deploy/SECRETS.md lists REGISTRY_USERNAME, REGISTRY_TOKEN, STAGING_HOST, STAGING_USER, and STAGING_SSH_KEY, and explicitly states that secret values do not belong in the repository. |
| `does_not_execute_delivery` | PASS | with_skill git evidence shows unchanged HEAD/branch, no commits or ref changes, and only untracked configuration files; output states no actual deployment or image publication was performed. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=218d78b7a8ea97a45d92074ef7fdba8d569a39aa87d9b7e2b17fd38ac1491e6e; fixture_sha256=343bcb839e30c78715e11895db5ff7bd71039ec73fe31429c1bbda5b9e3e2a90; output_sha256=babafd243d6f46d45c851f662d3ec29d5b24c37517df45b7c8de7544f2fe4b68; snapshot_sha256=a2d1ef2ecb628d5bb2f520bc1aca6567442f269f0911afc96cf18528ffc5659c
- Behavior: Generated all requested configuration files with repository-aligned commands, main-only staging deployment, GHCR/Compose integration, named secrets, and no repository or deployment side effects.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=218d78b7a8ea97a45d92074ef7fdba8d569a39aa87d9b7e2b17fd38ac1491e6e; fixture_sha256=343bcb839e30c78715e11895db5ff7bd71039ec73fe31429c1bbda5b9e3e2a90; output_sha256=6b9c21bb613a28df1d8b06108b6267f9bc5d38d3ef89466b2f13bdc050ab01ee; snapshot_sha256=8a9926151d5515151733473973ae3f8c94886923c87b3eec9fc92656298284bf
- Behavior: Generated the requested CI, deployment, and secrets files and reported no deployment, but did not provide the same level of deployment verification detail.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e575c1d3a1c91f460942675e7572f24424d7186546327f9d3fb6028046c4eca9`
- Skill overlay SHA-256: `35e1addc81106457a31cc80acfe03c60ba6a9d5ae75c3411408e4bb92991c900`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `e302fa46977944ed026b10f7f1ded4b3717a6c85f19be1f78da9c42d4b0c0b8d`
- Metadata SHA-256: `9e986f54be95fd6454e99ce66dc884d4d84134a4b07d49e0942d5d6169d042bf`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_repo_native_ci` | PASS | with_skill 生成 .github/workflows/ci.yml，配置 pull_request、Node.js 22.x、npm ci，并按 lint、test、build 顺序执行仓库脚本。 |
| `creates_staging_deployment_workflow` | PASS | with_skill 生成 deploy-staging.yml，仅监听 main push，上传现有 Compose 文件，使用 ghcr.io/example/acme-web，并通过 .env 设置 APP_IMAGE_TAG。 |
| `documents_required_secrets` | PASS | with_skill 的 deploy/SECRETS.md 列出全部五个要求的 secret 名称，未包含真实凭据。 |
| `does_not_execute_delivery` | PASS | git evidence 显示未提交、未推送且 HEAD/分支未变化；候选仅报告本地质量检查，没有实际构建/推送镜像、连接 staging 或声称部署成功。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=218d78b7a8ea97a45d92074ef7fdba8d569a39aa87d9b7e2b17fd38ac1491e6e; fixture_sha256=343bcb839e30c78715e11895db5ff7bd71039ec73fe31429c1bbda5b9e3e2a90; output_sha256=8fd06c2b33ac0220208be174d4cd2704787db56973d778d36c418c2b62840614; snapshot_sha256=ac3ef34e03e4d3d18501b2c68a32b75f2d8c59c7ac88890e4a220743eff14168
- Behavior: 完整生成 PR CI、main 到 staging 的 Docker Compose 部署配置及 secrets 文档，并保持交付未执行。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=218d78b7a8ea97a45d92074ef7fdba8d569a39aa87d9b7e2b17fd38ac1491e6e; fixture_sha256=343bcb839e30c78715e11895db5ff7bd71039ec73fe31429c1bbda5b9e3e2a90; output_sha256=3d29e36a041044a0f3471b9585f921df0a6344d743bd181757bc2a3f9a198fb5; snapshot_sha256=d16f38f24081b25583dedffa59a8dcdfa73665bceac1cc0a0070754ab5d7039c
- Behavior: 生成了所需配置并保持仓库未提交；输出中的 deploy-staging 链接路径存在格式错误，但这不影响 with_skill 判定。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Migration Status

## Current Result

- Evidence status: **STALE**
- Migration status: **PENDING**
- Blocking reason: this eval has not yet been rerun under the Issue #246 scenario, lane-isolation, and fresh-judge contract.
Overall result: BLOCKED

## Historical Context (Superseded)

The complete pre-migration comparison follows unchanged. It is retained only as historical context and is not current release evidence.

---

# Eval Result: eval-001-github-actions-docker

## Evaluation Target

- Agent: `devops`
- Skill: `cicd-bootstrap`
- Eval: `eval-001-github-actions-docker`
- Test case: `github-actions-docker`
- Workspace: `agents/devops/test/cicd-bootstrap/evals/workspace/eval-001-github-actions-docker`

## Latest Result

- Fresh run: `2026-08-07`（issue #238 严格隔离重跑）
- Model: `gpt-5.6-luna`，`model_reasoning_effort=medium`
- Isolation: baseline 使用随机顶层 root；完成后仅保存在内存快照并删除 root，随后才创建 with_skill root；with_skill root 删除后才创建独立 judge root。两条 lane 的原始 prompt、fixture snapshot、`HOME` 与 `CODEX_HOME` 值相同。
- Judge: 独立 fresh `codex exec`，读取实际产物、final、status 与工具轨迹，对照当前 assertions 判定；不采信 lane 自评。
- Behavior result: PASS
- Coverage result: FULL
- Without-skill comparison: PASS（仅作对照，不参与 durable Overall 组合）

Overall result: PASS

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Eval definition: `agents/devops/test/cicd-bootstrap/evals/evals.json`
- Metadata: `agents/devops/test/cicd-bootstrap/evals/workspace/eval-001-github-actions-docker/eval_metadata.json`
- Expected output: 生成 GitHub Actions workflows，包含 CI 和 staging 部署
- Fixture: `PM_HANDOFF.md`, `package.json`, `package-lock.json`, `eslint.config.js`, `src/server.js`, `test/server.test.js`, `deploy/docker/Dockerfile`, `deploy/docker/docker-compose.staging.yml`

## Assertion Results

| Assertion | with_skill | without_skill | Evidence |
| --- | --- | --- | --- |
| `github_workflows_ci_yml` | PASS | PASS | 两条 lane 均实际生成 .github/workflows/ci.yml。 |
| `ci_yml_lint_test_build` | PASS | PASS | 两条 lane 的 ci.yml 均包含 npm run lint、npm test 和 npm run build 步骤。 |
| `github_workflows_deploy_staging_yml` | PASS | PASS | 两条 lane 均实际生成 .github/workflows/deploy-staging.yml。 |
| `deploy_staging_yml_push_to_main` | PASS | PASS | 两条 lane 的 deploy-staging.yml 均配置 on.push.branches.main。 |
| `deploy_secrets_md_secrets` | PASS | PASS | 两条 lane 均生成 deploy/SECRETS.md，并列出 REGISTRY_USERNAME、REGISTRY_TOKEN、STAGING_HOST、STAGING_USER、STAGING_SSH_KEY。 |

## With-Skill Behavior

- 独立核对 evaluation.json、fixture、两条 lane 的实际文件、final、status 与 tool-trace；with_skill 的全部断言均可评估且满足，因此 Coverage 为 FULL、durable Overall 为 PASS。without_skill 也满足全部断言。
- Workspace changes: added: `.github/workflows/ci.yml`, `.github/workflows/deploy-staging.yml`, `deploy/SECRETS.md`。

## Fresh Without-Skill Baseline

- baseline 在本轮重新生成，没有复用历史 baseline，也没有读取 target skill、with_skill 产物或旧 comparison。
- Workspace changes: added: `.github/workflows/ci.yml`, `.github/workflows/deploy-staging.yml`, `deploy/SECRETS.md`。
- assertion 结果见上表；baseline 只用于比较 skill 增益，不作为 durable Overall 的独立机器门禁。

## Failures and Coverage Gaps

- with_skill 无 assertion failure。
- 所有当前 assertions 均已实际覆盖。
- 无模型、认证、runner 或外部服务 blocker。

## Historical Result (Old Contract)

- 旧结论为 PASS（5/5）；issue #234 修复 eval 泄漏后，该结论被标为 BLOCKED 等待重跑。
- 该历史结论适用旧 eval 契约；本文件顶部的 2026-08-07 fresh 结果已取代它作为 latest durable 结论。

## Next Steps

- 保留当前回归用例；后续 skill、fixture 或断言变化时继续执行同等严格的 fresh paired run。

## Runtime Artifact Policy

- 两条 lane、工具轨迹、状态、文件快照、judge verdict 与隔离事件只保存在 `tmp/eval-runs/issue-238-devops-strict-20260806/`，不提交 git。
- durable 结果只保留本 `comparison.md`。
