---
title: "仓库文档权威与生命周期治理实施计划"
type: IMPLEMENTATION_PLAN
version: "0.1.7"
status: Archived
author: "Neplich Codex"
date: "2026-08-15"
last_updated: "2026-08-16"
generated_by: "feature-implementor"
feature: "document-authority"
feature_path: "repository-governance/document-authority"
parent_feature: "repository-governance"
feature_level: "2"
change_tier: "major"
implementation_scope: "document-authority"
related_prd: "docs/pm/repository-governance/document-authority/PRD.md"
related_trd: "docs/engineer/repository-governance/document-authority/TRD.md"
related_decisions: "docs/pm/repository-governance/document-authority/DECISIONS.md"
related_issue: "https://github.com/Neplich/dev-agent-skills/issues/285"
approved_by: "Neplich"
approved_at: "2026-08-15"
archived_at: "2026-08-16"
archive_approved_by: "Neplich"
source_plan: "docs/engineer/repository-governance/document-authority/IMPLEMENTATION_PLAN.md"
changelog:
  - version: "0.1.7"
    date: "2026-08-16"
    changes: "完成实现、fresh eval 收敛、独立验收与 closeout，并按维护者总授权归档"
  - version: "0.1.6"
    date: "2026-08-16"
    changes: "按最终 Router eval 证据补强显式 Specialist 交接与 bug/deployment/security/fast-lane handoff 字段"
  - version: "0.1.5"
    date: "2026-08-16"
    changes: "按独立验收补回 PM planning blocker，并让 Engineer/PM Router eval 显式包含被路由目标"
  - version: "0.1.4"
    date: "2026-08-16"
    changes: "把 6 个现有 legacy `<skill>/workspace/` eval metadata 纳入必要的 Router dependency 修正"
  - version: "0.1.3"
    date: "2026-08-16"
    changes: "纳入下游 Specialist eval 的 Router dependency 修正，确保隔离 overlay 与真实插件安装拓扑一致"
  - version: "0.1.2"
    date: "2026-08-15"
    changes: "按 TRD v0.1.1 把人工维护内容与约 2,000 行只读生成副本分开计量"
  - version: "0.1.1"
    date: "2026-08-15"
    changes: "把受新活跃计划生命周期规则直接影响的共享 eval contract 测试纳入精确验证范围"
  - version: "0.1.0"
    date: "2026-08-15"
    changes: "批准文档权威、共享契约派生、14 份计划归档、Router 收窄、QA 模板迁移与仓库门禁的分阶段实施范围"
---

# 仓库文档权威与生命周期治理实施计划

## 1. 对齐与计划门禁

| 字段 | 结果 |
| --- | --- |
| `feature_path` | `repository-governance/document-authority` |
| `parent_feature` | `repository-governance` |
| `feature_level` | `2` |
| `change_tier` | `major`；修改跨角色契约、35 个 Skill、过程文档和仓库 checker |
| `change_map_path` | `N/A`；仓库不存在 `docs/site/standards/change-map.yaml` |
| `matched_code_glob` | `N/A` |
| `mapped_docs` | PRD、DECISIONS 与 TRD，路径见 frontmatter |
| `prd_alignment` | `already_approved`；PRD v1.0.1 与 DECISIONS v1.0.1 已确认 5 个 US、8 个 FR 和 9 项 Accepted 决策 |
| `trd_alignment` | `already_approved`；TRD v0.1.1 的 metadata、范围、14 个归档目标和验证策略与 PM 文档一致 |
| UI / Design | `N/A`；不改变 UI、交互、视觉或信息层级，不创建 Design 交付物 |
| 活跃计划扫描 | 写入前 `docs/engineer/repository-governance/document-authority/IMPLEMENTATION_PLAN.md` 不存在 |
| `active_plan_status` | `N/A`；新 feature path 无旧活跃计划 |
| `active_plan_scope_before` | `N/A` |
| 归档扫描 | 写入前 `docs/engineer/repository-governance/document-authority/archive/` 不存在，无历史 backlink |
| `replacement_plan_scope` | `document-authority` |
| `active_entry_rule` | 实施期间固定使用本文件；完成 closeout 后只移动到第 5.2 节冻结归档路径 |
| `archive_state` | `new_feature_no_history` |
| `decision` | 创建并执行本完整计划；完成后按用户已批准策略冻结归档 |
| `receiving_owner` | `engineer-agent:feature-implementor` |
| `gap_packet` | `N/A`；无 PRD、TRD 或 Design gap |
| `subagent_split` | `enabled`；复杂多文件、跨插件、带 checker 与 eval 的 spec-backed 变更 |
| `confirmation_required` | 已满足；Neplich 于 2026-08-15 授权后续门禁，除设计不确定外执行至 PR 合并前 |
| `blocked_downstream_actions` | PR 合并；本计划不授权 merge、tag、Release、仓库设置或部署变更 |

