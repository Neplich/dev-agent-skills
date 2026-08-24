---
title: "计划与 TRD 门禁批准者授权实施计划"
type: IMPLEMENTATION_PLAN
version: "0.1.0"
status: Archived
author: "Neplich Codex"
date: "2026-08-20"
last_updated: "2026-08-24"
generated_by: "feature-implementor"
feature: "gate-approver-authorization"
feature_path: "agents/engineer-agent/skills/feature-implementor/gate-approver-authorization"
parent_feature: "agents/engineer-agent/skills/feature-implementor"
feature_level: "5"
implementation_scope: "gate-approver-authorization"
archived_at: "2026-08-24"
archive_approved_by: "Neplich"
source_plan: "docs/engineer/agents/engineer-agent/skills/feature-implementor/gate-approver-authorization/IMPLEMENTATION_PLAN.md"
change_tier: "major"
related_prd: "docs/pm/agents/engineer-agent/skills/feature-implementor/gate-approver-authorization/PRD.md"
related_trd: "docs/engineer/agents/engineer-agent/skills/feature-implementor/gate-approver-authorization/TRD.md"
related_issue: "https://github.com/Neplich/dev-agent-skills/issues/316"
---

# 计划与 TRD 门禁批准者授权实施计划

## 1. 对齐与状态

| Gate | Status | Evidence |
| --- | --- | --- |
| Product scope | 已确认 | GitHub issue #316 和对应 PRD |
| Technical design | 已确认 | 本路径 TRD |
| Change tier | `major` | 共享 handoff contract、两个 Engineer skill 和六份生成副本同时变化 |
| Active plan | 本轮新建 | 此前该 feature path 无活跃计划或归档计划 |
| Implementation authorization | 已由任务指令给出 | 仅执行本计划所列范围 |

## 2. 预期改动声明

| Field | Expected Value |
| --- | --- |
| `expected_files` | 15 个文件：3 份过程文档、1 份权威 handoff contract、6 份生成副本、3 份 `feature-implementor` 门禁文档、1 份 `trd-gen` skill、1 份 `skills-lock.json`。 |
| `expected_new_dependencies` | `0` |
| `expected_new_config` | `0` |
| `expected_new_abstractions` | `0` |
| `expected_loc_magnitude` | 约 450–700 行净增或机械同步；其中过程文档 240–500 行，skill 与权威契约约 100–160 行，其余为六份副本同步和 lock hash。 |
| `expected_tests_vs_acceptance` | 不新增测试文件；7 条 PRD 验收标准由 4 项确定性命令和逐项文档审查覆盖。 |

该声明用于实施后提问和对账，不是文件数或行数的硬性准入上限。任何实际偏离都按
closeout 规则记录原因和处理结果。

## 3. 文件范围

### 3.1 过程文档

| Path | Operation |
| --- | --- |
| `docs/pm/agents/engineer-agent/skills/feature-implementor/gate-approver-authorization/PRD.md` | Create |
| `docs/engineer/agents/engineer-agent/skills/feature-implementor/gate-approver-authorization/TRD.md` | Create |
| `docs/engineer/agents/engineer-agent/skills/feature-implementor/gate-approver-authorization/IMPLEMENTATION_PLAN.md` | Create |

### 3.2 权威源与门禁文档

| Path | Operation | Change |
| --- | --- | --- |
| `agents/product_manager/skills/idea-to-spec/_internal/_shared/handoff-contract.md` | Modify | 新增批准方式可选扩展和自动审查者最低要求。 |
| `agents/engineer/skills/feature-implementor/SKILL.md` | Modify | 计划 checkpoint、流程与硬门禁接受显式授权。 |
| `agents/engineer/skills/feature-implementor/_internal/planner/INSTRUCTIONS.md` | Modify | 渲染批准者条件，并把预期改动声明交给自动审查。 |
| `agents/engineer/skills/feature-implementor/_internal/implementor/INSTRUCTIONS.md` | Modify | 实施入口接受有效的用户或授权自动审查凭据。 |
| `agents/engineer/skills/trd-gen/SKILL.md` | Modify | 四处 TRD 门禁接受显式授权，并增加定性判据。 |

### 3.3 生成副本

| Path | Operation |
| --- | --- |
| `agents/designer/skills/designer-agent/_internal/_generated/shared-contracts/handoff-contract.md` | Regenerate |
| `agents/devops/skills/devops-agent/_internal/_generated/shared-contracts/handoff-contract.md` | Regenerate |
| `agents/docs/skills/docs-agent/_internal/_generated/shared-contracts/handoff-contract.md` | Regenerate |
| `agents/engineer/skills/engineer-agent/_internal/_generated/shared-contracts/handoff-contract.md` | Regenerate |
| `agents/qa/skills/qa-agent/_internal/_generated/shared-contracts/handoff-contract.md` | Regenerate |
| `agents/security/skills/security-agent/_internal/_generated/shared-contracts/handoff-contract.md` | Regenerate |

