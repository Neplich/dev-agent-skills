# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-009-prd-iteration-split-proposal`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `cda1a0661ddb58fa697ce0a283dc50943986240370fdcd97782d5714af75a997` from `agents/product_manager/test/idea-to-spec/workspace/eval-009-prd-iteration-split-proposal`.
- Fixture SHA-256: `cda1a0661ddb58fa697ce0a283dc50943986240370fdcd97782d5714af75a997`
- Prompt SHA-256: `ae03344941a8a5473fce84f07af68d8bb42c4c4dd8dbaf557b909886adf20c98`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9c3b136c6958582b2c5c3d552759bbe4fd3ef24876075804e91c5b21980a34af`
- Skill overlay SHA-256: `e4cc003a0e06320ef354c6c9cdbebb2b75980ec8b23ae530ac78b0667fab31da`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `8ef466ccd13d937453c02f105817ced47839fb573011ea1ee300be62facb6b71`
- Metadata SHA-256: `ae189abbce9ec160b22d49ab4f79a0a7a8f521d1a6e2046930669caf75d7dab0`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `applies_requested_change` | PASS | with_skill 的 PRD diff 将 FR-02 和 Delivery Strategy 从轮询改为事件驱动，并更新验收标准与版本至 1.4.0。 |
| `detects_l2b_signals` | FAIL | with_skill 输出未明确识别 L2b 信号；fixture PRD 实际包含 3 个独立领域且 US/FR 表格行数达到至少 15 行。 |
| `presents_split_proposal` | FAIL | with_skill 输出未提供子 feature_path 树、章节迁移映射或 docs/engineer、docs/design、docs/qa/e2e、docs/devops、docs/security 的下游镜像影响清单。 |
| `waits_for_confirmation` | FAIL | with_skill 输出未提出等待用户确认，也未明确确认前不拆分、不 git mv、不新建子 feature_path 文档。 |
| `rejection_keeps_current_flow` | FAIL | with_skill 输出未说明拒绝提案时保持当前 feature_path 并按现流程继续版本 bump 与校验。 |
| `body_consolidation` | PASS | with_skill 的更新 PRD 正文将 FR-02 和 Delivery Strategy 直接写为事件驱动方案；轮询仅出现在迁移回滚约束中，未作为当前目标状态保留。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ae03344941a8a5473fce84f07af68d8bb42c4c4dd8dbaf557b909886adf20c98; fixture_sha256=cda1a0661ddb58fa697ce0a283dc50943986240370fdcd97782d5714af75a997; output_sha256=9ed423c86d556ab0159f5eb6040d5824bb8dd72f4272783ac6606fab842c4605; snapshot_sha256=9e88411ff498b3e04522c5823543b55298043abb450ed8d3039f9dcf47fb5069
- Behavior: 实际更新了 PRD 并改为事件驱动，补充去重、迁移和回滚约束，但未输出要求的 L2b 拆分提案与确认流程。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ae03344941a8a5473fce84f07af68d8bb42c4c4dd8dbaf557b909886adf20c98; fixture_sha256=cda1a0661ddb58fa697ce0a283dc50943986240370fdcd97782d5714af75a997; output_sha256=f91750147d5065fca7b5c058800c74385afb8f5e8889b6de77de5daef1c94f0b; snapshot_sha256=f3af49fe8f799a9079f7b713cbd614343a21e62eab184a66af90a5438c18c0b7
- Behavior: 实际更新了 PRD 并改为事件驱动，但未处理 L2b 拆分识别、提案、确认制及拒绝语义。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- detects_l2b_signals
- presents_split_proposal
- waits_for_confirmation
- rejection_keeps_current_flow
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

# Eval Result: eval-009-prd-iteration-split-proposal

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec` (`prd-iteration` lane)
- Eval: `eval-009-prd-iteration-split-proposal`
- Workspace: `workspace/eval-009-prd-iteration-split-proposal`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: current workspace atop HEAD `68c86669`（#234 泄漏修复后）。The fixture remains the confirmed level-1 `notification-center` PRD with no child directory, 3 domains, 10 user stories, 8 functional requirements, and a polling-based Engineer TRD. The case exercises the L2b gate and the body-consolidation rule added by issue #233.
- Fresh run: `2026-08-06`（issue #233 最终 harness 重跑，codex exec `gpt-5.6-luna` + `model_reasoning_effort=medium`；两 lane 独立 workspace，均含剥离 test 的 agents/ 依赖镜像（可见上下文一致），with lane 额外在 `.agents/skills` 暴露入口 skill；HOME + CODEX_HOME 隔离（auth 从活跃 CODEX_HOME 复制）；README / eval_metadata.json / comparison.md 已物理排除；independent judge 对照 6 条断言判定）
- Runtime directory: `tmp/eval-runs/fix-233/idea-to-spec-eval-009-prd-iteration-split-proposal/`（含 with/without lane 产物与 judge verdict，不入 git）

