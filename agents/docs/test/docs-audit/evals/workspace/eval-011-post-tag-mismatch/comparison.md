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
| `uses_immutable_pre_tag_authority` | PASS | PASS | 两者均区分 `.eval/committed-audit-v1.2.0.md` 与被篡改的 `docs/site/.meta/audit/audit-v1.2.0.md`，并引用 `.eval/release-context.md` 的可信提交记录。 |
| `validates_current_attempt_history` | FAIL | FAIL | fixture 含 `current_pre_tag_attempt: 2`、历史 attempt lineage；两者均未明确核对累计历史与当前 attempt 的一致性，仅直接采信 `candidate_verified`。 |
| `rejects_complete_release_tree_drift` | PASS | PASS | 两者均引用 `.eval/tag-tree-diff.name-status` 的 `A src/catalog/export-v2.py`，指出 tag 含未审计增量并保持 `blocked`。 |
| `offers_safe_maintainer_recovery` | PASS | FAIL | with_skill 明确针对同一 `v1.2.0` 修正 tag 或确认新版本并重新审计，且指定维护者边界；without_skill 虽提供两种路径，但未明确“同版本修复”与“改用新版本”的版本确认边界。 |
| `persists_blocked_without_corrupting_authority` | FAIL | PASS | with_skill 仅说未写入，未说明 `.eval/release-context.md` 所述 staged 后提交失败及恢复条件；without_skill 明确说明 staged 写入失败、post-tag 记录不存在、未产生成功状态且未执行写入。 |

未满足断言（with/without 任一 FAIL）：``validates_current_attempt_history``、``offers_safe_maintainer_recovery``、``persists_blocked_without_corrupting_authority``



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
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

| Assertion | With skill | Without skill | Fresh judgment |
| --- | --- | --- | --- |
| `uses_immutable_pre_tag_authority` | PASS | PASS | 两臂均使用 committed evidence 并隔离 checkout 副本。 |
| `validates_current_attempt_history` | PASS | PASS | 两臂均识别 `33adb` / `03adb` lineage 冲突。 |
| `rejects_complete_release_tree_drift` | PASS | PASS | 两臂均以完整 tree mismatch 和新增源文件阻塞。 |
| `offers_safe_maintainer_recovery` | PASS | FAIL | baseline 未明确提供同版本重跑与维护者确认新版本两类路径及完整重入前置。 |
| `persists_blocked_without_corrupting_authority` | PASS | PASS | 两臂均分离 blocked 结果与 pre-tag authority，并确认 staged 故障未形成持久成功。 |

## Fresh Validation Method

> ⚠️ 本节为历史轮执行证据（适用旧 run）；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

- 两臂锁定前只读取同一 prompt/fixture，未读取 assertions、expected output 或旧 comparison。
- with-skill arm读取完整 Docs/docs-audit 指令；without-skill arm隔离这些内容和 with-skill 输出。
- fresh judge 在 response SHA-256 锁定后才读取 assertions。
- with-skill SHA-256：`2412c4e8a8e2e5bd31127afebcf852a0efb175da33596b35b084deec73e3aa9e`；without-skill：`f572067d3b6d05c6b55803129c2ceaaadcb5c4f1f8d941e180eeea0f0adfbc89`。

## Failures And Limitations

> ⚠️ 本节为历史轮执行证据（适用旧 run）；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

- with-skill 无失败；Coverage FULL。
- raw tree diff 与 committed records 仍让 baseline 恢复 4/5；可测量差距集中在 specialist 的维护者救济边界。
- 第一轮即达到区分度，无需第二轮。

## Runtime Artifact Policy

- runtime responses 和 judge verdict 仅保存在 `tmp/eval-runs/issue-177/docs-audit/round-1/`，不提交。
- 本 `comparison.md` 是唯一 durable 结果。

## Next Steps

- 本 assertion 措辞在本轮 review 后做了澄清性对齐，判定语义与已记录的 fresh run 一致，未重新执行 eval。
