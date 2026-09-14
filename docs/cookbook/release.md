# 手动发布

发布使用维护者确认的范围与不可变 SemVer。仓库通过 PR 完成版本准备，取得明确授权后合并和发布。

1. 将 `.claude-plugin/marketplace.json` 的 `metadata.version`、六个 `agents/*/.claude-plugin/plugin.json` 的 `version` 和 `.kimi-plugin/plugin.json` 的 `version` 更新为相同的无 `v` 前缀版本。
2. 编写 `docs/changelog/changelog-v{version}.md`，并更新根 `CHANGELOG.md` 索引。记录可核实的能力变化、修复和升级操作。
3. 运行共享参考检查、仓库检查、文档检查、安装测试与受影响的行为测试。
4. 创建 release PR，确认三个 CI 检查通过，按维护者授权合并。
5. 为已核实的发布提交创建带 `v` 前缀的 SemVer tag。
6. 准备 GitHub Release 草稿，可直接使用 `github-release-gen`；核对版本、tag、正文和升级说明后，按维护者明确授权发布。

现有 tag ruleset 与手动发布方式共同管理发布权限。
