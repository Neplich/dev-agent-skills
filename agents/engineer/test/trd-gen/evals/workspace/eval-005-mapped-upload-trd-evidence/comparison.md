# Consumption Regression Comparison

## Evaluation Target

- Skill: `trd-gen`
- Eval: `eval-005-mapped-upload-trd-evidence`

## Test Set / Fixture Version

- Fixture: `ws1-consumption-v1`
- Commit: `0b000b9`

## Latest Result

**PASS** — with-skill 以接口证据核查发现代码 10 MB 与文档 20 MB 的上限冲突，按 gate 停在 PM 决策点补齐产品基线，未带着未验证预期起草 TRD。

## With-Skill Behavior

- 命中映射文档后回代码核证上传上限，识别并结构化列出 10 MB / 20 MB 冲突与待确认契约问题。
- 严格遵守协作链：PM 确认 → TRD → 维护者确认 → 实施计划，未越权产出正式 TRD。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 或消费契约提示。
- baseline 同样发现冲突并请求基线确认，但对文档采信边界与协作链停点的处理是临场组织，未引用契约协议。

## Failures

- 无。

## Next Steps

- 保留本结果；后续 fixture 可增加干扰文档以放大行为差距。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
