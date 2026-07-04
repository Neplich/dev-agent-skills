---
title: "PM 唯一对外入口与下游编排 PRD"
type: PRD
version: "1.0.0"
status: Draft
author: "Neplich Codex"
date: "2026-07-05"
generated_by: "prd-gen"
feature: "pm-single-entry"
feature_path: "repository-governance/pm-single-entry"
parent_feature: "repository-governance"
feature_level: "2"
last_updated: "2026-07-05"
related_issue: "https://github.com/Neplich/dev-agent-skills/issues/52"
related_docs:
  - "AGENTS.md"
  - "README.md"
  - "README_zh.md"
  - ".claude-plugin/marketplace.json"
  - ".codex/INSTALL.md"
  - "docs/README.codex.md"
  - "agents/product_manager/skills/pm-agent/SKILL.md"
  - "agents/engineer/skills/engineer-agent/SKILL.md"
  - "agents/engineer/skills/feature-implementor/SKILL.md"
  - "agents/engineer/skills/debugger/SKILL.md"
  - "docs/pm/repository-governance/feature-path-contract/PRD.md"
  - "https://github.com/Neplich/dev-agent-skills/issues/61"
  - "https://github.com/Neplich/dev-agent-skills/issues/59"
  - "https://github.com/Neplich/dev-agent-skills/issues/60"
  - "https://github.com/Neplich/dev-agent-skills/issues/55"
changelog:
  - version: "1.0.0"
    date: "2026-07-05"
    changes: "初始版本：定义 PM 唯一对外入口、高召回触发、统一路由编排、下游内部化和防绕过需求"
---

# PM 唯一对外入口与下游编排 PRD

## 1. 背景与动机

本仓库当前将 6 个入口 dispatcher skills 和 28 个 specialist skills 一起暴露在
`.claude-plugin/marketplace.json` 和 Codex skill discovery 中。即使 README 建议优先调用
入口 agent，用户的新需求、问题反馈、修复诉求或上线准备仍可能直接命中
`engineer-agent`、`feature-implementor`、`debugger`、`qa-agent` 等下游能力，绕过 PM 侧的
统一需求判断、范围确认、PRD/TRD 对齐和跨角色编排（issue #52）。

这与现实协作模型不一致：实际项目里，用户提出的新需求、问题反馈、变更想法、测试诉求、
部署诉求或安全诉求，都应先从 PM 侧进入，由 PM 判断它是新需求、现有功能变更、缺陷、
验证、部署、安全审查，还是需要继续澄清，再编排到下游角色。

issue #61 为「防绕过」需求提供了直接证据：34 个 skill 的 frontmatter description 全部常驻
harness 上下文（router 类普遍 500-670 字符，合计约 10KB），且 router 与 specialist 的触发
短语大量重叠。例如「实现这个功能」同时出现在 `engineer-agent`（router）和
`feature-implementor`（specialist）的 description 中。harness 层由模型基于 description 自主
选择 skill，完全可能直接命中 specialist、跳过 router，router 精心设计的路由前置检查
（Existing Feature Alignment Gate、PM Handoff Guardrail 等）随之被绕开。当前的实际缓解
方式是把 gate 复制进 specialist，功能上兜住了，但造成 issue #59 描述的三层重复维护。

本 PRD 更新并覆盖早先的「6 个 role-based agent 对外入口」方案。新的目标是：`pm-agent`
是唯一对外公开入口；其他 role agent 和 specialist skills 都变成 PM 编排下的内部/下游能力，
同时正面回答 #61 提出的双入口架构决策问题。

## 2. 目标与非目标

### 目标

1. 对外只推荐和公开 `pm-agent` 作为唯一用户入口。
2. `pm-agent` 扩大触发范围，能捕获近似、模糊、不完整的需求和问题表达（高召回）。
3. `pm-agent` 负责统一路由和编排：需求澄清、范围判断、feature_path 解析、PM 文档更新、
   下游角色 handoff、执行状态追踪。
4. `engineer-agent`、`designer-agent`、`qa-agent`、`devops-agent`、`security-agent` 不再作为
   用户公开入口，而是 PM handoff 后的下游 role capability。
5. 28 个 specialist skills 保留目录和协议能力，但定位为 role agent 或 PM 编排下的内部
   执行模块，不再面向用户直接触发。
6. 防止「用户提了一个新需求，直接被 `engineer-agent` / `feature-implementor` 响应并进入
   实现」的路径；承认平台无法完全阻止直接触发时，提供明确的纵深防御与降级策略。
