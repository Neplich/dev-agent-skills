# Consumption Regression Comparison

## Evaluation Target

- Skill: `debugger`
- Eval: `eval-005-mapped-cache-debug-evidence`

## Test Set / Fixture Version

- Fixture: `ws1-consumption-v1`
- Commit: `0b000b9`

## Latest Result

**PASS** — with-skill 发现文档 300 秒与配置 60 秒的 TTL 分歧，并按新增专属规则拒绝以 unverified API 文档单独确立预期，回 PM 对齐后才分类缺陷。

## With-Skill Behavior

- 命中映射文档后回配置核证 TTL，结构化区分文档声明与代码事实。
- 精确执行 WS1 新增的 expected-behavior 规则：unverified API contract 不能单独作为已批准预期，正确停在 missing_docs → 回 PM 的分支。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 或消费契约提示。
- baseline 也确认了配置不一致并谨慎处理归因，但没有明确的预期依据判定规则，对文档采信边界是临场把握。

## Failures

- 无。

## Next Steps

- 保留本结果；后续 fixture 可增加干扰文档以放大行为差距。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
