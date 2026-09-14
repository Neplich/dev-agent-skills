---
title: 操作手册模板
visibility: internal
doc_type: manual
stage: dev
owners:
  - docs
related_code:
  - docs/site
last_verified_version: unverified
---

# 操作手册模板

以真实运行界面说明可复现的用户操作。截图与手册页位于同一目录，使用 `./` 相对路径引用，图片和图注对应当前步骤。

使用脱敏测试数据，通过安全占位或遮盖保护 Token、密钥、个人信息和环境标识。截图保持自然宽高比。

<!-- docs-scaffold:start -->
```md
---
title: {{title}}
visibility: {{visibility}}
doc_type: {{doc_type}}
stage: {{stage}}
owners:
  - {{owner}}
related_code:
  - {{related_code}}
last_verified_version: unverified
---

# {{title}}

## 适用范围

- 适用角色：
- 前置条件：

## 操作步骤

1. 描述要执行的操作。
   - 可见界面说明：说明当前页面区域、控件和操作后的可见变化。
   - 截图与图注：用 Markdown 图片语法引用同目录截图，路径形如
     `./step-1-<描述>.png`，图注说明该图展示的界面区域与关键控件。

## 预期结果

说明目标角色完成步骤后可以观察到的结果。

## 注意事项与异常处理

说明操作限制、常见异常、用户可见反馈和可执行的处理方式。
```
<!-- docs-scaffold:end -->
