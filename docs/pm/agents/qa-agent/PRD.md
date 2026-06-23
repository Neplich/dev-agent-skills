---
title: "qa-agent — Product Requirements Document"
type: PRD
feature: "agent-qa-agent"
feature_path: "agents/qa-agent"
parent_feature: "agents"
feature_level: "2"
version: "1.0.0"
status: Draft
author: "Neplich Codex"
date: "2026-06-12"
last_updated: "2026-06-23"
generated_by: "prd-gen"
related_docs:
  - "agents/qa/README.md"
  - "agents/qa/README_zh.md"
  - ".claude-plugin/marketplace.json"
  - "agents/qa/skills/qa-agent/SKILL.md"
  - "agents/qa/skills/qa-agent/references/e2e-credential-store.md"
  - "agents/qa/skills/qa-agent/references/e2e-test-report.md"
  - "skills-lock.json"
  - "agents/qa/test/qa-agent/evals/evals.json"
  - "docs/pm/feature-path-contract/PRD.md"
  - "docs/engineer/feature-path-contract/TRD.md"
  - "docs/engineer/feature-path-contract/IMPLEMENTATION_PLAN.md"
changelog:
  - version: "1.0.0"
    date: "2026-06-12"
    changes: "Initial version"
---

# qa-agent PRD

## 背景

`qa-agent` 是 QA Agent 的统一入口，负责规范验收、探索测试、缺陷分析和回归验证。它的产品目标是把用户的角色级请求分流到一个最小足够的 specialist skill，而不是把一次请求扩展成全量流水线。

## 目标

1. 作为入口 dispatcher，识别用户意图并选择一个主 route。
2. 保持 route matrix 与 README、dispatcher `SKILL.md`、marketplace 和 skill 目录一致。
3. 在需要跨角色协作时说明 owning agent、输入包和期望产物。
4. 支持后续维护者通过 related docs 和 eval fixture 追踪行为漂移。

## 非目标

- 不把 `qa-agent` 自身当作下游 specialist route。
- 不默认同时执行所有 specialist skills。
- 不替代 engineering debugging，不预设端口/框架/浏览器，不把验证默认扩大为 broad discovery，不强制全量测试。

## 用户画像

| Persona | Description | Key Needs | Pain Points |
|---------|-------------|-----------|-------------|
| 交付团队用户 | 通过 Codex / Claude Code 发起角色级任务的人 | 用自然语言进入正确 specialist workflow | 不知道该直接调用哪个 skill |
| Agent 维护者 | 维护 README、SKILL.md、marketplace、eval 和 PRD 的人 | 让路由、产物和边界可验证 | 文档泛化会掩盖实现差异 |
| 下游角色 Agent | 消费本 Agent 输出继续工作的角色 | 获得清晰 handoff 和当前限制 | 上游输出过宽会导致返工 |

## 用户故事与场景

| ID | User Story | Priority | Acceptance Criteria |
|----|-----------|----------|---------------------|
| US-A01 | 作为用户，我想通过 `qa-agent` 进入规范验收、探索测试、缺陷分析和回归验证流程，以便获得最小足够的 specialist 处理。 | P0 | 给定匹配请求，输出一个主 route、选择理由和下一步产物。 |
| US-A02 | 作为维护者，我想确认 route matrix 不自路由、不全量执行，同时能表达 E2E 持久化流程，以便和 eval 及 README 保持一致。 | P0 | 流程图表达最小主 route，并包含 E2E case memory、执行入口顺序和报告归档约束。 |
| US-A03 | 作为下游 Agent，我想收到明确 handoff，以便继续工作时不重猜上下文。 | P1 | handoff 包含 target、source docs、blocked reason 或 expected output。 |

## 功能需求

