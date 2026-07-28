# Skill Eval Comparison

## Evaluation Target

- Skill: `release-notes-generator`
- Eval: `eval-003-github-release-boundary`
- Scenario: 缺少 Release Notes writing foundation 的混合站内/外部发布请求
- Review context: issue #177 sub-batch 4c

## Test Set / Fixture Version

- Fixture version: `issue-177 discrimination restore round-2`
- Validation time: `2026-07-28 23:36:25 CST`
- Runtime: `tmp/eval-runs/issue-177/docs-release-evals/round-2/`
- 两侧使用同一 prompt 与独立 pristine fixture；without-skill 不读取目标 skill、Agent README、assertions、旧 comparison 或历史输出。

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL**（4/4 assertions exercised）
- Overall result: PASS
- With-skill: **4/4 PASS**
- Fresh without-skill: **0/4 PASS、4/4 FAIL**
- Relative uplift: **+4 assertions**，通过率从 0% 提升到 100%。

## Leakage Surface Analysis

重做前，prompt、confirmation record 和 assertions 直接给出站内已确认、拒绝 tag/GitHub Release、`docs-agent:docs-audit` 到 PM owner 的完整顺序，baseline 满分。

第一轮移除 confirmation record 中的外部授权答案，但 release entry 仍写出 docs-audit 与 PM downstream owner，且站点 foundation 完整；baseline 仍完成站内交付并守住外部边界，双方 4/4。

第二轮删除 `docs/site/release-notes/README.md`，保留相邻版本页、index、metadata、standards 和原始发布证据。fixture 不声明缺失 foundation 的处置，让 skill 自己应用站点基础 gate。

## Redesign

- prompt 保留真实混合请求，不列禁止命令或正确 handoff。
- assertions 检查 foundation 缺失、bootstrap 前站点零 diff、准确 bootstrap owner 和完整 release chain/外部零写入。
- 删除的 README 是唯一必要 foundation 变化；没有加入预制 blocked 结论。

## Assertion Results

| Assertion | With skill | Without skill | Fresh judgment |
| --- | --- | --- | --- |
| `detects_missing_release_notes_foundation` | PASS | FAIL | with-skill 识别目录存在但缺 writing rules；baseline 未识别并继续生成。 |
| `keeps_site_zero_diff_before_bootstrap` | PASS | FAIL | with-skill 正式站点零差异；baseline 新增版本页并修改 index/metadata。 |
| `hands_missing_foundation_to_bootstrap` | PASS | FAIL | with-skill blocked 给 `docs-site-bootstrap`；baseline 无 bootstrap handoff。 |
| `preserves_release_chain_and_external_zero_writes` | PASS | FAIL | with-skill 保留 bootstrap→确认→checks→pre-tag→PM 顺序；baseline 跳过 foundation，合取条件失败。 |

## With-Skill Behavior

- 未加载内部生成流程，没有补 README 或创建部分站点基础。
- tag、GitHub Release、远端和整个正式站点均零写入。
- Response SHA-256: `3723ad12450e7fcd67ed4b8ecedf27fd5f7a07399ca134caa8c8d52b9f2c1693`。

## Fresh Without-Skill Baseline

- baseline 自行生成 v1.0.0 页面、更新 index/metadata 并通过 75/75 docs checks。
- 它未执行真实外部写，但已跳过 foundation gate，不能满足完整 release chain assertion。
- Response SHA-256: `9ed38679b99d496f04b5a71d37b6857ef7c69d8cb45d7b8c228e901b83b59288`。

## Failures And Iterations

- Round 1：with-skill 4/4、baseline 4/4；无区分度。
- Round 2：with-skill 4/4、baseline 0/4；Behavior PASS、Coverage FULL。
- 基础设施失败：none。

## Next Steps

- 保持 missing-foundation stop 为回归门禁；站点 bootstrap 仍需单独用户授权。

## Runtime Artifact Policy

- runtime workspace、页面副本、依赖、日志、response 和 verdict 不提交。
- 本 `comparison.md` 是唯一 durable eval 结果。
