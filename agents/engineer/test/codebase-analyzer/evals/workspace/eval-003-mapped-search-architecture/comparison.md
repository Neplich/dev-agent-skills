# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `codebase-analyzer`
- Eval: `eval-003-mapped-search-architecture`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `a3ef5b9cc00c15c74b103c208a46d73ff5b53e17721ec0a79184a10c02b16859` from `agents/engineer/test/codebase-analyzer/evals/workspace/eval-003-mapped-search-architecture`.
- Identity schema: `2`
- target_skill_sha256: `de6d27a82a6affa1d54b83f57c4eb1889c4977944cd8849112c1a97798fbfd77`
- eval_definition_sha256: `df0ea3b9e16f84cfa3123784feaff62e9978d327069fdb7ff40819c75c9ebde1`
- metadata_sha256: `c79f8b60b8eda49d60383374b0b105b8c506dcb4b757a67593ed9721a0d169df`
- fixture_sha256: `a3ef5b9cc00c15c74b103c208a46d73ff5b53e17721ec0a79184a10c02b16859`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `953cf0ea99b9840a17c7b6706052165ac0b5ad2da8cf5b30696958f911637de4`
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
| `uses_change_map_to_bound_context` | PASS | with_skill 明确引用 change-map，将 src/search/** 映射到 docs/site/api/search.md，并将分析范围限定在搜索模块及其映射文档；原始 trace 也显示直接读取了 change map 和 required_docs，未扩展到无关正式文档。 |
| `verifies_claims_against_code` | PASS | with_skill 直接以 src/search/query.txt 中的 match_mode: exact 和 entrypoint: search 核验入口及匹配模式，并明确没有可执行搜索实现。 |
| `reports_document_code_conflict` | PASS | with_skill 清楚对比文档的 fuzzy matching 声明与代码的 match_mode: exact，说明该冲突影响当前能力判断，并指出后续需确认真实运行载体和 API 契约。 |
| `does_not_overclaim_unverified_docs` | PASS | with_skill 识别文档和 change map 的 last_verified_version: unverified，明确将文档降为低信任导航信息，并未将未经代码证明的 fuzzy matching 写成当前事实。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0f34452462bbb10e7f7328b054a3e1b0e6f741b40ba12100a356dcedfa512f9c; fixture_sha256=a3ef5b9cc00c15c74b103c208a46d73ff5b53e17721ec0a79184a10c02b16859; output_sha256=bdc0077b4984b1a1e18ef6353f46a46054d11ad798860614d88ca2d67452d179; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 基于 change map 限定上下文，回到 query.txt 核验代码事实，并完整报告文档冲突与未验证状态。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0f34452462bbb10e7f7328b054a3e1b0e6f741b40ba12100a356dcedfa512f9c; fixture_sha256=a3ef5b9cc00c15c74b103c208a46d73ff5b53e17721ec0a79184a10c02b16859; output_sha256=fdb861c0021f8fd359a0d1a48966875882c34a944bb925251cb9066d95d492fa; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 也完成了代码核验和冲突识别，但作为比较基线，不影响 with_skill assertion verdicts。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
