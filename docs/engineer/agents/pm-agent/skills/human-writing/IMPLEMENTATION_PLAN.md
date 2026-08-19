---
title: "human-writing Skill 实施计划"
type: IMPLEMENTATION_PLAN
feature: "skill-human-writing"
feature_path: "agents/pm-agent/skills/human-writing"
parent_feature: "agents/pm-agent/skills"
feature_level: "4"
implementation_scope: "human-writing-skill-integration"
version: "0.4.0"
status: Pending Confirmation
author: "Neplich Codex"
date: "2026-08-19"
last_updated: "2026-08-19"
related_prd: "docs/pm/agents/pm-agent/skills/human-writing/PRD.md"
related_trd: "docs/engineer/agents/pm-agent/skills/human-writing/TRD.md"
changelog:
  - version: "0.4.0"
    date: "2026-08-19"
    changes: "完成六个下游 Router 与三十二个 Specialist 的共同加载适配并通过验证"
  - version: "0.3.0"
    date: "2026-08-19"
    changes: "扩展为六个下游 Router 与三十二个 Specialist 的共同加载适配计划"
  - version: "0.2.0"
    date: "2026-08-19"
    changes: "完成 Skill、注册和验证，记录实际结果并等待归档确认"
  - version: "0.1.1"
    date: "2026-08-19"
    changes: "记录用户确认并对齐 quick_validate 的仓库扩展字段兼容方式"
  - version: "0.1.0"
    date: "2026-08-19"
    changes: "建立 human-writing Skill 本体、注册、发现和验证计划"
---

# human-writing Skill 实施计划

## 1. 前置对齐

- `request_type: new_feature`
- `change_tier: major`
- `hotfix_disposition: rejected`
- PRD 对齐结果：`already_approved`
- 功能位置固定为 `agents/product_manager/skills/human-writing/`。
- `human-writing` 是独立组合能力，随 PM 插件发布，不并入 `pm-agent`，不新增根 `/share`。
- 第一批 Skill 本体与 PM 发现面已完成；本计划继续承接第二批周边引用适配。
- 分批是撰写与确认顺序，不是提交边界：两批改动随同一 PR 一并交付，第 2 节的禁止清单只约束第二批相对第一批的增量改动。

## 2. 规模与边界

第一批实际新建 9 个文件、修改 10 个文件。第二批预计不新建文件，修改 44 个文件，净增
约 350 至 500 行：38 个目标 `SKILL.md`、`skills-lock.json`、`docs/architecture.md` 和
四份本功能过程文档。没有运行时代码、依赖、配置、schema、服务或新抽象。

禁止修改 frontmatter 描述、Router 主路由表、Specialist entry gate、`human-writing` 本体、
`pm-agent`、marketplace、plugin descriptor、README、共享 handoff、生成契约、宿主模板、
安装器算法、eval runner 和发布配置。

## 3. 文件级范围

### 3.1 已完成的需求与设计对齐

| 路径 | 操作 | 内容 |
| --- | --- | --- |
| `docs/pm/agents/pm-agent/skills/human-writing/PRD.md` | 新建 | 固化用户、目标、规则优先级、文种和验收标准 |
| `docs/pm/agents/pm-agent/skills/human-writing/DECISIONS.md` | 新建 | 记录名称、位置、组合关系、开放输入和批次边界 |
| `docs/engineer/agents/pm-agent/skills/human-writing/TRD.md` | 新建 | 定义目录、运行流程、注册同步和验证 |
| `docs/engineer/agents/pm-agent/skills/human-writing/IMPLEMENTATION_PLAN.md` | 新建 | 保存当前活跃实施范围 |
| `docs/pm/agents/pm-agent/PRD.md` | 修改 | 注册直接子功能并增加辅助写作能力目标 |

### 3.2 Skill 本体

| 路径 | 操作 | 内容 |
| --- | --- | --- |
| `agents/product_manager/skills/human-writing/SKILL.md` | 新建 | 触发、优先级、推断、事实保护、工作流和交付规则 |
| `agents/product_manager/skills/human-writing/agents/openai.yaml` | 新建 | Skill UI 和默认提示 |
| `agents/product_manager/skills/human-writing/references/chinese-prose.md` | 新建 | 自然中文与段落推进规则 |
| `agents/product_manager/skills/human-writing/references/document-patterns.md` | 新建 | 九类文档的信息组织方式 |
| `agents/product_manager/skills/human-writing/references/revision.md` | 新建 | 克制改写和静默复核 |

### 3.3 注册与发现

| 路径 | 操作 | 内容 |
| --- | --- | --- |
| `agents/product_manager/skills/pm-agent/SKILL.md` | 修改 | 增加 `human-writing` 发现与组合说明 |
| `.claude-plugin/marketplace.json` | 修改 | 注册新 Skill 并更新 PM 描述 |
| `agents/product_manager/.claude-plugin/plugin.json` | 修改 | 与 marketplace PM 描述对齐 |
| `.kimi-plugin/plugin.json` | 修改 | 更新仓库能力描述；skills 目录数组不变 |
| `agents/product_manager/README.md` | 修改 | 增加英文能力清单和组合说明 |
| `agents/product_manager/README_zh.md` | 修改 | 增加中文能力清单和组合说明 |
| `README.md` | 修改 | Skills 总数、内部 Skill 数、PM 计数和能力描述 |
| `README_zh.md` | 修改 | 同步中文发现信息 |
| `skills-lock.json` | 修改 | 新增 `human-writing` 并刷新 `pm-agent` hash |

