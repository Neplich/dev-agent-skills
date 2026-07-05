---
title: "PM 唯一入口 Batch 4 实施计划"
type: IMPLEMENTATION_PLAN
version: "0.4.0"
status: "Implemented"
author: "Neplich Codex"
date: "2026-07-05"
last_updated: "2026-07-05"
generated_by: "feature-implementor"
feature: "pm-single-entry"
feature_path: "repository-governance/pm-single-entry"
parent_feature: "repository-governance"
feature_level: "2"
implementation_scope: "eval-contract-closeout"
related_prd: "docs/pm/repository-governance/pm-single-entry/PRD.md"
related_trd: "docs/engineer/repository-governance/pm-single-entry/TRD.md"
related_issue: "https://github.com/Neplich/dev-agent-skills/issues/52"
related_issues:
  - "https://github.com/Neplich/dev-agent-skills/issues/55"
  - "https://github.com/Neplich/dev-agent-skills/issues/59"
  - "https://github.com/Neplich/dev-agent-skills/issues/60"
  - "https://github.com/Neplich/dev-agent-skills/issues/61"
  - "https://github.com/Neplich/dev-agent-skills/issues/62"
changelog:
  - version: "0.4.0"
    date: "2026-07-05"
    changes: "Batch 4 实施完成：补齐 PM entry eval 全量、missing handoff target 与 change_tier eval 覆盖，并增加非 PM skill internal visibility contract"
  - version: "0.3.12"
    date: "2026-07-05"
    changes: "Codex Review 修复：designer-agent 移除缺 PM handoff 的非持久设计建议绕过"
  - version: "0.3.11"
    date: "2026-07-05"
    changes: "Codex Review 修复：AGENTS 仓库级 PM-first 规则保留 project-bootstrap 显式 skip-PM scaffold 例外"
  - version: "0.3.10"
    date: "2026-07-05"
    changes: "Codex Review 修复：DevOps 与 Security router 的 PM handoff gate 前移到 routing 前"
  - version: "0.3.9"
    date: "2026-07-05"
    changes: "Codex Review 修复：更新 Batch 3 验证记录中的 pytest 计数"
  - version: "0.3.8"
    date: "2026-07-05"
    changes: "Codex Review 修复：FR-006 场景 7-8 comparison 不再把未运行 fresh validation 的 eval 标为 PASS"
  - version: "0.3.7"
    date: "2026-07-05"
    changes: "Codex Review 修复：同日 last_updated 例外只接受顶层 frontmatter changelog key"
  - version: "0.3.6"
    date: "2026-07-05"
    changes: "Codex Review 修复：同日 last_updated 例外只匹配 frontmatter changelog block，并补回归测试"
  - version: "0.3.5"
    date: "2026-07-05"
    changes: "Codex Review 修复：同日 last_updated 例外只扫描 frontmatter changelog entry"
  - version: "0.3.4"
    date: "2026-07-05"
    changes: "Codex Review 修复：同日 last_updated 例外必须同时匹配 changelog version 与 date"
  - version: "0.3.3"
    date: "2026-07-05"
    changes: "Codex Review 修复：FR-006 场景 8 不再把已存在 IMPLEMENTATION_PLAN 当作 feature-implementor 入口前置条件"
  - version: "0.3.2"
    date: "2026-07-05"
    changes: "Codex Review 修复：engineer-agent router 按 specialist entry basis 放行 trd-gen 与 project-bootstrap 合法路径，并补 deterministic 断言"
  - version: "0.3.1"
    date: "2026-07-05"
    changes: "实施完成：下游 gate 指针化与 specialist 权威副本统一、入口 SKILL.md 瘦身、FR-006 场景 7-8 eval 与 deterministic pytest 补齐"
  - version: "0.3.0"
    date: "2026-07-05"
    changes: "规划 Batch 3：下游 gate 指针化与去重、feature-implementor / idea-to-spec 正文瘦身、防绕过 eval 场景 7-8"
  - version: "0.2.5"
    date: "2026-07-05"
    changes: "Batch 2 已完成并合并：补齐 PM 入口分类、handoff packet、FR-006 场景 1-6 和 Codex Review 修复"
---

# PM 唯一入口 Batch 4 实施计划

