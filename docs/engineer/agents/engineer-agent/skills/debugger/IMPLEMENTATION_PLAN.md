---
title: "debugger 只读诊断模式实施计划"
type: IMPLEMENTATION_PLAN
version: "0.5.0"
status: "Implemented"
author: "Neplich Codex"
date: "2026-08-13"
last_updated: "2026-08-13"
generated_by: "feature-implementor"
feature: "skill-debugger"
feature_path: "agents/engineer-agent/skills/debugger"
parent_feature: "agents/engineer-agent/skills"
feature_level: "4"
implementation_scope: "diagnosis-only-mode"
change_tier: "major"
related_issue: "https://github.com/Neplich/dev-agent-skills/issues/274"
related_prd: "docs/pm/agents/engineer-agent/skills/debugger/PRD.md"
related_trd: "docs/engineer/agents/engineer-agent/skills/debugger/TRD.md"
changelog:
  - version: "0.5.0"
    date: "2026-08-13"
    changes: "按 PR review 同步权威 diagnosis-only handoff 可选扩展，并刷新 idea-to-spec eval"
  - version: "0.4.0"
    date: "2026-08-13"
    changes: "完成实现、32 条 fresh eval、独立验收与交付前确定性门禁"
  - version: "0.3.0"
    date: "2026-08-13"
    changes: "记录计划已确认且静态实施与独立验收完成，等待单独授权 32 条 fresh eval"
  - version: "0.2.0"
    date: "2026-08-13"
    changes: "补充 PM 入口正反例确定性测试，并明确 diagnosis_only supplemental fields 不扩展通用 handoff schema"
  - version: "0.1.0"
    date: "2026-08-13"
    changes: "初始草案，定义 debugger 双模式、路由同步、四条新增 eval 与 32 条 fresh 范围"
---

# debugger 只读诊断模式实施计划

## 1. 实施上下文与门禁

本计划承接 Issue #274，在现有 `debugger` 中增加 `diagnosis_only`，并同步
`pm-agent` 与 `engineer-agent` 路由。PRD、DECISIONS 与 TRD 使用同一
`feature_path: agents/engineer-agent/skills/debugger`；TRD 的 `related_prd` 指向同路径
PRD。

本功能路径此前没有活动 `IMPLEMENTATION_PLAN.md`，也没有 `archive/` 历史，因此不触发
归档选择，本文从 `v0.1.0` 开始且不声明 `previous_plan_archive`。

变更跨越 PM 与 Engineer 两个角色的路由和行为契约，并修改三项 skill eval，按仓库规则
分类为 `major`。用户已确认本精确计划及后续模型执行；skill、README、eval、lockfile、
32 条 fresh eval、独立验收和交付前门禁均已完成。

## 2. 目标实施边界

- 复用现有 `debugger`，增加 `diagnosis_only` 与既有 `repair` 双模式。
- 只读 handoff 使用 `mode: diagnosis_only`、`allowed_mutations: none`。
- 缺 PRD/TRD 不阻断客观调查，但输出必须标记预期未对齐，不能确认实现偏差。
- 报告包含事实、证据、根因与置信度、影响、未知项和最小下一步，然后停止。
- 后续修复重新进入完整 PM/Engineer、PRD/TRD、repair plan confirmation 和验证门禁。

## 3. 精确文件范围

### 3.1 文档链

| Path | Operation |
| --- | --- |
| `docs/pm/agents/engineer-agent/skills/debugger/PRD.md` | 更新至 v1.2.0，定义双模式产品契约。 |
| `docs/pm/agents/engineer-agent/skills/debugger/DECISIONS.md` | 新建 v1.0.0，记录最终决策。 |
| `docs/engineer/agents/engineer-agent/skills/debugger/TRD.md` | 新建 v1.0.0，定义 handoff、权限和验证设计。 |
| `docs/engineer/agents/engineer-agent/skills/debugger/IMPLEMENTATION_PLAN.md` | 新建本活动计划。 |

