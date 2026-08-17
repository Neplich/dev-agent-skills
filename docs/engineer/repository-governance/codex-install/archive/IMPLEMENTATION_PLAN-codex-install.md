---
title: "Codex 安装器统一全量安装实施计划"
type: IMPLEMENTATION_PLAN
version: "0.2.0"
status: Archived
author: "Neplich Claude"
date: "2026-08-17"
last_updated: "2026-08-17"
generated_by: "feature-implementor"
feature: "codex-install"
feature_path: "repository-governance/codex-install"
parent_feature: "repository-governance"
feature_level: "2"
change_tier: "standard"
implementation_scope: "codex-install"
related_prd: "N/A"
related_trd: "N/A"
related_issue: "https://github.com/Neplich/dev-agent-skills/issues/288"
approved_by: "Neplich"
approved_at: "2026-08-17"
archived_at: "2026-08-17"
archive_approved_by: "Neplich"
source_plan: "docs/engineer/repository-governance/codex-install/IMPLEMENTATION_PLAN.md"
changelog:
  - version: "0.2.0"
    date: "2026-08-17"
    changes: "用户确认后完成实施、独立验收 ACCEPT 与 closeout；全部验证通过"
  - version: "0.1.0"
    date: "2026-08-17"
    changes: "初始版本，定义移除 Codex 安装器 routers-only 策略、统一全量安装的实施范围"
---

# Codex 安装器统一全量安装实施计划

## 1. 对齐与计划门禁

| 字段 | 结果 |
| --- | --- |
| `feature_path` | `repository-governance/codex-install` |
| `parent_feature` | `repository-governance` |
| `feature_level` | `2` |
| `change_tier` | `standard`；单功能行为变更（安装策略收敛），跨安装器、测试与多份文档引用 |
| `change_map_path` | `N/A`；仓库不存在 `docs/site/standards/change-map.yaml` |
| `matched_code_glob` | `N/A` |
| `mapped_docs` | `N/A`；本 feature 无 PRD/TRD 文档树，已确认规格来源为 GitHub issue #288 |
| `prd_alignment` | `issue_based`；PM 已分类为 existing_update、standard tier，issue #288 为已确认需求来源，不补建 PRD 文档树 |
| `trd_alignment` | `issue_based`；改动为既有行为的删除式收敛，issue #288 与本计划共同构成技术规格，不补建 TRD |
| UI / Design | `N/A`；不改变 UI、交互、视觉或信息层级，不创建 Design 交付物 |
| 活跃计划扫描 | 写入前 `docs/engineer/repository-governance/codex-install/IMPLEMENTATION_PLAN.md` 不存在 |
| `active_plan_status` | `N/A`；新 feature path 无旧活跃计划 |
| `active_plan_scope_before` | `N/A` |
| 归档扫描 | 写入前 `docs/engineer/repository-governance/codex-install/archive/` 不存在，无历史 backlink |
| `replacement_plan_scope` | `codex-install` |
| `active_entry_rule` | 实施期间固定使用本文件；完成 closeout 后只移动到 `archive/` 子目录冻结归档 |
| `archive_state` | `new_feature_no_history` |
| `decision` | 用户已于 2026-08-17 确认本计划；实施与独立验收已完成 |
| `receiving_owner` | `engineer-agent:feature-implementor` |
| `gap_packet` | `N/A`；无 PRD、TRD 或 Design gap |
| `subagent_split` | `enabled`；实现委派 codex CLI（代码改动超过 50 行），验收由独立 validation sub-agent 完成（结论 ACCEPT） |
| `confirmation_required` | 已满足；用户已确认本计划 |
| `blocked_downstream_actions` | PR 合并；本计划不授权 merge、tag、Release、仓库设置或部署变更 |

QA E2E 不适用：本变更不影响用户界面流程，属于仓库工具链改动，不产生 QA E2E 移交包，
不创建或更新 `docs/qa/e2e/` 测试用例。若实现证据推翻该判断，停止并先由主进程补充
QA handoff；不得由实施 subagent 自行扩大范围。

## 2. 背景与目标

`scripts/install_codex_skills.py` 的 `--routers-only` 只在目标根目录暴露 7 个 role
router，specialist 仅存在于隐藏镜像中，不会被 Codex 注册为可调用 Skill，导致 router
路由到 specialist 时按"目标能力未安装"停止。本变更移除该策略，统一为全量安装：
安装器只保留一种安装形态（隐藏镜像 + 目标根目录全量软链），用户不再面对范围选择。

