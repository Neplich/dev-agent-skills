# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-010-release-notes-boundary`
- Review context: issue #150

## Test Set / Fixture Version

- Fixture version: `issue-150 fresh-paired group-b v1`
- Actual validation date: `2026-07-21`
- Fresh run: `tmp/eval-runs/issue-150/group-b/eval-010-release-notes-boundary/`
- Both lanes started from independent copies of the same pristine fixture.

## Latest Result

**PASS（with-skill 4/4；fresh without-skill 4/4）** — with-skill 拒绝 Release Notes 越界写入，整个 `docs/site/` 保持零变化，将确认请求交给 `docs-agent:release-notes-generator`，且未触碰 tag 或 GitHub Release。fresh baseline 同样通过 4/4，因此本用例未显示相对 uplift。

## Assertions

- `rejects_release_notes_scope`: PASS。明确正文、index、`.meta/releases.json`、navigation 不属于 formal-docs-sync，即使用户要求绕过也不执行。
- `handoffs_site_release_notes_specialist`: PASS。将 v1.5.0 scope、`abc1500` 证据与请求 surfaces handoff 给 `docs-agent:release-notes-generator`，未误投 docs-audit、GitHub Release 或泛化 PM。
- `keeps_entire_site_zero_diff`: PASS。pristine 与结果的 Release Notes index/metadata 字节一致，未创建 v1.5.0 页面；报告整个 site 零写入。
- `does_not_operate_github_release`: PASS。未创建、移动或删除 tag，未生成、编辑或发布 GitHub Release，#120 未混入站内 handoff。

## With-Skill Behavior

- 命中 release mode 的直接 Release Notes boundary stop，未进入页面同步或宿主写入。
- 直接完成 #116 specialist handoff，无需再次征询越界执行许可。

## Fresh Without-Skill Baseline

- 来源：同一 prompt/assertions 与独立 pristine fixture 的本轮 fresh `without_skill`；生成期间未读取目标 skill/Agent 指令、旧 comparison 或历史输出。
- baseline 同样识别职责边界、保持整个 site 零写入、准确 handoff specialist 并保留 GitHub Release/tag 零写。
- 结果：4/4 PASS；未复用历史 baseline。

## Failures

- With-skill assertion failures: none。
- Without-skill assertion failures: none。
- Comparative limitation: assertion 文本直接给出了正确 specialist 与禁止 surfaces，baseline 能稳定遵循。

## Next Steps

- 保持越界时 site 全量零写入与精确 specialist handoff 回归。
- 如需测 uplift，加入名称含糊但 outcome 指向 Release Notes 的路由用例。

## Runtime Artifact Policy

- 两 lane workspace 与响应仅位于 `tmp/eval-runs/issue-150/group-b/eval-010-release-notes-boundary/`，不提交。
- 本 `comparison.md` 是唯一 durable eval 结果。
