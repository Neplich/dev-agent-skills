---
title: "Docs Site Layout 实施计划"
type: IMPLEMENTATION_PLAN
version: "0.3.0"
status: Archived
author: "Neplich Codex"
date: "2026-08-18"
last_updated: "2026-08-18"
feature: "docs-site-layout"
feature_path: "agents/docs-agent/docs-site-layout"
parent_feature: "agents/docs-agent"
feature_level: "3"
implementation_scope: "docs-site-layout"
archived_at: "2026-08-18"
archive_approved_by: "Neplich"
source_plan: "docs/engineer/agents/docs-agent/docs-site-layout/IMPLEMENTATION_PLAN.md"
related_prd: "docs/pm/agents/docs-agent/docs-site-layout/PRD.md"
related_trd: "docs/engineer/agents/docs-agent/docs-site-layout/TRD.md"
related_issues:
  - "https://github.com/Neplich/dev-agent-skills/issues/303"
  - "https://github.com/Neplich/dev-agent-skills/issues/304"
changelog:
  - version: "0.3.0"
    date: "2026-08-18"
    changes: "维护者确认创建 PR，完成 closeout 并归档实施计划"
  - version: "0.2.0"
    date: "2026-08-18"
    changes: "记录实现文件、自动化检查、真实浏览器测量、清理结果与下一 owner"
  - version: "0.1.0"
    date: "2026-08-18"
    changes: "建立双站点导航与文档布局的一轮活跃实施计划"
---

# Docs Site Layout 实施计划

## 1. 前置对齐

- 已批准输入：同 feature PRD 与 TRD，来源为 issue #303/#304 和维护者确认数值。
- Feature path 为 `agents/docs-agent/docs-site-layout`，父功能
  `agents/docs-agent`，层级 `3`。
- `change_type: modify`；`change_tier: major`。本路径无既有 active plan 或 archive。
- W1–W4 已完成；维护者于 2026-08-18 明确要求创建 PR，批准 closeout 与归档。

## 2. 目标、规模与边界

同一 PR 完成双站点入口一致性和固定页面骨架。代码与测试预计净增约 120–220 行，
不新增依赖；三份文档预计约 250–350 行。明显超出时先核对范围。

允许修改当前 Skill 的 inventory、导航/主题资产、两个根首页、八个分区首页、既有
Node 测试、`skills-lock.json`、本 feature 三份文档和父级 docs-agent PRD 的
`child_features` 索引。禁止修改其他 Skill、
Router、README、注册、`AGENTS.md`、宿主 CI、依赖、模板、脚手架和发布配置。

## 3. 文件级范围

| 路径 | 操作与内容 |
| --- | --- |
| 本 feature 的 `PRD.md`、`TRD.md`、`IMPLEMENTATION_PLAN.md` | 新增批准文档链和活跃计划 |
| 父级 `docs/pm/agents/docs-agent/PRD.md` | 把本 feature 加入 `child_features` 索引 |
| `docs-site-bootstrap/_internal/INSTRUCTIONS.md` | inventory 42→44，登记两份导航 JSON |
| `assets/docs/site/.vitepress/navigation.public.json`、`navigation.internal.json` | 新增两套目标专属有序入口 |
| `assets/docs/site/.vitepress/config.public.ts`、`config.internal.ts` | 只消费各自目标入口 |
| `assets/docs/site/index.public.md`、`index.internal.md` | 唯一 marker 与 `aside: false` |
| `assets/docs/site/scripts/lib/pages.mjs` | JSON 校验和首页列表渲染 |
| `assets/docs/site/scripts/prepare-site.mjs` | 按目标渲染首页并复制 JSON |
| `assets/docs/site/{standards,product,manual,design,api,database,ops,release-notes}/index.md` | 分区首页 `aside: false` |
| `assets/docs/site/.vitepress/theme/custom.css` | 1440/240/752/224/256、居中、空目录和层级 |
| `assets/docs/site/scripts/__tests__/scaffold-doc.test.mjs` | 导航、首页、分区与 CSS 回归 |
| `skills-lock.json` | 刷新 `docs-site-bootstrap.computedHash` |

表中 `docs-site-bootstrap/` 的完整前缀是 `agents/docs/skills/`，`assets/` 的完整
前缀是 `agents/docs/skills/docs-site-bootstrap/`。`config.shared.ts`、
`package.json`、`package-lock.json` 预计零修改；需要修改时先更新 TRD 和本计划。

## 4. 分阶段实施

