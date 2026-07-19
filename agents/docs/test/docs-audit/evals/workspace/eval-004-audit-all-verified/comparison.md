# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-004-audit-all-verified`

## Test Set / Fixture Version

- Fixture version: A3 / 2026-07-19
- Assertions: 4

## Latest Result

**PASS — 4 / 4 assertions passed.** Fresh with-skill 候选完成两页事实核验、完整集合统一盖章与回读，并在 `audit-v1.1.0.md` 中持久化页面及文件型版本面的精确字节证据后返回 `ready_for_tag`。

## Assertion Results

| Assertion | Result | Evidence summary |
| --- | --- | --- |
| `verifies_complete_affected_set` | PASS | `src/catalog/routes.txt` 命中 change-map 的两张 required docs；两页均逐项核对路由、鉴权、参数、响应、错误、流式与文件行为并判 `verified`，无证据缺口。 |
| `stamps_all_pages_together` | PASS | 两页只在完整集合通过后同时由 `v1.0.0` 更新为 `v1.1.0`，隔离副本回读均为 `v1.1.0`。 |
| `verifies_release_metadata_read_only` | PASS | `releases.json` 与目标版本一致；源 fixture 与运行副本内容未发生差异，报告仅记录其 SHA-256。 |
| `persists_versioned_report` | PASS | 报告记录 refs、目标版本、盖章后锚点、两页章前/章后值、页面与 #116 handoff、Release Notes、索引、metadata、宿主版本文件 SHA-256、结果时间、命令和 `ready_for_tag`；所有所记哈希均由 judge 回算匹配，且未表述为已发布。 |

## With-Skill Behavior

- 来源：本轮 fresh with-skill，使用应用 `docs-audit` 与 Docs README 后的同一 prompt 和 pristine 隔离副本；证据位于 `tmp/eval-runs/128-a3-20260719-213128/with_skill/eval-004-audit-all-verified/`。
- 实际变更仅为两张 API 页面统一盖章、创建契约路径审计报告及运行期输出；版本 metadata 保持只读。

## Without-Skill Baseline

- 来源：本轮 `fork_turns=none` 的独立 fresh baseline，仅读取本例 prompt/assertions 与 pristine fixture；证据位于 `tmp/eval-runs/128-a3-20260719-213128/without_skill/eval-004-audit-all-verified/`，未复用历史 baseline。
- baseline 完成两页盖章并返回 `ready_for_tag`，但成功报告未记录文件型 #116 handoff `.eval/release-context.md` 的 SHA-256，因此只满足 3 / 4 assertions；with-skill 对完整成功记录的版本面内容证据有可观测增益。

## Failures

- With-skill 无 assertion failure。
- Baseline 的 `persists_versioned_report` 未完整满足：缺少文件型 #116 handoff 内容哈希。
- fixture 使用合成 refs；隔离运行中的 post-stamp anchor 按 fixture 语义记录，不代表真实宿主仓库提交。

## Next Steps

- 保留本结果；成功记录字段、文件型 release surface 或统一盖章协议变化时重跑。

## Runtime Artifact Policy

- 本轮 `candidate-output.md`、`run-summary.md`、隔离盖章页面与审计报告只保留在 `tmp/eval-runs/128-a3-20260719-213128/`，不提交；durable 产物仅为本 `comparison.md`。
