---
feature: auth-model
feature_path: auth-model
parent_feature: N/A
feature_level: 1
version: 1.0.0
date: 2026-07-20
last_updated: 2026-07-20
---

# 登录与权限模型

## 问题与目标

当前多租户场景下的角色边界不够清晰，敏感操作的鉴权校验分散，存在 admin 跨越租户或平台权限边界的越权风险。本次重构的目标是统一登录会话与权限校验规则，在上线前确认认证、授权和依赖供应链风险均有明确证据。

成功标准：

- admin 越权路径为零。
- 所有敏感路由统一执行会话与角色校验。
- 上线前完成依赖漏洞扫描并留存结果。

## 范围

### MVP

- 重构登录会话生命周期与请求校验流程。
- 收敛 guest、member、admin、platform-ops 的角色权限矩阵。
- 为敏感路由统一挂载鉴权中间件。

### 非目标

- SSO 接入。
- 密码策略调整。

## 认证流程

1. 用户使用用户名和密码登录。
2. 服务端验证身份后颁发 session token。
3. 每次请求校验 session 有效性与角色 claim。
4. 敏感操作在进入业务处理前执行二次权限校验。

## 角色权限矩阵

| 角色 | 允许能力 | 禁止边界 |
| --- | --- | --- |
| guest | 访问公开内容与登录入口 | 不得访问成员、管理或平台配置能力 |
| member | 访问所属租户的成员功能 | 不得执行 admin 或 platform-ops 操作 |
| admin | 管理所属租户成员并读取所属租户审计日志 | 不得跨租户访问，也不得使用 platform-ops 的平台配置能力 |
| platform-ops | 维护平台级配置与平台运营能力 | 仅限受控的平台运维身份使用 |

## 敏感路由

- `POST /admin/members`：仅 admin 可管理所属租户成员。
- `GET /admin/audit-logs`：仅 admin 可读取所属租户审计日志。
- `POST /platform/config`：仅 platform-ops 可访问，admin 必须被拒绝。

## 依赖

- `express`：作为统一鉴权中间件的挂载点；上线前必须确认当前版本是否存在已知 CVE。

## 验收测试期望

- admin 访问 `POST /platform/config` 必须被拒绝，并留存测试证据。
- 过期 session 访问任一敏感路由必须被拒绝，并留存测试证据。
- 上线前完成依赖漏洞扫描并留存扫描证据。

## 决策锁定

- 所有敏感路由使用统一鉴权中间件，不在各 handler 中散落权限校验。
- session 由服务端管理，本次重构不引入 JWT。
