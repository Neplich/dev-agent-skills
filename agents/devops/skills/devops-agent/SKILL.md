---
name: devops-agent
description: DevOps Agent intelligent dispatcher - analyzes deployment needs and executes appropriate DevOps skills.
---

# DevOps Agent

DevOps Agent 智能入口，根据部署需求自动选择执行合适的运维 skills。

## 使用场景

- 需要规划部署但不确定从哪开始
- 需要完整的 CI/CD 配置
- 需要审计环境配置

## 输入

用户的自然语言描述，例如：
- "规划部署方案"
- "配置 CI/CD"
- "审计环境配置"

## 输出

根据部署需求自动调用相应的 skills 并输出配置文档。

## 使用方式

```bash
/devops-agent "规划部署方案"
/devops-agent "配置完整的 CI/CD 流程"
```

---

详细实现指南请查看 `_internal/INSTRUCTIONS.md`
