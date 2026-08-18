---
title: "Manual Gen 全量与增量手册治理实施计划"
type: IMPLEMENTATION_PLAN
version: "0.2.0"
status: Archived
author: "Neplich Codex"
date: "2026-08-18"
last_updated: "2026-08-18"
feature: "manual-gen"
feature_path: "agents/docs-agent/manual-gen"
parent_feature: "agents/docs-agent"
feature_level: "3"
change_type: "modify"
change_tier: "major"
implementation_scope: "manual-scope-and-coverage"
archived_at: "2026-08-18"
archive_approved_by: "Neplich"
source_plan: "docs/engineer/agents/docs-agent/manual-gen/IMPLEMENTATION_PLAN.md"
previous_plan_archive: "docs/engineer/agents/docs-agent/manual-gen/archive/IMPLEMENTATION_PLAN-manual-gen.md"
related_prd: "docs/pm/agents/docs-agent/manual-gen/PRD.md"
related_trd: "docs/engineer/agents/docs-agent/manual-gen/TRD.md"
---

# Manual Gen 全量与增量手册治理实施计划

## 对齐与批准

批准依据：用户在 2026-08-18 明确要求按已给 Case 和四条批注开始实施，不再等待额外范围确认。
本轮为 `change_type: modify` / `change_tier: major`：按已批准 PRD v1.1.0 与 TRD v0.2.0，将 `scope_mode` 与 `change_mode`/目录策略分离，同时支持 bounded 增量补增、full-manual 全量写作/重写，并实施写前覆盖、任务拆页、分批不缩范围、写后门禁与真实 Chrome 视口/自然比例契约。

## 精确触点

| 分组 | 文件与动作 |
| --- | --- |
| 过程文档 | `docs/pm/agents/docs-agent/manual-gen/PRD.md`、`docs/engineer/agents/docs-agent/manual-gen/TRD.md`、本计划：对齐需求、设计、范围与验收。 |
| Router / Specialist | `agents/docs/skills/docs-agent/SKILL.md`、`agents/docs/skills/manual-gen/SKILL.md`、`agents/docs/skills/manual-gen/_internal/INSTRUCTIONS.md`：修改路由上下文、入口分类和权威执行契约。 |
| 宿主标准与说明 | `agents/docs/skills/docs-site-bootstrap/assets/docs/site/standards/doc-granularity.md`、`agents/docs/README.md`、`agents/docs/README_zh.md`：同步 Manual 粒度与双模式能力说明。 |
| 注册派生 | `skills-lock.json`：仅刷新 `docs-agent`、`manual-gen`、`docs-site-bootstrap` 的 `computedHash`。 |

## 禁止区

不修改上表以外文件，尤其是 marketplace / plugin / Kimi 登记、根 README / `AGENTS.md`、PM 入口、共享或生成契约、其他 Docs Specialist、`docs-site-bootstrap` 其他资产、CI / pytest 、冻结归档及任何截图、手册页或临时运行产物。

## 实施批次

| 批次 | 内容 | 验证 |
| --- | --- | --- |
| B1 过程对齐 | 完成 PRD / TRD / 计划的 FR、模式、视口与完成定义映射。 | 三份文档无冲突旧规则。 |
| B2 执行契约 | 修改 Router、Specialist 入口和执行指令。 | bounded / full-manual 与 extend / rewrite 正交可用，full-site 不越过 Specialist 边界。 |
| B3 宿主与派生同步 | 修改文档粒度标准、双语 Docs README，刷新三个 Skill hash。 | 页面拆分与双语语义一致，禁止区零 diff。 |
| B4 验证与独立复核 | 运行全部命令，由与实施上下文分离的验证者核对 Case、批注、计划与 diff。 | 命令全部 PASS，无未解释遗漏或范围外改动。 |

## 量级、验证与成功标准

除本计划外的产品/技术/Skill 净新增约 180–280 行；本计划自身约 50 行，不新增抽象。明显偏离时停止并核对范围。

验证命令：`uv run scripts/generate_shared_contracts.py --check`；`uv run scripts/check_repository_contract.py`；`uv run scripts/check_doc_contract.py`；`uv run --with pytest pytest agents/test_doc_contract.py scripts/test_generate_shared_contracts.py scripts/test_install_codex_skills.py scripts/test_check_repository_contract.py`；`git diff --check`。
成功标准：全部命令 PASS；最终 diff 严格匹配精确触点且禁止区零 diff；四种范围/目录组合、写前覆盖与拆页、全量分批不缩范围、写后校验、Chrome 真实窗口/内容视口与截图自然比例都能从权威契约直接定位；独立复核无遗漏。

## 实施结果

- B1 过程对齐：PRD v1.1.0、TRD v0.2.0 与本计划的 FR、模式、视口与完成定义已对齐，无冲突旧规则。
- B2 执行契约：Router、`manual-gen` 入口与执行指令已更新；`scope_mode`（bounded / full-manual / full-site 手册切片）与 `change_mode`（extend / rewrite）正交可用。
- B3 宿主与派生同步：`doc-granularity.md` Manual 粒度、双语 Docs README 已更新；`docs-agent`、`manual-gen`、`docs-site-bootstrap` 三个 Skill 的 `computedHash` 已刷新，禁止区零 diff。
- B4 验证与独立复核：三项契约检查与 `git diff --check` 全部 PASS；pytest 112 passed；与实施上下文分离的只读独立复核 PASS，无必须修复项。
- 交付：PR #307（`neplich-codex/manual-gen-scope-coverage` → `main`）。
