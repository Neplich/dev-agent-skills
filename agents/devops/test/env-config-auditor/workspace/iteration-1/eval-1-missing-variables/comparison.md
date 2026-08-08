# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `env-config-auditor`
- Eval: `eval-001-missing-variables`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `4e6c22cd2abded0cbcf31007050064d16e8cb14c8ccdda445c9587853833ba57` from `agents/devops/test/env-config-auditor/workspace/iteration-1/eval-1-missing-variables`.
- Fixture SHA-256: `4e6c22cd2abded0cbcf31007050064d16e8cb14c8ccdda445c9587853833ba57`
- Prompt SHA-256: `75e60dc10eb3fef811146cbd4dcc0df487be3bd537e40cef0747bad2cca106cf`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a23a5206e5734d346e9cc05988abcd19e92dc09bd52f243173dd300d409a14ca`
- Skill overlay SHA-256: `cf962faf729c051cb7dfd2e1a6a7c8c9a1b7f9b67501cbf18f492cb32a84adc7`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `5217a2bb49f0b8e0ba081e4029f81b07efd6b07af9fb34ce9773ecbde5d00a5b`
- Metadata SHA-256: `f2d1d6d11daf93046843d6cf276fdc2c30cd77fd3602aa38ebdb9fcc3d6c1a85`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_durable_config_audit` | PASS | with_skill created deploy/ENV_AUDIT.md containing missing variables, a coverage matrix, security issues, recommendations, and source-line evidence. |
| `compares_code_deploy_and_cicd` | PASS | The report compares src/server.ts, local, Docker, CI/CD, and explicitly records Helm/Kubernetes as absent/unknown; it correctly identifies Docker/CI gaps for API_KEY and REDIS_URL and CI-only STRIPE_SECRET_KEY. |
| `keeps_secrets_and_unknowns_honest` | PASS | No real secret values are disclosed; the report identifies the local example key as non-production, marks Helm and runtime/deployment evidence unknown, and does not claim production readiness. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=75e60dc10eb3fef811146cbd4dcc0df487be3bd537e40cef0747bad2cca106cf; fixture_sha256=4e6c22cd2abded0cbcf31007050064d16e8cb14c8ccdda445c9587853833ba57; output_sha256=f16b96ba913745c2fe9b62ea3df63ea114179de9e7b1f0cf82d02f406c5c3485; snapshot_sha256=7ef41d8245979e43994d26682e7e60f69ccf4104b97efa1f08c0dc87ccecf104
- Behavior: Created the required repository audit with accurate coverage, security cautions, source evidence, and explicit unknowns for absent Helm/runtime configuration.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=75e60dc10eb3fef811146cbd4dcc0df487be3bd537e40cef0747bad2cca106cf; fixture_sha256=4e6c22cd2abded0cbcf31007050064d16e8cb14c8ccdda445c9587853833ba57; output_sha256=4ac2fadbce35e4922af8a1dada4e3a601c3ffceabf0df655fbe79878c66eb897; snapshot_sha256=040488ccdf25cfb0b300f47329efc230608d03e041e7e58fc11deb9a678418a8
- Behavior: Created a report at the wrong path and omitted the required Helm comparison, though its variable-gap findings were largely correct.
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
- Skill: `env-config-auditor`
- Eval: `eval-001-missing-variables`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `4e6c22cd2abded0cbcf31007050064d16e8cb14c8ccdda445c9587853833ba57` from `agents/devops/test/env-config-auditor/workspace/iteration-1/eval-1-missing-variables`.
- Fixture SHA-256: `4e6c22cd2abded0cbcf31007050064d16e8cb14c8ccdda445c9587853833ba57`
- Prompt SHA-256: `75e60dc10eb3fef811146cbd4dcc0df487be3bd537e40cef0747bad2cca106cf`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `672542b4c547ee15b5007c81b95d14b5fa65c727675122bbb5a233f553fe8ae7`
- Skill overlay SHA-256: `de10ec2dd3547ee5b7a57196d7f9e6584e3ffbd9e717a8e1c8e3b5506cd96520`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `5217a2bb49f0b8e0ba081e4029f81b07efd6b07af9fb34ce9773ecbde5d00a5b`
- Metadata SHA-256: `f2d1d6d11daf93046843d6cf276fdc2c30cd77fd3602aa38ebdb9fcc3d6c1a85`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_durable_config_audit` | PASS | with_skill creates deploy/ENV_AUDIT.md containing missing variables, coverage matrices, security risks, recommendations, and cited repository evidence. |
| `compares_code_deploy_and_cicd` | PASS | The report compares source, local, Docker, CI/CD, and Helm/Kubernetes; correctly identifies REDIS_URL and API_KEY missing from Docker/CI/CD and STRIPE_SECRET_KEY present only in CI/CD. |
| `keeps_secrets_and_unknowns_honest` | PASS | No real secret values are disclosed. Helm/Kubernetes is explicitly marked unknown/not represented, and incomplete coverage is not described as production-ready. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=75e60dc10eb3fef811146cbd4dcc0df487be3bd537e40cef0747bad2cca106cf; fixture_sha256=4e6c22cd2abded0cbcf31007050064d16e8cb14c8ccdda445c9587853833ba57; output_sha256=fe4637a83c155d562c9258f667add04d84205eb354f8b6df2c7dd38b6bb4db5c; snapshot_sha256=e85727ee596608314ad5028693965f0fbed0e26e62d494c6dd2e7261752afd00
- Behavior: Produced the required deploy/ENV_AUDIT.md with complete coverage findings, explicit unknowns, security considerations, evidence sources, and recommendations.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=75e60dc10eb3fef811146cbd4dcc0df487be3bd537e40cef0747bad2cca106cf; fixture_sha256=4e6c22cd2abded0cbcf31007050064d16e8cb14c8ccdda445c9587853833ba57; output_sha256=97354526ff81751f405d5fcfe92cb746f7f9a5d088082da982f6078aee13408f; snapshot_sha256=c4cf0d2d83b4056733b6dce7a5da19f2f9e1f248209e69e0e715a0cf21b55c3a
- Behavior: Produced a report under docs/ with mostly accurate variable findings, but not at the required deploy/ENV_AUDIT.md path and without explicit Helm/unknown-runtime treatment.
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
- Skill: `env-config-auditor`
- Eval: `eval-001-missing-variables`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `4e6c22cd2abded0cbcf31007050064d16e8cb14c8ccdda445c9587853833ba57` from `agents/devops/test/env-config-auditor/workspace/iteration-1/eval-1-missing-variables`.
- Fixture SHA-256: `4e6c22cd2abded0cbcf31007050064d16e8cb14c8ccdda445c9587853833ba57`
- Prompt SHA-256: `75e60dc10eb3fef811146cbd4dcc0df487be3bd537e40cef0747bad2cca106cf`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `30d88474014fd1654b2afdad809dd429177b5ede44673678193420a680992fce`
- Skill overlay SHA-256: `4a296e51a1a55fbed13be81dcfbf208640c3c058625400ff291752ea55bee7b8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `5217a2bb49f0b8e0ba081e4029f81b07efd6b07af9fb34ce9773ecbde5d00a5b`
- Metadata SHA-256: `f2d1d6d11daf93046843d6cf276fdc2c30cd77fd3602aa38ebdb9fcc3d6c1a85`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_durable_config_audit` | PASS | with_skill 生成 deploy/ENV_AUDIT.md，包含缺失变量、覆盖矩阵、安全问题、建议及文件/行号证据来源。 |
| `compares_code_deploy_and_cicd` | PASS | 报告核对了代码、local、Docker 与 CI/CD，记录 Helm 配置未发现，并准确指出 Docker/CI/CD 缺少 REDIS_URL 和 API_KEY，STRIPE_SECRET_KEY 仅在 CI/CD 中声明。 |
| `keeps_secrets_and_unknowns_honest` | PASS | 报告未写入真实 secret 值；明确记录未发现 Helm 及实际部署运行时配置，标为 unknown，且未将部分覆盖描述为生产就绪。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=75e60dc10eb3fef811146cbd4dcc0df487be3bd537e40cef0747bad2cca106cf; fixture_sha256=4e6c22cd2abded0cbcf31007050064d16e8cb14c8ccdda445c9587853833ba57; output_sha256=a2bb5f586a1b3e209d2139357e5f29e11f988d611be81efee27abc1ce0cd354a; snapshot_sha256=1fed315b7c794a1284cf72c3c4be782fbdd78f957f8e58cf6a4dfd2615412aac
- Behavior: 生成 deploy/ENV_AUDIT.md，完成变量覆盖、安全与未知配置审计，并提供可复查证据和建议。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=75e60dc10eb3fef811146cbd4dcc0df487be3bd537e40cef0747bad2cca106cf; fixture_sha256=4e6c22cd2abded0cbcf31007050064d16e8cb14c8ccdda445c9587853833ba57; output_sha256=8d24016436033d499f53b7339ae9fd21140679a807c291de65f2f703abcf3c2b; snapshot_sha256=2668c0fc02ae47ed1608ff3f4337383c5a74a16ef31f53e74633120166bddb32
- Behavior: 生成了仓库根目录 ENV_CONFIG_AUDIT.md，覆盖主要变量缺失情况，但路径和报告名称不符合断言要求，且未明确记录 Helm 未知状态。
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

# Eval Result: eval-001-missing-variables

## Evaluation Target

- Agent: `devops`
- Skill: `env-config-auditor`
- Eval: `eval-001-missing-variables`
- Test case: `missing-variables`
- Workspace: `agents/devops/test/env-config-auditor/workspace/iteration-1/eval-1-missing-variables`

## Latest Result

- Fresh run: `2026-08-07`（issue #238 严格隔离重跑）
- Model: `gpt-5.6-luna`，`model_reasoning_effort=medium`
- Isolation: baseline 使用随机顶层 root；完成后仅保存在内存快照并删除 root，随后才创建 with_skill root；with_skill root 删除后才创建独立 judge root。两条 lane 的原始 prompt、fixture snapshot、`HOME` 与 `CODEX_HOME` 值相同。
- Judge: 独立 fresh `codex exec`，读取实际产物、final、status 与工具轨迹，对照当前 assertions 判定；不采信 lane 自评。
- Behavior result: PASS
- Coverage result: FULL
- Without-skill comparison: FAIL（仅作对照，不参与 durable Overall 组合）

Overall result: PASS

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Eval definition: `agents/devops/test/env-config-auditor/evals/evals.json`
- Metadata: `agents/devops/test/env-config-auditor/workspace/iteration-1/eval-1-missing-variables/eval_metadata.json`
- Expected output: 生成 durable 审计报告，指出 deploy 和 CI/CD 配置中缺失的变量
- Fixture: metadata 未声明 `fixture_context`；本轮复制 workspace 中除 comparison、metadata、README 和声明输出外的纯净 fixture 文件。

## Assertion Results

| Assertion | with_skill | without_skill | Evidence |
| --- | --- | --- | --- |
| `deploy_env_audit_md_docs_devops_feature_path_env_audit_md` | PASS | FAIL | with_skill 创建了 deploy/ENV_AUDIT.md；without_skill 未创建耐久审计报告文件。 |
| `missing_variables` | PASS | FAIL | with_skill 报告包含 ## Missing Variables 章节并列出 API_KEY、REDIS_URL 等缺失项；without_skill 仅输出摘要，没有该章节。 |
| `api_key_stripe_secret_key_deploy_ci_cd` | PASS | PASS | with_skill 明确指出 API_KEY 在 CI/CD 缺失；without_skill 也明确指出 CI 缺少 API_KEY。 |
| `recommendations` | PASS | FAIL | with_skill 报告包含 ## Recommendations 章节；without_skill 未生成报告或 Recommendations 章节。 |

## With-Skill Behavior

- with_skill 的四项断言均满足且全部可评估，因此 durable Overall 按 binding_result_model 为 PASS；without_skill 仅作对照，基线缺少耐久报告并不改变 durable Overall。
- Workspace changes: added: `deploy/ENV_AUDIT.md`。

## Fresh Without-Skill Baseline

- baseline 在本轮重新生成，没有复用历史 baseline，也没有读取 target skill、with_skill 产物或旧 comparison。
- Workspace changes: 无文件变更。
- assertion 结果见上表；baseline 只用于比较 skill 增益，不作为 durable Overall 的独立机器门禁。

## Failures and Coverage Gaps

- with_skill 无 assertion failure。
- 所有当前 assertions 均已实际覆盖。
- 无模型、认证、runner 或外部服务 blocker。

## Historical Result (Old Contract)

- 旧结论为 PARTIAL，原因是没有 fresh without_skill baseline；issue #234 后进一步标为 BLOCKED 等待重跑。
- 该历史结论适用旧 eval 契约；本文件顶部的 2026-08-07 fresh 结果已取代它作为 latest durable 结论。

## Next Steps

- 保留当前回归用例；后续 skill、fixture 或断言变化时继续执行同等严格的 fresh paired run。

## Runtime Artifact Policy

- 两条 lane、工具轨迹、状态、文件快照、judge verdict 与隔离事件只保存在 `tmp/eval-runs/issue-238-devops-strict-20260806/`，不提交 git。
- durable 结果只保留本 `comparison.md`。
