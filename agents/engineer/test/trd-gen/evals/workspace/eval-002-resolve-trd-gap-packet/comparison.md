# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `trd-gen`
- Eval: `eval-002-resolve-trd-gap-packet`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `d58240709fd95e80376991be4d5ae0d8785faa7c898ac347279a20ad514acd7a` from `agents/engineer/test/trd-gen/evals/workspace/eval-002-resolve-trd-gap-packet`.
- Fixture SHA-256: `d58240709fd95e80376991be4d5ae0d8785faa7c898ac347279a20ad514acd7a`
- Prompt SHA-256: `bc732b2f79cac8748a3ffddfa2548eb3ee6c28a29e001f66a5d7af673ecfa482`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b66f9acea93e151819a21f82909f9a6b7d44c68fa52d2116667525e2fe8e9bd7`
- Skill overlay SHA-256: `e4cc003a0e06320ef354c6c9cdbebb2b75980ec8b23ae530ac78b0667fab31da`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `96fd70658261e3a17be616b06efc13bb061ebd641ee5ed5f4b30d21e34984bf7`
- Metadata SHA-256: `4025e3b1dd282f00d05c7506655215876b7bcc3af8d7657c77ae8574687fce25`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_gap_packet_as_trd_work` | FAIL | with_skill 输出未明确说明这是 trd-gen 的 TRD 编写/更新工作；仅称已补齐技术方案并提到下一步交给 feature-implementor。 |
| `resolves_named_gap_categories` | PASS | with_skill 交付的 TRD/API/ADR 覆盖组件职责、事件与幂等、API/集成影响、验证命令、发布回滚、错误处理、死信、可观测性和组织隔离。 |
| `keeps_finder_trd_gen_boundary` | FAIL | with_skill 输出及交付文档未明确说明发现者负责报告缺口、trd-gen 负责补全 docs/engineer/capture-loop/TRD.md 或记录 open questions。 |
| `unresolved_gap_blocks_e2e` | FAIL | 文档仍包含 open technical questions，并明确建议交给 feature-implementor 编写 IMPLEMENTATION_PLAN.md；未声明 feature-implementor、debugger 或 QA E2E 文档补充应 blocked。 |
| `no_implementation_plan_or_code` | PASS | with_skill 未新增 IMPLEMENTATION_PLAN.md、未修改业务代码、未补测试；新增的是 TRD、API 和 ADR 文档。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=bc732b2f79cac8748a3ffddfa2548eb3ee6c28a29e001f66a5d7af673ecfa482; fixture_sha256=d58240709fd95e80376991be4d5ae0d8785faa7c898ac347279a20ad514acd7a; output_sha256=5a19a05ad509b60f957a23a98bbe1961a5641a2fe419a0a0983f3ac5c0b7338d; snapshot_sha256=d2b263b3b7750f2fe8af47869b59cf43caea9a38250ecc75fc89d87713fd0b80
- Behavior: 新增 TRD/API/ADR 并覆盖主要技术缺口，保持未改代码，但遗漏 trd-gen 边界和未决缺口阻断要求。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=bc732b2f79cac8748a3ffddfa2548eb3ee6c28a29e001f66a5d7af673ecfa482; fixture_sha256=d58240709fd95e80376991be4d5ae0d8785faa7c898ac347279a20ad514acd7a; output_sha256=a657de9c9b37fddffe15783d40c8d329d4b9985d5b398d182c3dce5beb7e68f1; snapshot_sha256=fe5a14f0830a2a61c30cebf9aeb9308560bf12295a7e074fbda4f8d4a517b2ad
- Behavior: 直接改写 TRD_GAP_PACKET.md，覆盖技术缺口，但未提供 trd-gen 边界或下游阻断说明。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- 未明确声明 trd-gen 的 TRD 工作边界。
- 未明确区分发现者与 trd-gen 的职责。
- 未对仍存在的 open questions 设置 feature-implementor/debugger/QA E2E 阻断。
- Next: 明确写出 trd-gen 工作性质及发现者/trd-gen 边界。
- Next: 将未决技术问题标为 open questions，并阻断 IMPLEMENTATION_PLAN.md、debugger 和 QA E2E 文档补充，直至决策完成。

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

