# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-007-frontmatter-contract-fixtures`

## Test Set / Fixture Version

- Fixture version: issue #117 A2 / 2026-07-19
- Assertions: 8

## Latest Result

**PASS — 8 / 8 assertions passed.** Fresh with-skill 候选接受维护者确认的等效入口，按共享 frontmatter 真源得到 1 个合法页面 `verified`、4 个非法页面 `stale`，pre-tag `blocked` 且不局部盖章。

## Assertion Results

| Assertion | Result | Evidence summary |
| --- | --- | --- |
| `accepts_confirmed_audit_entry` | PASS | 从 `release-entry.md` 分别解析 `v0.4.0`、base `4a1b2c3`、target `7c9e2af`、pre-tag 请求和证据清单，未从 ref 推断版本。 |
| `rejects_standard_doc_type` | PASS | `doc_type: standard` 不在合法枚举中，页面判 `stale`。 |
| `rejects_empty_related_code` | PASS | `related_code: []` 违反非空字符串数组契约，页面判 `stale`。 |
| `rejects_missing_last_verified_version` | PASS | 缺少无条件必填的 `last_verified_version`，页面判 `stale`。 |
| `rejects_empty_owners` | PASS | `owners: []` 违反非空字符串数组契约，页面判 `stale`。 |
| `accepts_valid_api_page` | PASS | 合法页七字段通过，并以 `routes.txt` 核对 GET/200/items 后判 `verified`。 |
| `blocks_release_for_invalid_frontmatter` | PASS | 完整集合含 4 个 stale，阶段 `blocked`，合法页保持 `unverified`，没有局部盖章。 |
| `uses_shared_contract_source` | PASS | 报告明确以 `frontmatter-contract.md` 为真源，并说明判定与 bootstrap 宿主 validator 应实现的共享契约一致；fixture 不含脚本，未虚构执行。 |

## With-Skill Behavior

- 来源：本轮成功 fresh rerun，证据位于 `tmp/eval-runs/117/eval-007-frontmatter-contract-fixtures/with_skill/`；首次并发尝试未产出最终候选，已从判定证据中排除。
- 候选只新增 `audit-v0.4.0.md`，未修复 fixture、修改页面 stamp 或创建 metadata。

## Without-Skill Baseline

- 来源：本轮独立 fresh baseline，使用同一 prompt 与 pristine fixture，证据位于 `tmp/eval-runs/117/eval-007-frontmatter-contract-fixtures/without_skill/`；未复用历史 baseline。
- baseline 也得到 1 合法/4 stale 与 blocked，但零写入，且无法提供 docs-audit 入口 gate、共享契约真源和契约报告持久化的同等证据。

## Failures

- 无 assertion failure。fixture 的合成 refs 不可解析且未附 patch；候选按维护者确认的 evidence inventory 复现影响集合并明确限制。本 eval 核心是入口与 frontmatter 契约，故为 harness 限制而非协议缺陷。

## Next Steps

- 保留本结果；入口 gate、共享 frontmatter 契约或 bootstrap validator 变化时重跑。

## Runtime Artifact Policy

- 本轮候选、transcripts、workspace 副本与失败尝试诊断仅位于 `tmp/eval-runs/117/`，不提交；durable 产物仅为本 `comparison.md`。