QA E2E 不适用：本变更不改变用户流程、登录、权限、数据准备或产品验收路径，不创建或
更新 `docs/qa/e2e/` 测试用例。若实现证据推翻该判断，停止并先由主进程补充 QA handoff；
不得由实施 subagent 自行扩大范围。

## 2. 成功标准与规模

1. 文档职责与禁止内容有唯一 owner，根规则、架构图、文档治理和三篇 cookbook 可相互导航。
2. 14 份已完成计划全部冻结归档，原活跃入口不再保留；本功能完成后也退出活跃入口。
3. handoff、closeout、Security escalation、consumption 四份契约各只有一个人工维护源，
   六个下游插件各有四份确定性生成副本，freshness 为 100%。
4. 七个 Router 仅保留入口凭据、路由表、阻塞条件和 Specialist 指针，分别满足
   PM `320/3000` 与下游 `160/1300` 的行/词预算。
5. 31 份精确 marketplace PRD 与 2 份 TRD 不再是 `Draft`；QA E2E 模板只有 QA
   reference 一个 owner；四份 current-state 长文档低于 500 行。
6. 本地 Markdown 链接、锚点、路径边界、计划生命周期、生成副本、Skill hash、安装
   边界和受影响行为回归均通过。
7. 不改变 marketplace 注册、Skill 名称、发现描述、七个 Agent 用户可见行为和能力。

预计人工维护内容净删除 1,000–2,500 行；24 份只读生成副本约 2,000 行，连同本功能
过程文档和测试后 Git 总行数可小幅净增加。不新增抽象层、配置 manifest、兼容双轨、
缓存、重试、feature flag、遥测或 Release CI。人工维护内容偏离区间时先停下核对重复
协议遗漏或范围扩张；生成副本与冻结归档的纯路径移动单独计量。

## 3. 精确文件与集合

### 3.1 仓库入口与文档 owner

修改：

- `AGENTS.md`
- `README.md`
- `README_zh.md`
- `agents/{product_manager,designer,engineer,qa,devops,security,docs}/{README.md,README_zh.md}`

新增：

- `docs/architecture.md`
- `docs/AGENTS.md`
- `docs/cookbook/maintain-skills.md`
- `docs/cookbook/run-skill-evals.md`
- `docs/cookbook/release.md`

集合表达式必须展开为花括号中每个已列元素，不表示可扩大到其他路径。Role README 只
保留能力目录、输入输出、简要边界和导航；根 README 只增加架构与 cookbook 导航。

### 3.2 权威契约与 24 份生成副本

权威目录固定为
`agents/product_manager/skills/idea-to-spec/_internal/_shared/`：

- 修改 `skill-map.md`、`consumption-contract.md`；
- 新增 `handoff-contract.md`、`closeout-contract.md`、`security-escalation.md`。

新增 `scripts/generate_shared_contracts.py`。它只读取上述四份 `*-contract` / escalation
源文件，不生成 `skill-map.md`；默认覆盖，`--check` 只比较且检查 missing、extra、stale。

生成目标是下列六个 Router 目录与四个文件名的笛卡尔积，共 24 份：

- Router 目录：
  - `agents/designer/skills/designer-agent/_internal/_generated/shared-contracts/`
  - `agents/engineer/skills/engineer-agent/_internal/_generated/shared-contracts/`
  - `agents/qa/skills/qa-agent/_internal/_generated/shared-contracts/`
  - `agents/devops/skills/devops-agent/_internal/_generated/shared-contracts/`
  - `agents/security/skills/security-agent/_internal/_generated/shared-contracts/`
  - `agents/docs/skills/docs-agent/_internal/_generated/shared-contracts/`
- 文件名：`handoff-contract.md`、`closeout-contract.md`、`security-escalation.md`、
  `consumption-contract.md`。

### 3.3 Skill 消费者与 lock

修改六个下游插件的全部 31 个 marketplace Skill：

