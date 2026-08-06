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
