# Consumption Regression Comparison

## Evaluation Target

- Skill: `ui-ux-design`
- Eval: `eval-005-mapped-notification-ui`

## Test Set / Fixture Version

- Fixture: `ws1-consumption-v1`
- Commit: `0b000b9`

## Latest Result

**PASS** — with-skill 完整执行消费链（change-map 反查 → 读映射文档 → 回 HTML 核证默认状态分歧 → unverified 以代码为准），随后正确停在 Designer 的 PM handoff 门禁，未越权产出设计文档。

## With-Skill Behavior

- 核证出文档声称默认开启 vs checkbox 无 checked 属性的分歧并结构化记录。
- 门禁行为最合规：缺 PM handoff packet 与 feature_path 时拒绝猜测 feature 路径写设计文档，回 pm-agent 补齐。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 或消费契约提示。
- baseline 走 pm-agent → designer-agent 链产出了设计文档，流程可用但越过了 handoff 凭据缺失的门禁，也未按契约组织分歧证据。

## Failures

- 无。

## Next Steps

- 保留本结果；后续 fixture 可增加干扰文档以放大行为差距。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
