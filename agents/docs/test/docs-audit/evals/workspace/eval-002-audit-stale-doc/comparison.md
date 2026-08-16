# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-002-audit-stale-doc`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583` from `agents/docs/test/docs-audit/evals/workspace/eval-002-audit-stale-doc`.
- Identity schema: `2`
- target_skill_sha256: `dafd53371901dfd724f88c70262b157e59494d29da1c613d0ef130564b6ff4f9`
- eval_definition_sha256: `65171d2c00ad7205a3b92eb523639da0ae1b9b851f9b225fb39f151ac8a09d1b`
- metadata_sha256: `393d49433e1e9b818095a60378e27c82e27a5159f0878e57881a2872b5feee91`
- fixture_sha256: `7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6c436d29e1c4d967534d387d71455397c2a958eb0e9fdd8f24d404e3a4bfc7c7`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `a0986a693a041b20341e8fc74006f156b719dab648f0efc1ee18f7a27b8849f4`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `7e61bd8eca6431729aee1f3be4656be0a4348119eb1218623bafd54cfaead2ab`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `marks_missing_doc_update_suspect` | PASS | 报告将未在同批变更中的正式 API 页面描述为 suspect，并在事实核查后确认其与代码契约不一致。 |
| `confirms_outdated_claim_stale` | PASS | 报告以目标代码中的必填非空 locale 和 400 invalid_locale 为证据，确认文档声明不同步（以 confirmed mismatch 表述）。 |
| `blocks_stale_release` | PASS | 报告列出文档契约缺失及具体修复/重审待办，阶段结果为 blocked，并明确禁止创建标签、未产生 ready_for_tag 结果。 |
| `does_not_stamp_stale_set` | PASS | 交付报告明确未盖章；git 状态和交付快照仅显示新增审计报告，没有页面或 releases.json 的更新。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a0986a693a041b20341e8fc74006f156b719dab648f0efc1ee18f7a27b8849f4; fixture_sha256=7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583; output_sha256=99f9469d5d7ecc39b41cbc00ba092037e65b2cdcb2b93cfbc5d95878eb6ab0ac; snapshot_sha256=4690bf63b82a5abeb3b7a5944b4b4d5afcdd723ee48975d065e04060d7c99fb0
- Behavior: 完成审计并保存报告，确认文档与新增 locale 契约不一致，阻断发布且未更新版本戳。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a0986a693a041b20341e8fc74006f156b719dab648f0efc1ee18f7a27b8849f4; fixture_sha256=7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583; output_sha256=882560f7f386f02534550c60be7d0de94f8582066a4749f4e5363da5074e92c4; snapshot_sha256=998b99c5e14e5836aacde17e8576892e644cc7f2fe7eeed9e1a21f0a086da75e
- Behavior: 基线也识别了 locale 文档缺失并保存了报告，但未展示确定性 suspect 到事实确认及版本面保护的完整审计行为。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
