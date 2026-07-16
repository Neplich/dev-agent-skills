# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-001-sync-feature-api`

## Test Set / Fixture Version

- Fixture: `ws2-docs-v1`
- Commit: `c05f689`

## Latest Result

**PASS** — with-skill 只更新命中 API 文档并从代码/契约测试取 path、参数、错误结构，保留人工 change-map 条目与 exclusions，未声称 database/ops 同步完成，测试环境限制诚实标注。

## With-Skill Behavior

- 文档事实全部来自实现与测试证据，认证行为无证据即不写入；页面置 unverified 等待审计。
- change-map 合并态核对正确（无重复条目、手工条目保留），建议下一节点 docs-audit。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 文档。
- baseline 同样完成了正确的同步与幂等合并，行为质量高；差异在协议引用与验证限制记录的结构化程度。

## Failures

- 无。

## Next Steps

- 保留本结果。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
