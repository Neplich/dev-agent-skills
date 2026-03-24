## 项目状态：anthropics/anthropic-sdk-python — 2026-03-20

### Milestones

暂无活跃 milestone（API 返回空列表）。

> 状态图例：✅ 完成 / 🟢 顺利 / 🟡 进行中 / 🔴 逾期 / ⚪ 无截止日期

---

### Open Issues（75 个）

**按 Milestone 分组：**
- **无 Milestone**（75 个）：所有 open issue 均未关联 milestone

**近期活跃（最近 14 天内更新）：**
- [#1258](https://github.com/anthropics/anthropic-sdk-python/issues/1258) Mid-stream SSE errors get `status_code=200` instead of the actual error code（3/19 更新）
- [#1257](https://github.com/anthropics/anthropic-sdk-python/issues/1257) MCP connectors non-functional on claude.ai（3/18 更新）
- [#1210](https://github.com/anthropics/anthropic-sdk-python/issues/1210) Bedrock beta.messages missing .stream() method（3/14 更新）
- [#1202](https://github.com/anthropics/anthropic-sdk-python/issues/1202) Use of `deepcopy_minimal` in `files.beta.upload` mutates dict in place（3/14 更新）
- [#1188](https://github.com/anthropics/anthropic-sdk-python/issues/1188) Structured outputs with Claude 4.6 on Vertex AI results in error（3/17 更新）
- [#1185](https://github.com/anthropics/anthropic-sdk-python/issues/1185) Structured outputs: "compiled grammar is too large" error（3/13 更新）

**按标签分布（open issues）：**
- `api` 标签：17 个
- `sdk` 标签：13 个
- `bedrock` 标签：10 个
- `enhancement` 标签：8 个
- `vertex` 标签：4 个
- `bug` 标签：3 个
- `documentation` 标签：2 个
- `question` 标签：1 个
- 无标签：约 30 个

**需关注：**
- 🙋 无 assignee：73 个（仅 #893 由 @kevinc13 负责、#671 由 @aaron-lerner 负责、#432 由 @RobertCraigie 负责）
- 😴 30 天未更新：52 个（最老的是 #432，创建于 2024-04-02）

---

### PR 队列

**待 Review（47 个，含已获批准）：**

*近期提交（3 月内）：*
- [#1263](https://github.com/anthropics/anthropic-sdk-python/pull/1263) fix: map SSE error types to correct HTTP status codes in streaming — @Jah-yee，1 天前
- [#1261](https://github.com/anthropics/anthropic-sdk-python/pull/1261) test(lib/tools): unit tests for tool_runner observability hooks — @AbdoKnbGit，1 天前
- [#1259](https://github.com/anthropics/anthropic-sdk-python/pull/1259) feat(lib/tools): add observability hooks to tool_runner — @AbdoKnbGit，1 天前
- [#1255](https://github.com/anthropics/anthropic-sdk-python/pull/1255) fix: remove spurious pass statement in signature_delta handler — @frankgoldfish，2 天前
- [#1253](https://github.com/anthropics/anthropic-sdk-python/pull/1253) docs: remove outdated single-content-block note from get_final_text — @frankgoldfish，2 天前
- [#1252](https://github.com/anthropics/anthropic-sdk-python/pull/1252) Add arithmetic calculator example using tool use — @omid-ant，3 天前
- [#1251](https://github.com/anthropics/anthropic-sdk-python/pull/1251) Fix: IndexError when streaming with multiple content blocks (#1192) — @Adityakk9031，3 天前
- [#1248](https://github.com/anthropics/anthropic-sdk-python/pull/1248) docs(examples): add module docstring to messages.py example — @vivekvar-dl，4 天前
- [#1247](https://github.com/anthropics/anthropic-sdk-python/pull/1247) perf: skip no-op recursive transform for types without PropertyInfo — @Scottcjn，4 天前
- [#1246](https://github.com/anthropics/anthropic-sdk-python/pull/1246) fix(bedrock): add missing stream() method to beta.messages — @passionworkeer，6 天前
- [#1245](https://github.com/anthropics/anthropic-sdk-python/pull/1245) fix: handle tuples in deepcopy_minimal to prevent dict mutation — @passionworkeer，6 天前
- [#1243](https://github.com/anthropics/anthropic-sdk-python/pull/1243) fix: pass aws_profile to boto3.Session() in _infer_region() — @alvinttang，6 天前
- [#1240](https://github.com/anthropics/anthropic-sdk-python/pull/1240) fix: handle empty text and malformed JSON in parse_text for thinking+tools — @gn00295120，8 天前
- [#1239](https://github.com/anthropics/anthropic-sdk-python/pull/1239) fix: defer async stream transforms for large payloads — @giulio-leone，9 天前
- [#1238](https://github.com/anthropics/anthropic-sdk-python/pull/1238) fix: resolve subscripted generics in _build_discriminated_union_meta (pydantic v1) — @ohxh，9 天前

*更多已有 Review_Required 的 PR（共 45 个待审核）：*
- [#1236](https://github.com/anthropics/anthropic-sdk-python/pull/1236) fix(bedrock): use boto3 Session region from aws_profile — @giulio-leone
- [#1235](https://github.com/anthropics/anthropic-sdk-python/pull/1235) fix(tools): continue tool_runner loop on pause_turn with server_tool_use blocks — @s-zx
- [#1234](https://github.com/anthropics/anthropic-sdk-python/pull/1234) Fix async compaction using unfiltered messages — @MaxwellCalkin
- [#1233](https://github.com/anthropics/anthropic-sdk-python/pull/1233) fix: add missing count_tokens to Bedrock beta.messages — @MaxwellCalkin
- [#1232](https://github.com/anthropics/anthropic-sdk-python/pull/1232) fix: raise ValueError when model is None in Bedrock client — @MaxwellCalkin
- [#1231](https://github.com/anthropics/anthropic-sdk-python/pull/1231) fix: use async_maybe_transform in AsyncMessages.stream() — @MaxwellCalkin
- [#1230](https://github.com/anthropics/anthropic-sdk-python/pull/1230) fix: add missing stream() method to Bedrock beta.messages — @MaxwellCalkin
- [#1229](https://github.com/anthropics/anthropic-sdk-python/pull/1229) fix: continue tool runner loop on server_tool_use with pause_turn — @MaxwellCalkin
- [#1228](https://github.com/anthropics/anthropic-sdk-python/pull/1228) fix: handle tuples in deepcopy_minimal to prevent in-place mutation — @MaxwellCalkin
- [#1226](https://github.com/anthropics/anthropic-sdk-python/pull/1226) fix: handle tuples in deepcopy_minimal — @giulio-leone
- [#1222](https://github.com/anthropics/anthropic-sdk-python/pull/1222) test: add unit tests for tool use example — @ozge-devops
- [#1221](https://github.com/anthropics/anthropic-sdk-python/pull/1221) add tool use example — @ozge-devops
- [#1220](https://github.com/anthropics/anthropic-sdk-python/pull/1220) docs: document 64-character limit for batch custom_id — @nielskaspers
- [#1219](https://github.com/anthropics/anthropic-sdk-python/pull/1219) feat(lib): add files_from_zip helper for skill uploads — @lyr408
- [#1218](https://github.com/anthropics/anthropic-sdk-python/pull/1218) fix: prevent dict mutation in deepcopy_minimal — @abdelhadi703
- [#1217](https://github.com/anthropics/anthropic-sdk-python/pull/1217) feat(exceptions): export missing HTTP status exceptions to public interface — @sbobryshev
- [#1213](https://github.com/anthropics/anthropic-sdk-python/pull/1213) fix: handle tuples in deepcopy_minimal to prevent mutation — @roli-lpci
- [#1207](https://github.com/anthropics/anthropic-sdk-python/pull/1207) fix(bedrock): use boto3 client for AWS region detection — @micheallam130
- [#1206](https://github.com/anthropics/anthropic-sdk-python/pull/1206) rewrite test_files: structured, parametrized, edge-case coverage — @tpbrown
- [#1203](https://github.com/anthropics/anthropic-sdk-python/pull/1203) feat: add double-buffer compaction for context window management — @marklubin
- [#1200](https://github.com/anthropics/anthropic-sdk-python/pull/1200) fix(streaming): preserve BetaCompactionBlock type during streaming accumulation — @bledden
- [#1199](https://github.com/anthropics/anthropic-sdk-python/pull/1199) fix(vertex): raise clear error when using structured outputs on Vertex AI — @bledden
- [#1196](https://github.com/anthropics/anthropic-sdk-python/pull/1196) Add CLAUDE.md documentation for AI assistants — @felippepestana
- [#1190](https://github.com/anthropics/anthropic-sdk-python/pull/1190) fix: correct typo 'overriden' → 'overridden' in README — @slegarraga
- [#1178](https://github.com/anthropics/anthropic-sdk-python/pull/1178) Adding support for enums in transform_schema — @Natooz
- [#1167](https://github.com/anthropics/anthropic-sdk-python/pull/1167) fix(models): correctly unwrap Annotated types for RawMessageStreamEvent — @Ashutosh0x
- [#1165](https://github.com/anthropics/anthropic-sdk-python/pull/1165) fix: handle None by_alias in model_dump for FastAPI contexts — @thecaptain789
- [#1153](https://github.com/anthropics/anthropic-sdk-python/pull/1153) fix(streaming): safely handle dicts in accumulate_event — @Ashutosh0x
- [#1151](https://github.com/anthropics/anthropic-sdk-python/pull/1151) fix(compaction): also filter out server_tool_use blocks before compaction — @stephaniepang97

*已获 APPROVED，等待合并：*
- [#1183](https://github.com/anthropics/anthropic-sdk-python/pull/1183) fix(structured outputs): improve error message for invalid output_format types — @karpetrosyan ✅ 已批准
- [#1174](https://github.com/anthropics/anthropic-sdk-python/pull/1174) fix(tool runner): don't exit early on pause_turn — @karpetrosyan ✅ 已批准

**草稿（4 个）：**
- [#1149](https://github.com/anthropics/anthropic-sdk-python/pull/1149) fix(bedrock): fix region inference when aws_profile is used — @Ashutosh0x
- [#1148](https://github.com/anthropics/anthropic-sdk-python/pull/1148) feat(bedrock): add support for passing boto3.Session — @Ashutosh0x
- [#1146](https://github.com/anthropics/anthropic-sdk-python/pull/1146) fix(streaming): handle raw dicts in accumulate_event — @Ashutosh0x
- [#1145](https://github.com/anthropics/anthropic-sdk-python/pull/1145) fix(streaming): handle out-of-order content blocks in accumulation — @Ashutosh0x

**近 14 天已合并（3 个）：**
- [#1249](https://github.com/anthropics/anthropic-sdk-python/pull/1249) release: 0.86.0（2026-03-18 by stainless-app）
- [#1244](https://github.com/anthropics/anthropic-sdk-python/pull/1244) fix(client): AsyncAnthropic._make_status_error missing 529 and 413 cases（2026-03-16 by @stephen）
- [#1209](https://github.com/anthropics/anthropic-sdk-python/pull/1209) release: 0.85.0（2026-03-16 by stainless-app）

---

### 健康摘要

- 共 **75 个** open issue，**51 个** open PR（含 4 个草稿）
- **0 个** milestone 进行中（暂无 milestone 设置）
- 近 14 天：合并 **3 个** PR（含 2 个 release），关闭 **5 个** issue
- **PR 队列积压严重**：45 个 PR 等待 review，多个 PR 修复同一问题（deepcopy_minimal 的 tuple 处理至少有 5 个 PR 同时在等审核）
- **2 个已批准 PR** 等待维护者合并（#1183、#1174）
- Issue 维护薄弱：73/75 个 issue 无 assignee，52 个 issue 超过 30 天未更新
- 最高频问题领域：Bedrock 集成（stream 方法缺失、region 检测）、streaming 稳定性、deepcopy_minimal 变异 bug
