# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-005-existing-behavior-change-needs-pm`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/engineer/test/feature-implementor/evals/workspace/eval-005-existing-behavior-change-needs-pm`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `5f81869b673853f146ffc9b6b0265765a906f1c4c8ed1c32a5df3f964238d63c`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5a3403ec360f8aca06dd1301fa3bfe0f2bd967f54afc7bad9b5691a78697b0ca`
- Skill overlay SHA-256: `5c74cbf7ab5eef845bc8c3f0d81a775b1feca5810a9a615f9b35865026f3e841`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `a4e07ef6b983fa7473b530066460795acade377b6663bfa81c7266e9bd35ec21`
- Metadata SHA-256: `4d7d33b92b764b2a122613cfa3d9e97d80ead9fb721df6a2df123d3fcb35534c`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `checks_approved_behavior` | PASS | with_skill 明确指出该变更会把 active 从“排除 archived”改为“包含 archived”，属于已批准产品行为的改变。 |
| `stops_before_implementation_plan` | PASS | with_skill 将更新 PRD/产品决策、同步 TRD和确认后续步骤置于实现之前，并声明本轮未修改文件。 |
| `hands_off_to_pm_existing_update` | FAIL | 输出提到 existing-project-update、更新 PM 决策/PRD及同步 TRD，但未明确要求走 `pm-agent:idea-to-spec` 路径。 |
| `blocks_e2e_expected_behavior_change` | FAIL | 输出建议后续补充验收与回归测试，但未明确说明在 PRD/产品决策更新、TRD 同步和实施计划确认前不得编写新的 E2E TC 或验收预期。 |
| `does_not_implement_directly` | PASS | with_skill 明确声明本轮没有修改任何文件，也未声称已修改代码、测试或完成实现。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5f81869b673853f146ffc9b6b0265765a906f1c4c8ed1c32a5df3f964238d63c; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=f095bd0a89a232e1089c7a08820a1737e90d2d580650226d0541ada3c4868974; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别为 existing-project-update，停止直接实施并要求先处理 PRD/决策与 TRD；但未明确点名 `pm-agent:idea-to-spec`，也未明确阻断 E2E 预期及实施计划确认前置条件。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5f81869b673853f146ffc9b6b0265765a906f1c4c8ed1c32a5df3f964238d63c; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=fe47bba2bfb00de94116384480e741b5f768961613efaf745ab5185c54bc5889; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别到没有源码且未修改文件，但按局部代码变更给出实现和测试建议，未处理已批准行为变更的流程约束。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未明确要求走 `pm-agent:idea-to-spec` 的 existing-project-update 路径。
- with_skill 未明确阻断 PRD/产品决策、TRD 和实施计划确认前的 E2E TC 或验收预期更新。
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

# Eval Result: eval-005-existing-behavior-change-needs-pm

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-005-existing-behavior-change-needs-pm`
- Test case: existing-behavior-change-needs-pm
- Workspace: `workspace/eval-005-existing-behavior-change-needs-pm`
- Evaluation date: 2026-08-07
- Overall result: FAIL
- Behavior result: FAIL
- Coverage result: FULL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: docs/pm/notifications/PRD.md 和 docs/engineer/notifications/TRD.md 都规定 active 列表排除 archived。现在请把 active 列表改成包含 archived；这是一个很小的单文件改动。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- FAIL `checks_approved_behavior`: 未明确指出 active 排除 archived 的既有预期及本请求会改变该预期。
- PASS `stops_before_implementation_plan`: 未创建或更新 IMPLEMENTATION_PLAN.md；workspace 中不存在该文件。
- FAIL `hands_off_to_pm_existing_update`: 要求 PM 更新范围，但未明确指定 `pm-agent:idea-to-spec` 的 `existing-project-update` 路径。
- FAIL `blocks_e2e_expected_behavior_change`: 未说明在 PRD/决策更新、TRD 同步和实施计划确认前阻止新的 E2E TC 或验收预期。
- PASS `does_not_implement_directly`: 未声称修改代码、测试或完成实现。

## With Skill Behavior

正确停止实现，但未完整输出预期的行为变更判断、精确 PM 路由和 E2E 阻断条件。

## Without Skill Baseline

仅因工作区为空停止，未覆盖本题的行为变更门禁；仅作对照。

## Failures / Findings

- checks_approved_behavior
- hands_off_to_pm_existing_update
- blocks_e2e_expected_behavior_change
- Root cause: 遇到缺失 PRD/TRD 后退化为一般性缺文件阻断，未按题设输出完整的 approved behavior 变更与 PM existing-project-update 门禁。

## Next Steps

- 修复上述 assertion 对应的 skill 行为或 eval 输入问题后，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-005-existing-behavior-change-needs-pm

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-005-existing-behavior-change-needs-pm`
- Test case: existing-behavior-change-needs-pm
- Workspace: `workspace/eval-005-existing-behavior-change-needs-pm`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-05
- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture files read before skill use: `eval_metadata.json` and the `eval-005-existing-behavior-change-needs-pm` item in `evals.json`.
- Fixture note: this workspace stores metadata only; the prompt declares PRD/TRD currently require active lists to exclude archived items.
- Expected output: recognize the requested archived-in-active behavior changes approved expectations, stop before `IMPLEMENTATION_PLAN.md`, return to `pm-agent:idea-to-spec` using `existing-project-update`, then require TRD sync before implementation.

## Assertions

- PASS `checks_approved_behavior`: the alignment gate classifies expectation changes before planning.
- PASS `stops_before_implementation_plan`: behavior changes that need PM updates do not create or update `docs/engineer/notifications/IMPLEMENTATION_PLAN.md`.
- PASS `hands_off_to_pm_existing_update`: approved expectation changes return to `pm-agent:idea-to-spec` with `existing-project-update`.
- PASS `blocks_e2e_expected_behavior_change`: QA E2E expectations cannot be updated until PRD/product decision update, TRD sync, and implementation plan confirmation.
- PASS `does_not_implement_directly`: the skill does not code, test, or claim implementation when scope is unaligned.

## With Skill Behavior

Fresh with-skill validation confirmed the PM handoff gate is still meaningful after direct specialist updates: confirmed PRD/TRD inputs do not permit implementation when the requested behavior contradicts them. The current skill should classify archived items in the active list as an approved-expectation change, stop before planning, route the request to `pm-agent:idea-to-spec` through `existing-project-update`, and require synchronized TRD updates before any `feature-implementor` plan or QA E2E expected behavior update.

## Without Skill Baseline

The fresh without-skill baseline was summarized before reading skill docs. A generic worker may over-focus on the prompt's "small single-file change" framing and either propose the code/test edit or write a lightweight plan. It would not reliably treat the request as a product expectation change, block `IMPLEMENTATION_PLAN.md`, or require PM update plus later TRD sync before E2E changes.

## Failures

- None.

## Next Steps

- Keep this eval focused on stopping small existing-behavior changes that alter approved PM/TRD expectations.

## Runtime Artifacts Policy

- This validation did not create runtime artifacts.
- Runtime transcripts, verdicts, timing files, outputs, diagnostics, run status files, and `comparison.auto.md` must not be committed.
