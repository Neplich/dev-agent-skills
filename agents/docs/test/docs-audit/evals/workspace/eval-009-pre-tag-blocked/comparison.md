# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-009-pre-tag-blocked`

## Test Set / Fixture Version

- Fixture version: issue #117 A2 / 2026-07-19
- Assertions: 4

## Latest Result

**PASS — 4 / 4 assertions passed.** Fresh with-skill 候选因维护者未确认目标版本且分支名只能推测而立即 `blocked`；只读诊断识别 1 verified/1 stale，但没有版本化报告、任何 stamp 或 metadata 写入。

## Assertion Results

| Assertion | Result | Evidence summary |
| --- | --- | --- |
| `rejects_missing_target_release_version` | PASS | 明确记录 `target_release_version` 缺失且未经维护者确认，结果 `blocked`。 |
| `rejects_branch_name_inference` | PASS | `release/v1.2.0` 只作为上下文，没有从分支或 target ref 推断版本。 |
| `writes_no_versioned_report` | PASS | cleanup 后审计目录不存在，运行结束 workspace 零写入，仅返回只读诊断与补充确认待办。 |
| `stamps_nothing_when_blocked` | PASS | items 保持 `v1.1.0`、status 保持 `unverified`，没有给 verified 子集局部盖章，releases.json 不变。 |

## With-Skill Behavior

- 来源：本轮 fresh with-skill，证据位于 `tmp/eval-runs/117/eval-009-pre-tag-blocked/with_skill/`。
- 候选在入口阻塞后仍以只读方式证明 mixed set 场景不会被局部盖章，且记录 status 页遗漏鉴权与 401 的 stale 证据。

## Without-Skill Baseline

- 来源：本轮独立 fresh baseline，使用同一 prompt 与 pristine fixture，证据位于 `tmp/eval-runs/117/eval-009-pre-tag-blocked/without_skill/`；未复用历史 baseline。
- baseline 也拒绝推测、blocked 且零写入，但选择不进入页面级只读诊断，无法提供 mixed set 零局部盖章的同等事实证据。

## Failures

- 无 assertion failure，无 harness 或协议缺陷。

## Next Steps

- 保留本结果；入口 gate、推测版本禁令或 partial-stamp 边界变化时重跑。

## Runtime Artifact Policy

- 本轮运行期证据仅位于 `tmp/eval-runs/117/`，不提交；durable 产物仅为本 `comparison.md`。
