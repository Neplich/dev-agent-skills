# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-006-design-gate-all-passed`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `98bf611a541c8fe0137472ae23a2bee304eb1dd895062850790d9e776e872e75` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-006-design-gate-all-passed`.
- Identity schema: `2`
- target_skill_sha256: `314b02febc2ef94201a8e1bf1080c874c355a0e47e6ac9a01b931425f08bfbd7`
- eval_definition_sha256: `409f0dff74eed97473da7310514056fa3150a1bcc243e245700365b8124e237d`
- metadata_sha256: `d850062d9ab19e577fb519798bc20c97592f06bfa16acdff382b6c2af72957e7`
- fixture_sha256: `98bf611a541c8fe0137472ae23a2bee304eb1dd895062850790d9e776e872e75`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `ebe36ab58d09b32dcb1d3a0e60e80a8c30163db5b3f4afa9ec0da402309c3c17`
- Source lock SHA-256: `c58f04d32c2ca3a22aec96f7ee027af648da5971453d2a5553d7ab2cd9272551`
- Prompt SHA-256: `c76b170dd7794d3734918c7a765e05580924d97e899b93480f8dc75124874544`
- Repository HEAD: `60a4b3602dc07f3f6683a8873529bbdba6f8d27d`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `84e19c3e634cfde176d2ff20ba8e9d25a4838db3ed1deb5def94a8d0f1d2ddd9`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `passes_completion_gates` | PASS | With_skill 提供逐项 closeout matrix，前六项均为 PASS；锁定的 PRD、TRD、计划、diff 与测试记录共同支持这些结论。 |
| `stops_at_scope_confirmation` | PASS | With_skill 展示了设计页、代码范围、证据、排除项和未决项，明确 Step 4 等待确认；锁定 git 证据显示工作区未修改。 |
| `current_state_only` | PASS | With_skill 提出的设计事实仅包括固定字段顺序、省略空值及 compact 复用有序非空值，均由锁定代码与通过测试支持。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c76b170dd7794d3734918c7a765e05580924d97e899b93480f8dc75124874544; fixture_sha256=98bf611a541c8fe0137472ae23a2bee304eb1dd895062850790d9e776e872e75; output_sha256=69381a5343cef34035d58fa8667af9534893905e627d98a9b7c5c122d769fbf6; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完成只读候选规划，准确绑定证据并停在维护者范围确认前，未修改站点。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c76b170dd7794d3734918c7a765e05580924d97e899b93480f8dc75124874544; fixture_sha256=98bf611a541c8fe0137472ae23a2bee304eb1dd895062850790d9e776e872e75; output_sha256=210e76073b905a7bab93383ed13bc606aabef0bd24cd0f396fc58ba7d8077f67; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 也完成了基本候选范围识别并停在确认前，但证据绑定和门禁呈现较简略。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
