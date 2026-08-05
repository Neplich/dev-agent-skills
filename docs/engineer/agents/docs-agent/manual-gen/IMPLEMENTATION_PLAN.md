---
title: "Manual Gen 实施计划"
type: IMPLEMENTATION_PLAN
version: "0.4.0"
status: Implemented
author: "Neplich Claude Code"
date: "2026-08-05"
last_updated: "2026-08-05"
generated_by: "feature-implementor"
feature: "manual-gen"
feature_path: "agents/docs-agent/manual-gen"
parent_feature: "agents/docs-agent"
feature_level: "3"
change_tier: "major"
implementation_scope: "manual-gen-skill-and-manual-doc-type"
related_prd: "docs/pm/agents/docs-agent/manual-gen/PRD.md"
related_trd: "docs/engineer/agents/docs-agent/manual-gen/TRD.md"
related_issues:
  - "https://github.com/Neplich/dev-agent-skills/issues/226"
changelog:
  - version: "0.4.0"
    date: "2026-08-05"
    changes: "批次 C 补齐发现层与 PM 入口触点（C1/C3/C6 描述、C7 根 README、C8 pm-agent 分类），并收窄截图卫生的浮层排除范围"
  - version: "0.3.1"
    date: "2026-08-05"
    changes: "修正导航触点与上游版本对齐，记录 manual 脚手架真实写入和宿主检查的端到端验证结果"
  - version: "0.3.0"
    date: "2026-08-05"
    changes: "独立核验：修正 pytest 记录为本机 213 passed，如实记录 codex 委派分工，补记模板资产引用缺陷的发现与修复"
  - version: "0.2.0"
    date: "2026-08-05"
    changes: "完成四批次实现、注册、eval 资产、契约检查与宿主 manual 类型实测"
  - version: "0.1.0"
    date: "2026-08-05"
    changes: "记录 issue #226 的四批次实施计划：类型层扩展、skill 本体、注册计数、eval"
---

# Manual Gen 实施计划

## 1. 对齐结果与门禁

| 项 | 结果 |
|---|---|
| PRD 对齐 | `already_approved` — `docs/pm/agents/docs-agent/manual-gen/PRD.md` v1.0.1，FR-M01~M16 与 US-M01~M10 覆盖本次全部改动 |
| TRD | `docs/engineer/agents/docs-agent/manual-gen/TRD.md` v0.1.2，`related_prd` 指向同 feature path 的 PRD |
| Feature path 门禁 | PRD / TRD / 本计划三者 `feature_path`、`parent_feature`、`feature_level` 一致 |
| Archive 扫描 | 新 feature path，无 active plan 也无 archive history，不需要 `previous_plan_archive` |
| UI 设计门禁 | 不适用。本次产出是 skill 契约文档与宿主脚本资产，不改动任何前端页面结构、交互流程或视觉系统，无需 Designer 输入 |
| `change_tier` | `major`，保持完整计划确认流程 |

## 2. 交付批次

四个批次按依赖顺序执行。批次 A 是批次 B 写入手册页的前置（没有 `manual` 枚举，手册页无法通过宿主 frontmatter 校验）。

### 批次 A — 类型层扩展

| # | 文件 | 动作 | 来源 |
|---|---|---|---|
| A1 | `agents/docs/skills/docs-agent/_internal/_shared/frontmatter-contract.md` | 修改 — `doc_type` 枚举加 `manual`，Notes 补一句手册页归属 | TRD §3.1 / FR-M10 |
| A2 | `agents/docs/skills/docs-audit/_internal/INSTRUCTIONS.md` | 修改 — 同步枚举表副本 | TRD §3.2 / FR-M10 |
| A3 | `agents/docs/skills/docs-site-bootstrap/assets/docs/site/scripts/lib/pages.mjs` | 修改 — `DOC_TYPES` 加 `'manual'`；`SECTION_ORDER` 在 `product` 后插入 `'manual'` | TRD §3.3、§3.4 / FR-M10 |
| A4 | `agents/docs/skills/docs-site-bootstrap/assets/docs/site/scripts/lib/sidebar.mjs` | 修改 — `SECTION_LABELS` 加 `manual: '操作手册'` | TRD §3.5 / FR-M10 |
| A5 | `agents/docs/skills/docs-site-bootstrap/assets/docs/site/scripts/scaffold-doc.mjs` | 修改 — `TYPES` 加 `manual: { directory: 'manual', template: 'manual-guide.md' }` | TRD §3 / FR-M11 |
| A6 | `agents/docs/skills/docs-site-bootstrap/assets/docs/site/standards/templates/manual-guide.md` | 新建 — 模板页，唯一 `docs-scaffold` 块，固化七项字段 | TRD §4 / FR-M08、FR-M11 |
| A7 | `agents/docs/skills/docs-site-bootstrap/assets/docs/site/manual/index.md` | 新建 — 类型根索引，`doc_type: landing` | TRD §4 / FR-M11 |
| A8 | `agents/docs/skills/docs-site-bootstrap/_internal/INSTRUCTIONS.md` | 修改 — 骨架目录清单补 `manual` | TRD §4 / FR-M11 |
| A9 | `agents/docs/skills/docs-site-bootstrap/assets/docs/site/.vitepress/config.public.ts` | 修改 — public 顶部 `nav` 增加 `/manual/` 入口 | TRD §3 / FR-M10 |
| A10 | `agents/docs/skills/docs-site-bootstrap/assets/docs/site/.vitepress/config.internal.ts` | 修改 — internal 顶部 `nav` 增加 `/manual/` 入口 | TRD §3 / FR-M10 |
| A11 | `agents/docs/skills/docs-site-bootstrap/assets/docs/site/index.public.md` | 修改 — public 落地页增加操作手册链接 | TRD §3 / FR-M10 |
| A12 | `agents/docs/skills/docs-site-bootstrap/assets/docs/site/index.internal.md` | 修改 — internal 落地页增加操作手册链接 | TRD §3 / FR-M10 |