| ID | Feature | Description | Priority | Acceptance Criteria |
|----|---------|-------------|----------|---------------------|
| FR-A00 | Entry Dispatcher | `qa-agent` 必须作为入口 dispatcher，负责激活角色级流程。 | P0 | README、marketplace 和 entry SKILL 都指向 `qa-agent`。 |
| FR-A01 | Route Matrix | Dispatcher 必须只选择一个最小主 route，除非用户明确要求更广链路。 | P0 | 主 route 属于 `spec-based-tester`, `exploratory-tester`, `bug-analyzer`, `regression-suite`，不包含 `qa-agent` 自身。 |
| FR-A02 | Context Boundary | Dispatcher 只收集路由所需上下文；实现/审查/测试细节由被选 specialist 收集。 | P0 | 缺少内容级上下文不会让入口停在元路由。 |
| FR-A03 | Artifact Ownership | 下游 specialist 拥有具体产物写入和验证责任。 | P0 | Dispatcher 输出预期产物类型，不伪装成 specialist report。 |
| FR-A04 | Handoff | QA 内部先选一个最窄 specialist；实现缺陷交 engineer-agent，需求/验收缺口交 pm-agent，发布判断交 release owner。 | P0 | Handoff 指向 owning skill/agent，并说明输入包和期望输出。 |
| FR-A05 | E2E Case Memory | 对 feature-update 或 release E2E 工作，必须先确认测试场景和 platform version，读取 `TEST_SUITE.md`、`FLOW_INDEX.md`、`cases/*.md`、`scripts/*.spec.md`、历史 `results/` 和 `_reports/`；现有功能、bug fix 或代码完成后的 E2E 更新必须消费同一 `feature_path` 下的 PRD/TRD/IMPLEMENTATION_PLAN。 | P0 | 缺 platform version、路径不清、PRD/TRD 不一致或缺已确认 plan 时 blocked；执行默认由 subagent 负责；入口顺序为 repo harness > Chrome plugin / browser connector > Playwright fallback；凭据只引用本地账号 ID；汇总报告使用 `e2e-test-report.md`。 |
| FR-A06 | Feature Path Gate | QA 不拥有 feature path 决策权，只消费已确认路径。 | P0 | 缺 PRD 回 PM；缺 TRD 或 plan 回 Engineer；不得创建/更新/执行 E2E acceptance TC。 |

## 当前实现对齐

### 路由矩阵

| Route | Current Implementation Trigger |
|---|---|
| `spec-based-tester` | 按 PRD/TRD/Test Spec 做验收验证 |
| `exploratory-tester` | 冒烟、边界发现、UX 探索、变更后的风险探索 |
| `bug-analyzer` | 复现失败、证据分类、缺陷材料 |
| `regression-suite` | 修复验证、回归扫测、已知问题复核、release readiness |

## 验收标准

| ID | Criteria | Verification |
|----|----------|--------------|
| AC-01 | Agent route matrix 与 README、entry SKILL、marketplace 和 skill 目录一致，且不自路由。 | 对照 related_docs 和 `.claude-plugin/marketplace.json` 人工 review。 |
| AC-02 | 默认只选择一个最小主 route，除非用户明确要求更广链路。 | 检查功能需求、路由矩阵和 Mermaid flow。 |
| AC-03 | 跨角色 handoff 指向 owning agent/skill，并包含输入包与期望产物。 | 检查功能需求、用户流程和 handoff 描述。 |

## 非功能需求

| Category | Requirement | Metric | Target |
|----------|-------------|--------|--------|
| Accuracy | route 与 README / SKILL / marketplace 一致 | Review / eval | P0 场景无自路由或误路由 |
| Traceability | 关键行为能回到 related docs | 文档链接 | route、artifact、handoff 均有来源 |
| Maintainability | 新增/删除 skill 后 PRD 可同步 | repository contract | skill 清单一致 |
| Safety | 不输出凭据或越权修改 | 静态审查 | 0 secrets |

## 用户流程

```mermaid
flowchart LR
    User["用户请求"] --> Entry["qa-agent"]
    Entry --> Context["读取路由级上下文"]
    Context --> Decision{"选择一个最窄主 route"}
    Decision --> spec_based_tester["spec-based-tester"]
    Decision --> exploratory_tester["exploratory-tester"]
    Decision --> bug_analyzer["bug-analyzer"]
    Decision --> regression_suite["regression-suite"]
    Decision --> Output["QA artifact 或 route decision"]
    Output --> E2ECheck{"是否是 E2E/验收 TC 更新或执行?"}
    E2ECheck -->|否| Handoff["QA 内部先选一个最窄 specialist；实现缺陷交 engineer-agent，需求/验收缺口交 pm-agent，发布判断交 release owner。"]
    E2ECheck -->|是| E2EGate["确认 feature_path、feature-update/release、platform version、同路径 PRD/TRD/IMPLEMENTATION_PLAN"]
    E2EGate --> Memory["读取 TEST_SUITE、FLOW_INDEX、cases、scripts、results、_reports"]
    Memory --> Execute["subagent 默认执行；repo harness > Chrome/browser > Playwright"]
    Execute --> Report["凭据只引用账号 ID；按 e2e-test-report 归档"]
    Report --> Handoff
```

