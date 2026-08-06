# Eval Result: eval-014-mapped-session-plan-evidence

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-014-mapped-session-plan-evidence`
- Test case: mapped-session-plan-evidence
- Workspace: `workspace/eval-014-mapped-session-plan-evidence`
- Evaluation date: 2026-08-07
- Overall result: PASS
- Behavior result: PASS
- Coverage result: FULL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: 请为 `src/session/` 增加会话续期，并先核对当前超时行为。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- PASS `reads_mapped_docs_first`: Transcript item_4 reads change-map.yaml, then mapped docs/site/api/session.md and src/session/config.txt; no full site-document traversal is evidenced.
- PASS `verifies_against_code`: Transcript and final identify config.txt as 30 minutes with renewal disabled, contrast it with the document's 60 minutes, and retain the conflict as an implementation blocker. With-skill workspace hashes match input hashes.
- PASS `treats_unverified_as_low_trust`: Both mapping and API documents state last_verified_version: unverified; the agent relies on config/code evidence, reports the discrepancy, and does not implement based on the document alone.

## With Skill Behavior

按映射读取 API 文档并回读代码配置，识别 30/60 分钟冲突；因缺少 PM/TRD 链未实施或写入计划。workspace 未变更，hash 与输入一致。

## Without Skill Baseline

未使用映射消费协议，直接修改 config.txt 与 API 文档，启用 renewal 并统一为 30 分钟；output hash 反映两文件变更。

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

- Skill: `feature-implementor`
- Eval: `eval-014-mapped-session-plan-evidence`

## Test Set / Fixture Version

- Fixture: `ws1-consumption-v1`
- Commit: `0b000b9`

## Latest Result

- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。

**PASS** — with-skill 以代码事实（30 分钟、续期禁用）核证出文档 60 分钟声明的分歧，PRD/TRD 前置门禁正确触发暂停，未在预期未对齐时编写实施计划。

## With-Skill Behavior

- 命中映射文档后回代码核证会话行为，结构化区分代码事实与文档声明。
- 变更按 standard 分级，正确停在 PM → trd-gen → 实施计划的协作链前置，未越权编码。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 或消费契约提示。
- baseline 同样停在门禁前请求预期确认，行为合规但对文档分歧的证据组织与契约引用较弱。

## Failures

- 无。

## Next Steps

- 保留本结果；后续 fixture 可增加干扰文档以放大行为差距。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
