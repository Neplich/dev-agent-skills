# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `qa-agent`
- Eval: `eval-001-route-mixed-qa-request`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `c9268123afd7a11d5bd4ac6d14865261ea2db8883ff6a745cea96f843ec5dbd5` from `agents/qa/test/qa-agent/evals/workspace/eval-1-route-mixed-qa-request`.
- Identity schema: `2`
- target_skill_sha256: `67401f0f5ce98032f224aebfb24715fe0d3d5f8bc92ca57ff320d37e3d49c72a`
- eval_definition_sha256: `0c9c4e17aa3aba15319c1b891ee6bf6eebad63436a6c10edd0a500e765aa29f6`
- metadata_sha256: `718fcc57ee1abd91d0d7551c46ebe8546481fa4f027452b86db232f30d15ab47`
- fixture_sha256: `c9268123afd7a11d5bd4ac6d14865261ea2db8883ff6a745cea96f843ec5dbd5`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `f4aaec46995456a39da2b489696e387a78408415038edddd6412ca13bedbc20a`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `d32b34f557a9af42827fae115c24f25ec47fe1e0fcda62e092dc3afa3789c767`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `07bcf2cf62398e35d6af14c6cbe959a504a24680a05115fbb8eaa9d7c4b5b04a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | 选择 `qa-agent:regression-suite` 作为唯一主路径，并依据确认文档、变更说明、QA 资料和 CI 风险推进。 |
| `assertion_2` | PASS | 明确传递 feature path、PRD/TRD/实现计划、QA 记忆、变更说明、CI 失败、执行入口及平台版本缺口。 |
| `specialist_gate_pointer` | PASS | 将后续执行明确交给 `regression-suite`，并列出其需检查的文档、E2E 记忆、平台版本、凭据、执行入口和证据门禁；未自行执行测试。 |
| `assertion_4` | PASS | 声明回归验证证据结构，包括状态、证据置信度、原始失败复核、修复行为、相邻风险、平台/环境/命令、结果文件和 release recommendation。 |
| `assertion_5` | PASS | 仅选择一个下游 QA specialist；将 WebKit 间歇性超时保留为风险和后续证据需求，未认定为 confirmed bug。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d32b34f557a9af42827fae115c24f25ec47fe1e0fcda62e092dc3afa3789c767; fixture_sha256=c9268123afd7a11d5bd4ac6d14865261ea2db8883ff6a745cea96f843ec5dbd5; output_sha256=cf10b51c7a18513627c8c8b63d77b975cd0ee1054dc78a5447dbb99d36bfdd99; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完成唯一 QA 路由并形成结构化 specialist handoff，保留证据缺口和风险，等待用户确认后继续下游验证。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d32b34f557a9af42827fae115c24f25ec47fe1e0fcda62e092dc3afa3789c767; fixture_sha256=c9268123afd7a11d5bd4ac6d14865261ea2db8883ff6a745cea96f843ec5dbd5; output_sha256=bcdf89296ebf048afc0444a11be00cadf02998ce63308ffc5c5ae8bc66a9e1e4; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 给出有条件验收建议和较完整证据清单，但未形成明确的 specialist 路由与职责边界。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