### 3.4 派生 metadata

| Path | Operation | Change |
| --- | --- | --- |
| `skills-lock.json` | Modify | 刷新所有 `sourceType=local` 条目的 `computedHash`，无变化条目保持原值。 |

禁止修改 `.claude-plugin/marketplace.json`、任何 `plugin.json`、Router `SKILL.md`、
测试资产、ADR 索引或本表之外的文件。

## 4. 实施顺序

```mermaid
flowchart LR
    D["补齐 PRD / TRD / 计划"] --> H["更新 handoff 权威契约"]
    H --> P["更新 feature-implementor 门禁"]
    P --> T["更新 trd-gen 门禁"]
    T --> G["生成六份契约副本"]
    G --> L["暂存并刷新 lock hash"]
    L --> V["运行四项验证"]
```

### Step 1：更新 handoff 权威契约

- 在 Diagnosis-Only Optional Extension 相邻位置新增批准方式可选扩展。
- 定义 `plan_approval`、`trd_approval` 的可选值与 `user` 缺省行为。
- 完整写入独立上下文、显式边界、发现定级、收敛条件和升级路径。

### Step 2：更新实施计划门禁

- 在 `SKILL.md` 的 checkpoint、Implementation Flow 和硬性确认文字中接受
  `plan_approval: authorized_auto_reviewer`。
- 在 planner 输出和 implementor 入口同步相同批准凭据定义。
- 自动审查输入携带六字段预期改动声明，作为 closeout 对账基线。
- 默认人工确认和 hotfix 确认保持不变。

### Step 3：更新 TRD 门禁

- 修改 Mermaid Review 节点、进入阶段话术、Quality Checks 和最终硬性语句。
- 接受 `trd_approval: authorized_auto_reviewer` 时满足最低要求的独立审查者。
- 写明 TRD 只核对涉及模块、数据结构变化和新增依赖三类定性改动面。
- TRD 侧轮数上限独立给足，不外推实施层验证经验。

### Step 4：同步派生内容

- 运行 `uv run scripts/generate_shared_contracts.py`。
- 只接受第 3.3 节六份 handoff contract 发生机械变化。
- 新文件进入 index 后，按仓库脚本相同算法刷新 local skill hash。

## 5. 验证

依次运行：

```bash
uv run scripts/generate_shared_contracts.py --check
uv run scripts/check_repository_contract.py
uv run scripts/check_doc_contract.py
git diff --cached --check
```

人工逐项检查：

- 缺少批准字段时，两类门禁仍等待用户确认。
- 只有显式 `authorized_auto_reviewer` 才启用自动批准。
- 五项最低要求在权威契约中没有缺项。
- 计划自动审查输入含预期改动声明。
- TRD 判据保持定性，且明确较低确定性和独立轮数设置。
- 六份生成副本与权威源一致。

## 6. 分工与边界

本变更为跨多个 role plugin 的契约同步，实施与独立验证分离。实施者只修改第 3 节文件；
验证者对照 issue #316、PRD、TRD、预期声明、生成结果和命令输出检查完整性。
主流程保留范围判断、集成、提交和 PR 交付责任。

## 7. 收尾要求

实施完成后逐项比较六字段预期值与实际值，并在 closeout 中记录所有偏离。
同时记录实际变更文件、命令与结果、剩余风险以及运行时产物清理情况。
生成脚本和验证命令产生的临时输出不得进入 Git。

计划完成后保持活跃入口不变；只有取得维护者明确归档批准，才移动到
`archive/IMPLEMENTATION_PLAN-gate-approver-authorization.md`。

## Closeout 对账

| 字段 | 预期 | 实际 | 结论 |
| --- | --- | --- | --- |
| `expected_files` | 15 个文件。 | 按本 `feature_path` 切分后，PR #317 修改计划内 15 个文件，并额外修改 1 份父功能 PRD 以登记子功能。 | 偏离：新增 1 份父功能 PRD。 |
| `expected_new_dependencies` | `0` | `0` | 一致 |
| `expected_new_config` | `0` | `0` | 一致 |
| `expected_new_abstractions` | `0` | `0` | 一致 |
| `expected_loc_magnitude` | 约 450–700 行净增或机械同步。 | 本范围约净增 650–700 行，包含 411 行过程文档、授权契约与门禁改动、六份机械生成副本及父功能 PRD 登记。 | 一致 |
| `expected_tests_vs_acceptance` | 不新增测试文件；7 条 PRD 验收标准由 4 项确定性命令和逐项文档审查覆盖。 | 新增测试文件 `0`；合并时 `repository-contract`、`doc-contract`、`python-tests` CI 全部通过。 | 一致 |

验证证据以 PR #317 合并记录为准：`repository-contract`、`doc-contract`、
`python-tests` 均为 SUCCESS。
