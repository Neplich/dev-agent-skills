---
title: "Eval 既有缺陷清理实施计划"
type: IMPLEMENTATION_PLAN
version: "0.5.0"
status: Archived
author: "Neplich Codex"
date: "2026-08-12"
last_updated: "2026-08-12"
generated_by: "feature-implementor"
feature: "eval-scenario-isolation"
feature_path: "repository-governance/eval-scenario-isolation"
parent_feature: "repository-governance"
feature_level: "2"
implementation_scope: "eval-existing-defect-cleanup"
archived_at: "2026-08-15"
archive_approved_by: "Neplich"
source_plan: "docs/engineer/repository-governance/eval-scenario-isolation/IMPLEMENTATION_PLAN.md"
change_tier: "major"
related_issue: "#277"
related_prd: "docs/pm/repository-governance/eval-scenario-isolation/PRD.md"
related_trd: "docs/engineer/repository-governance/eval-scenario-isolation/TRD.md"
previous_plan_archive: "docs/engineer/repository-governance/eval-scenario-isolation/archive/IMPLEMENTATION_PLAN-eval-scenario-isolation-refactor.md"
changelog:
  - version: "0.5.0"
    date: "2026-08-12"
    changes: "完成 identity schema v2、协议模块拆分、187 份机械迁移、runner/checker 与 skill 修复、25 条受影响 fresh eval 和独立验收；Issue #277 目标通过，保留无关 PM eval-016 FAIL 为后续缺陷"
  - version: "0.4.0"
    date: "2026-08-12"
    changes: "维护者确认 v0.3.0 实施计划，解除 schema v2、模块拆分、迁移器、确定性测试与一次性 comparison 迁移门禁；模型 eval 仍未授权"
  - version: "0.3.0"
    date: "2026-08-12"
    changes: "按维护者授权加入 identity schema v2、协议模块边界、196 份 comparison 一次性迁移与 9 条 fresh 回归；扩大后的计划等待再次确认"
  - version: "0.2.0"
    date: "2026-08-12"
    changes: "维护者确认按计划实施，解除代码、测试、skill、eval 定义与 lockfile 修改门禁；模型 eval 仍需单独授权"
  - version: "0.1.0"
    date: "2026-08-12"
    changes: "初始草案，定义冻结后 eval 持久化、严格检查与 trd-gen eval-006 混合缺陷"
---

# Eval 既有缺陷清理实施计划

## 1. 实施上下文与门禁

本计划承接 Issue #277，处理冻结后新增 PM scope-guard eval 的持久化缺陷、`trd-gen`
eval-006 的混合缺陷，并按维护者确认的 schema v2 方案收敛 durable identity、协议模块边界
与一次性 comparison 迁移。该范围改变仓库级 eval identity 和 checker 契约，按仓库分级为
`major`。

来源文档已经对齐：PRD `1.4.0`、DECISIONS `1.3.0` 与 TRD `1.5.0` 使用相同
`feature_path`、`parent_feature`、`feature_level`，TRD `related_prd` 指向同路径 PRD。
原 `eval-scenario-isolation-refactor` 计划已按维护者批准归档，新活动入口保持为本文路径。

维护者已于 2026-08-12 确认 v0.3.0 实施计划，schema v2、模块拆分、迁移器、确定性测试与
一次性 comparison 迁移门禁已解除。模型 eval 消耗模型时间并改写 fresh comparison，仍未
授权；本次计划确认不视为模型运行授权。QA E2E、创建 PR 和关闭 Issue #277 继续等待实施
与验收完成。

### 1.1 Planning checkpoint