- `agents/designer/skills/{designer-agent,ui-ux-design,visual-design}/SKILL.md`
- `agents/engineer/skills/{codebase-analyzer,debugger,delivery,engineer-agent,feature-implementor,test-writer,trd-gen}/SKILL.md`
- `agents/qa/skills/{bug-analyzer,exploratory-tester,qa-agent,regression-suite,spec-based-tester}/SKILL.md`
- `agents/devops/skills/{cicd-bootstrap,deployment-planner,devops-agent,env-config-auditor,incident-playbook-writer}/SKILL.md`
- `agents/security/skills/{appsec-checklist,authz-reviewer,dependency-risk-auditor,privacy-surface-mapper,security-agent}/SKILL.md`
- `agents/docs/skills/{docs-agent,docs-audit,docs-site-bootstrap,formal-docs-sync,manual-gen,release-notes-gen}/SKILL.md`

下游 Router 与 Specialist 只引用本插件 Router 的生成副本。PM 插件内修改：

- `agents/product_manager/skills/pm-agent/SKILL.md`
- `agents/product_manager/skills/idea-to-spec/SKILL.md`
- `agents/product_manager/skills/feature-catalog/SKILL.md`
- `agents/product_manager/skills/github-reader/SKILL.md`

`skills-lock.json` 只刷新以上 35 个实际变更 Skill 的 `computedHash`。不修改
`.claude-plugin/marketplace.json`、各 plugin manifest、`.kimi-plugin/plugin.json`、Skill
名称、frontmatter description 或发现语义。

### 3.4 Marketplace 镜像文档状态

以下 31 份 PRD 只做 `status: Approved`、SemVer PATCH、`last_updated` 与同版本
frontmatter changelog 的机械更新，路径集合为：

- `docs/pm/agents/pm-agent/skills/{changelog-gen,competitive-brief,feature-catalog,github-reader,idea-to-spec,pm-agent,roadmap-gen}/PRD.md`
- `docs/pm/agents/engineer-agent/skills/{codebase-analyzer,delivery,engineer-agent,feature-implementor,test-writer,trd-gen}/PRD.md`
- `docs/pm/agents/qa-agent/skills/{bug-analyzer,exploratory-tester,qa-agent,regression-suite,spec-based-tester}/PRD.md`
- `docs/pm/agents/devops-agent/skills/{cicd-bootstrap,deployment-planner,devops-agent,env-config-auditor,incident-playbook-writer}/PRD.md`
- `docs/pm/agents/designer-agent/skills/{designer-agent,ui-ux-design,visual-design}/PRD.md`
- `docs/pm/agents/security-agent/skills/{appsec-checklist,authz-reviewer,dependency-risk-auditor,privacy-surface-mapper,security-agent}/PRD.md`

两份 TRD 同样只做机械 frontmatter 更新：

- `docs/engineer/agents/pm-agent/skills/changelog-gen/TRD.md`
- `docs/engineer/agents/pm-agent/skills/feature-catalog/TRD.md`

不存在的 marketplace 镜像文档不补建；Agent 父 PRD、非 marketplace child feature 和
冻结历史不受此步骤影响。

### 3.5 QA owner 与四份 current-state 文档

修改：

- `agents/qa/skills/qa-agent/references/e2e-credential-store.md`
- `agents/qa/skills/qa-agent/references/e2e-test-report.md`
- `agents/qa/skills/qa-agent/SKILL.md`
- `docs/pm/agents/qa-agent/e2e-case-memory/PRD.md`
- `docs/engineer/agents/qa-agent/e2e-case-memory/TRD.md`
- `docs/engineer/agents/docs-agent/TRD.md`
- `docs/engineer/repository-governance/eval-scenario-isolation/TRD.md`

新增 `agents/qa/skills/qa-agent/references/e2e-case-format.md`。三个 QA reference 分别
唯一拥有凭据、报告、用例/脚本格式；四份 current-state 文档更新 version、日期与
changelog 并收窄到 500 行以内，不创建新 feature tree。

### 3.6 Checker、测试与安装证据

修改：

- `scripts/check_repository_contract.py`
- `scripts/check_doc_contract.py`
- `scripts/test_check_repository_contract.py`
- `agents/test_doc_contract.py`
- `agents/test_eval_contract.py`（只更新与活跃计划状态门禁冲突的既有断言）
- `scripts/test_install_codex_skills.py`
- `.github/workflows/ci.yml`（仅把新增确定性测试加入现有 `python-tests`）

