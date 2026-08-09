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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `d70112827b0542d867a7689306d190b9c9a901f0d16faf502ff69330466e810c`
- Skill overlay SHA-256: `738b2bf1d3ac1adbd5e2b7ad94592b274ea7b5d29a4ca3f3a5fc51fa86b342bc`
- Judge schema SHA-256: `f4aaec46995456a39da2b489696e387a78408415038edddd6412ca13bedbc20a`
- Eval definition SHA-256: `2ad0a90eac7fca1f06d238ff5d3d06535381ddd810d8a9e8e9e423ce29483f2c`
- Metadata SHA-256: `718fcc57ee1abd91d0d7551c46ebe8546481fa4f027452b86db232f30d15ab47`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | with_skill 选择 regression-suite，并以已实现登录刷新变更、现有 QA 资料及 WebKit 间歇性失败说明当前应走回归验证路径。 |
| `assertion_2` | PASS | with_skill 明确列出 PRD/TRD/实施计划、implementation changes、QA 测试资料、CI 日志、环境说明缺失项及 npm test -- login 执行入口。 |
| `specialist_gate_pointer` | PASS | with_skill 声明 regression-suite 为 execution_owner，并保留其 E2E memory、平台版本、凭据和 execution-entry gates 及结果产出责任。 |
| `assertion_4` | PASS | with_skill 使用结构化 YAML 字段声明 accepted_test_basis、required_evidence、执行路径、风险/阻塞状态、evidence_confidence 和 release_recommendation，并要求逐 TC 结果及回归汇总报告。 |
| `assertion_5` | PASS | with_skill 只选择 regression-suite；将 WebKit 超时保留为主要风险和原始失败复核项，没有将其确认成产品 bug。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d32b34f557a9af42827fae115c24f25ec47fe1e0fcda62e092dc3afa3789c767; fixture_sha256=c9268123afd7a11d5bd4ac6d14865261ea2db8883ff6a745cea96f843ec5dbd5; output_sha256=d629b9bd7586bdf25f4e9a1362275b55520565bfdee5f4d0064f652875487810; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 选择 regression-suite，明确下游门禁、输入资料、阻塞条件和预期证据，未执行多个下游 skill，也未确认间歇性失败为 bug。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d32b34f557a9af42827fae115c24f25ec47fe1e0fcda62e092dc3afa3789c767; fixture_sha256=c9268123afd7a11d5bd4ac6d14865261ea2db8883ff6a745cea96f843ec5dbd5; output_sha256=11d0226cd7f91ca679c66dae460065a8d4ab16e66468716c9ef2fc6d2c997bf9; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 给出较完整的验收阻断和重跑建议，但未形成明确的 specialist 路由、下游上下文清单或 specialist 执行责任指针。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
