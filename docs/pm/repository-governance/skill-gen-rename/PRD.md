---
title: "生成类 skill 后缀统一为 -gen PRD"
type: PRD
version: "1.0.0"
status: Implemented
author: "Neplich Claude"
date: "2026-08-06"
generated_by: "prd-gen"
feature: "skill-gen-rename"
feature_path: "repository-governance/skill-gen-rename"
parent_feature: "repository-governance"
feature_level: "2"
child_features: "N/A"
last_updated: "2026-08-06"
related_issues:
  - "https://github.com/Neplich/dev-agent-skills/issues/230"
---

# 生成类 skill 后缀统一为 -gen

## 背景

仓库表示「从证据生成一份文档产物」的 skill 存在两套后缀习惯：`-gen`（`trd-gen`、`prd-gen`、`manual-gen`）与 `-generator`（`changelog-generator`、`github-release-generator`、`roadmap-generator`、`release-notes-generator`）。issue #226 新增 `manual-gen` 采用 `-gen` 后缀后，两套习惯共存问题显性化：后续每新增一个生成类 skill 都要重新判断该跟哪一套。

## 范围

统一 4 个注册 skill 的后缀为 `-gen`：

| 旧名 | 新名 | 所属 agent |
| --- | --- | --- |
| `changelog-generator` | `changelog-gen` | product_manager |
| `github-release-generator` | `github-release-gen` | product_manager |
| `roadmap-generator` | `roadmap-gen` | product_manager |
| `release-notes-generator` | `release-notes-gen` | docs |

同步面（每个改名的 skill 逐一核对）：skill 目录与 `SKILL.md` frontmatter `name`、test 目录与 `evals.json` `skill_name`、marketplace 注册路径、`skills-lock.json`（含 computedHash）、router SKILL.md、AGENTS.md 与 README、PRD/TRD/`feature_path` 目录、eval 断言与 workspace fixture、跨 skill handoff 指针。

## 影响

- **Breaking**：marketplace 注册名即用户 slash 命令名。4 个旧命令（`/pm-agent:changelog-generator`、`/pm-agent:github-release-generator`、`/pm-agent:roadmap-generator`、`/docs-agent:release-notes-generator`）失效，迁移方式为改用新命令。changelog 标注 breaking。
- **`feature_path` 同步改名**：`docs/pm/` 与 `docs/engineer/` 下的对应目录改为新 skill 名，保持契约一致。
- **历史记录保留旧名**：`docs/changelog/` 发布记录、已结案实施计划正文与 `implementation-plans/archive/` 归档正文保留当时的事实；归档 frontmatter 链接字段（`feature_path`、`source_plan`、`related_prd`、`related_trd`）按契约指向当前路径。

## 变更分级

`major`：影响 marketplace 注册表、多个角色文档与契约脚本覆盖面。

## 验收标准

1. 全仓（排除 `docs/changelog/` 与归档文件）无 4 个旧名残留。
2. 5 项验证全绿：`check_repository_contract.py`、`check_eval_contract.py`、`check_eval_artifacts.py`、`check_doc_contract.py`、CI `python-tests`。
3. 改名 skill 的 eval `comparison.md` 标注旧名评测事实，PASS 结论重标 `BLOCKED` 待 fresh eval 重跑（#238）。
