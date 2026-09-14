# Mermaid 图示

根据用户描述或已验证的实现选择合适图形。节点名称准确，边说明关系，子图表达有实际意义的边界。

| 类型 | 用途 |
| --- | --- |
| flowchart | 操作、决策和控制流 |
| sequenceDiagram | 调用与交互时序 |
| erDiagram | 数据实体与关系 |
| C4Context / C4Container | 系统与容器关系 |
| gantt | 有依据的时间计划 |
| stateDiagram-v2 | 状态与事件转换 |
| classDiagram | 类型结构与关系 |
| pie | 有来源的分布 |

复杂主题按读者问题拆成几张图。核对语法、标签、方向、字段与真实关系，必要时渲染检查，使用 Mermaid 代码块或宿主支持的最终图形交付。

```mermaid
flowchart LR
  A[用户提交] --> B[校验输入]
  B --> C[执行任务]
  C --> D[返回结果]
```