依赖：A3 的 `SECTION_ORDER` 需与 A4 的 `SECTION_LABELS` 同批次改，否则 sidebar 生成时取到 `undefined` 标签。

侧边栏由 `SECTION_ORDER` 与 `SECTION_LABELS` 自动生成；顶部 nav 与落地页链接是手写内容，按 A9~A12 更新。

**禁止区**：`prepare-site.mjs`（截图复用既有 `referencedAssets()`）。

### 批次 B — skill 本体

| # | 文件 | 动作 | 来源 |
|---|---|---|---|
| B1 | `agents/docs/skills/manual-gen/SKILL.md` | 新建 — 入口门禁、环境协商协议、执行指针 | TRD §6、§7 / FR-M01、FR-M02 |
| B2 | `agents/docs/skills/manual-gen/_internal/INSTRUCTIONS.md` | 新建 — 八步执行契约、截图卫生、写入纪律、报告模板 | TRD §6、§7 / FR-M03~M09、FR-M12~M15 |

依赖：批次 A 完成。

`SKILL.md` 职责边界：只承载入口门禁与环境协商（决定是否继续的两步），执行细节全部在 `_internal/INSTRUCTIONS.md`。单层 `_internal`，不建 `types/` 子模块。

`_internal/INSTRUCTIONS.md` 八步：读宿主标准入口与 change-map → 读模板与既有 manual 结构 → 梳理角色/场景/流程 → 候选范围确认 → 视口设定与回读校验后采集 → 写入页面与截图并生长 change-map → 宿主检查与渲染验收 → handoff 至 docs-audit。

报告模板必须把「视口设定」与「视口回读」分列两个字段。

### 批次 C — 注册与计数

| # | 文件 | 动作 | 来源 |
|---|---|---|---|
| C1 | `.claude-plugin/marketplace.json` | 修改 — `docs-agent.skills` 加 `./skills/manual-gen`；**agent `description` 加图文手册能力** | TRD §8 |
| C2 | `skills-lock.json` | 修改 — 加 manual-gen 条目，`computedHash` 随契约脚本刷新 | TRD §8 |
| C3 | `agents/docs/skills/docs-agent/SKILL.md` | 修改 — Available Skills、Routing Signals、Specialist Gate Pointers 各加一条；**frontmatter `description` 与 Role Boundary 列举句同步** | TRD §8 |
| C4 | `agents/docs/README.md` | 修改 — skills 表、Specialist skills 计数 4 → 5、**Routing Rules 小节** | TRD §8 |
| C5 | `agents/docs/README_zh.md` | 修改 — 同步 skills 表、计数与 Routing Rules | TRD §8 |
| C6 | `AGENTS.md` | 修改 — `docs-agent` skill 数 4 → 5，Specialist skills 总数 31 → 32，**根路由指针句加手册分流** | TRD §8 |
| C7 | 根 `README.md` / `README_zh.md` | 修改 — 顶层 Agent 表的 Docs Agent 行由 `5 (1 + 4)` 改为 `6 (1 + 5)` 并补图文手册能力 | TRD §8 |
| C8 | `agents/product_manager/skills/pm-agent/SKILL.md` | 修改 — Downstream Role Handoff Targets、`formal_docs` 分类行、Default Routes 三处补图文手册，使默认用户入口能分类该请求 | TRD §8 |

