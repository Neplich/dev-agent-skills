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

- Behavior result: `FAIL`（with）/ `FAIL`（without）— 本轮 #238 fresh 隔离重跑（2026-08-06）
- Coverage result: `FULL`（with）/ `FULL`（without）— 本轮重跑实际触发的断言场景
Overall result: FAIL
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `FAIL` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `preserves_complete_version_identity` | PASS | PASS | 两条产物均确认 `v1.2.0-rc.1+Build.7` 为完整 identity，并指出前缀、大小写、预发布标识和 build metadata 不能被丢失或视为等价（with_skill: `result.txt:5,7,17`；without_skill: `result.txt:6-8,23`）。 |
| `enforces_each_source_contract` | PASS | PASS | 均按来源识别 raw form、selector/extractor 和缺失值问题；未用其他来源补值，也未静默修复非法值（with_skill: `result.txt:7,12-16`；without_skill: `result.txt:8,16-25`）。 |
| `reports_all_version_blockers` | PASS | PASS | 两条产物均覆盖大小写/前缀非法、缺失、非 SemVer、selector 解析失败、重复匹配、extractor 不一致及 identity 差异，并分别给出发布前和发布后的失败结论（with_skill: `result.txt:8,12-18`；without_skill: `result.txt:10,14-27`）。 |
| `binds_pre_and_post_tag_inventory` | FAIL | FAIL | 产物仅列出 pre-tag 的 6 个来源和 post-tag 的 7 个来源，没有说明 pre-tag 如何固化完整来源集合，也没有说明 post-tag 消费同一绑定；with_skill: `result.txt:6`，without_skill: `result.txt:5`。 |
| `makes_inventory_integrity_reproducible` | FAIL | FAIL | 产物提到 selector 数量、匹配数量和 extractor identity，但没有给出可独立重算的 inventory integrity 证据，也没有说明来源集合、定位契约或顺序被篡改时如何阻止阶段成功（with_skill: `result.txt:13-14,18`；without_skill: `result.txt:19-25,27`）。 |

未满足断言：``binds_pre_and_post_tag_inventory``、``makes_inventory_integrity_reproducible``


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
- 将历史 issue locator 替换为 `docs-agent:release-notes-gen`。

## Assertion Results
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

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
