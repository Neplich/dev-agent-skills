# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `trd-gen`
- Eval: `eval-001-prd-to-engineer-trd`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `874c9a19c616d97ed625612e04c37ce561c010e8908c127503ea72d53817db55` from `agents/engineer/test/trd-gen/evals/workspace/eval-001-prd-to-engineer-trd`.
- Fixture SHA-256: `874c9a19c616d97ed625612e04c37ce561c010e8908c127503ea72d53817db55`
- Prompt SHA-256: `59315add19ee6ece2648d62000ea89257cb037f1973ece31adc62018b509f700`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `bb3f875298d7fef0fcd2297b4e59b33b5c034efad4a2286dcaede91ec0863c72`
- Skill overlay SHA-256: `12aaaef0d075d133bbbdc681f598fd09807b211a4377dcfbc6cbbfcaa30909e0`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `763059af120165947ccbb1397278bf0acb3f4c96fd42875970c4e31154f717da`
- Metadata SHA-256: `b33234ce56a0b715b632f392ff44ba7c27cad834dbc654110228254e610f01ec`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `engineer_owns_trd` | PASS | With-skill artifacts place TRD at docs/engineer/capture-loop/TRD.md and identify it as an Engineer TRD. |
| `prd_confirmed_handoff` | PASS | TRD states that the PRD and confirmed DECISIONS are prerequisites and that the workflow is entering the Engineer TRD stage. |
| `document_subagent` | FAIL | The with-skill output does not require TRD writing or updating to be performed by a document-writing sub-agent, nor state that the main process retains context and final review. |
| `implementation_plan_handoff` | PASS | The output and TRD state that after Engineer-document confirmation, feature-implementor writes IMPLEMENTATION_PLAN.md, with code implementation deferred until confirmation. |
| `qa_e2e_after_confirmed_plan` | FAIL | The with-skill output and artifacts do not describe the required QA E2E documentation handoff after confirmed TRD, confirmed implementation plan, and implementation completion. |
| `no_code_implementation` | PASS | The output explicitly says it did not enter code implementation; raw git evidence shows only untracked documentation artifacts and no code changes. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59315add19ee6ece2648d62000ea89257cb037f1973ece31adc62018b509f700; fixture_sha256=874c9a19c616d97ed625612e04c37ce561c010e8908c127503ea72d53817db55; output_sha256=af7a1e5a0eff728cfa3bc6d0a23b3a5d560b9b700f9632f864801dd4919537ab; snapshot_sha256=d5224ff90386d7d0faf0312f302dc441c9a0589e88a70d69c8871f6438aeb34c
- Behavior: Produced Engineer-scoped TRD/API documentation at docs/engineer/capture-loop, preserved the no-code boundary, and described implementation-plan handoff, but omitted document-subagent delegation and QA E2E handoff.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59315add19ee6ece2648d62000ea89257cb037f1973ece31adc62018b509f700; fixture_sha256=874c9a19c616d97ed625612e04c37ce561c010e8908c127503ea72d53817db55; output_sha256=2280be0b2a0dfadddc1949e11ad441e4952717974e8137e572b0b207a104ab4c; snapshot_sha256=18d280051eeb91ecef92688db092bdc289c6ed530f5e3a93e659d54a8b80c62e
- Behavior: Produced a TRD under docs/pm/... and did not establish the required Engineer ownership or downstream workflow.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- document_subagent: omitted required document-writing sub-agent delegation and main-process review responsibility.
- qa_e2e_after_confirmed_plan: omitted required post-implementation QA E2E documentation handoff conditions.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `trd-gen`
- Eval: `eval-001-prd-to-engineer-trd`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `874c9a19c616d97ed625612e04c37ce561c010e8908c127503ea72d53817db55` from `agents/engineer/test/trd-gen/evals/workspace/eval-001-prd-to-engineer-trd`.
- Fixture SHA-256: `874c9a19c616d97ed625612e04c37ce561c010e8908c127503ea72d53817db55`
- Prompt SHA-256: `59315add19ee6ece2648d62000ea89257cb037f1973ece31adc62018b509f700`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a696884cd8ec31e2137cab6da5326eb0f6fb0d49089fe5e32218dce4da5cdfee`
- Skill overlay SHA-256: `14328c4af5595e19e21331fb22dcc6dda56844ee6c4f2ee6382997e7ffe0af37`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `763059af120165947ccbb1397278bf0acb3f4c96fd42875970c4e31154f717da`
- Metadata SHA-256: `b33234ce56a0b715b632f392ff44ba7c27cad834dbc654110228254e610f01ec`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `engineer_owns_trd` | FAIL | 输出给出了 docs/engineer/capture-loop/TRD.md 和 Engineer 文档状态，但未明确说明 TRD 由 Engineer Agent 负责。 |
| `prd_confirmed_handoff` | FAIL | 输出提到 TRD 确认后移交，但未说明必须在 PRD、DECISIONS 或等价产品范围确认后才进入 TRD 阶段。 |
| `document_subagent` | FAIL | 输出和交付文档均未要求由文档编写 sub-agent 执行 TRD 编写或更新，并由主进程保留上下文和最终审查。 |
| `implementation_plan_handoff` | PASS | 输出明确说明 TRD 确认后移交 feature-implementor 编写 IMPLEMENTATION_PLAN.md，随后进入实现。 |
| `qa_e2e_after_confirmed_plan` | FAIL | 虽包含 E2E 测试内容，但未说明 QA E2E 文档补充依赖已确认 TRD、已确认 IMPLEMENTATION_PLAN、实现完成后的交接包，且不能由 TRD 请求直接触发。 |
| `no_code_implementation` | PASS | git_evidence 显示仅新增 Engineer 文档文件，未修改代码或测试；输出也未宣称已执行实现。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59315add19ee6ece2648d62000ea89257cb037f1973ece31adc62018b509f700; fixture_sha256=874c9a19c616d97ed625612e04c37ce561c010e8908c127503ea72d53817db55; output_sha256=a9a6bdda03cafa2dc10f17e56afc5da99bb7b185aa14a34d36018c2cfd18ed44; snapshot_sha256=fabe1bd1dfc59435d8acb9c8c002f6d446ceafb546a8c7e85fa5094c22839ffc
- Behavior: 输出了 docs/engineer/capture-loop/TRD.md、API.md 和 ADR，并明确 TRD 确认后移交 feature-implementor 编写 IMPLEMENTATION_PLAN.md；但缺少 Engineer Agent 责任、确认前置条件、文档 sub-agent 和受控 QA E2E 交接说明。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59315add19ee6ece2648d62000ea89257cb037f1973ece31adc62018b509f700; fixture_sha256=874c9a19c616d97ed625612e04c37ce561c010e8908c127503ea72d53817db55; output_sha256=c949838a6b4c808485afc989c676480ea0d64224ba720ab6ff0fe7cffa66ca30; snapshot_sha256=5813f97680621ba5f65494579a62525914769049bd3a027b0d379e56496a0ab4
- Behavior: 输出了 docs/pm/capture-loop/TRD.md，描述技术方案并声明未修改代码，但未遵循 Engineer 文档路径或后续交接流程。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- 未明确 TRD 由 Engineer Agent 负责。
- 未说明 PRD/DECISIONS 确认是进入 TRD 的前置条件。
- 未要求文档编写 sub-agent 执行 TRD 编写或更新。
- 未定义确认 TRD 与 IMPLEMENTATION_PLAN、实现完成后的 QA E2E 文档交接条件。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `trd-gen`
- Eval: `eval-001-prd-to-engineer-trd`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `874c9a19c616d97ed625612e04c37ce561c010e8908c127503ea72d53817db55` from `agents/engineer/test/trd-gen/evals/workspace/eval-001-prd-to-engineer-trd`.
- Fixture SHA-256: `874c9a19c616d97ed625612e04c37ce561c010e8908c127503ea72d53817db55`
- Prompt SHA-256: `59315add19ee6ece2648d62000ea89257cb037f1973ece31adc62018b509f700`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b66f9acea93e151819a21f82909f9a6b7d44c68fa52d2116667525e2fe8e9bd7`
- Skill overlay SHA-256: `e4cc003a0e06320ef354c6c9cdbebb2b75980ec8b23ae530ac78b0667fab31da`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `763059af120165947ccbb1397278bf0acb3f4c96fd42875970c4e31154f717da`
- Metadata SHA-256: `b33234ce56a0b715b632f392ff44ba7c27cad834dbc654110228254e610f01ec`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `engineer_owns_trd` | FAIL | with_skill 输出给出 docs/engineer/capture-loop/TRD.md 并提及 Engineer 文档，但未明确说明 TRD 由 Engineer Agent 负责。 |
| `prd_confirmed_handoff` | FAIL | with_skill 文档引用 PRD/DECISIONS 并要求维护者确认一致，但未明确说明仅在产品范围确认后才开始编写 TRD。 |
| `document_subagent` | FAIL | with_skill 输出和 TRD 未要求文档编写 sub-agent 执行 TRD 编写/更新，也未说明主进程保留上下文并进行最终审查。 |
| `implementation_plan_handoff` | PASS | 输出明确说明 TRD 确认后移交 feature-implementor，并指定 docs/engineer/capture-loop/IMPLEMENTATION_PLAN.md。 |
| `qa_e2e_after_confirmed_plan` | FAIL | with_skill 输出未说明 QA E2E 文档补充依赖已确认 TRD、已确认 IMPLEMENTATION_PLAN、实现完成及交接包，也未说明不能由 TRD 请求直接触发。 |
| `no_code_implementation` | PASS | TRD 明确列出不在本任务实现代码、API 客户端、数据库迁移或部署资源，输出也说明仅产出文档。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59315add19ee6ece2648d62000ea89257cb037f1973ece31adc62018b509f700; fixture_sha256=874c9a19c616d97ed625612e04c37ce561c010e8908c127503ea72d53817db55; output_sha256=3d4b7fd9bc9d3269acf08adb160079a27ad4c9990a2aa733ce91f645d23c0cdb; snapshot_sha256=b2a48f563e73d4103a4924c576c3b18f460e9e088e7936310e46d8a61e077ba3
- Behavior: 生成了 docs/engineer/capture-loop/TRD.md，包含 feature-implementor 交接和不实施代码约束，但缺少 Engineer Agent 归属、文档 sub-agent、确认前置条件及 QA E2E 交接链路。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59315add19ee6ece2648d62000ea89257cb037f1973ece31adc62018b509f700; fixture_sha256=874c9a19c616d97ed625612e04c37ce561c010e8908c127503ea72d53817db55; output_sha256=857dff0d4fa77bf39d3ab4efca108fd50f41748f91f3dfd58350492a16a74606; snapshot_sha256=d5ce8fcb55114f5af046e8eb3fd7544669c77af5ebb14784966197837626b9d8
- Behavior: 生成了 docs/pm/capture-loop/TRD.md，未采用 Engineer 文档路径或规定的交接流程。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill lane 未满足 4 项流程断言：Engineer Agent 归属、PRD/DECISIONS 确认前置、文档编写 sub-agent 委派、确认计划后的 QA E2E 交接。
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

