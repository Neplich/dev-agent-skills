---
name: security-agent
description: Security Agent intelligent dispatcher - analyzes security needs and executes appropriate security skills.
---

# Security Agent

Security Agent 智能入口，根据安全需求自动选择执行合适的安全审查 skills。

## 使用场景

- 需要安全审查但不确定检查哪些方面
- 需要完整的安全审计
- 准备发布前的安全检查

## 输入

用户的自然语言描述，例如：
- "进行安全审查"
- "检查认证授权"
- "审计依赖安全"

## 输出

根据安全需求自动调用相应的 skills 并输出安全报告。

## 使用方式

```bash
/security-agent "进行完整的安全审查"
/security-agent "检查应用安全漏洞"
```

---

详细实现指南请查看 `_internal/INSTRUCTIONS.md`
