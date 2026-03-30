---
name: engineer-agent
description: Engineer Agent intelligent dispatcher - analyzes context and automatically selects appropriate engineering skills.
---

# Engineer Agent

Engineer Agent 智能入口，根据项目状态和用户需求自动选择执行合适的工程 skills。

## 使用场景

- 不确定该用哪个具体的工程 skill
- 需要完整的开发流程（分析→实现→测试→交付）
- 希望 Agent 自动判断当前阶段并执行相应任务

## 输入

用户的自然语言描述，例如：
- "实现用户登录功能"
- "分析这个项目的技术栈"
- "修复这个 bug"
- "创建 PR 并交付"

## 输出

根据项目状态和用户意图自动调用相应的 skills 并输出结果。

## 使用方式

```bash
/engineer-agent "实现用户登录功能"
/engineer-agent "分析项目结构"
/engineer-agent "修复登录失败的 bug"
```

---

详细实现指南请查看 `_internal/INSTRUCTIONS.md`