# Eval Result: eval-001-prd-to-engineer-trd

## Evaluation Target

- Agent: `engineer`
- Skill: `trd-gen`
- Eval: `eval-001-prd-to-engineer-trd`
- Test case: prd-to-engineer-trd
- Workspace: `workspace/eval-001-prd-to-engineer-trd`
- Evaluation date: 2026-08-07
- Overall result: FAIL
- Behavior result: FAIL
- Coverage result: FULL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: PM 已经确认 docs/pm/capture-loop/PRD.md 和 docs/pm/capture-loop/DECISIONS.md。请准备这个功能的技术方案。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- PASS `engineer_owns_trd`: transcript 明确进入 Engineer TRD 阶段并指定 docs/engineer/{feature_path}/TRD.md；实际生成 TRD.md。
- PASS `prd_confirmed_handoff`: transcript 明确写出“PRD 已确认，当前进入 Engineer TRD 阶段”；实际读取并核对 PRD 与 DECISIONS。
- FAIL `document_subagent`: final、transcript 和生成文档均未要求由文档编写 sub-agent 执行并由主进程保留上下文和最终审查；不能据 AGENTS 指令推断实际委派。
- PASS `implementation_plan_handoff`: final 明确说明 TRD 确认后移交 feature-implementor 编写 IMPLEMENTATION_PLAN.md；TRD 第 11 节也明确该路径和前置确认条件。
- FAIL `qa_e2e_after_confirmed_plan`: final 和 TRD 未说明 QA E2E 文档补充必须依赖已确认 TRD、已确认 IMPLEMENTATION_PLAN 及实现完成后的交接包，也未说明不能由 TRD 请求直接触发。
- PASS `no_code_implementation`: final 明确“未进入代码实现”；workspace 实际仅新增 Engineer 文档，无 IMPLEMENTATION_PLAN 或代码文件。

