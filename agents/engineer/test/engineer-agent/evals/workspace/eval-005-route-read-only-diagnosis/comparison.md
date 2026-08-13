# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `engineer-agent`
- Eval: `eval-005-route-read-only-diagnosis`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `e469c8867c3eaab395b1e2ecf769900426fc05c37fc44889d5555593c06bb9a0` from `agents/engineer/test/engineer-agent/evals/workspace/eval-005-route-read-only-diagnosis`.
- Identity schema: `2`
- target_skill_sha256: `4bbafb4fd1b263bfdfde7c9e30fb901fcf24822b1fff3e0e99c5d830d36c45cc`
- eval_definition_sha256: `ef789eef7ae75d20cd2b4f7363ad1491d04eb3cdb6114859d0ec16b9b00b6acb`
- metadata_sha256: `48a05f29fee0a106e78e2786488d2a57e30800d3511c0e6a27dab7a0cee8b2d5`
- fixture_sha256: `e469c8867c3eaab395b1e2ecf769900426fc05c37fc44889d5555593c06bb9a0`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `50ba2d2012c41a93dc7606cfb865565f1a5b791f485b360a632d9cb7b9413bac`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `6501dca073ea693c3fce773a64fba0b68444a0b5dc8e1f9f199b652d00d7a920`
- Repository HEAD: `2f950c46c67111058957774f796ccf97ae616d36`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `93852e7b81da4b65a2f6e7e6b552fb8fc2585f12fb1990e01ea0c8684431a23e`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_read_only_fields` | PASS | with_skill 输出明确保留 `current_delivery_stage: diagnosis_only` 与 `allowed_mutations: none`，并列出禁止修改代码、测试、配置、数据库及外部状态。git evidence 显示无改动。 |
| `routes_to_existing_debugger` | PASS | with_skill 输出将 `selected_specialist` 明确设为唯一的 `engineer-agent:debugger`，并说明 dispatcher 不代替 debugger，也未新建或建议平行 diagnosis specialist。 |
| `does_not_require_repair_docs_first` | PASS | with_skill 输出将 `expected_behavior_alignment` 标为 `unaligned`，明确 PRD/TRD 缺失只限制结论，并允许只读收集；同时明确不得确认实现偏差、提出修复方案或修改状态。其 blocked 原因是 debugger 插件不可用，而非要求先补修复文档。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6501dca073ea693c3fce773a64fba0b68444a0b5dc8e1f9f199b652d00d7a920; fixture_sha256=e469c8867c3eaab395b1e2ecf769900426fc05c37fc44889d5555593c06bb9a0; output_sha256=f32c68ab8ecd422d94e70db1d46428892d7adab2b66aa4a33e8b6d1c2a7ccd76; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 保留只读边界，正确路由至现有 debugger，并在期望文档缺失时保持 unaligned，不进入修复流程。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6501dca073ea693c3fce773a64fba0b68444a0b5dc8e1f9f199b652d00d7a920; fixture_sha256=e469c8867c3eaab395b1e2ecf769900426fc05c37fc44889d5555593c06bb9a0; output_sha256=4a3480667b7cb8c356fa27acd0b9bdf40da1b78bf5f521f335d741411915fafe; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提供了只读调查结论并保持工作区无改动，但未呈现 engineer-agent 到 debugger 的明确路由，也未明确 expected_behavior_alignment: unaligned。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