## 1. 实施上下文

本计划继续实施 issue #52 的最终 Batch 4：在 Batch 1 完成公开发现面收口、Batch 2 完成
`pm-agent` 高召回分类与 handoff packet、Batch 3 完成下游 gate 去重和 SKILL.md 瘦身后，
收尾 PM-only 入口 eval、#62 missing handoff target eval、#55 FR-008 变更分级 eval 和可机器
检查的 internal visibility contract。

本批 `change_tier` 自判为 `major`：它修改 eval 契约、deterministic pytest、repository
contract 脚本和本实施计划。用户已明确确认继续 Batch 4；实施已完成。

```mermaid
flowchart TD
    U["用户直接请求下游"] --> R["role router"]
    U --> S["specialist"]
    R --> G1{"有 PM handoff packet 或等效已确认文档链？"}
    S --> G2{"specialist 入口 gate 通过？"}
    G1 -->|"否"| PM["回 pm-agent 分类"]
    G1 -->|"是"| P["只保留 gate 指针并继续路由"]
    G2 -->|"否"| PM
    G2 -->|"是"| X["按 specialist 协议执行"]
```

来源文档：

- PRD：`docs/pm/repository-governance/pm-single-entry/PRD.md`
- TRD：`docs/engineer/repository-governance/pm-single-entry/TRD.md`
- 分级与归档契约：`AGENTS.md`
- 关联 issue：#52、#55、#59、#60、#61、#62

## 2. 当前门禁状态

| 门禁 | 状态 | 证据 |
| --- | --- | --- |
| PRD 对齐 | 已完成 | PM single-entry PRD 覆盖 FR-006；change-tier PRD 覆盖 FR-008；#62 留有 missing target eval 要求 |
| TRD 对齐 | 已完成 | PM single-entry TRD 第 8 节定义 Batch 4：eval 全量、contract 收尾、durable comparison 更新 |
| Feature path | 已解析 | `repository-governance/pm-single-entry` |
| 设计输入 | 不适用 | 本批为 skill / 文档契约变更，不涉及 UI |
| Archive gate | 继续更新当前计划 | PR #73 已合并，维护者明确进入最后 Batch 4；本 feature 连续分批实施仍使用当前活跃计划，不新建归档 |
| Sub-agent 写计划 | 不启用 | 当前任务是单一实施计划更新；主进程保留 PRD/TRD/AGENTS 约束并在用户确认后实施 |

## 3. 范围

### 3.1 计划修改文件

