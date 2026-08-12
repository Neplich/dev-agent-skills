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
- target_skill_sha256: `dd975083d3977d90b71b3396dff2498ef2b7e8d49c50fab50b5462a26f3248ee`
- eval_definition_sha256: `c9bcafbf3ecc8c0e0ac28908b463b075e9d1371a95444953a8afc3d41757e192`
- metadata_sha256: `d04b92e9a3754ad51ae5d707b3601a2084dc53a6e309122269ca881bc88a10ef`
- fixture_sha256: `88db6a4117456e7d2f0e14115ea2a173ee0022fedba47576986e4b24262edb75`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `56b98af2f6fc5a04535db999157836236eb69830528cbecc99ca00f23b4d8d9e`
- Identity migration: **MIGRATED_WITHOUT_MODEL_RERUN**
- Identity migration source commit: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Identity migration audit: `docs/engineer/repository-governance/eval-scenario-isolation/eval-identity-v2-migration-audit.json`
- Repository HEAD: `f2aa9b2c49be68550ec45538c221425607f428ce`
- Repository worktree state: **DIRTY**
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `limits_release_to_affected_product_ops` | PASS | 交付快照与 git diff 仅包含 product/dashboard-limits.md 和 ops/dashboard-runtime.md；change-map 保持既有两条映射，未扩展到 API、database、design 或其他页面。 |
| `reconciles_confirmed_version_facts` | PASS | 两页交付内容均写入 dashboard 上限 25 和 v1.5.0 runtime 镜像；原始 release evidence、代码、配置和测试均一致，未写入 v1.5.1 计划。 |
| `preserves_release_notes_surfaces` | PASS | 交付快照、git diff 和 workspace manifest 显示 Release Notes 页面、.meta/releases.json、navigation 及部署资产均未修改；输出明确排除 Release Notes。 |
| `keeps_release_pages_unverified` | PASS | product 与 ops 两个交付文件的原始内容均为 last_verified_version: unverified。 |
| `runs_release_host_checks_and_handoffs` | NOT_EXERCISED | runner trace 证明 npm run test:docs 在命令事件中以 exit 0 完成，候选输出记录 cwd、affected set、target_release_version 和 docs-agent:docs-audit handoff；但 handoff 明确 blocked pending docs-audit specialist availability，因此 pre-tag 阶段未能实际完成。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8feaf10d86a83aace4d8ae6456c2cfec394b2d1dd27b83a16d97b82d9a82c1f2; fixture_sha256=88db6a4117456e7d2f0e14115ea2a173ee0022fedba47576986e4b24262edb75; output_sha256=3bd35caea39c2fe0150761a62ed807d351f430c8a916f3df1d5e8c6b0ebd05c1; snapshot_sha256=acb0996c968a8620faea65c68cbad2c1a46267cf91f64952880e7e39cf77e13d
- Behavior: 正确完成受影响 product/ops 页面同步、版本事实核对、Release Notes 隔离和 unverified 保留；宿主检查通过，但审计 specialist 不可用使 pre-tag handoff 未完成。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8feaf10d86a83aace4d8ae6456c2cfec394b2d1dd27b83a16d97b82d9a82c1f2; fixture_sha256=88db6a4117456e7d2f0e14115ea2a173ee0022fedba47576986e4b24262edb75; output_sha256=42eb11612ff6ebf1a50c406002b4a1c248b6686962fcc8e6af333384465a2805; snapshot_sha256=f47425bc0a1be580afccf4a5b7c0559dfadea50e981cd7af8a4bd117e4cd477a
- Behavior: 完成了两页及版本内容更新，但错误地将页面标记为 v1.5.0 verified，且未展示完整的审计交接与真实宿主检查证据。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 在 docs-agent:docs-audit 可用后，将已完成的两页及匹配 change-map 条目推进 pre-tag 审计。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
