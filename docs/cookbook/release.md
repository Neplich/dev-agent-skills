# 手动发布

1. 确认发布范围与目标不可变 SemVer。
2. 把 `.claude-plugin/marketplace.json` 的 `metadata.version` 和
   `.kimi-plugin/plugin.json` 的 `version` 更新为相同、不带 `v` 前缀的版本。
3. 确认 `docs/changelog/changelog-v{version}.md` 存在，并被根 `CHANGELOG.md` 索引。
4. 运行生成契约、repository/doc/eval contract、eval artifact、安装与受影响测试；执行
   必需的 fresh eval，并汇总其持久化 comparison。
5. 创建 release PR 并等待全部 CI 通过；不要新增 Release CI 或绕过 tag ruleset。
6. PR 获批合并后，按手动清单创建带 `v` 前缀的 tag。
7. 通过 `pm-agent -> github-release-gen` 创建 GitHub Release draft；发布仍需维护者明确
   批准。

生产镜像若在范围内，使用不可变 SemVer tag，并在发布前验证同时包含
`linux/amd64` 与 `linux/arm64`。