| 类别 | 路径 | 实际操作 |
| --- | --- | --- |
| 仓库契约 | `AGENTS.md` | 收敛为 PM 唯一入口与 gate 指针声明；保留变更分级、QA E2E、archive 等仓库级规则，不复制 specialist 操作步骤 |
| Role router | `agents/engineer/skills/engineer-agent/SKILL.md` | 把 Existing Feature Alignment Gate 改为轻量指针；新增直接用户请求无 PM handoff 时回 PM 的统一规则 |
| Role router | `agents/designer/skills/designer-agent/SKILL.md` | Feature Path Gate 指针化；直接设计请求无 PM handoff 时回 PM |
| Role router | `agents/qa/skills/qa-agent/SKILL.md` | QA / E2E gate 指针化；保留 QA 路由摘要，完整 E2E 执行门禁下沉到 QA specialist 入口 |
| Role router | `agents/devops/skills/devops-agent/SKILL.md` | Feature Path Gate 指针化；repo-wide DevOps handoff 继续允许 `N/A` feature scope |
| Role router | `agents/security/skills/security-agent/SKILL.md` | Feature Path Gate 指针化；安全 review 无 PM handoff 时回 PM |
| Specialist gate | `agents/engineer/skills/feature-implementor/SKILL.md` | 保留并压缩 PRD alignment、UI design handoff、plan/archive/closeout gate；作为实现类 gate 权威副本 |
| Specialist gate | `agents/engineer/skills/debugger/SKILL.md` | 保留 expected-behavior / repair gate；无 PM handoff 或等效文档链时回 PM |
| Specialist gate | `agents/engineer/skills/project-bootstrap/SKILL.md`、`trd-gen/SKILL.md`、`test-writer/SKILL.md` | 保留各自最小前置门禁；避免复制 PM packet 字段清单 |
| QA specialist gate | `agents/qa/skills/spec-based-tester/SKILL.md`、`exploratory-tester/SKILL.md`、`bug-analyzer/SKILL.md`、`regression-suite/SKILL.md` | 保留 E2E / feature-scoped QA 的完整门禁；`qa-agent` 只指向这些权威副本 |
| 其他 specialist gate | Designer / DevOps / Security specialist `SKILL.md` | 只在已有 feature-path gate 处统一 PM handoff 与回 PM wording；不新增重复大段 gate |
| 正文瘦身样本 | `agents/product_manager/skills/idea-to-spec/SKILL.md` | 目标压到约 150 行；保留入口协议，阶段细节与示例下沉 `_internal` |
| 正文瘦身样本 | `agents/engineer/skills/feature-implementor/SKILL.md` | 目标压到约 150 行；gate 必须留在 SKILL.md，阶段执行细节下沉 `_internal` |
| 内部模块 | `agents/product_manager/skills/idea-to-spec/_internal/**`、`agents/engineer/skills/feature-implementor/_internal/**` | 承接从 SKILL.md 移出的阶段流程、模板和输出约定 |
| Eval | `agents/product_manager/test/pm-agent/evals/evals.json` 与 workspace | 补齐 FR-006 场景 7-8 的 durable eval 定义、workspace、comparison |
| Eval | `agents/product_manager/test/pm-agent/evals/evals.json` 与 workspace | Batch 4 补齐 #62 missing handoff target 与 #55 FR-008 change_tier 场景 9-13，更新 1-8 comparison 的 post-merge fresh validation 状态 |
| Pytest | `agents/product_manager/test/pm-agent/test_pm_entry_eval.py` | 增加防绕过 deterministic 断言 |
| Pytest | `agents/product_manager/test/pm-agent/test_pm_entry_eval.py` | Batch 4 增加 missing target、hotfix fast lane、standard full gate、hotfix abuse blocked、hotfix E2E direct-path deterministic 断言 |
| Contract | `scripts/check_repository_contract.py` | 兼容同一天内连续 Batch 修改同一实施计划时的 `version` / `last_updated` 检查，避免要求写未来日期 |
| Contract | `scripts/check_repository_contract.py` | Batch 4 增加 PM-only public entry 静态检查：除 `pm-agent` 外所有 skill 必须声明 `visibility: internal` |
| Lock | `skills-lock.json` | 重算所有被修改 skill 目录的 `computedHash` |

### 3.2 明确不做

- 不修改 marketplace / README / installer 公开发现面；这些已由 Batch 1 完成。
- 不重新设计 PM handoff packet 字段；字段权威定义沿用 Batch 2 的 PM `_internal` 共享契约。
- 不新增 release CI、GitHub ruleset 或运行时强制拦截。
- 不执行 PR 合并；PR 创建后仍等待 Codex Review、CI 和维护者确认。

## 4. 实施顺序

### 4.1 Gate 去重与指针化

1. 先建立 gate 家族清单：
   - PM handoff packet 字段：权威副本在 PM `_internal` 共享契约。
   - 实现前 PRD/TRD/plan gate：权威副本在 `feature-implementor/SKILL.md`。
   - bug repair expected-behavior gate：权威副本在 `debugger/SKILL.md`。
   - bootstrap settled-spec gate：权威副本在 `project-bootstrap/SKILL.md`。
   - QA E2E / feature-scoped validation gate：权威副本在 QA specialist `SKILL.md`。
   - DevOps / Security / Designer feature path gate：权威副本在对应 specialist `SKILL.md`。
2. 更新 5 个 role router：
   - 只保留“PM handoff packet 或等效已确认文档链”的入口判断。
   - 没有 PM handoff 的直接用户请求，统一回 `pm-agent` 分类。
   - 具体执行 gate 只引用 specialist 权威副本，不复制步骤。
3. 更新 `AGENTS.md`：
   - 保留仓库级结论和路径规则。
   - 删除或压缩与 specialist gate 重复的操作性步骤。
   - 指向本 feature 的 TRD / specialist gate 作为执行细节来源。

