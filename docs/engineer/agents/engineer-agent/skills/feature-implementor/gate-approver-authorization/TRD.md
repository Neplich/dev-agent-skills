---
title: "计划与 TRD 门禁批准者授权 TRD"
type: TRD
version: "0.1.1"
status: Approved
author: "Neplich Codex"
date: "2026-08-20"
last_updated: "2026-09-01"
generated_by: "trd-gen"
feature: "gate-approver-authorization"
feature_path: "agents/engineer-agent/skills/feature-implementor/gate-approver-authorization"
parent_feature: "agents/engineer-agent/skills/feature-implementor"
feature_level: "5"
related_prd: "docs/pm/agents/engineer-agent/skills/feature-implementor/gate-approver-authorization/PRD.md"
related_issue: "https://github.com/Neplich/dev-agent-skills/issues/316"
changelog:
  - version: "0.1.1"
    date: "2026-09-01"
    changes: "按 skill 最新约定补齐 frontmatter 字段（changelog）"
---

# 计划与 TRD 门禁批准者授权 TRD

## 1. 技术目标

通过 PM handoff packet 的可选字段，为实施计划门禁和 TRD 门禁增加显式授权的
自动审查批准路径。既有人工确认仍是缺省路径，自动审查只改变批准凭据来源，
不跳过产物审查或降低门禁标准。

## 2. 技术边界

- 权威字段只定义在 PM 共享 handoff contract 中。
- 下游角色继续读取生成的本地副本，不手工维护副本内容。
- `plan_approval` 只控制实施计划门禁，`trd_approval` 只控制 TRD 门禁。
- 门禁未收到显式授权时，必须继续等待用户确认。
- 不新增配置文件、运行时依赖、抽象层、脚本或测试资产。

## 3. Handoff 字段契约

在 Diagnosis-Only Optional Extension 相邻位置增加批准方式可选扩展：

```yaml
plan_approval: user | authorized_auto_reviewer
trd_approval: user | authorized_auto_reviewer
```

两个字段均缺省为 `user`。字段缺失、值为 `user` 或无法确认字段来源时，
门禁只能由用户批准。一个字段的授权不得推导出另一个字段也已授权。

## 4. 自动审查者最低要求

| Requirement | Technical Rule | Blocking Condition |
| --- | --- | --- |
| 独立上下文 | 审查者不与撰写者共享会话，只读目标产物和 PRD、DECISIONS、TRD 等上游文档。 | 同会话自审或继承撰写推理。 |
| 显式边界 | 审查 prompt 携带来自 PRD `non_goals` 的「有意不做」清单。 | 清单缺失或来源不明。 |
| 发现定级 | 每条发现标注 `P0`、`P1` 或 `P2`。 | 存在未定级发现。 |
| 收敛条件 | 某轮零确认缺陷，或达到轮数上限且当轮无未解决 `P0` 或 `P1`。 | 尚未满足任一条件。 |
| 升级路径 | 上限轮仍有未收敛 `P0` 或 `P1` 时生成一个待人工回答的问题。 | 不得自行批准。 |

## 5. 实施计划门禁

`feature-implementor` 在 public skill、planner 和 implementor 三处统一采用以下规则：

1. 默认展示精确计划并等待用户确认。
2. 只有 handoff packet 显式携带
   `plan_approval: authorized_auto_reviewer` 时，才接受自动审查批准。
3. 自动审查者必须满足第 4 节全部最低要求。
4. 审查输入必须包含六字段预期改动声明，批准后的声明成为 closeout 对账基线。
5. hotfix 仍需确认；批准者来源变化不改变其轻量计划形态。

预期改动声明是审查和对账的问询触发器，不是代码规模或文件数量的准入上限。

## 6. TRD 门禁

`trd-gen` 的流程图、进入阶段话术、Quality Checks 和最终硬门禁统一采用
`trd_approval` 授权规则。TRD 侧没有实施 diff，因此不建立量化对账模型。

TRD 自动审查只使用以下定性改动面清单：

- 涉及哪些模块或组件；
- 是否改动数据结构；
- 是否引入新依赖。

TRD 审查的判定确定性低于实施计划与实际 diff 的对账。TRD 侧应单独设置足够的
轮数上限，不复用实施层经验推导轮数，也不把实施层验证结论外推到技术设计阶段。

## 7. 文件影响

| Area | File | Change |
| --- | --- | --- |
| Handoff authority | `agents/product_manager/skills/idea-to-spec/_internal/_shared/handoff-contract.md` | 增加批准方式扩展和五项最低要求。 |
| Plan public gate | `agents/engineer/skills/feature-implementor/SKILL.md` | 支持显式授权的计划自动审查者。 |
| Plan rendering | `agents/engineer/skills/feature-implementor/_internal/planner/INSTRUCTIONS.md` | 同步批准者条件和预期声明输入。 |
| Implementation entry | `agents/engineer/skills/feature-implementor/_internal/implementor/INSTRUCTIONS.md` | 同步进入实施的有效批准凭据。 |
| TRD gate | `agents/engineer/skills/trd-gen/SKILL.md` | 四处门禁支持 `trd_approval` 并补定性判据。 |
| Generated contracts | 六份 Router 本地 `handoff-contract.md` | 由生成脚本从权威源同步。 |
| Skill lock | `skills-lock.json` | 刷新受影响 local skill 的 `computedHash`。 |

## 8. 生成副本

以下文件只能由 `uv run scripts/generate_shared_contracts.py` 更新：

1. `agents/designer/skills/designer-agent/_internal/_generated/shared-contracts/handoff-contract.md`
2. `agents/devops/skills/devops-agent/_internal/_generated/shared-contracts/handoff-contract.md`
3. `agents/docs/skills/docs-agent/_internal/_generated/shared-contracts/handoff-contract.md`
4. `agents/engineer/skills/engineer-agent/_internal/_generated/shared-contracts/handoff-contract.md`
5. `agents/qa/skills/qa-agent/_internal/_generated/shared-contracts/handoff-contract.md`
6. `agents/security/skills/security-agent/_internal/_generated/shared-contracts/handoff-contract.md`

## 9. 验证策略

```bash
uv run scripts/generate_shared_contracts.py --check
uv run scripts/check_repository_contract.py
uv run scripts/check_doc_contract.py
git diff --cached --check
```

验收时同时人工核对：两个批准字段的缺省行为、五项最低要求、计划预期声明输入、
TRD 定性改动面和六份副本与权威源的一致性。

## 10. 兼容与回滚

新增字段是可选扩展，既有 handoff packet 不需要迁移。标准 git revert 可以同时回滚
权威契约、生成副本、两个 skill 门禁和 lock hash；回滚后两类门禁恢复为仅接受用户确认。

## 11. 已决技术结论

| # | Decision | Rationale |
| --- | --- | --- |
| 1 | 授权字段进入共享 handoff contract。 | 让 PM 明确授权来源，并由所有下游读取同一契约。 |
| 2 | 两类门禁使用独立字段。 | 防止计划授权被误用于 TRD，或反向继承。 |
| 3 | 自动审查保持独立上下文。 | 避免撰写者在同一会话中自证通过。 |
| 4 | TRD 使用定性改动面，不建立虚假量化对账。 | 设计阶段没有实际 diff 可作为逐项实际值。 |
| 5 | 本次不新增 ADR。 | 已决方案直接落入现有共享契约和 skill 门禁，没有额外技术分叉。 |
