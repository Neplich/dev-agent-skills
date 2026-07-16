# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-003-audit-pure-refactor`

## Test Set / Fixture Version

- Fixture: `ws2-docs-v1`
- Commit: `c05f689`

## Latest Result

**PASS** — with-skill 对命中 change-map 的纯实现重构判 verified：API 契约逐项核对未变化，不强制文档编辑、不 blocked，全 verified 后统一盖章 v1.1.0 并同步 releases.json，release 建议 proceed。

## With-Skill Behavior

- suspect 两段式判定正确：确定性层圈候选、事实层核对契约后放行。
- 审计报告落 .meta/audit/audit-v1.1.0.md，SHA 证据来源限制明确记录。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 文档。
- baseline 同样得出不应阻塞的结论且不改写准确文档，但未执行盖章语义与报告归档协议。

## Failures

- 无。

## Next Steps

- 保留本结果。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
