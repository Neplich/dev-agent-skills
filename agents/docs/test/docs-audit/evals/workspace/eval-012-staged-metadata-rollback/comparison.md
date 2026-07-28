# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-012-staged-metadata-rollback`
- Scenario: 非文本 candidate drift、committed boundary 与失败事务恢复
- Review context: issue #177 sub-batch 4b

## Test Set / Fixture Version

- Fixture version: `issue-177 discrimination restore round-1`
- Validation time: `2026-07-28 22:48:16 CST`
- Runtime: `tmp/eval-runs/issue-177/docs-audit/round-1/`
- Assertions: 5，全部实际触发

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL**（5/5 assertions exercised）
- Overall result: PASS
- With-skill: **5/5 PASS**
- Fresh without-skill: **4/5 PASS、1/5 FAIL**
- Relative uplift: **+1 assertion**

两臂都从 raw event log 识别 executable bit、symlink、rename、delete、额外 path、gitlink 和清理后的 staged fingerprint 漂移。with-skill 进一步把 anchor/handoff committed delta 作为 staged 之后的独立成功门禁；baseline 虽报告 hypothetical committed 异常，却没有建立“早期 staged 通过不能成为最终 authority”的二次验证要求。

## Leakage Surface Analysis

重做前，prompt、assertions 和两份 fixture prose 直接列出两次 staged gate、两段 committed gate、所有拒绝类型、rollback 动作与完整恢复证明。

重做后，fixture 只保留 staged snapshot A/B、hypothetical committed snapshot 以及 before/after fingerprints。输入不再说明哪些 Git 维度必须检查、何时复检或恢复失败应如何裁定。

## Redesign

- prompt 只要求判断 attempt、决定性证据、清理范围与成功边界。
- assertions 改为 non-content drift、unauthorized transformations、committed recheck、attempt-scoped rollback 和 host restoration 五个语义结果。
- 将答案型 prose 改为 raw Git-like event log 和 fingerprint snapshot。
- 增加第二层阻塞：failed cleanup 后 branch/porcelain/unstaged/path identity 已恢复，但 staged raw digest 仍不等于 before snapshot。
- 保留 `notes/local.txt` 的一致 identity，用于验证不覆盖无关用户状态。

## Assertion Results

| Assertion | With skill | Without skill | Fresh judgment |
| --- | --- | --- | --- |
| `detects_non_content_candidate_drift` | PASS | PASS | 两臂均覆盖 mode/type/path/object 语义。 |
| `rejects_every_unauthorized_transformation` | PASS | PASS | 两臂均报告 fixture 中全部转换类别。 |
| `rechecks_committed_candidate_boundaries` | PASS | FAIL | skill arm 将 anchor/handoff commit 级边界作为 staged 后的独立门禁；baseline 未建立该成功 authority 要求。 |
| `rolls_back_only_the_failed_attempt` | PASS | PASS | 两臂均限制 attempt-owned delta 并保留用户状态。 |
| `proves_host_state_restoration` | PASS | PASS | 两臂均因 staged digest 未恢复而继续 blocked。 |

## Fresh Validation Method

- 两臂锁定前只读取同一 prompt 和两份 raw fixture，未读取 eval object、assertions 或旧 comparison。
- with-skill arm读取完整 Docs/docs-audit 指令；without-skill arm未读取或应用这些内容。
- response 锁定后才由 fresh judge 逐 assertion 判定。
- with-skill SHA-256：`eda6aa97bde26a253263458c4acb8148ea3ff37170cecde32f3c886ced8bed6a`；without-skill：`62b16aaf0056ac379c53eaca4a9571b9bad68779a42ac0193d6f53b7f9b95909`。

## Failures And Limitations

- with-skill 无失败；Coverage FULL。
- raw log 仍直接暴露异常类型，因此 baseline 可恢复 4/5；差距集中在 committed confirmation 仍是独立 success authority。
- 第一轮即达到区分度，无需第二轮。

## Runtime Artifact Policy

- runtime responses 和 judge verdict 仅保存在 `tmp/eval-runs/issue-177/docs-audit/round-1/`，不提交。
- 本 `comparison.md` 是唯一 durable 结果。