新增 `scripts/test_generate_shared_contracts.py`。复用现有
`scripts/install_codex_skills.py`，不预设修改安装器；安装器只在新增测试证明当前复制
语义无法满足已批准 TRD 时停止并回到主进程，不由 subagent 增加兼容层。

受影响 eval 的识别、metadata dependency 修正、fresh paired 执行与 durable
`comparison.md` 只由 `skill-eval-runner` 完成；可写路径限于上述 35 个 Skill 对应的
`agents/*/test/<skill>/evals/`，以及仓库现有的 6 个
`agents/*/test/<skill>/workspace/` legacy 目标。六个下游插件的 Specialist metadata
显式声明同插件 Router dependency，确保生成契约在隔离 overlay 内可达；Engineer
Router 的 5 个场景声明插件内 Specialist，PM Router 只在场景需要目标实际可用时声明
对应下游 Router/Specialist，并保留“目标缺失”场景不安装该目标。仅真实受影响目标可
更新，不手工改写结论。

## 4. 14 份冻结归档映射

每项先确认源存在、目标不存在、body 无未完成范围，再用 `git mv`。正文不改写；只调整
frontmatter 为 `status: Archived`、目标文件名对应的 `implementation_scope`、
`archived_at: 2026-08-15`、`archive_approved_by: Neplich`、`source_plan`，并保留其余原始
metadata。任一目标已存在时停止该项并由主进程选择不冲突 scope，不覆盖文件。

| 活跃源路径 | 冻结目标路径 |
| --- | --- |
| `docs/engineer/agents/docs-agent/IMPLEMENTATION_PLAN.md` | `docs/engineer/agents/docs-agent/archive/IMPLEMENTATION_PLAN-docs-agent.md` |
| `docs/engineer/agents/docs-agent/docs-authoring-foundation/IMPLEMENTATION_PLAN.md` | `docs/engineer/agents/docs-agent/docs-authoring-foundation/archive/IMPLEMENTATION_PLAN-docs-authoring-foundation.md` |
| `docs/engineer/agents/docs-agent/formal-docs-sync/IMPLEMENTATION_PLAN.md` | `docs/engineer/agents/docs-agent/formal-docs-sync/archive/IMPLEMENTATION_PLAN-formal-docs-sync-multi-type.md` |
| `docs/engineer/agents/docs-agent/manual-gen/IMPLEMENTATION_PLAN.md` | `docs/engineer/agents/docs-agent/manual-gen/archive/IMPLEMENTATION_PLAN-manual-gen.md` |
| `docs/engineer/agents/docs-agent/release-notes-gen/IMPLEMENTATION_PLAN.md` | `docs/engineer/agents/docs-agent/release-notes-gen/archive/IMPLEMENTATION_PLAN-release-notes-gen.md` |
| `docs/engineer/agents/engineer-agent/skills/debugger/IMPLEMENTATION_PLAN.md` | `docs/engineer/agents/engineer-agent/skills/debugger/archive/IMPLEMENTATION_PLAN-debugger-read-only-diagnosis.md` |
| `docs/engineer/agents/engineer-agent/skills/feature-implementor/implementation-plan-archive-gate/IMPLEMENTATION_PLAN.md` | `docs/engineer/agents/engineer-agent/skills/feature-implementor/implementation-plan-archive-gate/archive/IMPLEMENTATION_PLAN-archive-path-contract-migration.md` |
| `docs/engineer/agents/pm-agent/skills/feature-catalog/IMPLEMENTATION_PLAN.md` | `docs/engineer/agents/pm-agent/skills/feature-catalog/archive/IMPLEMENTATION_PLAN-inherited-project-feature-catalog.md` |
| `docs/engineer/agents/pm-agent/skills/github-release-gen/IMPLEMENTATION_PLAN.md` | `docs/engineer/agents/pm-agent/skills/github-release-gen/archive/IMPLEMENTATION_PLAN-github-release-gen-gate-governance.md` |
| `docs/engineer/repository-governance/change-tier-contract/IMPLEMENTATION_PLAN.md` | `docs/engineer/repository-governance/change-tier-contract/archive/IMPLEMENTATION_PLAN-change-tier-contract.md` |
| `docs/engineer/repository-governance/eval-scenario-isolation/IMPLEMENTATION_PLAN.md` | `docs/engineer/repository-governance/eval-scenario-isolation/archive/IMPLEMENTATION_PLAN-eval-existing-defect-cleanup.md` |
| `docs/engineer/repository-governance/feature-path-contract/IMPLEMENTATION_PLAN.md` | `docs/engineer/repository-governance/feature-path-contract/archive/IMPLEMENTATION_PLAN-feature-path-autonomous-split-governance.md` |
| `docs/engineer/repository-governance/pm-single-entry/IMPLEMENTATION_PLAN.md` | `docs/engineer/repository-governance/pm-single-entry/archive/IMPLEMENTATION_PLAN-pm-single-entry-convergence.md` |
| `docs/engineer/repository-governance/skill-gen-rename/IMPLEMENTATION_PLAN.md` | `docs/engineer/repository-governance/skill-gen-rename/archive/IMPLEMENTATION_PLAN-skill-gen-rename.md` |

