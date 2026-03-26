# QA Agent 设计文档

> **设计日期**: 2026-03-27
> **Agent 类型**: 智能探索型质量保证 Agent
> **协作对象**: PM Agent, Engineer Agent

---

## 1. Agent 定位

**QA Agent** 是一个智能探索型质量保证 Agent，既能执行基于规范的标准测试，也能自主探索发现文档未覆盖的问题。

### 核心职责
- 基于 Test Spec 执行规范测试
- UI 自动探索测试（发现意外问题）
- 边界和异常场景测试
- Bug 分析和详细报告
- 回归测试管理

### 使用场景
- **使用者**: 个人使用（手动触发）
- **输入来源**: PM Agent 的 Test Spec + PRD + TRD
- **输出形式**: 测试报告（简洁版）+ Bug 报告（详细版）
- **测试范围**: UI 交互测试 + 边界测试（补充 Engineer 未覆盖的场景）

---

## 2. 技术栈

### 测试框架
- **Playwright**: UI 交互测试（浏览器自动化）
- **目标浏览器**: Chrome（优先支持）

### 测试数据策略
- **优先级 1**: 从 Test Spec 读取 PM 定义的标准测试数据
- **优先级 2**: 自动生成边界测试数据（空值、超长字符串、特殊字符、负数等）
- **存储位置**: `test-data/` 目录（可复用）

### Bug 报告输出
- **本地项目**: Markdown 文件（`docs/bugs/bug-NNN.md`）
- **GitHub 项目**: 自动创建 GitHub Issue（带 `bug` 标签）
- **自动检测**: 通过 `gh` CLI 判断是否连接到远程仓库

---

## 3. Skills 设计

### Skill 1: `exploratory-tester`
**用途**: 自动探索 UI，发现文档未覆盖的问题

**核心功能**:
- 模拟用户随机操作（点击、输入、滚动、导航）
- 发现崩溃、错误提示、性能问题
- 记录异常行为和复现路径
- 生成探索测试报告

**输入**:
- 应用 URL
- 探索时长配置（默认 10 分钟）

**输出**:
- 发现的异常列表
- 复现路径记录

---

### Skill 2: `spec-based-tester`
**用途**: 基于 Test Spec 执行标准测试用例

**核心功能**:
- 读取 Test Spec + PRD + TRD
- 生成测试用例（UI 交互 + 边界测试）
- 使用 Playwright 执行测试
- 生成测试报告

**测试类型**:
1. **UI 交互测试**: 用户流程、表单提交、页面跳转
2. **边界测试**: 异常输入、极端值、空值、特殊字符

**输入**:
- `docs/test-spec.md`
- `docs/prd.md`
- `docs/trd.md`

**输出**:
- 测试报告（简洁版）
- 失败用例列表

---

### Skill 3: `bug-analyzer`
**用途**: 分析测试失败，生成详细 Bug 报告

**核心功能**:
- 分析测试失败原因
- 生成详细 Bug 报告
- 自动截图和日志收集
- 选择输出方式（Markdown 或 GitHub Issue）

**Bug 报告格式**:
```markdown
# Bug #NNN: [标题]

**严重程度**: Critical / High / Medium / Low
**发现时间**: YYYY-MM-DD HH:MM
**复现率**: 100% / 偶现

## 复现步骤
1. 打开页面 [URL]
2. 点击 [按钮]
3. 输入 [数据]
4. 观察结果

## 预期结果
[描述预期行为]

## 实际结果
[描述实际行为]

## 环境信息
- 浏览器: Chrome 120.0
- 操作系统: macOS 14.0
- 应用版本: v1.2.3

## 相关日志
```
[错误堆栈或日志]
```

## 截图
![screenshot](path/to/screenshot.png)

## 关联文档
- Test Spec: docs/test-spec.md#section-3
- PRD: docs/prd.md#feature-login
```

**输入**:
- 测试失败信息
- 截图和日志

**输出**:
- `docs/bugs/bug-NNN.md` 或 GitHub Issue

---

