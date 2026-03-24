# 产品经理 Agent

基于 GitHub 仓库的产品管理 Agent，主要职责是在项目 `docs/` 目录下维护产品文档。

## Agent 定位

- **使用者**：个人使用（手动触发）
- **核心场景**：应用开发项目的产品管理，基于 GitHub 仓库进行文档管理
- **输出形式**：Markdown 文档，写入项目 `docs/` 目录
- **行业背景**：不限，依项目目标群体而定

---

## Skill 清单

> 所有 skill 源文件统一在 `agents/product_manager/skills/` 下自管理，通过 `npx skills add ./agents/product_manager/skills/<name>` 安装到项目运行时（`.agents/skills/`）。

### 核心 Skill

| Skill | 目录 | 主要用途 | 安全评级 |
|-------|------|---------|---------|
| `idea-to-spec` | `skills/idea-to-spec/` | PRD、BRD、用户故事、ADR、API 文档等全套产品文档生成 | ✅ 低风险 |
| `competitive-brief` | `skills/competitive-brief/` | 竞品简报、定位差距、Battlecard | ✅ 低风险 |
| `changelog-generator` | `skills/changelog-generator/` | 从 GitHub PR/Commits/Release Tags 生成版本日志 | ✅ 低风险 |
| `github-reader` | `skills/github-reader/` | 读取 GitHub 仓库状态（Issues/PRs/Milestones），为 PM 提供项目健康报告 | ✅ 低风险 |
| `roadmap-generator` | `skills/roadmap-generator/` | 从 GitHub Milestones/Issues 生成或更新 `docs/roadmap.md`，支持日期分类和语义推断 | ✅ 低风险 |
| `release-notes-generator` | `skills/release-notes-generator/` | 生成面向用户的发版说明（highlights 提炼、代码示例、Upgrade Actions），与 changelog-generator 互补 | ✅ 低风险 |

### 按需使用

| Skill | 目录 | 说明 |
|-------|------|------|
| `competitive-intelligence` | `skills/competitive-intelligence/` | 销售向竞品 Battlecard（HTML），有 ToB 销售场景时使用 |

### 已排除

| Skill | 原因 |
|-------|------|
| ~~`github-project-management`~~ | Gen 安全评级 Critical Risk，依赖 alpha 版 claude-flow MCP |

---

## idea-to-spec 能力覆盖

`idea-to-spec` 已覆盖以下三类场景，无需额外安装对应 skill：

- `borghei/claude-skills@product-manager` → **由 idea-to-spec 覆盖**
- `davila7/claude-code-templates@agile-product-owner` → **由 idea-to-spec 覆盖**
- `smithery.ai@github-prd` → **由 idea-to-spec/prd-gen 覆盖**

内置子模块：`prd-gen` / `brd-gen` / `api-gen` / `trd-gen` / `adr-gen` / `mermaid-gen` / `weekly-report-gen`

---

## 管理的文档结构（目标）

```
docs/
├── prd.md                    # 产品需求文档（idea-to-spec/prd-gen）
├── roadmap.md                # 路线图（roadmap-generator）
├── changelog.md              # 版本日志（changelog-generator）
├── release-notes/            # 发版说明（release-notes-generator）
├── brd.md                    # 业务需求文档（idea-to-spec/brd-gen）
├── user-stories/             # 用户故事（idea-to-spec）
├── competitive-analysis.md   # 竞品分析（competitive-brief）
├── api/                      # API 文档（idea-to-spec/api-gen）
└── decisions/                # 架构决策记录 ADR（idea-to-spec/adr-gen）
```

---

## 下一步计划

1. ~~自建 `changelog-generator` skill~~ ✅ 已完成
2. ~~自建 `github-reader` skill~~ ✅ 已完成
3. ~~自建 `roadmap-generator` skill~~ ✅ 已完成
4. ~~自建 `release-notes-generator` skill~~ ✅ 已完成
5. 逐步自动化触发（GitHub webhook → Agent）
