# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-009-pre-tag-blocked`

## Test Set / Fixture Version

- Fixture version: A6 / 2026-07-19
- Assertions: 4

## Latest Result

**PASS — fresh with-skill 4 / 4 assertions passed.** 入口、页面事实与版本表面本可通过；完整 post-stamp 差异中出现白名单外的 `src/catalog/debug-trace.txt`，因此持久化越界差异并返回宿主阶段 `blocked`，不返回 `ready_for_tag`。

Fresh without-skill baseline 同样为 **4 / 4**。当前 prompt、release context 与独立 patch 已直接指出 staged 路径和预期边界，未观察到断言级 skill 增益。

## Assertion Results

| Assertion | With skill | Without skill | Evidence summary |
| --- | --- | --- | --- |
| `audits_valid_pre_tag_inputs` | PASS | PASS | 三项输入独立且已确认；actual diff 仅为 API 不变的 dispatcher 内部重构，两张 API 页、Release Notes、索引、releases.json 与 package 版本事实均可通过。 |
| `detects_unrelated_staged_path` | PASS | PASS | 完整 post-stamp diff 显示 `src/catalog/debug-trace.txt` 从 `TRACE disabled` 变为 `TRACE verbose`；该路径不属于盖章页、release Markdown 或审计记录。 |
| `persists_blocked_convergence_evidence` | PASS | PASS | 候选审计记录包含完整差异清单、逐路径授权判断、越界源码路径和 `blocked` 结论。 |
| `withholds_ready_for_tag` | PASS | PASS | 越界 staged 源码阻止 `ready_for_tag`、成功时间和可信成功 handoff。 |

## With-Skill Behavior

- 来源：本会话 A6 fresh with-skill validation；读取当前 `docs-audit` skill、内部指令、Docs README、同一 prompt/assertions 与更新后的 pristine fixture，不读取历史 comparison。
- 结果：4 / 4。确认事实层仅遇到纯内部重构，唯一 blocker 是盖章 commit 混入的无关 staged 源码；按协议记录越界差异并 withholding `ready_for_tag`。

## Without-Skill Baseline

- 来源：本会话 A6 fresh without-skill validation；仅读取同一 prompt/assertions、eval metadata 与 pristine fixture，不读取 skill、Docs README、comparison 或历史 baseline。
- 结果：4 / 4。也识别越界 staged 路径、持久化 blocked 证据并拒绝成功 handoff。
- 对比结论：无断言级差异；fixture 对唯一 blocker 与期望行为提示度较高。

## Failures and Limitations

- With-skill 与 baseline 均无 assertion failure。
- 这是只读协议模拟；fixture 没有真实 Git refs、post-stamp commit/tree/blob 或已落盘 audit record，不能证明真实 commit diff 与记录持久化已执行。
- 唯一 blocker 同时出现在 prompt、release context 和 patch 中，降低了 skill 区分度。

## Next Steps

- 当 pre-tag commit 差异白名单、blocked 持久化边界或 fixture 变化时，重新运行 fresh 配对验证。
- 后续提高区分度时，减少 release context 对越界结论的直接陈述，只保留原始 staged diff 证据。

## Runtime Artifact Policy

- 本轮只使用当前会话最终有效的 fresh with-skill、fresh without-skill 与独立 judge 结果，未复用历史 baseline。
- 未创建、引用或提交 `tmp/`、transcript、candidate output、verdict、timing 或其他运行期产物；durable 产物仅为本 `comparison.md`。
