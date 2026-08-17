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
- target_skill_sha256: `944bb130633ab2aa16595ed1d51c447f77cd06660f1aafc548f03bd9b22af162`
- eval_definition_sha256: `0c9c4e17aa3aba15319c1b891ee6bf6eebad63436a6c10edd0a500e765aa29f6`
- metadata_sha256: `718fcc57ee1abd91d0d7551c46ebe8546481fa4f027452b86db232f30d15ab47`
- fixture_sha256: `c9268123afd7a11d5bd4ac6d14865261ea2db8883ff6a745cea96f843ec5dbd5`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `f4aaec46995456a39da2b489696e387a78408415038edddd6412ca13bedbc20a`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `d32b34f557a9af42827fae115c24f25ec47fe1e0fcda62e092dc3afa3789c767`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `b72f030fc95be72eca667c1396fcf25fade5c01afa11ea1d384304d1797aeac5`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | with_skill 明确选择 regression-suite 作为主 QA 验收路径，并将 WebKit 间歇性超时保留为风险。 |
| `assertion_2` | PASS | 交接中保留了 PRD、TRD、实现计划、变更说明、QA memory、CI 日志、平台版本状态和执行入口。 |
| `specialist_gate_pointer` | PASS | 明确将后续验证交给 regression-suite，并声明本次路由阶段不自行执行下游回归。 |
| `assertion_4` | PASS | 声明了原始失败复核、修复验证、相邻路径结果、置信度、平台状态、发布建议及逐 TC result.md/testcase.snapshot.md 等产物结构。 |
| `assertion_5` | PASS | 仅选择一个下游 specialist；将证据不足的 WebKit 超时作为风险和待复核事项，未确认其为产品缺陷。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d32b34f557a9af42827fae115c24f25ec47fe1e0fcda62e092dc3afa3789c767; fixture_sha256=c9268123afd7a11d5bd4ac6d14865261ea2db8883ff6a745cea96f843ec5dbd5; output_sha256=a5a2e1e10cf6d79cebdb477ca9af194bcb3395e006bf6df4176abc679c2cc189; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 选择单一 regression-suite 路径，完整传递上下文并声明后续验证所需证据与风险边界；未执行下游回归。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d32b34f557a9af42827fae115c24f25ec47fe1e0fcda62e092dc3afa3789c767; fixture_sha256=c9268123afd7a11d5bd4ac6d14865261ea2db8883ff6a745cea96f843ec5dbd5; output_sha256=484eecf66c9fee9bac541d4cf91380afb475fbd8fd9f929be455fdb82ed7ba10; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 给出条件验收建议和证据清单，但未形成明确 specialist 路由或结构化 handoff。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
