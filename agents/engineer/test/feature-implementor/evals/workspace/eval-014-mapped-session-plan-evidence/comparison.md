# Consumption Regression Comparison

## Evaluation Target

- Skill: `feature-implementor`
- Eval: `eval-014-mapped-session-plan-evidence`

## Test Set / Fixture Version

- Fixture: `ws1-consumption-v1`
- Commit: `0b000b9`

## Latest Result

- Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。

**PASS** — with-skill 以代码事实（30 分钟、续期禁用）核证出文档 60 分钟声明的分歧，PRD/TRD 前置门禁正确触发暂停，未在预期未对齐时编写实施计划。

## With-Skill Behavior

- 命中映射文档后回代码核证会话行为，结构化区分代码事实与文档声明。
- 变更按 standard 分级，正确停在 PM → trd-gen → 实施计划的协作链前置，未越权编码。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 或消费契约提示。
- baseline 同样停在门禁前请求预期确认，行为合规但对文档分歧的证据组织与契约引用较弱。

## Failures

- 无。

## Next Steps

- 保留本结果；后续 fixture 可增加干扰文档以放大行为差距。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