依赖：批次 B 完成（`skills-lock.json` 的 hash 依赖 SKILL.md 最终内容）。

C1、C3、C6、C7、C8 属发现层：客户端与 PM 入口在读正文前先按这些描述选路，只改正文与计数会让新能力在元数据层不可达。

路由信号措辞按证据链区分：`manual-gen` 是「基于运行界面截图生成或更新站内图文用户操作手册」，`formal-docs-sync` 是「同步当前事实」，避免路由重叠。

### 批次 D — eval

| # | 文件 | 动作 | 来源 |
|---|---|---|---|
| D1 | `agents/docs/test/manual-gen/evals/evals.json` | 新建 — schema v1.0，5 个 eval item | TRD §9 |
| D2 | `.../workspace/eval-001-domain-provided/` | 新建 — `eval_metadata.json`、`comparison.md`、环境描述、`scripts/*.spec.md` | TRD §9 |
| D3 | `.../workspace/eval-002-local-start-consent/` | 新建 — 同上，环境描述标明无域名环境 | TRD §9 |
| D4 | `.../workspace/eval-003-no-environment-blocked/` | 新建 — 同上，环境描述标明环境不可用 | TRD §9 |
| D5 | `.../workspace/eval-004-share-link-identifier/` | 新建 — 同上，覆盖导出与分享流程 | TRD §9 |
| D6 | `.../workspace/eval-005-manual-hierarchy/` | 新建 — 同上，判定三层次语义 | TRD §9 |

依赖：批次 B 完成。

断言取向：一律语义判断，不比对具体目录结构，不断言划分出哪几个业务模块或模块叫什么名字。`evals.json` 不声明截图类 runner output。截图与手册页产物写隔离 scratch workspace，不入库。

## 3. 验证

每批次完成后运行完整链：

```bash
uv run scripts/check_repository_contract.py && uv run scripts/check_eval_contract.py && uv run scripts/check_eval_artifacts.py && uv run scripts/check_doc_contract.py
```

批次 D 完成后追加仓库既有 pytest。

批次 A 的宿主脚本改动不被本仓库 pytest 覆盖，需按 TRD §10 在临时 bootstrap 出的站点上实测一次：创建一个 `doc_type: manual` 页面，运行宿主 `check:frontmatter` 与导航生成，确认通过并记录结果。

skill 行为验证（fresh subagent validation 与 `without_skill` baseline）在实施完成后单独执行，属交付前门禁，不在本计划的编码批次内。

## 4. 执行分工

- PRD、TRD 与本实施计划由 Claude 主进程直接编写，上下文不转手。
- 批次 A 的 `pages.mjs`、`sidebar.mjs` 两处常量增补由 Claude 主进程完成。
- 批次 A 剩余项与批次 B、C、D 的实现委派 `codex exec` 执行（`-s workspace-write`，只改文件，不 commit / push / 建 PR）；codex 在其会话内部使用了实现与只读验收两个 sub-agent。
- codex 侧的自评不作为判定。Claude 主进程独立核验：禁止区零 diff、四条契约检查、CI 同款 pytest、eval 断言语义取向、行数量级，并回读关键产物。

## 5. 实施约束

- 只实现本计划逐条列出的改动，每处 diff 可追溯到 PRD 的 FR 或 TRD 的章节。
- 禁止新增抽象层或基类、重试与退避、缓存、降级开关、feature flag、新配置项、包装函数、事件钩子、监控埋点、额外日志层。
- 不为不可能发生的场景写错误处理，不预留扩展点，不做防御式空值兜底。
- 沿用相邻文件的既有写法与分层：skill 文档对齐 `formal-docs-sync` 与 `release-notes-generator` 的结构，宿主资产对齐现有五类模板与根索引。
- 不改动 `formal-docs-sync` 的五类契约与八步流程，不改 `prepare-site.mjs`。
- 量级预期：净新增约 800–1100 行，不新增抽象层。实际偏离明显时停下核对范围。

## 6. 阻塞项与风险

| 项 | 处理 |
|---|---|
| 五处枚举同步遗漏会让手册页在宿主校验中失败 | 批次 A 作为独立批次先完成并单独验证 |
| `SECTION_ORDER` 与 `SECTION_LABELS` 不同步会让 sidebar 取到 `undefined` | 两处在同一批次内改，验证时检查生成的 sidebar |
| 宿主脚本改动无本仓库 pytest 覆盖 | 在临时站点上实测一次并记录结果 |
| 临时宿主无法为 strict affected check 确定 Git 基线 | `check-affected.mjs` 的候选基线是 `origin/HEAD` 或 `HEAD^1`；只有单个 commit 的临时仓库两者都不存在，建立两个 commit 后即可通过 |
| eval 依赖外部站点 mermaid.live | 不可访问时该轮记 blocked；断言无触发条件时记 `NOT EXERCISED` |

