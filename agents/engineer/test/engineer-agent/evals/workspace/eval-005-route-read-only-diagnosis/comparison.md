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
- target_skill_sha256: `4844b5e075259765184f2662312a91c5cdcb5ff00686044034ea15af2e50c5ac`
- eval_definition_sha256: `ef789eef7ae75d20cd2b4f7363ad1491d04eb3cdb6114859d0ec16b9b00b6acb`
- metadata_sha256: `e4901c042b0409a9250648c22e35f5aa91c71bf1facf120010b04e53329e73e7`
- fixture_sha256: `e469c8867c3eaab395b1e2ecf769900426fc05c37fc44889d5555593c06bb9a0`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `50ba2d2012c41a93dc7606cfb865565f1a5b791f485b360a632d9cb7b9413bac`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `6501dca073ea693c3fce773a64fba0b68444a0b5dc8e1f9f199b652d00d7a920`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `65d01d81aab66b453dc18dc77df0f17f854503579e4f5025c7c7c7f0257e73eb`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_read_only_fields` | PASS | with_skill 输出明确保留 `mode: diagnosis_only` 与 `allowed_mutations: none`，并声明禁止修改代码、测试、配置、数据库及外部状态。 |
| `routes_to_existing_debugger` | PASS | with_skill 输出明确将下一专员设为 `debugger`，并将只读诊断交给 `debugger`；未提出并行 specialist 或新建 route。 |
| `does_not_require_repair_docs_first` | PASS | with_skill 输出在缺少 PRD/TRD 时仍安排有限的客观证据收集，标记 `expected_behavior_alignment: unaligned`，且明确不得确认 `implementation_deviation`、不得生成或执行修复计划。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6501dca073ea693c3fce773a64fba0b68444a0b5dc8e1f9f199b652d00d7a920; fixture_sha256=e469c8867c3eaab395b1e2ecf769900426fc05c37fc44889d5555593c06bb9a0; output_sha256=6ccb9d3fee247a9e77bbd88960928683eb0b99fa1226a571ac37bb08f8f6b2a8; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 保留只读边界，路由至现有 debugger，并在缺少 PRD/TRD 时继续有限证据收集而不进入修复。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6501dca073ea693c3fce773a64fba0b68444a0b5dc8e1f9f199b652d00d7a920; fixture_sha256=e469c8867c3eaab395b1e2ecf769900426fc05c37fc44889d5555593c06bb9a0; output_sha256=1927e423a3d013d6f03330cf83927f22c42d82f61cb016949d403ac2da56ead8; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 保持未修改工作区，但将缺少 PRD/TRD 视为诊断阻塞，未路由至 debugger。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
