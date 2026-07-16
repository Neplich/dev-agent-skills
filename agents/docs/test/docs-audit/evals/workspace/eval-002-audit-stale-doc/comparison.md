# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-002-audit-stale-doc`

## Test Set / Fixture Version

- Fixture: `ws2-docs-v1`
- Commit: `c05f689`

## Latest Result

**PASS** — with-skill 确定性层记 suspect 后事实层确认文档过期（遗漏 locale 必填参数、invalid_locale 错误、limit 默认/上限）判 stale，release blocked、不盖章，解锁路径指向 formal-docs-sync 同步后复审。

## With-Skill Behavior

- 两段式判定完整：不因未改文档直接 stale，由事实核对确认不同步后才阻塞。
- 只产出审计报告，未越权改文档或版本元数据。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 文档。
- baseline 也识别了文档缺口，但阻塞语义、盖章禁止与复审路径由临场组织，未按审计协议产出三态报告。

## Failures

- 无。

## Next Steps

- 保留本结果。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