7. 消除 router 与 specialist 触发描述的重叠（#61），让路由竞争行为可预期、gate 不因入口
   不同而失效。

### 非目标

1. 不删除或迁移任何 specialist skill 目录；协议能力全部保留。
2. 不改变 PRD、TRD、实施计划、QA E2E 等既有文档契约的职责边界。
3. 不在本 feature 内实现 #59 的 gate 去重和 #60 的 SKILL.md 瘦身，但本 PRD 的决策会约束
   它们的方向（见 FR-004 与 TRD 决策记录）。
4. 不承诺在 Claude Code / Codex 平台机制上「物理隐藏」非 PM skill；只承诺发现面收口与
   行为层防绕过（降级策略在 TRD 中明确）。
5. 不引入新的运行时服务或 CI 强制拦截；防绕过通过文档契约、description 分工和 eval 保障。

## 3. 用户画像

| 用户画像 | 描述 | 核心诉求 | 痛点 |
| --- | --- | --- | --- |
| 终端用户 | 在自己项目里安装本 marketplace 的开发者。 | 说一句需求就能被正确编排，不需要先学 34 个 skill 的分工。 | 直接命中下游 skill 后跳过范围确认，产出与预期不符。 |
| 仓库维护者 | 维护 Agent skill 行为、文档契约和 eval 的人。 | 路由竞争行为可预期，治理规则不因入口不同而失效。 | router/specialist 描述重叠，gate 被绕过时只能靠三层复制兜底。 |
| Skill 作者 | 维护单个 agent 或 specialist skill 的人。 | description 分工清晰，改一处不用同步多处。 | 触发短语互相抄写，改任意一条要检查多个文件。 |
| 下游 Agent 使用者 | 已有明确 PM handoff、需要执行下游能力的用户。 | 携带 handoff packet 时下游直接承接，不被反复拉回 PM。 | 收口过严会让明确的执行请求也被强制绕路。 |

## 4. 用户故事与场景

| ID | 用户故事 | 优先级 | 验收标准 |
| --- | --- | --- | --- |
| US-001 | 作为终端用户，我说「做一个新功能」时希望先进入需求澄清，而不是直接被写代码。 | P0 | 请求命中 `pm-agent`，PM 完成分类和范围确认后才 handoff Engineer，`feature-implementor` 不直接响应。 |
| US-002 | 作为终端用户，我报告一个 bug 时希望先确认预期，而不是被直接「修掉」。 | P0 | 请求命中 `pm-agent`，先做预期分类（预期冲突回 PM，实现偏离 handoff debugger）。 |
| US-003 | 作为终端用户，我提出部署/安全/测试诉求时希望 PM 记录目标、范围和风险后再编排。 | P0 | 请求命中 `pm-agent`，分类后按 handoff packet 交给 DevOps/Security/QA。 |
| US-004 | 作为携带已确认 handoff 的用户，我希望下游直接承接，不被重复拉回 PM。 | P0 | 请求携带明确 PM handoff packet（或等效已确认文档链）时，下游 role agent 直接执行。 |
| US-005 | 作为维护者，我希望用户直接点名下游 agent/specialist 时有可预期的防绕过行为。 | P0 | 无 handoff packet 的直接触发默认回 `pm-agent` 分类；specialist 内 gate 保留作为纵深防御。 |
| US-006 | 作为 Skill 作者，我希望 router 和 specialist 的 description 不再互相抄触发词。 | P0 | specialist description 收敛为弱触发表述，router/PM description 承担用户侧短语；无重叠触发短语。 |
| US-007 | 作为维护者，我希望 eval 能持续验证 PM-only 入口和防绕过行为不回退。 | P0 | PM 入口 eval 覆盖 FR-006 列举的用户起点场景与直接点名下游的防绕过场景。 |

## 5. 功能需求

### FR-001: PM agent 是唯一公开入口（P0）

- `README.md`、`README_zh.md`、`.codex/INSTALL.md`、`docs/README.codex.md` 等安装与使用
  文档只把 `pm-agent` 描述为用户可直接调用的入口；其余 role agent 和 specialist 均描述为
  「PM 编排下的下游/内部能力」。
- `.claude-plugin/marketplace.json` 的 plugin 与 skill description 收口公开发现面：非 PM 入口
  的描述改写为 handoff 后使用的定位，不再包含用户侧第一人称触发短语。
- Codex 安装逻辑（symlink 安装模型）保持 skill 目录完整安装（下游能力仍需可被 PM 编排
  调用），但安装文档的「可直接调用入口」只列 `pm-agent`。
