# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-010-release-notes-boundary`
- Scenario: 从非协议化结果语义识别独立站内版本说明工作流
- Review context: issue #177 sub-batch 4c

## Test Set / Fixture Version

- Fixture version: `issue-177 discrimination restore round-1`
- Validation time: `2026-07-28 23:36:25 CST`
- Runtime: `tmp/eval-runs/issue-177/docs-release-evals/round-1/`
- 两侧使用同一 prompt 与独立 pristine fixture；baseline 不读取目标 skill、assertions、旧 comparison 或 with-skill 输出。

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL**（4/4 assertions exercised）
Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。

- With-skill: **4/4 PASS**
- Fresh without-skill: **1/4 PASS、3/4 FAIL**
- Relative uplift: **+3 assertions**，通过率从 25% 提升到 100%。

## Leakage Surface Analysis

重做前，prompt 与 assertions 直接写出 `formal-docs-sync` 必须拒绝、四类禁止 surface、准确 specialist 名和整个站点零 diff；fixture 还声明用户正在强迫错误 owner。baseline 因此可复述完整边界。

重做后 prompt 只用“面向用户的本次更新页面、版本列表、发布元数据”描述目标结果；fixture 只保留 host、版本、范围、来源和目标站点面，不标注正确 owner 或越界结论。

## Redesign

- 按 requested outcome 而不是协议术语判断路由。
- assertions 只检查 workflow 识别、完整入口交接、当前 specialist 零写入和外部发布边界。
- 不在 prompt/assertions 中给出 specialist 名称或精确禁止路径清单。

## Assertion Results

| Assertion | With skill | Without skill | Fresh judgment |
| --- | --- | --- | --- |
| `recognizes_release_communication_outcome` | PASS | FAIL | with-skill 识别独立 Release Notes workflow；baseline 直接生成页面。 |
| `routes_complete_entry_to_site_owner` | PASS | FAIL | with-skill 将 confirmed host/version/scope/evidence/surfaces 交给 `docs-agent:release-notes-generator`；baseline 无 handoff。 |
| `keeps_entire_site_zero_diff` | PASS | FAIL | with-skill 站点零写入；baseline 新增版本页并修改 index/metadata。 |
| `preserves_external_release_boundary` | PASS | PASS | 两侧均未执行 tag 或 GitHub Release。 |

## With-Skill Behavior

- 未加载 Product/Ops 类型模块，也未进入 current-state 页面同步。
- 直接生成站内版本说明 specialist handoff，整个 `docs/site/` 保持 pristine。
- Response SHA-256: `3941048d7ac38a20485a8f6a0101d59fa5be1b6566b64543584c531198ee9e69`。

## Fresh Without-Skill Baseline

- baseline 自行新增 v1.5.0 页面、更新版本索引和 release metadata，并运行宿主检查。
- 它保留外部 tag/GitHub Release 零写入，但没有识别当前 specialist 的站内职责边界。
- Response SHA-256: `5b0e0bb59cf7311e9269f8ae69bbcaf1a3d22834a76d32000e0dbc6658ed8931`。

## Failures And Iterations

- Round 1 即达到区分度，无需第二轮。
- with-skill 无 assertion failure；基础设施失败 none。

## Next Steps

- 保持本例为 outcome-based routing 回归，不把 specialist 名称重新泄漏到 prompt。

## Runtime Artifact Policy

- 两 lane workspace、responses、依赖、日志和 judge verdict 仅位于 gitignored runtime，不提交。
- 本 `comparison.md` 是唯一 durable eval 结果。
