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

- Behavior result: **PASS**
- Coverage result: **FULL**（5/5 assertions exercised）
Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。

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
- 将历史 issue 身份引用替换为 `docs-agent:release-notes-generator`，并重算 inventory digest、candidate blob、discovery blob 与 lineage digest。

## Assertion Results

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
