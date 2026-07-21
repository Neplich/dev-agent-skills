---
feature: dependency-inventory
feature_path: dependency-inventory
parent_feature: N/A
feature_level: 1
version: 1.0.0
date: 2026-07-21
last_updated: 2026-07-21
---

# 依赖清单与漏洞审计

## 当前状态

服务使用 Node.js 生产依赖处理用户请求。`package.json` 是当前版本事实来源，依赖版本在发布前保持固定。

## 目标

- 识别生产依赖及其固定版本。
- 对公开漏洞、过期版本和供应链风险给出证据与严重度。
- 为每项风险提供可执行的升级或临时缓解建议。

## 范围

- 审查 `package.json` 中的生产依赖。
- 重点检查直接处理对象路径和命令行参数的依赖。
- 输出审计结果，不在安全审查中直接更新依赖。

## 验收期望

- 审计引用具体包名、版本和风险类型。
- 高风险项说明受影响面与安全升级目标。
- 无法立即升级的项目说明短期缓解措施。