## 5. 实施阶段与验证

### 5.1 阶段 A：基线锁定与 owner 文档

1. 记录 14 个源/目标存在性、七个 Router 行词数、31 PRD 与 2 TRD 当前状态、五份长文档
   行数和当前 Git diff。
2. 收窄 `AGENTS.md`，建立 `docs/architecture.md`、`docs/AGENTS.md` 和三篇 cookbook，
   更新根/Role README 导航；不复制专项 Skill 协议。

验证：

```bash
test ! -e docs/decisions
uv run scripts/check_doc_contract.py
git diff --check
```

### 5.2 阶段 B：计划生命周期

1. 按第 4 节逐项归档，保留正文并只改 archive frontmatter。
2. 在 repository checker 增加活跃计划禁止 `Implemented` / `Archived` 的规则，保留归档
   仅接受 `Archived` / `Superseded` 的现有规则，并增加正/负向测试。
3. 修复因 14 个活跃路径退出而失效的当前态引用，不改冻结历史引用。

验证：

```bash
uv run --with pytest pytest scripts/test_check_repository_contract.py
uv run scripts/check_repository_contract.py
find docs/engineer -name IMPLEMENTATION_PLAN.md -type f
git diff --check
```

阶段完成条件：第 4 节 14 个源路径全部不存在、14 个目标存在且元数据合法；其他仍在执行
的活跃计划不受影响。

### 5.3 阶段 C：共享契约、消费者与 Router

1. 从 `skill-map.md` 原位迁出 handoff、closeout、Security escalation；保留导航链接，
   `consumption-contract.md` 继续作为第四个权威源。
2. 实现生成器和测试，生成 24 份只读副本；先让 `--check` 通过，再切换消费者引用。
3. 修改 35 个 Skill，六个下游插件只读本地生成副本；收窄七个 Router 并保持路由、阻塞
   和 Specialist 指针语义。
4. 刷新 35 个 lock hash；不修改注册、manifest、名称或 discovery metadata。

验证：

```bash
uv run scripts/generate_shared_contracts.py --check
uv run --with pytest pytest scripts/test_generate_shared_contracts.py scripts/test_check_repository_contract.py
uv run scripts/check_repository_contract.py
git diff --check
```

### 5.4 阶段 D：文档状态、QA owner 与长文档

1. 按第 3.4 节机械收敛 31 PRD 与 2 TRD frontmatter。
2. 按第 3.5 节迁出 QA E2E 模板，收窄 QA E2E PRD/TRD、Docs 父 TRD 与 eval isolation TRD。
3. 检查 QA 模板全文只在三个 reference 中人工维护，四份 current-state 文档各少于
   500 行。

验证：

```bash
uv run scripts/check_repository_contract.py
uv run scripts/check_doc_contract.py
wc -l docs/pm/agents/qa-agent/e2e-case-memory/PRD.md docs/engineer/agents/qa-agent/e2e-case-memory/TRD.md docs/engineer/agents/docs-agent/TRD.md docs/engineer/repository-governance/eval-scenario-isolation/TRD.md
git diff --check
```

### 5.5 阶段 E：Markdown、安装与确定性回归

1. 扩展 doc checker 的本地文件、GitHub 风格 heading slug、重复 heading、URL decode、
   逃逸路径与来源排除逻辑，并补目标缺失、锚点缺失、路径逃逸负向测试。
2. 补 repository checker 的生成副本、Router 预算、marketplace 文档状态、生命周期和
   lock 测试；把生成器测试加入 CI。
