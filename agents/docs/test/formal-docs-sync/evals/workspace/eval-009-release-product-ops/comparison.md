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
- target_skill_sha256: `314b02febc2ef94201a8e1bf1080c874c355a0e47e6ac9a01b931425f08bfbd7`
- eval_definition_sha256: `c9bcafbf3ecc8c0e0ac28908b463b075e9d1371a95444953a8afc3d41757e192`
- metadata_sha256: `d04b92e9a3754ad51ae5d707b3601a2084dc53a6e309122269ca881bc88a10ef`
- fixture_sha256: `88db6a4117456e7d2f0e14115ea2a173ee0022fedba47576986e4b24262edb75`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `56b98af2f6fc5a04535db999157836236eb69830528cbecc99ca00f23b4d8d9e`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `8feaf10d86a83aace4d8ae6456c2cfec394b2d1dd27b83a16d97b82d9a82c1f2`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `84e19c3e634cfde176d2ff20ba8e9d25a4838db3ed1deb5def94a8d0f1d2ddd9`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `limits_release_to_affected_product_ops` | FAIL | with_skill 提议了正确的两个页面及映射范围，但 delivery_snapshot 为空、git_status 为空，未实际同步。 |
| `reconciles_confirmed_version_facts` | FAIL | with_skill 正确列出 25、v1.5.0 和证据绑定，但未交付更新后的文件；其声称缺少正式证据与 fixture 中已提供的 handoff/evidence 相矛盾。 |
| `preserves_release_notes_surfaces` | PASS | delivery_snapshot 为空且 git_status 为空；输出明确将 Release Notes 列为排除项。 |
| `keeps_release_pages_unverified` | PASS | 未发生文件变更，原始 fixture 中 product 与 ops 页面仍为 last_verified_version: unverified。 |
| `runs_release_host_checks_and_handoffs` | FAIL | with_skill 明确报告 host_checks 未运行、audit_handoff 为 blocked，未记录真实 npm run test:docs 通过结果或完成 docs-agent:docs-audit handoff。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8feaf10d86a83aace4d8ae6456c2cfec394b2d1dd27b83a16d97b82d9a82c1f2; fixture_sha256=88db6a4117456e7d2f0e14115ea2a173ee0022fedba47576986e4b24262edb75; output_sha256=dfb0db33b645390e64c4a00ca62930732b6fb87d10c539fa830e3406a51fcd49; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了正确范围和版本事实，并避免了 Release Notes 变更，但因不受证据支持的前置门禁阻断，未完成文档同步、宿主检查和 handoff。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8feaf10d86a83aace4d8ae6456c2cfec394b2d1dd27b83a16d97b82d9a82c1f2; fixture_sha256=88db6a4117456e7d2f0e14115ea2a173ee0022fedba47576986e4b24262edb75; output_sha256=088d9cc7bc57991fbe90052f648b80571c4ea010a7c0a2a2e174678371f89f05; snapshot_sha256=b8c49129916021af6ae10e243fb213fba462e65c14b359e2cbb5e59ded5d38f0
- Behavior: 实际更新了目标页面和 change-map，且报告测试通过，但错误地将两个页面的 last_verified_version 写为 v1.5.0。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- 未交付两个受影响页面及 change-map 的实际更新。
- 未运行宿主检查或完成 pre-tag handoff。
- Next: 移除无依据的 changelog/release-process/audit context 阻断，更新两个目标页面及其 change-map。
- Next: 在 docs/site/ 执行 npm run test:docs 并记录 cwd、命令和退出状态，随后完成 docs-agent:docs-audit handoff。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