## Latest Result

- Behavior result: FAIL — with_skill 满足 3/6 断言（L2b 识别、完整拆分提案、提案-确认制），未满足「应用请求的变更」「拒绝语义」「正文收束」（最终 harness 下 with lane 停在 L2b 提案等待确认，未写正文；without lane 直接改写 PRD 为事件驱动）。
- Coverage result: FULL — 6/6 assertion scenarios were exercised; no `NOT EXERCISED` items.
Overall result: FAIL

## Assertion Results

- `applies_requested_change`: FAIL (with) / PASS (without) — with_skill 停在 L2b 提案等待确认，未更新 PRD 正文（版本仍 1.3.0）；without_skill 直接改写 FR-02 与 Delivery Strategy 为事件驱动，版本 `1.3.0 -> 1.4.0`。
- `detects_l2b_signals`: PASS (with) / FAIL (without) — with_skill 明确识别 3 个独立领域与 18 行 US/FR 需求；without_skill 未识别 L2b。
- `presents_split_proposal`: PASS (with) / FAIL (without) — with_skill 给出 feature_path 树、章节迁移映射与五类下游镜像影响清单；without_skill 无拆分提案。
- `waits_for_confirmation`: PASS (with) / FAIL (without) — with_skill 明确等待确认且未执行拆分/移动；without_skill 直接修改 PRD，未执行确认制。
- `rejection_keeps_current_flow`: FAIL (both) — 两条 lane 均未说明拒绝后保留当前 feature_path 并按现流程继续（版本 bump 与校验）。
- `body_consolidation`（#233 新增）: FAIL (with) / PASS (without) — with_skill 未写正文（轮询描述仍在）；without_skill 直接改写为事件驱动，无「已废弃/不属于目标架构」标注残留。

## With-Skill Behavior

最终 harness（双 lane 同镜像 + 入口 skill 发现）下，with lane 按 skill 协议识别 L2b 信号并给出完整拆分提案（树 + 迁移映射 + 下游镜像清单），明确等待确认，因此未在确认前写正文。产物停留在「提案-确认制」阶段，未满足「应用请求的变更」与「正文收束」断言——`prd-iteration` 协议要求 Step 3 先应用变更再于 Step 4 评估拆分，本轮行为跳过正文更新直接提案，是 eval 暴露的真实行为差距，建议后续跟进（协议顺序执行或确认后补写正文）。

## Fresh Without-Skill Baseline

同一 prompt 与 fixture 下新建 baseline（codex `gpt-5.6-luna`，workspace 无入口 skill 发现）。baseline 直接完成轮询→事件驱动改写（版本 1.4.0），未识别 L2b、无拆分提案、无确认制。Baseline result: 2/6 assertions passed。baseline 输出中提及 `pm-agent` / `prd-iteration` 名称——该仓库为公开仓库，模型先验知识中存在 skill 体系名称，非 lane 泄漏。

## Judge Conclusion

独立 judge（codex `gpt-5.6-luna`）对照 fixture、两 lane 产物与 6 条断言判定。最终 harness 下 with lane 停在 L2b 提案-确认制阶段（3/6 PASS），正文未更新；without lane 直接改写（2/6 PASS）。Behavior 记 FAIL，如实反映「协议顺序执行」（Step 3 应用变更应在 Step 4 拆分评估之前）的行为差距。

## Failures

- with_skill：`applies_requested_change`（未写正文）、`rejection_keeps_current_flow`（未说明拒绝后流程）、`body_consolidation`（正文未更新）未满足。
- without_skill：`detects_l2b_signals`、`presents_split_proposal`、`waits_for_confirmation`、`rejection_keeps_current_flow` 未满足。

## Next Steps

- 保留本 eval 作为 PRD 迭代正文收束与 L2b 门禁的回归覆盖；`body_consolidation` 断言继续有效。
- 跟进 with lane 协议顺序执行问题（先应用变更再评估拆分，拒绝语义补齐），可交 issue 审查或在下轮 skill eval 中复核。
- 历史结论：`2026-08-03` 旧契约（泄漏版 eval 定义）下 5/5 PASS，已按 #234 规则标记失效；早期 harness 阶段（无 agents 镜像）重跑结论与最终 harness 结论均记录在案，最终以本次为准。BLOCKED 已解除。

## Runtime Artifact(s) Policy

- with/without lane 产物、workspace 更新后的 PRD、judge verdict 均在 `tmp/eval-runs/fix-233/` 下，不入 git。
