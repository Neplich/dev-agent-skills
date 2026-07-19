---
title: "Formal Docs Sync 多类型扩展实施计划"
type: IMPLEMENTATION_PLAN
version: "0.4.1"
status: Implemented
author: "Neplich Codex"
date: "2026-07-19"
last_updated: "2026-07-19"
generated_by: "feature-implementor"
feature: "formal-docs-sync"
feature_path: "agents/docs-agent/formal-docs-sync"
parent_feature: "agents/docs-agent"
feature_level: "3"
implementation_scope: "formal-docs-sync-multitype"
related_prd: "docs/pm/agents/docs-agent/formal-docs-sync/PRD.md"
related_trd: "docs/engineer/agents/docs-agent/formal-docs-sync/TRD.md"
related_issues:
  - "https://github.com/Neplich/dev-agent-skills/issues/121"
changelog:
  - version: "0.4.1"
    date: "2026-07-19"
    changes: "记录 issue #117 target_release_version handoff 收紧后的邻接 fresh 回归"
  - version: "0.4.0"
    date: "2026-07-19"
    changes: "记录 S2c 维护者决策：eval-010 改为语义 handoff 断言并完成 fresh validation，S2 门禁解除"
  - version: "0.3.0"
    date: "2026-07-19"
    changes: "记录 S2 fresh validation 结果：eval 001-009 PASS，eval 010 NON-PASS，交付门禁阻塞"
  - version: "0.2.0"
    date: "2026-07-19"
    changes: "完成 S1 实现、lock hash 刷新、仓库契约检查与 CI 同款 Python 回归"
  - version: "0.1.0"
    date: "2026-07-19"
    changes: "记录维护者已确认的 issue #121 S1 实现与 S2 eval 交付计划"
---

# Formal Docs Sync 多类型扩展实施计划

## 1. 实施依据与确认状态

- 已批准 PRD：`docs/pm/agents/docs-agent/formal-docs-sync/PRD.md`。
- 已批准 TRD：`docs/engineer/agents/docs-agent/formal-docs-sync/TRD.md`。
- GitHub issue：#121；`request_type: existing_update`；`change_tier: major`。
- Feature metadata：`agents/docs-agent/formal-docs-sync`，父功能
  `agents/docs-agent`，层级 `3`。
- 硬前置 #118 与 #122 已合并；#116 站内 Release Notes specialist 已交付；#117 是
  同步后的审计与统一盖章 owner。
- 维护者已明确批准总纲并要求直接执行：S1 完成实现和确定性验证；S2 完成 eval、fresh
  validation、durable comparison 与后续交付。S2c 将 eval-010 的 issue 编号字面要求修订
  为 specialist handoff 语义断言；本轮 fresh judge 判定 PASS，当前计划状态为
  `Implemented`，交付门禁已解除。

## 2. 目标与非目标

目标是把现有 `formal-docs-sync` 从 API-only 已验收范围扩展为 API、database、design、
ops、product 五类同步；以四模式和通用八步站点契约组织执行；通过五个类型模块实现
单类型渐进加载；消费宿主模板与 `new:doc` 单一来源，并保持 #116/#117/#118/#122 边界。

非目标：新增重复 specialist；复制宿主模板正文或 AI Hub 业务事实；定义 frontmatter；
盖章；生成 Release Notes；操作 GitHub Release、tag、镜像、Helm 或部署；初始化站点；
迁移非 VitePress 逻辑；新增动态 schema；在 S1 修改现有 eval fixture 或 durable
comparison。

## 3. 分阶段计划

