# Eval Result: eval-001-route-implementation-chain

## Evaluation Target

- Agent: `engineer`
- Skill: `engineer-agent`
- Eval: `eval-001-route-implementation-chain`
- Test case: route-implementation-chain
- Workspace: `workspace/eval-1-route-implementation-chain`
- Evaluation date: 2026-08-07
- Overall result: FAIL
- Behavior result: FAIL
- Coverage result: FULL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: 用户说：请接手这个仓库，按 docs/engineer/billing-webhook/TRD.md 实现 webhook 重试逻辑，补测试，最后提交 PR。先做工程路由，不要直接改代码。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- PASS `starts_with_codebase_context`: with_skill final 明确将 codebase-analyzer 放在工程链首位；transcript 也先读取仓库文件、AGENTS.md、TRD 与源码说明。
- FAIL `routes_implementation_to_feature_implementor`: 虽列出 feature-implementor，但未说明其基于已确认 TRD、IMPLEMENTATION_PLAN.md 和现有代码执行；且当前明确因缺少 PRD/PM handoff 而阻塞。
- PASS `routes_tests_to_test_writer`: with_skill final 明确列出 codebase-analyzer → feature-implementor → test-writer → delivery，测试 route 未被省略。
- FAIL `routes_qa_e2e_handoff`: final 与 transcript 均未包含 QA E2E 文档补充检查或交接包，也未引用 PRD、确认的 IMPLEMENTATION_PLAN、变更文件、验证命令、风险及 docs/qa/e2e/{feature_path}。
- PASS `routes_delivery_last`: with_skill final 将 delivery 放在 feature-implementor 与 test-writer 之后。
- PASS `does_not_execute_directly`: transcript 明确只做路由判断；final 声明本轮未修改代码。workspace 文件与输入 hash 一致，未发现实现/测试/提交产物；exit_code 为 0。

## With Skill Behavior

明确识别缺少 PRD、PM handoff 和 Git 仓库，并停止直接执行；给出 codebase-analyzer、feature-implementor、test-writer、delivery 链。但缺少实现阶段所需 IMPLEMENTATION_PLAN 依据，也遗漏 QA E2E handoff。

## Without Skill Baseline

仅作对照：识别最小 fixture、缺少实际服务代码/测试/Git 元数据，并提出后续实现建议；未明确 specialist 路由链。

## Failures / Findings

- routes_implementation_to_feature_implementor：缺少基于已确认 TRD、IMPLEMENTATION_PLAN.md 与现有代码执行的明确说明。
- routes_qa_e2e_handoff：完全遗漏 QA E2E 文档补充检查及交接包要求。
- Root cause: with_skill 过早将缺少 PM 准入作为主要阻塞，并只输出简化的四段工程链；没有把 AGENTS.md 中实现计划前置要求和实现后 QA E2E safety-net closeout 纳入最终路由。

## Next Steps

- 修复上述 assertion 对应的 skill 行为或 eval 输入问题后，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-001-route-implementation-chain

## Evaluation Target

- Agent: `engineer`
- Skill: `engineer-agent`
- Eval: `eval-001-route-implementation-chain`
- Test case: route-implementation-chain
- Workspace: `workspace/eval-1-route-implementation-chain`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: existing billing webhook service with a TRD and route-only implementation, test, QA E2E handoff, and delivery request.
- Fixture version: current HEAD `a452319`.
- Fresh run time: `2026-08-03 11:58:13 +0800`.
- Runtime directory: `tmp/eval-runs/issue-198-brd/engineer/20260803-115813/engineer-agent/eval-001-route-implementation-chain/`.
- With-skill source: current Engineer README, current `engineer-agent` SKILL, eval definition, and fixture README, metadata, TRD, and code notes.
- Without-skill source: the same prompt and fixture, freshly regenerated this run without applying the target README/SKILL, with-skill output, historical comparison, or any prior baseline.

## Latest Result

- Behavior result: PASS
- Coverage result: FULL
Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


All 6 assertions were exercised and passed. Removing BRD from the planning-input wording did not change the engineering route, implementation-plan gate, QA E2E handoff, or delivery order.

## Assertion Results

- PASS `starts_with_codebase_context`: starts with `codebase-analyzer` for repository structure, stack, constraints, and existing patterns.
- PASS `routes_implementation_to_feature_implementor`: assigns implementation to `feature-implementor` after the confirmed PRD/TRD/implementation-scope entry gate and requires the implementation plan before code.
- PASS `routes_tests_to_test_writer`: keeps automated coverage in a distinct `test-writer` stage.
- PASS `routes_qa_e2e_handoff`: after implementation and deterministic tests, requires the PRD/TRD/confirmed-plan QA E2E handoff package, changed files, verification commands, risks, and suggested feature directory.
- PASS `routes_delivery_last`: leaves `delivery` after implementation, tests, and the QA handoff check.
- PASS `does_not_execute_directly`: performs route-only work and does not modify code, run tests, or create delivery artifacts.

## With-Skill Behavior

The fresh route starts with `codebase-analyzer`, preserves the specialist entry-basis check, then routes confirmed work through `feature-implementor`, `test-writer`, the QA E2E handoff check, and `delivery`. It identifies `docs/engineer/billing-webhook/IMPLEMENTATION_PLAN.md` as the pre-code gate and carries the complete QA package requirements. BRD is neither requested nor treated as a missing prerequisite; PRD, product decisions, TRD, and current implementation scope retain their existing responsibilities.

## Fresh Without-Skill Baseline

The without-skill baseline was newly generated in this run from the same prompt and fixture. It gives a generic inspect-implement-test-PR sequence and obeys the no-execution request, but it does not select the repository's named specialists, require a confirmed durable implementation plan, or include the QA E2E handoff package. Baseline assertion result: 1/6.

## Failures

- None.

## Next Steps

- Keep this eval as regression coverage for route-only implementation chains after BRD contract removal.

## Runtime Artifact Policy

- Fresh runtime evidence is under `tmp/eval-runs/issue-198-brd/engineer/20260803-115813/engineer-agent/eval-001-route-implementation-chain/`.
- `with_skill.md`, `without_skill.md`, and `verdict.md` are ignored scratch evidence and must not be committed.
- This `comparison.md` is the only durable result for this case.
