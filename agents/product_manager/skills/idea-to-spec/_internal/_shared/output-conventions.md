# 正式规格格式

独立规格适合长期维护的需求、设计或决策。采用宿主仓库已有格式；使用本资料库默认格式时，以下字段帮助检索与版本比较。

```yaml
---
title: "文档标题"
type: PRD
status: Draft | In Review | Approved | Superseded | Deprecated
---
```

默认通用状态为 `Draft`、`In Review`、`Approved`、`Superseded`、`Deprecated`。状态描述文档成熟度；已实施事实写入当前行为及验证说明。各类正式规格使用相同状态枚举。

版本、作者、日期、`last_updated`、`generated_by` 与关联资料按维护需要添加。已有字段在实质更新时保持准确。版本号按实际内容变动维护：范围或结构重写为 major，实质内容更新为 minor，文字修正为 patch。历史由 Git 与发布记录承载，正文集中说明当前事实。

## 路径参考

| 内容 | 默认位置 |
| --- | --- |
| 产品规格与决定 | `docs/pm/{feature_path}/PRD.md`、`DECISIONS.md` |
| 技术规格与接口 | `docs/engineer/{feature_path}/TRD.md`、`API.md` |
| 架构决策 | `docs/engineer/{feature_path}/ADR-<NNN>.md` |
| 测试资料 | `docs/qa/{feature_path}/TEST_SUITE.md` |

需要功能索引时，`feature_path` 使用斜杠分隔的 lower kebab-case 段；`feature` 为末段，`parent_feature` 为父路径或 `N/A`，`feature_level` 为深度。PRD 的 `child_features` 可列出直接子功能。关联字段指向实际存在的资料，目录深度以维护价值决定。

交付时链接最终文件并说明验证结果。模板和 schema 按任务适用性裁剪；宿主工具读取的字段与格式保持一致。
