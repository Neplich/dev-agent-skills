# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-004-small-change-plan-gate`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/engineer/test/feature-implementor/evals/workspace/eval-004-small-change-plan-gate`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `78a38f2825c3f49238f0218d2c37fda54f328e48d02e714402d6027e16d2911e`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5a3403ec360f8aca06dd1301fa3bfe0f2bd967f54afc7bad9b5691a78697b0ca`
- Skill overlay SHA-256: `5c74cbf7ab5eef845bc8c3f0d81a775b1feca5810a9a615f9b35865026f3e841`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `e8113c8f9ac27e12faac063db222c170fc22f3e44873b19aceac594a7e81169a`
- Metadata SHA-256: `74367c62f9d5c4aae964f8fe1660f63ee4472124c71cb1b116797d64179c211b`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `records_prd_alignment` | FAIL | with_skill 输出未说明产品与技术负责人已确认，也未在实施安排中记录该对齐依据。 |
| `writes_plan_for_small_change` | FAIL | with_skill 输出未要求产出或更新 docs/engineer/settings-label/IMPLEMENTATION_PLAN.md。 |
| `records_split_decision` | FAIL | with_skill 输出未说明是否触发 implementation/validation sub-agent split，也未说明不拆分不等于跳过实施计划。 |
| `waits_for_user_confirmation` | FAIL | with_skill 输出未要求用户确认实施计划后再开始实施。 |
| `blocks_e2e_without_confirmed_plan` | FAIL | with_skill 输出未说明 E2E 文档补充需引用已确认计划，或计划缺失/未确认时必须 blocked。 |
| `does_not_modify_code` | PASS | with_skill 输出仅描述拟议步骤，并明确当前无法开始修改；原始 git evidence 也显示无代码变更。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=78a38f2825c3f49238f0218d2c37fda54f328e48d02e714402d6027e16d2911e; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=aca63787cb104759a6c9ee8656a681be026dd5b602053d24c4b2985173c201d8; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提供了简单的修改安排并说明当前无法修改，但未满足五项流程与依赖记录要求；未发生代码变更。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=78a38f2825c3f49238f0218d2c37fda54f328e48d02e714402d6027e16d2911e; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=fda6c0091c7bbf5530192060b43f456a3ea81117a6fa9125cf39b11276bc6585; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提供了简单的按钮文案修改安排，但未涵盖所要求的确认、计划文件、拆分判断或 E2E 依赖。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 输出未满足 records_prd_alignment、writes_plan_for_small_change、records_split_decision、waits_for_user_confirmation、blocks_e2e_without_confirmed_plan。
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

# Eval Result: eval-004-small-change-plan-gate

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-004-small-change-plan-gate`
- Test case: small-change-plan-gate
- Workspace: `workspace/eval-004-small-change-plan-gate`
- Evaluation date: 2026-08-07
- Overall result: FAIL
- Behavior result: FAIL
- Coverage result: FULL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: docs/pm/settings-label/PRD.md 和 docs/engineer/settings-label/TRD.md 已确认。请把设置页按钮文案从「保存」改成「保存设置」，这是一个单文件小改动。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- FAIL `records_prd_alignment`: final 仅称 PRD/TRD 缺失，未确认已读取/对齐，也未在实施计划中记录状态；且未生成计划。
- FAIL `writes_plan_for_small_change`: final 明确表示“不能创建实施计划”，workspace 中也不存在 IMPLEMENTATION_PLAN.md。
- FAIL `records_split_decision`: final 未说明 implementation/validation sub-agent split 判断。
- FAIL `waits_for_user_confirmation`: final 未提交实施计划供用户确认，反而要求先补充文档。
- FAIL `blocks_e2e_without_confirmed_plan`: final 未说明 E2E 文档补充必须依赖已确认计划及缺失/未确认时 blocked。
- PASS `does_not_modify_code`: final 未声称修改代码；transcript 仅执行读取/检查命令，workspace 文件清单与输入 hash 一致。

## With Skill Behavior

with_skill 成功执行且检查了文档存在性，但因文档缺失直接阻塞，未产出计划、拆分判断或确认请求。

## Without Skill Baseline

without_skill 仅作对照：因 workspace 为空未实施，也未覆盖计划门禁要求。

## Failures / Findings

- 未按要求处理单文件小改动的实施计划流程。
- 未记录 sub-agent split 决策。
- 未说明 E2E 文档依赖确认计划的阻塞规则。
- Root cause: with_skill 将缺少 PRD/TRD 视为无法继续的总阻塞，导致未输出任务要求的计划门禁内容；实际 workspace 确实没有这些文档，但该事实不足以满足 expected_output 中要求的计划、拆分和确认说明。

## Next Steps

- 修复上述 assertion 对应的 skill 行为或 eval 输入问题后，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-004-small-change-plan-gate

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-004-small-change-plan-gate`
- Test case: small-change-plan-gate
- Workspace: `workspace/eval-004-small-change-plan-gate`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-05
- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture files read before skill use: `eval_metadata.json` and the `eval-004-small-change-plan-gate` item in `evals.json`.
- Fixture note: this workspace stores metadata only; the prompt declares `docs/pm/settings-label/PRD.md` and `docs/engineer/settings-label/TRD.md` are confirmed.
- Expected output: produce a short `docs/engineer/settings-label/IMPLEMENTATION_PLAN.md`, record PRD alignment and split decision, wait for user confirmation, and do not edit code.

## Assertions

- PASS `records_prd_alignment`: planner requires an alignment result from PRD/TRD and does not block merely because standalone `DECISIONS.md` is absent.
- PASS `writes_plan_for_small_change`: planner runs for every implementation task, including small, single-file changes.
- PASS `records_split_decision`: the plan must state whether the complex implementation/validation split is needed.
- PASS `waits_for_user_confirmation`: implementation cannot start before exact plan confirmation.
- PASS `blocks_e2e_without_confirmed_plan`: QA E2E handoff requires a confirmed implementation plan even for small changes.
- PASS `does_not_modify_code`: no button text or code changes happen during Phase 1 planning.

## With Skill Behavior

Fresh with-skill validation confirmed that small-change handling was not loosened by the direct specialist gate. The prompt-declared confirmed PRD/TRD chain is sufficient to enter planning, but the task still must create or update `docs/engineer/settings-label/IMPLEMENTATION_PLAN.md`. The plan should record PRD alignment, target file and text change, verification command, and the decision that complex sub-agent split is unnecessary because the change is single-file and low risk. The skill must then wait for user confirmation before code edits or E2E documentation changes.

## Without Skill Baseline

The fresh without-skill baseline was summarized before reading skill docs. A generic worker is likely to treat the requested label change as trivial and either modify the file directly or give a brief implementation note without a durable plan. It may also skip the split decision and omit the rule that E2E documentation updates are blocked until a confirmed implementation plan exists.

## Failures

- None.

## Next Steps

- Keep this eval focused on small changes still requiring PRD/TRD alignment, implementation planning, and confirmation.

## Runtime Artifacts Policy

- This validation did not create runtime artifacts.
- Runtime transcripts, verdicts, timing files, outputs, diagnostics, run status files, and `comparison.auto.md` must not be committed.
