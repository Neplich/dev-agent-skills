---
title: "生成类 skill 后缀统一为 -gen 实施计划"
type: IMPLEMENTATION_PLAN
version: "1.0.0"
status: Archived
author: "Neplich Claude"
date: "2026-08-06"
last_updated: "2026-08-06"
generated_by: "feature-implementor"
feature: "skill-gen-rename"
feature_path: "repository-governance/skill-gen-rename"
parent_feature: "repository-governance"
feature_level: "2"
implementation_scope: "skill-gen-rename"
archived_at: "2026-08-15"
archive_approved_by: "Neplich"
source_plan: "docs/engineer/repository-governance/skill-gen-rename/IMPLEMENTATION_PLAN.md"
related_prd: "docs/pm/repository-governance/skill-gen-rename/PRD.md"
related_trd: "docs/engineer/repository-governance/skill-gen-rename/TRD.md"
related_issue: "https://github.com/Neplich/dev-agent-skills/issues/230"
---

# 生成类 skill 后缀统一为 -gen 实施计划

## 1. 实施范围

按 TRD 的 15 个目录重命名清单与同步面表格执行，只实现 PRD 与 TRD 逐条列出的改动，不新增任何范围外修改。

## 2. 实施步骤

1. 从最新 main 创建分支 `refactor/skill-gen-rename`。
2. `git mv` 15 个目录（4 skill + 4 test + 7 feature_path）。
3. 全仓替换 4 个旧名为新名（精确完整字符串替换），逐文件核对每个命中：SKILL.md frontmatter、evals.json 断言、eval_metadata.json、workspace fixture、router、AGENTS.md、README、PRD/TRD、跨 skill 引用、`scripts/test_install_codex_skills.py`。
4. 刷新 `skills-lock.json`：4 个目标 skill 的 key/source/computedHash，6 个被引用 skill 的 computedHash（SKILL.md 内容随替换变化）。
5. 处置历史保留边界：`docs/changelog/` 与已结案计划正文、归档正文与文件名 scope 保留旧名；归档 frontmatter 链接字段指向当前路径。
6. 处置 eval `comparison.md`：Skill 行保留旧名评测事实并标注改名；PASS 结论重标 `BLOCKED`（roadmap-gen ×3、github-release-gen eval-002）；BLOCKED 文件追加改名因素说明。
7. 更新被改 PRD/TRD 的 `last_updated`。
8. 运行验证清单（TRD 第 4 节），全部通过后交付。

## 3. 验证结果

| Command | Result |
| --- | --- |
| `uv run scripts/check_repository_contract.py` | PASS |
| `uv run scripts/check_eval_contract.py` | PASS |
| `uv run scripts/check_eval_artifacts.py` | PASS |
| `uv run scripts/check_doc_contract.py` | PASS |
| CI `python-tests`（`uv run --with pytest pytest scripts/ -q`） | 103 passed |
| CI checks（PR #241） | repository-contract / eval-contract / doc-contract / python-tests 全绿 |
| `git diff --check` | PASS |

## 4. 交付

PR #241（`refactor/skill-gen-rename`），breaking 说明与迁移映射表见 PR 正文。合并等待维护者确认。

## 5. 遗留事项

- 4 个改名 skill 的 eval 待 fresh 重跑（#238），完成后更新 comparison.md 覆盖 BLOCKED。
- 已结案实施计划正文中的旧名引用（如 formal-docs-sync 计划的 `docs-agent:release-notes-generator`）随未来归档门禁流程更新，不单独处理。
