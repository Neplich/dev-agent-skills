# QA Agent

`qa-agent` 是证据优先的 QA dispatcher skill，负责把验收验证、探索测试、缺陷分析和回归复测请求路由到合适的 QA specialist skill。它的目标不是“多测一点”，而是产出可追溯、可交接的质量证据。

> [!NOTE]
> 其他语言：[English](./README.md)

> [!NOTE]
> 独立 QA 或 E2E 请求应先复用 `docs/qa/{feature}/` 下的既有测试用例，再决定是否扩充探索范围。

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 入口 skill | `qa-agent` |
| Specialist skills | 4 个 |
| 主要输入 | PM 文档、测试用例、代码变更、PR 描述、失败日志、截图、录屏 |
| 主要输出 | 验证矩阵、探索报告、缺陷报告、回归结论 |
| 下游协作 | 实现缺陷交给 `engineer-agent`，需求缺口交给 `pm-agent` |

## Skill 清单

| Skill | 适用场景 | 主要产物 |
| --- | --- | --- |
| `qa-agent` | QA 请求入口与路由 | 下游 skill 选择与执行路径 |
| `spec-based-tester` | 按 PRD/TRD/Test Spec 做文档化验收 | 测试摘要、通过/失败判定、覆盖缺口、证据 |
| `exploratory-tester` | 冒烟、边界发现、体验探索 | 探索记录、异常发现、风险点、待确认事项 |
| `bug-analyzer` | 复现失败、整理缺陷、判断影响 | 复现步骤、失败证据、缺陷矩阵、影响评估 |
| `regression-suite` | 验证修复、扫回归、复核已知问题 | 回归结果、修复确认、残余风险 |

## 路由规则

- 文档化验收、规范验证：使用 `spec-based-tester`
- 探索式发现、冒烟、边界发现：使用 `exploratory-tester`
- 失败复现、缺陷写作、归因整理：使用 `bug-analyzer`
- 修复验证、回归扫测、已知问题复核：使用 `regression-suite`

默认规则：先判断用户要的证据类型，再选择最小足够的 QA skill，不把探索测试伪装成全量验收。

## 用例持久化

QA 独立使用时的默认目录：

```text
docs/
└── qa/
    └── {feature-name}/
        ├── TEST_SPEC.md
        ├── FILE_EXPLORATION.md
        ├── test-cases/
        │   └── TC-NNN-<short-slug>.md
        └── reports/
```

工作顺序：

1. 读取 `TEST_SPEC.md` 和 `test-cases/*.md`
2. 询问是否有新功能变化、是否需要扩充文件探索
3. 仅在需要时更新 `FILE_EXPLORATION.md` 和新增 test case
4. 基于持久化用例执行验证并输出报告

## 典型工作流

```mermaid
flowchart LR
    Input["PM docs / PR / bug report"] --> QA["qa-agent"]
    QA --> Spec["spec-based-tester"]
    QA --> Explore["exploratory-tester"]
    QA --> Bug["bug-analyzer"]
    QA --> Regression["regression-suite"]
    Spec --> Evidence["QA evidence"]
    Explore --> Evidence
    Bug --> Engineer["engineer-agent"]
    Regression --> Release["release owner"]
```

## 协作边界

- QA 输出证据、风险和复现材料，不直接修改生产代码。
- 实现问题交给 Engineer；需求或验收标准问题交给 PM。
- QA 报告应明确区分已验证、未覆盖、被阻塞和残余风险。

## 本地维护

```bash
# 安装某个 QA skill 到当前项目运行时
npx skills add ./agents/qa/skills/spec-based-tester

# 运行 QA eval
uv run agents/qa/test/run_all_evals.py
```