| 字段 | 值 |
| --- | --- |
| `feature_path` | `repository-governance/eval-scenario-isolation` |
| `parent_feature` | `repository-governance` |
| `feature_level` | `2` |
| `change_map_path` | `N/A`（仓库无 `docs/site/standards/change-map.yaml`） |
| `matched_code_glob` | `N/A` |
| `mapped_docs` | PRD `1.4.0`、DECISIONS `1.3.0`、TRD `1.5.0` |
| `prd_alignment` | `already_approved`：Issue #277 的 inventory、混合缺陷与 identity v2 已写入 PRD/DECISIONS |
| `prd_path` | `docs/pm/repository-governance/eval-scenario-isolation/PRD.md` |
| `trd_alignment` | `already_approved`：TRD 已定义 0/1/>1、协议模块、v2-only checker 与一次性迁移 |
| `trd_path` | `docs/engineer/repository-governance/eval-scenario-isolation/TRD.md` |
| `active_plan_path` | `docs/engineer/repository-governance/eval-scenario-isolation/IMPLEMENTATION_PLAN.md` |
| `active_plan_status` | `Draft` |
| `active_plan_scope_before` | `eval-scenario-isolation-refactor` |
| `replacement_plan_scope` | `eval-defect-cleanup` |
| `archive_directory` | `docs/engineer/repository-governance/eval-scenario-isolation/archive/` |
| `active_entry_rule` | 活动入口固定为 `IMPLEMENTATION_PLAN.md`；历史计划只在 `archive/` |
| `archive_state` | 原计划已归档为 `IMPLEMENTATION_PLAN-eval-scenario-isolation-refactor.md` |
| `decision` | 维护者选择“完成态归档后创建新计划” |
| `receiving_owner` | `engineer-agent:feature-implementor` |
| `gap_packet` | `N/A` |
| `planned_files` | 第 3 节列出的协议/identity/persistence 模块、checker、迁移器、测试、audit、skill、eval、lockfile 与 196 份 comparison |
| `verification_commands` | 第 5 节命令 |
| `subagent_split` | 启用；实现与独立验收分离，主进程保留集成与交付判断 |
| `blocked_downstream_actions` | 模型 eval、QA E2E、交付、PR 和 issue closeout 仍阻塞 |
| `confirmation_required` | v0.3.0 已确认；模型 eval 另需明确授权且当前未授权 |
| `qa_e2e_tc_create_or_update` | `blocked_until_plan_confirmed`；本变更预计无需新增 E2E TC |
| `qa_e2e_source_after_confirmation` | 本文路径 |
| `qa_e2e_handoff_package_after_implementation` | PRD/TRD/计划路径已知；changed files、测试结果与风险待实施后填写；建议目录 `docs/qa/e2e/repository-governance/eval-scenario-isolation/` |

## 2. 成功标准与收紧边界

1. `migration-inventory.json` 保持 schema `1.0`、193 条冻结记录和 counts，无内容 diff。
2. Durable writer 对 retained identity 实现零匹配只写 comparison、唯一匹配同步更新、
   多匹配拒绝写入，并有确定性回归测试。
3. `check_eval_contract.py` 对全部当前常规 eval 使用同一严格输入契约，不以 complete inventory
   identity 决定 scenario、metadata、runtime isolation 或 fixture 的校验强度。
4. `trd-gen` eval-006 允许完成 TRD 后在交付摘要中提示合法下一阶段，但要求 `trd-gen`
   自己完成本轮 TRD，且 TRD 正文不写 routing；正文归一化、frontmatter changelog 与不进入
   实现三项要求保持不变。
5. `trd-gen` 交付前自检明确验证正文没有旧方案状态标注，删除记录位于 frontmatter
   changelog；skill 职责、路由和 discovery 不改变。
6. Schema v2 只包含七字段：`target_skill_sha256`、`eval_definition_sha256`、
   `metadata_sha256`、`fixture_sha256`、`execution_protocol_sha256`、
   `runtime_protocol_sha256`、`judge_schema_sha256`；完整源码 manifest 只锁同轮 drift。
7. 一次性迁移将 196 份常规 comparison 分类为 187 机械迁移、trd-gen 6 stale、PM 3 PENDING；
   manual-only 1 份不迁移。187 份 verdict/evidence 与 807 条 assertion 逐字保持。
8. 四项静态 contract、受影响 pytest、summarizer、whitespace 检查通过；模型获授权后，
   9 个目标 eval 各产生一份 fresh durable comparison，runtime artifact 为零。

预计机械移动约 900 至 1100 行，手写净新增约 350 至 550 行；移动只用于形成确认的模块
边界。模型运行另更新 9 份 comparison。不新增额外抽象层、永久兼容桥、重试、缓存、配置项、
feature flag、hook、监控或日志层。实际量级明显超出时停止并重新确认范围。

## 3. 文件范围

