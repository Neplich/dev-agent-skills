# Eval Result: eval-001-github-actions-docker

## Evaluation Target

- Agent: `devops`
- Skill: `cicd-bootstrap`
- Eval: `eval-001-github-actions-docker`
- Test case: github-actions-docker
- Workspace: `workspace/eval-001-github-actions-docker`
- Latest result: PASS - 2026-07-26 fresh paired validation completed; with_skill and fresh without_skill both satisfied 5/5 assertions.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: confirmed repo-wide handoff, real package commands, Dockerfile, and staging Compose target
- Expected output: 生成 GitHub Actions workflows，包含 CI 和 staging 部署

## Assertions

- PASS `github_workflows_ci_yml`: with_skill 生成 `.github/workflows/ci.yml`。
- PASS `ci_yml_lint_test_build`: CI 包含 lint、test、build。
- PASS `github_workflows_deploy_staging_yml`: 生成 `.github/workflows/deploy-staging.yml`。
- PASS `deploy_staging_yml_push_to_main`: staging workflow 由 push 到 main 触发。
- PASS `deploy_secrets_md_secrets`: 生成 `deploy/SECRETS.md` 并列出 secret 名称。

## With Skill

- 除满足 5 项断言外，还加入最小权限、并发控制、部署前验证与不可变 SHA 镜像引用。
- workflow YAML 解析通过。

## Without Skill / Baseline

- 2026-07-26 使用同一 prompt 和 fixture 重新生成 fresh baseline，未读取或应用 cicd-bootstrap skill、Agent README、历史 comparison 或旧 baseline。
- baseline 同样满足 5/5 assertions，但权限、并发和部署安全门禁较简略。

## Failures

- 无 assertion failure。
- 未真实触发 GitHub Actions，环境中没有 `actionlint`；当前 assertions 对 skill 增益的区分度有限。

## Next Steps

- 保留当前 CI/CD 产物断言，并在后续单独评估是否需要增强安全门禁断言。

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics were generated only in an ignored scratch workspace and are not committed.