### 4.2 Specialist gate 统一

1. 按 TRD 6.2 统一三段判断顺序：
   - 显式 PM handoff packet 完整时执行。
   - 无 packet 但存在等效已确认文档链时执行。
   - 二者都没有时不执行本 skill 协议，回 `pm-agent` 分类。
2. 保留各 specialist 的专业 gate：
   - `feature-implementor` 不直接接新需求、改功能或“帮我实现”原始请求。
   - `debugger` 不直接修未对齐预期的 bug。
   - QA specialist 不在预期未确认时固化 E2E 预期。
3. 避免在每个 specialist 重复 PM packet 字段清单；只引用 PM `_internal` 权威定义。

### 4.3 SKILL.md 瘦身

1. `feature-implementor/SKILL.md`：
   - 保留 frontmatter、职责、使用/拒绝条件、关键 gate、高层 phase、输出边界。
   - 将上下文读取细节、计划模板、实现步骤、自检模板、handoff 模板下沉到现有
     `_internal/planner`、`_internal/implementor`、`_internal/reviewer` 和 `_internal/_shared`
     模块。
   - gate 不下沉；只压缩文案。
2. `idea-to-spec/SKILL.md`：
   - 保留 Non-Negotiable Protocol、Operating Modes、Execution Lanes、Internal Routing
     Contract、Feature Document Memory 和高层 phases。
   - 将 workspace detection、lane playbooks、phase 细节、deliverable shapes、examples 下沉到
     `_internal/orchestration`、`_internal/gen` 和 `_internal/_shared`。
3. 目标：
   - 两个样本入口文件各自约 150 行。
   - 如果 `feature-implementor` 因 gate 必须留在入口文件导致略超，必须在 closeout 记录行数和原因。

### 4.4 Eval 场景 7-8

新增 FR-006 防绕过覆盖：

| 场景 | 验证点 |
| --- | --- |
| `eval-007-direct-downstream-without-handoff` | 直接点名 role router / downstream agent 且无 PM handoff packet 时，应回 `pm-agent` 分类 |
| `eval-008-direct-specialist-bypass-gate` | 绕过 router 直接触发 `feature-implementor` 等 specialist 时，specialist gate 仍执行并阻止直接实现 |

Deterministic pytest 至少检查：

- eval 定义、workspace、`comparison.md` 存在且符合 durable artifact 策略。
- role router SKILL.md 含统一 direct-request guardrail。
- `feature-implementor` / `debugger` / QA specialist 含无 handoff 回 PM 的 gate 行为。

Fresh subagent validation 仍按仓库 eval 门禁执行；若本批实际运行，则同步更新对应
`comparison.md`。

### 4.5 Contract 同日更新兼容

当前 `check_repository_contract.py` 要求 implementation plan 的 `version` 变化时
`last_updated` 字符串也必须变化，但 `last_updated` 又只能使用 `YYYY-MM-DD`。当 Batch 2 与
Batch 3 在同一天连续推进时，真实日期不能变化，不能通过写未来日期绕过。本批需要把该
校验调整为：同一天内只要 `version` 已更新、changelog 含对应版本条目，就接受
`last_updated` 保持当天日期。

## 5. Hash 重算

所有修改过的 skill 目录在提交前重算 `skills-lock.json`。命令：

```bash
uv run python - <<'EOF'
import json, importlib.util, sys
from pathlib import Path
spec = importlib.util.spec_from_file_location("checker", "scripts/check_repository_contract.py")
m = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = m
spec.loader.exec_module(m)
root = Path(".")
lock_path = root / "skills-lock.json"
lock = json.loads(lock_path.read_text())
for name, entry in lock["skills"].items():
    entry["computedHash"] = m.compute_tracked_directory_hash(root, entry["source"])
lock_path.write_text(json.dumps(lock, indent=2, ensure_ascii=False) + "\n")
print("refreshed", len(lock["skills"]), "hashes")
EOF
```

## 6. 验证结果