### 3.2 Skill 与路由文档

| Path | Operation |
| --- | --- |
| `agents/product_manager/skills/pm-agent/SKILL.md` | 仅在用户明确只读意图时构造零修改 Engineer handoff；`mode` / `allowed_mutations` 是 `diagnosis_only` 专属 supplemental fields，不修改 `idea-to-spec` `skill-map.md` 的通用 required fields。 |
| `agents/product_manager/skills/idea-to-spec/_internal/_shared/skill-map.md` | 按 PR review 登记 diagnosis-only 条件性可选扩展及预期未对齐的只读 Engineer 路由；不升级为通用 required fields。 |
| `agents/engineer/skills/engineer-agent/SKILL.md` | 将只读模式路由到现有 `debugger` 并保留约束字段。 |
| `agents/engineer/skills/debugger/SKILL.md` | 增加 `diagnosis_only` 流程、报告契约和修复重新入场门禁。 |
| `agents/product_manager/README.md`, `agents/product_manager/README_zh.md` | 同步 PM bug_report 只读路由说明。 |
| `agents/engineer/README.md`, `agents/engineer/README_zh.md` | 同步 debugger 双模式说明。 |

### 3.3 Eval、fixture 与 lockfile

| Path | Operation |
| --- | --- |
| `agents/product_manager/test/pm-agent/evals/evals.json` | 新增 `eval-020-route-read-only-diagnosis`。 |
| `agents/engineer/test/engineer-agent/evals/evals.json` | 新增 `eval-005-route-read-only-diagnosis`。 |
| `agents/engineer/test/debugger/evals/evals.json` | 新增 `eval-006-diagnosis-only-without-product-docs` 与 `eval-007-repair-after-diagnosis-reenters-gates`。 |
| 对应 `evals/workspace/<eval-id>/` | 增加必要 fixture、`eval_metadata.json` 与 runner 生成的 `comparison.md`。 |
| `agents/product_manager/test/pm-agent/test_pm_entry_eval.py` | 新增约 15–30 行确定性正反例断言：明确“只读/不要修”产生 `diagnosis_only` / `allowed_mutations: none`；模糊“查一下/为什么挂了”不得自动推断零修改模式。 |
| `skills-lock.json` | 刷新 `pm-agent`、`engineer-agent`、`debugger` 三项 `computedHash`。 |

## 4. 实施顺序

1. 修改 `pm-agent`：只在 `bug_report` 包含明确只读意图时传递
   `mode: diagnosis_only` 与 `allowed_mutations: none`；模糊“查一下”“为什么挂了”保持普通
   bug_report，不推断零修改模式。两个字段仅为该模式的 supplemental fields，不改变
   request_type 枚举或 `idea-to-spec` `skill-map.md` 的通用 required fields。
2. 修改 `engineer-agent`：以现有 `debugger` 为唯一主 route，保留只读约束，不要求先补齐
   仅供修复使用的 PRD/TRD。
3. 修改 `debugger`：在现有 repair checkpoint 之前分流模式；为只读模式定义允许操作、
   预期对齐状态、报告结构和停止条件；保持 repair 流程原文语义。
4. 同步 Product Manager 与 Engineer 双语 README，不改 skill 数量、注册或顶层入口。
5. 在 `test_pm_entry_eval.py` 增加约 15–30 行正反例确定性断言，锁定明确与模糊诊断意图
   的分界。
6. 按 skill-eval-runner authoring 契约增加四条真实用户场景 eval、最小 fixture 和 metadata；
   不手工创建结论。
7. 刷新三项 skill lock hash，运行确定性契约与测试。
8. 已向用户报告静态结果，并取得 32 条模型 eval 的单独授权。
9. 已以单一 runner 进程执行 32 条 fresh；仅重试 BLOCKED、timeout 或 incomplete，未重跑
   已完成 verdict。
10. 已清理运行期产物，复跑契约、summary 和差异检查，并完成计划 closeout。