### Skill 4: `regression-suite`
**用途**: 管理回归测试套件

**核心功能**:
- 维护回归测试用例集
- Engineer 修复后手动触发验证
- 更新测试套件状态
- 生成回归测试报告

**工作流程**:
1. Bug 修复后，QA 手动触发回归测试
2. 执行相关测试用例
3. 验证修复效果
4. 更新测试套件状态

**输入**:
- Bug ID 或 PR 链接
- 回归测试范围

**输出**:
- 回归测试报告
- 测试套件状态更新

---

## 4. 测试环境管理

### 环境启动策略

**检测流程**:
1. 检测应用是否已运行（端口探测）
2. 如果未运行，按以下顺序尝试启动：
   - 读取 `deploy/local.md` 获取启动命令
   - 尝试常见启动方式：
     - `npm run dev` / `npm start`
     - `yarn dev` / `yarn start`
     - `pnpm dev`
     - `docker-compose up`
3. 启动后等待健康检查（HTTP 200 响应）
4. 健康检查通过后开始测试

### 健康检查
- 最大等待时间: 60 秒
- 检查间隔: 2 秒
- 检查方式: HTTP GET 请求根路径

---

## 5. 输出规范

### 测试报告（简洁版）

**位置**: `docs/qa-reports/YYYY-MM-DD-test-report.md`

**格式**:
```markdown
# 测试报告 - YYYY-MM-DD

**执行时间**: YYYY-MM-DD HH:MM - HH:MM
**测试类型**: 规范测试 / 探索测试

## 统计
- 总用例数: 50
- 通过: 45
- 失败: 5
- 跳过: 0

## 失败用例
1. [Bug #001](../bugs/bug-001.md) - 登录表单验证失败
2. [Bug #002](../bugs/bug-002.md) - 用户列表加载超时
...
```

### Bug 报告（详细版）
见 Skill 3 的格式定义

---

## 6. 与其他 Agent 的协作

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

## 7. 设计原则

1. **探索优先** — 不局限于 Test Spec，主动发现潜在问题
2. **环境自适应** — 自动检测和启动测试环境
3. **详细可追溯** — Bug 报告包含完整复现信息
4. **补充而非重复** — 关注 Engineer 覆盖不到的场景（UI 交互、边界条件）
5. **Chrome 优先** — 先保证主流浏览器支持
6. **手动触发** — 不做自动化监听，保持简单

---

## 8. 技术依赖

### 运行时依赖
- Node.js (>= 18)
- Playwright
- Git
- GitHub CLI (`gh`) - 可选，用于创建 Issue

### 项目约定
- `deploy/local.md` - 本地启动文档（由 Engineer Agent 维护）
- `docs/test-spec.md` - 测试规范（由 PM Agent 维护）
- `docs/bugs/` - Bug 报告目录
- `docs/qa-reports/` - 测试报告目录
- `test-data/` - 测试数据目录

---

## 9. 未来扩展

### 短期（v1.0）
- 支持 Chrome 浏览器
- 基础探索测试
- Markdown Bug 报告

### 中期（v2.0）
- 支持 Firefox、Safari
- 性能测试（页面加载时间、资源大小）
- 可访问性测试（WCAG 标准）

### 长期（v3.0）
- 视觉回归测试（截图对比）
- 自动化监听（PR 创建后自动触发）
- AI 辅助 Bug 分析（根因推断）

---

## 10. 风险和限制

### 当前限制
- 仅支持 Chrome 浏览器
- 不支持移动端测试
- 探索测试结果可能不稳定
- 需要手动触发，无自动化流程

### 风险缓解
- 探索测试设置超时和重试机制
- Bug 报告包含详细复现步骤，降低误报
- 优先执行规范测试，探索测试作为补充

---

## 11. 成功指标

- Bug 发现率：每次测试发现的有效 Bug 数量
- 回归测试覆盖率：修复后的回归验证通过率
- 测试执行时间：单次完整测试的耗时
- Bug 报告质量：Engineer 能否根据报告快速定位问题
