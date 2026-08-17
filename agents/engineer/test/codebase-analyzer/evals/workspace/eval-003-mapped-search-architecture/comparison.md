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
- target_skill_sha256: `41cf810393df0fdc64cc71f6ce5757c78fe5ad5c36eeff2140239588b7aedce4`
- eval_definition_sha256: `df0ea3b9e16f84cfa3123784feaff62e9978d327069fdb7ff40819c75c9ebde1`
- metadata_sha256: `dbe2c312aedb05903b843574c5ca000268c3b521104a50c6ae4c45e6b526236f`
- fixture_sha256: `a3ef5b9cc00c15c74b103c208a46d73ff5b53e17721ec0a79184a10c02b16859`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `953cf0ea99b9840a17c7b6706052165ac0b5ad2da8cf5b30696958f911637de4`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `0f34452462bbb10e7f7328b054a3e1b0e6f741b40ba12100a356dcedfa512f9c`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `c866a1fd5261fa544cd5ead0d94e8cdbb452e17b33cb77d4568d44490e6053bf`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_change_map_to_bound_context` | PASS | with_skill 输出明确引用 change map `docs/site/standards/change-map.yaml`，命中 `src/search/**` 并定位其 required_docs 为 `docs/site/api/search.md`，同时声明分析范围为 `src/search/**`。 |
| `verifies_claims_against_code` | PASS | with_skill 输出直接核验并引用 `src/search/query.txt`，准确报告 `entrypoint: search` 与 `match_mode: exact`，且未以文档声明替代代码事实。 |
| `reports_document_code_conflict` | PASS | with_skill 输出明确对比文档的 fuzzy matching 声明与代码的 `exact` 配置，并说明该冲突使 fuzzy matching 不能视为当前真实能力，影响后续改造评估。 |
| `does_not_overclaim_unverified_docs` | PASS | with_skill 输出识别 `last_verified_version: unverified`，将文档作为低信任声明处理，并明确未由代码证明的行为不写成当前事实。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0f34452462bbb10e7f7328b054a3e1b0e6f741b40ba12100a356dcedfa512f9c; fixture_sha256=a3ef5b9cc00c15c74b103c208a46d73ff5b53e17721ec0a79184a10c02b16859; output_sha256=81fb42887c290ad22bfdaa1dee5408298f1a48ebe2f4ca01775cee03805f15df; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完整完成只读分析：限定 change-map 上下文，回到 query.txt 核验代码，报告文档与代码冲突，并避免采信未验证文档结论。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0f34452462bbb10e7f7328b054a3e1b0e6f741b40ba12100a356dcedfa512f9c; fixture_sha256=a3ef5b9cc00c15c74b103c208a46d73ff5b53e17721ec0a79184a10c02b16859; output_sha256=6e50ee390f2517e2db48ea88b6f991b22fca9be57718c7bbf03429fa3cbaf97c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline 也完成了核心分析并满足这些断言，但其内容仅作为比较上下文，不影响 with_skill 判定。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
