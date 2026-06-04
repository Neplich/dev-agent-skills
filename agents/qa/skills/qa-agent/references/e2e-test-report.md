# E2E Test Report Reference

This reference defines the required Markdown format for E2E summary reports
created by the main agent after subagent execution.

## Report Paths

Feature update reports:

```text
docs/qa/e2e/{一级功能}/{二级功能}/{三级功能}/_reports/{platform-version}/test-reports-{test-time}.md
```

Release full-run reports:

```text
docs/qa/e2e/_reports/{platform-version}/test-reports-{test-time}.md
```

`{test-time}` uses local test time in this format:

```text
YYYY-MM-DDTHH-mm-ss
```

Do not use `unknown` for `{platform-version}`. If the version is missing, the
test run is `blocked` until the user provides the platform version.

## Result Values

Allowed result values:

- `pass`
- `fail`
- `blocked`

Use `blocked` for missing version, unavailable environment, unresolved
credential reference, missing harness, missing PRD/TRD alignment, or missing
confirmed implementation plan.

## Required Format

```markdown
# E2E 测试汇总报告

## 基本信息
- 测试场景：feature-update / release
- 测试平台版本：
- 测试环境：开发环境本地 / 发版测试环境
- 测试时间：
- 测试范围：
- 整体结论：pass / fail / blocked

## 测试项汇总
| 测试项 | 功能目录 | TC | 执行入口 | 结果 | 证据 | Blocked 原因 | 风险 |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 结果说明
- 通过项：
- 失败项：
- 阻塞项：

## 风险与后续
- 风险：
- 后续动作：
```

## Field Rules

- `测试场景` must be `feature-update` or `release`.
- `测试平台版本` is required; missing version blocks the run.
- `测试环境` must name the actual local development or release test
  environment used.
- `测试范围` must identify the functional tree scope or `all active E2E TC`
  for release runs.
- `整体结论` is `fail` when any item fails, `blocked` when no reliable
  conclusion can be made, otherwise `pass`.
- Each table row must link or point to the corresponding `result.md`, evidence
  file, command output, screenshot, or blocked reason.
- Keep P0 fields in the order above. If a field has no value, write `N/A` or
  the concrete blocked reason.

The final conversation summary may quote the report result, but it must not
replace the report file.
