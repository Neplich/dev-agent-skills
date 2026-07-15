# Consumption Regression Comparison

## Evaluation Target

- Skill: `incident-playbook-writer`
- Eval: `eval-002-mapped-doc-incident-playbook`

## Test Set / Fixture Version

- Fixture: `ws1-consumption-v1`
- Commit: `0b000b9`

## Latest Result

**PASS** — with-skill 以代码阈值 5 次为准制定处置手册，文档记载的 3 次被识别为 unverified 分歧，且在无部署配置时不虚构回滚命令。

## With-Skill Behavior

- 命中映射文档后回代码核证健康检查阈值，手册流程锚定代码事实。
- 保持证据边界：无 Docker/Helm/CI 证据时不臆造平台命令，明确要求发布负责人补齐。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 或消费契约提示。
- baseline 同样不臆造命令且流程合理，但对文档阈值分歧的处理未形成契约格式的证据记录。

## Failures

- 无。

## Next Steps

- 保留本结果；后续 fixture 可增加干扰文档以放大行为差距。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
