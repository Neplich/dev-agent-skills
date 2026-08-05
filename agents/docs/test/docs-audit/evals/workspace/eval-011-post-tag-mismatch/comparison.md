# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-011-post-tag-mismatch`
- Scenario: same-version history、当前副本漂移与未审计 tag 增量
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
- Fresh without-skill: **4/5 PASS、1/5 FAIL**
- Relative uplift: **+1 assertion**

两臂都识别当前 checkout 副本不是可信 pre-tag authority、lineage tuple 冲突以及 tag tree 新增 `src/catalog/export-v2.py`。with-skill 额外给出协议允许的两类维护者选择：修正错误 tag 后按同一版本完整重跑，或放弃该版本并明确确认新版本后完整重跑；baseline 只围绕暂停、改写或保留 tag，未提供完整的版本选择与审计重入前置。

## Leakage Surface Analysis

重做前，prompt、assertions 和 release context 直接提供 immutable record 选择、strict tree equality、lineage digest 算法、两条 remedy、re-entry 条件、blocked record 事务和 rollback 清单。

重做后，fixture 只保留两份 repository-state bytes、raw tag tuple、raw tree diff、committed candidate/discovery 和一次 staged 写入失败事件。显眼 tree delta 仍对 baseline 可见，但维护者版本选择契约不再出现在生成输入中。

## Redesign

- prompt 只要求给出结论、决定性差异、可持久化结果和维护者后续选择。
- assertions 改为 immutable authority、attempt history、complete tree、maintainer recovery 和 blocked persistence 五个语义结果。
- 删除 equality、active attempt、lineage rule、CAS policy 与标准答案 prose。
- 在 committed discovery 的 current tuple 中引入单字符 `previous_lineage_digest` 冲突，与 visible code-tree drift 形成两个独立 blocker。
- 清理历史 issue 身份引用，并重算 inventory/candidate/discovery object identities；只保留刻意的 lineage 冲突。

## Assertion Results

| Assertion | With skill | Without skill | Fresh judgment |
| --- | --- | --- | --- |
| `uses_immutable_pre_tag_authority` | PASS | PASS | 两臂均使用 committed evidence 并隔离 checkout 副本。 |
| `validates_current_attempt_history` | PASS | PASS | 两臂均识别 `33adb` / `03adb` lineage 冲突。 |
| `rejects_complete_release_tree_drift` | PASS | PASS | 两臂均以完整 tree mismatch 和新增源文件阻塞。 |
| `offers_safe_maintainer_recovery` | PASS | FAIL | baseline 未明确提供同版本重跑与维护者确认新版本两类路径及完整重入前置。 |
| `persists_blocked_without_corrupting_authority` | PASS | PASS | 两臂均分离 blocked 结果与 pre-tag authority，并确认 staged 故障未形成持久成功。 |

## Fresh Validation Method

- 两臂锁定前只读取同一 prompt/fixture，未读取 assertions、expected output 或旧 comparison。
- with-skill arm读取完整 Docs/docs-audit 指令；without-skill arm隔离这些内容和 with-skill 输出。
- fresh judge 在 response SHA-256 锁定后才读取 assertions。
- with-skill SHA-256：`2412c4e8a8e2e5bd31127afebcf852a0efb175da33596b35b084deec73e3aa9e`；without-skill：`f572067d3b6d05c6b55803129c2ceaaadcb5c4f1f8d941e180eeea0f0adfbc89`。

## Failures And Limitations

- with-skill 无失败；Coverage FULL。
- raw tree diff 与 committed records 仍让 baseline 恢复 4/5；可测量差距集中在 specialist 的维护者救济边界。
- 第一轮即达到区分度，无需第二轮。

## Runtime Artifact Policy

- runtime responses 和 judge verdict 仅保存在 `tmp/eval-runs/issue-177/docs-audit/round-1/`，不提交。
- 本 `comparison.md` 是唯一 durable 结果。

## Next Steps

- 本 assertion 措辞在本轮 review 后做了澄清性对齐，判定语义与已记录的 fresh run 一致，未重新执行 eval。