## 3. 成功标准与规模

1. 安装器不再存在 `--routers-only` 参数、`routers_only` 传参链路、unselected 扫描与
   输出段；`select_skill_specs` 恒返回全部 specs。
2. 默认安装器对旧 routers-only 受管安装（镜像完整、目标根目录仅 7 个 router 软链）
   重跑后自动补齐全部 specialist 软链，由新增升级回归测试证明；不新增迁移代码。
3. `.codex/INSTALL.md`、`docs/README.codex.md`、maintain-skills 两份 reference、两份
   TRD 中所有 routers-only 引用按第 4 节收敛或删除。
4. 第 6 节全部验证命令通过，包括安装器测试全绿与仓库契约检查。

规模预期：净删除约 100–150 行（issue 预估 40–100 行，因测试与文档引用点比 issue
列出的多，实际略超；属于同一删除性质，不新增抽象）。不新增抽象层、配置项、兼容
开关、重试、缓存、feature flag 或迁移逻辑；实际偏离明显时先停下核对范围。

## 4. 精确改动清单（按依赖顺序）

### 4.1 `scripts/install_codex_skills.py`（净删除约 60 行）

- `parse_args`：删除 `--routers-only` 参数定义。
- `select_skill_specs(specs, routers_only)`：删除 `routers_only` 参数，函数体收敛为
  返回全部 specs；空列表错误信息收敛为单一路径，不再区分模式。
- `PreflightPlan`：删除 `unselected_remove`、`unselected_skipped` 字段。
- `build_preflight_plan(...)`：删除 `routers_only` 参数与 `if routers_only:` 的
  unselected 扫描分支（约 310–326 行）。
- `render_results(...)`：删除 `routers_only` 参数、`--routers-only` 警告块和
  unselected 两个输出段（约 638–658 行）。
- `main()`：删除 `args.routers_only` 的三处传参与 `plan.unselected_remove` 的删除
  循环。
- 注意：旧 routers-only 受管安装重跑默认安装器时，缺失的 specialist 软链会被正常
  创建（`install_selected_skill` 的新建路径），无需新增迁移代码。

### 4.2 `scripts/test_install_codex_skills.py`（净删除约 50 行 + 新增约 25 行）

- 删除 `test_routers_only_links_only_router_skills_but_keeps_full_hidden_mirror`。
- 删除 `test_switching_to_routers_only_removes_previously_managed_specialist_links`。
- 删除 `test_force_errors_on_unowned_unselected_directory_without_partial_changes`
  （routers-only 移除后 debugger 变为 selected，与既有
  `test_force_errors_on_unowned_selected_directory_without_partial_changes` 覆盖
  重复）。
- 删除不再被引用的 `router_skill_names()` helper。
- `test_generated_shared_contracts_are_reachable_in_full_and_router_mirrors`：去掉对
  `("--routers-only",)` 模式的循环，只保留全量安装单次执行，测试名改为
  `test_generated_shared_contracts_are_reachable_in_mirror`。
- 新增升级回归测试：先全量安装，再手动删除目标根目录下全部非 router 的受管软链
  （模拟旧 routers-only 受管安装状态：镜像 + 仅 7 个 router 软链），重跑默认安装
  器，断言 `scanned_skill_entries(target) == marketplace_skill_names()` 即全部
  specialist 被补齐。
- 沿用既有测试写法（`run_installer`、`tmp_path`、断言风格），不新增测试辅助抽象。

### 4.3 `.codex/INSTALL.md`

删除 "Before You Install" 的问题 2（routers-only 选择）、第 24–29 行的 routers-only
说明段、第 131–141 行的受限模式安装小节；保留 personal/project 范围选择。

### 4.4 `docs/README.codex.md`

删除第 16 行问题 2、第 28 行 routers-only 段落、第 131–137 行受限模式小节。

### 4.5 `.agents/skills/maintain-skills/references/sync-surfaces.md`

第 11 行：删除括号内 ``install_codex_skills.py` `--routers-only` relies on the
equality` 的失效依据；router 名 = plugin 名的规则本身保留。

### 4.6 `.agents/skills/maintain-skills/references/change-types.md`

