---
feature: dependency-inventory
feature_path: dependency-inventory
parent_feature: N/A
feature_level: 1
version: 1.0.0
date: 2026-07-21
last_updated: 2026-07-21
---

# Python 依赖清单与漏洞审计

## 当前状态

Python 服务通过 `requirements.txt` 固定 HTTP、TLS 和模板渲染依赖，当前固定版本是发布候选的事实来源。

## 目标

- 识别固定依赖版本中的公开漏洞与过期风险。
- 说明风险影响的运行时入口。
- 给出兼容的安全升级目标或临时缓解建议。

## 范围

- 审查 `requirements.txt` 中的直接依赖。
- 覆盖 HTTP 请求、连接处理和模板渲染风险。
- 不在安全审查阶段直接修改版本固定。

## 验收期望

- 结论引用包名和精确版本。
- 漏洞风险说明影响与优先级。
- 升级建议区分直接升级与无法立即升级时的缓解措施。
