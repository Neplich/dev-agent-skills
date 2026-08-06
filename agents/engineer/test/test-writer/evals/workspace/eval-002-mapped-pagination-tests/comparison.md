# Eval Result: eval-002-mapped-pagination-tests

## Evaluation Target

- Agent: `engineer`
- Skill: `test-writer`
- Eval: `eval-002-mapped-pagination-tests`
- Test case: mapped-pagination-tests
- Workspace: `workspace/eval-002-mapped-pagination-tests`
- Evaluation date: 2026-08-07
- Overall result: PASS
- Behavior result: PASS
- Coverage result: FULL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: 请为 `src/pagination/` 的边界行为设计并编写测试，先核对当前默认页大小。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- PASS `reads_mapped_docs_first`: transcript item_2 先读取 change-map.yaml，随后读取 docs/site/api/pagination.md；未读取无关文档内容。
- PASS `verifies_against_code`: transcript item_2/item_3 读取并确认 src/pagination/defaults.txt 为 25，识别文档 50 的冲突；最终测试断言默认值为 25。
- PASS `treats_unverified_as_low_trust`: transcript item_2 读取消费契约及文档中的 last_verified_version: unverified；最终以代码值 25 而非文档值 50 编写测试。

## With Skill Behavior

final 报告默认值 25、最大值 100，新增 4 项测试并报告 4/4 通过。workspace 测试文件与 output.sha256 内容一致，exit_code 为 0。

## Without Skill Baseline

作为对照，without_skill 也读取了代码和文档并生成边界测试；不影响 with_skill 判定。

## Failures / Findings

- None.
- Root cause: None.

## Next Steps

- 后续修改该 skill、fixture 或 assertions 时，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

# Consumption Regression Comparison

## Evaluation Target

- Skill: `test-writer`
- Eval: `eval-002-mapped-pagination-tests`

## Test Set / Fixture Version

- Fixture: `ws1-consumption-v1`
- Commit: `0b000b9`

## Latest Result

- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。

**PASS** — with-skill 以代码事实 25 为测试基准，拒绝采用 unverified 文档声明的 50，且不臆造缺失运行时的边界行为测试。

## With-Skill Behavior

- 命中映射文档后核证默认值，测试锚定代码事实并显式记录文档不一致。
- 对无实现证据的边界行为（0、101 的截断/报错）明确不臆造，保持证据边界。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 或消费契约提示。
- baseline 停在'以哪个值为准'的询问上未产出测试；行为稳妥但未按契约以代码为 ground truth 直接推进可交付产物。

## Failures

- 无。

## Next Steps

- 保留本结果；后续 fixture 可增加干扰文档以放大行为差距。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