| 阶段 | 内容 | 验证与完成条件 | 状态 |
| --- | --- | --- | --- |
| S1 — 实现 | 建立 Approved 文档链；瘦身 `SKILL.md` 为入口门禁、四模式和流程指针；将 `_internal/INSTRUCTIONS.md` 改为通用八步站点契约；新增 API、database、design、ops、product 五类型模块；落实模式边界、模板消费、design closeout、有限 backfill、缺站 handoff、#116/#117/#118/#122 边界；刷新 `formal-docs-sync` computedHash。 | 渐进加载结构与类型职责静态核对；4 个仓库 checker 和 CI 同款 pytest 全部通过。既有 eval 如仅因旧表述失效则如实记录，不在 S1 修改。 | Completed |
| S2 — Eval 与交付 | 基于 #122 资产扩展 AI Hub-shaped fixtures，覆盖 feature database / design、deployment ops、product sync 和 Release Notes 越界；按同一 prompt / fixture 生成 fresh with-skill 与 fresh without-skill，交由 fresh Codex subagent 评审并更新 durable `comparison.md`；完成最终仓库验证与 PR 交付。 | eval contract / artifact checks 通过；所有本轮 assertions 有 fresh evidence；comparison 与实际结果一致；不提交运行期 transcript、verdict 或 diagnostics；PR 等待 CI / review 与维护者确认，不自动 merge。 | Completed |

```mermaid
flowchart LR
    S1A["S1 文档链"] --> S1B["入口 + 八步通用协议"]
    S1B --> S1C["五类型渐进模块"]
    S1C --> S1D["Lock hash + 确定性验证"]
    S1D --> S2A["S2 多类型 eval fixtures"]
    S2A --> S2B["Fresh with / without + judge"]
    S2B --> S2C["Durable comparison + PR 交付"]
```

## 4. S1 实施清单

### 4.1 文档链

- 创建 level-3 PRD、TRD 与活动实施计划，统一 metadata、Approved 状态和 issue #121
  关联。
- PRD 只保存当前问题、目标、最终决策、范围和验收面；TRD 固化四模式、八步契约、
  渐进加载结构与相邻职责；本计划只定义 S1 / S2 边界。

### 4.2 `SKILL.md` 入口

- 保留 PM handoff 或等效 entry basis、模式特有证据门禁、缺证据 owner 和缺站行为。
- 将模式表更新为五类正式文档已验收范围，删除 API-only MVP / future-target 表述。
- 通用执行细节只指向 `_internal/INSTRUCTIONS.md`；设计 closeout 只保留入口级硬门禁和
  权威内部指针。

### 4.3 通用入口与五类型模块

- `_internal/INSTRUCTIONS.md` 按固定顺序实现八步站点契约。
- 通用入口保留候选范围、change-map 合并、current-state trust model、backfill 单批次、
  缺站、检查、审计 handoff 和报告结构。
- 五类型模块分别只保存本类型的证据清单、目标模板与输出约束；单类型执行不读取其他
  模块。
- Design 模块复用现有七项 closeout gate，不弱化完成、diff、测试和候选确认要求。

### 4.4 模式和职责边界

- Feature delivery：API / database / design / product 与 change map；design 服从 gate。
- Deployment verification：ops / upgrade / rollback 的已验证当前事实。
- Release：只更新受影响 product / ops；Release Notes surface handoff #116。
- Backfill：五类有限确认批次，优先 catalog / map，不全站扩张。
- 所有新改页面应用 #118 并保持 `unverified`，检查成功后 handoff #117。

### 4.5 Lock 与验证

- 只刷新 `skills-lock.json` 中 `formal-docs-sync` 的 `computedHash`。
- 按仓库规定顺序执行四个 checker 与 CI 同款 pytest；检查工作区只包含本任务文件。
- 不运行模型 eval，不修改 `agents/docs/test/formal-docs-sync/**`；旧 fixture 断言若因
  `SKILL.md` 从 API-only 更新为五类而失败，记录为 S2 输入。

## 5. S2 验收计划

S2 至少覆盖：

1. Feature delivery 同时识别 database 与 design，design 失败和成功门禁均有证据。
2. Deployment verification 只把已验证配置、命令、upgrade / rollback 写入 ops。
3. Product 同步基于已交付用户行为，保持当前状态纪律。
4. Release Notes 正文、索引或 metadata 请求不写入并 handoff #116。
5. Backfill 在五类中选择一个有限批次，页面与 map 同确认范围，不扩张到全站。
6. 单类型运行只读取通用入口与目标模块，模板来自宿主 `standards/templates/`。
7. AI Hub-shaped fixture 真实执行 `npm run test:docs`；缺站时 handoff bootstrap。

