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
- target_skill_sha256: `ed93e443692bf05e76aaa38c8a5b8faff57190219ed48b9335316584424e6eb9`
- eval_definition_sha256: `f60ba5f87c066f48ffe21c8bbf0d933ae8b1ea45687ee0ce3091684db29e3750`
- metadata_sha256: `6cfa251efb3ddd0fc9104e40cad56a0dd759fb7068ac87a40ec1d705be391717`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `00a01c5f9432a18e723abe9a7b1a555e5a2a41dc2c36a101ed91497434d1c7f4`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `3622b3dfdb9bef50766ff22e70a5639483865b84fa39f8a64f027bc492debda1`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `67e6ae6bfee138166b25d903bb8ed5fced4658c060c4a43be1e074d3795bfaaa`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `request_type_bug_report` | PASS | With_skill 的 PM checkpoint 明确写出 `request_type: bug_report`，且没有直接进入修复。 |
| `expectation_first` | NOT_EXERCISED | 工作区没有应用源码或 PRD/TRD；with_skill 明确记录 `source_documents: []`、预期行为尚缺文档依据并将入口置为 blocked。因此该确认步骤因缺少运行时证据未被实际执行。 |
| `debugger_handoff_after_confirmation` | NOT_EXERCISED | with_skill 设置 `confirmation_required: true` 并停留在 PM/idea-to-spec，未 handoff 给 Engineer/debugger；由于实现偏差尚未确认，该后续步骤未被执行。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3622b3dfdb9bef50766ff22e70a5639483865b84fa39f8a64f027bc492debda1; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=cb03d98223b08949d9ee04c8ca308d954d83dd603127b9f4a9a856bf713c6728; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别为 bug_report，并在缺少代码与产品预期证据时停留在 PM 阻塞状态，未错误进入实现或 debugger handoff。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3622b3dfdb9bef50766ff22e70a5639483865b84fa39f8a64f027bc492debda1; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=41f5936a88db7fb4b97ea9ec2c994631c18e6334506f9fe03d8d1f3b4582b47a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 仅识别为空仓库并阻塞，trace 中一度直接计划定位、修复和测试，未体现 PM 分类与预期确认门槛。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 提供或恢复应用源码及 approved PRD/TRD 或等价预期证据。
- Next: 确认 token 过期时请求应结束并退出登录页加载态后，再 handoff 给 Engineer/debugger。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
