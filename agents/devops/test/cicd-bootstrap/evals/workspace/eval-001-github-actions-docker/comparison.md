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
