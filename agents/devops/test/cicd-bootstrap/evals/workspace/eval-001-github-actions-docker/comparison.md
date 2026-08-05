# Eval Result: eval-001-github-actions-docker

## Evaluation Target

- Agent: `devops`
- Skill: `cicd-bootstrap`
- Eval: `eval-001-github-actions-docker`
- Test case: github-actions-docker
- Workspace: `workspace/eval-001-github-actions-docker`
- Latest result: PASS - 2026-07-26 fresh paired validation completed; with_skill and fresh without_skill both satisfied 5/5 assertions.
- Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: confirmed repo-wide handoff, lockfile, lintable source/test, flat ESLint config, real package commands, Dockerfile, and staging Compose target
- Expected output: 生成 GitHub Actions workflows，包含 CI 和 staging 部署

## Assertions

- PASS `github_workflows_ci_yml`: with_skill 生成 `.github/workflows/ci.yml`。
- PASS `ci_yml_lint_test_build`: CI 包含 lint、test、build。
- PASS `github_workflows_deploy_staging_yml`: 生成 `.github/workflows/deploy-staging.yml`。
- PASS `deploy_staging_yml_push_to_main`: staging workflow 由 push 到 main 触发。
- PASS `deploy_secrets_md_secrets`: 生成 `deploy/SECRETS.md` 并列出 secret 名称。

## With Skill

- 除满足 5 项断言外，还加入最小权限、并发控制、部署前 lint/test/build、显式 registry 登录、远端 pull/up 与失败即停。
- 2026-07-26 将 ESLint 精确更新到 10.8.0 并重建 lockfile 后，重新执行最终 fresh paired validation；`npm ci`、lint、1/1 test、build、high-severity audit、Docker build 与两份 workflow YAML 解析均通过。

## Without Skill / Baseline

- 2026-07-26 使用更新后的同一 prompt 和 fixture 重新生成 fresh baseline，未读取或应用 cicd-bootstrap skill、Agent README、历史 comparison 或旧 baseline。
- baseline 同样满足 5/5 assertions，且相同 npm、0-vulnerability audit、Docker 与 YAML 验证均通过；但缺少 staging 前置 lint/test、远端 registry 登录、显式 pull、最小权限、并发保护与失败即停。

## Failures

- 无 assertion failure。
- 未真实触发 GitHub Actions、GHCR 或 staging 部署；第三方 Actions 使用版本 tag 而非 commit SHA。
- 本机 Node 24 与 fixture 的 Node 22 engine 产生非失败 warning，Docker build 已使用 Node 22 验证通过。

## Next Steps

- 保留当前 CI/CD 产物断言，并在后续单独评估是否需要增强安全门禁断言。

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics were generated only in an ignored scratch workspace and are not committed.
