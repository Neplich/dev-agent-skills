# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-009-release-product-ops`
- Scenario: release 模式下未确认的 Product 原子 mapping closure 与冲突 Ops 证据
- Review context: issue #177 sub-batch 4c

## Test Set / Fixture Version

- Fixture version: `issue-177 discrimination restore round-2`
- Validation time: `2026-07-28 23:36:25 CST`
- Runtime: `tmp/eval-runs/issue-177/docs-release-evals/round-2/`
- 两侧使用同一最终 prompt 和独立 pristine fixture；with-skill 不读取 assertions，without-skill 不读取或应用目标 skill、Docs README、旧 comparison、历史 baseline 或 with-skill 输出。

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL**（5/5 assertions exercised）
- Overall result: PASS
- With-skill: **5/5 PASS**
- Fresh without-skill: **1/5 PASS、4/5 FAIL**
- Relative uplift: **+4 assertions**，通过率从 20% 提升到 100%。

## Leakage Surface Analysis

重做前，prompt 直接给出只更新哪两页、Release Notes 零变化、`unverified`、宿主检查与 docs-audit handoff；assertions 进一步写出精确版本事实、页面路径和 handoff 字段。fixture 又把两张叶子页及 mapping 描述为已确认成功范围，baseline 可按答案写入。

第一轮移除这些执行答案并加入 runtime 原始冲突后，双方仍都识别 v1.4.0/v1.5.0 镜像冲突并只更新 Product，结果同为 5/5。第二轮改为只确认两个叶子候选；Product root 缺少到叶子的直接链接，现有 change-map 也没有包含 ancestor index 的原子 closure。fixture 只提供这些原始状态，不声明判定。

## Redesign

- prompt 只要求依据 handoff 与证据完成同步并报告结果。
- assertions 改为候选闭包确认、冲突 Ops、Release Notes boundary、全站零 diff 和双 blocker owner 五个语义结果。
- Product 叶子事实本身有实现/测试证据，但 ancestor index 与扩展 mapping closure 未经提出和确认。
- Ops 保留 release 摘要、checked-in v1.4.0 配置和缺失 runtime check 的冲突。

## Assertion Results

| Assertion | With skill | Without skill | Fresh judgment |
| --- | --- | --- | --- |
| `detects_unconfirmed_product_mapping_closure` | PASS | FAIL | with-skill 识别叶子、祖先 index、直接链接和 change-map closure 是原子范围并停止；baseline 直接写 Product 叶页。 |
| `keeps_conflicting_ops_candidate_unchanged` | PASS | FAIL | with-skill 保持 Ops 零写入；baseline 虽披露冲突仍修改 Ops 页。 |
| `preserves_release_notes_surfaces` | PASS | PASS | 两侧均未触碰独立 Release Notes 交付面。 |
| `keeps_entire_site_zero_diff` | PASS | FAIL | with-skill 正式站点零差异；baseline 修改 Product 与 Ops 两页。 |
| `separates_scope_and_technical_blockers` | PASS | FAIL | with-skill 分别返回维护者确认完整闭包与 release engineering 补技术证据；baseline 未把 Product closure 当 blocker，并运行写后检查。 |

## With-Skill Behavior

- 在写前候选确认门禁停止，Product、Ops、index、change map 与 Release Notes surfaces 均保持 pristine。
- 分开报告 Product scope-confirmation gap 和 Ops evidence gap，没有运行写后宿主检查，也没有输出成功审计 handoff。
- Response SHA-256: `129c10dd2d93e72b0de3c5d83eb4e2d56a1d32615f7f9e4be25d603e6c1b6b1f`。

## Fresh Without-Skill Baseline

- baseline 将“只确认叶子”当作允许窄写入，修改 Product 与 Ops 两页；没有补 ancestor index 或 change-map closure。
- 它运行 `npm run test:docs` 并通过 74/74，但检查通过不能替代写前范围确认。
- Response SHA-256: `86a6069a37a0ee0ef43b159fc68c1aebbc0bb61946deb93e92d9be4f73cf172e`。

## Failures And Iterations

- Round 1：with-skill 5/5、baseline 5/5；冲突对 baseline 也足够明显，无区分度。
- Round 2：with-skill 5/5、baseline 1/5；Behavior PASS、Coverage FULL。
- 基础设施失败：none。

## Next Steps

- 保持本例为 release mode 的写前 atomic closure 回归；若候选确认或 change-map closure 协议变化，重新执行 fresh paired validation。

## Runtime Artifact Policy

- responses、workspace 副本、依赖、日志和 judge verdict 仅位于 gitignored `tmp/eval-runs/issue-177/docs-release-evals/`，不提交。
- 本 `comparison.md` 是唯一 durable eval 结果。
