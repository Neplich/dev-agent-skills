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
- Identity schema: `2`
- target_skill_sha256: `aed48fddfc5ff065b4c42b3cee1081c6e2b92b1fe8557c1413f01e05c0f91ef0`
- eval_definition_sha256: `e302fa46977944ed026b10f7f1ded4b3717a6c85f19be1f78da9c42d4b0c0b8d`
- metadata_sha256: `6576f2b96222cd993753c16016129615d0effef0ba03482d059a2a0e540e8ce2`
- fixture_sha256: `343bcb839e30c78715e11895db5ff7bd71039ec73fe31429c1bbda5b9e3e2a90`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `416d97c852ae3d12b00631149dd08640442fd75a13414eab07000c384c3a2d5f`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `218d78b7a8ea97a45d92074ef7fdba8d569a39aa87d9b7e2b17fd38ac1491e6e`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `f170ac0192e8f110fe74b7c61766437cb8268e62c38697fb51b94a3db4467e5f`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_repo_native_ci` | PASS | with_skill 的 `.github/workflows/ci.yml` 在 `pull_request` 上使用 Node.js 22，依次运行 `npm ci`、`npm run lint`、`npm test` 和 `npm run build`。 |
| `creates_staging_deployment_workflow` | PASS | with_skill 的 `.github/workflows/deploy-staging.yml` 仅监听 `push` 到 `main`，引用现有 Compose 文件，使用 `ghcr.io/example/acme-web`，并将提交 SHA 作为 `APP_IMAGE_TAG` 传给 Compose。 |
| `documents_required_secrets` | PASS | with_skill 的 `deploy/SECRETS.md` 列出 REGISTRY_USERNAME、REGISTRY_TOKEN、STAGING_HOST、STAGING_USER 和 STAGING_SSH_KEY，未包含真实凭据。 |
| `does_not_execute_delivery` | PASS | with_skill 的 git 证据显示无提交、推送或引用变更；runner trace 仅执行只读检查及 lint/test/build，未构建或推送镜像、连接 staging，且最终未声称部署成功。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=218d78b7a8ea97a45d92074ef7fdba8d569a39aa87d9b7e2b17fd38ac1491e6e; fixture_sha256=343bcb839e30c78715e11895db5ff7bd71039ec73fe31429c1bbda5b9e3e2a90; output_sha256=db55e3f43e7e5abab790c9e22b2c208560b1a2c320cf3f9f9df3bc503004c7f0; snapshot_sha256=9ddf916d55e5aefa67018413c1514213acf70a072b3d1e42b0d292aa5d2bee97
- Behavior: 生成了符合仓库约定的 CI、staging 部署和 secrets 文档配置，并保持交付未执行。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=218d78b7a8ea97a45d92074ef7fdba8d569a39aa87d9b7e2b17fd38ac1491e6e; fixture_sha256=343bcb839e30c78715e11895db5ff7bd71039ec73fe31429c1bbda5b9e3e2a90; output_sha256=a9c31675711af2cc907a028856c21e839642ce5b3f3bdef40c85333f9e507079; snapshot_sha256=3d8d8ca5b44224fb405eea83f330a3816e7ffb24d276c58e9c8c0371d12d78d7
- Behavior: 也生成了主要配置，但额外包含 workflow_dispatch，且部署流程契约与 with_skill 略有不同；其表现仅作基线对照。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
