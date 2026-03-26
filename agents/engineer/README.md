# 工程师 Agent

基于 PM 产品文档的纯实现层工程师 Agent，主要职责是将 PRD、TRD、ADR、API Spec、Test Spec 转化为可运行的代码和测试。

## Agent 定位

- **使用者**：个人使用（手动触发）
- **核心场景**：基于 PM Agent 产出的文档进行代码实现、测试编写、调试修复、交付管理
- **输入来源**：项目 `docs/` 目录下的 PM 文档（PRD / TRD / ADR / API Spec / Test Spec）
- **输出形式**：代码文件、测试文件、Git 提交、GitHub PR
- **技术栈**：通用（根据项目自动适配）

---

## Skill 清单

> 所有 skill 源文件统一在 `agents/engineer/skills/` 下自管理，通过 `npx skills add ./agents/engineer/skills/<name>` 安装到项目运行时。

### 按开发阶段排列

| Skill | 目录 | 主要用途 | 阶段 |
|-------|------|---------|------|
| `codebase-analyzer` | `skills/codebase-analyzer/` | 扫描已有项目的结构、技术栈、规范、依赖，生成 Project Profile | 1. 理解 |
| `project-bootstrap` | `skills/project-bootstrap/` | 基于 TRD 初始化新项目（智能选择官方 CLI 或手动搭建） | 2. 搭建 |
| `feature-implementor` | `skills/feature-implementor/` | 核心：读取 PM 文档 → 拆分实现步骤 → 逐步编码 → 自检 | 3. 编码 |
| `test-writer` | `skills/test-writer/` | 基于 Test Spec + 代码编写测试并运行验证 | 4. 测试 |
| `debugger` | `skills/debugger/` | 复现、定位、修复 bug，回归验证 | 5. 调试 |
| `delivery` | `skills/delivery/` | Git 分支管理、Commit、PR 创建、CI 状态检查 | 6. 交付 |

---

## 与 PM Agent 的接口

| PM 文档 | Engineer 消费方 | 获取内容 |
|---------|----------------|---------|
| PRD | feature-implementor | 功能需求、用户故事、验收标准 |
| TRD | feature-implementor, project-bootstrap | 技术方案、架构决策、组件划分 |
| ADR | feature-implementor | 关键技术决策和约束 |
| API Spec | feature-implementor | 接口契约、请求/响应格式 |
| Test Spec | test-writer | 测试场景、测试数据、覆盖要求 |

---

## 设计原则

1. **文档驱动** — PM 文档是唯一的需求来源
2. **先读后写** — 修改任何代码前必须先理解现有代码
3. **最小变更** — 只改需要改的
4. **规范优先** — 跟随项目已有的编码风格和结构
5. **渐进加载** — 只加载当前步骤需要的内部模块
6. **可独立触发** — 每个 skill 可以单独使用
7. **GitHub 原生** — 通过 `gh` CLI 交互
