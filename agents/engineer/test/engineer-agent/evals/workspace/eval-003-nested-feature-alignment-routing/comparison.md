# Eval Result: eval-003-nested-feature-alignment-routing

## Evaluation Target

- Agent: `engineer`
- Skill: `engineer-agent`
- Eval: `eval-003-nested-feature-alignment-routing`
- Test case: nested-feature-alignment-routing
- Workspace: `workspace/eval-003-nested-feature-alignment-routing`
- Evaluation date: 2026-08-07
- Overall result: FAIL
- Behavior result: FAIL
- Coverage result: PARTIAL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: 用户说：Chat Interface 已经有 History Search 子功能 PRD/TRD，现在想调整搜索结果排序，这是个很小的现有功能改动。请先做工程路由，不要改代码。相关文档在 docs/pm/chat-interface/history-search/PRD.md 和 docs/engineer/chat-interface/history-search/TRD.md。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- PASS `resolves_nested_feature_path`: final 明确识别 `chat-interface/history-search`；with_skill transcript 实际读取了嵌套路径下的 PRD.md 与 TRD.md。
- PASS `does_not_use_sibling_or_parent_only_path`: transcript 与 final 均使用完整嵌套路径，未读取错误的 sibling 或 parent-only 路径。
- FAIL `routes_requirement_change_to_pm`: 排序调整属于已批准行为的变更，但 final 仍将目标技能写为 `engineer-agent:feature-implementor`，没有路由到 `pm-agent:idea-to-spec` 的 `existing-project-update`。
- NOT EXERCISED `routes_trd_mismatch_to_trd_gen`: 当前 TRD 存在、状态为 Approved，feature_path 与 related_prd 均匹配，未触发该条件。
- PASS `does_not_execute_directly`: workspace hash 与输入一致；无代码、IMPLEMENTATION_PLAN 或测试变更，transcript 也未显示执行测试。

## With Skill Behavior

解析并读取了正确的嵌套 PRD/TRD，且未修改 workspace；但在 alignment gate 未通过时仍指向 feature-implementor，缺少 PM existing-project-update 路由。

## Without Skill Baseline

正确识别并引用嵌套 PRD/TRD，未修改 workspace；仅作对照，不影响 with_skill 判定。

## Failures / Findings

- routes_requirement_change_to_pm：未路由到 `pm-agent:idea-to-spec` 的 `existing-project-update`。
- Root cause: with_skill 在已批准排序行为的变更尚未完成需求对齐时错误保留了 feature-implementor 路由。

## Next Steps

- 修复上述 assertion 对应的 skill 行为或 eval 输入问题后，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-003-nested-feature-alignment-routing

## Evaluation Target

- Agent: `engineer`
- Skill: `engineer-agent`
- Eval: `eval-003-nested-feature-alignment-routing`
- Test case: nested-feature-alignment-routing
- Workspace: `workspace/eval-003-nested-feature-alignment-routing`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: approved `chat-interface/history-search` PRD/TRD with a small search-ordering change.
- Fresh validation date: 2026-08-01.
- With-skill source: current Engineer README, current `engineer-agent` SKILL, eval definition, metadata, README, and same-path PRD/TRD.
- Without-skill source: the same prompt and fixture, freshly regenerated without reading or applying the target README/SKILL, with-skill output, historical comparison, or prior baseline.

## Latest Result

- Behavior result: PASS
- Coverage result: FULL
Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


All 5 assertions were exercised and passed in the with-skill run.

## Assertions

- PASS `resolves_nested_feature_path`: preserves `chat-interface/history-search` and reads its same-path PRD/TRD.
- PASS `does_not_use_sibling_or_parent_only_path`: does not collapse evidence to a sibling or parent-only path.
- PASS `routes_requirement_change_to_pm`: sends approved sorting changes to the PM `existing-project-update` lane.
- PASS `routes_trd_mismatch_to_trd_gen`: sends missing, stale, or path-mismatched TRDs to `engineer-agent:trd-gen`.
- PASS `does_not_execute_directly`: remains route-only.

## With Skill Behavior

The fresh route resolves the nested path, compares the explicit sorting contract, sends a changed expectation to PM, and sends technical freshness/path mismatches to `trd-gen`. It does not create a plan, edit code, or run tests.

## Without Skill Baseline

The fresh baseline preserves the exact nested paths, recognizes a possible product requirement change, and stays route-only. It does not name the required PM `existing-project-update` or `engineer-agent:trd-gen` routes. Baseline assertion result: 3/5.

## Failures

- None.

## Next Steps

- Keep this eval as regression coverage for nested feature-path resolution and same-path alignment.

## Runtime Artifacts Policy

- Fresh runtime evidence is under `tmp/eval-runs/issue-196-project-bootstrap-removal-20260801-131022/engineer-agent/eval-003-nested-feature-alignment-routing/`.
- `with_skill.md`, `without_skill.md`, and `verdict.md` are scratch evidence and must not be committed.
- This `comparison.md` is the only durable result.