| 验证项 | 命令 |
| --- | --- |
| diff 空白检查 | `git diff --check` -> PASS |
| 行数检查 | `wc -l agents/engineer/skills/feature-implementor/SKILL.md agents/product_manager/skills/idea-to-spec/SKILL.md` -> `feature-implementor` 152 行、`idea-to-spec` 147 行 |
| 仓库契约 | `uv run scripts/check_repository_contract.py` -> PASS |
| eval 契约 | `uv run scripts/check_eval_contract.py` -> PASS |
| eval 产物策略 | `uv run scripts/check_eval_artifacts.py` -> PASS |
| pm-agent eval pytest | `uv run --with pytest pytest agents/product_manager/test/pm-agent/test_pm_entry_eval.py -q` -> 11 passed |
| CI 同款 pytest | `uv run --with pytest pytest agents/product_manager/test/idea-to-spec agents/product_manager/test/pm-agent agents/qa/test/test_qa_run_eval.py agents/designer/test/test_designer_run_eval.py agents/devops/test/test_devops_run_eval.py agents/test_eval_contract.py` -> 97 passed |

## 7. 风险与缓解

| 风险 | 缓解 |
| --- | --- |
| gate 过度指针化导致直接触发 specialist 时失去拦截 | gate 权威副本必须留在 specialist `SKILL.md`，不移入 `_internal` |
| router 指针太弱导致合法 handoff 被反复拉回 PM | role router 保留 PM handoff packet / 等效文档链放行条件 |
| #60 瘦身删除了必要上下文 | 只下沉阶段细节与模板，不删除职责、gate、输出边界 |
| QA E2E gate 在 router 和 specialist 间漂移 | `qa-agent` 只保留路由和指针；QA specialist 保留执行门禁 |
| eval 场景 7-8 只测文本、不测行为 | 本批先补 deterministic 防回退；fresh subagent validation 如执行则更新 durable comparison |
| 同一天连续批次导致 `last_updated` 无法变化 | 小范围调整 repository contract，不写未来日期 |

## 8. 完成标准

- Batch 4 计划范围内文件已更新，未触碰 Batch 1 / Batch 2 已完成的公开发现面和 PM packet 字段定义。
- `feature-implementor` 与 `idea-to-spec` 入口文件显著瘦身，并记录最终行数。
- FR-006 场景 7-8 eval 定义、workspace、comparison 和 pytest 覆盖已补齐。
- FR-006 场景 1-8 eval 定义与 deterministic pytest 全量覆盖已保留。
- #62 missing handoff target eval 场景已补齐，断言目标 agent 未安装时 blocked 且不代行职责。
- #55 FR-008 change_tier eval 场景已补齐，覆盖 hotfix fast lane、standard full gate、hotfix 滥用阻断和 hotfix QA 直接影响路径。
- repository contract 已校验非 PM skill 的 `visibility: internal` 声明。
- Batch 4 未修改 skill 目录，未产生新的 `skills-lock.json` 更新。
- 本地验证命令全部通过。
- PR 创建后通过 GitHub CI 和 Codex Review；如 Codex Review 提出问题，只追加 commit 修复并再次触发一次 `@codex review`。

## 9. Batch 2 已合并摘要

Batch 2 PR #72 已合并到 `main`，完成 `pm-agent` 高召回入口、请求分类、handoff packet
权威定义、FR-006 场景 1-6 eval 和多轮 Codex Review 修复。本批从该合并后基线继续，不再
重复修改 Batch 2 已确认的 PM packet 字段。

## 10. 实施 Closeout

最终状态：Batch 4 本地实施完成，进入 PR、CI 和 Codex Review 阶段。

已完成变更：

