# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-012-implementation-plan-archive-preflight`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `681e197eb0a978ca201707a3d3b58dd8ed78255de8e5033ca94ef611ea90807e` from `agents/engineer/test/feature-implementor/evals/workspace/eval-012-implementation-plan-archive-preflight`.
- Fixture SHA-256: `681e197eb0a978ca201707a3d3b58dd8ed78255de8e5033ca94ef611ea90807e`
- Prompt SHA-256: `9c7650cd9313e12223d2a68ebc3c37905ca839128cbb6b36d20fc7541af57b74`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `31ea692709a0817bc32ab74f76490bf0edfdea6902d08e36d2b8cbddeb78aee4`
- Skill overlay SHA-256: `32c9b06579315c3f3af57ed46ca530329febcbd28b2adfca751e5c7d8b333736`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `3628876acf1d52ad92b5faf79f556bf7cb6aca5a88b0bd15975a544759685f18`
- Metadata SHA-256: `158f5bafaa3ad4ac6ba561642292db5794c29432044a423049518391aa4f0dbd`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `runs_pre_plan_archive_scan` | NOT_EXERCISED | With-skill output does not state that either the existing plan or archive directory was scanned; locked raw evidence cannot prove this hidden process. |
| `blocks_direct_overwrite` | PASS | Output explicitly says the existing Implemented plan cannot be directly overwritten; git evidence shows no mutation. |
| `offers_implemented_handling_options` | PASS | Output offers archiving then creating a new plan, or archiving as Superseded with a reason then creating a new plan, without offering status-only updating. |
| `keeps_active_entry_fixed` | FAIL | Output does not state that the active entry remains docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md or that archives belong under implementation-plans/archive/. |
| `does_not_implement_directly` | PASS | Output makes no claim of code changes, implementation, or verification; git evidence is clean. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9c7650cd9313e12223d2a68ebc3c37905ca839128cbb6b36d20fc7541af57b74; fixture_sha256=681e197eb0a978ca201707a3d3b58dd8ed78255de8e5033ca94ef611ea90807e; output_sha256=b54c6bd1198f197e25f581b32a4af4a8852ddfd54de2f0cc36d2e3bed35c8db7; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly paused before mutation and requested a handling choice, but omitted the required scan and active-entry/archive-location explanation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9c7650cd9313e12223d2a68ebc3c37905ca839128cbb6b36d20fc7541af57b74; fixture_sha256=681e197eb0a978ca201707a3d3b58dd8ed78255de8e5033ca94ef611ea90807e; output_sha256=690c1228ccc66f76fc7607438e7aeb50fcbdc1f5879156dd9823d2cf0139007d; snapshot_sha256=8dd447564d88629d75c77eefbfedbfed8cd3dc7a253a527577ba2fc887e58c63
- Behavior: Claimed completion, used the wrong archive path, and directly modified the active plan.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with-skill output omits the required fixed active-entry path and archive directory location.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-012-implementation-plan-archive-preflight`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `681e197eb0a978ca201707a3d3b58dd8ed78255de8e5033ca94ef611ea90807e` from `agents/engineer/test/feature-implementor/evals/workspace/eval-012-implementation-plan-archive-preflight`.
- Fixture SHA-256: `681e197eb0a978ca201707a3d3b58dd8ed78255de8e5033ca94ef611ea90807e`
- Prompt SHA-256: `9c7650cd9313e12223d2a68ebc3c37905ca839128cbb6b36d20fc7541af57b74`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b2870e3d0eb112e2c40f35446120217b8d8a18d55835b9d634a5a2c9c71dcb55`
- Skill overlay SHA-256: `eb10f50f1bee1354d4cdc15dfff5d3853f5131c3abdfbb65a03b041f90906b17`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `3628876acf1d52ad92b5faf79f556bf7cb6aca5a88b0bd15975a544759685f18`
- Metadata SHA-256: `158f5bafaa3ad4ac6ba561642292db5794c29432044a423049518391aa4f0dbd`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `runs_pre_plan_archive_scan` | FAIL | with_skill 输出说明做了实施前检查，并提到当前计划及“归档目录目前为空”，但未明确说明扫描了精确路径 `docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md` 和 `docs/engineer/payment-refund/implementation-plans/archive/`。 |
| `blocks_direct_overwrite` | PASS | with_skill 输出在用户选择处理方式前明确表示不会写出新计划，并且 raw git evidence 显示工作区无修改。 |
| `offers_implemented_handling_options` | PASS | with_skill 提供了归档已完成计划后新建，以及以 `Superseded` 并记录原因后归档再新建两种选项，未提供继续更新当前计划为 Implemented 的选项。 |
| `keeps_active_entry_fixed` | FAIL | with_skill 未说明活跃入口固定为 `docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md`，也未明确说明归档只能放入 `implementation-plans/archive/`。 |
| `does_not_implement_directly` | PASS | with_skill 表示确认后才会写计划，并等待计划确认后再编码；raw git evidence 显示未发生文件、索引或提交变更。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9c7650cd9313e12223d2a68ebc3c37905ca839128cbb6b36d20fc7541af57b74; fixture_sha256=681e197eb0a978ca201707a3d3b58dd8ed78255de8e5033ca94ef611ea90807e; output_sha256=d581aaea937a0cc4f7e0154053a7f57c0f30af9e22d39a63f2eddbaf0b7e5aba; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别出当前计划已完成且归档目录为空，暂停写入并请求两种归档处理方式确认；未产生任何工作区变更，但未明确满足精确扫描路径和固定入口要求。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9c7650cd9313e12223d2a68ebc3c37905ca839128cbb6b36d20fc7541af57b74; fixture_sha256=681e197eb0a978ca201707a3d3b58dd8ed78255de8e5033ca94ef611ea90807e; output_sha256=1004379e66eb6778451a0cb9558a70a90d9e23d1d657040ba5b54ada5ea1dfce; snapshot_sha256=a51f9b89d969685ebec5c32e47d10b1e84e5a328d96a96a2ed815d70c0b0c7a2
- Behavior: 直接修改并覆盖活跃实施计划，归档到错误的 `payment-refund/archive/` 路径；未请求处理方式确认。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未明确说明扫描两个精确归档前置路径。
- with_skill 未明确说明活跃入口固定且归档仅限 `implementation-plans/archive/`。
- Next: 明确列出并说明已扫描 `docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md` 与 `docs/engineer/payment-refund/implementation-plans/archive/`。
- Next: 明确声明活跃入口保持不变，归档文件仅放入 `docs/engineer/payment-refund/implementation-plans/archive/`。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-012-implementation-plan-archive-preflight`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `681e197eb0a978ca201707a3d3b58dd8ed78255de8e5033ca94ef611ea90807e` from `agents/engineer/test/feature-implementor/evals/workspace/eval-012-implementation-plan-archive-preflight`.
- Fixture SHA-256: `681e197eb0a978ca201707a3d3b58dd8ed78255de8e5033ca94ef611ea90807e`
- Prompt SHA-256: `9c7650cd9313e12223d2a68ebc3c37905ca839128cbb6b36d20fc7541af57b74`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5a3403ec360f8aca06dd1301fa3bfe0f2bd967f54afc7bad9b5691a78697b0ca`
- Skill overlay SHA-256: `5c74cbf7ab5eef845bc8c3f0d81a775b1feca5810a9a615f9b35865026f3e841`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `3628876acf1d52ad92b5faf79f556bf7cb6aca5a88b0bd15975a544759685f18`
- Metadata SHA-256: `158f5bafaa3ad4ac6ba561642292db5794c29432044a423049518391aa4f0dbd`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `runs_pre_plan_archive_scan` | FAIL | with_skill 输出仅说明需先处理旧计划，未说明已扫描 docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md 和 implementation-plans/archive/ 归档目录。 |
| `blocks_direct_overwrite` | PASS | with_skill 输出要求用户先选择处理方式后再创建新计划；git_status 和 git_diff 均为空，未发生覆盖或写入。 |
| `offers_implemented_handling_options` | PASS | with_skill 明确提供“归档旧计划后创建新计划”和“将旧计划标记为 Superseded 并注明原因，再创建新计划”两项，未提供继续更新为 Implemented 的选项。 |
| `keeps_active_entry_fixed` | FAIL | with_skill 输出未说明活跃入口固定为 docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md，也未说明归档仅放入 implementation-plans/archive/。 |
| `does_not_implement_directly` | PASS | with_skill 未声称修改代码、运行实现或完成验证；git_evidence 显示无工作区变更。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9c7650cd9313e12223d2a68ebc3c37905ca839128cbb6b36d20fc7541af57b74; fixture_sha256=681e197eb0a978ca201707a3d3b58dd8ed78255de8e5033ca94ef611ea90807e; output_sha256=b3d23358d65ceb62c4355bcd038af096ce162de4d911647e22c4f9ea48d6de25; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 阻止立即创建计划并提供两种处理选项，保持工作区无变更；但未说明前置扫描和固定活跃入口。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9c7650cd9313e12223d2a68ebc3c37905ca839128cbb6b36d20fc7541af57b74; fixture_sha256=681e197eb0a978ca201707a3d3b58dd8ed78255de8e5033ca94ef611ea90807e; output_sha256=4c3b0eef65c99e0f65f26e6708a7215078c7a1e97d6233813f2349c562d7fe70; snapshot_sha256=c4a1e24113846372e0fa4a9c0ef4e4ad366f8d8dcd7233bd04ca97e832309f83
- Behavior: 直接修改并替换活跃计划，且将旧计划归档到错误的 archive/ 路径；未提供用户选择。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未说明归档前置扫描。
- with_skill 未说明活跃计划入口和归档目录路径保持固定。
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

