# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-006-audit-no-version-anchor`

## Test Set / Fixture Version

- Fixture: `ws2-docs-v1`
- Branch fixture commit: `71bbb09`

## Latest Result

**PASS** — fresh judge 对 4 条 assertions 全部判定 PASS。with-skill 在没有 tag、GitHub Release 或显式版本锚时仍完成确定性层与事实层审计，将页面判为 `verified`，把报告写入 `docs/site/.meta/audit/audit-7c9e2af.md`，记录 `version_anchor: unavailable`，并保持 `last_verified_version: unverified`、不创建或修改 `.meta/releases.json`。

## With-Skill Behavior

- 使用显式 `e1f2a3b..7c9e2af` 范围完成 change-map 命中、`suspect` 识别和事实层逐项核对，确认 dispatcher 重构未改变 API 对外行为。
- 报告路径、target 短 SHA 回退命名和机器可读版本锚不可用标记均符合协议。
- 区分“事实结论为 `verified`”与“无版本锚所以不得盖章”，页面和 release metadata 均未改写。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，使用相同原始 prompt 与 fixture，新生成且未接触 skill 文档或 Agent README。
- baseline 同样识别内部重构、记录版本锚不可用并保持页面 `unverified`，但把报告写入错误的 `docs/site/_reports/audit-report-7c9e2af.md`。
- baseline 未完整保存 `suspect → fact layer → verified` 两层审计链路，也没有清晰区分事实核验结论与版本盖章状态。

## Failures

- 无 assertion failure。

## Next Steps

- 保留本结果；后续修改无版本锚审计或报告路径协议时重跑此 eval。

## Runtime Artifact Policy

- 本次 transcripts、workspace 副本和 judge verdict 仅位于 `tmp/eval-runs/118/eval-006-audit-no-version-anchor/`，不提交到 git。
