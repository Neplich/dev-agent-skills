# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-003-route-release-audit`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `c4a69775f21689d655afd993fc0db7c357209ede650d2394be50a3f72bd824b5` from `agents/docs/test/docs-agent/evals/workspace/eval-003-route-release-audit`.
- Identity schema: `2`
- target_skill_sha256: `cf826e2e86ef193d8a7294a87c743dead6af892aefcc220dd56ae949fa5c3b40`
- eval_definition_sha256: `6d6a401b76741386ad3f6aee549b3bfaa2f477f4ced9973b14647dc8b591096b`
- metadata_sha256: `d582bafa2b7d4e637ef2b4b71f14f435256d70c30e92f7097a43cd40dc9da750`
- fixture_sha256: `c4a69775f21689d655afd993fc0db7c357209ede650d2394be50a3f72bd824b5`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `f4f786bd56d6a5cbcee24193816a462566a8caafb4c223ef38759bdf64ee0486`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `099569afeec045caa3e4e020611c72b9def7b5897f52222810916bd2477fd230`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `4f8c2e7785cbff8446ac2450d611cce0b0fa2bab79e21c8ccd8c57b18b15a51c`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_equivalent_chain` | PASS | with_skill 复述了 release scope、v0.4.0/v0.3.0、changelog、Release Notes、检查证据和 requested node，构成等效确认链。 |
| `routes_docs_audit` | FAIL | with_skill 将已满足入口的请求判定为缺少 host_repository/required_output，并返回 pm-agent，而不是选择 docs-audit 并保留上下文交接。 |
| `references_audit_gate_only` | PASS | with_skill 明确指出后续 specialist 为 docs-audit，未执行审计，也未向用户暴露本地 SKILL.md 路径或复制详细审计协议。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=099569afeec045caa3e4e020611c72b9def7b5897f52222810916bd2477fd230; fixture_sha256=c4a69775f21689d655afd993fc0db7c357209ede650d2394be50a3f72bd824b5; output_sha256=43f17cbe59aed2ceacf5808fde869410032d79d70e374cb98c907dae623bcb31; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了等效确认链并保持了 specialist 边界，但错误地拒绝路由到 docs-audit。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=099569afeec045caa3e4e020611c72b9def7b5897f52222810916bd2477fd230; fixture_sha256=c4a69775f21689d655afd993fc0db7c357209ede650d2394be50a3f72bd824b5; output_sha256=7df0bd78c2b8863728c113c1ee0da89593dc85c85c9f23234962abea27c5dbca; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 未执行路由，直接对发布材料做了仓库审计并给出 BLOCKED/NOT READY 结论，偏离了 Router 职责。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 错误扩展了 Router 入口要求，导致本应路由至 docs-audit 的请求被阻断并退回 pm-agent。
- Next: 将 release-entry.md 视为完整等效确认入口，保留其 release scope、版本 tag、changelog 和 release evidence，并路由至 docs-audit。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
