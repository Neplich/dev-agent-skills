# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-015-implemented-status-detected-from-fixture`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `081f99f1748dae6b1e4b0b232ec7c1df3a484b0c63d868321dc8a1e16a817449` from `agents/engineer/test/feature-implementor/evals/workspace/eval-015-implemented-status-detected-from-fixture`.
- Fixture SHA-256: `081f99f1748dae6b1e4b0b232ec7c1df3a484b0c63d868321dc8a1e16a817449`
- Prompt SHA-256: `94992d68c84f843faca4d58c6bb2c604bfcff22e23ecd95ba7c0c306fd36011b`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5a3403ec360f8aca06dd1301fa3bfe0f2bd967f54afc7bad9b5691a78697b0ca`
- Skill overlay SHA-256: `5c74cbf7ab5eef845bc8c3f0d81a775b1feca5810a9a615f9b35865026f3e841`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `b2cb611a2eb526b32fe7d8233b7af41b5dc9690189d7d476ddf33384f3fb4855`
- Metadata SHA-256: `b8899bf7ae5f8fcc629e9bed966ceb9612aaea2fc7055363d1e8ea6b2efd4e30`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_active_plan_frontmatter` | FAIL | with_skill 输出未提及或依据 IMPLEMENTATION_PLAN.md 的 frontmatter。 |
| `detects_implemented_status` | FAIL | 未明确识别 status: Implemented、计划路径或 implementation_scope: full-refund-flow。 |
| `blocks_direct_overwrite` | FAIL | 未要求先确认完成态计划的处理决定，反而表示将更新文档并继续实现。 |
| `offers_implemented_handling_options` | FAIL | 未提供“归档完成计划后新建”或“归档为 Superseded 并记录原因后新建”两种选项。 |
| `does_not_implement_code` | PASS | 输出未声称已修改代码或已开始实现；仅作未来计划表述。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=94992d68c84f843faca4d58c6bb2c604bfcff22e23ecd95ba7c0c306fd36011b; fixture_sha256=081f99f1748dae6b1e4b0b232ec7c1df3a484b0c63d868321dc8a1e16a817449; output_sha256=8b161af293fe2aaeba633208d434a5271069928ce69d01c01630904dd381a561; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 请求本轮具体变更目标，但未读取或识别已完成的 active plan，也未提供归档处理选项。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=94992d68c84f843faca4d58c6bb2c604bfcff22e23ecd95ba7c0c306fd36011b; fixture_sha256=081f99f1748dae6b1e4b0b232ec7c1df3a484b0c63d868321dc8a1e16a817449; output_sha256=a2c069a71238ec689cd44d7024e087be9b39f96d9a44a760d0934368bbb271b3; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 只确认 PRD/TRD 范围并请求具体需求，未处理 active plan 状态。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 输出未满足读取 active plan、识别 Implemented 状态、阻止覆盖及提供两种处理选项的要求。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge package, verdict, timing, and diagnostics remain under ignored `tmp/eval-runs/` or short-lived CI artifacts and are not committed.
- This durable comparison retains only the reviewable summary and superseded history.

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

# Eval Result: eval-015-implemented-status-detected-from-fixture

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-015-implemented-status-detected-from-fixture`
- Test case: implemented-status-detected-from-fixture
- Workspace: `workspace/eval-015-implemented-status-detected-from-fixture`
- Evaluation date: 2026-08-07
- Overall result: PASS
- Behavior result: PASS
- Coverage result: FULL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: docs/pm/payment-refund/PRD.md 和 docs/engineer/payment-refund/TRD.md 已确认。现在要在这个功能上做下一轮更新。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- PASS `reads_active_plan_frontmatter`: transcript item_5 明确执行并输出 IMPLEMENTATION_PLAN.md 内容，包含 frontmatter。
- PASS `detects_implemented_status`: final 明确指出活动计划路径、status `Implemented` 与 implementation scope `full-refund-flow`。
- PASS `blocks_direct_overwrite`: final 在处理决定确认前停下并提供选择；with_skill 输入/输出 workspace hash 完全一致，未新增归档或计划文件。
- PASS `offers_implemented_handling_options`: final 明确提供“归档后新建”和“归档为 Superseded 并填写原因后新建”两项，未提供继续更新当前计划选项。
- PASS `does_not_implement_code`: final 未声称开始实现；workspace 仅保留原有文档，hash 与 fixture/input manifest 一致。

## With Skill Behavior

with_skill transcript、final、JSONL、hash manifest 与 workspace 均核验通过；正确识别 Implemented 活动计划并触发归档门禁。

## Without Skill Baseline

without_skill 仅作对照：识别了 Implemented，但未按要求停在两选项归档门禁，转而要求代码仓库或更新计划。

## Failures / Findings

- None.
- Root cause: None.

## Next Steps

- 后续修改该 skill、fixture 或 assertions 时，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-015-implemented-status-detected-from-fixture

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-015-implemented-status-detected-from-fixture`
- Test case: implemented-status-detected-from-fixture
- Workspace: `workspace/eval-015-implemented-status-detected-from-fixture`
- Latest result: PARTIAL - the 2026-07-27 fresh validation still covers reading
- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。

  frontmatter, detecting `Implemented`, and blocking overwrite, but the
  handling-options assertion changed from three choices to two and has not been
  rerun.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture files read before skill use: `README.md`, `eval_metadata.json`,
  `docs/pm/payment-refund/PRD.md`, `docs/engineer/payment-refund/TRD.md`, and
  `docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md`.
- Fixture summary: the prompt omits plan status; the active plan frontmatter has
  `status: Implemented` and `implementation_scope: full-refund-flow`.

## Assertions

- PASS `reads_active_plan_frontmatter`: the response derives the completed state
  from the active plan frontmatter instead of the prompt.
- PASS `detects_implemented_status`: it reports the active path,
  `status: Implemented`, and `implementation_scope: full-refund-flow`.
- PASS `blocks_direct_overwrite`: it stops before creating or overwriting an
  active plan.
- NOT RERUN `offers_implemented_handling_options`: the current assertion
  requires archive-then-create or Superseded-then-create and forbids continuing
  an `Implemented` plan.
- PASS `does_not_implement_code`: it makes no code or implementation claim.

## With Skill Behavior

The prior fresh with-skill validator read the Engineer entry and
feature-implementor planner instructions, inspected the fixture active plan,
and stopped at the archive gate. Its three-choice result is historical and
does not validate the current two-choice rule.

## Without Skill Baseline

The prior fresh zero-exposure baseline predates the current two-choice
assertion and cannot serve as the required fresh baseline for a rerun.

## Failures

- The current two-choice handling assertion has not received fresh with-skill
  and without-skill validation.

## Next Steps

- Keep the case focused on discovering `Implemented` from frontmatter rather
  than from a prompt hint.
- Rerun fresh with-skill and without-skill validation before treating the
  updated handling assertion as PASS.
- If stronger differentiation is needed later, reduce rule-level hints in the
  fixture README and metadata without weakening the real active-plan evidence.

## Runtime Artifacts Policy

- The paired validation returned results in the subagent response and did not
  create repository runtime files.
- Runtime transcripts, verdicts, timing files, outputs, diagnostics, run status
  files, and `comparison.auto.md` must not be committed.
