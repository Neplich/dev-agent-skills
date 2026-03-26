# QA Agent

智能探索型质量保证 Agent，既能执行基于规范的标准测试，也能自主探索发现文档未覆盖的问题。

## Agent 定位

- **使用者**：个人使用（手动触发）
- **核心场景**：UI 交互测试、边界测试、探索测试、Bug 分析、回归验证
- **输入来源**：PM Agent 的 Test Spec + PRD + TRD
- **输出形式**：测试报告（简洁版）+ Bug 报告（详细版，Markdown 或 GitHub Issue）
- **测试范围**：UI 交互测试 + 边界测试（补充 Engineer 未覆盖的场景）

---

## Skill 清单

> 所有 skill 源文件统一在 `agents/qa/skills/` 下自管理，通过 `npx skills add ./agents/qa/skills/<name>` 安装到项目运行时。

| Skill | 目录 | 主要用途 | 阶段 |
|-------|------|---------|------|
| `exploratory-tester` | `skills/exploratory-tester/` | 自动探索 UI，发现文档未覆盖的问题 | 1. 探索 |
| `spec-based-tester` | `skills/spec-based-tester/` | 基于 Test Spec 执行标准测试用例（UI 交互 + 边界测试） | 2. 规范测试 |
| `bug-analyzer` | `skills/bug-analyzer/` | 分析测试失败，生成详细 Bug 报告（Markdown 或 GitHub Issue） | 3. Bug 分析 |
| `regression-suite` | `skills/regression-suite/` | 管理回归测试套件，验证 Bug 修复效果 | 4. 回归验证 |

---

## 与其他 Agent 的协作接口

### 与 PM Agent 的接口

| PM 文档 | QA 消费内容 |
|---------|------------|
| Test Spec | 测试场景、测试数据、覆盖要求 |
| PRD | 功能需求、用户故事、验收标准 |
| TRD | 技术实现细节、架构约束 |

### 与 Engineer Agent 的协作流程

1. **Engineer 实现完成** → 提交代码
2. **QA 手动触发测试** → 执行 `spec-based-tester` + `exploratory-tester`
3. **发现 Bug** → 使用 `bug-analyzer` 生成报告
4. **Engineer 修复** → 提交修复代码
5. **QA 回归验证** → 使用 `regression-suite` 验证修复

---

## 设计原则

1. **探索优先** — 不局限于 Test Spec，主动发现潜在问题
2. **环境自适应** — 自动检测和启动测试环境
3. **详细可追溯** — Bug 报告包含完整复现信息
4. **补充而非重复** — 关注 Engineer 覆盖不到的场景（UI 交互、边界条件）
5. **Chrome 优先** — 先保证主流浏览器支持
6. **手动触发** — 不做自动化监听，保持简单
