# Microsoft VS Code 项目路线图

> 基于 GitHub 仓库 [microsoft/vscode](https://github.com/microsoft/vscode) 数据自动生成
> 生成日期：2026-03-20

---

## 📊 总览

| 阶段 | 里程碑 | 状态 | 进度 |
|------|--------|------|------|
| ✅ 已完成 | 1.112.0 | 已关闭 | █████████████████████ 100% (588/588) |
| 🔄 当前迭代 | 1.113.0 | 进行中 | █████████░░░░░░░░░░░ 52% (306/588) |
| 📋 下一迭代 | 1.114.0 | 规划中 | ░░░░░░░░░░░░░░░░░░░░ 0% (0/7) |
| 📌 待定 | On Deck | 开放 | — (998 个开放议题) |
| 📁 积压 | Backlog | 开放 | — (5,525 个开放议题) |
| 💡 候选 | Backlog Candidates | 开放 | — (161 个开放议题) |

---

## ✅ 已完成阶段 — 近期发布

### [1.112.0](https://github.com/microsoft/vscode/milestone/370) — 截止 2026-03-17

**进度：██████████████████████ 100%** — 588 个议题已关闭

近期完成的重点工作：

| # | 标题 | 分类 |
|---|------|------|
| [#302477](https://github.com/microsoft/vscode/issues/302477) | Fetch Telemetry is collected in stable | bug, candidate |
| [#302408](https://github.com/microsoft/vscode/issues/302408) | Debounce and getting lang ctx should respect cancellation token | bug, NES |
| [#302330](https://github.com/microsoft/vscode/issues/302330) | Flickering in editor decorations while debugging | bug |
| [#302182](https://github.com/microsoft/vscode/issues/302182) | bypass approvals skips confirmation in CLI | insiders-released |
| [#302158](https://github.com/microsoft/vscode/issues/302158) | no other options in worktree CLI except `bypass approvals` | candidate |
| [#302128](https://github.com/microsoft/vscode/issues/302128) | Handle NES patch-based model: Response contained no choices | bug, NES |
| [#302113](https://github.com/microsoft/vscode/issues/302113) | Restart to update | bug, install-update |

### 更早版本

| 里程碑 | 关闭日期 | 已关闭议题 | 链接 |
|--------|----------|-----------|------|
| [1.111.0](https://github.com/microsoft/vscode/milestone/376) | 2026-03-06 | 478 | [查看](https://github.com/microsoft/vscode/milestone/376) |
| [February 2026](https://github.com/microsoft/vscode/milestone/357) | 2026-02-27 | 2,068 | [查看](https://github.com/microsoft/vscode/milestone/357) |
| [January 2026](https://github.com/microsoft/vscode/milestone/361) | 2026-01-30 | 2,044 | [查看](https://github.com/microsoft/vscode/milestone/361) |
| [December 2025](https://github.com/microsoft/vscode/milestone/351) | 2026-01-09 | 1,140 | [查看](https://github.com/microsoft/vscode/milestone/351) |
| [November 2025](https://github.com/microsoft/vscode/milestone/338) | 2025-12-05 | 1,680 | [查看](https://github.com/microsoft/vscode/milestone/338) |

---

## 🔄 当前迭代 — 1.113.0

**[里程碑链接](https://github.com/microsoft/vscode/milestone/395)** | 截止日期：2026-03-23 | **进度：52%** (306 已关闭 / 282 开放)

### 🤖 Copilot / AI 智能助手

| # | 标题 | 状态 | 标签 |
|---|------|------|------|
| [#302814](https://github.com/microsoft/vscode/issues/302814) | Chat hangs when Copilot chat is installed without being signed in | 🔴 开放 | bug, important |
| [#302762](https://github.com/microsoft/vscode/issues/302762) | Copilot CLI: When using prompt files, attachments are not included | 🔴 开放 | bug, copilot-cli-agent |
| [#302659](https://github.com/microsoft/vscode/issues/302659) | Applying Changes fail | 🔴 开放 | bug, copilot-cli-agent |
| [#302658](https://github.com/microsoft/vscode/issues/302658) | Can't easily open a file in a worktree not modified by the agent | 🔴 开放 | feature-request, copilot-cli-agent |
| [#302656](https://github.com/microsoft/vscode/issues/302656) | Simpler way to open terminal associated with Session | 🔴 开放 | copilot-cli-agent |
| [#302654](https://github.com/microsoft/vscode/issues/302654) | Can't run multiple sessions on the same worktree | 🔴 开放 | feature-request, copilot-cli-agent |
| [#302622](https://github.com/microsoft/vscode/issues/302622) | Sub agents tool calls not grouped correctly | 🔴 开放 | bug, copilot-cli-agent |
| [#302551](https://github.com/microsoft/vscode/issues/302551) | Worktree sessions seem to sometimes stop updating | 🔴 开放 | bug, important, copilot-cli-agent |
| [#302257](https://github.com/microsoft/vscode/issues/302257) | Disabling Autopilot setting should deselect the mode | 🔴 开放 | bug |
| [#302187](https://github.com/microsoft/vscode/issues/302187) | Can't steer copilot cli requests after reloading an active session | 🔴 开放 | bug, copilot-cli-agent |
| [#302164](https://github.com/microsoft/vscode/issues/302164) | Invalid tip shown on Claude | 🔴 开放 | bug, chat-tips |
| [#302153](https://github.com/microsoft/vscode/issues/302153) | Autopilot mode -> task_completed tool call is shown in chat | 🔴 开放 | ux |
| [#302089](https://github.com/microsoft/vscode/issues/302089) | Context Auto Compact is not always triggered | 🔴 开放 | bug |
| [#301355](https://github.com/microsoft/vscode/issues/301355) | Steering messages disappear from Copilot CLI | 🔴 开放 | bug, copilot-cli-agent |
| [#300531](https://github.com/microsoft/vscode/issues/300531) | Allow to "Continue In" Claude Agent | 🔴 开放 | feature-request, claude-agent |

### 🪟 Sessions / 会话窗口

| # | 标题 | 状态 | 标签 |
|---|------|------|------|
| [#303076](https://github.com/microsoft/vscode/issues/303076) | Sessions: title is not good for cloud sessions | 🔴 开放 | bug, chat-agents-window |
| [#302665](https://github.com/microsoft/vscode/issues/302665) | Sessions: New session initial send just opens up latest session | 🔴 开放 | bug, chat-agents-window |
| [#302453](https://github.com/microsoft/vscode/issues/302453) | The "Other" group should be at the bottom when grouped by repo | ✅ 已关闭 | bug, chat-agents-view |
| [#303022](https://github.com/microsoft/vscode/issues/303022) | Different history and options depending on how launched | ✅ 已关闭 | bug, chat-agents-window |
| [#303014](https://github.com/microsoft/vscode/issues/303014) | Consider making `Group by Repository` the default state | ✅ 已关闭 | feature-request, chat-agents-window |
| [#301503](https://github.com/microsoft/vscode/issues/301503) | Title bar is sized in a way that chat is cropped weirdly | 🔴 开放 | ux, chat-agents-window |

### 🔌 MCP / 工具 / 插件

| # | 标题 | 状态 | 标签 |
|---|------|------|------|
| [#302394](https://github.com/microsoft/vscode/issues/302394) | MCP Streamable HTTP client does not send cookies | 🔴 开放 | bug, mcp |
| [#302393](https://github.com/microsoft/vscode/issues/302393) | Allow tool confirmations for specific arguments | 🔴 开放 | feature-request, api |
| [#302514](https://github.com/microsoft/vscode/issues/302514) | How to maintain info that a customization is from an installed plugin | 🔴 开放 | feature-request, agent-plugins |
| [#302152](https://github.com/microsoft/vscode/issues/302152) | Read Copilot CLI user-installed plugins from `~/.copilot/installed-plugins/` | 🔴 开放 | feature-request, agent-plugins |
| [#301690](https://github.com/microsoft/vscode/issues/301690) | Tool conflict between MCP and built-in tools | 🔴 开放 | bug, mcp |
| [#302181](https://github.com/microsoft/vscode/issues/302181) | Skills duplication when 'Agent Skills Location' overlaps | 🔴 开放 | bug |

### 🖥️ 终端 / 编辑器 / UI

| # | 标题 | 状态 | 标签 |
|---|------|------|------|
| [#303202](https://github.com/microsoft/vscode/issues/303202) | Automatic entering after the latest update | 🔴 开放 | accessibility, regression |
| [#303118](https://github.com/microsoft/vscode/issues/303118) | ⇧⌘W is hijacked by terminal when using `fish` | 🔴 开放 | bug, terminal-input |
| [#302406](https://github.com/microsoft/vscode/issues/302406) | editor.emmet.action.toggleComment | 🔴 开放 | bug, emmet |
| [#302275](https://github.com/microsoft/vscode/issues/302275) | Nested CLI linking not working | 🔴 开放 | bug, terminal-links |
| [#302212](https://github.com/microsoft/vscode/issues/302212) | Other Models experience not a delightful screen reader experience | 🔴 开放 | bug, accessibility |
| [#301645](https://github.com/microsoft/vscode/issues/301645) | Built-in Profile template "Python" fails to create | 🔴 开放 | bug |
| [#301564](https://github.com/microsoft/vscode/issues/301564) | Accessible View should include file paths for file references | 🔴 开放 | bug, accessibility |
| [#301471](https://github.com/microsoft/vscode/issues/301471) | Incorrect IInspectValue property used in scope detection | ✅ 已关闭 | bug, terminal |
| [#302690](https://github.com/microsoft/vscode/issues/302690) | ExtensionEditor can not show dependencies | 🔴 开放 | bug, extensions |

### 近期合并的 Pull Requests（精选）

| # | 标题 |
|---|------|
| [#303267](https://github.com/microsoft/vscode/pull/303267) | Sessions: Consider making `Group by Repository` the default state |
| [#303263](https://github.com/microsoft/vscode/pull/303263) | Enhance URL glob matching to enforce subdomain wildcard matching |
| [#303244](https://github.com/microsoft/vscode/pull/303244) | chat - prevent race conditions in `loadSession` |
| [#303242](https://github.com/microsoft/vscode/pull/303242) | Fix infinite enter for pwsh5 when screen reader is enabled |
| [#303228](https://github.com/microsoft/vscode/pull/303228) | sessions - allow to collapse section headers |
| [#303213](https://github.com/microsoft/vscode/pull/303213) | fix light theme contrast issue in questions feature |
| [#303180](https://github.com/microsoft/vscode/pull/303180) | Enhance modal editor and improve empty state styling |
| [#303172](https://github.com/microsoft/vscode/pull/303172) | Adding chat debug view in Sessions window |
| [#303161](https://github.com/microsoft/vscode/pull/303161) | Add inlineChat.askInChat setting to toggle Ask in Chat vs Inline Chat |
| [#303043](https://github.com/microsoft/vscode/pull/303043) | new thinking design |
| [#303039](https://github.com/microsoft/vscode/pull/303039) | Add disable/enable toggle for built-in skills in AI Customization editor |
| [#303036](https://github.com/microsoft/vscode/pull/303036) | customizations: harness filtering for Claude, agent gating |
| [#303028](https://github.com/microsoft/vscode/pull/303028) | feat: enable image carousel viewer for chat image attachments |
| [#302944](https://github.com/microsoft/vscode/pull/302944) | Support for nested subagents |
| [#302816](https://github.com/microsoft/vscode/pull/302816) | feat: native macOS service provider for 'Open with Code' in Finder |

---

## 📋 下一迭代 — 1.114.0

**[里程碑链接](https://github.com/microsoft/vscode/milestone/399)** | 截止日期：2026-03-30 | **进度：0%** (0 已关闭 / 7 开放)

| # | 标题 | 标签 |
|---|------|------|
| [#302884](https://github.com/microsoft/vscode/pull/302884) | Fix terminal tool output truncation | — |
| [#302215](https://github.com/microsoft/vscode/issues/302215) | /troubleshoot relies on independent log flush | — |
| [#302181](https://github.com/microsoft/vscode/issues/302181) | Skills duplication when 'Agent Skills Location' overlaps | bug |
| [#302052](https://github.com/microsoft/vscode/issues/302052) | Support Gemini 3.1 Pro to BYOK Models in GitHub Copilot | — |
| [#301758](https://github.com/microsoft/vscode/issues/301758) | Chats in Editor are not able get Debug Logs | bug |
| [#301690](https://github.com/microsoft/vscode/issues/301690) | Tool conflict between MCP and built-in tools | bug, mcp |
| [#301538](https://github.com/microsoft/vscode/issues/301538) | chat debug event log: repeated entries | bug |

---

## 📌 待定阶段 — On Deck

**[里程碑链接](https://github.com/microsoft/vscode/milestone/27)** | 998 个开放议题 | 1,056 个已关闭

> 已分配到 On Deck 的议题正在考虑纳入即将到来的迭代。

### 重点议题（精选）

#### 🐛 缺陷修复

| # | 标题 | 标签 |
|---|------|------|
| [#302206](https://github.com/microsoft/vscode/issues/302206) | Copilot cli doesn't show `needs input` status | copilot-cli-agent |
| [#302205](https://github.com/microsoft/vscode/issues/302205) | Session hover card overlaps with window controls | copilot-cli-agent |
| [#302201](https://github.com/microsoft/vscode/issues/302201) | Copilot cli sessions seem to get stuck | copilot-cli-agent |
| [#302199](https://github.com/microsoft/vscode/issues/302199) | Chat content flashes/scrolls oddly when first sending a steering message | copilot-cli-agent |
| [#302185](https://github.com/microsoft/vscode/issues/302185) | `Stop and send` doesn't work with copilot cli | copilot-cli-agent |
| [#302004](https://github.com/microsoft/vscode/issues/302004) | Failed to apply changes error after applied succeeded | copilot-cli-agent |
| [#301984](https://github.com/microsoft/vscode/issues/301984) | Image carousel shows UUID on hover | bug |
| [#300770](https://github.com/microsoft/vscode/issues/300770) | Agent Sessions Tree is extremely inefficient | important |
| [#300749](https://github.com/microsoft/vscode/issues/300749) | Model picker should support fuzzy searching | model-picker |
| [#300625](https://github.com/microsoft/vscode/issues/300625) | Input/output confirmation cuts off text | chat-tools |
| [#297308](https://github.com/microsoft/vscode/issues/297308) | Chat: It's easy to accidentally enable editing all sensitive files | important, security |
| [#296741](https://github.com/microsoft/vscode/issues/296741) | Context widget frequently breaks | chat |

#### ✨ 功能请求

| # | 标题 | 标签 |
|---|------|------|
| [#302238](https://github.com/microsoft/vscode/issues/302238) | Modal: allow viewlets to show to the side | workbench-modal-editor |
| [#300235](https://github.com/microsoft/vscode/issues/300235) | Surface reasoning effort controls in chat UI | model-picker |
| [#300149](https://github.com/microsoft/vscode/issues/300149) | Integrated browser: Enable Http Basic Authentication | browser-integration |
| [#299787](https://github.com/microsoft/vscode/issues/299787) | Show `title` from `serverInfo` for MCP Servers | mcp |
| [#299521](https://github.com/microsoft/vscode/issues/299521) | Permissions Access in Integrated Browser | browser-integration |
| [#298207](https://github.com/microsoft/vscode/issues/298207) | Copilot chat AwaitingInput Hook | chat-hooks |
| [#298063](https://github.com/microsoft/vscode/issues/298063) | Remove visibility as a concept in the new model picker | model-picker |
| [#294247](https://github.com/microsoft/vscode/issues/294247) | Support OSC 99 notifications | terminal |
| [#293405](https://github.com/microsoft/vscode/issues/293405) | Modernizing VS Code Default Themes (2026 Refresh) | 2026-themes |
| [#293007](https://github.com/microsoft/vscode/issues/293007) | Configurable location for MCP configuration files | mcp |
| [#292445](https://github.com/microsoft/vscode/issues/292445) | Electron 40 Update | electron |

#### 🔧 技术债务 / 工程

| # | 标题 | 标签 |
|---|------|------|
| [#299127](https://github.com/microsoft/vscode/issues/299127) | Add a warning when there's no Show Details | debt, chat-setup |
| [#299010](https://github.com/microsoft/vscode/issues/299010) | Adopt SDK listSessions() / getSessionMessages() APIs | debt, claude-agent |
| [#298762](https://github.com/microsoft/vscode/issues/298762) | Remove simple browser extension | debt, browser-integration |
| [#293200](https://github.com/microsoft/vscode/issues/293200) | Leaks! | freeze-slow-crash-leak |
| [#291904](https://github.com/microsoft/vscode/issues/291904) | Create `IAgentSessionsFilterService` and refactor | debt |
| [#291190](https://github.com/microsoft/vscode/issues/291190) | Chat code still often falls back to `ChatMode.Ask` | debt |

---

## 💡 候选阶段 — Backlog Candidates

**[里程碑链接](https://github.com/microsoft/vscode/milestone/107)** | 161 个开放议题 | 6,338 个已关闭

> 尚未被接受进入 Backlog 的工作项。等待社区投票和反馈。

### 热门候选议题（精选）

| # | 标题 | 标签 |
|---|------|------|
| [#303085](https://github.com/microsoft/vscode/issues/303085) | Integrated Browser: Add configurable User-Agent setting | browser-integration |
| [#302930](https://github.com/microsoft/vscode/issues/302930) | Open telemetry should include some PII data in GitHub Copilot | feature-request |
| [#302817](https://github.com/microsoft/vscode/issues/302817) | Plan More -> Add option to "Start implementation in new chat" | feature-request |
| [#302329](https://github.com/microsoft/vscode/issues/302329) | Allow sending images without text in Copilot Chat | feature-request |
| [#302056](https://github.com/microsoft/vscode/issues/302056) | Agent Teams: multi-agent collaboration for complex tasks | chat-agent |
| [#301655](https://github.com/microsoft/vscode/issues/301655) | Auto-mode Selection: Let Copilot Intelligently Choose Modes | feature-request |
| [#301588](https://github.com/microsoft/vscode/issues/301588) | Allow extensions to use variable line height | editor-core |
| [#300886](https://github.com/microsoft/vscode/issues/300886) | Add a suggestions pane | suggest |
| [#299961](https://github.com/microsoft/vscode/issues/299961) | Drag-and-drop to reorder code blocks in Outline view | outline |
| [#299944](https://github.com/microsoft/vscode/issues/299944) | Native "Voice-Only" Mode for VS Code Copilot Chat | accessibility |
| [#299869](https://github.com/microsoft/vscode/issues/299869) | Floating Dialog Panel Mode | layout |
| [#298757](https://github.com/microsoft/vscode/issues/298757) | Multi-Agent Standardized Communication Protocol | chat-subagents |
| [#297666](https://github.com/microsoft/vscode/issues/297666) | Add Computer Use / Desktop Automation Support to Copilot | copilot-cli-agent |
| [#297140](https://github.com/microsoft/vscode/issues/297140) | Allow Copilot Chat extension to work on VS Code Web | web, chat |

---

## 📁 积压阶段 — Backlog

**[里程碑链接](https://github.com/microsoft/vscode/milestone/8)** | 5,525 个开放议题 | 10,758 个已关闭

> 已接受但尚未安排到具体版本的工作项。

### 按类型分布

| 类型 | 数量 | 占比 |
|------|------|------|
| 🐛 Bug（缺陷） | 1,948 | 35.3% |
| ✨ Feature Request（功能请求） | 3,034 | 54.9% |
| 🔧 Debt（技术债务） | 159 | 2.9% |
| ♿ Accessibility（无障碍） | 123 | 2.2% |
| 🏗️ Engineering（工程） | 34 | 0.6% |
| 💬 Under Discussion（讨论中） | 231 | 4.2% |

### 按功能区域分布

| 区域 | 开放议题数 | 链接 |
|------|-----------|------|
| 🔍 Debug（调试） | 184 | [查看](https://github.com/microsoft/vscode/issues?q=is%3Aopen+milestone%3ABacklog+label%3Adebug) |
| 📝 SCM（源代码管理） | 153 | [查看](https://github.com/microsoft/vscode/issues?q=is%3Aopen+milestone%3ABacklog+label%3Ascm) |
| ✏️ Editor Core（编辑器核心） | 138 | [查看](https://github.com/microsoft/vscode/issues?q=is%3Aopen+milestone%3ABacklog+label%3Aeditor-core) |
| 🧩 Extensions（扩展） | 66 | [查看](https://github.com/microsoft/vscode/issues?q=is%3Aopen+milestone%3ABacklog+label%3Aextensions) |
| 📑 Editors（编辑器组） | 33 | [查看](https://github.com/microsoft/vscode/issues?q=is%3Aopen+milestone%3ABacklog+label%3Aworkbench-editors) |
| 💻 Terminal（终端） | 12 | [查看](https://github.com/microsoft/vscode/issues?q=is%3Aopen+milestone%3ABacklog+label%3Aterminal) |

---

## 🔥 活跃 Pull Requests

> 当前仓库中最近更新的开放 PR（精选）

| # | 标题 | 作者 |
|---|------|------|
| [#303280](https://github.com/microsoft/vscode/pull/303280) | Add block-no-verify PreToolUse hook to .claude/settings.json | tupe12334 |
| [#303277](https://github.com/microsoft/vscode/pull/303277) | Bug fix: Fix skill load regression | vijayupadya |
| [#303270](https://github.com/microsoft/vscode/pull/303270) | plugins: fix a bunch of issues in customizations | connor4312 |
| [#303266](https://github.com/microsoft/vscode/pull/303266) | sessions - allow to create new chat per repository | bpasero |
| [#303261](https://github.com/microsoft/vscode/pull/303261) | Sessions: Refactor Changes view title handling | mrleemurray |
| [#303258](https://github.com/microsoft/vscode/pull/303258) | Fix operator precedence in timeline pageSize calculation | ShehabSherif0 |
| [#303255](https://github.com/microsoft/vscode/pull/303255) | Fix `get_terminal_output` Invalid ID Handling | meganrogge |
| [#303253](https://github.com/microsoft/vscode/pull/303253) | Sessions: Implement collapsed panel widgets | mrleemurray |
| [#303156](https://github.com/microsoft/vscode/pull/303156) | fix(mcp): resolve env vars in agent plugin MCP server definitions | ConsoleTVs |
| [#303110](https://github.com/microsoft/vscode/pull/303110) | Skills usage telemetry | AbhitejJohn |
| [#303058](https://github.com/microsoft/vscode/pull/303058) | Browser Quick Open / Tab Management | kycutler |
| [#302944](https://github.com/microsoft/vscode/pull/302944) | Support for nested subagents | aeschli |

---

## 📈 关键趋势

- **Copilot CLI Agent** 是当前迭代中最活跃的开发领域，大量议题和 PR 围绕会话管理、worktree 集成和工具调用展开。
- **Sessions（会话窗口）** 正在经历重大 UI 重构，包括分组、折叠面板、辅助栏样式等改进。
- **MCP 集成** 持续完善，涉及 HTTP 客户端、工具冲突解决和配置管理。
- **AI 定制化** 方面新增了插件系统、技能管理和 Claude Agent 支持。
- **2026 主题刷新** ([#293405](https://github.com/microsoft/vscode/issues/293405)) 已列入 On Deck，计划对默认主题进行现代化改造。
- **Electron 40 升级** ([#292445](https://github.com/microsoft/vscode/issues/292445)) 在 On Deck 中等待排期。

---

*数据来源：[microsoft/vscode GitHub Repository](https://github.com/microsoft/vscode) | 通过 `gh` CLI 获取*
