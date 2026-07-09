# Engineer Agent

`engineer-agent` 是工程角色的 dispatcher skill，负责把代码库分析、TRD 生成、项目初始化、功能实现、测试补齐、缺陷修复和交付收尾请求路由到合适的工程 specialist skill。

> [!NOTE]
> 其他语言：[English](./README.md)

> [!IMPORTANT]
> Engineer Agent 只在需求或修复目标已经明确时接手。如果用户还在定义产品目标或空仓库里只有一个想法，应先回到 `pm-agent`。

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 入口 skill | `engineer-agent` |
| Specialist skills | 7 个 |
| 主要输入 | PM 文档、可选设计文档、现有代码库、测试结果、失败日志 |
| 主要输出 | TRD、实现计划、代码变更、测试、工程文档、Git commit / PR |
| 上下游协作 | 上游 `pm-agent` / `designer-agent`，下游 `qa-agent` / `devops-agent` / `security-agent` |

## Skill 清单

| Skill | 适用场景 | 主要产物 |
| --- | --- | --- |
| `engineer-agent` | 工程请求入口与路由 | 下游 skill 选择与执行路径 |
| `codebase-analyzer` | 接手现有仓库、理解结构和约束 | Project Profile、技术栈与架构摘要 |
| `trd-gen` | PRD / DECISIONS 确认后的技术计划、API 文档和 ADR 编写 | `docs/engineer/{feature_path}/TRD.md`，可选 `API.md` / `ADR-*.md` |
| `project-bootstrap` | 基于已确认 PRD/TRD 初始化项目 | 项目骨架、基础配置、启动说明 |
| `feature-implementor` | 按已确认 TRD 或设计文档实现功能 | `docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md`、代码变更、必要工程文档 |
| `test-writer` | 补单测、集成测试或验证覆盖 | 测试文件、测试运行证据 |
| `debugger` | 复现、定位、修复 bug 或失败构建 | 最小修复、回归验证证据 |
| `delivery` | 分支、commit、push、PR、交付收尾 | Git 提交、PR、交付摘要 |

## 路由规则

- 理解仓库、技术栈、架构边界：使用 `codebase-analyzer`
- PRD 确认后编写或更新技术计划、API 文档或 ADR：使用 `trd-gen`
- 新项目或新服务初始化：使用 `project-bootstrap`
- 功能实现、行为变更、按设计落地：使用 `feature-implementor`
- 前端代码更新、UI 实现或设计落地：先进入 Engineer；只有设计交付物缺失或过期时才 handoff 到 Designer
- 测试补齐、覆盖率、验证实现：使用 `test-writer`
- bug、失败日志、测试失败、构建失败：使用 `debugger`
- commit、push、PR、交付整理：使用 `delivery`

默认规则：只要请求会改变生产行为，先确认需求来源和代码上下文；只要请求从失败症状开始，优先进入 `debugger`。

## 典型工作流

```mermaid
flowchart LR
    PM["PM 文档 / 决策记录"] --> Engineer["engineer-agent"]
    Design["设计文档"] --> Engineer
    Engineer --> Analyze["codebase-analyzer"]
    Engineer --> Align["现有功能 PRD/TRD 对齐"]
    Analyze --> TRD["trd-gen"]
    Align --> TRD
    TRD --> Plan["确认 IMPLEMENTATION_PLAN"]
    Plan --> Implement["feature-implementor"]
    Plan -. "失败 / 回归" .-> Debug["debugger"]
    Implement --> Test["test-writer"]
    Debug --> Test
    Implement --> QAHandOff["QA E2E handoff package"]
    Debug --> QAHandOff
    QAHandOff --> QA["qa-agent"]
    Test --> Delivery["delivery"]
```

## 工程门禁

现有功能变更、bug fix 和用户可见实现应先完成 PRD/TRD 对齐，再进入工程执行。Engineer 在实现前确认 TRD 和 `IMPLEMENTATION_PLAN.md`；影响用户流程的实现完成后，通过 QA E2E 交接包移交给 QA。

```mermaid
flowchart LR
    Align["PRD/TRD 对齐"] --> TRD["TRD 已确认"]
    TRD --> Plan["IMPLEMENTATION_PLAN 已确认"]
    Plan --> Work["实现 / 修复"]
    Work --> QAHandOff["QA E2E handoff"]
```

## 输入与产物

Engineer 主要消费：

- `docs/pm/{feature_path}/PRD.md`
- `docs/pm/{feature_path}/DECISIONS.md`
- `docs/engineer/{feature_path}/TRD.md`
- `docs/design/{feature_path}/ui-ux-spec.md`
- `docs/design/{feature_path}/visual-system.md`

`feature_path` 是功能级文档的主路径键。新的 Engineer 文档必须镜像 PM 路径，并在
frontmatter 中包含 `feature_path`、`parent_feature`、`feature_level`。旧的单层文档缺少这些字段时，仍兼容为一级功能。

Engineer 的主产物包括技术计划、API / ADR 文档、实现计划、代码和测试：

- `docs/engineer/{feature_path}/TRD.md`
- `docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md`
- `docs/engineer/{feature_path}/API.md`
- `docs/engineer/{feature_path}/ADR-*.md`

## 协作边界

- Engineer 是唯一负责把 PM/Designer 文档转成代码、测试和交付资产的角色。
- Engineer 在 PM 范围确认后负责 TRD、API 文档和 ADR 编写；`feature-implementor` 消费已确认 Engineer 文档并产出实现计划。
- Engineer 不替代 PM 做需求定义，也不替代 Designer 做视觉或交互决策。
- 前端 UI 实现完成 PRD/TRD 对齐后仍由 Engineer 承接；如果 UI/UX 或视觉文档缺失、过期，再由 Engineer 把设计缺口交给 Designer。
- QA 发现实现缺陷时回到 Engineer；发现需求缺口时回到 PM。
- DevOps 和 Security 只在部署、运行、安全审查成为当前目标时介入。

## 本地维护

```bash
# 安装某个 Engineer skill 到当前项目运行时
npx skills add ./agents/engineer/skills/trd-gen

# 查看工程 eval 定义
find agents/engineer/test -path '*/evals/evals.json' -print
```
