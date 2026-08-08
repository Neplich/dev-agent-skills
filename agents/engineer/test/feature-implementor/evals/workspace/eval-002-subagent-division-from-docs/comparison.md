# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-002-subagent-division-from-docs`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `8481ed80b8f086d56a7d099cb26476a4c1557eb2e668f63f4464955938246974` from `agents/engineer/test/feature-implementor/evals/workspace/eval-002-subagent-division-from-docs`.
- Fixture SHA-256: `8481ed80b8f086d56a7d099cb26476a4c1557eb2e668f63f4464955938246974`
- Prompt SHA-256: `6d68306ed0e21eb7949f908f4dc831f18272177bd88aed14ab9420f34207f51f`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5a3403ec360f8aca06dd1301fa3bfe0f2bd967f54afc7bad9b5691a78697b0ca`
- Skill overlay SHA-256: `5c74cbf7ab5eef845bc8c3f0d81a775b1feca5810a9a615f9b35865026f3e841`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `f4a3318c26964c6e50e73da4a0083b2eedeed8886d0685576f77ee1323f675a5`
- Metadata SHA-256: `0a81d92a9af555dbb300e83a7ff4d8024a21161273fe243a2bbb1dbd8da3747a`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_main_context` | FAIL | 未说明主进程保留仓库规则、实现边界及最终交付判断，也未明确主进程不吞并编码和验收细节。 |
| `writes_implementation_plan_doc` | FAIL | 虽提到稍后固化 IMPLEMENTATION_PLAN.md，但未安排文档编写 sub-agent，也未说明 TRD 不由 feature-implementor 改写。 |
| `delegates_implementation_scope` | FAIL | 列出了三个文件和范围约束，但未明确委派给实现 sub-agent。 |
| `delegates_independent_validation` | FAIL | 描述了验收侧检查，但未安排不同于实现 sub-agent 的独立验收 sub-agent。 |
| `keeps_simple_path_exception` | FAIL | 未保留简单单文件修改、纯解释或用户明确不拆分时的轻量路径例外。 |
| `final_summary_contract` | FAIL | 提到汇总测试结果和遗留风险，但未完整说明最终交付需包含实现结果、测试情况、验收结论和遗留风险。 |
| `qa_e2e_handoff_contract` | FAIL | 未说明形成 QA E2E 文档补充交接包，也未给出 docs/qa/e2e/{feature_path} 功能目录或所需内容。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6d68306ed0e21eb7949f908f4dc831f18272177bd88aed14ab9420f34207f51f; fixture_sha256=8481ed80b8f086d56a7d099cb26476a4c1557eb2e668f63f4464955938246974; output_sha256=194feb4ac09939ba258ef272b8fd6b1ac50f288ecda3e61fb0c82bb19f97c005; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提出了较清晰的三文件实现与验收范围，并要求先确认技术参数，但未满足所需的主进程、sub-agent、简单任务例外及 QA E2E 交接契约。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6d68306ed0e21eb7949f908f4dc831f18272177bd88aed14ab9420f34207f51f; fixture_sha256=8481ed80b8f086d56a7d099cb26476a4c1557eb2e668f63f4464955938246974; output_sha256=ccd0c58cc8e6cb205302737649a9b2b5bc16d5be42104b06c37c8bea611cb853; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提供了直接实现方案并将验收留给用户或评审人，未采用 sub-agent 分工和 QA E2E 交接约定。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足全部七项断言。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Migration Status

## Current Result

- Evidence status: **STALE**
- Migration status: **PENDING**
- Blocking reason: this eval has not yet been rerun under the Issue #246 scenario, lane-isolation, and fresh-judge contract.
Overall result: BLOCKED

## Historical Context (Superseded)

The complete pre-migration comparison follows unchanged. It is retained only as historical context and is not current release evidence.

---

