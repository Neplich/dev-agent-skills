---
name: qa-agent
description: QA Agent intelligent dispatcher - analyzes testing needs and executes appropriate QA skills.
---

# QA Agent

QA Agent 智能入口，根据测试需求自动选择执行合适的测试 skills。

## 使用场景

- 需要执行测试但不确定用哪种测试方式
- 需要完整的测试流程
- 需要分析和报告 bug

## 输入

用户的自然语言描述，例如：
- "测试登录功能"
- "执行探索性测试"
- "分析这个 bug"

## 输出

根据测试需求自动调用相应的 skills 并输出测试报告。

## 使用方式

```bash
/qa-agent "测试用户登录功能"
/qa-agent "执行完整的测试流程"
```

---

详细实现指南请查看 `_internal/INSTRUCTIONS.md`
