# Skill Eval Comparison

## Evaluation Target

- Skill: `release-notes-generator`
- Eval: `eval-001-generate-site-release-notes`
- Scenario: target release version 只有协调者候选值、缺少维护者确认
- Review context: issue #177 sub-batch 4c

## Test Set / Fixture Version

- Fixture version: `issue-177 discrimination restore round-2`
- Validation time: `2026-07-28 23:36:25 CST`
- Runtime: `tmp/eval-runs/issue-177/docs-release-evals/round-2/`
- with-skill 只在入口门禁读取公开 SKILL；without-skill 不读取目标 skill、Agent README、assertions、旧 comparison、round-1 或 with-skill 输出。

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

## Redesign

- prompt 不再写出版本值、执行步骤或 handoff 字段。
- assertions 检查版本确认主体、入口 stop point、全站零写入、不运行后置流程和 PM return。
- fixture 只保留协调者候选版本及缺少维护者来源这一原始身份事实。

## Assertion Results

| Assertion | With skill | Without skill | Fresh judgment |
| --- | --- | --- | --- |
| `detects_missing_version_confirmation` | PASS | PASS | 两侧均识别协调者 planning note 不是维护者确认。 |
| `stops_before_loading_execution_workflow` | PASS | PASS | 两侧均未生成候选或应用正文确认；baseline 的后置检查违规单独计分。 |
| `keeps_all_site_surfaces_unchanged` | PASS | PASS | 两侧正式站点均零差异。 |
| `does_not_run_post_entry_checks` | PASS | FAIL | with-skill 在入口停止；baseline 安装依赖并运行 `test:docs`，因缺页面得到 74/75。 |
| `returns_version_ambiguity_to_pm` | PASS | FAIL | with-skill blocked 并返回 `pm-agent` 补齐确认；baseline 只要求维护者确认，未回 PM 且越过入口跑检查。 |

## With-Skill Behavior

- 未加载内部七步流程，未生成页面、未应用 body confirmation、未安装依赖或运行 docs checks。
- 返回 PM 补齐可追溯维护者版本确认，tag/GitHub Release 零写入。
- Response SHA-256: `b57b255d584902f0d22002d192a50a050fcbf32cdb5f46c1090baa6c6f66d3a8`。

## Fresh Without-Skill Baseline

- baseline 也保持站点零写入，但越过入口执行 locked install 与 `npm run test:docs`，后者因 `v1.0.0.md` 不存在失败。
- baseline 没有把入口歧义交回 PM owner。
- Response SHA-256: `02ce0644dec4cf342d0085e94dec7ad1ceb477cba1a4a141a51cb46915c0c539`。

## Failures And Iterations

- Round 1：with-skill 3/5、baseline 3/5；with-skill 自身两条 FAIL，Behavior FAIL。
- Round 2：with-skill 5/5、baseline 3/5；Behavior PASS、Coverage FULL。
- Round-1 问题来自错误 assertion 语义，不把失败篡改为 PASS。
- 基础设施失败：none；baseline 的 74/75 是被测业务行为，不是 infrastructure failure。

## Next Steps

- 保持版本确认主体与 stop point 为入口回归；不要把 body confirmation 当作 target version confirmation。

## Runtime Artifact Policy

- runtime 页面副本、日志、response 与 verdict 不提交。
- 本 `comparison.md` 是唯一 durable eval 结果。
