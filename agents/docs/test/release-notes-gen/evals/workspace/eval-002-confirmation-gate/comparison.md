# Skill Eval Comparison

## Evaluation Target

- Skill: `release-notes-generator` → `release-notes-gen`（改名后新入口待重跑验证）
- Eval: `eval-002-confirmation-gate`
- Review context: issue #150

## Test Set / Fixture Version

- Fixture version: `issue-150 fresh-paired group-b v1`
- Actual validation date: `2026-07-21`
- Fresh run: `tmp/eval-runs/issue-150/group-b/eval-002-confirmation-gate/`
- Both lanes started from independent copies of the same pristine fixture.

## Latest Result

- Overall result: PASS
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `PASS` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| keeps_derived_surfaces_unchanged | PASS | PASS | with_skill 的 `releases.json` 仍为 `latest: v0.9.0`，未新增索引/导航文件；without_skill 同样仅新增 `v1.0.0.md`，派生面保持原状。 |
| reports_unconfirmed_not_ready | PASS | PASS | with_skill 明确 `confirmation_status: unconfirmed`、`handoff_status: blocked`；without_skill 正文标注“待确认”，并明确确认前不纳入版本索引、metadata 或站点导航，属于未 ready 状态。 |
| waits_for_explicit_confirmation | PASS | FAIL | with_skill 展示完整候选正文、列出 `evidence/01` 至 `evidence/06` 来源，并写明“请确认该正文”及确认后更新 metadata/索引；without_skill 仅写“待确认”，未列出来源证据，也未明确等待确认后的修改计划路径。 |

未满足断言（with/without 任一 FAIL）：`waits_for_explicit_confirmation`



## Assertions
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- `keeps_derived_surfaces_unchanged`: PASS。结果与 pristine fixture 的 `release-notes/index.md`、`.meta/releases.json` 字节一致，未修改 navigation。
- `reports_unconfirmed_not_ready`: PASS。明确 `confirmation_status: unconfirmed` 与 `handoff_status: blocked`，未把候选页存在描述为 ready。
- `waits_for_explicit_confirmation`: PASS。展示完整六类候选正文与来源，列出确认后计划路径，明确等待用户或维护者确认，未模拟确认。

## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 候选页采用七字段 release frontmatter，并保持 `last_verified_version: unverified`。
- 未运行确认后的派生写入或 ready 流程，也未执行 GitHub Release、tag、部署或 #117 盖章。

## Fresh Without-Skill Baseline

- 来源：同一 prompt/assertions 与独立 pristine fixture 的本轮 fresh `without_skill`；生成期间未读取目标 skill/Agent 指令、旧 comparison 或历史输出。
- baseline 也保持三类派生面零变化，输出 blocked/unconfirmed，完整展示正文、证据与确认后路径。
- 结果：3/3 PASS；未复用历史 baseline。

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- With-skill assertion failures: none。
- Without-skill assertion failures: none。
- Comparative limitation: prompt、README 与 assertions 直接声明未确认时的零写入门禁。

## Next Steps

- 保持“完整候选展示 + 明确确认”作为任何派生写入与 ready handoff 的前置门禁。
- 如需测 uplift，加入含模糊批准语句或正文修订后旧确认失效的 case。

## Runtime Artifact Policy

- 候选页、响应与 isolated workspace 仅位于 `tmp/eval-runs/issue-150/group-b/eval-002-confirmation-gate/`，不提交。
- 本 `comparison.md` 是唯一 durable eval 结果。

## 磨平记录（2026-07-29）

维护者裁定本 eval 的零区分度属于模型能力进步磨平（(b) 类），批次 4 的重写已回滚。该 eval 作为 [issue #188](https://github.com/neplich/dev-agent-skills/issues/188) 的 skill 能力审查标本保留原样；在 #188 得出审查结论前不重做本 eval。
