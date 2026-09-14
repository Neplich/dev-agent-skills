# 架构决策参考

根据任务和读者需要选择以下内容，沿用宿主实际工具读取的格式。

```yaml
---
title: "文档标题"
type: ADR
status: Draft
---
```

状态使用 `Draft`、`In Review`、`Approved`、`Superseded`、`Deprecated`。版本、作者、日期、feature_path 与关联资料按维护需要添加，见 [输出约定](../output-conventions.md)。

- 决定标题与稳定编号。
- 产生决定的技术和业务背景。
- 当前采用的方案与适用范围。
- 影响后续维护的取舍、后果和支持证据。
- 替代或废弃关系以及相关实现、规格和评测链接。

记录当前结论及必要理由。需要保留方案比较时，围绕真正影响决定的差异组织内容。`Superseded` 可配合 `superseded_by` 引用新决策。

正文以当前事实或明确目标为依据，关键声明链接可核对来源。
