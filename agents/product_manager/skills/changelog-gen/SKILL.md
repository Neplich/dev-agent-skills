---
name: changelog-gen
description: "根据标签可达提交和 PR 生成开发者变更记录，支持单版本、Unreleased 与历史整理。"
---

# 开发者变更记录

使用已合并 PR、可达提交和标签确定本次范围。带来源的历史导出也可使用，核对仓库、采集时间、标签范围与提交可达性。

| 范围 | 提交区间 | 默认文件 |
| --- | --- | --- |
| Unreleased | `LATEST_TAG..HEAD` | `docs/changelog/changelog-unreleased.md` |
| 已发布版本 | `PREV_TAG..TARGET_TAG` | `docs/changelog/changelog-v{VERSION}.md` |
| 首次标签 | 到 TARGET_TAG 的全部可达提交 | 对应版本文件 |

```bash
git log --format='%H%x09%s' PREV_TAG..TARGET_TAG
gh pr view NUMBER --json number,title,body,author,labels,state
```

从 squash subject 的 `(#NNN)` 或 merge subject 提取 PR 编号，再核对实际 PR。直接提交也保留并按变化含义分类。仓库尚未使用标签时，可按已知发布截止日获取 merged PR 并说明范围；结果超过 limit 时分页或拆分时间窗。

展示标题前去掉完整 Conventional Commit 前缀，包括 scope 和 breaking marker。按实际影响组织 Added、Changed、Deprecated、Removed、Fixed、Security，关键破坏性变化置前并说明迁移。相关 PR 合并为读者能理解的一条变化，保留来源链接。

评估 docs、test、ci、build 和 style 的实际影响：安装、公开能力、验证、发布或使用方式变化值得记录；日常格式、依赖例行更新与内部维护可合并概述。细节见 [前缀参考](references/cc-prefixes.md)。

读取已有版本文件，保留有效人工内容，整合当前变更。根 CHANGELOG.md 可作为版本索引。版本日期和链接来自真实记录，完成后核对范围、分类与链接。
