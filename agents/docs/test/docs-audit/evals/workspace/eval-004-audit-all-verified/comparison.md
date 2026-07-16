# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-004-audit-all-verified`

## Test Set / Fixture Version

- Fixture: `ws2-docs-v1`
- Commit: `c05f689`

## Latest Result

**PASS** — with-skill 在显式 base/target 与版本锚 v1.1.0 下判定全部 verified：统一盖章两张受审页面、同步 releases.json 三字段、报告落 audit-v1.1.0.md、release 建议 proceed。

## With-Skill Behavior

- 统一盖章语义完整执行（不局部盖章场景的正向验证），diff 清单复现与版本戳一致性检查通过。
- fixture SHA 非真实 Git 对象的限制在报告中显式记录，以 .eval diff 为确定性证据。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 文档。
- baseline 因无法解析 SHA 且无 skill 协议而拒绝执行审计与盖章——保守正确但未交付审计产物，与 with-skill 形成鲜明对照。

## Failures

- 无。

## Next Steps

- 保留本结果。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