- 平台限制导致无法完全隐藏其他 agent / specialist（Claude Code 与 Codex 的 skill discovery
  均基于 frontmatter description，凡安装即可被模型选中）；降级策略必须在 TRD 中明确，
  候选包括：internal-only 标记、frontmatter 触发描述弱化、触发后强制回 PM。

验收标准：用户文档中唯一被推荐直接调用的入口是 `pm-agent`；TRD 有明确的平台约束
分析和降级策略决策。

### FR-002: PM agent 高召回触发（P0）

`pm-agent` 的 description / routing contract 必须覆盖所有用户侧起点，而不只覆盖传统产品
工作：

- 新想法、新功能、新模块、空仓库产品形态。
- 现有功能行为调整、体验调整、规则变更、文案变更。
- 用户报告问题、bug、异常现象、失败日志、CI 失败。
- 「帮我实现 / 改一下 / 修一下 / 补测试 / 提 PR」等工程诉求。
- 设计、页面、交互、视觉系统诉求。
- 验收、冒烟、复测、回归、探索测试诉求。
- 部署、CI/CD、环境变量、Docker/Helm、发布、回滚、runbook 诉求。
- 安全、权限、登录、依赖、secrets、隐私、数据流、webhook/upload 等风险诉求。
- GitHub issue / PR / milestone / release / changelog / roadmap / repo status 诉求。

验收标准：`pm-agent` description 覆盖上述九类起点的代表性短语；FR-006 的 eval 场景全部
命中 `pm-agent`。

### FR-003: PM 先分类，再 handoff（P0）

`pm-agent` 必须先把请求分类，而不是直接放行到下游：

| 请求类型 | PM 处理 | Handoff 条件 |
| --- | --- | --- |
| 新需求或范围未定 | 停留在 PM，走 `idea-to-spec` / PRD / DECISIONS。 | PRD/范围确认后才 handoff Engineer。 |
| 现有功能变更 | 先走 PM existing-project-update，更新 PRD 或产品决策。 | PRD 更新后同步 TRD，再 handoff。 |
| 用户报告 bug | 先判断是否与现有 PRD/TRD 预期冲突。 | 预期不清或变更诉求回 PM；确认实现偏离后 handoff Engineer/debugger。 |
| 设计诉求 | 先确认是设计产物需求还是前端实现需求。 | 设计产物 handoff Designer；前端实现需 PM/TRD/设计对齐后 handoff Engineer。 |
| 测试诉求 | 先确认测试依据（PRD/TRD/已确认实施计划）。 | 预期未确认不得让 QA 或 test-writer 固化新预期。 |
| 部署/运维/安全诉求 | PM 记录目标、范围和风险。 | 记录完成后 handoff DevOps/Security。 |
| 已完成工作交付 | 确认变更范围和验证状态。 | 确认后 handoff Engineer/delivery，不得绕过状态确认。 |

分类时同步判定变更等级（`change_tier`，衔接 issue #55 / PR #68 的变更分级契约）：
`hotfix` 与交付/状态查询类请求走 fast lane，分类后立即放行；新需求、预期变更、范围不清
一律留在 PM。

验收标准：每类请求都有明确的 PM 处理动作与 handoff 条件；fast lane 不跳过分类本身。

### FR-004: 下游 agent 不直接响应用户入口（P0）

- 5 个下游 role agent（Engineer、Designer、QA、DevOps、Security）的公开触发描述调整为
  「PM handoff 后使用」；specialist 的 description 移除与用户侧起点重叠的触发短语，改为
  弱触发表述（#61 方案 B 语义应用于 specialist 层）。
- 用户直接点名下游 agent 或 specialist 时，默认先回到 `pm-agent` 做入口分类，除非该请求
  已携带明确、已确认的 PM handoff packet（或等效的已确认 PRD/TRD/实施计划文档链）。
- `feature-implementor` 不得直接响应「新需求 / 改功能 / 做个功能 / 帮我实现」等用户原始
  请求。
- `debugger` 不得直接响应用户报告的 bug 并进入修复；必须先有 PM/PRD/TRD 预期对齐或
  PM handoff。
- `qa-agent` 不得在预期未确认时直接生成或更新 E2E 预期。
- 承认平台无法完全阻止直接触发：specialist 内的入口校验 gate 保留作为纵深防御（deep
  defense），即使 description 弱化后仍被直接命中，gate 依然执行并把无凭据请求拉回 PM。
  该决策同时约束 #59（gate 去重时唯一权威副本放 specialist，router/PM 留指针）和 #60
  （SKILL.md 瘦身不得把入口 gate 摘除出 specialist 入口文件）。