| 路径 | 操作 | 计划内容 |
| --- | --- | --- |
| `scripts/run_skill_eval.py` | 修改 | 收敛为薄 CLI、target selection 与 orchestration；保留单轮源码 manifest 锁入口。 |
| `scripts/eval_execution.py`、`scripts/eval_judging.py` | 新增 | 分别承接 candidate/evidence 与 judge/schema/Overall，形成 execution protocol。 |
| `scripts/eval_runtime.py` | 修改 | 保留 fixture、lane、Git/HOME/CODEX_HOME、preflight、cleanup，形成 runtime protocol。 |
| `scripts/eval_persistence.py`、`scripts/eval_identity.py` | 新增 | 分离 durable comparison/inventory 与 schema v2 identity；persistence 不进入跨版本 freshness。 |
| `scripts/check_eval_contract.py` | 修改 | 迁移后单轨严格校验 schema v2；正常路径不调用 Git、不兼容 v1。 |
| `scripts/migrate_eval_identity_v2.py`、migration audit JSON | 新增 | 一次性核验来源、分类、逐字保持并原子迁移；audit 记录实际旧 hash/source commit。 |
| 相关 4 至 5 份测试 | 新增/修改 | 覆盖协议 hash、0/1/>1、source drift、v2-only checker、原子迁移和逐字 evidence。 |
| `agents/engineer/skills/trd-gen/SKILL.md` | 修改 | 强化 current-state TRD 交付前自检，不改变 handoff 和角色边界。 |
| `agents/engineer/test/trd-gen/evals/evals.json` | 修改 | 收窄 eval-006 的 ownership/handoff 断言，保留其余三项要求。 |
| `skills-lock.json` | 修改 | 刷新 `trd-gen` 的 `computedHash`。 |
| 196 份常规 `comparison.md` | 迁移器/runner 更新 | 187 机械迁移、6 stale、3 PENDING；模型另授权后对后两组共9条 fresh。 |
| 本活动计划 | closeout 更新 | 实施后记录 changed files、命令结果、残余风险和 runtime 清理。 |

禁止修改：

- `docs/engineer/repository-governance/eval-scenario-isolation/migration-inventory.json` 的任何 bytes，以及 manual-only `manual-gen` evaluation result；
- marketplace、plugin manifest、router、README、AGENTS.md 与 discovery 描述；
- PM eval-017/018/019 的定义、metadata 和 fixture，除非 fresh 诊断证明其自身另有缺陷并重新确认；
- 无关 FAIL、comparison、skill、测试和过程文档；
- `tmp/eval-runs/` 或任何 transcript、output、snapshot、judge verdict、timing、diagnostics、
  run status、`comparison.auto.md`。

## 4. 实施顺序

1. **先写持久化与 checker 回归测试**
   - 验证零匹配时 comparison 更新且 inventory bytes 不变；唯一匹配保持现有事务更新；
     多匹配不写 comparison 或 inventory。
   - 验证冻结后 eval 缺少 scenario、runtime isolation 或合法 fixture 时仍被 checker 拒绝。
2. **先写 schema v2 与模块边界回归测试**
   - 验证七字段精确集合；execution/judging、runtime/isolation 变化只更新对应 protocol hash，
     persistence/inventory/report format 变化不改变跨版本 identity。
   - 验证同轮完整源码 manifest 任意 drift 均 `BLOCKED`，checker 只接受 v2 且不调用 Git。
3. **拆分模块并修复 runner/checker**
   - 实现 TRD 5.1 的 0/1/>1 语义，将 execution、judging、persistence、identity 从薄 runner
     中按第 3 节边界移出，runtime 保持唯一隔离实现。
4. **执行一次性迁移**
   - 先 dry-run 核验可信旧源码、196 分类和 187 份 verdict/evidence；生成 audit 后原子迁移，
     再次 dry-run 必须零 diff，inventory bytes 与 manual-only result 不变。
5. **收敛 trd-gen 混合缺陷**
   - 修改 eval-006 ownership 断言，允许交付摘要中的合法 handoff；强化 skill 的最终文档自检；
     刷新 lockfile hash。
6. **执行确定性验证**
   - 四项 contract 与受影响 pytest 全部通过后，检查 inventory 零 diff和禁止区。
7. **执行精确 fresh eval（已完成）**
   - 单一 runner 进程运行 trd-gen 全部 6 条与 PM eval-017/018/019，最多 `--jobs 9`；保留每个
     有效 PASS、PASS (partial coverage) 或 FAIL，只重试 BLOCKED、timeout 或 incomplete。
