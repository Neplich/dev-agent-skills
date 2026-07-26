# PM Handoff Packet

```yaml
request_type: deployment
change_tier: standard
feature_path: N/A
feature: N/A
parent_feature: N/A
feature_level: N/A
feature_path_evidence: []
source_documents:
  - package.json
  - package-lock.json
  - eslint.config.js
  - src/server.js
  - test/server.test.js
  - deploy/docker/Dockerfile
  - deploy/docker/docker-compose.staging.yml
scope_decision:
  summary: 为现有 GitHub + Docker 项目新增 PR CI 和 main 分支 staging 自动部署配置。
  expectation_changed: false
  non_goals:
    - production 部署
    - 实际构建或发布镜像
    - 修改应用代码
downstream_owner: DevOps
required_output:
  - .github/workflows/ci.yml
  - .github/workflows/deploy-staging.yml
  - deploy/SECRETS.md
blockers_risks:
  - workflow 只能引用 secrets 名称，不得保存真实凭据
```

项目使用 Node.js 22，现有 source、test 与 flat ESLint 配置可直接执行。CI 必须先运行 `npm ci`，再调用 `npm run lint`、`npm test` 和 `npm run build`。staging 使用 Docker Compose，镜像为 `ghcr.io/example/acme-web:${APP_IMAGE_TAG}`，main push 触发；只生成配置，不执行部署。

需要记录的 GitHub secrets 名称为 `REGISTRY_USERNAME`、`REGISTRY_TOKEN`、`STAGING_HOST`、`STAGING_USER` 和 `STAGING_SSH_KEY`。
