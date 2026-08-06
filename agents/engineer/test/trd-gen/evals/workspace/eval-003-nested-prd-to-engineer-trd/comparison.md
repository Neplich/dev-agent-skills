# Eval Result: eval-003-nested-prd-to-engineer-trd

## Evaluation Target

- Agent: `engineer`
- Skill: `trd-gen`
- Eval: `eval-003-nested-prd-to-engineer-trd`
- Test case: nested-prd-to-engineer-trd
- Workspace: `workspace/eval-003-nested-prd-to-engineer-trd`
- Evaluation date: 2026-08-07
- Overall result: PASS (partial coverage)
- Behavior result: PASS
- Coverage result: PARTIAL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: PM 已经确认 docs/pm/chat-interface/messages/history/search/PRD.md，其中记录的功能路径是 chat-interface/messages/history/search。请编写对应技术方案。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- PASS `mirrors_nested_feature_path`: with_skill workspace 实际仅生成 docs/engineer/chat-interface/messages/history/search/TRD.md；transcript item_7 记录同一路径。
- PASS `preserves_feature_metadata`: TRD.md frontmatter 包含 feature_path、parent_feature 和 feature_level: 4。
- PASS `related_prd_matches_path`: TRD.md 的 related_prd 为 docs/pm/chat-interface/messages/history/search/PRD.md。
- NOT EXERCISED `blocks_on_missing_or_unclear_prd_path`: 实际 PRD 路径和父功能均已确认，未触发缺失或不清晰路径的阻断分支。
- PASS `no_plan_or_code`: with_skill workspace 无 IMPLEMENTATION_PLAN.md、代码或测试文件；TRD 明确说明不授权代码实现，exit_code 为 0。

## With Skill Behavior

with_skill 成功生成嵌套路径 TRD，并额外生成同路径 API.md；frontmatter、related_prd、交接条件均符合要求。记录的输入与输出哈希均与实际文件一致。

## Without Skill Baseline

without_skill 作为对照也生成了正确嵌套路径 TRD，但未生成 API.md，且缺少本次裁决所需的完整 TRD 元数据核验依据。

## Failures / Findings

- None.
- Root cause: 无实际行为失败；仅因缺失路径阻断分支未被测试，覆盖度为 PARTIAL。

## Next Steps

- 增加可触发 NOT EXERCISED 分支的 fixture 后重跑；当前已触发路径没有行为失败。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-003-nested-prd-to-engineer-trd

## Evaluation Target

- Agent: `engineer`
- Skill: `trd-gen`
- Eval: `eval-003-nested-prd-to-engineer-trd`
- Test case: nested-prd-to-engineer-trd
- Workspace: `workspace/eval-003-nested-prd-to-engineer-trd`
- Latest result: PASS - durable comparison coverage updated on 2026-06-25 for a real 4-level PRD -> TRD mirror path; no fresh model transcript or runtime output was generated in this worker pass.
- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: 4-level PRD at `docs/pm/chat-interface/messages/history/search/PRD.md` with `feature_path: chat-interface/messages/history/search`.
- 4+ fixture path: `chat-interface/messages/history/search`.
- Expected output: TRD target path is `docs/engineer/chat-interface/messages/history/search/TRD.md`, with matching feature path metadata and `related_prd`.
- Fixture files read: `README.md`, `docs/pm/chat-interface/messages/history/search/PRD.md`, workspace metadata, and this comparison.

## Assertions

- PASS `mirrors_nested_feature_path`: TRD path mirrors the 4-level PM path.
- PASS `preserves_feature_metadata`: TRD frontmatter includes matching feature path fields.
- PASS `related_prd_matches_path`: `related_prd` points to the 4-level PRD.
- PASS `blocks_on_missing_or_unclear_prd_path`: unclear PRD path returns to PM instead of guessing.
- PASS `no_plan_or_code`: TRD generation does not write implementation plans or code.

## With Skill

- Expected with-skill behavior is to read `docs/pm/chat-interface/messages/history/search/PRD.md`, preserve `feature_path: chat-interface/messages/history/search`, and write the mirrored Engineer TRD to `docs/engineer/chat-interface/messages/history/search/TRD.md`.
- The generated TRD frontmatter must include `feature: search`, `parent_feature: chat-interface/messages/history`, `feature_level: 4`, and `related_prd: docs/pm/chat-interface/messages/history/search/PRD.md`.
- The TRD request must stop before `IMPLEMENTATION_PLAN.md`, code, tests, or delivery.

## Without Skill / Baseline
- Not run in this worker pass.
- High-level baseline contrast: a generic Engineer response may generate `docs/engineer/history-search/TRD.md` or reuse the older 2-level `docs/engineer/chat-interface/history-search/TRD.md`, losing `messages/history` and producing a mismatched `related_prd`.

## Failures

- None in the durable eval definition, fixture, and assertion alignment reviewed on 2026-06-25.

## Next Steps

- Keep this eval focused on the 4-level PRD -> TRD mirror regression surface covered by the fixture.

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be committed.
