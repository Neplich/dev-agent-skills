---
title: "实施计划归档路径契约迁移实施计划"
type: IMPLEMENTATION_PLAN
version: "0.4.0"
status: Archived
author: "Neplich Codex"
date: "2026-08-12"
last_updated: "2026-08-12"
generated_by: "feature-implementor"
feature: "implementation-plan-archive-gate"
feature_path: "agents/engineer-agent/skills/feature-implementor/implementation-plan-archive-gate"
parent_feature: "agents/engineer-agent/skills/feature-implementor"
feature_level: "5"
implementation_scope: "archive-path-contract-migration"
archived_at: "2026-08-15"
archive_approved_by: "Neplich"
source_plan: "docs/engineer/agents/engineer-agent/skills/feature-implementor/implementation-plan-archive-gate/IMPLEMENTATION_PLAN.md"
previous_plan_archive: "docs/engineer/agents/engineer-agent/skills/feature-implementor/implementation-plan-archive-gate/archive/IMPLEMENTATION_PLAN-archive-content-settlement-model.md"
related_prd: "docs/pm/agents/engineer-agent/skills/feature-implementor/implementation-plan-archive-gate/PRD.md"
related_trd: "docs/engineer/agents/engineer-agent/skills/feature-implementor/implementation-plan-archive-gate/TRD.md"
related_issue: "https://github.com/Neplich/dev-agent-skills/issues/264"
change_tier: "major"
---

# 实施计划归档路径契约迁移实施计划

## 1. 实施上下文

