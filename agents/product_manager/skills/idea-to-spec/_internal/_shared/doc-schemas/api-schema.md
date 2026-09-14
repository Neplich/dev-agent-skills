# 接口说明参考

根据任务和读者需要选择以下内容，沿用宿主实际工具读取的格式。

```yaml
---
title: "文档标题"
type: API
status: Draft
---
```

状态使用 `Draft`、`In Review`、`Approved`、`Superseded`、`Deprecated`。版本、作者、日期、feature_path 与关联资料按维护需要添加，见 [输出约定](../output-conventions.md)。

- 服务范围、基础地址、版本与鉴权方式。
- 每个接口的方法、路径、职责和权限。
- 路径、查询、头部与请求体的类型、必填性和校验。
- 响应模型、状态码、业务错误和恢复条件。
- 分页、排序、限流、幂等与兼容性。
- 可执行请求示例及对应响应。
- 路由、schema、handler 与 contract tests 证据。

正文以当前事实或明确目标为依据，关键声明链接可核对来源。
