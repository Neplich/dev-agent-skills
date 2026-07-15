# Consumption Regression Comparison

## Evaluation Target

- Skill: `env-config-auditor`
- Eval: `eval-003-mapped-doc-config-audit`

## Test Set / Fixture Version

- Fixture: `ws1-consumption-v1`
- Commit: `0b000b9`

## Latest Result

**PASS** — with-skill 按 change-map 定位文档、以 required.env 核证出文档 optional 声明与代码 required 的分歧，审计结论以代码为准并落档 ENV_AUDIT 报告。

## With-Skill Behavior

- 消费路径完全按契约：change-map 定位 → 文档声明 → 回代码验证 → 以代码为准判定 API_TOKEN 必填。
- 产出结构化审计报告，未覆盖的环境（Docker/Helm/CI）诚实标记无法确认。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 或消费契约提示。
- baseline 也得出 required 为准的结论并建议修正文档，但读取路径未经 change-map 组织，审计证据的结构化程度较低。

## Failures

- 无。

## Next Steps

- 保留本结果；后续 fixture 可增加干扰文档以放大行为差距。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
