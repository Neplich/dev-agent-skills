# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-010-post-tag-match`
- Scenario: direct handoff 与 fresh clone 两种对象可达性下的 post-tag authority 与持久化门禁
- Review context: issue #177 sub-batch 4b

## Test Set / Fixture Version

- Fixture version: `issue-177 discrimination restore round-1`
- Validation time: `2026-07-28 22:48:16 CST`
- Runtime: `tmp/eval-runs/issue-177/docs-audit/round-1/`
- Assertions: 5，全部实际触发

## Latest Result

- Behavior result: `PASS`（with）/ `FAIL`（without）— 本轮 #238 fresh 隔离重跑（2026-08-06）
- Coverage result: `FULL`（with）/ `FULL`（without）— 本轮重跑实际触发的断言场景
Overall result: FAIL
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `PASS` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `selects_pre_tag_authority_safely` | PASS | FAIL | with_skill 明确区分 direct-handoff 与 fresh-clone，并在 fresh-clone 使用 tag tree 固定路径回退校验；without_skill 明确称 fresh-clone 无法重建完整审计链。 |
| `proves_released_tree_binding` | PASS | FAIL | with_skill 给出 `entry_tag_tuple` 与 `pre_result_tag_tuple` 一致、实际 tree 为 `666…666`，并解释 commit identity 不同但 tree 一致；without_skill 的 fresh-clone 仅能看到 tag tree，无法完成完整绑定复核。 |
| `verifies_version_surfaces_from_release` | PASS | PASS | 两条 lane 均核验 tag、Release Notes、索引、`releases.json` 与 `package.json`，并处理 `v1.2.0` / `1.2.0` 表示差异；证据指向 tag tree 与已提交路径。 |
| `requires_durable_post_tag_evidence` | PASS | FAIL | with_skill 明确识别 `release_evidence_branch_confirmation` 和 `release_evidence_expected_head` 缺失，并将两个场景均保持为 `blocked`；without_skill 将 direct-handoff 描述为“文档内容已验证、发布闭环待确认”，未按断言要求保持 blocked。 |
| `preserves_upstream_release_artifacts` | PASS | PASS | 两条 lane 均明确“未执行任何 tag、branch 或 release 写入”，且未重新生成、盖章或改变 pre-tag handoff。 |

未满足断言：``selects_pre_tag_authority_safely``、``proves_released_tree_binding``、``requires_durable_post_tag_evidence``


- With-skill: **5/5 PASS**
- Fresh without-skill: **1/5 PASS、4/5 FAIL**
- Relative uplift: **+4 assertions**

两臂都看到一致的 tag/tree/version 原始证据。with-skill 在 direct handoff 可用时验证外部 authority，在 fresh clone 对象不可达时从 tag tree 固定 discovery path 重建 authority；同时因维护者未确认独立 post-tag evidence branch 与 expected head，让两个场景都保持 `blocked`。baseline 只完成 direct 场景，并把它表述为只读审计通过。

## Leakage Surface Analysis

重做前，baseline 可直接从 prompt、assertions 与 release context 取得 package 优先级、fixed-path fallback、anchor tree 重建、tag tuple 双读、object-read 范围、版本规范化、独立记录路径、FF/CAS 和成功状态。

重做后仍可见的是原始 object identity、candidate/discovery 记录和版本表面；不再预告 locator 选择、fallback 算法或独立持久化 gate。release context 只声明 direct/fresh 对象可达性和一个未确认 branch hint。

## Redesign

- prompt 只保留 post-tag 任务、两个场景、输入指针与只读边界。
- assertions 收敛为 authority、release tree、version surfaces、durable result 和上游不可变性五个语义结果。
- 删除 fixture 中的 locator 优先级、tree equality 结论、normalization 结论和 CAS 恢复答案。
- 增加阻塞型凭据缺口：branch hint 存在，但 maintainer confirmation 与 expected head 均缺失。
- 将历史 issue 身份引用替换为 `docs-agent:release-notes-gen`，并重算 inventory digest、candidate blob、discovery blob 与 lineage digest。

## Assertion Results
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

| Assertion | With skill | Without skill | Fresh judgment |
| --- | --- | --- | --- |
| `selects_pre_tag_authority_safely` | PASS | FAIL | skill arm 分别验证 direct handoff 与 tag-tree fixed-path fallback；baseline 将 fresh clone 判为无法建立 authority。 |
| `proves_released_tree_binding` | PASS | FAIL | skill arm 在两种可达性下都证明完整 tag tree 绑定；baseline 只完成 direct 场景。 |
| `verifies_version_surfaces_from_release` | PASS | FAIL | skill arm 从 peeled tag tree 复核完整来源；baseline 未完成 fresh 场景的发布对象复核。 |
| `requires_durable_post_tag_evidence` | PASS | FAIL | skill arm 因 evidence branch/head 未确认让两场景都 blocked；baseline 错误放行 direct 场景。 |
| `preserves_upstream_release_artifacts` | PASS | PASS | 两臂均未改 pre-tag authority、stamp、tag 或 Release。 |

## Fresh Validation Method

1. 两个生成 arm 只读取 `eval_metadata.json` 的 prompt 与 fixture_context；锁定前均未读取 `evals.json`、assertions、expected output 或旧 comparison。
2. with-skill arm读取 Docs README、`docs-audit/SKILL.md` 和完整内部指令；without-skill arm 不读取或应用这些内容，也不读取 with-skill 输出。
3. 两臂基于同一最终 fixture revision 生成 response 并锁定 SHA-256 后，fresh judge 才读取 assertions。
4. with-skill response SHA-256：`0605883f82aff53f7bf03dbe5a90b6e950989032fc041a169af38aaaeb81b8e4`；without-skill：`475f755dcf05f9a146e36c5f3925600165794cc0db9122574bf90db09553dfa7`。

## Failures And Limitations

- with-skill 无失败；Coverage FULL。
- baseline 仍能从 committed records 恢复部分 authority 与版本事实，但未恢复 fresh-clone fallback 和 durable-result credential gate。
- 第一轮即达到区分度，无需第二轮。

## Runtime Artifact Policy

- responses、judge verdict 与校验和仅位于 git 忽略的 `tmp/eval-runs/issue-177/docs-audit/round-1/`，不提交。
- 本 `comparison.md` 是唯一 durable 结果。