# Eval Result: eval-002-resolve-trd-gap-packet

## Evaluation Target

- Agent: `engineer`
- Skill: `trd-gen`
- Eval: `eval-002-resolve-trd-gap-packet`
- Test case: resolve-trd-gap-packet
- Workspace: `workspace/eval-002-resolve-trd-gap-packet`
- Evaluation date: 2026-08-07
- Overall result: PASS
- Behavior result: PASS
- Coverage result: FULL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: workspace `TRD_GAP_PACKET.md` 记录了当前缺少的技术决策，PM 的 docs/pm/capture-loop/PRD.md 已确认。请补齐技术方案。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- PASS `accepts_gap_packet_as_trd_work`: Transcript states entering Engineer TRD stage and updating docs/engineer/capture-loop/TRD.md; final says handoff occurs only after confirmation.
- PASS `resolves_named_gap_categories`: TRD documents components, data flow and envelope, validation command, rollout/rollback, error handling, observability, and security.
- PASS `keeps_finder_trd_gen_boundary`: Gap packet and AGENTS.md state finder reports gaps while trd-gen owns the Engineer document; transcript follows this boundary.
- PASS `unresolved_gap_blocks_e2e`: TRD records open questions and explicitly keeps implementation, debugger, and QA E2E updates blocked until confirmation.
- PASS `no_implementation_plan_or_code`: Only TRD.md was added; source-file hashes are unchanged, no IMPLEMENTATION_PLAN.md exists, and tests were not run.

## With Skill Behavior

With-skill final and transcript show TRD gap resolution. Workspace TRD exists, covers all named gaps, records open questions, and preserves implementation boundaries. Runtime exited 0 and output hashes match workspace files.

## Without Skill Baseline

Without-skill produced a comparable TRD artifact and exited 0; it is used only as contrast and does not determine the with-skill judgment.

## Failures / Findings

- None.
- Root cause: None.

## Next Steps

- 后续修改该 skill、fixture 或 assertions 时，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-002-resolve-trd-gap-packet

## Evaluation Target

- Agent: `engineer`
- Skill: `trd-gen`
- Eval: `eval-002-resolve-trd-gap-packet`
- Test case: resolve-trd-gap-packet
- Workspace: `workspace/eval-002-resolve-trd-gap-packet`
- Latest result: PASS - 2026-07-26 fresh paired validation completed; with_skill and fresh without_skill both satisfied 5/5 assertions.
- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: confirmed PRD, explicit TRD gap packet, and minimal capture/queue code evidence
- Expected output: 确认发现者负责说明缺口，trd-gen 负责补完整 docs/engineer/capture-loop/TRD.md；逐项处理 gap packet 中的组件、数据流、验证命令、发布风险和错误处理策略，不进入实现计划或代码。

## Assertions

- PASS `accepts_gap_packet_as_trd_work`: 将 gap packet 识别为 TRD 补全，不是实现任务。
- PASS `resolves_named_gap_categories`: 覆盖组件、数据流、验证、发布/回滚、错误、可观测性和安全。
- PASS `keeps_finder_trd_gen_boundary`: 保持 finder 与 trd-gen 的职责边界。
- PASS `unresolved_gap_blocks_e2e`: 未决 gap 阻断 plan、debugger 和 QA E2E。
- PASS `no_implementation_plan_or_code`: 没有进入计划或代码实现。

## With Skill

- 逐项处理 gap packet，并识别 `maxAttempts=3` 与 `[5,30,120]` 的语义歧义，记录 Queue owner 与 unblock condition。

## Without Skill / Baseline

- 2026-07-26 使用同一 prompt 和 fixture 重新生成 fresh baseline，未读取或应用 trd-gen skill、Agent README、历史 comparison 或旧 baseline。
- baseline 同样满足 5/5 assertions，但静默选择 retry 语义，没有显式记录该冲突的 owner 与 unblock condition。

## Failures

- 无 assertion failure。
- 当前 assertions 没有捕获“保留未决技术语义”这一产物质量增益。

## Next Steps

- 保留 gap 分类、角色边界和阻断门禁；后续可单独评估是否增强 open-question 断言。

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, generated TRD, outputs, and diagnostics were kept only in an ignored scratch workspace and are not committed.
