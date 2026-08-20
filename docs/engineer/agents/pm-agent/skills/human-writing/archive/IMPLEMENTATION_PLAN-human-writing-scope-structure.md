---
title: "human-writing 范围判断与结构权限实施计划"
type: IMPLEMENTATION_PLAN
feature: "skill-human-writing"
feature_path: "agents/pm-agent/skills/human-writing"
parent_feature: "agents/pm-agent/skills"
feature_level: "4"
implementation_scope: "human-writing-scope-structure"
version: "0.1.0"
status: Archived
archived_at: "2026-08-20"
archive_approved_by: "Neplich"
source_plan: "docs/engineer/agents/pm-agent/skills/human-writing/IMPLEMENTATION_PLAN.md"
author: "Neplich Codex"
date: "2026-08-20"
last_updated: "2026-08-20"
related_prd: "docs/pm/agents/pm-agent/skills/human-writing/PRD.md"
related_trd: "docs/engineer/agents/pm-agent/skills/human-writing/TRD.md"
related_issue: "https://github.com/Neplich/dev-agent-skills/issues/313"
changelog:
  - version: "0.1.0"
    date: "2026-08-20"
    changes: "完成编写范围判断、必要结构权限与高风险事实回传的契约修改并通过验证"
---

# human-writing 范围判断与结构权限实施计划

## 对齐与批准

批准依据：Issue #313 给出产品目标与建议修改面；用户在 2026-08-20 确认三项执行决策——
共同加载条款按最小改动一词同步、范围判断写入 `SKILL.md` 主体、按标准流程建分支提 PR。
本轮为 `change_type: modify` / `change_tier: major`：按已批准 PRD v1.2.0 与 TRD v1.2.0，
补齐 `human-writing` 本体的编写方式与范围判断、作者决策链、必要结构权限和高风险事实
回传，并同步周边共同加载条款措辞。

## 精确触点

| 分组 | 文件与动作 |
| --- | --- |
| Skill 本体 | 修改 `agents/product_manager/skills/human-writing/SKILL.md`（description、规则优先级、新增范围判断/结构权限/高风险事实三节、Create, Revise, or Audit 分层）与 `agents/openai.yaml`（默认提示同步 required structure） |
| 参考规则 | 修改 `references/document-patterns.md`（新增文档集合与文档站模式）和 `references/revision.md`（复核项增强）；`references/chinese-prose.md` 不改 |
| 周边条款 | 38 个 Router/Specialist `SKILL.md` 共同加载条款一词同步为 required structure；`pm-agent` 中 human-writing 职责描述同步扩展 |
| 文档面 | PRD/DECISIONS/TRD 升至 v1.2.0；`docs/architecture.md` 写作组合层段落更新 |
| 锁文件 | `skills-lock.json` 刷新 40 个被修改 Skill 的 computedHash |

禁止修改 marketplace、plugin descriptor、README、`references/chinese-prose.md`、共享
handoff、生成契约、宿主模板、安装器算法和发布配置；不新增参考文件，不恢复 Skill eval
体系，不增加 prose lint 或写作评分。

## 规模预期

不新建 Skill 文件，修改约 47 个文件，净增约 200 至 300 行。无运行时代码、依赖、配置、
schema 或新抽象。

## 验证

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

另按 TRD §9.3 的整站场景执行一次人工语义验收（LLM Wiki 案例，合并后另行执行）。

## 实施结果

- 实际修改 47 个文件，净增 287 行、删除 72 行，符合规模预期。
- 38 处共同加载条款全部同步为 required structure，无遗漏；`pm-agent` 职责描述同步扩展。
- 四项契约检查全部通过；repository contract、安装器和文档契约共 109 条 pytest 通过。
- 40 个被修改 Skill 的 `computedHash` 已刷新（首个 commit 漏提锁文件，由后续 commit
  `8eae6658` 补上，未 amend）。
- 未修改 `chinese-prose.md`、marketplace、plugin descriptor、README、共享契约或安装器。
- LLM Wiki 整站人工语义验收待合并后执行，不属于本计划的确定性验证范围。