## 5. Sub-Agent 分工

本变更涉及三项 skill、三个 eval target 和跨角色契约，采用复杂任务分工：

- 实现 sub-agent：只负责计划列出的 skill、README、PM 入口确定性测试、eval definitions、
  fixtures、metadata 和 lockfile；不得修改文档链、runner/checker 或注册面。
- 独立验收 sub-agent：对照 PRD、DECISIONS、TRD、Issue #274 与最终 diff，验证只读边界、
  repair re-entry、四条 eval、32 条 freshness 范围和禁止区。
- 主进程：审查文档与实现、处理 eval 结果和范围变化、决定交付状态。

## 6. 规模预估

- 权威文档净增约 300–420 行。
- 三项 SKILL 与四份双语 README 净增约 70–120 行。
- PM 入口确定性测试净增约 15–30 行。
- 四条 eval 定义、fixtures、metadata 和 runner 生成的 comparison 净增约 335–490 行。
- 总净增预计约 720–1,060 行；除约 15–30 行确定性 Python 测试外不新增生产
  Python/JavaScript 代码，不新增抽象、配置或 feature flag。若实际超过约 1,100 行，停止
  实施并重新确认范围。

## 7. 验证命令

实施前后执行：

```bash
uv run scripts/check_repository_contract.py
uv run scripts/check_eval_contract.py
uv run scripts/check_eval_artifacts.py
uv run scripts/check_doc_contract.py
uv run --with pytest pytest agents/product_manager/test/pm-agent/test_pm_entry_eval.py agents/test_eval_contract.py scripts/test_run_skill_eval.py scripts/test_eval_execution.py scripts/test_eval_persistence.py
uv run scripts/summarize_eval_results.py
git diff --check
git status --short
test ! -d tmp/eval-runs
```

新增四条 eval 后，三项 target skill 共 32 条 fresh：`pm-agent` 20、
`engineer-agent` 5、`debugger` 7。模型执行已单独获得授权，并通过一个
`run_skill_eval.py` 进程、最多 10 workers、32 个精确目标完成。

## 8. 禁止区

- 不新增 `diagnose-only`、`diagnosis-only` 或其他平行 skill、目录、注册项。
- 不削弱 debugger 现有 expected-behavior checkpoint、repair plan confirmation、最小修复
  和验证门禁。
- 不修改 `.claude-plugin/marketplace.json`、Agent plugin manifest、根 README、
  `AGENTS.md`、发布版本或 changelog。
- 不修改 eval runner、checker、identity schema、migration inventory 或 migration audit。
- `mode` / `allowed_mutations` 只在权威 `skill-map.md` 中作为 diagnosis-only 条件性可选扩展，
  不进入通用 handoff required fields。
- 不手工编辑 `comparison.md` 冒充 fresh，不复用 stale verdict。
- `diagnosis_only` 不得修改源码、测试、E2E、配置、数据库或任何外部状态，不得执行
  commit、push、PR。
- 不创建 QA E2E 用例；若后续 repair 影响用户流程，只在修复完成后交给 QA。

## 9. 完成标准

- PM 和 Engineer 均能把明确只读 bug_report 路由到现有 debugger。
- 无 PRD/TRD 的只读诊断能给出证据分层报告，并保持零修改。
- 诊断后的修复请求重新进入完整门禁。
- 四项 contract、针对性 pytest、summary 和 diff check 通过。
- 获得单独授权后，32 条 comparison 均为 fresh，结果中的任何 FAIL 都完成归因。
- `tmp/eval-runs` 与其他运行期产物为零。

## 10. 实施结果

### 10.1 文件与行为

- `pm-agent` 仅对明确“只读 / 只诊断 / 不要修”意图添加
  `mode: diagnosis_only` 与 `allowed_mutations: none`，并在 handoff 中逐项列出代码、测试、
  E2E、配置、数据库、外部状态、commit、push 与 PR 的禁止边界；模糊调查表达保持普通
  `bug_report`。
