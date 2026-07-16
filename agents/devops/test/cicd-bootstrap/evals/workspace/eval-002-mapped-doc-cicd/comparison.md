# Consumption Regression Comparison

## Evaluation Target

- Skill: `cicd-bootstrap`
- Eval: `eval-002-mapped-doc-cicd`

## Test Set / Fixture Version

- Fixture: `ws1-consumption-v1`
- Commit: `0b000b9`

## Latest Result

**PASS** — with-skill 以 pipeline.rules 的 verify 命令核证出文档声称 test 的分歧，CI 配置锚定代码事实，且在平台不明时不落盘 workflow 文件。

## With-Skill Behavior

- 命中映射文档后回规则文件核证校验命令，分歧以文档/代码/判断/影响表结构化输出。
- 保持工程边界：平台未确认不写 CI 文件，runner 可用性问题诚实标注。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 或消费契约提示。
- baseline 同样识别 verify 为准并保持不落盘，但分歧记录为叙述式，未形成契约格式证据。

## Failures

- 无。

## Next Steps

- 保留本结果；后续 fixture 可增加干扰文档以放大行为差距。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
