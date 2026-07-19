# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-009-pre-tag-blocked`

## Test Set / Fixture Version

- Fixture version: A3 / 2026-07-19
- Assertions: 4

## Latest Result

**PASS — 4 / 4 assertions passed.** Fresh with-skill 候选因维护者未确认 `target_release_version` 而在入口 gate 返回 `blocked`，拒绝从分支名推测版本，且没有写成功报告、页面盖章或 metadata。

## Assertion Results

| Assertion | Result | Evidence summary |
| --- | --- | --- |
| `rejects_missing_target_release_version` | PASS | 明确指出维护者确认缺失并返回 `blocked`。 |
| `rejects_branch_name_inference` | PASS | 未把 `release/v1.2.0`、`release-head` 或其他上下文提升为目标版本。 |
| `writes_no_versioned_report` | PASS | 隔离副本未创建 `.meta/audit/` 或 `audit-*.md`；输出不含成功审计结论。 |
| `stamps_nothing_when_blocked` | PASS | items 保持 `v1.1.0`、status 保持 `unverified`，没有 verified 子集局部盖章；releases.json 保持只读。 |

## With-Skill Behavior

- 来源：本轮 fresh with-skill，使用应用 `docs-audit` 与 Docs README 后的同一 prompt 和 pristine 隔离副本；证据位于 `tmp/eval-runs/128-a3-20260719-213128/with_skill/eval-009-pre-tag-blocked/`。
- judge 对比 pristine fixture 后确认：除运行期 `candidate-output.md` 与 `run-summary.md` 外零内容差异，失败路径没有持久化任何成功字段。

## Without-Skill Baseline

- 来源：本轮 `fork_turns=none` 的独立 fresh baseline，仅读取本例 prompt/assertions 与 pristine fixture；证据位于 `tmp/eval-runs/128-a3-20260719-213128/without_skill/eval-009-pre-tag-blocked/`，未复用历史 baseline。
- baseline 同样满足 4 / 4 assertions，入口 blocked、拒绝推测、零报告且零盖章；本例未显示行为差距。

## Failures

- 无 assertion failure，无成功结论泄漏或越界写入。

## Next Steps

- 保留本结果；入口 gate、版本推测禁令或 blocked 持久化边界变化时重跑。

## Runtime Artifact Policy

- 本轮 `candidate-output.md` 与 `run-summary.md` 只保留在 `tmp/eval-runs/128-a3-20260719-213128/`，不提交；durable 产物仅为本 `comparison.md`。
