# 测试规格参考

根据任务和读者需要选择以下内容，沿用宿主实际工具读取的格式。

```yaml
---
title: "文档标题"
type: TEST_SPEC
status: Draft
---
```

状态使用 `Draft`、`In Review`、`Approved`、`Superseded`、`Deprecated`。版本、作者、日期、feature_path 与关联资料按维护需要添加，见 [输出约定](../output-conventions.md)。

- 被测行为、范围和验收目标。
- 单元、集成、E2E 或性能等适用测试层级。
- 测试环境、角色、账号、数据、初始化和清理。
- 每个用例的稳定 ID、前置状态、输入步骤与可观察结果。
- 正常、异常、边界、权限、安全和可靠性场景。
- 要求到用例的覆盖关系、烟测与回归范围。
- 实际执行结果、失败证据和覆盖缺口。

持久 E2E 资产沿用宿主约定。需要独立用例文件时，一个文件承载一个稳定 ID 的场景，可使用 `cases/TC-001-login-success.md`。`FLOW_INDEX.md` 可记录可复用入口、harness、fixtures 和探索结果，`TEST_SUITE.md` 可作为用例索引。

正文以当前事实或明确目标为依据，关键声明链接可核对来源。
