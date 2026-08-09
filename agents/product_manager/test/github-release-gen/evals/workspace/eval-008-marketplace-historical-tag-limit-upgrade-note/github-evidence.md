# GitHub 维护证据

> **离线证据快照**：发布负责人已在导出时核对下列 compare、PR 与 commit，
> 并确认它们属于本次 Release 范围。当前评审环境没有远端访问权限，预览以这份
> 已签认快照为维护证据；真正发布仍需完成发布门禁与维护者批准。

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

- release tooling acceptance suite：PASS
- assertions：14/14 通过
- PR review：已完成第二轮
- QA 证据汇总：8 条 E2E 用例全部通过，覆盖附件兼容与回滚

以上内容只用于仓库内部审计，不是站内已确认的用户版本事实。

## Complete maintenance feed

该范围另有 15 个格式化、依赖更新和测试 commit。它们属于审计范围，但不支持新的用户版本事实，不应原样堆入正文。