- `engineer-agent` 保留只读字段并唯一主路由到现有 `debugger`；缺 PRD/TRD 不阻断客观
  诊断，后续修复重新进入正常门禁。
- `debugger` 在 repair checkpoint 前完成双模式分流，交付结构化只读报告后停止；既有
  repair 流程、预期对齐与 repair-plan confirmation 未削弱。
- Product Manager / Engineer 双语 README、四条新增 eval、PM 入口正反例测试及三项
  `skills-lock.json` hash 已同步；未修改 marketplace、plugin manifest、通用 handoff
  schema、eval 基础设施或冻结 inventory。
- PR review 指出的共享契约缺口已修复：`skill-map.md` 现登记 diagnosis-only 的条件性可选
  字段、完整零修改边界和未对齐只读路由例外；`idea-to-spec` 9 条 eval 已 fresh。

### 10.2 验证结果

| Check | Result |
| --- | --- |
| `uv run scripts/check_repository_contract.py` | PASS |
| `uv run scripts/check_eval_contract.py` | PASS；200 份 comparison 均满足 schema v2 与 freshness 契约 |
| `uv run scripts/check_eval_artifacts.py` | PASS |
| `uv run scripts/check_doc_contract.py` | PASS |
| `uv run --with pytest pytest -q agents/product_manager/test/pm-agent/test_pm_entry_eval.py agents/test_eval_contract.py scripts/test_run_skill_eval.py scripts/test_eval_execution.py scripts/test_eval_persistence.py` | PASS；131 passed、6 subtests passed |
| `uv run scripts/summarize_eval_results.py` | PASS；200 comparisons = 133 PASS、49 partial、18 FAIL |
| `git diff --check` | PASS |
| `test ! -d tmp/eval-runs` | PASS |

### 10.3 Fresh eval 结论

- 计划范围 32 条均已 fresh：`pm-agent` 20、`engineer-agent` 5、`debugger` 7。
- #274 新增场景全部 PASS：
  `pm-agent/eval-020-route-read-only-diagnosis`、
  `engineer-agent/eval-005-route-read-only-diagnosis`、
  `debugger/eval-006-diagnosis-only-without-product-docs`、
  `debugger/eval-007-repair-after-diagnosis-reenters-gates`。
- 受影响三组中保留四条与 #274 无关的有效 FAIL：
  `pm-agent/eval-010-change-tier-hotfix-fast-lane`、
  `engineer-agent/eval-001-route-implementation-chain`、
  `engineer-agent/eval-002-existing-feature-alignment-gate`、
  `debugger/eval-005-mapped-cache-debug-evidence`。这些结果分别涉及 scope guard、既有实现链
  路由、用户行为基线复述和 mapped-doc trust discipline；均不涉及 diagnosis-only 新路径，
  不在本 Issue 中弱化断言或扩大修复范围。
- PR review 修复后，`idea-to-spec` 9 条也已 fresh：7 PASS、2 partial；其中
  `eval-008-mapped-notification-update` 保留一个 mapped-doc-first 读取顺序的有效 FAIL。
  该失败与 diagnosis-only 可选扩展无关，不在本 PR 中弱化断言或扩大范围。

### 10.4 独立验收与遗留风险

- 独立验收未发现 P0/P1/P2；确认零修改边界、unaligned 结论、repair re-entry、README/
  lock 同步和禁止区均符合 PRD/TRD。
- 无运行期 eval 产物残留，无 QA E2E handoff 需求。
- 最终净增约 1,240 行，比约 1,100 行停审线高 140 行；偏差来自 32 条 fresh
  `comparison.md` 的实际 durable evidence 长度，不新增文件类别、实现行为或抽象。维护者已授权
  后续流程默认继续到 PR 合并前，因此接受该机械证据增量。
- 下一 owner：维护者审查 PR；上述四条无关 fresh FAIL 可作为后续独立 issue 的输入。