| 阶段 | 内容 | 验证 |
| --- | --- | --- |
| W1 导航 | 建立 JSON、接入两套 config、用 marker 生成根首页。 | 固定顺序与逐项 `text/link/order` 测试。 |
| W2 页面骨架 | 根页/分区页关闭 aside，CSS 固定三列、居中和层级。 | 页面分类和数值断言。 |
| W3 Bootstrap 同步 | 更新 44 项 inventory，刷新 Skill hash。 | 新资产复制、hash 与禁改面零 diff。 |
| W4 页面验证 | Node、双 build、真实浏览器和仓库检查。 | 所有门禁 PASS，清理运行期产物。 |

```mermaid
flowchart LR
    W1["W1 双站点导航"] --> W2["W2 页面骨架"]
    W2 --> W3["W3 Inventory 与 hash"]
    W3 --> W4["W4 构建与真实页面验证"]
```

## 5. 验证

在站点资产目录执行：

```bash
node --test scripts/__tests__/*.test.mjs
npm run build:public
npm run build:internal
```

真实 Chrome 以 1280×900、2560×1440 检查双站点 `/`、`/product/` 和 internal
`/standards/doc-lifecycle`，记录 1440px 整体、240px 左栏、约 688px 正文、
224px 目录、约 256px aside、目录显隐、两侧空白和顶部点击；再以 390px 烟测
VitePress 既有移动端折叠。

仓库根执行：

```bash
uv run scripts/generate_shared_contracts.py --check
uv run scripts/check_repository_contract.py
uv run scripts/check_doc_contract.py
git diff --check
git diff --exit-code -- agents/docs/skills/docs-site-bootstrap/assets/docs/site/package.json agents/docs/skills/docs-site-bootstrap/assets/docs/site/package-lock.json
```

最后确认 `skills-lock.json` 仅目标 hash 变化，`git status --short` 不包含
`.generated/`、`node_modules/`、截图、临时服务文件或其他无关内容。

## 6. 停止与收尾

入口不一致、页面分类错误、顶部栏被覆盖、1280/2560 布局不符、移动端回归、build
或契约失败均阻塞交付。不得通过扩大正文、隐藏测试或升级依赖绕过失败。完成后在
本计划记录实际文件、命令结果、浏览器测量、残余风险和下一 owner；维护者已批准
归档和 PR 交付，但未经明确授权不得 merge。

## 7. 实施结果

W1–W4 已按计划完成，共修改或新增 19 个 Skill 文件、4 个正式文档文件和
`skills-lock.json`；未修改依赖、其他 Skill、Router、README、注册、宿主 CI、
模板或脚手架。实际代码与测试增量接近预期数量级，未新增抽象层或运行时依赖。

自动化结果：

- Node 测试 82/82 通过。
- Public 与 internal 生产构建通过；仅保留既有模板资源跳过和大 chunk 警告。
- 共享契约生成检查、仓库契约、文档契约和 diff whitespace 检查通过。
- 仓库 CI 对应 pytest 集合 112/112 通过。
- `docs-site-bootstrap.computedHash` 更新为
  `793ff9d21499c57964e9ed1f3e77da1d5590adec976fdbbcf5dd6d0dad8364fc`。

真实 Chrome 验收结果：

| 视口与页面 | 实际结果 |
| --- | --- |
| 1280×900 `/` | 无左栏和右侧目录，根首页入口与目标顶部导航逐项一致 |
| 1280×900 `/product/` | 240px 左栏、752px 内容列，无右侧目录；顶部栏层级更高 |
| 1280×900 具体文档 | 在可用宽度内保持三列，正文约 656px，目录 224px |
| 2560×1440 具体文档 | 1440px 骨架居中，左栏 240px、正文 688px、目录 224px，两侧各 560px 空白 |
| 390×844 页面烟测 | 保留 VitePress 顶部菜单、侧栏和目录折叠，桌面 CSS 未侵入 |

额外执行完整 `npm run test:docs` 时，frontmatter 与 affected 检查通过；version
检查因当前仓库 `HEAD` 正好位于 `v0.6.0` tag，而脚手架 fixture 的
`.meta/releases.json.latest` 按设计为 `null` 而停止。该宿主版本上下文不属于本
feature 的实现缺陷，版本校验函数本身已由通过的 Node 测试覆盖。

构建产生的 `.generated/`、`node_modules/` 和临时浏览器页面均已清理，工作区只
保留计划内文件。当前残余风险仍是 VitePress 1.6.4 默认主题类名和 `:has()` 结构；
锁定版本、CSS 契约测试与真实页面检查已提供当前范围内的验证。下一 owner 为
Delivery；维护者已确认提交并创建 PR，本计划完成归档，但本轮不得自行 merge。