# Eval Result: eval-012-implementation-plan-archive-preflight

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-012-implementation-plan-archive-preflight`
- Test case: implementation-plan-archive-preflight
- Workspace: `workspace/eval-012-implementation-plan-archive-preflight`
- Evaluation date: 2026-08-07
- Overall result: FAIL
- Behavior result: FAIL
- Coverage result: FULL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: docs/pm/payment-refund/PRD.md 和 docs/engineer/payment-refund/TRD.md 已确认，现在要新增部分退款能力。docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md 已存在且是上一轮全额退款的完成态计划，尚未归档。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- PASS `runs_pre_plan_archive_scan`: with_skill transcript 的成功命令读取了活动计划并检查了 docs/engineer/payment-refund/implementation-plans/archive/；final 报告归档前置检查。
- PASS `blocks_direct_overwrite`: with_skill final 未创建新计划；workspace 活动计划仍为原文件，哈希与 fixture-input.sha256 一致，且没有归档或替换文件。
- PASS `offers_implemented_handling_options`: final 提供归档完成计划后新建、归档为 Superseded 并注明原因后新建两项选择，未提供继续更新 Implemented 计划。
- FAIL `keeps_active_entry_fixed`: final 未明确说明活跃入口固定为 docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md，也未明确说明归档只放到 implementation-plans/archive/。
- PASS `does_not_implement_directly`: final 未声称修改代码、运行实现或完成验证；workspace 文件未发生变化，with_skill 输入哈希与实际哈希一致。

## With Skill Behavior

总体阻止了直接覆盖并提出了正确的两种处理选项，但遗漏了固定活跃入口及指定归档目录的明确说明。

## Without Skill Baseline

仅作对照：without_skill 实际归档并新建了计划，未遵守阻止直接覆盖要求。

## Failures / Findings

- keeps_active_entry_fixed FAIL：缺少要求的固定入口与 implementation-plans/archive/约束说明。
- Root cause: with_skill final 未完整复述 archive preflight 对活动入口和归档目录的明确约束。

## Next Steps

- 修复上述 assertion 对应的 skill 行为或 eval 输入问题后，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-012-implementation-plan-archive-preflight

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-012-implementation-plan-archive-preflight`
- Test case: implementation-plan-archive-preflight
- Workspace: `workspace/eval-012-implementation-plan-archive-preflight`
- Latest result: PARTIAL - the 2026-07-05 fresh validation still covers archive
- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。

  scanning and overwrite blocking, but the handling-options assertion changed
  from three choices to two and has not been rerun.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture files read before skill use: `README.md`, `eval_metadata.json`, `docs/pm/payment-refund/PRD.md`, `docs/engineer/payment-refund/TRD.md`, and `docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md`.
