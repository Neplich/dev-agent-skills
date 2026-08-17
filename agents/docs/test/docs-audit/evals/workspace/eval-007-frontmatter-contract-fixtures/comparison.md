# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-007-frontmatter-contract-fixtures`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1219a80a8f97201ae3cdd929f2d631a2ba100cf6ab153bec6afe2b6d163ff59f` from `agents/docs/test/docs-audit/evals/workspace/eval-007-frontmatter-contract-fixtures`.
- Identity schema: `2`
- target_skill_sha256: `a5e0bb043d61dbbb218e7d7efc08374e0d16a4d7aaa3b31817f2038830c90941`
- eval_definition_sha256: `6bde344495a08502946e81bb93f2ae1c40e1aff64c95e853b673dd5a307e9ade`
- metadata_sha256: `ac5c625c3b447eed92814a4915de66331bf3c2449cbef00676c3c687ad5d80de`
- fixture_sha256: `1219a80a8f97201ae3cdd929f2d631a2ba100cf6ab153bec6afe2b6d163ff59f`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `216827bc3e07bc68d228647a6fadcd479f48a986964f70c0c40f48052e42886f`
- Source lock SHA-256: `c58f04d32c2ca3a22aec96f7ee027af648da5971453d2a5553d7ab2cd9272551`
- Prompt SHA-256: `49a9f020c04120ad8bdb6f9b036cf5ce5bd9266f99e431e7e0059400223b90de`
- Repository HEAD: `60a4b3602dc07f3f6683a8873529bbdba6f8d27d`
- Repository worktree state: **CLEAN**
- Skill overlay SHA-256: `d7e2242fcdf83209e6c0cb5ec9544aa009e79488a72f81ebd4bf387289fbabec`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_confirmed_audit_entry` | PASS | 读取并接受了维护者确认的 v0.4.0、4a1b2c3、7c9e2af、pre-tag 阶段和证据清单。 |
| `rejects_standard_doc_type` | PASS | 明确将 catalog-search.md 的 doc_type: standard 判为 stale。 |
| `rejects_empty_related_code` | PASS | 明确将 catalog-export.md 的 related_code: [] 判为 stale。 |
| `rejects_missing_last_verified_version` | PASS | 明确将 catalog-status.md 因缺少 last_verified_version 判为 stale。 |
| `rejects_empty_owners` | PASS | 明确将 catalog-bulk-update.md 因 owners: [] 判为 stale。 |
| `accepts_valid_api_page` | PASS | 确认 catalog-items.md 的声明得到 routes.txt 中 GET /catalog/items、200 和 items 的事实支持；原始页面包含七个合法必填字段。 |
| `blocks_release_for_invalid_frontmatter` | PASS | 四个非法页面均保留为 stale，阶段结果为 blocked，且明确未统一 stamp、未返回 ready_for_tag。 |
| `uses_shared_contract_source` | NOT_EXERCISED | 原始 trace 证明读取了 docs-agent 的 frontmatter-contract.md，但没有证明检查了 docs-site-bootstrap 交付的 check-frontmatter.mjs 或确认两者逻辑一致。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=49a9f020c04120ad8bdb6f9b036cf5ce5bd9266f99e431e7e0059400223b90de; fixture_sha256=1219a80a8f97201ae3cdd929f2d631a2ba100cf6ab153bec6afe2b6d163ff59f; output_sha256=ab62ec42390ae258a5a549bde2f44bd6a650ffda06c88e54393c7c7f275b63b8; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确接受审计入口，识别四类非法 frontmatter，验证合法 API 页面的路由事实，并阻塞 pre-tag 发布。共享契约与宿主校验逻辑的一致性无法由锁定证据完整证明。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=49a9f020c04120ad8bdb6f9b036cf5ce5bd9266f99e431e7e0059400223b90de; fixture_sha256=1219a80a8f97201ae3cdd929f2d631a2ba100cf6ab153bec6afe2b6d163ff59f; output_sha256=3870a1e0dd015f661824b6af1ecd7c5bbee4d5706dc85d0106905925cce8ae80; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提供了 fresh baseline：同样给出 NO-GO 并识别主要页面问题，但证据核对和契约一致性说明较不完整。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
