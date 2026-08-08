# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `engineer-agent`
- Eval: `eval-002-existing-feature-alignment-gate`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/engineer/test/engineer-agent/evals/workspace/eval-002-existing-feature-alignment-gate`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `d08d04c31266e7709df236e5a84b0516db051d4099fdd86927601fc672aa3954`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `757a4f95af830e3468b6c44e54e5901a0cc27f0a6d0aa7ecc8b703b612007d3a`
- Skill overlay SHA-256: `ed4d8f534d0e5c1c334b4a13d67b6d20c37dceb98e00e4e2ea3b6a2c0112faad`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `35bf0057341046be2b5db3cd90c99d825b61efaf315ed25428b5eda571894209`
- Metadata SHA-256: `43542dab517c382c8ae0bc3c7332df9e98a97a6229686bf334f88c000c1ef95a`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_user_provided_behavior_baseline` | FAIL | With-skill output calls this an existing behavior change but never explicitly establishes the user-provided rule that the active list currently excludes archived as the approved baseline. |
| `classifies_expectation_change` | PASS | It explicitly classifies the request as an existing-behavior change and recommends impact analysis before implementation. |
| `routes_to_existing_project_update` | FAIL | It names the existing-project-update path but does not route to pm-agent:idea-to-spec or require recording a new product decision and then synchronizing the TRD. |
| `routes_trd_gap_to_trd_gen` | NOT_EXERCISED | The locked fixture is empty and the candidate reports no product documents, so the condition of an established PRD/product decision with a missing or stale TRD is not evidenced. |
| `requires_plan_after_alignment` | FAIL | The output says to hand off to engineering after confirming acceptance criteria, but does not require PRD/TRD alignment or an IMPLEMENTATION_PLAN.md before implementation. |
| `does_not_route_directly_to_implementation` | PASS | It does not directly start implementation and explicitly places confirmation and impact analysis before the engineering handoff. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d08d04c31266e7709df236e5a84b0516db051d4099fdd86927601fc672aa3954; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=a03ccf8f09c541accc8dd45f84218658526b97ee7b9714941df41c23eff36519; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Recognizes an existing behavior change and avoids immediate coding, but omits the required named PM route, baseline statement, and implementation-plan requirement.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d08d04c31266e7709df236e5a84b0516db051d4099fdd86927601fc672aa3954; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=7b1ea33afe719f90ded8550e5809f34363dce6c187ef6082eb8553c3112a3f57; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides general semantic-change and impact-analysis advice, but does not route through the required product/TRD workflow.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with-skill output does not explicitly use the user-provided active-excludes-archived rule as the approved baseline.
- It omits the required pm-agent:idea-to-spec existing-project-update routing and product-decision/TRD synchronization step.
- It omits the required PRD/TRD alignment and IMPLEMENTATION_PLAN.md gate before engineering implementation.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `engineer-agent`
- Eval: `eval-002-existing-feature-alignment-gate`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/engineer/test/engineer-agent/evals/workspace/eval-002-existing-feature-alignment-gate`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `d08d04c31266e7709df236e5a84b0516db051d4099fdd86927601fc672aa3954`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8d8fb0fa400e90f6295a8210be17110ea5dbf40c02704b7c3c2d90e5fd3722a5`
- Skill overlay SHA-256: `5d21e5d4fde13b79efe9b8a3a45224c9f9295ffd2ea23291a6557ce52b7a55ce`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `35bf0057341046be2b5db3cd90c99d825b61efaf315ed25428b5eda571894209`
- Metadata SHA-256: `43542dab517c382c8ae0bc3c7332df9e98a97a6229686bf334f88c000c1ef95a`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_user_provided_behavior_baseline` | FAIL | with_skill 未明确把“active 列表排除 archived”表述为当前批准基线；仅泛称旧规则，并说明工作区无产品文档。 |
| `classifies_expectation_change` | PASS | with_skill 明确建议按“产品约定变更”推进，而不是直接改查询条件，并指出 active 可能具有更广语义。 |
| `routes_to_existing_project_update` | FAIL | 未提及 `pm-agent:idea-to-spec` 或 `existing-project-update`，也未明确要求先记录新产品决定再同步 TRD。 |
| `routes_trd_gap_to_trd_gen` | FAIL | 未构造 TRD gap packet，也未交回 `engineer-agent:trd-gen` 补完整 TRD 或记录 open questions。 |
| `requires_plan_after_alignment` | FAIL | 未明确要求 PRD/TRD 对齐后才进入 `feature-implementor`，也未产出或引用 `IMPLEMENTATION_PLAN.md`。 |
| `does_not_route_directly_to_implementation` | PASS | with_skill 未将请求直接交给 `feature-implementor`，而是先建议确认规则、更新产品文档或决策并进行技术评估。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d08d04c31266e7709df236e5a84b0516db051d4099fdd86927601fc672aa3954; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=777d24c1104c16b8d7e8a3d5f5564ecd7ddbf81a74cd6debf5de7fd798240531; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别为产品约定变更并提出文档、影响面和验证步骤，但缺少规定的 PM、TRD gap 和实施计划路由。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d08d04c31266e7709df236e5a84b0516db051d4099fdd86927601fc672aa3954; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=83cdb047392c4dd6fde2384b74c79f5a1f0fefe4a7266c3b92e52e875eafb9b0; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 基于代码定位、测试和实现建议推进，未处理现行批准行为与产品/TRD 对齐路径。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未完整满足现行行为基线、PM existing-project-update、TRD gap packet/trd-gen 以及对齐后 IMPLEMENTATION_PLAN.md 要求。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `engineer-agent`
- Eval: `eval-002-existing-feature-alignment-gate`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/engineer/test/engineer-agent/evals/workspace/eval-002-existing-feature-alignment-gate`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `d08d04c31266e7709df236e5a84b0516db051d4099fdd86927601fc672aa3954`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `83f220b482f661eab0884cc4770c84fbb545af7bd74199e0b9f4ba499020031a`
- Skill overlay SHA-256: `94585e968fb2a0b5b29dd98429a0ee0f98e86ec73794257bcf099dd92d775e4c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `35bf0057341046be2b5db3cd90c99d825b61efaf315ed25428b5eda571894209`
- Metadata SHA-256: `43542dab517c382c8ae0bc3c7332df9e98a97a6229686bf334f88c000c1ef95a`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_user_provided_behavior_baseline` | PASS | with_skill 保留 active 的原定义，并未声称读取不存在的 PRD、TRD 或决策文件。 |
| `classifies_expectation_change` | PASS | with_skill 明确将其归为“现有功能行为变更”，而非直接按小改动处理。 |
| `routes_to_existing_project_update` | FAIL | 未路由到 pm-agent:idea-to-spec 的 existing-project-update 路径，也未要求记录产品决定后同步 TRD。 |
| `routes_trd_gap_to_trd_gen` | FAIL | 工作区 fixture 为空且输出确认缺少业务文档，但未构造 TRD gap packet 或交回 engineer-agent:trd-gen。 |
| `requires_plan_after_alignment` | FAIL | 仅泛称形成变更说明/技术方案，未要求 PRD/TRD 对齐后进入 feature-implementor，并先产出或引用已确认的 IMPLEMENTATION_PLAN.md。 |
| `does_not_route_directly_to_implementation` | PASS | with_skill 未将请求直接交给 feature-implementor 开始编码，且要求先确认需求。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d08d04c31266e7709df236e5a84b0516db051d4099fdd86927601fc672aa3954; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=eee995dd908fa613f2d9a3554011a27ff187fd4e7fdf6c5a050388f855f9ab9e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别为现有功能行为变更并暂停代码修改，但缺少指定的 PM existing-project-update、TRD gap 及实施计划路径。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d08d04c31266e7709df236e5a84b0516db051d4099fdd86927601fc672aa3954; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=36d558d7b95851c2f74ccc1bbc85efe10859a63aa4404d0c25ac1b1ca131955f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了需要产品语义确认和影响分析，但未体现受批准基线冲突后的产品/TRD 路由。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足 existing-project-update 路由要求。
- with_skill 未满足 TRD gap packet 回交 trd-gen 要求。
- with_skill 未满足对齐后 IMPLEMENTATION_PLAN.md 要求。
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
