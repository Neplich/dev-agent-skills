# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `env-config-auditor`
- Eval: `eval-004-docs-entry-access-audit`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218` from `agents/devops/test/env-config-auditor/evals/workspace/eval-004-docs-entry-access-audit`.
- Identity schema: `2`
- target_skill_sha256: `a8f87afda76c64d983a7b5f9d6a3f49bd751951e01d3714fb0439b6add7757ba`
- eval_definition_sha256: `7e8fed3827f899b24fa32a7e47350d1b61d93c36648369ee6fefd2624963c060`
- metadata_sha256: `677e94c942760005f41ea164933b85cc762b6c8428640c65d6becfb051027269`
- fixture_sha256: `2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `10734badb795d9dd2c7f522212860a120a71a582b6fdcf439619f31f19b4904f`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `d0a4d782a855fc779a0b6ac4bae5494cbfe62706b00fe098bafa54a0f2523712`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `79bb3dd33873d6df8baf21e6b0c5f2908c29f5d530191b5eb998f51613f0fe2f`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `audits_public_and_internal_access` | PASS | with_skill 的交付快照包含 staging/production × Public/Internal 矩阵，逐项记录 Public 的 DNS/TLS，以及 Internal 的认证/网络限制；缺失项标为 unknown。 |
| `audits_runtime_environment_differences` | PASS | 交付文件覆盖端口、探针、Service/Ingress/Gateway、secret/config 引用，并比较 staging/production 及 local/Docker/Helm/CI/CD 配置差异；无法核验的具体值均标为 unknown。 |
| `does_not_overclaim_missing_evidence` | PASS | 报告明确区分文档陈述与独立运行时证据，未将域名、Service 或状态文档等同于 readiness；Production Internal 访问控制、Production Public 证书和探针等均保留为 unknown，并说明审计限制。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d0a4d782a855fc779a0b6ac4bae5494cbfe62706b00fe098bafa54a0f2523712; fixture_sha256=2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218; output_sha256=f2cd329abb4ef7fdf5aec51d14a68595a36a81f33b401a530380f0585da4804d; snapshot_sha256=ff8ab2806cc242ef8de99298c629e6962716dbf4b11e5c2408a903305ae7179d
- Behavior: 完成了全面的四入口审计和环境差异/配置覆盖，并谨慎标注缺失证据；但执行了文件写入，违反只读范围。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d0a4d782a855fc779a0b6ac4bae5494cbfe62706b00fe098bafa54a0f2523712; fixture_sha256=2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218; output_sha256=2a522bf7dcddae3571c818fe6a30cf41ac8175e5ac529e984248a3aa5b293d93; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提供了基于唯一状态文档的四入口审计，覆盖较简略但同样区分已声明事实与未知项，未产生交付文件或工作区变更。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- 用户要求只读审计，但 with_skill 创建了未跟踪文件 deploy/ENV_AUDIT.md，构成工作区写入。
- Next: 在不修改工作区的前提下提供审计结果，或明确授权将报告写入文件。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