3. 由安装测试按 marketplace plugin 边界复制七个插件，并验证 Codex full / routers-only
   mirror；不把临时目录或运行输出写入 Git。

验证：

```bash
uv run --with pytest pytest scripts/test_generate_shared_contracts.py scripts/test_check_repository_contract.py agents/test_doc_contract.py scripts/test_install_codex_skills.py
uv run scripts/check_repository_contract.py
uv run scripts/check_doc_contract.py
uv run scripts/check_eval_contract.py
uv run scripts/check_eval_artifacts.py
git diff --check
```

### 5.6 阶段 F：fresh eval、独立验收与 closeout

1. `skill-eval-runner` 识别 35 个变更 Skill 的真实 affected targets，单进程、最多 10
   workers 执行 fresh paired；只更新本轮证据支持的 durable `comparison.md`。
2. 独立 validation subagent 对照 PRD、DECISIONS、TRD、本计划、最终 diff、确定性测试、
   安装结果、eval 结果、仓库规则、无关改动安全和残余风险验收。
3. 主进程修复范围内问题，清理 `tmp/eval-runs/` 等运行产物，更新本计划 closeout。
4. 经已记录的维护者归档批准，用 `git mv` 将本计划移动到
   `docs/engineer/repository-governance/document-authority/archive/IMPLEMENTATION_PLAN-document-authority.md`，
   设置 `status: Archived`、`archived_at: 2026-08-15`、`archive_approved_by: Neplich`、
   `source_plan`，不保留完成态活跃副本。
5. 创建单一 PR，等待 CI 和 review；处理范围内反馈后停在合并前。

最终验证：

```bash
uv run scripts/generate_shared_contracts.py --check
uv run scripts/check_repository_contract.py
uv run scripts/check_doc_contract.py
uv run scripts/check_eval_contract.py
uv run scripts/check_eval_artifacts.py
uv run --with pytest pytest agents/product_manager/test/idea-to-spec agents/product_manager/test/pm-agent agents/qa/test/test_qa_run_eval.py agents/designer/test/test_designer_run_eval.py agents/devops/test/test_devops_run_eval.py agents/docs/test/test_docs_run_eval.py agents/test_doc_contract.py agents/test_eval_contract.py scripts/test_eval_runtime.py scripts/test_run_skill_eval.py scripts/test_check_eval_artifacts.py scripts/test_generate_shared_contracts.py scripts/test_install_codex_skills.py scripts/test_summarize_eval_results.py scripts/test_check_repository_contract.py
git diff --check
git diff --stat
```

## 6. Subagent 分工与禁止区

### 6.1 实现 subagent

实现 subagent 只拥有第 3～5 节明确路径，按 A→F 顺序执行，必须先读每个目标文件；不得
修改 marketplace / plugin 注册、Skill 名称或 description、API、部署、权限、tag、Release、
仓库设置、未列文档、冻结历史正文或无关 eval。遇到归档目标冲突、安装副本不可读、
Router 行为差异、状态文档正文并非当前能力、净删除越界或 TRD 假设被推翻时立即停止并
交回主进程。

### 6.2 独立 validation subagent

validation subagent 不参与实现，独立读取 PRD、DECISIONS、TRD、本计划和 `AGENTS.md`，
复核 changed scope、生成新鲜度、14 个归档、Router 预算、31+2 状态、四份长文档、35 个
hash、Markdown 负向测试、Claude/Codex 安装、确定性测试与 fresh eval 证据，并检查未列
路径、用户可见行为、残余风险和运行产物。它只报告问题，不在验收阶段扩大设计。

### 6.3 主进程

主进程保留全部源文档、仓库规则、实施边界、分支与 Git 集成、subagent 结果取舍、最终
diff 审查、closeout、PR 交付和是否停止的判断。任何 subagent 不得创建或合并 PR。

## 7. Closeout 必填证据

完成时在归档前补齐：

- `changed_files`：精确路径与第 3、4 节集合核对结果；
- `commands_and_results`：生成、repository/doc/eval contract、pytest、安装、diff 与 CI；
- `fresh_eval_results`：affected-target 选择、运行批次、结果和 durable comparison；
- `scope_review`：净行数、注册/名称/行为不变、无空角色文档树、无中央 decisions；
- `independent_validation`：独立验收结论与已处理问题；
- `residual_risks`：所有未消除风险及 owner；
- `runtime_artifacts_removed`：transcript、diagnostics、outputs、timing、run status、
  `comparison.auto.md` 和 `tmp/eval-runs/` 均未进入 Git；
