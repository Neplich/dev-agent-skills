# E2E Result Reports

Use a report when test results need to be shared or reused. A concise structure
is sufficient:

```markdown
# 测试结果

- 范围：
- 构建或提交：
- 环境与时间：
- 结论：

| 场景 | 预期 | 实际结果 | 执行入口 | 证据 |
| --- | --- | --- | --- | --- |

## 待处理项

记录失败的影响、未执行项的实际原因和后续动作。
```

Use `pass`, `fail`, and `blocked` for individual results. A blocked check names
its unavailable execution dependency. Build identity may be a release version,
commit SHA, or an accurate local working-tree description.

The overall conclusion describes the tested scope and any material coverage
gaps. Link commands, screenshots, or other sanitized evidence. Store durable
reports beside the project's existing test assets and retain distinct run
records for later comparison.
