# Delivery Handoff

```yaml
request_type: delivery
change_tier: standard
feature_path: notifications
related_issue: "#123"
source_documents:
  - docs/pm/notifications/PRD.md
completed_scope:
  - 新增通知状态标签格式化函数
  - 覆盖 active、read 和 archived 状态测试
changed_files:
  - src/notification-status.js
  - test/notification-status.test.js
verification:
  command: npm test
  result: PASS
delivery_action:
  - 创建符合仓库规范的功能分支
  - 使用 Conventional Commit 提交
  - push 并创建关联 Issue #123 的 PR
  - PR 正文包含摘要、PM 文档引用和测试状态
  - 创建 PR 后检查 CI
non_goals:
  - 合并 PR
  - 修改功能范围
```

本 fixture 是隔离的交付输入。Fresh validation 可以在 scratch copy 初始化本地 git 并评审外部 PR/CI 操作协议；不得把运行期 `.git`、transcript 或模拟 PR 产物提交到 canonical workspace。
