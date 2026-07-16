# Consumption Regression Comparison

## Evaluation Target

- Skill: `privacy-surface-mapper`
- Eval: `eval-004-mapped-profile-retention`

## Test Set / Fixture Version

- Fixture: `ws1-consumption-v1`
- Commit: `0b000b9`

## Latest Result

**PASS** — with-skill 核证出文档 30 天与配置 90 天的保留期分歧并列为高风险，隐私面按代码证据梳理，缺证据项诚实标注而非推断。

## With-Skill Behavior

- 命中映射文档后回配置核证保留期限，产出结构化隐私映射报告并通过字段一致性验证。
- 法律依据、清除机制、用户权利等无证据项明确标注缺失，不虚构合规能力。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 或消费契约提示。
- baseline 同样识别 30/90 天冲突且证据边界谨慎，但未按契约组织分歧证据与隐私映射产物结构。

## Failures

- 无。

## Next Steps

- 保留本结果；后续 fixture 可增加干扰文档以放大行为差距。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
