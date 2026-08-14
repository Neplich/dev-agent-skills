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
- target_skill_sha256: `87273b18e32710512ee493a3e80a098f8b357ae29e71e4e0a6f3bdb4e8e38c08`
- eval_definition_sha256: `0c9c4e17aa3aba15319c1b891ee6bf6eebad63436a6c10edd0a500e765aa29f6`
- metadata_sha256: `718fcc57ee1abd91d0d7551c46ebe8546481fa4f027452b86db232f30d15ab47`
- fixture_sha256: `c9268123afd7a11d5bd4ac6d14865261ea2db8883ff6a745cea96f843ec5dbd5`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `f4aaec46995456a39da2b489696e387a78408415038edddd6412ca13bedbc20a`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `d32b34f557a9af42827fae115c24f25ec47fe1e0fcda62e092dc3afa3789c767`
- Repository HEAD: `2f950c46c67111058957774f796ccf97ae616d36`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `8e73acbd41a735f43f1f03a7222bf46710fac8290789ae5f94fc114c9a9ac613`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | with_skill 明确选择一个主路径：进入验收准备/QA 路由，选择 spec-based-tester，并将 WebKit 超时保留为风险。 |
| `assertion_2` | PASS | with_skill 传递了 PM/Engineer 文档、实现变更、QA 套件/流程记忆、CI 失败信息和 npm test -- login 执行入口，同时保留环境、凭据、平台版本缺口，未假设浏览器或端口。 |
| `specialist_gate_pointer` | PASS | with_skill 明确将后续执行和最终判定交给 qa-agent:spec-based-tester，并列出其需检查的平台版本、环境、账号、执行入口及相关资料；同时说明 router 不执行测试。 |
| `assertion_4` | PASS | with_skill 声明了每个 TC 的 result.md、testcase.snapshot.md、feature-update 汇总报告、需求—执行结果矩阵、阻塞项和风险等产物结构。 |
| `assertion_5` | PASS | with_skill 只选择一个下游 specialist，明确不是 bug-analyzer，并将 WebKit 间歇性超时作为风险记录而非 confirmed bug。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d32b34f557a9af42827fae115c24f25ec47fe1e0fcda62e092dc3afa3789c767; fixture_sha256=c9268123afd7a11d5bd4ac6d14865261ea2db8883ff6a745cea96f843ec5dbd5; output_sha256=11eba24a5736bed601b9714c44030b13e4c72a7f08dc84d9518760f49f1f9f32; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完成单一路由选择、上下文传递、specialist 权威门禁指针和结构化证据产物声明；未执行测试。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d32b34f557a9af42827fae115c24f25ec47fe1e0fcda62e092dc3afa3789c767; fixture_sha256=c9268123afd7a11d5bd4ac6d14865261ea2db8883ff6a745cea96f843ec5dbd5; output_sha256=99c03ee60d4647bb341e295721407c1aa897401c87321b123576dc933080a0e1; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 给出合理的 QA 准备建议和证据清单，但未提供 specialist 路由与权威门禁指针。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 由 spec-based-tester 在取得平台版本、凭据、环境和可执行入口后继续验证。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