本计划承接 GitHub issue
[#264](https://github.com/Neplich/dev-agent-skills/issues/264)。Issue #54 引入
归档门禁时使用 `docs/engineer/{feature_path}/implementation-plans/archive/` 保存
完成态或废弃态实施计划。该中间层 `implementation-plans/` 没有独立语义——计划类型
已由文件名 `IMPLEMENTATION_PLAN-<scope>.md` 与归档 frontmatter 表达，中间层只会
让功能树变深。本变更将归档路径契约定为：

```text
docs/engineer/{feature_path}/archive/IMPLEMENTATION_PLAN-<scope>.md
```

活跃计划入口 `docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md` 保持不变。

## 2. 已确认技术设计

### 2.1 新路径契约

- 归档目录直接位于对应 `feature_path` 下：`docs/engineer/{feature_path}/archive/`。
- 归档文件名规则不变：`IMPLEMENTATION_PLAN-<scope>.md`，`<scope>` 使用
  lower kebab-case。
- 活跃计划入口不变：`docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md`。
- `previous_plan_archive` 指向同一 `feature_path` 下的新路径归档。
- `archive/` 被结构治理识别为所属功能的历史存储，不被识别为子功能。

### 2.2 存量迁移

当前仓库 14 份跟踪归档执行纯路径迁移，正文和 frontmatter 内容保持不变：

```text
docs/engineer/{feature_path}/implementation-plans/archive/IMPLEMENTATION_PLAN-<scope>.md
→ docs/engineer/{feature_path}/archive/IMPLEMENTATION_PLAN-<scope>.md
```

迁移后删除已空的 `implementation-plans/` 目录。

### 2.3 契约与校验

- `AGENTS.md` 窄例外与归档门禁 PRD/TRD 的路径描述同步为新契约。
- `feature-implementor`、`trd-gen`、`idea-to-spec` 的指令文件同步新路径。
- `check_repository_contract.py` 识别新路径，拒绝新增或修改仍使用旧路径的归档。
- `archive/` 不再被结构治理误识别为子功能节点。

## 3. 实施范围

| Path | Operation | Result |
| --- | --- | --- |
| `AGENTS.md` | Modify | 窄例外路径更新为 `archive/`。 |
| 归档门禁 PRD/TRD | Modify | FR-002 / US-001 / TRD 路径描述更新为 `archive/`；PRD 非目标补充存量迁移说明。 |
| `feature-implementor` / `trd-gen` / `idea-to-spec` 指令 | Modify | 归档路径引用全部更新为 `archive/`。 |
| `scripts/check_repository_contract.py` | Modify | 正则与归档目录构造识别新路径；`previous_plan_archive` 纯路径迁移视为内容未变。 |
| `scripts/check_doc_contract.py` | Modify | 归档工件路径识别更新。 |
| `scripts/test_check_repository_contract.py`、`agents/test_eval_contract.py` | Modify | fixture 与断言路径更新。 |
| `agents/engineer/test/feature-implementor/evals/` | Modify | eval 断言、prompt、fixture 路径更新；eval-013 workspace fixture 迁移。 |
| 14 份跟踪归档 | Move | 纯路径迁移到 `{feature_path}/archive/`。 |
| 3 份 active 计划 | Modify | `previous_plan_archive` 指向新路径。 |
| 本文件 | Modify | 归档 #172 计划到 `archive/`，记录本轮实施。 |

明确不修改：

- 历史 changelog（`docs/changelog/changelog-v0.2.0.md`）与已结案文档中的历史叙述。
- closeout、归档审批、`Archived` / `Superseded` 状态或 `previous_plan_archive`
  的业务语义。
- 归档文件名 `IMPLEMENTATION_PLAN-<scope>.md` 与 `<scope>` 的 lower kebab-case 规则。

## 4. 实施步骤

1. 更新归档门禁 PRD/TRD 与 `AGENTS.md` 窄例外的路径描述。
2. 更新 `feature-implementor`、`trd-gen`、`idea-to-spec` 指令文件中的归档路径。
3. 更新 `check_repository_contract.py` 正则与目录构造，识别 `archive/` 新路径，
   并在 `previous_plan_archive` 纯路径迁移时判定内容未变。
4. 更新 `check_doc_contract.py` 与两个 contract 测试文件的路径与断言。
5. 更新 `feature-implementor` eval 定义与 eval-013 fixture 路径，迁移 fixture 归档。
6. 对 14 份跟踪归档执行 `git mv` 迁移，删除空 `implementation-plans/` 目录。
7. 同步 3 份 active 计划的 `previous_plan_archive` 到新路径。
8. 归档 #172 实施计划到 `archive/`（新路径真实案例验证），产出本计划。
9. 运行仓库四项契约脚本、contract 单测与 `git diff --check`。
10. 按 `skill-eval-runner` 执行受影响的 fresh paired eval 并更新 durable
    `comparison.md`。

## 5. 验证覆盖

- repository / eval / artifact / documentation 四项契约脚本全部 PASS。
- `scripts/test_check_repository_contract.py` 与 `agents/test_eval_contract.py`
  单测通过（旧路径 fixture 全部迁移）。
- `feature-implementor` fresh paired eval 完成且无未解释 FAIL。
- `git diff --check` 干净。
- 仓库中除明确保留的历史事实外，不再有会指导 Agent 生成旧路径的有效契约或断言。

## 6. 实施结果

### 6.1 代码与测试

- 归档路径契约迁移完成：14 份跟踪归档 + 1 份 eval fixture 归档 `git mv`
  到 `{feature_path}/archive/`，3 份 active 计划 `previous_plan_archive` 同步，
  空 `implementation-plans/` 目录已删除。
- `check_repository_contract.py` 正则、目录构造与校验消息全部识别新路径；
  `previous_plan_archive` 纯路径迁移（`implementation-plans/archive/` →
  `archive/`）在 base round 判定中视为内容未变。
- `check_doc_contract.py` 的归档工件识别收窄为精确 `IMPLEMENTATION_PLAN_ARCHIVE_RE`
  匹配，不再以 `/archive/` 子串误伤 feature_path 含 `archive` 段的合法文档。
- 针对性 repository contract pytest：`scripts/test_check_repository_contract.py`
  + `agents/test_eval_contract.py` + `scripts/test_run_skill_eval.py`
  合计 174 项通过。

### 6.2 Eval

受影响 target skill（feature-implementor、trd-gen、idea-to-spec）共 32 个 eval
执行 fresh paired 验证：

| Eval | Durable latest result |
| --- | --- |
| feature-implementor 17 个 | 15 PASS / PASS (partial)；eval-004、eval-006、eval-010 首次 FAIL 重跑确认模型方差后 PASS |
| trd-gen 6 个 | 5 PASS / PASS (partial)；eval-006 为既有 FAIL（main 上即 FAIL，与本次变更无关） |
| idea-to-spec 9 个 | 全部 PASS / PASS (partial) |

### 6.3 契约与格式

| Command | Result |
| --- | --- |
| `uv run scripts/check_repository_contract.py` | PASS |
| `uv run scripts/check_eval_contract.py` | PASS |
| `uv run scripts/check_eval_artifacts.py` | PASS |
| `uv run scripts/check_doc_contract.py` | PASS |
| pytest（174 项） | PASS |
| `git diff --check` | PASS |

## 7. 自审结论

- 存量迁移为纯 `git mv`，正文与 frontmatter 内容不变，仅路径变化；历史
  changelog 与已结案文档中的历史叙述保留当时事实。
- `archive/` 被结构治理识别为所属功能的历史存储（`structure-governance`
  指令已同步），不被识别为子功能。
- 已知边界：feature_path 本身可含 `archive` 段（lower kebab-case 语法允许），
  归档目录识别依赖 `IMPLEMENTATION_PLAN_ARCHIVE_RE` 精确匹配，不会把
  `{feature_path}/archive/IMPLEMENTATION_PLAN.md` 或 `TRD.md` 误判为归档工件。
- 未发现额外绕过或阻塞问题。
- 下一 owner 为 Engineer delivery：单次提交、普通 push、PR 评论并触发
  `@codex review`；不等待 review，不合并 PR。
