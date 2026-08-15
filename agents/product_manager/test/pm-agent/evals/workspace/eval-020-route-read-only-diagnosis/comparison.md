# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-020-route-read-only-diagnosis`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `0c37c580ec355abeaea3f2fc33d6ed8061916801102550f7da9905107759e638` from `agents/product_manager/test/pm-agent/evals/workspace/eval-020-route-read-only-diagnosis`.
- Identity schema: `2`
- target_skill_sha256: `ed93e443692bf05e76aaa38c8a5b8faff57190219ed48b9335316584424e6eb9`
- eval_definition_sha256: `ac2e29c8ea600b5bded6655e93f469267e3a3d70f27c2a43049a20f14780fa3c`
- metadata_sha256: `626240265d5c7ac5c06804a17b53a20dce96bac558a2504b82b9a8f747b23779`
- fixture_sha256: `0c37c580ec355abeaea3f2fc33d6ed8061916801102550f7da9905107759e638`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `25ec3d21dbc5318b2aa7981fadceeb5bd08d4e0daef2594dfe1fa5018e038ab2`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `548143066f55535e284127a49d04caed1052641b0e381dde2aacad45c5301978`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `67e6ae6bfee138166b25d903bb8ed5fced4658c060c4a43be1e074d3795bfaaa`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `classifies_read_only_bug_report` | PASS | with_skill 明确将请求标为 bug_report，并以 diagnosis_only 处理，声明不修复。 |
| `sets_zero_mutation_boundary` | PASS | with_skill 明确声明 allowed_mutations: none，并列出不修改代码、配置、测试、数据库、外部状态、提交或 PR；git evidence 也显示无变更。 |
| `allows_unaligned_diagnosis_handoff` | PASS | with_skill 在缺少 PRD/TRD 时选择 Engineer，设置 expected_behavior_alignment: unaligned，保留 feature_path: unresolved，并要求继续前确认；未确认 implementation_deviation 或进入修复。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=548143066f55535e284127a49d04caed1052641b0e381dde2aacad45c5301978; fixture_sha256=0c37c580ec355abeaea3f2fc33d6ed8061916801102550f7da9905107759e638; output_sha256=5fe7f24e0a7182a3d706c882ea04a4d901c88275240efcb9b379d965a726dfcd; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完成只读 bug_report 分类，建立零修改边界，并准备保持 unaligned 的 Engineer 诊断交接。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=548143066f55535e284127a49d04caed1052641b0e381dde2aacad45c5301978; fixture_sha256=0c37c580ec355abeaea3f2fc33d6ed8061916801102550f7da9905107759e638; output_sha256=7ca4b89737237c74f9e33326affafb3c59c3dc7bd697061ebb3d55e9ee339ebb; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提供了只读故障摘要和无变更证据，但未展示结构化 bug_report 分类、零修改交接边界或 unaligned Engineer handoff。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