验收标准：无 handoff packet 的直接触发在行为上回到 PM 分类；specialist description 不再
包含用户侧原始触发短语；gate 在绕过 router 直接触发场景下仍然执行。

### FR-005: PM handoff packet 标准化（P0）

PM handoff 到下游角色时必须携带结构化输入：

| 字段 | 说明 |
| --- | --- |
| `request_type` | new_feature / existing_update / bug_report / validation / deployment / security / delivery / status 等。 |
| `change_tier` | hotfix / standard / major（衔接 issue #55 / PR #68 的变更分级契约；契约未合入前由 PM 按同一定义判级）。 |
| `feature_path` / `feature` / `parent_feature` / `feature_level` / `feature_path_evidence` | 功能归属主键与证据，遵循 feature-path-contract。 |
| `source_documents` | PRD / DECISIONS / TRD / design docs / issue / PR / release context。 |
| `scope_decision` | 本次范围、非目标、是否改变已批准预期。 |
| `downstream_owner` | Designer / Engineer / QA / DevOps / Security / delivery 等。 |
| `required_output` | 下游需要产出的文档、计划、实现、报告或验证证据。 |
| `blockers_risks` | 缺失文档、未确认决策、平台限制、验证风险。 |

验收标准：packet 字段被文档化；下游 agent 把 packet（或等效已确认文档链）作为入口
校验依据。

### FR-006: Eval 覆盖 PM-only 入口（P0）

需要新增或改造 eval，验证以下路径：

1. 用户说「做一个新功能」，命中 `pm-agent`，不会直接进 `feature-implementor`。
2. 用户说「帮我修这个 bug」，命中 `pm-agent`，先做预期分类，再 handoff debugger。
3. 用户说「帮我补测试」，命中 `pm-agent`，先确认测试依据，再 handoff QA 或
   Engineer/test-writer。
4. 用户说「更新前端 UI」，命中 `pm-agent`，再判断 PM / Designer / Engineer 路径。
5. 用户说「部署一下 / 配 CI / 上线前检查」，命中 `pm-agent`，再 handoff DevOps。
6. 用户说「看下权限 / 依赖漏洞 / secrets 风险」，命中 `pm-agent`，再 handoff Security。
7. 用户直接调用下游 agent 或 specialist 时，如果没有 PM handoff packet，应被拉回 PM 分类。
8. 绕过 router 直接触发 specialist 时（#61 场景），specialist 内 gate 仍然执行。

验收标准：eval 使用 schema `1.0` 与语义断言；实际执行后更新 durable `comparison.md`。

## 6. 用户流程

```mermaid
flowchart TD
    U["用户请求（任意起点）"] --> PM["pm-agent 入口分类"]
    PM --> C{"请求类型 + change_tier"}
    C -->|新需求 / 范围未定| Spec["idea-to-spec: PRD / DECISIONS"]
    C -->|现有功能变更| Update["PM existing-project-update -> 同步 TRD"]
    C -->|bug 报告| Align{"与 PRD/TRD 预期冲突？"}
    Align -->|预期不清 / 预期变更| Spec
    Align -->|实现偏离| HE["handoff Engineer / debugger"]
    C -->|设计诉求| DQ{"设计产物 or 前端实现？"}
    DQ -->|设计产物| HD["handoff Designer"]
    DQ -->|前端实现| HE
    C -->|测试诉求| TQ{"测试依据已确认？"}
    TQ -->|否| Spec
    TQ -->|是| HQ["handoff QA / test-writer"]
    C -->|部署 / 安全| HO["记录目标范围风险 -> handoff DevOps / Security"]
    C -->|交付 / 状态 (fast lane)| HL["确认范围与验证状态 -> handoff delivery / github-reader"]
    Spec --> Packet["PM handoff packet"]
    Update --> Packet
    Packet --> Down["下游 role agent / specialist 执行"]
    Direct["用户直接点名下游 / specialist"] --> Guard{"携带 handoff packet 或已确认文档链？"}
    Guard -->|否| PM
    Guard -->|是| Down
```

## 7. 验收标准

