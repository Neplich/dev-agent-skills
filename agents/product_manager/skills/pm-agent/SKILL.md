---
name: pm-agent
description: PM Agent intelligent dispatcher - analyzes user intent and automatically selects and executes appropriate PM skills.
---

# PM Agent

PM Agent 智能入口，自动分析用户意图并选择执行合适的 PM skills。

## 使用场景

- 不确定该用哪个具体的 PM skill
- 需要执行多个 PM 任务的组合
- 希望 Agent 自动判断并执行完整的 PM 工作流

## 输入

用户的自然语言描述，例如：
- "我想做一个任务管理应用"
- "帮我分析竞品"
- "生成这个版本的 changelog"
- "查看 GitHub 项目状态"

## 输出

根据用户意图自动调用相应的 skills 并输出结果。

## 使用方式

```bash
/pm-agent "我想做一个任务管理应用"
/pm-agent "分析竞品并生成路线图"
/pm-agent "生成 v2.0 的发版说明"
```

---

详细实现指南请查看 `_internal/INSTRUCTIONS.md`