每个实际执行的 eval 都必须以同一 prompt 和 fixture 重新生成 with-skill 与
without-skill，不复用历史 baseline。最终判断由当前会话中的 fresh Codex subagent
根据 assertions 和两份输出作出，并在同轮更新 durable `comparison.md`。

## 6. 验证命令

S1 按以下顺序执行：

```bash
uv run scripts/check_repository_contract.py
uv run scripts/check_eval_contract.py
uv run scripts/check_eval_artifacts.py
uv run scripts/check_doc_contract.py
```

随后执行 `.github/workflows/ci.yml` 当前定义的同款 pytest 命令。实际命令、测试数量和
退出状态以运行结果为准，不以计划值代替验证证据。

## 7. 风险与缓解

| 风险 | 缓解 |
| --- | --- |
| 通用入口和类型模块重复同一规则 | 共享八步、map、trust model 与报告只保留在入口；类型模块只保留差异。 |
| Skill 内形成第二份模板 | 只引用宿主模板路径和规则，不复制 scaffold 区块或完整章节骨架。 |
| S1 顺手修改旧 eval 掩盖行为变化 | S1 完全不碰 eval；确定性结果如实报告，S2 重新建立 fresh 对照。 |
| Release 模式接管 #116 | 入口、通用协议与相关类型模块都明确 handoff Release Notes surface。 |
| Design 在实现未完成时提前成为正式事实 | 七项 closeout gate 任一失败即页面和 map 零变化。 |
| Backfill 因扫描变成全站生成 | 优先 catalog / map，按有限批次展示并逐次确认。 |
| 新改页面被提前盖章 | S1 固定 `unverified` 并将检查成功结果交给 #117。 |

## 8. 阶段门禁与收尾

- S1 完成后只提交实现、文档链和精确 lock hash，停在功能分支，不 push、不建 PR。
- S1 不宣称 skill eval 已通过；既有 fixture 变化只作为 S2 待办记录。
- S2 必须重新获得实际 eval 运行授权并遵守 fresh baseline 与 durable comparison 契约。
- 后续创建 PR 后仍等待 CI、review 和维护者明确合并确认；不自动 merge、tag、release
  或部署。

## 9. S1 实施结果

- 已完成 `SKILL.md`、通用八步入口和五个类型模块，未新增 specialist。
- `skills-lock.json` 仅刷新 `formal-docs-sync.computedHash` 为
  `66cacc2c5b2009d41ccbd0f23a069b2d0406a1f1341e2bb319550a11d773ec50`。
- 四个确定性 checker 全部通过：repository contract、eval contract、eval artifact
  policy 与 documentation contract。
- CI 同款 Python 测试收集并通过 `128` 项，无失败。
- 当前仓库实际有 `6` 个 formal-docs-sync eval case；本轮未运行模型 eval、未修改
  fixture 或 durable `comparison.md`，原因是 issue #121 已将这些工作明确划入 S2。
- S1 残余风险仅是旧 eval 的自然语言断言可能受 API-only 表述移除影响；须在 S2 通过
  fresh with-skill / without-skill 与 durable comparison 验证，不以本轮确定性检查替代。

## 10. S2 实施结果

### 10.1 Fresh validation 取舍

- 本轮开始时已有的运行目录不沿用。其 fixture 与 skill 文档在运行后仍有修改，且无法
  同时确认每个 eval 的 with-skill、without-skill 与独立 judge 记录都基于最终输入完整
  生成，不满足 fresh validation 沿用条件。
- eval 001-009 的最终结论来自统一协议补强后的第三轮全量 fresh 重跑；eval-010 在 S2c
  断言语义化修订后单独重新生成全新 with-skill 与独立 without-skill baseline，并由独立
  fresh judge 按当前 assertions 评审。
- 运行期 transcript、verdict、timing、status 与 diagnostics 只保留在
  `tmp/eval-runs/121/` 与 `tmp/eval-runs/121-s2c-eval010/`，不作为提交内容。

### 10.2 Eval 结论

