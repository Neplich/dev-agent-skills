# Eval Result: eval-003-mapped-search-architecture

## Evaluation Target

- Agent: `engineer`
- Skill: `codebase-analyzer`
- Eval: `eval-003-mapped-search-architecture`
- Test case: mapped-search-architecture
- Workspace: `workspace/eval-003-mapped-search-architecture`
- Evaluation date: 2026-08-07
- Overall result: FAIL
- Behavior result: FAIL
- Coverage result: FULL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: 请分析 `src/search/` 的模块职责、请求流程和当前接口能力。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- FAIL `reads_mapped_docs_first`: with_skill transcript 中 item_2 先读取 agents/.../consumption-contract.md，再读取 docs/site/api/search.md；未满足命中 change-map 后首先读取映射 API 文档。
- PASS `verifies_against_code`: transcript item_2/item_4 实际读取并核查 src/search/query.txt；final.md 明确指出文档默认 fuzzy 与代码 match_mode: exact 的分歧及其影响（应以代码为准、文档需校准）。
- PASS `treats_unverified_as_low_trust`: 实际 docs/site/api/search.md 与 change-map.yaml 均含 last_verified_version: unverified；final.md 按最低信任处理文档，并以 query.txt 的代码事实核证职责、流程和能力。

## With Skill Behavior

with_skill 实际读取了 change-map、映射 API 文档和代码，并正确报告 fuzzy/exact 冲突；但命中 change-map 后先读取了 shared consumption-contract，未满足映射文档优先顺序。workspace hashes 与 input/output hashes 一致，未发生文件写入。

## Without Skill Baseline

without_skill 在同一 fixture 上读取了代码、API 文档和 change-map，最终也识别出 unverified 文档与 exact 代码的冲突；仅作为 baseline 对照，不影响单独 assertion 判定。其 workspace input/output hashes 一致，未发生文件写入。

## Failures / Findings

- reads_mapped_docs_first
- Root cause: with_skill 在确认 change-map 后先读取 shared consumption-contract 而非映射的 docs/site/api/search.md，导致文档优先读取断言失败。

## Next Steps

- 修复上述 assertion 对应的 skill 行为或 eval 输入问题后，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

# Consumption Regression Comparison

## Evaluation Target

- Skill: `codebase-analyzer`
- Eval: `eval-003-mapped-search-architecture`

## Test Set / Fixture Version

- Fixture: `ws1-consumption-v1`
- Commit: `0b000b9`

## Latest Result

- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。

**PASS** — with-skill 输出满足全部 3 条断言：命中 change-map 后以映射文档 `docs/site/api/search.md` 为地图、以 `src/search/query.txt` 为 ground truth 核证出"文档声称模糊匹配、代码只实现精确匹配"的分歧，并按 `unverified` 最低信任规则以代码为准。

## With-Skill Behavior

- 显式声明按 consumption contract 执行，只读取命中的映射文档，未做无关文档遍历。
- 产出契约要求的结构化分歧表（文档路径 / 文档声明 / 代码事实 / 影响），可直接供 `docs-audit` 消费。
- 对 `last_verified_version: unverified` 显式引用最低信任规则，全部关键能力结论以代码证据支撑，未证实项明确标注"无法确认"。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 或消费契约提示。
- baseline 也识别了模糊/精确匹配分歧并倾向以代码为准，但没有产出契约格式的结构化分歧证据，信任降级是临场推断而非协议行为。

## Failures

- 无。

## Next Steps

- 保留本结果；后续可在 fixture 中加入多个无关文档以放大"精准读取"与全库遍历的行为差距。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