- Fixture summary: PRD/TRD now cover partial refunds, but an existing active `IMPLEMENTATION_PLAN.md` for `implementation_scope: full-refund-flow` has `status: Implemented` and has not been archived.
- Expected output: run archive preflight, block direct overwrite, report existing plan path/status/scope, and ask the user to choose archive-then-create or supersede-then-create.

## Assertions

- PASS `runs_pre_plan_archive_scan`: the skill scans active `IMPLEMENTATION_PLAN.md` and `implementation-plans/archive/` before a new plan.
- PASS `blocks_direct_overwrite`: unresolved active-plan handling blocks overwriting or replacing the active entry.
- NOT RERUN `offers_implemented_handling_options`: the current assertion
  requires archive completed plan then create or archive as `Superseded` with
  reason then create, and forbids continuing an `Implemented` plan.
- PASS `keeps_active_entry_fixed`: active entry stays `docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md`; history goes under `implementation-plans/archive/`.
- PASS `does_not_implement_directly`: no code, implementation, or verification is performed before plan handling and confirmation.

## With Skill Behavior

The prior fresh with-skill validation confirmed the archive scan and blocking
behavior. Its three-choice handling result is historical and does not validate
the current two-choice rule for `status: Implemented`.

## Without Skill Baseline

The prior fresh without-skill baseline was summarized before reading skill
docs. It predates the current two-choice assertion and cannot serve as the
required fresh baseline for a rerun.

## Failures

- The current two-choice handling assertion has not received fresh with-skill
  and without-skill validation.

## Next Steps

- Rerun fresh with-skill and without-skill validation before treating the
  updated handling assertion as PASS.

## Runtime Artifacts Policy

- This validation did not create runtime artifacts.
- Runtime transcripts, verdicts, timing files, outputs, diagnostics, run status files, and `comparison.auto.md` must not be committed.
