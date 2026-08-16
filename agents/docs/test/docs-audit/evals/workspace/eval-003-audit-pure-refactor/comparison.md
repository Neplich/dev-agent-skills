# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-003-audit-pure-refactor`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `a0071569c74867aaacfda16310f9f4a06e50a375aa0e6b62ee25e801db096677` from `agents/docs/test/docs-audit/evals/workspace/eval-003-audit-pure-refactor`.
- Identity schema: `2`
- target_skill_sha256: `dafd53371901dfd724f88c70262b157e59494d29da1c613d0ef130564b6ff4f9`
- eval_definition_sha256: `a7212e3282f2eaaa660e0675fb965d5050f366a07c153f3821d78fdab8976de5`
- metadata_sha256: `1e20c97bb5ffc477023f6bbbd217e71d747297cb0b8f52652660b6b2d10adc7a`
- fixture_sha256: `a0071569c74867aaacfda16310f9f4a06e50a375aa0e6b62ee25e801db096677`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `3e58dae2a34edb25f9589f7bddb4e3282cd1f66e3b0c3f35187db4ed16fd5f23`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `20617e4b8714b5129b537177e8c463822eec4083d7fdd0d6520c27013f94489f`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `7e61bd8eca6431729aee1f3be4656be0a4348119eb1218623bafd54cfaead2ab`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `sends_refactor_suspect_to_fact_layer` | NOT_EXERCISED | 锁定原始 trace 仅证明加载并遵循两层审计协议，未证明实际将页面标记为 suspect 并交给事实层。 |
| `classifies_accurate_refactor_verified` | PASS | with_skill 输出明确将页面结论标为 `verified`，并核对了 GET 路径、limit 参数、200 响应及 400 错误声明。 |
| `does_not_force_noop_doc_edit` | PASS | with_skill 输出明确声明纯实现重构不需要无意义的文档改动，并将 `documentation_change_required` 设为 false。 |
| `does_not_block_for_unchanged_accurate_doc` | PASS | with_skill 输出将页面判为 `verified` 而非 `stale`，并将整体结果阻塞归因于缺少 Release Notes、版本索引及其他完整版本面证据；明确未返回 `ready_for_tag` 且未执行统一版本戳更新。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=20617e4b8714b5129b537177e8c463822eec4083d7fdd0d6520c27013f94489f; fixture_sha256=a0071569c74867aaacfda16310f9f4a06e50a375aa0e6b62ee25e801db096677; output_sha256=ce99540d8143e1c4d72e9b2a2b08202a2a20fcdf9426b24f62e944746a092ce1; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 准确识别纯实现重构，确认 API 页面仍 verified、无需无意义编辑，并因缺失完整 release-version surface 证据而阻塞整体 pre-tag 结论。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=20617e4b8714b5129b537177e8c463822eec4083d7fdd0d6520c27013f94489f; fixture_sha256=a0071569c74867aaacfda16310f9f4a06e50a375aa0e6b62ee25e801db096677; output_sha256=6038eefdc1da9d64933e8b8770c10143c94d63bbdf3c22bab5caec9b0af77aa1; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别 API 内容未漂移，但将未更新的版本标记作为后续跟进项，未形成 with_skill 的事实层 verified 与完整版本面阻塞结论。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