# Eval Result: eval-002-subagent-division-from-docs

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-002-subagent-division-from-docs`
- Test case: subagent-division-from-docs
- Workspace: `workspace/eval-002-subagent-division-from-docs`
- Evaluation date: 2026-08-07
- Overall result: FAIL
- Behavior result: FAIL
- Coverage result: PARTIAL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: 请根据 docs/pm/capture-loop/PRD.md、docs/engineer/capture-loop/TRD.md 和 docs/design/capture-loop/ui-ux-spec.md 实现 Capture Loop 队列重试能力。现在进入编码阶段，需要先编写 docs/engineer/capture-loop/IMPLEMENTATION_PLAN.md，再说明如何安排实现与验收分工。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- NOT EXERCISED `preserves_main_context`: transcript 仅说明已读取文档并进入计划阶段，未形成要求的主进程职责说明。
- FAIL `writes_implementation_plan_doc`: with_skill/final.md 表明仍停在写入前询问 author；with_skill/workspace/docs/engineer/capture-loop/IMPLEMENTATION_PLAN.md 不存在。
- NOT EXERCISED `delegates_implementation_scope`: 未看到实际实现 sub-agent 分工输出。
- NOT EXERCISED `delegates_independent_validation`: 未看到实际独立验收 sub-agent 安排及验收依据输出。
- NOT EXERCISED `keeps_simple_path_exception`: 最终输出未说明简单任务例外。
- NOT EXERCISED `final_summary_contract`: 最终输出仅请求用户提供 author，未包含实现结果、测试情况、验收结论和遗留风险。
- NOT EXERCISED `qa_e2e_handoff_contract`: 未形成 QA E2E 交接包说明。

## With Skill Behavior

已读取 PRD、TRD、设计文档及规划规则；源文档和代码文件 hash 与 fixture 记录一致，且未改动业务文件。但在写入 IMPLEMENTATION_PLAN.md 前因 author 信息请求用户，最终未产出计划或分工交付。

## Without Skill Baseline

对照运行实际创建了 IMPLEMENTATION_PLAN.md，final/transcript 包含文件范围、实现方与独立验收方分工、测试矩阵和遗留风险；其输入/输出 hash 与 workspace 实际文件一致。

## Failures / Findings

- with_skill 未创建要求的 docs/engineer/capture-loop/IMPLEMENTATION_PLAN.md。
- with_skill final 未提供 expected_output 要求的分工、交付契约和 QA E2E 交接说明。
- Root cause: with_skill 在计划写入前将仓库规则中的 author 元数据要求升级为阻塞条件，因缺少用户显示名而停止；该阻塞不在用户请求中，导致核心计划和后续分工输出未发生。

## Next Steps

- 修复上述 assertion 对应的 skill 行为或 eval 输入问题后，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-002-subagent-division-from-docs

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-002-subagent-division-from-docs`
- Test case: subagent-division-from-docs
- Workspace: `workspace/eval-002-subagent-division-from-docs`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-05
- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture files read before skill use: `README.md`, `eval_metadata.json`, `docs/pm/capture-loop/PRD.md`, `docs/engineer/capture-loop/TRD.md`, `docs/design/capture-loop/ui-ux-spec.md`, `src/capture-loop/queue-service.ts`, `src/capture-loop/event-handler.ts`, and `tests/capture-loop/queue-service.test.ts`.
- Fixture summary: Capture Loop needs retry scheduling, bounded retries, and test coverage across `queue-service.ts`, `event-handler.ts`, and queue-service tests; the design file states there is no visual UI change.
- Expected output: preserve main-process context, write `docs/engineer/capture-loop/IMPLEMENTATION_PLAN.md` through a document-writing sub-agent, separate implementation and validation responsibilities for complex work, and include final delivery and QA E2E handoff expectations.

## Assertions

- PASS `preserves_main_context`: the skill keeps PRD/TRD/design docs, repo rules, implementation boundaries, final integration, and delivery risks in the main process.
- PASS `writes_implementation_plan_doc`: planner requires a fresh document-writing sub-agent when available and forbids rewriting TRD decisions in the implementation plan.
- PASS `delegates_implementation_scope`: planner and implementor require owned files/modules, source docs, tests, forbidden areas, and no unrelated reverts for implementation delegation.
- PASS `delegates_independent_validation`: reviewer requires a separate validation sub-agent for complex split work.
- PASS `keeps_simple_path_exception`: single-file small edits, pure explanation, code reading, or user opt-out can skip complex split only, not planning or confirmation.
- PASS `final_summary_contract`: implementor and reviewer collect changed files, verification results, open issues, findings, blockers, and residual risks.
- PASS `qa_e2e_handoff_contract`: closeout requires a QA E2E handoff package when user-facing flows, acceptance paths, permissions, login, data setup, or regression coverage may be affected.

## With Skill Behavior

Fresh with-skill validation read the public skill, Engineer README, planner, implementor, reviewer, coding rules, and output conventions. The PRD/TRD/design fixtures form an equivalent confirmed document chain, so the PM handoff gate is satisfied without weakening the direct specialist gate. The work is multi-file and spec-heavy, so the skill should keep the main process responsible for context and final judgment, delegate plan writing for `docs/engineer/capture-loop/IMPLEMENTATION_PLAN.md`, then use separate implementation and validation sub-agents after plan confirmation. The implementation scope should cover `src/capture-loop/queue-service.ts`, `src/capture-loop/event-handler.ts`, and `tests/capture-loop/queue-service.test.ts`, with no unrelated module changes.

## Without Skill Baseline

The fresh without-skill baseline was summarized before reading skill docs. A generic worker could read the PRD/TRD/source files and propose the same code edits, but it would likely collapse planning, implementation, and validation into one response or one agent. It would not reliably preserve the main-process context contract, require a document-writing sub-agent for the plan, assign a separate validation sub-agent, or produce the QA E2E handoff package after implementation.

## Failures

- None.

## Next Steps

- Keep this eval focused on complex spec-backed work where sub-agent splitting is valuable, while preserving the small-task exception.

## Runtime Artifacts Policy

- This validation did not create runtime artifacts.
- Runtime transcripts, verdicts, timing files, outputs, diagnostics, run status files, and `comparison.auto.md` must not be committed.
