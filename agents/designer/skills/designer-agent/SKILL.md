---
name: designer-agent
description: Designer Agent intelligent dispatcher - analyzes design needs and executes appropriate design skills.
---

# Designer Agent

Designer Agent 智能入口，根据设计需求自动选择执行合适的设计 skills。

## 使用场景

- 需要设计 UI/UX 但不确定从哪开始
- 需要完整的设计系统
- 需要视觉风格定义

## 输入

用户的自然语言描述，例如：
- "设计用户登录界面"
- "创建设计系统"
- "定义视觉风格"

## 输出

根据设计需求自动调用相应的 skills 并输出设计文档。

## 使用方式

```bash
/designer-agent "设计用户登录流程"
/designer-agent "创建完整的设计系统"
```

---

详细实现指南请查看 `_internal/INSTRUCTIONS.md`
