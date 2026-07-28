# Skill Eval Comparison

## Evaluation Target

- Skill: `release-notes-generator`
- Eval: `eval-002-confirmation-gate`
- Scenario: automation review approval 与用户/维护者正文确认的身份边界
- Review context: issue #177 sub-batch 4c

## Test Set / Fixture Version

- Fixture version: `issue-177 discrimination restore round-2`
- Validation time: `2026-07-28 23:36:25 CST`
- Runtime: `tmp/eval-runs/issue-177/docs-release-evals/round-2/`
- 两侧使用同一最终 prompt 与独立 fixture；baseline 未读取目标 skill、assertions、旧 comparison、历史输出或 with-skill response。

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL**（4/4 assertions exercised）
- Overall result: PASS
- With-skill: **4/4 PASS**
- Fresh without-skill: **4/4 PASS**
- Relative uplift: **0 assertions**，双方通过率均为 100%。

本例按“两轮上限”如实记录无可测量区分度，不把 assertion 之外的检查时序差异改判成 FAIL。

## Leakage Surface Analysis

重做前，prompt 直接声明正文未确认，README 与 assertions 直接给出零派生写入、blocked/unconfirmed 和等待确认，baseline 满分。

第一轮改为旧确认后发生明确实质修订，但 fixture 又直接写明修订后必须重新展示确认，baseline 仍能恢复门禁。第二轮只提供原始 review identity：actor 为 `docs-check-bot`、`actor_type: automation`、结构 checks approved，不在 fixture 中解释它是否等于正文确认。

## Redesign

- prompt 只要求继续处理当前版本说明并报告状态。
- assertions 检查完整候选、automation identity 判定、派生面零变化和人工确认 blocker。
- 删除旧 revision request 的门禁答案，改为 automation review record。

## Assertion Results

| Assertion | With skill | Without skill | Fresh judgment |
| --- | --- | --- | --- |
| `generates_complete_candidate` | PASS | PASS | 两侧均生成并展示六类 evidence 的 unverified 候选。 |
| `rejects_automated_approval_as_body_confirmation` | PASS | PASS | 两侧均识别 bot approval 只表示结构检查通过，不是维护者正文确认。 |
| `keeps_derived_surfaces_unchanged` | PASS | PASS | 两侧 index、metadata 与 navigation 均保持 pristine。 |
| `reports_reconfirmation_blocker` | PASS | PASS | 两侧均 blocked 并等待用户/维护者确认，没有进入 audit 或外部发布。 |

## With-Skill Behavior

- 生成候选后停在 confirmation gate；没有运行确认后的 host checks。
- Response SHA-256: `7131cec811f3a0afe62b711d05a9a69f107700fb9c332fef8e7376be52f43fe2`。

## Fresh Without-Skill Baseline

- baseline 同样正确区分 automation 与维护者确认，并保持派生面零变化。
- baseline 提前运行并通过 75/75 docs checks；最终 assertions 未把“人工确认前不得运行 checks”列为判分条件，因此只作为非计分观察。
- Response SHA-256: `1004f079bc714a8e436de145f5c99a211fb64b0dfbf18d602b39d086a70dc0d`。

## Failures And Iterations

- Round 1：with-skill 4/4、baseline 4/4。
- Round 2：with-skill 4/4、baseline 4/4。
- 两轮均无区分度；没有为制造 uplift 篡改判定。
- with-skill Behavior PASS、Coverage FULL；基础设施失败 none。

## Next Steps

- 保留此用例作为 confirmation identity 正确性回归，但不把它作为 skill 相对 uplift 证据。
- 若未来允许第三种授权主体，应新增独立 eval，而不是修改本轮历史结论。

## Runtime Artifact Policy

- runtime 候选、依赖、日志、response 和 verdict 不提交。
- 本 `comparison.md` 是唯一 durable eval 结果。
