# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-016-draft-status-continues-current-plan`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `e083cacd49102d9384a79c9ea941e92b48d18d81842c0cbf72510a9b890d7c7d` from `agents/engineer/test/feature-implementor/evals/workspace/eval-016-draft-status-continues-current-plan`.
- Fixture SHA-256: `e083cacd49102d9384a79c9ea941e92b48d18d81842c0cbf72510a9b890d7c7d`
- Prompt SHA-256: `94992d68c84f843faca4d58c6bb2c604bfcff22e23ecd95ba7c0c306fd36011b`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `31ea692709a0817bc32ab74f76490bf0edfdea6902d08e36d2b8cbddeb78aee4`
- Skill overlay SHA-256: `32c9b06579315c3f3af57ed46ca530329febcbd28b2adfca751e5c7d8b333736`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `bb7bf0f3a482a77a018b0515b1c16fcfc9e7cd11c5d0dea890b0578898ccf6a8`
- Metadata SHA-256: `566e39d7363acab918c0b8b38f7cebac43ee4f4a9069dd6e8b635d61f1c29eb0`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_active_plan_frontmatter` | NOT_EXERCISED | The locked evidence shows the plan was updated, but cannot prove the hidden read order or that the frontmatter, rather than the prompt, was the basis. |
| `detects_non_implemented_status` | PASS | The with_skill diff retains status: "Draft" and the output states implementation cannot proceed yet and requires confirmation. |
| `continues_current_plan` | PASS | Only docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md was modified; no second active plan was created. |
| `bumps_plan_version` | PASS | The diff updates version from 0.1.0 to 0.2.0 and last_updated from 2026-07-27 to 2026-08-08. |
| `does_not_force_archive_link` | PASS | The plan and output impose no archive or previous_plan_archive prerequisite. |
| `waits_before_coding` | PASS | The output requests confirmation and a code baseline before implementation; raw git evidence shows only the plan file changed. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=94992d68c84f843faca4d58c6bb2c604bfcff22e23ecd95ba7c0c306fd36011b; fixture_sha256=e083cacd49102d9384a79c9ea941e92b48d18d81842c0cbf72510a9b890d7c7d; output_sha256=f2589d675f71cb009b5d12a58ab79671a3924b64680907a2a98f24a6eeecadcc; snapshot_sha256=4f1e75707f395bc6b3304be1822824e4e3773e9d63750e467b94d8a97817da1f
- Behavior: Updated the existing Draft implementation plan, bumped its version and date, and paused for confirmation and code baseline before coding.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=94992d68c84f843faca4d58c6bb2c604bfcff22e23ecd95ba7c0c306fd36011b; fixture_sha256=e083cacd49102d9384a79c9ea941e92b48d18d81842c0cbf72510a9b890d7c7d; output_sha256=6ab2fade8acd6b2c107fcd5f58b9fb2abdd20cc51901285f828599aa35fcd022; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Asked for additional requirements and made no changes.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-016-draft-status-continues-current-plan`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `e083cacd49102d9384a79c9ea941e92b48d18d81842c0cbf72510a9b890d7c7d` from `agents/engineer/test/feature-implementor/evals/workspace/eval-016-draft-status-continues-current-plan`.
- Fixture SHA-256: `e083cacd49102d9384a79c9ea941e92b48d18d81842c0cbf72510a9b890d7c7d`
- Prompt SHA-256: `94992d68c84f843faca4d58c6bb2c604bfcff22e23ecd95ba7c0c306fd36011b`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b2870e3d0eb112e2c40f35446120217b8d8a18d55835b9d634a5a2c9c71dcb55`
- Skill overlay SHA-256: `eb10f50f1bee1354d4cdc15dfff5d3853f5131c3abdfbb65a03b041f90906b17`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `bb7bf0f3a482a77a018b0515b1c16fcfc9e7cd11c5d0dea890b0578898ccf6a8`
- Metadata SHA-256: `566e39d7363acab918c0b8b38f7cebac43ee4f4a9069dd6e8b635d61f1c29eb0`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_active_plan_frontmatter` | FAIL | with_skill 输出未提及读取 IMPLEMENTATION_PLAN.md 的 frontmatter，也未基于其状态作判断。 |
| `detects_non_implemented_status` | FAIL | with_skill 输出未识别 status: Draft，也未判断当前轮次尚未完成。 |
| `continues_current_plan` | FAIL | 仅承诺按 payment-refund 路径更新对应文档，未明确继续更新固定入口 IMPLEMENTATION_PLAN.md。 |
| `bumps_plan_version` | FAIL | 未要求同步 bump version 或更新 last_updated。 |
| `does_not_force_archive_link` | PASS | 输出未要求归档或 previous_plan_archive 作为继续计划的前置条件。 |
| `waits_before_coding` | FAIL | 未明确在更新实施计划后等待用户确认；仅表示收到变更描述后会做影响分析并更新文档。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=94992d68c84f843faca4d58c6bb2c604bfcff22e23ecd95ba7c0c306fd36011b; fixture_sha256=e083cacd49102d9384a79c9ea941e92b48d18d81842c0cbf72510a9b890d7c7d; output_sha256=beb79ccabe1198dd7ae2dabce13d1e34d8b2d313464c052cd1074151090bff01; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 索要具体变更，并泛泛承诺后续影响分析及按 payment-refund 路径更新文档，但未处理 active plan 状态、版本或确认门槛。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=94992d68c84f843faca4d58c6bb2c604bfcff22e23ecd95ba7c0c306fd36011b; fixture_sha256=e083cacd49102d9384a79c9ea941e92b48d18d81842c0cbf72510a9b890d7c7d; output_sha256=8365f41f84f7891d4f1c88bb55347cb4689ccd9a5dc260a3522cce05f8a2f67c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 确认 PRD/TRD 后索要具体变更，未读取或处理 active implementation plan。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill candidate output 未满足 5 项断言，只有不强制归档回链满足。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-016-draft-status-continues-current-plan`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `e083cacd49102d9384a79c9ea941e92b48d18d81842c0cbf72510a9b890d7c7d` from `agents/engineer/test/feature-implementor/evals/workspace/eval-016-draft-status-continues-current-plan`.
- Fixture SHA-256: `e083cacd49102d9384a79c9ea941e92b48d18d81842c0cbf72510a9b890d7c7d`
- Prompt SHA-256: `94992d68c84f843faca4d58c6bb2c604bfcff22e23ecd95ba7c0c306fd36011b`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5a3403ec360f8aca06dd1301fa3bfe0f2bd967f54afc7bad9b5691a78697b0ca`
- Skill overlay SHA-256: `5c74cbf7ab5eef845bc8c3f0d81a775b1feca5810a9a615f9b35865026f3e841`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `bb7bf0f3a482a77a018b0515b1c16fcfc9e7cd11c5d0dea890b0578898ccf6a8`
- Metadata SHA-256: `566e39d7363acab918c0b8b38f7cebac43ee4f4a9069dd6e8b635d61f1c29eb0`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_active_plan_frontmatter` | FAIL | With-skill output does not mention reading or using IMPLEMENTATION_PLAN.md frontmatter. |
| `detects_non_implemented_status` | FAIL | It does not identify status: Draft or state that the current round is unfinished. |
| `continues_current_plan` | FAIL | It proposes generating an implementation plan and does not continue the fixed existing plan entry. |
| `bumps_plan_version` | FAIL | It does not require bumping version or updating last_updated. |
| `does_not_force_archive_link` | PASS | The output does not require archiving or previous_plan_archive as a prerequisite. |
| `waits_before_coding` | FAIL | It asks for more requirements and proposes updating PRD/TRD before generating a plan; it does not update the plan and then wait for confirmation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=94992d68c84f843faca4d58c6bb2c604bfcff22e23ecd95ba7c0c306fd36011b; fixture_sha256=e083cacd49102d9384a79c9ea941e92b48d18d81842c0cbf72510a9b890d7c7d; output_sha256=0657424f71528cda7e4d6ce18bd05ed508641e99890b2073cf5c0b5a7d5eae8c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Requests clarification, does not identify the Draft active plan, and does not perform the required plan-continuation workflow.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=94992d68c84f843faca4d58c6bb2c604bfcff22e23ecd95ba7c0c306fd36011b; fixture_sha256=e083cacd49102d9384a79c9ea941e92b48d18d81842c0cbf72510a9b890d7c7d; output_sha256=f0900c2d147356e90d0c3331e4426bcdcad1790008546bec6aa081492b133489; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Requests clarification and does not inspect or update the active implementation plan.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- With-skill output fails five of six required behaviors; only the non-forced-archive condition is satisfied.
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

# Eval Result: eval-016-draft-status-continues-current-plan

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-016-draft-status-continues-current-plan`
- Test case: draft-status-continues-current-plan
- Workspace: `workspace/eval-016-draft-status-continues-current-plan`
- Evaluation date: 2026-08-07
- Overall result: FAIL
- Behavior result: FAIL
- Coverage result: FULL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: docs/pm/payment-refund/PRD.md 和 docs/engineer/payment-refund/TRD.md 已确认。现在要在这个功能上做下一轮更新。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- PASS `reads_active_plan_frontmatter`: with_skill transcript item_4 explicitly reads IMPLEMENTATION_PLAN.md, including its frontmatter; the resulting final identifies status Draft.
- PASS `detects_non_implemented_status`: Final explicitly states current plan is `Draft` and treats the round as unfinished.
- FAIL `continues_current_plan`: Final explicitly says 暂不更新计划; workspace plan remains unchanged and no file_change item exists.
- FAIL `bumps_plan_version`: Workspace and fixture hashes match; plan remains version 0.1.0 with last_updated 2026-07-27, not bumped.
- PASS `does_not_force_archive_link`: Final says there is no archive history and no archive choice is needed; it does not require archival or previous_plan_archive before proceeding.
- FAIL `waits_before_coding`: No plan update occurred and the final does not present an updated plan followed by a confirmation request; it only reports a TRD blocker.