## With Skill Behavior

with_skill exit_code 为 0；实际生成 TRD.md、API.md、ADR，且 PM 输入文件 hash 与记录一致，生成文件 hash 也与 output.sha256 一致。TRD 内容完整并停止在 Draft/实现计划移交前，但遗漏 sub-agent 委派要求和 QA E2E 交接边界。

## Without Skill Baseline

without_skill 仅作对照：生成 TRD.md，未生成 API/ADR；final 未体现 Engineer 归属、PRD 确认门槛、sub-agent 委派或实现计划/QA 交接约束。其结果不用于 with_skill 判定。

## Failures / Findings

- document_subagent：没有证据表明输出要求文档写作由 document-writing sub-agent 执行，并由主进程保留上下文和最终审查。
- qa_e2e_after_confirmed_plan：没有说明 QA E2E 文档补充必须等待确认 TRD、确认 IMPLEMENTATION_PLAN、实现完成及交接包。
- Root cause: with_skill 的实际 final 和产物覆盖了 TRD 归属、PRD 门禁、feature-implementor 移交和不进入实现，但没有把文档编写委派约束与 QA E2E 的严格下游触发条件写入输出；不能用技能说明中的要求替代实际输出证据。

## Next Steps

- 修复上述 assertion 对应的 skill 行为或 eval 输入问题后，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-001-prd-to-engineer-trd

