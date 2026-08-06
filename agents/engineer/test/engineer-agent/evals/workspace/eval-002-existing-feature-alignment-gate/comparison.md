# Eval Result: eval-002-existing-feature-alignment-gate

## Evaluation Target

- Agent: `engineer`
- Skill: `engineer-agent`
- Eval: `eval-002-existing-feature-alignment-gate`
- Test case: existing-feature-alignment-gate
- Workspace: `workspace/eval-002-existing-feature-alignment-gate`
- Evaluation date: 2026-08-07
- Overall result: FAIL
- Behavior result: FAIL
- Coverage result: PARTIAL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: 用户说：现有通知中心已经有 PRD/TRD，现在想把 archived 通知也显示在 active 列表里，这是一个小改动，直接走工程实现吧。先做工程路由，不要改代码。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- FAIL `reads_product_and_engineer_docs`: with_skill transcript 仅可见读取 AGENTS.md 与共享 skill 文件；final 未明确要求先读取 PRD.md、TRD.md 及存在的 DECISIONS.md/产品决策记录。
- FAIL `classifies_expectation_change`: final 仅称范围、feature path 和验收预期未具备依据，未判断 archived 进入 active 可能改变已批准预期。
- FAIL `routes_to_existing_project_update`: final 写的是泛化的 pm-agent（补齐/确认 existing-update handoff），未明确路由到 pm-agent:idea-to-spec 的 existing-project-update 路径。
- NOT EXERCISED `routes_trd_gap_to_trd_gen`: PRD、产品决策与 TRD 均未在 workspace 中出现，无法观测到“PRD/决策已明确但 TRD 缺失或过期”的条件。
- FAIL `requires_plan_after_alignment`: final 后续指向 feature-implementor，但未要求对齐完成后先产出或引用已确认的 IMPLEMENTATION_PLAN.md。
- PASS `does_not_route_directly_to_implementation`: final 明确写“当前不能直接路由到 feature-implementor”，并要求 PM 先补齐/确认材料；transcript 无代码写入操作。

## With Skill Behavior

with_skill 正确停在门禁处且未改代码，但缺少对 archived 行为预期变更的明确分类、精确 existing-project-update 路由、文档读取要求和实施计划要求。workspace 仅有 AGENTS.md 与三个共享文件；exit_code 为 0，最终产物哈希文件存在但记录的是 fixture workspace 文件哈希。

## Without Skill Baseline

without_skill 仅观测到列举空 workspace，随后请求用户确认代码是否挂载；未作工程路由判断。其 workspace 无文件，exit_code 为 0，input/output 哈希文件为空。仅作对照，不影响 with_skill 判定。

## Failures / Findings

- reads_product_and_engineer_docs
- classifies_expectation_change
- routes_to_existing_project_update
- requires_plan_after_alignment
- Root cause: with_skill 虽识别到工程门禁未满足并停止实现，但没有按断言明确表达既有预期变更、PM existing-project-update 精确路径及对齐后的 IMPLEMENTATION_PLAN.md 门禁。

## Next Steps

- 修复上述 assertion 对应的 skill 行为或 eval 输入问题后，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-002-existing-feature-alignment-gate

## Evaluation Target

- Agent: `engineer`
- Skill: `engineer-agent`
- Eval: `eval-002-existing-feature-alignment-gate`
- Test case: existing-feature-alignment-gate
- Workspace: `workspace/eval-002-existing-feature-alignment-gate`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: small existing-feature behavior change request for Notification Center archived items.
- Fresh validation date: 2026-08-01.
- With-skill source: current Engineer README, current `engineer-agent` SKILL, eval definition, and workspace metadata.
- Without-skill source: the same prompt and fixture, freshly regenerated without reading or applying the target README/SKILL, with-skill output, historical comparison, or prior baseline.

## Latest Result

- Behavior result: PASS
- Coverage result: FULL
Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


All 6 assertions were exercised and passed in the with-skill run.

## Assertions

- PASS `reads_product_and_engineer_docs`: requires the same-feature PRD, TRD, and present decision records.
- PASS `classifies_expectation_change`: treats archived entries in active as a possible approved-expectation change.
- PASS `routes_to_existing_project_update`: sends conflicts to `pm-agent:idea-to-spec` through `existing-project-update`.
- PASS `routes_trd_gap_to_trd_gen`: constructs a gap packet for missing, stale, or incomplete TRD coverage and sends it to `trd-gen`.
- PASS `requires_plan_after_alignment`: preserves the confirmed implementation-plan gate after alignment.
- PASS `does_not_route_directly_to_implementation`: does not accept “small change” as permission to bypass alignment.

## With Skill Behavior

The fresh route blocks direct implementation until PRD, TRD, and decision records establish expected behavior. It distinguishes a PM expectation conflict from a TRD gap and keeps `feature-implementor` behind the confirmed implementation-plan gate.

## Without Skill Baseline

The fresh baseline routes directly to implementation and only suggests optional product confirmation. It omits the required document reads, named PM update lane, TRD gap packet/specialist, and confirmed implementation-plan gate. Baseline assertion result: 0/6.

## Failures

- None.

## Next Steps

- Keep this eval as regression coverage for existing-feature alignment and attempts to bypass PM/TRD gates.

## Runtime Artifacts Policy

- Fresh runtime evidence is under `tmp/eval-runs/issue-196-project-bootstrap-removal-20260801-131022/engineer-agent/eval-002-existing-feature-alignment-gate/`.
- `with_skill.md`, `without_skill.md`, and `verdict.md` are scratch evidence and must not be committed.
- This `comparison.md` is the only durable result.
