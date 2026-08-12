# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `regression-suite`
- Eval: `eval-003-mapped-doc-regression`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `b09fa431bfb2ae442891b6d53441773dfe7d31b84ffb9e7738912c1ba9a50a94` from `agents/qa/test/regression-suite/evals/workspace/eval-3-mapped-doc-regression`.
- Identity schema: `2`
- target_skill_sha256: `4e9403c0e6549024a79156a156c1294488d1a418598e88e3e9565298bc6bae6a`
- eval_definition_sha256: `e133160262ed184852d28136da76d373bddc3830b084351e43f62baba3d14a43`
- metadata_sha256: `8f1420b83ef9d543d57a760ebba7fc169b9c3d2172e7b3b1e191d47cfe76b856`
- fixture_sha256: `b09fa431bfb2ae442891b6d53441773dfe7d31b84ffb9e7738912c1ba9a50a94`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Identity migration: **MIGRATED_WITHOUT_MODEL_RERUN**
- Identity migration source commit: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Identity migration audit: `docs/engineer/repository-governance/eval-scenario-isolation/eval-identity-v2-migration-audit.json`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | with_skill 的锁定 trace 先读取 change-map，再读取其 required_docs 中的 search-query.md，未遍历其他站点文档。 |
| `verifies_against_code` | PASS | with_skill 直接核对 query.rules 得到阈值 3，并记录其与文档阈值 2 的差异及规则加载、长度校验、搜索请求路径。 |
| `treats_unverified_as_low_trust` | PASS | with_skill 明确将 last_verified_version: unverified 视为低信任，进一步核对代码/文件清单，并将修复验证和发布结论标为 blocked/needs more verification。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ffcf3a2d7addddf903f6f7ab8491b7d6388aab8f8d43086a53d98c797d44a47b; fixture_sha256=b09fa431bfb2ae442891b6d53441773dfe7d31b84ffb9e7738912c1ba9a50a94; output_sha256=1f72fea030893d0b54d2226b3606e55c83c5a4340b0b02f766a6501eab7817fd; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 按映射定位文档并回到代码核证，识别文档与代码冲突，谨慎报告阻塞状态和直接影响路径。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ffcf3a2d7addddf903f6f7ab8491b7d6388aab8f8d43086a53d98c797d44a47b; fixture_sha256=b09fa431bfb2ae442891b6d53441773dfe7d31b84ffb9e7738912c1ba9a50a94; output_sha256=67a7aac6b3917133439664b58455ed3b04259d29fb27f0f1238e95bb99e90252; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了阈值差异并给出回归边界，但直接建议以文档 2 为修复目标，未体现 unverified 文档的低信任处理。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 补齐原始失败、修复上下文、实现调用方、测试和平台版本后执行边界回归。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
