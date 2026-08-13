---
title: "研发意图入口与路由过程收敛实施计划"
type: IMPLEMENTATION_PLAN
version: "0.2.0"
status: "Implemented"
author: "Neplich Codex"
date: "2026-08-14"
last_updated: "2026-08-14"
generated_by: "feature-implementor"
feature: "pm-single-entry"
feature_path: "repository-governance/pm-single-entry"
parent_feature: "repository-governance"
feature_level: "2"
change_tier: "major"
implementation_scope: "intent-routing-output"
previous_plan_archive: "docs/engineer/repository-governance/pm-single-entry/archive/IMPLEMENTATION_PLAN-eval-contract-closeout.md"
related_prd: "docs/pm/repository-governance/pm-single-entry/PRD.md"
related_trd: "docs/engineer/repository-governance/pm-single-entry/TRD.md"
related_issues:
  - "https://github.com/Neplich/dev-agent-skills/issues/281"
  - "https://github.com/Neplich/dev-agent-skills/issues/282"
changelog:
  - version: "0.2.0"
    date: "2026-08-14"
    changes: "完成研发意图入口、显式调用优先、7 个 router 输出收敛、42 条 fresh paired eval、确定性验证与独立验收"
  - version: "0.1.0"
    date: "2026-08-14"
    changes: "规划意图优先入口与 7 个 router 路由过程输出收敛；归档前一轮 eval-contract-closeout 计划"
---

# 研发意图入口与路由过程收敛实施计划

## 1. 对齐与门禁

| 项 | 结果 |
| --- | --- |
| PRD | `docs/pm/repository-governance/pm-single-entry/PRD.md` v1.1.0，覆盖 #281 与 #282 |
| TRD | `docs/engineer/repository-governance/pm-single-entry/TRD.md` v1.1.0，实施面和验证策略已确认 |
| Feature path | `repository-governance/pm-single-entry`，PRD/TRD/计划一致 |
| Change tier | `major`：修改默认入口、7 个 router、发现面、文档与 eval 契约 |
| Archive gate | 旧 `eval-contract-closeout` 计划已按批准归档，新计划通过 `previous_plan_archive` 回链 |
| 计划与实施门禁 | Neplich 已于 2026-08-14 明确批准文档、归档、计划和实施，可直接执行至 PR 合并前 |
| PR 策略 | 全部变更放在同一个 PR；PR 不自动合并，合并前向维护者确认 |

## 2. 成功标准

1. 未显式点名能力时，研发请求进入 `pm-agent`，普通非研发请求不进入。
2. 显式点名 `pm-agent`、role agent 或 skill 时，无条件使用被点名能力，其既有 gate 继续执行。
3. docs、PRD、TRD、代码和 marker 仅作为进入 PM 后的上下文与门禁证据。
4. 7 个 router 不再强制展示“已路由到”、routing decision、routing block/YAML、selected
   specialist、owner 等过程信息。
5. 内部分类、specialist gate、handoff packet schema 与职责边界没有变化。
6. 静态契约、确定性测试和 fresh paired eval 得到可审计证据；本次目标不新增
   FAIL，既有无关 FAIL 如实保留。CI 和 PR review 在 PR 阶段继续核对。
7. 创建单一 PR 并停在合并前等待维护者确认。

## 3. 计划文件范围

### 3.1 PM 入口、发现描述和文档

| 路径或类别 | 操作 |
| --- | --- |
| `agents/product_manager/skills/pm-agent/SKILL.md` | 调整判定顺序；保留显式调用；后置上下文检查；删除强制路由输出 |
| `.claude-plugin/marketplace.json` 与 PM plugin description | 同步“研发意图默认入口 + 显式调用”发现语义 |
| `AGENTS.md` | 替换与目标冲突的旧 Scope Guard / 默认入口文案 |
| `README.md`、`README_zh.md`、`.codex/INSTALL.md`、`docs/README.codex.md` | 仅更新直接描述旧触发语义的内容 |
| `agents/product_manager/README.md`、`README_zh.md` | 同步 PM 入口说明 |

### 3.2 七个 router

修改以下 router 的 `SKILL.md`：

- `agents/product_manager/skills/pm-agent/SKILL.md`
- `agents/designer/skills/designer-agent/SKILL.md`
- `agents/engineer/skills/engineer-agent/SKILL.md`
- `agents/qa/skills/qa-agent/SKILL.md`
- `agents/devops/skills/devops-agent/SKILL.md`
- `agents/security/skills/security-agent/SKILL.md`
- `agents/docs/skills/docs-agent/SKILL.md`

每个文件只删除或改写强制显式输出 routing block、routing decision、selected specialist、
owner 或等价过程信息的句子。分类表、gate 指针、specialist entry basis、handoff 和边界规则
保持原样。

### 3.3 必要 PRD 文档

- 更新本 feature 的 PRD/TRD 与本实施计划。
- 仅当 router 自身既有 PRD 明确要求用户侧展示路由过程时，才同步改写对应要求。
- 不因为 SKILL.md 文案删除而扩写新的 router 输出协议。

### 3.4 Eval、确定性测试和 lock

| 类别 | 操作 |
| --- | --- |
| PM entry eval | 新增或改造“无 docs 的研发请求”“有 docs 的非研发请求”“显式调用优先”场景 |
| Router eval | 删除要求 routing block/decision 的 prompt 和断言，保留正确分流、gate、边界与任务结果断言 |
| Durable comparison | 仅根据本轮 fresh paired 结果更新实际受影响的 `comparison.md` |
| Deterministic tests | 覆盖入口三分支，静态确认 7 router 无强制输出要求且 handoff/gate 未丢失 |
| `skills-lock.json` | 重算本 PR 修改过的 skill 目录 `computedHash` |