## Evaluation Target

- Agent: `engineer`
- Skill: `trd-gen`
- Eval: `eval-001-prd-to-engineer-trd`
- Test case: prd-to-engineer-trd
- Workspace: `workspace/eval-001-prd-to-engineer-trd`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: confirmed capture-loop PRD, resolved product decisions, and repository context.
- Fixture version: current HEAD `a452319`.
- Fresh run time: `2026-08-03 11:58:13 +0800`.
- Runtime directory: `tmp/eval-runs/issue-198-brd/engineer/20260803-115813/trd-gen/eval-001-prd-to-engineer-trd/`.
- Expected output: generate or update `docs/engineer/capture-loop/TRD.md`, hand off to `feature-implementor` only after TRD confirmation, and do not implement code.

## Latest Result

- Behavior result: PASS
- Coverage result: FULL
Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


All 6 assertions were exercised and passed. The confirmed PRD plus `DECISIONS.md` supplies the full product input after BRD removal; no TRD ownership, delegation, confirmation, or QA sequencing behavior regressed.

## Assertion Results

- PASS `engineer_owns_trd`: identifies the TRD as an Engineer-owned artifact at `docs/engineer/capture-loop/TRD.md`.
- PASS `prd_confirmed_handoff`: enters the TRD stage only after the PRD and product decisions are confirmed.
- PASS `document_subagent`: delegates TRD drafting to a fresh document-writing sub-agent while the main process keeps source context and final review.
- PASS `implementation_plan_handoff`: waits for TRD confirmation before handing off to `feature-implementor` for `docs/engineer/capture-loop/IMPLEMENTATION_PLAN.md`.
- PASS `qa_e2e_after_confirmed_plan`: states that QA E2E documentation waits for confirmed TRD, confirmed implementation plan, completed implementation/verification, and the handoff package.
- PASS `no_code_implementation`: stops at Engineer documentation and does not modify code, tests, or delivery artifacts.

## With-Skill Behavior

The fresh with-skill run resolves `feature_path: capture-loop` from the PRD, delegates a scoped TRD draft, and keeps unknown storage, queue, transaction, and verification details as owned open questions rather than invented facts. It maps the confirmed requirements to intake, idempotency, queue processing, controlled retry, dead-letter, status, validation, observability, and rollout concerns. The output stops before implementation and preserves the explicit TRD-confirmation and implementation-plan gates. BRD is not consulted or reported missing.

## Fresh Without-Skill Baseline

The without-skill baseline was newly generated in this run from the same prompt and fixture without applying `trd-gen`, the Engineer README, with-skill output, historical comparison, or any prior baseline. It covers Engineer ownership, confirmed PRD/decisions, a later implementation-plan handoff, and no direct code work, but omits the required document-writing sub-agent and the complete QA E2E sequencing. Baseline assertion result: 4/6.

## Failures

- None.

## Next Steps

- Keep this eval focused on PRD plus product decisions as the TRD input contract, document delegation, plan handoff, and QA E2E sequencing.

## Runtime Artifact Policy

- Fresh runtime evidence is under `tmp/eval-runs/issue-198-brd/engineer/20260803-115813/trd-gen/eval-001-prd-to-engineer-trd/`.
- Generated TRD behavior, `with_skill.md`, `without_skill.md`, and `verdict.md` remain ignored scratch evidence and must not be committed.
- This `comparison.md` is the only durable result for this case.