## 7. Closeout

### 7.1 实施结果

| 批次 | 完成内容 | 状态 |
|---|---|---|
| A | 同步 `manual` frontmatter 枚举与审计副本，接入 scaffold、bootstrap inventory、唯一 manual 模板与类型根索引 | Implemented |
| B | 新增 `manual-gen` 入口门禁、条件式环境协商与八步截图证据执行契约 | Implemented |
| C | 完成 router、marketplace、skills-lock、双语 README 与仓库计数注册 | Implemented |
| D | 新增 5 个语义 eval、5 份 metadata、5 份未执行 comparison 与 3 个 Playwright 脚本片段 | Implemented |

### 7.2 验证结果

| 命令 | 结果 |
|---|---|
| `UV_CACHE_DIR=/tmp/manual-gen-uv-cache uv run scripts/check_repository_contract.py` | PASS |
| `UV_CACHE_DIR=/tmp/manual-gen-uv-cache uv run scripts/check_eval_contract.py` | PASS |
| `UV_CACHE_DIR=/tmp/manual-gen-uv-cache uv run scripts/check_eval_artifacts.py` | PASS |
| `UV_CACHE_DIR=/tmp/manual-gen-uv-cache uv run scripts/check_doc_contract.py` | PASS |
| CI 同款 `uv run --with pytest pytest ...` | PASS：213 passed（Claude 主进程本机复跑。codex 会话内该命令因 sandbox 禁止访问 PyPI 而 BLOCKED，属环境限制，非实现缺陷） |
| 临时宿主初始化 | PASS：复制 `docs-site-bootstrap` 交付资产（42 个文件），`git init` 后建立两个 commit |
| 临时宿主 `npm ci --offline --ignore-scripts` | PASS：从本地缓存安装锁定依赖 |
| `npm run new:doc -- --type manual --path docs/site/manual/diagram-authoring/create-first-diagram.md --title "创建第一张图表" --visibility both --stage dev --owner docs --related-code "src/routes/editor/**"` | PASS：输出 `"dryRun": false`、`"docType": "manual"`、`"lastVerifiedVersion": "unverified"`，页面真实落盘 |
| `new:doc` 内部 `npm run test:docs` | PASS：`check:frontmatter`、`check:affected --strict`、`check:version` 与 `node --test` 全部通过 |
| 独立 `npm run check:frontmatter` | PASS：`Frontmatter check passed` |
| `npm run prepare:nav` | PASS：生成的 `.generated/.navigation/sidebar.public.mjs` 中 `/manual/` 分区正确包含新页 `/manual/diagram-authoring/create-first-diagram`，层级为“操作手册 → 根索引 → 创建第一张图表” |
| 生成页面检查 | PASS：frontmatter 七字段合法（`doc_type: manual`、`last_verified_version: unverified`），正文含完整七项字段骨架 |

结论：批次 A 的五处枚举改动、manual 模板与脚手架类型映射已端到端验证可用。`check-affected.mjs` 的候选基线是 `origin/HEAD` 或 `HEAD^1`；只有单个 commit 的临时仓库两者都不存在，因此无法确定基线，建立两个 commit 后即可通过。

### 7.3 Eval、残余风险与下一 owner

- 本轮按实施范围只创建 durable eval 资产，未执行 fresh subagent validation，也未生成新的 `without_skill` baseline；5 份 `comparison.md` 均如实记录 `Overall result: BLOCKED`。
- 未创建或跟踪截图、lane、transcript、verdict、timing、status、diagnostics 等运行期 eval 产物。
- 独立核验发现并修复一处实现缺陷：`manual-guide.md` 的 `docs-scaffold` 块内原含完整 Markdown 图片语法 `![...](./step-1-example.png)`，指向不存在的文件。宿主 `prepare-site.mjs` 的 `referencedAssets()` 以纯文本正则提取引用，不区分 fence 内外，会在每次站点构建产生一条 `file does not exist` 警告。现有五类模板均无图片引用，属本次新引入。已改为不构成可解析图片语法的描述式说明，复测捕获引用数为 0，并同步刷新 `docs-site-bootstrap` 的 `computedHash`。
- 残余验证缺口是 Playwright live selector 尚待 fresh eval 实际验证；没有已知实现缺口。
- 下一 owner 为维护者：按仓库 Fresh Sub-Agent 门禁决定何时执行 5 个 eval；本轮不 commit、不 push、不建 PR。
