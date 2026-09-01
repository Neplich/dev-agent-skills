---
title: "debugger 只读诊断模式决策记录"
type: DECISIONS
version: "1.0.1"
status: Approved
author: "Neplich Codex"
date: "2026-08-13"
last_updated: "2026-09-01"
generated_by: "idea-to-spec"
feature: "skill-debugger"
feature_path: "agents/engineer-agent/skills/debugger"
parent_feature: "agents/engineer-agent/skills"
feature_level: "4"
related_issue: "https://github.com/Neplich/dev-agent-skills/issues/274"
related_docs:
  - "docs/pm/agents/engineer-agent/skills/debugger/PRD.md"
changelog:
  - version: "1.0.1"
    date: "2026-09-01"
    changes: "清理已失效的 eval 机制残留引用"
  - version: "1.0.0"
    date: "2026-08-13"
    changes: "确认 debugger 双模式、零修改边界与修复重新入场规则"
---

# debugger 只读诊断模式决策记录

## 已确认决策

| ID | 决策 | 理由 |
| --- | --- | --- |
| D-001 | 本请求分类为 `existing_update`、`change_tier: major`，功能路径固定为 `agents/engineer-agent/skills/debugger`。 | 变更同时影响 PM 路由、Engineer 路由、debugger 行为和三组 eval，属于跨角色契约面变化。 |
| D-002 | 在现有 `debugger` 中增加 `diagnosis_only`，不新增平行 skill。 | 复现、证据收集与根因判断已经由 debugger 拥有；新增 skill 会造成能力和治理门禁重复。 |
| D-003 | PM/Engineer 的只读诊断 handoff 显式携带 `mode: diagnosis_only` 和 `allowed_mutations: none`。 | 下游必须能机械辨认只读边界，不能仅依赖自然语言推断。 |
| D-004 | `allowed_mutations: none` 覆盖代码、测试、E2E、配置、数据库写入、外部状态以及 commit、push、PR。 | 只读诊断的核心承诺是仓库和外部系统状态均不改变。 |
| D-005 | `diagnosis_only` 可读取代码、文档、配置、日志、只读查询结果和运行状态；可能产生持久副作用的复现不得执行。 | 诊断需要充分证据，但不能以“辅助复现”为由扩大修改权限。 |
| D-006 | 缺少 PRD/TRD 时仍允许客观诊断，但必须标记 `expected_behavior_alignment: unaligned`。 | 产品预期缺失不应阻断事实收集，也不能被自动推断为实现缺陷。 |
| D-007 | 诊断报告分开陈述已证实事实、推断和未确认信息，并给出根因置信度、影响范围和最小下一步。 | 让用户能够区分证据强度，避免把可能性误读成确定结论。 |
| D-008 | `diagnosis_only` 输出报告后停止，不生成 repair plan，不询问是否立即修复。 | 只读请求的终点是诊断结论，不应主动推进到修改阶段。 |
| D-009 | 后续修复请求必须重新进入正常 PM/Engineer handoff、PRD/TRD 对齐、repair plan confirmation、最小修复和验证流程。 | 只读诊断提供的信息可以复用，但其授权不能复用。 |
| D-010 | 新增四条路由与行为 eval；三项目标 skill 变化后共 32 条 eval 需要 fresh，模型执行必须单独获得授权。（eval 机制已随 #301 移除，本条不再执行） | 新行为必须覆盖 PM 路由、Engineer 路由、无文档诊断和修复重新入场；计划确认不等于模型消耗授权。 |

## 约束

- 不新增 skill、注册项、feature flag、配置项或运行时抽象。
- 不削弱现有 `debugger` 修复 checkpoint 和 repair-plan confirmation。
- 除不修改已移除机制相关的历史表述外，本决策不引入新的验证基础设施。