| ID | 验收标准 | 验证方式 |
| --- | --- | --- |
| AC-001 | 用户文档只把 `pm-agent` 描述为公开入口。 | 审查 README / README_zh / `.codex/INSTALL.md` / `docs/README.codex.md`。 |
| AC-002 | 新需求、功能变更、bug、测试、部署、安全、交付请求默认先进入 PM 分类和编排。 | PM 入口 eval（FR-006 场景 1-6）。 |
| AC-003 | 无 PM handoff packet 时，下游 role agent / specialist 不直接承接用户原始请求。 | 防绕过 eval（FR-006 场景 7-8）。 |
| AC-004 | `feature-implementor` 不直接响应用户新需求并进入实现。 | `feature-implementor` eval 与 gate 审查。 |
| AC-005 | PM handoff packet 字段被文档化，并被下游 agent 作为入口校验依据。 | 审查 PM skill-map / handoff contract 与下游 SKILL.md。 |
| AC-006 | PM-only 入口 eval 覆盖主要用户侧起点和防绕过场景。 | `check_eval_contract.py` + fresh subagent validation + `comparison.md`。 |
| AC-007 | repository contract、eval contract、eval artifacts 检查通过。 | 三个契约脚本 + pytest。 |
| AC-008 | 平台无法完全隐藏非 PM skills 时，TRD 明确残余风险和降级策略。 | 审查 `docs/engineer/repository-governance/pm-single-entry/TRD.md`。 |
| AC-009 | router 与 specialist 的 description 不再互相抄触发词（#61）。 | description 分工审查 + 绕过 eval。 |

## 8. 发布计划与里程碑

| Phase | Scope | Owner |
| --- | --- | --- |
| PRD/TRD（本次交付） | 固化需求、平台约束分析、#61 入口策略决策和实施拆分。 | PM / Engineer |
| Implementation Plan | 待在途 PR（#57/#64/#65/#66/#67/#68）合并后，由 `feature-implementor` 产出。 | Engineer |
| 实施批次 | 按 TRD 第 8 节分批 PR 实施。 | Engineer |
| Eval | 更新并执行 PM 入口与防绕过 eval，刷新 durable `comparison.md`。 | Engineer / QA |
| Release Preflight | 运行仓库契约、eval 契约和 artifact 检查。 | Maintainer |

## 9. 风险与缓解

| 风险 | 影响 | 缓解 |
| --- | --- | --- |
| 平台机制无法物理隐藏非 PM skill，收口只是「弱化 + 行为拦截」。 | 直接触发仍可能发生。 | specialist 内 gate 作为纵深防御；eval 覆盖绕过场景；TRD 记录残余风险。 |
| specialist description 弱化过度，导致携带 handoff 的合法调用也触发不到。 | 编排链路断裂，PM 无法调用下游。 | description 保留「PM/router handoff 后使用」的明确定位短语；eval 覆盖 handoff 放行场景。 |
| PM 高召回描述过宽，抢走本应直达的非工作型请求。 | 简单状态查询被拖入重流程。 | FR-003 fast lane：delivery/status/hotfix 分类后立即放行。 |
| 所有请求过 PM 增加流程成本，反向促使用户绕开流程。 | 与收口目标冲突。 | `change_tier` 分级放行（衔接 #55）；分类本身保持轻量。 |
| description 大改与在途 PR（#57/#64-#68）冲突。 | 大面积 merge 冲突。 | 本次 docs-only；实现推迟到在途 PR 合并后分批进行。 |

## 10. 假设与待确认问题

| 类型 | 内容 | Owner | Blocking |
| --- | --- | --- | --- |
| Decision | 入口策略采用「PM 收口 + specialist description 弱化 + specialist 内 gate 纵深防御」，不采用 #61 纯方案 A（双入口对等）。理由与影响见 TRD 决策记录。 | Maintainer | No |
| Decision | 本 feature 使用 `repository-governance/pm-single-entry` 作为 feature_path，覆盖 issue #52 中建议的 `agent-collaboration/pm-only-public-entry` 路径口径。 | Maintainer | No |
| Assumption | `change_tier` 分级契约（issue #55 / PR #68）先于或与本 feature 实现阶段同步合入；未合入时 PM 按 PRD 中同一定义判级。 | Maintainer | No |
| Assumption | 实现阶段在在途 PR #57/#64/#65/#66/#67/#68 合并后进行，避免 SKILL.md / AGENTS.md 大面积冲突。 | Maintainer | No |
| Open Question | marketplace.json 是否需要为非 PM plugin 增加显式 `internal` 类元数据字段（取决于 Claude Code marketplace schema 支持度），或仅通过 description 收口。 | Engineer | No |
