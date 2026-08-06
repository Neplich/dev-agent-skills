# Eval Result: eval-006-delivery-polling-to-events

## Evaluation Target

- Agent: `engineer`
- Skill: `trd-gen`
- Eval: `eval-006-delivery-polling-to-events`
- Test case: delivery-polling-to-events
- Workspace: `workspace/eval-006-delivery-polling-to-events`
- Latest result: PASS - 2026-08-06 fresh paired validation completed; with_skill and fresh without_skill both satisfied 4/4 assertions.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: delivery-pipeline PRD v1.2.0（事件驱动已确认）与 TRD v1.1.0（定时轮询旧方案：60 秒扫描、`poller.ts` / `batch.ts`）
- Expected output: 更新 docs/engineer/delivery-pipeline/TRD.md：正文直接描述事件驱动方案，轮询旧方案从正文移除并留痕，不进入实现计划或代码。
- Fresh run: `2026-08-06`（issue #233 新增 eval 首跑，codex exec `gpt-5.6-luna` + `model_reasoning_effort=medium`，仓库外 workspace 拷贝隔离，两 lane 独立拷贝互不可见；independent judge 对照 4 条断言判定）
- Runtime directory: `tmp/eval-runs/fix-233/trd-gen-eval-006-delivery-polling-to-events/`（不入 git）

## Assertions

- PASS `updates_existing_trd`: 两条 lane 均更新目标 `docs/engineer/delivery-pipeline/TRD.md`，未新建 feature 文档或转交任务。
- PASS `body_consolidation`: 两份正文均改写为事件驱动方案；60 秒扫描、`poller.ts`、`batch.ts` 旧方案细节已移除，仅保留「不再使用轮询」的当前约束（with 的「非目标」节与 without 的「实施约束」节），无「已废弃」等状态标注。
- PASS `removal_recorded_in_changelog`: 原始 TRD 无 changelog 结构（TRD schema 不含 changelog 字段），按断言适配口径以版本号 `1.1.0 -> 1.2.0` 与 `last_updated` 更新作为删除留痕。
- PASS `no_implementation_plan_or_code`: 两条 lane 均未生成 `IMPLEMENTATION_PLAN.md`、修改代码或补测试。

## With Skill

更新后的 TRD 与已确认 PRD 对齐：`delivery.created` 事件发布、异步消费者、状态机（pending → processing → delivered）、重试队列与 dead-letter、验证项与 P0 目标；正文直接改写、版本 bump、未进入实现。

## Without Skill

同一 prompt 与 fixture 下新建 baseline（codex `gpt-5.6-luna`，workspace 无 skill 文档）。baseline 同样完成事件驱动改写与版本 bump，产物更泛化（中间件留待实现阶段确定），并编造了 frontmatter `author: 用户 / Codex` 字段（原始 fixture 无 author）；未进入实现。baseline 回复提及 `pm-agent` / `trd-gen` 名称——该仓库为公开仓库，模型先验知识中存在 skill 体系名称，非 lane 泄漏。

## Conclusion

**Skill impact:** LOW

本次断言下未形成 with/without 行为差异：两条 lane 均满足全部 4 条断言。事件驱动改写、正文收束、版本留痕属于模型基线能力已覆盖的行为（对应 AGENTS.md 判定表「模型基线能力已覆盖该行为 → 记为 skill 生命周期信号」）。skill 加载后的可观测差异在产物细节：with 产出具体模块结构（publisher/consumer/retry/status）与状态机，baseline 为泛化模板且编造 frontmatter 字段。该 eval 保留为正文收束与不越界的回归覆盖，判别力观察点可考虑后续增强（如断言覆盖模块具体性或不编造字段纪律）。

## Runtime Artifact(s) Policy

- with/without lane 产物、workspace 更新后的 TRD、judge verdict 均在 `tmp/eval-runs/fix-233/` 下，不入 git。
