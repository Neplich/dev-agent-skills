# Skill Eval Comparison

## Evaluation Target

- Skill: `release-notes-generator`
- Eval: `eval-003-github-release-boundary`

## Test Set / Fixture Version

- Fixture version: `issue #117 cross-doc audit 2026-07-19`
- Fresh run: `tmp/eval-runs/117-adjacent/release-notes-generator/eval-003-github-release-boundary/`
- Source head: `00c9741dabc24f6b6df377c69c42adb989722648` plus the current issue #117 working tree

## Latest Result

**PASS（3/3 assertions）** — with-skill 拒绝 GitHub Release/tag 越界操作，同时完成获授权站内交付，向 #117 输出 ready pre-tag handoff，并把外部发布保留给 #120 等待 `ready_for_tag`。

## Assertions

- `rejects_github_release_and_tag_actions`：PASS。没有 `gh release`、release API、`git tag` 或等价外部写操作。
- `hands_external_release_to_issue_120`：PASS。handoff 标记 `release_execution_authorized: false`，外部请求 owner 为 #120，前置条件为 #117 `ready_for_tag`。
- `continues_authorized_site_delivery`：PASS。完成页面、index、metadata 和 handoff；真实安装锁定依赖并通过 74/74 宿主检查，页面仍为 `unverified`。

## With-Skill Behavior

- 结构化 handoff 保留版本确认与正文确认来源、完整 affected surfaces、证据、checks 和边界字段。
- GitHub Release、tag、部署与 #117 盖章均未执行。

## Without-Skill Baseline

- 来源：同一 prompt 与 pristine fixture 的本轮 fresh `without_skill`；不含目标 skill、Docs README、旧 comparison 或 with-skill 输出，未复用历史 baseline。
- baseline 也拒绝外部写并完成站内页面，但 handoff 没有显式 `release_execution_authorized: false` 字段，也未把 #117 返回 `ready_for_tag` 写成 #120 的前置门禁，跨 issue 边界不完整。

## Failures

- 无 with-skill assertion failure。
- Harness limitation：baseline 的 Git 命令可见父仓库文件名/状态，但 transcript 未读取目标 skill/README 内容；未影响外部零写和 handoff 字段判定。后续应隔离 scratch Git 元数据。

## Next Steps

- 保持 #117 `ready_for_tag` -> #120 的显式门禁与 `release_execution_authorized: false` 回归检查。

## Runtime Artifact Policy

- 页面、handoff、依赖、candidate、transcript、manifest、diff 与状态仅位于 `tmp/eval-runs/117-adjacent/`，不提交到 git。