## 4. 实施顺序

```mermaid
flowchart LR
    A["确认本计划"] --> B["用 skill-creator 初始化目录"]
    B --> C["编写核心契约与三份参考规则"]
    C --> D["同步 PM 发现、插件注册和 README"]
    D --> E["刷新 lock hash"]
    E --> F["结构检查与三类前向样例"]
```

1. 使用仓库规定的 `skill-creator` 初始化脚本创建标准目录和 `openai.yaml`。
2. 用 `apply_patch` 写入核心规则与三个按需参考文件，不添加 prose lint 脚本。
3. 更新 PM Router 的能力发现、插件 descriptor、marketplace 和中英文 README。
4. 按安装器现有 hash 算法更新 `skills-lock.json`，不修改算法本身。
5. 运行确定性检查，并用用户手册、TRD、Release Notes 三组输入复核规则效果。

### 4.1 第二批顺序

```mermaid
flowchart LR
    P["确认第二批计划"] --> R["适配六个 Router"]
    R --> S["适配三十二个 Specialist"]
    S --> A["更新架构说明"]
    A --> H["刷新 38 个 lock hash"]
    H --> V["引用、契约和测试验证"]
```

1. 完整读取每个目标 `SKILL.md`，在首个执行章节前加入最小共同加载条款。
2. Router 条款只负责在主 Specialist 选定后共同加载，不增加主 route。
3. Specialist 条款覆盖直接调用，且排除纯代码、配置、schema、lockfile 和数据输出。
4. 更新 `docs/architecture.md`，刷新 38 个 `computedHash`。
5. 运行引用覆盖、仓库契约、文档契约、安装器测试和 diff 审查。

## 5. 验证

```bash
uv run scripts/generate_shared_contracts.py --check
uv run scripts/check_repository_contract.py
uv run scripts/check_doc_contract.py
uv run --with pytest pytest \
  scripts/test_check_repository_contract.py \
  scripts/test_install_codex_skills.py \
  agents/test_doc_contract.py
git diff --check
```

官方 `quick_validate.py` 在临时副本中运行：只移除它不认识、但本仓库要求保留的
`visibility: internal`，其余内容与实际 Skill 一致；实际文件仍由仓库和文档契约检查。

前向样例分别检查用户手册、TRD 和 Release Notes。验收重点是事实不变、术语不丢、段落
有推进、普通用户正文不泄露 Agent 执行口径。若任何检查失败，修正 Skill 或同步面，不
放宽检查器。

## 6. 分工与停止条件

当前环境没有独立文档编写与验证 sub-agent 接口，本轮由主进程实施并进行两遍审查：第一遍
对照 PRD/TRD 和文件范围，第二遍只看验证结果、diff 和越界修改。

若实施需要修改范围外 Router、Specialist、共享契约、安装器算法或增加运行时代码，立即
停止并重新确认范围。活跃计划保持 `Pending Confirmation`；只有用户明确批准归档后，才以
`Implemented` 状态移入 `archive/IMPLEMENTATION_PLAN-human-writing-skill-integration.md`。

## 7. 实施结果

### 7.1 第一批

- 新建 9 个文件、修改 10 个文件，新增 957 行、删除 19 行；没有运行时代码或依赖。
- Skill 核心、三份参考规则和 OpenAI 元数据共 383 行，符合计划中的 250 至 400 行范围。
- 官方 `quick_validate.py` 在只移除仓库扩展字段的临时副本上通过；实际 `visibility`
  由仓库检查器验证。
- shared contracts、repository contract、documentation contract 和 diff 检查通过。
- repository contract、安装器和文档契约共 109 条 pytest 通过。
- 用户手册、TRD 和 Release Notes 三组前向样例保留受保护事实，并移除目标 Agent/过程口径。
- 未修改其他 Router、文档生成 Skill、共享契约、安装器算法、eval runner 或发布配置。

### 7.2 第二批

- 已适配 38 个目标 Skill：6 个下游 Router 和 32 个会生成面向读者文本的 Specialist。
- Router 在主 Specialist 选定后按需共同加载 `human-writing`；Specialist 直接调用时执行同一
  规则，不形成前后消费链。
- 共同加载只影响读者视角、信息顺序和表达；事实、结构、路径、门禁和验证仍由主 Skill 负责。
- 纯代码、配置、schema、lockfile 和数据输出明确不触发，避免无关任务增加上下文。
- 38 个目标引用覆盖率为 38/38；其中 Router 6/6、直接调用 Specialist 32/32。
- shared contracts、repository contract、documentation contract 和 diff 检查通过；相关
  repository contract、安装器和文档契约共 109 条 pytest 通过。
- 第二批没有修改 frontmatter 描述、主路由表、entry gate、共享 handoff、生成契约、安装器
  算法、eval runner、宿主模板、运行时代码、依赖或发布配置。
