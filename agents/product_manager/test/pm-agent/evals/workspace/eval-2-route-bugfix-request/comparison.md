# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-002-route-bugfix-request`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-2-route-bugfix-request`.
- Identity schema: `2`
- target_skill_sha256: `6f8f132bc1f6eba3f9eb10727126ee30960b503351486b4fb6204e20571ffb35`
- eval_definition_sha256: `fe6d213ce4edb254dae39c5fefca87002824c8356e6ca05dfa6b8b92c57d378d`
- metadata_sha256: `163386e80d321ea48ddfd244853e278bc70ea13a08cdc68ac01f85bf3ba7240f`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `00a01c5f9432a18e723abe9a7b1a555e5a2a41dc2c36a101ed91497434d1c7f4`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `3622b3dfdb9bef50766ff22e70a5639483865b84fa39f8a64f027bc492debda1`
- Repository HEAD: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `6c6b79d36b8b3a1bf132fd82bfece3cf6e7b256e3a9a58a0cdb78f4a09e26e69`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `request_type_bug_report` | PASS | with_skill 输出明确包含 `request_type: bug_report`。 |
| `expectation_first` | NOT_EXERCISED | 工作区没有 approved PRD/TRD 或等价预期文档；候选正确报告缺失该依据并停止，因此未能实际 exercise 对照预期步骤。 |
| `debugger_handoff_after_confirmation` | NOT_EXERCISED | 未确认实现偏差，且输出明确禁止工程调试、代码修改和测试；后续 handoff 尚未发生。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3622b3dfdb9bef50766ff22e70a5639483865b84fa39f8a64f027bc492debda1; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=24b4b04abdada91c45454dccabd1353bff29f3e97ba65f465be82be060c49dd9; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别为 bug_report，发现缺少预期与实现证据后阻止 Engineer/debugger 执行，未发生越权修复或 handoff。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3622b3dfdb9bef50766ff22e70a5639483865b84fa39f8a64f027bc492debda1; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=fa8428a62b0a23f65218cc22b2930047d2cc9d775358386e949e523b694ba5d9; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 仅报告空仓库并请求补充源码，未进行请求分类或流程门控。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 补充 approved PRD/TRD 或等价产品预期、源码及错误日志后，再确认实现偏差并决定是否 handoff。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