## 4. 明确禁区

- specialist gate 逻辑；
- PM handoff packet 字段 schema、必填性和 owner 映射；
- 无关 agent、skills、eval 与文档；
- release 版本、tag、release notes 和发布流程；
- 新的隐藏路由协议、输出抽象、配置项或运行时机制；
- PR 合并。

## 5. 实施顺序

1. 更新 PM 自动入口判断与发现描述。
2. 同步 AGENTS、用户文档和 PM Agent README 中直接冲突的旧规则。
3. 删除 7 个 router 的强制路由过程输出要求。
4. 核对受影响 router PRD，只同步实际冲突的既有要求。
5. 由 `skill-eval-runner` 更新受影响 eval、workspace、deterministic tests 和 comparison。
6. 重算 `skills-lock.json` 中受影响 skill hash。
7. 执行静态契约、确定性测试和 fresh paired eval，修复本次范围内失败。
8. 对照 PRD/TRD、计划文件表和禁区审查最终 diff。
9. 创建一个工作 PR，等待 CI 与 Codex Review；处理意见后停在合并前通知维护者。

## 6. 分工

`subagent_split: enabled`

- 实现：由独立 subagent 按第 3～5 节实施，不能修改禁区。
- 验证：由另一独立 subagent 审查 diff、执行静态契约与确定性测试，并核对 fresh eval 证据。
- 主进程：整合文档与实现、处理冲突、确认范围、创建 PR，并在合并前向维护者交付。

## 7. 规模预期

预计整个 PR 净改约 500–900 行，以删除和改写为主，不新增抽象。若明显超出该量级，先
停止实施并核对是否误触 specialist gate、handoff schema、无关 skill 或新的输出协议。

实际暂存 diff 为新增 1729 行、删除 1776 行、raw net -47 行；其中约 500 行来自将上一轮
活动计划忠实复制到新归档文件。排除这份已批准的机械归档后，主体净改约 -548 行，符合
预期量级，未发现范围扩张。

## 8. 验证命令

```bash
uv run scripts/check_repository_contract.py
uv run scripts/check_eval_contract.py
uv run scripts/check_eval_artifacts.py
uv run scripts/check_doc_contract.py
uv run --with pytest pytest <受影响的确定性测试>
git diff --check
```

静态检查通过后，由 `skill-eval-runner` 对实际受影响的 PM entry 与 router eval 执行 fresh
paired validation，最多 10 workers，并根据真实结果更新 durable `comparison.md`。随后检查
GitHub CI 与 Codex Review 状态。

## 9. 验收清单

- [x] PM 自动入口按显式调用、研发意图、非研发直处三分支运行。
- [x] 项目上下文不再作为自动触发首要依据。
- [x] 7 个 router 的强制路由过程输出要求全部移除。
- [x] Specialist gate 与 handoff schema 未被删除或改义。
- [x] 必要发现描述、用户文档和 router PRD 已同步。
- [x] 受影响 eval 与 deterministic tests 已更新。
- [x] `skills-lock.json` 已刷新。
- [x] 本地合同、确定性测试与本次目标 fresh paired eval 通过；既有无关 FAIL 保留。
- [ ] 单一 PR 已创建，CI 和 Codex Review 已完成。
- [ ] PR 未合并，已通知维护者确认。

## 10. 风险

| 风险 | 控制 |
| --- | --- |
| 意图判断过宽或过窄 | 相反场景成对 eval，不依赖 marker 作为断言代理 |
| 显式调用被拒绝 | 单独覆盖显式点名 PM 与下游能力的场景 |
| 删除输出要求时误删路由行为 | 独立验证 subagent 对比 gate、handoff 和 specialist 路由表 |
| comparison 与真实运行不一致 | 只接受本轮 fresh paired 证据，不手工复制旧结论 |
| PR 范围漂移 | 最终逐项对照第 3、4 节与 `git diff --name-only` |

## 11. Closeout 记录

- `changed_files`：PM 入口和发现描述、7 个 role router、直接冲突的用户/角色文档与
  PRD/TRD、入口与 router eval、42 份 fresh comparison、PM 确定性测试、7 个 skill
  lock hash，以及上一轮计划归档。
- `commands_and_results`：repository/eval/artifact/doc 四项 contract 全部 PASS；独立全仓
  pytest `318 passed, 6 subtests passed`；`git diff --check` PASS；`tmp/eval-runs/` 已清理。
- `fresh_eval_results`：7 个既有 router 的 41 项 affected-target regression 已完成；新增
  `eval-021-explicit-downstream-specialist` fresh PASS。PM 21 项无 FAIL，Designer、Engineer、
  QA、DevOps、Security router 无 FAIL。Docs router 保留 eval-004、005、006 三项变更前已
  存在的 FAIL；eval-004 已恢复为原有单一 entry-basis 缺陷，没有新增 handoff/输出断言
  回归。本次需求引入的 FAIL 为 0。
- `scope_review`：共享 handoff contract、specialist gate、eval runtime 和 release 流程均
  未修改；raw net -47 行，排除约 500 行忠实计划归档后主体净改约 -548 行，未新增输出
  协议或抽象。
- `independent_validation`：独立只读验收提出的下游显式调用覆盖、Docs eval-004 断言和
  README 中文措辞问题已修复并 fresh/静态复核。
- `residual_risks`：Docs eval-004、005、006 的既有 skill 缺陷仍按 fresh FAIL 保存，超出
  #281/#282 范围，后续应独立处理。
- `next_owner`：创建单一 draft PR，等待 GitHub CI 与 review；不得自动合并。
