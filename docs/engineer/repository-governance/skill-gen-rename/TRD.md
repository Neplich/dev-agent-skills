---
title: "生成类 skill 后缀统一为 -gen TRD"
type: TRD
version: "1.0.0"
status: Implemented
author: "Neplich Claude"
date: "2026-08-06"
generated_by: "trd-gen"
feature: "skill-gen-rename"
feature_path: "repository-governance/skill-gen-rename"
parent_feature: "repository-governance"
feature_level: "2"
last_updated: "2026-08-06"
related_prd: "docs/pm/repository-governance/skill-gen-rename/PRD.md"
related_issue: "https://github.com/Neplich/dev-agent-skills/issues/230"
---

# 生成类 skill 后缀统一为 -gen TRD

## 技术方案

### 目录重命名（git mv，保留历史）

15 个目录，新名映射见 PRD：

- 4 个 skill 目录：`agents/product_manager/skills/{changelog-generator,github-release-generator,roadmap-generator}`、`agents/docs/skills/release-notes-generator`
- 4 个 test 目录：对应 `agents/{product_manager,docs}/test/`
- 7 个 `feature_path` 目录：`docs/pm/agents/docs-agent/release-notes-generator`、`docs/engineer/agents/docs-agent/release-notes-generator`、`docs/pm/agents/pm-agent/skills/{github-release-generator,roadmap-generator,changelog-generator}`、`docs/engineer/agents/pm-agent/skills/{github-release-generator,changelog-generator}`

### 同步面（每个改名 skill 逐面核对）

| 面 | 变更 |
| --- | --- |
| 注册 | `.claude-plugin/marketplace.json` skills 路径；`skills-lock.json` key、source、computedHash |
| 路由 | `pm-agent`、`docs-agent` router SKILL.md 的 Available Skills、Routing Signals、Specialist Gate Pointers、分类表、Default Routes |
| 发现 | marketplace agent description、router frontmatter description（无描述变化则跳过） |
| Agent 文档 | `agents/{docs,product_manager}/README.md` 与 `README_zh.md` skills 表、Routing Rules |
| 顶层入口 | 根 `README.md` / `README_zh.md`、`AGENTS.md`（CLAUDE.md 软链接自动同步） |
| 过程文档 | PRD/TRD 正文与 `feature_path` 目录、实施计划正文（活跃计划跟随改名，已结案计划正文保留旧名） |

### computedHash 刷新

`skills-lock.json` 的 hash 由 `check_repository_contract.py` 的 `compute_tracked_directory_hash`（git tracked 文件路径+内容 sha256）校验。改名替换会改变 4 个目标 skill 与 6 个被引用 skill（`pm-agent`、`idea-to-spec`、`github-reader`、`docs-agent`、`formal-docs-sync`、`docs-audit`）的 SKILL.md 内容，10 个条目的 computedHash 一并刷新。

### 历史保留边界

| 位置 | 处置 |
| --- | --- |
| `docs/changelog/` 全部历史文件 | 保留旧名（历史发布记录） |
| 已结案实施计划正文（status: Implemented） | 保留旧名（closeout 历史记录）；更新需走归档门禁，超出本变更范围 |
| `implementation-plans/archive/` 归档正文与文件名 scope | 保留旧名；归档 frontmatter 链接字段（`feature_path`、`source_plan`、`related_prd`、`related_trd`）按契约指向当前路径 |

## 验证

1. `uv run scripts/check_repository_contract.py`
4. `uv run scripts/check_doc_contract.py`
5. `uv run --with pytest pytest scripts/ -q`（CI `python-tests`）

全部通过后方可交付。

## 风险与已知边界

- 已结案实施计划（如 `formal-docs-sync` 的 `IMPLEMENTATION_PLAN.md`）正文保留旧名引用 `docs-agent:release-notes-generator`，更新需先走归档门禁（创建忠实归档 + 声明 `previous_plan_archive`），作为独立变更处理，不在本变更内执行。
- 归档文件的 `source_plan` 指向 `changelog-gen/IMPLEMENTATION_PLAN.md`，该文件当前不存在（changelog 无活跃计划入口）；契约仅校验字段值格式，不校验目标存在性，随未来计划创建自然满足。
