# Consumption Regression Comparison

## Evaluation Target

- Skill: `idea-to-spec`
- Eval: `eval-008-mapped-notification-update`

## Test Set / Fixture Version

- Fixture: `ws1-consumption-v1`
- Commit: `0b000b9`

## Latest Result

**PASS** — with-skill 以代码证据确认仅 email 启用，把文档声称的 webhook 支持结构化记录为分歧，按 standard 分级推进现有功能更新并回用户确认关键决策。

## With-Skill Behavior

- 命中映射文档后以 src 代码核证渠道能力，明确区分'代码已证实 / 文档声称但无证据'。
- 分歧以文档声明/代码事实/影响结构化记录；未虚构供应商、接口与数据模型；正确停在 PM 决策点。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 或消费契约提示。
- baseline 走了合理的 PM 澄清流程，但未结构化记录文档与代码的渠道能力分歧，对文档声明的采信边界不明确。

## Failures

- 无。

## Next Steps

- 保留本结果；后续 fixture 可增加干扰文档以放大行为差距。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
