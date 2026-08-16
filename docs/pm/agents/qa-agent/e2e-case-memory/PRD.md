---
title: "QA Agent E2E 用例沉淀与复用 PRD"
type: PRD
version: "1.0.10"
status: Approved
author: "Neplich Codex"
date: "2026-05-19"
last_updated: "2026-08-15"
generated_by: "prd-gen"
feature: "qa-e2e-case-memory"
feature_path: "agents/qa-agent/e2e-case-memory"
parent_feature: "agents/qa-agent"
feature_level: "3"
related_issue: "https://github.com/Neplich/dev-agent-skills/issues/18"
related_issues:
  - "https://github.com/Neplich/dev-agent-skills/issues/18"
  - "https://github.com/Neplich/dev-agent-skills/issues/20"
  - "https://github.com/Neplich/dev-agent-skills/issues/21"
  - "https://github.com/Neplich/dev-agent-skills/issues/23"
related_docs:
  - "agents/qa/skills/qa-agent/SKILL.md"
  - "agents/qa/skills/qa-agent/references/e2e-credential-store.md"
  - "agents/qa/skills/qa-agent/references/e2e-case-format.md"
  - "agents/qa/skills/qa-agent/references/e2e-test-report.md"
changelog:
  - version: "1.0.10"
    date: "2026-08-15"
    changes: "收窄为产品要求与验收；凭据、用例、脚本和报告格式迁至 QA reference 唯一 owner"
  - version: "1.0.9"
    date: "2026-06-15"
    changes: "修正 E2E 汇总报告 reference 的当前状态描述"
---

# QA Agent E2E 用例沉淀与复用 PRD

## 1. 背景

QA 应在每次 E2E 工作前复用已有可执行测试记忆，避免重复探索、步骤漂移和结果不可追溯。
持久化资产按 `feature_path` 组织，测试格式由 QA Skill reference 唯一维护。

## 2. 目标与非目标

目标：

1. 功能更新只验证更新功能和直接影响路径，发版执行全部 active E2E 用例。
2. 每个测试流程有稳定 TC、脚本、平台版本和追加式结果。
3. 代码完成后的 E2E 资产引用已确认 PRD、TRD 和实施计划。
4. 凭据只通过本地账号 ID 引用，仓库不保存 secret。
5. 主 Agent 汇总 subagent 执行结果并持久化报告。

非目标：

- 不建设通用 E2E runner、凭据服务或新的测试平台。
- 不把单元测试、Skill eval 或角色过程报告混入 E2E 功能树。
- 不在产品文档复制凭据 schema、TC、脚本或报告模板。

## 3. 用户故事与验收

| ID | 用户故事 | 验收 |
| --- | --- | --- |
| US-001 | QA 复用既有用例 | 执行前读取 suite、flow、case、script 和历史结果 |
| US-002 | 维护者区分功能更新与发版 | 场景、环境、范围与平台版本均明确 |
| US-003 | QA 增量沉淀新流程 | 一项 TC 一个 case，一个对应 script，索引同步 |
| US-004 | 测试执行不泄露凭据 | 仓库资产仅含 credential ID |
| US-005 | 结果可追溯 | 每次结果和汇总报告按平台版本、时间追加 |

## 4. 功能要求

| ID | 要求 | 完成条件 |
| --- | --- | --- |
| FR-001 | 场景分类 | `feature-update` 使用本地开发环境并覆盖直接影响路径；`release` 使用发版测试环境并覆盖全部 active TC |
| FR-002 | 平台版本门禁 | 版本缺失时 blocked，不创建 `unknown` 目录 |
| FR-003 | 预期对齐 | 功能或 bug 改变现有行为时先完成 PRD/TRD 对齐 |
| FR-004 | 实施计划门禁 | 代码完成后补 E2E 文档必须引用已确认实施计划 |
| FR-005 | 持久化结构 | 使用 `docs/qa/e2e/{feature_path}/` 的 suite、flow、cases、scripts、results、reports |
| FR-006 | 执行入口 | repo harness 优先，其次 Chrome/browser connector，最后 Playwright |
| FR-007 | Subagent | 单个 E2E 默认由 subagent 执行，主 Agent 负责范围和汇总 |
| FR-008 | 凭据 | 本地账号文件被 gitignore；文档和脚本只引用 ID |
| FR-009 | 增量历史 | 更新索引和当前 case/script；结果与报告只追加，不覆盖 |
| FR-010 | 结果 | 使用 `pass`、`fail`、`blocked` 并附证据、风险和 owner |

## 5. 用户流程

1. 确认测试场景和平台版本。
2. 解析 `feature_path`，读取既有 suite、flow、case、script 和历史结果。
3. 对功能更新核对 PRD/TRD 与已确认实施计划；发现预期或技术缺口时回对应 owner。
4. 选择 repo harness、Chrome/browser 或 Playwright。
5. 解析 credential ID；缺失或环境不可用则记录 blocked。
6. 执行已有 TC；只有真实覆盖缺口才新增或更新用例。
7. 追加单次结果并由主 Agent生成汇总报告。
8. 发版场景聚合全部 active TC；功能更新只聚合直接影响路径。

## 6. 格式 Owner

- 凭据：[e2e-credential-store.md](../../../../../agents/qa/skills/qa-agent/references/e2e-credential-store.md)
- 用例与脚本：[e2e-case-format.md](../../../../../agents/qa/skills/qa-agent/references/e2e-case-format.md)
- 汇总报告：[e2e-test-report.md](../../../../../agents/qa/skills/qa-agent/references/e2e-test-report.md)

这些 reference 是唯一模板 owner；本 PRD 只定义产品结果。

## 7. 非功能要求与风险

- 可重复：同一 TC 的步骤和断言稳定。
- 可追溯：源 spec、计划、执行入口、版本和证据可定位。
- 安全：任何 secret 都不能进入 Git、报告、fixture 或对话摘要。
- 兼容：历史结果保留，旧功能树内容按维护任务增量迁移。
- 失败安全：缺少版本、预期、计划、凭据、环境或 harness 时 blocked，不伪造结论。

## 8. 发布与完成条件

本能力随 QA Skill 文档和 checker 普通 PR 发布，不需要服务部署或数据迁移。完成要求：
格式 owner 唯一，已有 QA 行为不变，确定性检查和受影响 eval 通过。
