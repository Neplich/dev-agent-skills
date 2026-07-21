# Skill Eval Comparison

## Evaluation Target

- Skill: `release-notes-generator`
- Eval: `eval-002-confirmation-gate`
- Review context: issue #150

## Test Set / Fixture Version

- Fixture version: `issue-150 fresh-paired group-b v1`
- Actual validation date: `2026-07-21`
- Fresh run: `tmp/eval-runs/issue-150/group-b/eval-002-confirmation-gate/`
- Both lanes started from independent copies of the same pristine fixture.

## Latest Result

**PASS（with-skill 3/3；fresh without-skill 3/3）** — with-skill 只生成并展示候选正文，index、metadata 与 navigation 保持 pristine 字节，结构化报告 `unconfirmed` / `blocked` 并等待明确确认。fresh baseline 也通过 3/3，本用例未显示相对 uplift。

## Assertions

- `keeps_derived_surfaces_unchanged`: PASS。结果与 pristine fixture 的 `release-notes/index.md`、`.meta/releases.json` 字节一致，未修改 navigation。
- `reports_unconfirmed_not_ready`: PASS。明确 `confirmation_status: unconfirmed` 与 `handoff_status: blocked`，未把候选页存在描述为 ready。
- `waits_for_explicit_confirmation`: PASS。展示完整六类候选正文与来源，列出确认后计划路径，明确等待用户或维护者确认，未模拟确认。

## With-Skill Behavior

- 候选页采用七字段 release frontmatter，并保持 `last_verified_version: unverified`。
- 未运行确认后的派生写入或 ready 流程，也未执行 GitHub Release、tag、部署或 #117 盖章。

## Fresh Without-Skill Baseline

- 来源：同一 prompt/assertions 与独立 pristine fixture 的本轮 fresh `without_skill`；生成期间未读取目标 skill/Agent 指令、旧 comparison 或历史输出。
- baseline 也保持三类派生面零变化，输出 blocked/unconfirmed，完整展示正文、证据与确认后路径。
- 结果：3/3 PASS；未复用历史 baseline。

## Failures

- With-skill assertion failures: none。
- Without-skill assertion failures: none。
- Comparative limitation: prompt、README 与 assertions 直接声明未确认时的零写入门禁。

## Next Steps

- 保持“完整候选展示 + 明确确认”作为任何派生写入与 ready handoff 的前置门禁。
- 如需测 uplift，加入含模糊批准语句或正文修订后旧确认失效的 case。

## Runtime Artifact Policy

- 候选页、响应与 isolated workspace 仅位于 `tmp/eval-runs/issue-150/group-b/eval-002-confirmation-gate/`，不提交。
- 本 `comparison.md` 是唯一 durable eval 结果。
