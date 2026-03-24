## 项目状态：anthropics/anthropic-sdk-python — 2026-03-20

### Milestones

暂无 milestone。该仓库当前没有设置任何 open milestone。

### Open Issues（75 个）

**按 Milestone 分组：**
- **无 Milestone**（75 个）：[#1258 Mid-stream SSE errors get `status_code=200` instead of the actual error code](https://github.com/anthropics/anthropic-sdk-python/issues/1258)、[#1257 MCP connectors non-functional on claude.ai](https://github.com/anthropics/anthropic-sdk-python/issues/1257)、[#1237 `web_search_20250209` dynamic filtering causes excessive `pause_turn`](https://github.com/anthropics/anthropic-sdk-python/issues/1237)、[#1215 Bug Report: Claude Pro weekly usage limits depleting drastically faster](https://github.com/anthropics/anthropic-sdk-python/issues/1215)、[#1212 Feature Request: Persistent context slot](https://github.com/anthropics/anthropic-sdk-python/issues/1212) 等

**需关注：**
- 🙋 无 assignee：72 个
- 😴 30 天未更新：52 个

### PR 队列

**待 Review — 人工贡献（72 个，按等待时间排序）：**

| # | 标题 | 作者 | 等待 | 标签 |
|---|------|------|------|------|
| [#543](https://github.com/anthropics/anthropic-sdk-python/pull/543) | feat(bedrock): support aws auth through role arn | @richzw | 639 天 | enhancement, bedrock, sdk |
| [#583](https://github.com/anthropics/anthropic-sdk-python/pull/583) | Feat: retry request on error 424 | @richzw | 617 天 | bedrock, sdk |
| [#1015](https://github.com/anthropics/anthropic-sdk-python/pull/1015) | [Fix] Add missing error mappings to Vertex AI client | @david-kunz-myriad | 216 天 | - |
| [#1043](https://github.com/anthropics/anthropic-sdk-python/pull/1043) | Support count tokens for bedrock client | @ogurash | 156 天 | - |
| [#1057](https://github.com/anthropics/anthropic-sdk-python/pull/1057) | fix(bedrock): preserve http_client in copy() and with_options() methods | @ljun20160606 | 139 天 | - |
| [#1066](https://github.com/anthropics/anthropic-sdk-python/pull/1066) | fix(security): prevent path traversal and add memory-efficient file handling | @padak | 128 天 | - |
| [#1067](https://github.com/anthropics/anthropic-sdk-python/pull/1067) | fix: resolve tool cache invalidation bug and bedrock HTTP/2 compatibility | @padak | 128 天 | - |
| [#1068](https://github.com/anthropics/anthropic-sdk-python/pull/1068) | fix(security): prevent presigned URL leak and exception data exfiltration | @padak | 128 天 | - |
| [#1070](https://github.com/anthropics/anthropic-sdk-python/pull/1070) | Accumulate extra pydantic fields from the sample event | @evanmiller-anthropic | 126 天 | - |
| [#1076](https://github.com/anthropics/anthropic-sdk-python/pull/1076) | feat: support special types for structured outputs | @karpetrosyan | 120 天 | - |

> 还有 62 个待 review PR 未列出，最老的是 #1080（117 天）

**已 Approved 待合并（2 个）：**
- [#1183 fix(structured outputs): improve error message for invalid `output_format` types](https://github.com/anthropics/anthropic-sdk-python/pull/1183) — @karpetrosyan
- [#1174 fix(tool runner): don't exit early on `pause_turn`](https://github.com/anthropics/anthropic-sdk-python/pull/1174) — @karpetrosyan

**Bot/自动化 PR（0 个）：**

当前无 bot PR 在队列中。

**草稿（4 个）：**
- [#1149 fix(bedrock): fix region inference when aws_profile is used](https://github.com/anthropics/anthropic-sdk-python/pull/1149) — @Ashutosh0x，56 天
- [#1148 feat(bedrock): add support for passing boto3.Session](https://github.com/anthropics/anthropic-sdk-python/pull/1148) — @Ashutosh0x，56 天
- [#1146 fix(streaming): handle raw dicts in accumulate_event to prevent AttributeError](https://github.com/anthropics/anthropic-sdk-python/pull/1146) — @Ashutosh0x，56 天
- [#1145 fix(streaming): handle out-of-order content blocks in accumulation](https://github.com/anthropics/anthropic-sdk-python/pull/1145) — @Ashutosh0x，56 天

**需作者跟进（Changes Requested，0 个）：**

无。

**近 14 天已合并（3 个）：**
- [#1249 release: 0.86.0](https://github.com/anthropics/anthropic-sdk-python/pull/1249)（stainless-app bot）
- [#1244 fix(client): AsyncAnthropic._make_status_error missing 529 and 413 cases](https://github.com/anthropics/anthropic-sdk-python/pull/1244)（@stephen）
- [#1209 release: 0.85.0](https://github.com/anthropics/anthropic-sdk-python/pull/1209)（stainless-app bot）

### 健康摘要
- 共 75 个 open issue，78 个 open PR
- 0 个 milestone 进行中，0 个逾期
- 近 14 天：合并 3 个 PR，关闭 5 个 issue
- ⚠️ 积压风险（等待 > 90 天的人工 PR）：15 个
