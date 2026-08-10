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
- Fixture SHA-256: `c9268123afd7a11d5bd4ac6d14865261ea2db8883ff6a745cea96f843ec5dbd5`
- Prompt SHA-256: `d32b34f557a9af42827fae115c24f25ec47fe1e0fcda62e092dc3afa3789c767`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `23a4457fc9bf10be6976d98ea55607b47c6c623db1e20d5c73160d9f386c2a36`
- Skill overlay SHA-256: `aba4853023a6c2866bcd67ad1139982ac56eeacfec787957221635a36cab60ad`
- Judge schema SHA-256: `f4aaec46995456a39da2b489696e387a78408415038edddd6412ca13bedbc20a`
- Eval definition SHA-256: `2ad0a90eac7fca1f06d238ff5d3d06535381ddd810d8a9e8e9e423ce29483f2c`
- Metadata SHA-256: `718fcc57ee1abd91d0d7551c46ebe8546481fa4f027452b86db232f30d15ab47`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | 选择 qa-agent:spec-based-tester，并以已确认的 PRD/TRD/IMPLEMENTATION_PLAN、变更说明、QA 记忆及 CI WebKit 间歇性失败说明其为最窄责任方。 |
| `assertion_2` | PASS | 列出了 PM/Engineer 文档、QA suite/flow、环境说明、账号凭据状态、QA application URL 和 npm test -- login 执行入口。 |
| `specialist_gate_pointer` | PASS | 明确由 spec-based-tester 负责 preflight、执行和证据归档，并将平台版本、环境 URL、账号、执行入口及确认文档核验留给 specialist；router 声明不执行测试或创建报告。 |
| `assertion_4` | PASS | 声明了每个 TC 的 result.md、testcase.snapshot.md，以及按平台版本归档的 feature-update 汇总报告，并包含 PASS/FAIL/BLOCKED、风险和验收建议。 |
| `assertion_5` | PASS | 仅选择一个下游 specialist；将 CI 超时保留为风险项，不直接认定为 confirmed bug 或改走 bug 分析。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d32b34f557a9af42827fae115c24f25ec47fe1e0fcda62e092dc3afa3789c767; fixture_sha256=c9268123afd7a11d5bd4ac6d14865261ea2db8883ff6a745cea96f843ec5dbd5; output_sha256=bd70db8423d67b7cdf9bcdddbd87fce0fe3986f5eb5ad950c1026b0f7236bf76; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完整完成单一路由、上下文传递、specialist 门禁指针、证据产物和风险边界控制。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d32b34f557a9af42827fae115c24f25ec47fe1e0fcda62e092dc3afa3789c767; fixture_sha256=c9268123afd7a11d5bd4ac6d14865261ea2db8883ff6a745cea96f843ec5dbd5; output_sha256=98b752b49faa7867014a55089cfb6394ff3302e17b5754af52c60e47e57d1fef; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提供了合理 QA 建议和证据清单，但未明确单一 specialist 路由及其责任边界。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