8. **独立验收与 closeout**
   - 核对来源文档、diff、确定性结果、9 份 comparison、inventory、runtime 清理和残余风险；
     全部完成后把本文更新为 `Implemented`，不在本轮自动归档新计划。

## 5. 验证命令

```bash
uv run scripts/check_repository_contract.py
uv run scripts/check_eval_contract.py
uv run scripts/check_eval_artifacts.py
uv run scripts/check_doc_contract.py
uv run --with pytest pytest scripts/test_run_skill_eval.py scripts/test_eval_runtime.py \
  scripts/test_eval_execution.py scripts/test_eval_persistence.py \
  scripts/test_migrate_eval_identity_v2.py agents/test_eval_contract.py
uv run scripts/summarize_eval_results.py
git diff --check
git status --short
```

模型获得明确授权后使用一个 runner 进程：

```bash
uv run scripts/run_skill_eval.py --jobs 9 \
  --select engineer/trd-gen/eval-001-prd-to-engineer-trd \
  --select engineer/trd-gen/eval-002-resolve-trd-gap-packet \
  --select engineer/trd-gen/eval-003-nested-prd-to-engineer-trd \
  --select engineer/trd-gen/eval-004-api-adr-owned-by-engineer \
  --select engineer/trd-gen/eval-005-mapped-upload-trd-evidence \
  --select engineer/trd-gen/eval-006-delivery-polling-to-events \
  --select product_manager/pm-agent/eval-017-scope-guard-unenabled-general \
  --select product_manager/pm-agent/eval-018-scope-guard-explicit-invocation \
  --select product_manager/pm-agent/eval-019-scope-guard-enabled-general
```

完成后再次运行 eval contract、artifact checker、summarizer、`git diff --check` 与
`git status --short`，并确认 `migration-inventory.json` 无 diff、`tmp/eval-runs/` 不存在。

## 6. Sub-Agent 分工

| 角色 | 范围 | 边界 |
| --- | --- | --- |
| 主进程 | 保留 PRD、DECISIONS、TRD、仓库规则、计划门禁、集成和最终交付判断 | 不把范围扩张、模型授权或 closeout 决策外包 |
| 实现 sub-agent | schema v2、模块拆分、迁移器、runner/checker 测试、trd-gen skill/eval 与 lockfile | 只改第 3 节文件，不运行模型 eval，不改 inventory 或无关资产 |
| 独立验收 sub-agent | 只读核对来源文档、最终 diff、确定性命令、comparison、inventory 与残余风险 | 不实现修复，不接受候选自评作为证据 |

## 7. Closeout 记录

- `changed_files`: schema v2 execution/judging/runtime/persistence/identity 模块、薄 runner、
  v2-only checker、一次性迁移器与 audit、确定性测试、trd-gen/pm-agent skill 与 trd-gen
  eval-006、lockfile、活动文档，以及 196 份常规 comparison 的 v2 identity；冻结
  `migration-inventory.json` 与 manual-only result 未改。
- `commands_and_results`: 四项 contract 全部 PASS；受影响 pytest `175 passed, 6 subtests
  passed`；迁移后二次 dry-run `0 changes`；summarizer 共 196 份 comparison，132 PASS、
  50 PASS (partial coverage)、14 FAIL；`git diff --check` PASS。
- `fresh_eval_results`: 首批 9 条确认 trd-gen eval-006 与 pm-agent eval-018 为 skill defect；
  最小 skill 修复后按维护者扩大授权运行 trd-gen 6 条与 pm-agent 19 条。trd-gen 6/6
  通过，pm-agent 18/19 通过；超时 BLOCKED 仅按 runbook 单目标提高至 900 秒重试并通过。
- `residual_risks`: pm-agent eval-016 保留 fresh FULL FAIL，实际只读结构治理、HTML 报告、
  六角色覆盖和 major 确认均通过，仅缺用户可见的显式 `idea-to-spec:structure-governance`
  主 route；该缺陷与 Issue #277 的 scope guard/冻结后持久化目标无关，后续单独处理。
- `runtime_artifacts_removed`: `tmp/eval-runs/` 不存在，artifact checker PASS。
- `next_owner`: 维护者审阅并决定是否提交/创建 PR，以及是否为 pm-agent eval-016 建立独立
  issue；本计划不自动归档。