- `AGENTS.md` 增加 PM 唯一入口与下游 gate 指针规则，不复制 PM packet 字段或 specialist 操作步骤。
- 5 个 role router 改为轻量 PM handoff entry gate；直接用户请求缺少 PM handoff 或等效文档链时回 `pm-agent` 分类。
- Engineer、Designer、QA、DevOps、Security specialist 入口补齐 PM handoff gate，专业 gate 保留在对应 specialist 作为权威副本。
- `feature-implementor/SKILL.md` 瘦身至 152 行；因实现类 gate 必须保留在入口文件，略高于 150 行目标。
- `idea-to-spec/SKILL.md` 瘦身至 147 行；阶段细节保留在 `_internal` 模块。
- 新增 FR-006 场景 7-8 eval、workspace、durable `comparison.md`，并扩展 pm-agent deterministic pytest。
- 新增 Batch 4 eval 场景 9-13：missing handoff target、hotfix fast lane、standard full gate、hotfix 滥用阻断和 hotfix QA 直接影响路径。
- 更新 FR-006 场景 1-8 durable `comparison.md` 的 next-step 说明，明确 fresh with/without-skill validation 转入 Batch 4 合并后的集中 skill-eval 阶段。
- `scripts/check_repository_contract.py` 增加 internal visibility 静态检查，确保除 `pm-agent` 外的 skill 均声明 `visibility: internal`。
- `scripts/check_repository_contract.py` 兼容同日连续批次更新 implementation plan 时的 `version` / `last_updated` 合法状态。
- Batch 4 本地验证通过：repository contract、eval contract、eval artifacts、pm-agent eval pytest 11 passed、CI 同款 pytest 97 passed。
- Batch 3 已全量重算 `skills-lock.json`；Batch 4 未修改 skill 目录，未产生新的 `skills-lock.json` 更新。

未运行项：

- Fresh Codex subagent validation 未在本 PR 执行；本批只补 deterministic eval / contract coverage 与 durable comparison 状态记录。维护者已安排 Batch 4 合并后集中执行受影响 skill 的 fresh subagent validation，并重新生成 without-skill baseline、同步更新 comparison。

剩余风险：

- 本批是 eval 与 contract 收尾，行为执行仍依赖后续集中 fresh validation 和实际 agent 调用遵循这些入口 gate。
- `feature-implementor` 入口文件保留 152 行，是为了不把关键实现 gate 下沉到 `_internal` 后降低直接触发时的拦截强度。

下一 owner：

- 维护者 / PR 流程：等待 GitHub CI、Codex Review 和维护者确认后再合并；若 Codex Review 提出问题，只追加 commit 修复并再次触发一次 `@codex review`。

## 11. Codex Review 修复记录

2026-07-05 Codex Review 对提交 `7de025d` 提出两条 P2：

- `engineer-agent` 不应在用户明确 skip PM 并请求 `project-bootstrap` scaffold 时，先于 specialist override 把请求拉回 PM。
- `engineer-agent` 不应把 `trd-gen` 路径要求成 PRD + TRD + confirmed implementation plan；TRD 创建路径应允许 confirmed PM docs + stable feature path 作为 specialist entry basis。

修复结果：

- `engineer-agent/SKILL.md` 的 PM handoff entry gate 改为按 selected specialist entry basis 判断。
- 明确 `trd-gen` 可从 confirmed PM documents 与 stable feature path 进入，即使 Engineer TRD 尚不存在。
- 明确 `project-bootstrap` 在用户显式 skip PM and scaffold anyway 时可进入 specialist，由 specialist 自己处理 override 和最小 stack question。
- `test_pm_entry_eval.py` 新增 deterministic 断言覆盖这两个合法路径。

2026-07-05 Codex Review 对提交 `5b8c500` 提出一条 P2：

- FR-006 场景 8 的断言不应要求等价 PRD/TRD/IMPLEMENTATION_PLAN 文档链；`feature-implementor` 合法入口是在 PM scope 和 TRD 已确认后创建 `IMPLEMENTATION_PLAN.md`。

修复结果：

- `eval-008-direct-specialist-bypass-gate` 改为要求 PM handoff packet，或等价已确认 PRD/TRD 与当前 implementation scope。
- 场景 8 durable `comparison.md` 明确已存在 `IMPLEMENTATION_PLAN.md` 不是首次进入 `feature-implementor` planning 的前置条件。

2026-07-05 Codex Review 对提交 `37ba7e6` 提出一条 P2：

- 同日 `last_updated` 例外只检查 changelog version 会让跨日遗漏 `last_updated` 的计划也通过；需要同时校验 changelog entry date。

修复结果：

- `markdown_changelog_has_version_date` 现在按 changelog entry 同时匹配 `version` 和 `date`。
- `validate_implementation_plan_metadata` 只有在当前 `last_updated` 与 changelog entry date 一致时才豁免同日连续版本更新。

2026-07-05 Codex Review 对提交 `1a43cb4` 提出一条 P2：

