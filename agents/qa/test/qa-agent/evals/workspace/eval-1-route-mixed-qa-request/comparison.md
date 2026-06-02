# Eval Result: eval-001-route-mixed-qa-request

## Evaluation Target

- Agent: `qa`
- Skill: `qa-agent`
- Eval: `eval-001-route-mixed-qa-request`
- Test case: route-mixed-qa-request
- Workspace: `workspace/eval-1-route-mixed-qa-request`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-06-02

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Verifies that qa-agent handles route-mixed-qa-request and produces the expected role-specific artifact.
- Expected output: QA 路由决策，明确选择最窄的下游 QA skill、选择理由、需要读取的上下文和预期 evidence artifact

## Assertions

- `assertion_1`: 路由选择
- `assertion_2`: 上下文传递
- `qa`: QA 用例记忆
- `assertion_4`: 结构化产物
- `assertion_5`: 边界控制

## With Skill

Observed behavior:

- 当前 dispatcher 要求先路由、选择一个最窄主 route、携带 PM/spec、实现变更、CI 失败信息和测试命令；对 mixed request，主 route 应为 spec-based-tester 用于验收判断，intermittent CI failure 应作为 risk note 或 potential bug-analyzer follow-up，不能直接执行测试或写 confirmed bug。

## Without Skill / Baseline

- Baseline behavior is diagnostic only.
- This comparison records whether the skill-specific protocol, routing, evidence, or artifact expectations are preserved.

## Failures

- None found in fresh Codex subagent validation.

## Next Steps

- 保持主 route 为 spec-based-tester 的结论。

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be committed.
