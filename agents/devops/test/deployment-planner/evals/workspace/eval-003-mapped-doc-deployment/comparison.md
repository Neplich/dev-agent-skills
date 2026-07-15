# Consumption Regression Comparison

## Evaluation Target

- Skill: `deployment-planner`
- Eval: `eval-003-mapped-doc-deployment`

## Test Set / Fixture Version

- Fixture: `ws1-consumption-v1`
- Commit: `0b000b9`

## Latest Result

**PASS** — with-skill 以配置文件 8081 为部署事实、识别文档 8080 声明为分歧并给出健康检查/流量转发失败的具体影响，部署方案锚定代码证据。

## With-Skill Behavior

- 命中映射文档后以 server.conf 核证端口，分歧以文档/代码/影响/建议表结构化输出。
- 部署拓扑图与配置基于代码事实 8081，不采信 unverified 文档端口。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 或消费契约提示。
- baseline 同样识别端口冲突并锚定实际配置，工程判断合格，但分歧记录为叙述式，未按契约形成结构化证据。

## Failures

- 无。

## Next Steps

- 保留本结果；后续 fixture 可增加干扰文档以放大行为差距。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
