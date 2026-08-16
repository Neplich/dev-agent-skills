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
- target_skill_sha256: `c9fd11f6d83f8ba28a8e7797fde5b9dd25e2a04cb6c37589ec154de48aa8548c`
- eval_definition_sha256: `df0ea3b9e16f84cfa3123784feaff62e9978d327069fdb7ff40819c75c9ebde1`
- metadata_sha256: `dbe2c312aedb05903b843574c5ca000268c3b521104a50c6ae4c45e6b526236f`
- fixture_sha256: `a3ef5b9cc00c15c74b103c208a46d73ff5b53e17721ec0a79184a10c02b16859`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `953cf0ea99b9840a17c7b6706052165ac0b5ad2da8cf5b30696958f911637de4`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `0f34452462bbb10e7f7328b054a3e1b0e6f741b40ba12100a356dcedfa512f9c`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `1f817d88b8e507da0a311c9d5e0c0422e91854cfcc0cc72bf66b96f5b16560f6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_change_map_to_bound_context` | PASS | with_skill 的原始轨迹读取并命中 change-map.yaml 中 `src/search/**` 条目，定位 required_docs 为 `docs/site/api/search.md`，且后续检索限定于相关文件。 |
| `verifies_claims_against_code` | PASS | with_skill 直接读取 `src/search/query.txt`，引用其中 `entrypoint: search` 与 `match_mode: exact`，并将其作为能力判断的代码依据。 |
| `reports_document_code_conflict` | PASS | with_skill 明确对比文档的 fuzzy matching 声明与 `query.txt` 的 `match_mode: exact`，并说明当前基线及后续改造评估影响。 |
| `does_not_overclaim_unverified_docs` | PASS | with_skill 识别 `last_verified_version: unverified`，将 fuzzy 视为未核实文档描述，未将其写成当前已支持能力。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0f34452462bbb10e7f7328b054a3e1b0e6f741b40ba12100a356dcedfa512f9c; fixture_sha256=a3ef5b9cc00c15c74b103c208a46d73ff5b53e17721ec0a79184a10c02b16859; output_sha256=4999fcae55dc310f96720f045fd9e5581565afd82eaa8870d5cf516f22c3f576; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完成了基于 change map、文档与代码交叉核验的证据化分析，准确报告了 exact/fuzzy 分歧及未验证文档的限制。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0f34452462bbb10e7f7328b054a3e1b0e6f741b40ba12100a356dcedfa512f9c; fixture_sha256=a3ef5b9cc00c15c74b103c208a46d73ff5b53e17721ec0a79184a10c02b16859; output_sha256=7105b9605ad05a7b9e5f9e69e9e02ca82bbd9b97f1b844b6a9d14c0246155afe; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提供了基本的代码、文档和能力冲突分析，整体结论相近，但作为比较基线不影响 with_skill 判定。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