- version/date 匹配不应扫描整篇 Markdown，正文示例里的 changelog 片段不能充当 frontmatter changelog entry。

修复结果：

- 新增 `markdown_frontmatter_block`，只提取 Markdown frontmatter。
- 同日 `last_updated` 例外改为调用 `markdown_frontmatter_changelog_has_version_date`，只在 frontmatter changelog entry 中匹配 version/date。

2026-07-05 Codex Review 对提交 `ed8a35d` 提出一条 P2：

- frontmatter 中其他 `version/date` 列表仍可能被误当作 changelog entry；同日例外必须限制到 `changelog:` block。

修复结果：

- 新增 `markdown_frontmatter_changelog_block`，只提取 frontmatter 中的 `changelog:` 子块。
- 同日 `last_updated` 例外只在该 changelog block 内匹配 version/date。
- `agents/test_eval_contract.py` 新增回归测试，验证 frontmatter 其他列表和正文 fenced YAML 示例不会触发同日例外。

2026-07-05 Codex Review 对提交 `f986e07` 提出一条 P2：

- 嵌套 frontmatter map 中的 `changelog:` 不应被当成顶层 canonical changelog；同日例外只能接受顶层 `changelog:` key。

修复结果：

- `markdown_frontmatter_changelog_block` 改为只匹配无缩进的顶层 `changelog:`。
- `agents/test_eval_contract.py` 补充嵌套 `release_metadata.changelog` 不会触发同日例外的回归断言。

2026-07-05 Codex Review 对提交 `84308bc` 提出一条 P2：

- 新增 eval 7/8 的 durable `comparison.md` 不应在 fresh Codex subagent validation 与新 baseline 尚未运行时写成 `PASS`。

修复结果：

- eval 7/8 的 `Latest result` 改为 `PARTIAL`，明确当前只有 deterministic Batch 3 gate 覆盖。
- eval 7/8 的 coverage gap 记录 fresh subagent validation 与 without-skill baseline 仍待 Batch 4 授权执行。

2026-07-05 Codex Review 对提交 `11192f1` 提出一条 P3：

- 实施计划中的验证计数仍记录为 `6 passed` / `91 passed`，与当前测试套件和 closeout 摘要不一致。

修复结果：

- Batch 3 验证结果更新为 pm-agent eval pytest `7 passed`、CI 同款 pytest `93 passed`。

2026-07-05 Codex Review 对提交 `c92e326` 提出两条 P2：

- `devops-agent` 的 PM handoff gate 位于 Available Skills / Routing Signals / Default Routes / Escalation Rules 之后，可能先选择 DevOps specialist 再检查 PM handoff。
- `security-agent` 的 PM handoff gate 同样位于 routing 内容之后，可能先选择 Security specialist 再检查 PM handoff。

修复结果：

- `devops-agent/SKILL.md` 将 PM Handoff Entry Gate 前移到 Role Boundary 后、Available Skills 前。
- `security-agent/SKILL.md` 将 PM Handoff Entry Gate 前移到 Role Boundary 后、Available Skills 前。

2026-07-05 Codex Review 对提交 `4760557` 提出一条 P2：

- 仓库级 `AGENTS.md` 的 PM-first 规则没有保留 `project-bootstrap` 显式 skip-PM scaffold override，可能先于 specialist gate 把合法 starter scaffold 路径拉回 PM。

修复结果：

- `AGENTS.md` 的直接调用下游规则补充唯一例外：用户直接请求 `project-bootstrap` 且明确要求跳过 PM 并立即 scaffold 时，可进入 `project-bootstrap` 的最小脚手架 override。

2026-07-05 Codex Review 对提交 `ee4ccc9` 提出一条 P2：

- `designer-agent` 的 PM handoff gate 已要求缺少 handoff/docs 时回 `pm-agent`，但 Escalation Rules 仍允许缺 PM docs 的直接设计请求进入最窄 design skill 做非持久建议，形成绕过。

修复结果：

- `designer-agent/SKILL.md` 移除缺 PM docs 的非持久设计建议 bypass；缺少 PM handoff context 或等效已确认 PM/design 文档时，先回 `pm-agent` 分类再选择 design skill。
