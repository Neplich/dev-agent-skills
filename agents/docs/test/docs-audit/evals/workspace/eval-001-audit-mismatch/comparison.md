# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-001-audit-mismatch`

## Test Set / Fixture Version

- Fixture version: issue #117 A2 / 2026-07-19
- Assertions: 4

## Latest Result

**PASS — 4 / 4 assertions passed.** Fresh with-skill 候选把映射命中的页面送入事实层，保留 `POST` 文档声明与 `GET` 代码事实并判为 `mismatch`，结果 `blocked`、零盖章。

## Assertion Results

| Assertion | Result | Evidence summary |
| --- | --- | --- |
| `includes_mapped_page` | PASS | `.eval/actual-diff.patch` 中的 `src/catalog/routes.txt` 命中 `src/catalog/**`，`catalog.md` 被纳入完整影响域。 |
| `classifies_direct_conflict_mismatch` | PASS | 报告并列保存 `POST /catalog/items`、`GET /catalog/items`、证据路径和调用影响，最终状态为 `mismatch`。 |
| `blocks_with_conflict_evidence` | PASS | 阶段结果为 `blocked`，要求负责方确认修文档还是修代码，未返回 `ready_for_tag`。 |
| `does_not_stamp_blocked_set` | PASS | 页面仍为 `v1.0.0`，未修改或创建 `.meta/releases.json`，没有局部盖章。 |

## With-Skill Behavior

- 来源：本轮 fresh session `019f7a73-2e16-7092-9d5d-a30bed3dd18c`，证据位于 `tmp/eval-runs/117/eval-001-audit-mismatch/with_skill/`。
- 候选写入契约路径 `docs/site/.meta/audit/audit-v1.1.0.md`，报告包含三项独立输入、影响域、冲突证据、blocker 和复核命令。

## Without-Skill Baseline

- 来源：本轮独立 fresh session `019f7a77-66e9-7a00-a328-c2041378d9b0`，同一 prompt 与 pristine fixture，证据位于 `tmp/eval-runs/117/eval-001-audit-mismatch/without_skill/`；未复用历史 baseline。
- baseline 也识别冲突并阻塞，但报告写入非契约路径 `.eval/docs-audit-report.md`，结构化 release-surface 与审计协议证据较弱。

## Failures

- 无 assertion failure。合成 refs 不在 Git object store 中，候选使用 fixture-authoritative `.eval/actual-diff.patch` 复现端点差异；这是已披露的 harness 限制，不是协议缺陷。

## Next Steps

- 保留本结果；docs-audit 冲突分类或 blocked 写入边界变化时重跑。

## Runtime Artifact Policy

- transcripts、候选输出、workspace 副本和 manifest 仅保留在 `tmp/eval-runs/117/`，不提交；durable 产物仅为本 `comparison.md`。