## With Skill Behavior

读取了 PRD、TRD、active plan 及归档状态并识别 Draft，但因自行判定 TRD gap 而不更新现有计划，导致未完成版本 bump、计划确认前置流程。

## Without Skill Baseline

without_skill 更新了固定 IMPLEMENTATION_PLAN.md、将版本改为 0.2.0 并更新 last_updated，且未编写代码；仅作对照。

## Failures / Findings

- 未继续更新固定 active IMPLEMENTATION_PLAN.md。
- 未 bump version 和 last_updated。
- 未在计划更新后等待用户确认。
- Root cause: with_skill transcript 显示其将简短但已批准的 TRD 误判为必须先补充技术决策的 TRD gap，并因此提前阻断了 Draft active plan 的继续更新流程。

## Next Steps

- 修复上述 assertion 对应的 skill 行为或 eval 输入问题后，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-016-draft-status-continues-current-plan

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-016-draft-status-continues-current-plan`
- Test case: draft-status-continues-current-plan
- Workspace: `workspace/eval-016-draft-status-continues-current-plan`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-27
- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture files read before skill use: `README.md`, `eval_metadata.json`,
  `docs/pm/payment-refund/PRD.md`, `docs/engineer/payment-refund/TRD.md`, and
  `docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md`.
- Fixture summary: the prompt omits plan status; the active plan frontmatter has
  `status: Draft`, `version: 0.1.0`, and
  `implementation_scope: refund-reason-codes`.

## Assertions

- PASS `reads_active_plan_frontmatter`: the response derives the current state
  from the active plan frontmatter instead of the prompt.
- PASS `detects_non_implemented_status`: it recognizes `status: Draft` as an
  unfinished current round.
- PASS `continues_current_plan`: it keeps the fixed active entry and does not
  create a second plan.
- PASS `bumps_plan_version`: it requires a substantive version bump and
  `last_updated` refresh.
- PASS `does_not_force_archive_link`: it does not require archive handling or
  `previous_plan_archive`.
- PASS `waits_before_coding`: it waits for confirmation after updating the plan.

## With Skill Behavior

The fresh with-skill validator read the Engineer entry and feature-implementor
planner instructions, inspected the fixture active plan, and identified
`status: Draft`, `version: 0.1.0`, and the current scope. It chose the continued
update path, required a version and date update, omitted archive linkage, and
stopped before code until user confirmation.

## Without Skill Baseline

A separate fresh zero-exposure subagent received only the eval prompt, fixture,
and assertions. It did not read the feature-implementor skill, internal
instructions, or Engineer README and did not reuse a historical baseline. It
also passed all six assertions by deriving the Draft state from the fixture and
continuing the fixed active plan.

## Failures

- None.
- The paired run showed no assertion-level difference. The assertions expose
  the full desired behavior, so this eval confirms correctness but has limited
  with-skill differentiation.

## Next Steps

- Keep the case focused on discovering the non-`Implemented` state from
  frontmatter and allowing a continued update.
- If stronger differentiation is needed later, reduce rule-level hints without
  weakening the real active-plan evidence.

## Runtime Artifacts Policy

- The paired validation returned results in the subagent response and did not
  create repository runtime files.
- Runtime transcripts, verdicts, timing files, outputs, diagnostics, run status
  files, and `comparison.auto.md` must not be committed.
