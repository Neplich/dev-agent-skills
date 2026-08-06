# Eval Result: eval-009-prd-iteration-split-proposal

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec` (`prd-iteration` lane)
- Eval: `eval-009-prd-iteration-split-proposal`
- Workspace: `workspace/eval-009-prd-iteration-split-proposal`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: current workspace atop HEAD `68c86669`（#234 泄漏修复后）。The fixture remains the confirmed level-1 `notification-center` PRD with no child directory, 3 domains, 10 user stories, 8 functional requirements, and a polling-based Engineer TRD. The case exercises the L2b gate and the body-consolidation rule added by issue #233.
- Fresh run: `2026-08-06`（issue #233 重跑，codex exec `gpt-5.6-luna` + `model_reasoning_effort=medium`，仓库外 workspace 拷贝隔离，两 lane 独立拷贝互不可见；independent judge 对照 6 条断言判定）
- Runtime directory: `tmp/eval-runs/fix-233/idea-to-spec-eval-009-prd-iteration-split-proposal/`（含 with/without lane 产物与 judge verdict，不入 git）

## Latest Result

- Behavior result: FAIL — with_skill 满足 4/6 断言（应用变更、L2b 识别、提案-确认制、正文收束），未满足「完整拆分提案三件套」与「拒绝语义」两条既有断言。
- Coverage result: FULL — 6/6 assertion scenarios were exercised; no `NOT EXERCISED` items.
Overall result: FAIL

## Assertion Results

- `applies_requested_change`: PASS (with) / FAIL (without) — with_skill 实际更新 PRD：FR-02 与 Delivery Strategy 改写为事件驱动，版本 `1.3.0 -> 2.0.0`，frontmatter 与 inline changelog 记录；without_skill 未写盘，PRD 与原始 fixture 一致。
- `detects_l2b_signals`: PASS (both) — 两条 lane 均明确识别 3 个独立领域与 18 行 US/FR 需求。
- `presents_split_proposal`: FAIL (both) — with_skill 给出拆分子 `feature_path` 树并等待确认，但未给出章节迁移映射与下游镜像影响清单；without_skill 同样缺少完整下游镜像清单。
- `waits_for_confirmation`: PASS (both) — 两条 lane 均要求确认后再拆分，workspace 无子 feature_path、新文档或移动动作。
- `rejection_keeps_current_flow`: FAIL (both) — with_skill 未说明拒绝后的继续流程（版本 bump 与校验）；without_skill 仅说明保留单一 PRD。
- `body_consolidation`（#233 新增）: PASS (with) / FAIL (without) — with_skill 正文直接改写为事件驱动，无「已废弃/不属于目标架构」标注残留；without_skill 正文保留轮询方案。

## With-Skill Behavior

实际更新了 PRD（事件驱动改写、版本 bump、changelog 记录、未动 TRD、未拆分移动），识别 L2b 信号并给出子 feature_path 树，明确等待确认。本轮 with lane 未输出完整拆分提案三件套（缺章节迁移映射与镜像影响清单），也未描述拒绝后的继续流程——`prd-iteration` Step 4 要求一次给出三件套再等确认，本轮行为不完整，是 eval 暴露的真实行为差距，建议后续跟进（可能与模型输出长度或执行细化有关）。

## Fresh Without-Skill Baseline

同一 prompt 与 fixture 下新建 baseline（codex `gpt-5.6-luna`，workspace 无 skill 文档）。baseline 未写盘（PRD 与原始一致），识别了 L2b 信号并给出拆分方向，未完成完整提案，未执行正文更新。Baseline result: 2/6 assertions passed。baseline 输出中提及 `pm-agent` / `prd-iteration` 名称——该仓库为公开仓库，模型先验知识中存在 skill 体系名称，非 lane 泄漏。

## Judge Conclusion

独立 judge（codex `gpt-5.6-luna`）对照 fixture、两 lane 产物与 6 条断言判定。正文收束断言具备判别力（with PASS / without FAIL，skill 加载后直接改写正文而非保留标注）；完整拆分提案与拒绝语义两条既有断言两条 lane 均未满足，Behavior 记 FAIL，如实反映本轮行为差距。

## Failures

- with_skill：`presents_split_proposal`（缺章节迁移映射与镜像影响清单）、`rejection_keeps_current_flow`（未说明拒绝后流程）未满足。
- without_skill：`applies_requested_change`、`presents_split_proposal`、`rejection_keeps_current_flow`、`body_consolidation` 未满足。

## Next Steps

- 保留本 eval 作为 PRD 迭代正文收束与 L2b 门禁的回归覆盖；`body_consolidation` 断言继续有效。
- 跟进 with lane 拆分提案不完整问题（完整三件套 + 拒绝语义），可交 issue 审查或在下轮 skill eval 中复核。
- 历史结论：`2026-08-03` 旧契约（泄漏版 eval 定义）下 5/5 PASS，已按 #234 规则标记失效并待重跑，本次重跑解除 BLOCKED。

## Runtime Artifact(s) Policy

- with/without lane 产物、workspace 更新后的 PRD、judge verdict 均在 `tmp/eval-runs/fix-233/` 下，不入 git。
