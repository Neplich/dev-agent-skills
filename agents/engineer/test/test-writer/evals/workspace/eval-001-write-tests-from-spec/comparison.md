# Eval Result: eval-001-write-tests-from-spec

## Evaluation Target

- Agent: `engineer`
- Skill: `test-writer`
- Eval: `eval-001-write-tests-from-spec`
- Test case: write-tests-from-spec
- Workspace: `workspace/eval-001-write-tests-from-spec`
- Evaluation date: 2026-08-07
- Overall result: PASS
- Behavior result: PASS
- Coverage result: FULL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: 根据 docs/test-spec.md 为 NotificationService 编写测试
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- PASS `test_spec`: 实际读取 Test Spec 与新增测试文件：4 个必需场景均有对应测试，且验证成功结果、错误消息、仓库未调用及错误对象原样透传。
- PASS `assertion_2`: with_skill transcript 记录执行新增测试及 npm test，结果为 5 tests、5 pass、0 fail；exit_code 为 0。
- PASS `assertion_3`: 新增文件为 test/services/notification-service.test.js，使用 node:test、node:assert/strict 和现有扁平 test() 结构，符合项目模式。

## With Skill Behavior

新增测试文件实际存在并覆盖全部 4 个规范场景；workspace 文件哈希与 output.sha256 一致；JSONL transcript 有效；测试报告 5/5 通过。

## Without Skill Baseline

作为对照，without_skill 也实际生成同名测试文件并记录 5/5 通过；其 workspace 哈希与 output.sha256 一致。

## Failures / Findings

- None.
- Root cause: None.

## Next Steps

- 后续修改该 skill、fixture 或 assertions 时，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-001-write-tests-from-spec

## Evaluation Target

- Agent: `engineer`
- Skill: `test-writer`
- Eval: `eval-001-write-tests-from-spec`
- Test case: write-tests-from-spec
- Workspace: `workspace/eval-001-write-tests-from-spec`
- Latest result: PASS - 2026-07-26 fresh paired validation completed; with_skill and fresh without_skill both satisfied 3/3 assertions.
- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: approved test spec, implementation code, existing test pattern, and runnable package scripts
- Expected output: 测试文件 + 测试运行结果

## Assertions

- PASS `test_spec`: with_skill 覆盖 test spec 的 4/4 场景，包括不调用 repository 与保留错误 identity。
- PASS `assertion_2`: `npm test` 报告 5 passed、0 failed。
- PASS `assertion_3`: 使用现有 `test/services/*.test.js`、`node:test` 和 `node:assert/strict` 规范。

## With Skill

- 新增与现有模式一致的 notification service 测试，明确记录 spec 场景到测试的追踪关系。

## Without Skill / Baseline

- 2026-07-26 使用同一 prompt 和 fixture 重新生成 fresh baseline，未读取或应用 test-writer skill、Agent README、历史 comparison 或旧 baseline。
- baseline 同样满足 3/3 assertions并通过相同测试命令；批准的 test spec 足够明确，因此没有 assertion-level 增益。

## Failures

- 无 assertion failure。

## Next Steps

- 保留 spec 全覆盖、真实运行和项目规范三项门禁。

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics were generated only in an ignored scratch workspace and are not committed.
