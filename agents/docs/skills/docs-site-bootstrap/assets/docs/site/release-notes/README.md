---
title: Release Notes 编写规范
visibility: internal
doc_type: release
stage: dev
owners:
  - docs
related_code:
  - docs/site/release-notes
last_verified_version: unverified
---

# Release Notes 编写规范

本目录保存按版本维护的站内 Release Notes。版本页帮助实际读者了解能力和修复、技术与部署变化、升级动作，以及兼容性和恢复方式。

## 目标读者

根据宿主项目选择研发、测试、运维、交付或终端用户需要的细节与可见性。先回答本版本改变了什么，再说明读者需要执行的动作和判断条件。

## 内容与证据

| 主题 | 核对内容 |
| --- | --- |
| 功能与修复 | 已实现行为、使用变化、问题影响 |
| 架构与代码 | 组件边界、初始化、调试、可观测性 |
| 数据库 | schema、迁移顺序、数据兼容与恢复 |
| 部署 | 配置、环境差异、启动和验证命令 |
| 交付资产 | 镜像、Chart、安装包的名称、版本、位置 |
| 升级与风险 | 前提、操作、验证、已知限制、回滚方式 |

使用真实 issue、PR、提交、测试、配置和发布资产支持结论。将这些证据按能力或操作主题组织，保留有定位价值的来源链接。章节深度依据版本的实际变化与读者需要选择。

## 表达与术语

沿用宿主文档的主要语言。接口名、字段、代码标识、命令、路径、镜像名和版本号保持准确。内部重构如果影响运行、调试、升级或交付，同样作为对应主题的版本事实说明。

升级操作写明适用条件、文件或命令、执行顺序、成功信号和恢复方法。资产状态依据实际发布结果描述，清晰标识需要后续完成的内容。

## 文件与页面字段

版本页使用实际版本命名，例如 `v1.2.3.md`，并沿用宿主支持的预发布版本标识。页面采用站点 frontmatter：

```yaml
---
title: v1.2.3 发布说明
visibility: internal
doc_type: release
stage: release
owners:
  - docs
related_code:
  - src
last_verified_version: unverified
---
```

`visibility`、`owners` 和 `related_code` 根据实际页面设置。`last_verified_version` 记录有依据且已完成核对的版本；尚待核对时使用 `unverified`。

## 推荐结构

1. 版本、日期与重点变化。
2. 功能更新和缺陷修复。
3. 重要内部结构与代码变化。
4. 数据库及升级说明。
5. 部署配置和发布资产。
6. 兼容性、已知风险和恢复方式。
7. 版本对比与来源链接。

## 索引与版本数据

更新版本页时同步 `index.md` 及 `.meta/releases.json`，保留已有发布记录。`released` 数组记录发布版本，`latest` 指向最后一项，`verifiedDocs` 记录已验证页面及对应版本。站点脚本根据页面生成导航。

## 验证与交付

在站点根目录执行依赖安装和相关检查：

```bash
npm ci --ignore-scripts
npm run test:docs
npm run build:public
npm run build:internal
```

按页面的实际可见性检查构建、链接和版本信息。站内版本页可以作为 GitHub Release 的内容来源；标签与发布操作沿用用户已有授权，并回读实际发布结果。
