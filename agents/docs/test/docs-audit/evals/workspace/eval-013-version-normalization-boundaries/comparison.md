# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-013-version-normalization-boundaries`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1cee6041bd72db3f52d6c6c5a5cd2b2192f387347cccb99c7f5a1da1c4e1e970` from `agents/docs/test/docs-audit/evals/workspace/eval-013-version-normalization-boundaries`.
- Fixture SHA-256: `1cee6041bd72db3f52d6c6c5a5cd2b2192f387347cccb99c7f5a1da1c4e1e970`
- Prompt SHA-256: `e4e9083fe5f80e87e2a90dbd2508e2ce8a005911bcd108e280ebfcc392bef53e`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2baee6e542351d5b0c46e79c685dd29ff93f0fee4a45cf4485afee7656248cf7`
- Skill overlay SHA-256: `a2871f547194089c5425585467f9bee6e3c85ea103d77933d85a4c4cf246fa7c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `6f3c010dbdde60de256381f298da12ba27ac671f9dba533a58464c18d69bbe20`
- Metadata SHA-256: `de723686d571b59f10dc657eaf98d1d9ad27c06a9381fcb0dfee19364fb401ec`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_complete_version_identity` | PASS | with_skill 将带 v 与不带 v 的版本归一化为同一完整 identity，并保留 rc.1 与 +Build.7；同时拒绝大小写、构建元数据和预发布部分不同的候选。 |
| `enforces_each_source_contract` | PASS | with_skill 逐项列出 target、tag、notes、index、releases、marketplace、package 的观测问题，指出缺失、非法 raw form、selector 解析为 0、非唯一匹配及 extractor identity 不一致，未将其他来源值作为补值。 |
| `reports_all_version_blockers` | PASS | with_skill 覆盖了 fixture 中的缺失、非法格式、大小写/前缀错误、identity 差异、selector 非唯一或无解析结果、extractor 不一致及 pre-tag 来源集合问题，并分别判定 pre-tag 与 post-tag blocked。 |
| `binds_pre_and_post_tag_inventory` | FAIL | with_skill 指出 pre-tag 缺少可验证 handoff，但没有说明应如何固定完整来源集合、如何让 post-tag 消费同一绑定，或为何多版本来源不能通过扫描挑选。 |
| `makes_inventory_integrity_reproducible` | FAIL | with_skill 仅指出 extractor identity 不一致会破坏可复现性；没有给出确定性的 inventory integrity 证据，也没有说明来源集合、定位契约或顺序变更时的阻断规则。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e4e9083fe5f80e87e2a90dbd2508e2ce8a005911bcd108e280ebfcc392bef53e; fixture_sha256=1cee6041bd72db3f52d6c6c5a5cd2b2192f387347cccb99c7f5a1da1c4e1e970; output_sha256=582eefc3872decc8188039db14b9d6123afc0c1fe9fc12d6f50f3e36095ee39c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 更完整地识别并阻断 pre-tag/post-tag 证据问题，但未满足来源绑定和 inventory integrity 可复现性要求。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e4e9083fe5f80e87e2a90dbd2508e2ce8a005911bcd108e280ebfcc392bef53e; fixture_sha256=1cee6041bd72db3f52d6c6c5a5cd2b2192f387347cccb99c7f5a1da1c4e1e970; output_sha256=268fab184efced03c3c678997644aa1ae17fed5fdc378736e78ee2c55baa0bea; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了主要 post-tag 版本问题，但将 pre-tag 判为通过且未充分逐源审查。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未说明 pre-tag 固定来源集合与 post-tag 同绑定复核机制。
- with_skill 未提供确定性的 inventory integrity 证据及其篡改阻断规则。
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

未满足断言（with/without 任一 FAIL）：``binds_pre_and_post_tag_inventory``、``makes_inventory_integrity_reproducible``



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

> ⚠️ 本节为历史轮执行证据（适用旧 run）；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

- 两臂锁定前只读取同一 prompt 和 `version-cases.md`，未读取 assertions、expected output、旧 comparison 或对方输出。
- with-skill arm读取完整 Docs/docs-audit 指令；without-skill arm隔离这些内容。
- fresh judge 在 SHA-256 锁定后才读取 assertions。
- with-skill SHA-256：`210a4836d46b095ef9ad18943784c5dcc55df4c9693a46a1351010c3bdab11b3`；without-skill：`e053ee70e2330b8c7b5138a57bdb1ce189170489dd169b5d182bf2fd8a068d9b`。

## Failures And Limitations

> ⚠️ 本节为历史轮执行证据（适用旧 run）；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

- with-skill 无失败；Coverage FULL。
- source table 仍暴露 raw forms、selector 和 extractor，所以 baseline 可恢复 3/5；区分度来自跨阶段 future-tag binding 与 canonical integrity。
- 第一轮即达到区分度，无需第二轮。

## Runtime Artifact Policy

- runtime responses 和 judge verdict 仅保存在 `tmp/eval-runs/issue-177/docs-audit/round-1/`，不提交。
- 本 `comparison.md` 是唯一 durable 结果。