| Eval | 场景 | 最终结论 | Durable comparison |
| --- | --- | --- | --- |
| `eval-001-sync-feature-api` | Feature 模式精准同步 API 正式文档 | PASS | `agents/docs/test/formal-docs-sync/evals/workspace/eval-001-sync-feature-api/comparison.md` |
| `eval-002-plan-backfill-batches` | Catalog 优先规划存量 API 回填批次 | PASS | `agents/docs/test/formal-docs-sync/evals/workspace/eval-002-plan-backfill-batches/comparison.md` |
| `eval-003-design-gate-incomplete-scope` | Design 收口门禁阻断未完成范围 | PASS | `agents/docs/test/formal-docs-sync/evals/workspace/eval-003-design-gate-incomplete-scope/comparison.md` |
| `eval-004-design-gate-failing-tests` | Design 收口门禁阻断失败测试 | PASS | `agents/docs/test/formal-docs-sync/evals/workspace/eval-004-design-gate-failing-tests/comparison.md` |
| `eval-005-design-gate-mismatched-evidence` | Design 收口门禁阻断路径证据不一致 | PASS | `agents/docs/test/formal-docs-sync/evals/workspace/eval-005-design-gate-mismatched-evidence/comparison.md` |
| `eval-006-design-gate-all-passed` | Design 收口门禁通过后停在范围确认 | PASS | `agents/docs/test/formal-docs-sync/evals/workspace/eval-006-design-gate-all-passed/comparison.md` |
| `eval-007-feature-database-design` | Feature 模式同步 Database 与 Design 当前状态 | PASS | `agents/docs/test/formal-docs-sync/evals/workspace/eval-007-feature-database-design/comparison.md` |
| `eval-008-deployment-ops-upgrade` | Deployment verification 同步 Ops 与 Upgrade 当前事实 | PASS | `agents/docs/test/formal-docs-sync/evals/workspace/eval-008-deployment-ops-upgrade/comparison.md` |
| `eval-009-release-product-ops` | Release 模式只同步受影响 Product 与 Ops | PASS | `agents/docs/test/formal-docs-sync/evals/workspace/eval-009-release-product-ops/comparison.md` |
| `eval-010-release-notes-boundary` | Release Notes 越界请求阻塞并零写入 handoff | PASS | `agents/docs/test/formal-docs-sync/evals/workspace/eval-010-release-notes-boundary/comparison.md` |

### 10.3 实施完成与门禁解除

- 最终确定性验证全部通过：repository contract、eval contract、eval artifact policy、
  documentation contract 均为 PASS；CI 同款 pytest 共 `128` 项通过、`0` 项失败。
- 维护者判定 eval-010 原 assertion 与 `expected_output` 中的 `issue #116` 字面要求违反
  `AGENTS.md` 的语义断言准则，因此移除该字符串要求；行为语义未变，仍要求将请求与证据
  handoff 给 `docs-agent:release-notes-generator`，而不是 docs-audit、GitHub Release 或
  泛化 PM 路由。
- 修订后的 `eval-010-release-notes-boundary` 已单独执行全新 with-skill、独立生成的
  without-skill baseline 与独立 fresh judge：with-skill 满足 `4/4` assertions，
  without-skill 满足 `1/4` assertions，最终结论为 PASS。
- with-skill 的 `docs/site/` 源文件数保持 41 → 41 且 aggregate hash 不变；baseline
  从 41 → 42 并修改 Release Notes 正文、index 与 metadata，形成明确行为对照。
- S2 已完成，eval-010 阻塞已解除，可以继续 commit、push、PR 与 CI 交付；仍不自动
  merge、tag、release 或部署。
- Issue #117 A2 将成功 handoff 收紧为“仅在维护者已确认 `target_release_version` 时
  进入 pre-tag，否则保持 `unverified` 并 blocked 等待 release context”后，受影响的
  eval-001、007、008、009 已重新生成 fresh with-skill / without-skill，并由独立 judge
  评审为 4/4 case、21/21 assertions PASS；父仓库 Git metadata 可见性仅作为已记录的
  harness limitation，不影响语义结论。
