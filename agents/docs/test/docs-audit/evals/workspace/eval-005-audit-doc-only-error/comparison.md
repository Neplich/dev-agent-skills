# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-005-audit-doc-only-error`

## Test Set / Fixture Version

- Fixture: `ws2-docs-v1`
- Commit: `c05f689`

## Latest Result

**PASS** — with-skill 把无代码 diff 的纯文档变更页面直接纳入影响域，事实层核证出文档新增 DELETE 端点而代码只有 GET，判 mismatch、blocked、不盖章。

## With-Skill Behavior

- 纯文档错误不因无代码变更放行，归属确认交回负责团队。
- 只产出审计报告，版本元数据零改动。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 文档。
- baseline 同样判 mismatch 阻断，方向一致；差异在影响域纳入规则与报告协议的显式执行。

## Failures

- 无。

## Next Steps

- 保留本结果。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
