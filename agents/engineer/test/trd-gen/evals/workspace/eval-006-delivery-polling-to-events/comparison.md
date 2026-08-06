# Eval Result: eval-006-delivery-polling-to-events

## Evaluation Target

- Agent: `engineer`
- Skill: `trd-gen`
- Eval: `eval-006-delivery-polling-to-events`
- Test case: delivery-polling-to-events
- Workspace: `workspace/eval-006-delivery-polling-to-events`
- Latest result: PASS - 2026-08-06 third fresh paired validation completed（frontmatter changelog 口径）；with_skill 4/4 assertions passed，without_skill 3/4。
- Behavior result: PASS — with_skill 实际触达路径满足全部 4 条断言（正文、版本与 changelog 事实一致）。
- Coverage result: FULL — 4/4 assertion scenarios were exercised; no `NOT EXERCISED` items.
Overall result: PASS

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: delivery-pipeline PRD v1.2.0（事件驱动已确认）与 TRD v1.1.0（定时轮询旧方案：60 秒扫描、`poller.ts` / `batch.ts`）
- Expected output: 更新 docs/engineer/delivery-pipeline/TRD.md：正文直接描述事件驱动方案，轮询旧方案从正文移除并留痕，不进入实现计划或代码。
- Fresh run: `2026-08-06`（issue #233 新增 eval 首跑，codex exec `gpt-5.6-luna` + `model_reasoning_effort=medium`，仓库外 workspace 拷贝隔离，两 lane 独立拷贝互不可见；independent judge 对照 4 条断言判定）
- Runtime directory: `tmp/eval-runs/fix-233/trd-gen-eval-006-delivery-polling-to-events/`（不入 git）

## Assertions

- PASS `updates_existing_trd`: 两条 lane 均更新目标 `docs/engineer/delivery-pipeline/TRD.md`，未新建 feature 文档或转交任务。
- PASS `body_consolidation`: 两份正文均改写为事件驱动方案；60 秒扫描、`poller.ts`、`batch.ts` 旧方案细节已移除，仅保留「不再使用轮询」的当前约束，无「已废弃」等状态标注。
- PASS `removal_recorded_in_changelog`（with）/ FAIL（without）: with_skill 在 frontmatter 新增 `changelog` 结构（version/date/summary）记录删除并同步版本 `1.1.0 -> 1.2.0`（对应 trd-gen SKILL.md「无 changelog 结构则新增到 frontmatter」指令）；without_skill 仅更新版本号，无 changelog 留痕。该断言在 frontmatter 口径下具备判别力。
- PASS `no_implementation_plan_or_code`: 两条 lane 均未生成 `IMPLEMENTATION_PLAN.md`、修改代码或补测试。

## With Skill

第三轮重跑（frontmatter 口径 + SKILL.md「无 changelog 结构则新增到 frontmatter」指令）：更新后的 TRD 与已确认 PRD 对齐，`delivery.created` 事件驱动方案、状态机、重试队列与 dead-letter；正文直接改写；**frontmatter 新增 `changelog` 结构**（version/date/summary）记录删除并同步版本 `1.1.0 -> 1.2.0`；未进入实现。

## Without Skill

同一 prompt 与 fixture 下新建 baseline（codex `gpt-5.6-luna`，workspace 无 skill 文档）。baseline 同样完成事件驱动改写与版本 bump，但**未新增 changelog 留痕**（仅版本号与 last_updated 更新）。baseline 回复提及 `pm-agent` / `trd-gen` 名称——该仓库为公开仓库，模型先验知识中存在 skill 体系名称，非 lane 泄漏。

## Conclusion

**Skill impact:** MEDIUM

frontmatter 口径下 `removal_recorded_in_changelog` 断言具备判别力（with PASS / without FAIL）：skill 加载后按「无 changelog 结构则新增到 frontmatter」指令补留痕，baseline 遗漏。事件驱动改写与正文收束仍属模型基线能力（两条 lane 均满足），但删除留痕纪律是 skill 带来的可观测差异。该 eval 保留为正文收束与删除留痕的回归覆盖。

## Runtime Artifact(s) Policy

- with/without lane 产物、workspace 更新后的 TRD、judge verdict 均在 `tmp/eval-runs/fix-233/` 下，不入 git。
