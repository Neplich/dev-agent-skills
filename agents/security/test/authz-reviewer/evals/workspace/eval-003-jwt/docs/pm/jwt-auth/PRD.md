---
feature: jwt-auth
feature_path: jwt-auth
parent_feature: N/A
feature_level: 1
version: 1.0.0
date: 2026-07-21
last_updated: 2026-07-21
---

# JWT 认证

## 当前状态

受保护 API 使用 JWT 识别用户，`role` 声明决定用户是否可访问管理端 API。

## 已确认信任边界

- 服务端必须验证令牌签名，并只接受配置允许的签名算法。
- 服务端必须校验 `exp`，过期令牌不得访问任何受保护 API。
- `sub` 和 `role` 只有在签名及有效期验证成功后才能用于身份和授权判断。
- 只有已验证为 `admin` 的令牌可访问 `/api/admin/*`。

审查范围包含令牌解析、签名与有效期校验以及管理端角色授权，不包含 OAuth 或 SSO 接入。

## 验收标准

- 篡改 payload、使用 `alg: none` 或过期令牌不能通过认证。
- 普通用户不能通过修改 `role` 声明访问管理端 API。
- 安全审查须给出可定位的代码证据、影响、严重度和修复及回归验证建议。
