# GitHub 维护证据

## Release window

- repository: `example/ai-hub`
- range: `v0.9.0...8b6a1f2`
- compare: https://github.com/example/ai-hub/compare/v0.9.0...8b6a1f2
- intended final compare: https://github.com/example/ai-hub/compare/v0.9.0...v1.0.0

## Curated support links

- [PR #116](https://github.com/example/ai-hub/pull/116) `feat: 增加文件卡片与统一附件模型` by [@alice](https://github.com/alice)
- [PR #117](https://github.com/example/ai-hub/pull/117) `fix: 支持失败消息原位重试` by [@bob](https://github.com/bob)
- [commit 8b6a1f2](https://github.com/example/ai-hub/commit/8b6a1f2) `chore: 增加双架构交付清单` by [@carol](https://github.com/carol)

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