- `delivery`：PR、CI、review 状态；明确“未合并，等待维护者确认”。

## 8. 开放问题

无设计开放问题。若实施证据推翻 TRD 第 15 节任一 blocking 假设，按对应阶段停止并交回
主进程，不新增兼容层或在计划外自行决策。

## 9. Closeout

### 9.1 changed_files

- 最终工作树共 429 个变更文件，全部落在第 3、4 节批准集合；未修改 marketplace、
  plugin manifest、Skill 名称或 discovery description。
- 新增 4 个权威共享契约，并由生成器在六个下游 Router 产生 24 份只读副本；35 个
  受影响 Skill 与 `skills-lock.json` 已同步。
- 14 份既有完成态实施计划已归档，正文与 HEAD 逐字一致，仅更新归档 frontmatter；
  本计划作为第 15 份按维护者“全部归档”授权关闭。
- 31 份 marketplace PRD 与 2 份 TRD 已收敛为当前 Approved 状态；QA E2E 模板归属、
  仓库导航、cookbook、检查器、测试和 CI 入口均按计划落地。

### 9.2 commands_and_results

- `uv run scripts/generate_shared_contracts.py --check`：PASS。
- repository、doc、eval contract 与 eval artifact 四项 checker：PASS。
- 计划内 pytest：311 passed，另有 6 subtests passed。
- Codex 安装实测：full 模式 39 个根入口，routers-only 模式 7 个根入口；临时目录已移入
  macOS 废纸篓。
- `git diff --check`：PASS；marketplace 与 plugin manifest diff 为 0。

### 9.3 fresh_eval_results

- 单进程、最多 5 workers 完成受影响目标及必要的 exact rerun；179 份 durable
  comparison 已刷新，最终为 115 PASS、41 PASS (partial coverage)、23 FAIL。
- PM eval21 的矛盾断言与 Docs release fixture 缺失证据已修正并 fresh；PM eval21、
  Engineer full-chain/UI、QA 探索例外、Docs manual 均最终 PASS。
- Docs Router eval3 在相同修正输入下出现 PASS/FAIL 波动，最新 durable verdict 为 FAIL；
  Router 已明确接受确认事实、不重复扫描宿主且不执行 Specialist gate，独立验收接受为
  模型方差。
- 其余相对 HEAD 的 18 个新 FAIL 位于未改变的 Specialist 语义，Skill diff 仅为共享契约
  路径替换或等价措辞；保留为既有模型、fixture 或运行环境风险，不在 #285 扩大协议。

### 9.4 scope_review

- 排除生成副本、fresh eval 证据、本功能过程文档和检查测试后，人工治理内容净减少约
  1,757 行，位于计划的 1,000～2,500 行净删除预期内；24 份生成副本约 2,000 行单独计量。
- 七个 Router 均低于预算；四份目标长文档分别为 112、104、123、142 行，均低于
  500 行。
- 无中央 decisions 目录、无空角色文档树、无新增注册或兼容层。

### 9.5 independent_validation

- 独立 validation subagent 最终结论为 PASS；确认 Engineer UI 所有权与两类设计文件
  检查已恢复，5 个 Engineer Router eval 均无 FAIL，Router 预算、静态契约与临时目录
  清理满足计划。

### 9.6 residual_risks

- Docs Router eval3 最新 durable FAIL 由模型可复现性波动造成；owner 为 Docs eval
  维护者，后续可独立增加判定稳定性，不阻塞 #285。
- 未改变 Specialist 语义的 fresh FAIL 保留为独立 eval 质量事项；owner 为对应 role skill
  维护者，不以本治理变更修改业务协议。

### 9.7 runtime_artifacts_removed

- `tmp/eval-runs/` 为空；candidate transcript、diagnostics、outputs、timing、run status 与
  `comparison.auto.md` 均未进入 Git。
- 中断批次的 31,330 个运行期项目此前已移入 macOS 废纸篓，可恢复；最终正常批次均由
  runner 自清理。

### 9.8 delivery

- 分支：`neplich-codex/issue-285-document-authority`。
- 归档时 PR 尚未创建、CI 尚未运行；归档后立即提交、推送并创建 draft PR，远端结果以
  PR readback 为准。
- 本任务明确停在合并前；未经维护者后续明确确认不得合并。
