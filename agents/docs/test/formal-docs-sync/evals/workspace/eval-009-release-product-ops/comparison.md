# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-009-release-product-ops`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `88db6a4117456e7d2f0e14115ea2a173ee0022fedba47576986e4b24262edb75` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-009-release-product-ops`.
- Identity schema: `2`
- target_skill_sha256: `a3e1263ac8acb74f106913f935cefb0ebe0f7f059ccc011cd16715592fd0163d`
- eval_definition_sha256: `c9bcafbf3ecc8c0e0ac28908b463b075e9d1371a95444953a8afc3d41757e192`
- metadata_sha256: `d04b92e9a3754ad51ae5d707b3601a2084dc53a6e309122269ca881bc88a10ef`
- fixture_sha256: `88db6a4117456e7d2f0e14115ea2a173ee0022fedba47576986e4b24262edb75`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `56b98af2f6fc5a04535db999157836236eb69830528cbecc99ca00f23b4d8d9e`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `8feaf10d86a83aace4d8ae6456c2cfec394b2d1dd27b83a16d97b82d9a82c1f2`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `b6ae3621879be63fa5b02212924eed11dd010ad027f0308f85d7666d26a57421`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `limits_release_to_affected_product_ops` | PASS | with_skill 明确列出 product 与 ops 两个 affected_docs，并排除 API、database、design 及无关页面；change-map 映射保持不变。 |
| `reconciles_confirmed_version_facts` | PASS | with_skill 正确核对代码中的 25、配置中的 registry.example/ai-hub:v1.5.0 与 25，以及测试证据；未采纳旧值或 v1.5.1 计划。 |
| `preserves_release_notes_surfaces` | PASS | with_skill 明确排除 Release Notes surfaces，且 git_status/git_diff 均为空，未发生相关变更。 |
| `keeps_release_pages_unverified` | NOT_EXERCISED | with_skill 未执行页面同步；当前 delivery_snapshot 为空，因此无法验证同步后页面是否保持 unverified。 |
| `runs_release_host_checks_and_handoffs` | NOT_EXERCISED | with_skill 记录 host_checks 为 not_run、audit_handoff 为 blocked，未运行 npm run test:docs 或完成 docs-audit handoff。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8feaf10d86a83aace4d8ae6456c2cfec394b2d1dd27b83a16d97b82d9a82c1f2; fixture_sha256=88db6a4117456e7d2f0e14115ea2a173ee0022fedba47576986e4b24262edb75; output_sha256=f4cb4732a24b121c456c9031ce6e2bb640dbfb726769a71d24a18b2b744ec1cb; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确核对范围与版本事实，保持无变更并在其判定的发布门禁处阻塞；未执行后续交付步骤。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8feaf10d86a83aace4d8ae6456c2cfec394b2d1dd27b83a16d97b82d9a82c1f2; fixture_sha256=88db6a4117456e7d2f0e14115ea2a173ee0022fedba47576986e4b24262edb75; output_sha256=fa312623e7c70861f09b2dd2c64e3eeac0a5e15bdb9c953fe08e777ebe3e47f6; snapshot_sha256=9b8715c484d0b2aaaff5224f4798d17b466b09ec2f1a0a67fe6c7fe41b19ec5f
- Behavior: 更新了两个受影响页面并运行测试，但错误地将页面 last_verified_version 写为 v1.5.0，且把不可解析的 abc1500 当作测试依据。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 补齐可验证的发布入口/版本锚与必要运行时证据后，更新两页并保持 last_verified_version: unverified。
- Next: 在 docs/site/ 执行 npm run test:docs，并将完整 affected set、target_release_version: v1.5.0 及确认来源 handoff 至 docs-agent:docs-audit。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
