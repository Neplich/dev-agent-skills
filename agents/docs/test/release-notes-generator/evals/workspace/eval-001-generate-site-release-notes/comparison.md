# Skill Eval Comparison

## Evaluation Target

- Skill: `release-notes-generator`
- Eval: `eval-001-generate-site-release-notes`
- Scenario: target release version 只有协调者候选值、缺少维护者确认
- Review context: issue #177 sub-batch 4c

## Test Set / Fixture Version

- Fixture version: `issue-177 target-version confirmation clarification round-3`
- Validation time: `2026-07-29 00:17:54 CST`
- Runtime: `tmp/eval-runs/issue-177/docs-release-evals/round-3-eval-001/`
- with-skill 读取公开 SKILL 和 Docs Agent README；入口未通过，因此未加载内部执行流程。
- without-skill 由全新 `fork_turns=none` 子 Agent 从同一最新 fixture 和 prompt 独立生成，不读取目标 skill、Agent README、assertions、旧 comparison、历史 round 或 with-skill 输出。

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL**（5/5 assertions exercised）
- Overall result: PASS
- With-skill: **5/5 PASS**
- Fresh without-skill: **3/5 PASS、2/5 FAIL**
- Relative uplift: **+2 assertions**，通过率从 60% 提升到 100%。

## Leakage Surface Analysis

重做前，prompt、assertions、Release Notes README、六份 evidence 和 confirmation record 共同给出六类正文、frontmatter、确认顺序、checks 与完整 ready handoff 字段，baseline 可完整恢复成功路径。

第一轮加入缺失镜像 digest/inspect 证据，但双方都正确记录缺口、更新 confirmed body 的 index/metadata 并返回 blocked audit handoff；原 assertions 错误要求缺证据时派生面零写入，导致 with-skill 3/5，说明用例把证据 blocker 与正文确认门禁混为一谈。

第二轮改测公开入口 gate：fixture 提供 `target_release_version: v1.0.0`，但来源只是 release coordinator planning note，没有维护者确认记录。正文确认与 evidence 仍存在，用于验证它们不能替代版本入口凭据。

Review 指出第二轮 `confirmation-record.md` 仍以“维护者确认 v1.0.0 页面”描述正文事实，并使用 `confirmation_status: confirmed`，与 `release-entry.md` 的“没有维护者版本确认记录”冲突。第三轮把该记录改为版本无关的 Release Notes 正文事实确认，并显式声明 `target_release_version_confirmation: not_confirmed`，使正文确认和目标版本确认成为无歧义的两个凭据。

## Redesign

- prompt 不再写出版本值、执行步骤或 handoff 字段。
- assertions 检查版本确认主体、入口 stop point、全站零写入、不运行后置流程和 PM return。
- release entry 只把版本标为协调者候选值；confirmation record 只确认正文事实，并显式不确认目标版本。

## Assertion Results

| Assertion | With skill | Without skill | Fresh judgment |
| --- | --- | --- | --- |
| `detects_missing_version_confirmation` | PASS | PASS | 两侧均识别协调者 planning note 只是候选来源，正文事实确认不构成目标版本确认。 |
| `stops_before_loading_execution_workflow` | PASS | FAIL | with-skill 停在入口且未生成候选；baseline 加工六份 evidence 并输出完整“版本待确认”正文，越过入口 stop point。 |
| `keeps_all_site_surfaces_unchanged` | PASS | PASS | 两侧 `docs/site/` 前后 SHA-256 manifest 一致，版本页、index、metadata 和导航均零差异。 |
| `does_not_run_post_entry_checks` | PASS | PASS | 两侧均未安装依赖、运行 docs checks 或生成 site-ready / pre-tag handoff。 |
| `returns_version_ambiguity_to_pm` | PASS | FAIL | with-skill blocked 并返回 `pm-agent` 补齐可追溯版本确认；baseline 只直接要求维护者确认，未回 PM，且已生成正文。 |

## With-Skill Behavior

- 识别 body confirmation 与 target version confirmation 是两个独立凭据。
- 未加载内部七步流程，未生成候选或页面、未应用 body confirmation、未安装依赖或运行 docs checks。
- 返回 PM 补齐可追溯维护者版本确认，tag/GitHub Release 零写入。
- Response SHA-256: `3fa99a9eaae344df5dedfc96344a99f0714e27f624051caec3b94803f803faf9`。

## Fresh Without-Skill Baseline

- baseline 也识别版本未确认并保持站点零写入，且没有运行后置 checks。
- baseline 越过入口 stop point，把 evidence 加工成完整的版本无关正文；后续只直接要求维护者确认，没有把入口歧义交回 PM owner。
- Response SHA-256: `b77a596122f0992c1523fc631c981c4c0c9cc1dc9f7392251d8ad72cb5a84377`。

## Failures And Iterations

- Round 1：with-skill 3/5、baseline 3/5；with-skill 自身两条 FAIL，Behavior FAIL。
- Round 2：with-skill 5/5、baseline 3/5；Behavior PASS、Coverage FULL。
- Round 3：澄清正文确认记录不确认目标版本后，with-skill 5/5、fresh baseline 3/5；Behavior PASS、Coverage FULL。
- Round-1 问题来自错误 assertion 语义，不把失败篡改为 PASS。
- Round-2 fixture 的确认记录同时绑定 v1.0.0 和标记 confirmed，可能被合理解释为维护者版本确认来源；Round-3 已消除该证据矛盾。
- 基础设施失败：none。

## Next Steps

- 保持正文确认与目标版本确认的显式分离，并继续以入口 stop point 和 PM return 作为核心回归。

## Runtime Artifact Policy

- runtime 页面副本、日志、response 与 verdict 不提交。
- 本 `comparison.md` 是唯一 durable eval 结果。
