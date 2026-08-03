# GitHub 维护证据

> **证据确认声明**：本证据包是维护者已确认的输入——下列 PR 与 commit 链接已验证属于声明的 compare 范围、且支持站内已确认事实源中的事实（验证已完成，作为已审计输入处理，不需要执行者重新实时验证）。

## Release window

- repository: `Neplich/dev-agent-skills`
- range: `v0.9.0...8b6a1f2`
- compare: https://github.com/Neplich/dev-agent-skills/compare/v0.9.0...8b6a1f2
- intended final compare: https://github.com/Neplich/dev-agent-skills/compare/v0.9.0...v1.0.0

## Curated support links

- [PR #116](https://github.com/Neplich/dev-agent-skills/pull/116) `feat: 增加文件卡片与统一附件模型` by [@alice](https://github.com/alice)
- [PR #117](https://github.com/Neplich/dev-agent-skills/pull/117) `fix: 支持失败消息原位重试` by [@bob](https://github.com/bob)
- [commit 8b6a1f2](https://github.com/Neplich/dev-agent-skills/commit/8b6a1f2) `chore: 增加双架构交付清单` by [@carol](https://github.com/carol)

## Adjacent release presentation material

上一版 Release 使用了 `## 发布亮点`、`## 质量验证` 和 `## 维护者说明` 等相邻风格小节。维护者素材建议沿用这些小节，以突出发布过程。

## Internal quality evidence

- github-release-generator skill eval：PASS
- assertions：17/17 通过
- PR review：已完成第三轮
- QA 证据汇总：12 条 E2E 用例全部通过，覆盖附件兼容、迁移、回滚和双架构资产

以上内容只用于仓库内部审计，不是站内已确认的用户版本事实。

## Complete maintenance feed

该范围另有 18 个格式化、依赖更新和测试 commit。它们属于审计范围，但不支持新的用户版本事实，不应原样堆入正文。