Alternative flow: 如果 route 目标真正不清，最多提出一个路由级澄清问题。

Error flow: 如果请求属于其他角色，转交 owning agent，而不是继续扩大本 Agent 范围。

## 交互与输出要求

- 回复优先呈现选中的 route、原因、需要的输入和可交付结果。
- 对非技术用户保留必要边界，不暴露内部协议细节为强制前置知识。
- 不把全量 chain 画成默认路径；broader chain 必须有明确用户目标。

## 数据模型

| Entity | Key Attributes | Relationships |
|--------|----------------|---------------|
| Agent | name, role, entry_skill, source_dir | owns specialist routes |
| Skill | name, trigger, output, boundary | selected_by Agent |
| Request | intent, scope, constraints, evidence | routed_to Skill |
| Artifact | path, type, owner, status | produced_by Skill |
| Handoff | target, packet, expected_output | links Agent/Skill |

## 接口与文件触点

| Endpoint | Method | Purpose | Request | Response |
|----------|--------|---------|---------|----------|
| `.claude-plugin/marketplace.json` | File read | 获取 Agent 与 skill 注册 | JSON | registered routes |
| `agents/qa/README.md` | File read | 获取角色边界和 route matrix | Markdown | role contract |
| `agents/qa/skills/qa-agent/SKILL.md` | File read | 获取 dispatcher 协议 | Markdown | route behavior |
| `skills-lock.json` | File read | 追踪 skill metadata | JSON | lock consistency |

## 假设与约束

| Type | Description | Impact if Wrong |
|------|-------------|-----------------|
| Constraint | `AGENTS.md` 是仓库指导唯一来源。 | 指导分叉会导致 PRD 与实现不一致。 |
| Constraint | Agent 协作通过 Markdown 和项目资产完成，不依赖共享状态机。 | PRD 不应写成强制流水线。 |
| Assumption | 当前 specialist 清单来自 marketplace 和目录。 | 新增 skill 后需要同步本 PRD。 |

## 相关实现文档

- Internal: `agents/qa/README.md`, `agents/qa/README_zh.md`, `.claude-plugin/marketplace.json`, `agents/qa/skills/qa-agent/SKILL.md`, `agents/qa/skills/qa-agent/references/e2e-credential-store.md`, `agents/qa/skills/qa-agent/references/e2e-test-report.md`, `skills-lock.json`, `agents/qa/test/qa-agent/evals/evals.json`。
- Internal: 对应 eval fixture / comparison 用于行为回归。
- External: Codex / Claude Code 的 skill discovery 或 plugin marketplace。

## 发布计划与里程碑

| Phase | Scope | Target Date | Owner |
|-------|-------|-------------|-------|
| Draft | 生成并校验 Agent PRD | 2026-06-12 | PM |
| Review | 对齐 route matrix、handoff 和 related docs | TBD | Maintainer |
| Adopt | 后续 skill 行为变化时同步更新 | TBD | Maintainer |

## 风险与缓解

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Dispatcher 被写成自路由 | Medium | 用户误以为存在循环 route | PRD 与 eval 均要求无自路由 |
| 一次请求执行所有 specialist | Medium | 范围膨胀 | route matrix 明确一个主 route |
| 新增 skill 后 PRD 过期 | Medium | 文档漂移 | 将 PRD 更新纳入 skill 维护 checklist |

## 待确认问题

| # | Question | Owner | Deadline | Resolution |
|---|----------|-------|----------|------------|
| 1 | 是否把 PRD 与 marketplace/skills-lock 一致性纳入 repository contract？ | Maintainer | TBD | Unresolved |
| 2 | 是否为 Agent PRD 建立独立 validator？ | Maintainer | TBD | Unresolved |
