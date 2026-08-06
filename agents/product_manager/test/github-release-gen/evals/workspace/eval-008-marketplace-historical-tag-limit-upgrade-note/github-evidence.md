# GitHub 维护证据

> **证据确认声明（mock 输入）**：本证据包是测试用 mock 数据，模拟「维护者已完成的 GitHub 验证」结果——下列 PR 与 commit 链接视为已属于声明的 compare 范围、且支持站内已确认事实源中的事实。执行者直接作为已审计输入使用，不得也不需要对它们做实时远端验证（这些链接是虚构对象）。

## Release window

- repository: `Neplich/dev-agent-skills`
- range: `v0.8.0...v0.9.0`
- compare: https://github.com/Neplich/dev-agent-skills/compare/v0.8.0...v0.9.0
- intended final compare: https://github.com/Neplich/dev-agent-skills/compare/v0.8.0...v0.9.0

## Curated support links

- [PR #98](https://github.com/Neplich/dev-agent-skills/pull/98) `feat: 支持失败消息原位重试` by [@alice](https://github.com/alice)
- [PR #99](https://github.com/Neplich/dev-agent-skills/pull/99) `fix: 统一附件模型链路兼容` by [@bob](https://github.com/bob)
- [commit a1b2c3d](https://github.com/Neplich/dev-agent-skills/commit/a1b2c3d) `chore: 增加双架构交付清单` by [@carol](https://github.com/carol)

## Adjacent release presentation material

上一版 Release 使用了 `## 发布亮点`、`## 质量验证` 和 `## 维护者说明` 等相邻风格小节。维护者素材建议沿用这些小节，以突出发布过程。

## Internal quality evidence

- github-release-gen skill eval：PASS
- assertions：14/14 通过
- PR review：已完成第二轮
- QA 证据汇总：8 条 E2E 用例全部通过，覆盖附件兼容与回滚

以上内容只用于仓库内部审计，不是站内已确认的用户版本事实。

## Complete maintenance feed

该范围另有 15 个格式化、依赖更新和测试 commit。它们属于审计范围，但不支持新的用户版本事实，不应原样堆入正文。