第 30–32 行：删除 `--routers-only` recognizes routers by that equality 的失效理由；
规则保留，理由改写或收敛为契约要求。

### 4.7 `docs/engineer/agents/docs-agent/release-notes-gen/TRD.md`

第 236 行：安装器回归断言清单中删除 routers-only。

### 4.8 `docs/engineer/repository-governance/document-authority/TRD.md`

第 204 行与第 327 行：验证面中"另测 --routers-only"/"完整与 routers-only 临时目标"
收敛为仅全量安装。

### 4.9 `skills-lock.json`（条件性）

若 maintain-skills 在 `skills-lock.json` 中有条目且 `computedHash` 因 references
改动过期（`uv run scripts/check_repository_contract.py` 报 stale），按仓库既有方式
刷新对应条目哈希。该刷新与 references 改动属于同一变更，不算范围外文件。

## 5. 明确不改

- 根 `README.md` / `README_zh.md`（已核实无 routers-only 引用）。
- `docs/architecture.md`（第 54–55 行的描述"复制完整 Agent 树到隐藏镜像再暴露
  Skill 目录"在改动后仍然准确）。
- 已归档的 `archive/IMPLEMENTATION_PLAN-document-authority.md`（历史记录不动）。
- 7 个 Agent 角色边界、PM-first 路由规则、specialist gate、Claude/Kimi 插件注册。
- 不新增任何抽象、配置项或兼容开关。

## 6. 验证（按序执行，全部通过才算完成）

1. `uv run --with pytest pytest scripts/test_install_codex_skills.py` — 全绿。
2. `uv run scripts/install_codex_skills.py --target <临时目录>` — 实测全量安装，
   确认无 routers-only 相关输出。
3. `uv run scripts/generate_shared_contracts.py --check`。
4. `uv run scripts/check_repository_contract.py`。
5. `uv run scripts/check_doc_contract.py`。
6. `git diff --check`。

## 7. Sub-agent 分工与验收

- 实现：委派 codex CLI 执行（用户全局规则：代码改动超过 50 行委派 codex）；委派
  prompt 逐条列出第 4 节改动与第 5 节禁令。codex 沙箱对 `.codex/` 与 `.agents/`
  只读，这 3 个文件的文档删除（合计约 10 行）由主进程直接完成，其余 5 个文件由
  codex 完成。
- 验收：独立 validation sub-agent 对照 issue #288 验收标准、本计划、测试结果与
  仓库规则复核 diff，结论 ACCEPT（8 个文件与计划逐条对应、无残留、无计划外抽象）。
- 完成 closeout 后本文件移入
  `docs/engineer/repository-governance/codex-install/archive/` 冻结归档。

## 8. Closeout

- `changed_files`：`scripts/install_codex_skills.py`、`scripts/test_install_codex_skills.py`、
  `.codex/INSTALL.md`、`docs/README.codex.md`、
  `.agents/skills/maintain-skills/references/sync-surfaces.md`、
  `.agents/skills/maintain-skills/references/change-types.md`、
  `docs/engineer/agents/docs-agent/release-notes-gen/TRD.md`、
  `docs/engineer/repository-governance/document-authority/TRD.md`，
  合计 +46/-162（净删除 116 行，落在预估区间）。
- `commands_and_results`：
  `uv run --with pytest pytest scripts/test_install_codex_skills.py` 23 passed；
  临时目录实测默认安装暴露全部 39 个 marketplace Skill 且无 routers-only 输出，
  `--routers-only` 参数实测被拒绝（unrecognized arguments）；
  `uv run scripts/generate_shared_contracts.py --check` fresh；
  `uv run scripts/check_repository_contract.py` PASS（skills-lock.json 不含
  maintain-skills 条目，无需刷新，未改动）；
  `uv run scripts/check_doc_contract.py` PASS；`git diff --check` 干净。
- `residual_risks`：`.codex/INSTALL.md` 保留 "Default all skills:" 小节标题（事实
  仍准确，属可选措辞优化）；已使用旧 routers-only 安装的环境在下次默认安装时会
  补齐全部 specialist 软链（预期行为，由升级回归测试覆盖）。
- `runtime_artifacts_removed`：委派 prompt 与 codex 输出均落于 /tmp，未进 Git；
  临时安装目录已删除；仓库内无运行时产物。
- 下一 owner：delivery（commit、push、PR），issue #288 随 PR 合并关闭。
