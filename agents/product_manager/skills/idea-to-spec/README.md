# idea-to-spec

`idea-to-spec` skills 组的公共入口 skill。

`idea-to-spec` 负责接住用户的第一轮诉求，
先判断当前请求属于哪一类，再按需加载 `_internal/` 下最窄的 `INSTRUCTIONS.md` 指令资源。
它同时负责控制功能设计对话的推进方式，而不仅仅是做文档路由。

## 它覆盖什么

- 从零开始的想法探索与验证
- 基于已有项目的新功能规划
- 基于已有文档的变更影响分析与更新编排
- 面向生成、校验、迭代、流程编排的渐进式交接

## 设计协议

对功能设计类请求，`idea-to-spec` 默认采用以下协议：

- 先做工作区与文档上下文检测
- 每个回合只推进一个待确认决策点
- 在关键设计取舍上先给 `2-3` 个备选方案与 trade-off
- 按固定 section 顺序逐段推进
- 已确认决策写入 `docs/pm/{feature-name}/DECISIONS.md`
- 已收敛 section 增量写入 PM 文档
- 每个阶段结束后做一次文档收束，正文只保留当前有效设计

## 逻辑路线图

```mermaid
flowchart TD
  A["用户请求进入 idea-to-spec"] --> B["Phase 0：检查工作区与文档现状"]
  B --> C{"选择执行路线"}

  C -->|空工作区 + 概念验证| D["greenfield-discovery"]
  C -->|空工作区 + 需要长期文档骨架| E["greenfield-bootstrap"]
  C -->|已有仓库 + 新能力/新模块| F["existing-project-feature"]
  C -->|已有仓库 + 已批准能力或文档变更| G["existing-project-update"]
  C -->|明确要求跑完整流程| H["pipeline"]
  C -->|只看版本差异| I["diff-only"]

  D --> D1["继续留在 idea-to-spec 内"]
  D1 --> D2["单决策点推进 -> 方案比较 -> section 确认"]
  D2 --> D3["增量写入 DECISIONS 与 PM 文档"]
  D3 --> D4["推荐最窄的下一个内部 skill"]

  E --> E1["加载 _internal/orchestration/project-init"]
  E1 --> E2["初始化长期文档骨架"]

  F --> F1["继续留在 idea-to-spec 内"]
  F1 --> F2["读取现有模块、权限、集成关系"]
  F2 --> F3["形成 delta brief"]
  F3 --> F4["section 逐段收敛并落档"]
  F4 --> F5["稳定后路由到 prd-gen，必要时再到 trd-gen"]

  G --> G1["总结需求变更 delta"]
  G1 --> G2["若影响范围不清晰，先加载 change-impactor"]
  G2 --> G3{"受影响的核心文档数量"}
  G3 -->|一个| G4["路由到对应的 *-iteration"]
  G3 -->|多个| G5["路由到 iteration-coordinator"]
  G4 --> G6["补 validator"]
  G5 --> G7["补 validator + trace-check"]

  H --> H1["加载 _internal/orchestration/flow"]
  I --> I1["加载 _internal/analysis/version-differ"]
```

## 内部结构

```text
idea-to-spec/
├─ SKILL.md
├─ README.md
└─ _internal/
   ├─ analysis/
   ├─ gen/
   ├─ iteration/
   ├─ orchestration/
   ├─ validator/
   └─ _shared/
```

以下划线开头的目录都视为内部资源。它们由 `idea-to-spec` 按需加载，内部代理指令统一使用
`INSTRUCTIONS.md` 文件名，不应该作为独立 skill 出现在 marketplace 或自动生成的 skill catalog 中。

## 文档输出约定

feature 文档统一采用短命名体系：

- `docs/pm/{feature-name}/DECISIONS.md`
- `docs/pm/{feature-name}/PRD.md`
- `docs/pm/{feature-name}/BRD.md`
- `docs/design/{feature-name}/...`
- `docs/engineer/{feature-name}/...`
- `docs/qa/{feature-name}/...`
- `docs/devops/{feature-name}/...`
- `docs/security/{feature-name}/...`

## 安装

本地项目安装：

```bash
cp -r agents/product_manager/skills/idea-to-spec .claude/skills/idea-to-spec
```

全局安装：

```bash
cp -r agents/product_manager/skills/idea-to-spec ~/.claude/skills/idea-to-spec
```
