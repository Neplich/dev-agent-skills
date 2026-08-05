# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-013-version-normalization-boundaries`
- Scenario: 多来源版本 identity、selector 边界与跨阶段 inventory 完整性
- Review context: issue #177 sub-batch 4b

## Test Set / Fixture Version

- Fixture version: `issue-177 discrimination restore round-1`
- Validation time: `2026-07-28 22:48:16 CST`
- Runtime: `tmp/eval-runs/issue-177/docs-audit/round-1/`
- Assertions: 5，全部实际触发

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL**（5/5 assertions exercised）
Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。

- With-skill: **5/5 PASS**
- Fresh without-skill: **3/5 PASS、2/5 FAIL**
- Relative uplift: **+2 assertions**

两臂都保留 prerelease/build/case identity，并逐来源识别 raw form、缺失、歧义 selector 和 unknown extractor。with-skill 额外要求 pre-tag inventory 预先包含 future actual-tag source 并记录 pending state，post-tag 只能消费同一 inventory；同时给出可独立重算的 canonical inventory digest。baseline 把 tag 当作 post-tag 新增来源，且没有提供稳定 serialization/digest 算法。

## Leakage Surface Analysis

重做前，prompt、assertions 和 `version-cases.md` 直接给出前缀算法、完整 expected identity、case/build 判定、全部 blocker、六字段 inventory、canonical serialization、预计算 digest 和 pre/post producer-consumer 答案。

重做后，fixture 只保留 source locator table、pre/post observed source ids 和 observation sets，不给 expected identity、valid/invalid 标签、canonical rules、digest 或阶段裁定。

## Redesign

- prompt 只要求分别给出两阶段 identity、全部 blocker、持久化证据与结论。
- assertions 改为完整 identity、source contract、全量 blocker、跨阶段 inventory binding 和 reproducible integrity 五个语义结果。
- 删除预计算 digest、canonical 答案、invalid 原因标签和 producer/consumer 指令。
- 增加 phase-boundary 变体：pre-tag declared source ids 缺少 future `tag`，post-tag observations 才出现该来源。
- 保留多版本 index 的双匹配、absent JSON Pointer 与 unknown extractor 原始观测。
- 将历史 issue locator 替换为 `docs-agent:release-notes-generator`。

## Assertion Results

| Assertion | With skill | Without skill | Fresh judgment |
| --- | --- | --- | --- |
| `preserves_complete_version_identity` | PASS | PASS | 两臂均保留 prerelease、build metadata 与大小写。 |
| `enforces_each_source_contract` | PASS | PASS | 两臂均逐来源拒绝 raw-form、selector 与 extractor 问题。 |
| `reports_all_version_blockers` | PASS | PASS | 两臂均覆盖缺失、非法、歧义和 identity 不一致类别。 |
| `binds_pre_and_post_tag_inventory` | PASS | FAIL | skill arm要求 pre-tag 固定 future tag pending source；baseline 将 tag 当作 post-tag 新增来源。 |
| `makes_inventory_integrity_reproducible` | PASS | FAIL | skill arm给出 canonical JSON、稳定排序、digest 重算和篡改阻塞；baseline 只有字段列表。 |

## Fresh Validation Method

- 两臂锁定前只读取同一 prompt 和 `version-cases.md`，未读取 assertions、expected output、旧 comparison 或对方输出。
- with-skill arm读取完整 Docs/docs-audit 指令；without-skill arm隔离这些内容。
- fresh judge 在 SHA-256 锁定后才读取 assertions。
- with-skill SHA-256：`210a4836d46b095ef9ad18943784c5dcc55df4c9693a46a1351010c3bdab11b3`；without-skill：`e053ee70e2330b8c7b5138a57bdb1ce189170489dd169b5d182bf2fd8a068d9b`。

## Failures And Limitations

- with-skill 无失败；Coverage FULL。
- source table 仍暴露 raw forms、selector 和 extractor，所以 baseline 可恢复 3/5；区分度来自跨阶段 future-tag binding 与 canonical integrity。
- 第一轮即达到区分度，无需第二轮。

## Runtime Artifact Policy

- runtime responses 和 judge verdict 仅保存在 `tmp/eval-runs/issue-177/docs-audit/round-1/`，不提交。
- 本 `comparison.md` 是唯一 durable 结果。
