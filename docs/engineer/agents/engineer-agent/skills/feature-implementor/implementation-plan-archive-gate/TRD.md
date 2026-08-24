---
title: "IMPLEMENTATION_PLAN 归档门禁 TRD"
type: TRD
version: "0.2.0"
status: Draft
author: "Neplich Codex"
date: "2026-07-01"
last_updated: "2026-08-12"
generated_by: "trd-gen"
feature: "implementation-plan-archive-gate"
feature_path: "agents/engineer-agent/skills/feature-implementor/implementation-plan-archive-gate"
parent_feature: "agents/engineer-agent/skills/feature-implementor"
feature_level: "5"
related_prd: "docs/pm/agents/engineer-agent/skills/feature-implementor/implementation-plan-archive-gate/PRD.md"
related_issue: "https://github.com/Neplich/dev-agent-skills/issues/54"
related_docs:
  - "docs/pm/agents/engineer-agent/skills/feature-implementor/PRD.md"
  - "agents/engineer/skills/feature-implementor/SKILL.md"
  - "agents/engineer/skills/feature-implementor/_internal/planner/INSTRUCTIONS.md"
  - "agents/engineer/skills/feature-implementor/_internal/reviewer/INSTRUCTIONS.md"
  - "agents/engineer/skills/feature-implementor/_internal/_shared/output-conventions.md"
  - "scripts/check_repository_contract.py"
changelog:
  - version: "0.2.0"
    date: "2026-07-27"
    changes: "Fix issue #172 by making active-plan status mandatory and using the merge-base active-plan status, rather than archive history or scope-name changes, to trigger previous_plan_archive linkage"
  - version: "0.1.3"
    date: "2026-07-04"
    changes: "Limit the closeout back-link exemption to archives added or updated in the same change set; pre-existing base archives no longer grant it"
  - version: "0.1.2"
    date: "2026-07-04"
    changes: "Clarify that changed active plans only require previous_plan_archive when implementation_scope does not match an existing archive scope"
  - version: "0.1.1"
    date: "2026-07-04"
    changes: "Require archive plans to keep feature_path, parent_feature, and feature_level consistent with the archive location"
  - version: "0.1.0"
    date: "2026-07-01"
    changes: "Initial technical design for implementation plan archive gate"
---

# IMPLEMENTATION_PLAN 归档门禁 TRD

## 1. 技术目标

为 `feature-implementor` 增加 Implementation Plan Archive Gate：

- 在创建同一 `feature_path` 的下一份活跃计划前，扫描并处理已有
  `docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md`。
- 将完成态或废弃态旧计划保存到
  `docs/engineer/{feature_path}/archive/IMPLEMENTATION_PLAN-<scope>.md`。
- 保留当前活跃计划入口不变，并通过 `previous_plan_archive` 记录新旧计划关系。
- 扩展 repository contract 和 eval，避免计划被直接覆盖或归档 metadata 漂移。

## 2. 影响范围

| Area | File | Change |
| --- | --- | --- |
| Owning PRD | `docs/pm/agents/engineer-agent/skills/feature-implementor/PRD.md` | 增加 Implementation Plan Archive Gate 产品契约和工作流节点。 |
| Repository guidance | `AGENTS.md` | 为实施计划归档增加窄例外，避免与“除 changelog 外不创建多个版本化文件”冲突。 |
| Public skill contract | `agents/engineer/skills/feature-implementor/SKILL.md` | 在 plan creation 前增加旧计划扫描，在 closeout 后增加 archive gate。 |
| Planner module | `agents/engineer/skills/feature-implementor/_internal/planner/INSTRUCTIONS.md` | 写计划前检查同 `feature_path` 下是否存在未归档活跃计划。 |
| Reviewer module | `agents/engineer/skills/feature-implementor/_internal/reviewer/INSTRUCTIONS.md` | 交付前检查 closeout 与 archive 状态一致。 |
| Output conventions | `agents/engineer/skills/feature-implementor/_internal/_shared/output-conventions.md` | 定义归档路径、metadata、状态值和 `previous_plan_archive`。 |
| Repository contract | `scripts/check_repository_contract.py` | 将 active plan 的 `status` 设为必填 metadata；以 merge-base 上 active plan 的存在性和 `status` 重写 archive linkage 判断，并保留 closeout + archive 同提交例外。 |
| Skill instructions | `agents/engineer/skills/feature-implementor/_internal/_shared/output-conventions.md`, planner / reviewer `INSTRUCTIONS.md` | 现有三选一处理、继续更新与归档回链规则原则上保持不变；实施时仅复核与 base-ref `status` 契约是否冲突。 |
| Skill lock | `skills-lock.json` | 仅当 `feature-implementor` skill 目录实际变更时刷新 `computedHash`。 |

## 3. 架构设计

```mermaid
flowchart TD
    Request["feature-implementor request"] --> Resolve["Resolve feature_path"]
    Resolve --> Active["Read active IMPLEMENTATION_PLAN.md"]
    Active --> Exists{"Active plan exists?"}
    Exists -->|No| NewPlan["Write new active plan"]
    Exists -->|Yes| State{"Handled decision recorded?"}
    State -->|Continue current plan| Update["Update active plan with version bump"]
    State -->|Archive completed plan| Archive["Create archive plan with status Archived"]
    State -->|Supersede old plan| Supersede["Create archive plan with status Superseded"]
    State -->|No decision| Block["Ask user before writing"]
    Archive --> Link["New plan previous_plan_archive points to archive"]
    Supersede --> Link
    Link --> NewPlan
```

核心设计是将“当前计划”和“历史计划”分层：

- 当前计划仍固定为 `docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md`。
- 历史计划只放在 `archive/` 下。
- 新计划引用上一份归档计划，repository contract 校验引用关系。

## 4. 文件与 metadata 契约

### 4.1 活跃计划

活跃计划路径：

```text
docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md
```

新增或更新后的活跃计划 frontmatter 应包含：

```yaml
implementation_scope: "<lower-kebab-scope>"
status: "<planning-or-closeout-status>"
previous_plan_archive: "docs/engineer/{feature_path}/archive/IMPLEMENTATION_PLAN-<scope>.md"
```

规则：

- `implementation_scope` 描述当前计划范围，使用 lower kebab-case。
- `status` 是 repository contract 对 active plan 无条件机器校验的必填字段，也是判断
  当前改动属于“继续修订未完成计划”还是“已完成计划后的下一轮计划”的依据。
- `previous_plan_archive` 的必填性由 merge-base 上同一路径 active plan 的存在性和
  `status` 决定，而不是由 archive 目录是否已有历史归档决定。
- 如果用户选择继续更新当前计划，且 merge-base 上的 `status` 不是
  `Implemented`，可不写 `previous_plan_archive`，但必须正常 bump `version` 和
  `last_updated`。
- 如果 merge-base 上的 `status` 是 `Implemented`，本次又修改 active plan，则必须
  声明合法的 `previous_plan_archive`，除非本次改动本身属于第 5 节定义的
  closeout + archive 同提交例外。

### 4.2 归档计划

归档计划路径：

```text
docs/engineer/{feature_path}/archive/IMPLEMENTATION_PLAN-<scope>.md
```

完成态归档 frontmatter 必填字段：

```yaml
implementation_scope: "<lower-kebab-scope>"
status: "Archived"
archived_at: "YYYY-MM-DD"
archive_approved_by: "<user or maintainer>"
source_plan: "docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md"
```

废弃态归档 frontmatter 必填字段：

```yaml
implementation_scope: "<lower-kebab-scope>"
status: "Superseded"
archived_at: "YYYY-MM-DD"
archive_approved_by: "<user or maintainer>"
source_plan: "docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md"
superseded_reason: "<reason>"
```

归档文件必须保留原计划的 `feature_path`、`parent_feature` 和
`feature_level`，且必须与归档所在 `feature_path` 一致；还应保留原计划的
`feature`、`related_prd`、`related_trd`、`version`、`date`、`last_updated`
和 `author`，以便独立审查。

## 5. Repository Contract 设计

在 `scripts/check_repository_contract.py` 中新增：

| Component | Behavior |
| --- | --- |
| `IMPLEMENTATION_PLAN_ARCHIVE_RE` | 匹配 archive 目录和 `<scope>`。 |
| Archive metadata validator | 校验必填字段、日期、状态值、scope 与文件名一致、`source_plan` 指向活跃入口，以及必填的 `feature_path`、`parent_feature`、`feature_level` 与归档所在 `feature_path` 一致。 |
| Active plan linkage validator | 当活跃计划声明 `previous_plan_archive` 时，校验文件存在且 feature metadata 一致。 |
| Changed active plan guard | 先复用 `implementation_plan_base_ref(root)` 取得 HEAD 与 `origin/main` / `main` 的 merge-base，再用 `content_at_ref(root, ref, rel)` 读取 base ref 上同一路径 active plan。base 内容为 `None` 时按新增计划处理；base 内容存在时通过 `parse_markdown_frontmatter(path, content, errors=None)` 只解析历史 frontmatter。若 base `status` 不是 `Implemented`，允许继续修订或追加原计划，不要求 `previous_plan_archive`，但仍须按现有版本契约 bump `version` 和 `last_updated`。若 base `status` 是 `Implemented` 且本次修改 active plan，则必须声明 `previous_plan_archive`，由 linkage validator 校验目标文件存在且 `feature_path` 一致。窄例外：若本次改动同时完成 closeout + archive，且 HEAD 的 `implementation_scope` 命中本次变更中新增或更新的 archive scope，则这是正确归档动作本身，可省略 `previous_plan_archive`。 |
| Path allowlist | 允许 archive 目录下的 `IMPLEMENTATION_PLAN-<scope>.md`，避免被现有 active-plan path check 误报。 |

语义说明：

- checker 负责可机器判断的路径和 metadata 约束。
- 是否“继续更新当前计划”还是“创建下一份计划”仍由 planner gate 和用户确认判断。
- `implementation_scope` 是否变化不得作为 guard 的触发条件；笼统或未改名的 scope
  不能成为绕过门禁的路径。scope 只用于识别 closeout + archive 同提交例外。
- archive 目录中是否已有历史归档也不得作为 guard 的触发条件；第一次归档前直接改写
  base `Implemented` active plan 必须被覆盖。
- 对历史无 `implementation_scope` 的旧计划不做批量失败；当旧计划被触及时由新规则收口。

## 6. Skill 行为设计

### 6.1 Plan Creation 前置门禁

`feature-implementor` 在写计划前：

1. 解析 `feature_path`。
2. 检查 `docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md` 是否存在。
3. 如果不存在，正常创建新计划。
4. 如果存在，读取 frontmatter 和 closeout 状态。
5. 如果没有用户确认的处理方式，先询问：
   - 归档旧计划后创建新计划；
   - 继续更新旧计划；
   - 将旧计划归档为 `Superseded` 并记录原因。

### 6.2 Closeout 后归档门禁

实现完成并同步 closeout 后：

- 只有用户或维护者确认后才能归档。
- 归档动作必须保留 closeout 证据、验证命令、skipped/blocked 记录和剩余风险。
- 归档后如果创建下一份活跃计划，新计划必须引用 `previous_plan_archive`。

### 6.3 Reviewer 检查

reviewer 在 handoff 或 delivery 前检查：

- 完成态计划是否已同步 closeout。
- 若本次创建了下一份计划，上一份计划是否已归档或明确继续更新。
- `previous_plan_archive` 是否存在且指向同一 `feature_path` 的 archive 文件。
- 归档状态是否只使用 `Archived` 或 `Superseded`。

## 7. Eval 设计

在既有两个 archive workflow eval 基础上，新增两个 repository contract 回归 eval：

| Eval | Scenario | Expected Behavior |
| --- | --- | --- |
| `eval-012-implementation-plan-archive-preflight` | 同一 `feature_path` 已存在未归档 `IMPLEMENTATION_PLAN.md`，用户要求创建新计划。 | skill 阻止直接覆盖，列出旧计划状态和三种处理选项。 |
| `eval-013-implementation-plan-archive-allows-next-plan` | 旧计划已 closeout 并归档，新请求创建下一份计划。 | skill 允许创建新活跃计划，并要求记录 `previous_plan_archive`。 |
| `eval-015-active-plan-base-implemented-requires-archive-link` | base ref 上 active plan 的 `status` 已是 `Implemented`，本次修改 active plan，但没有声明 `previous_plan_archive`。 | repository contract 拦截改动，要求提供存在且 `feature_path` 一致的归档回链。 |
| `eval-016-active-plan-base-in-progress-allows-update` | base ref 上 active plan 的 `status` 不是 `Implemented`，本次继续修订 active plan，正常 bump `version` 和 `last_updated`，但不声明 `previous_plan_archive`。 | repository contract 放行合法的同轮计划更新。 |

每个 eval fixture 应包含：

- PRD / TRD；
- 活跃或归档计划；
- 对 `eval-015` / `eval-016`，能够构造并验证 base ref 与 HEAD 差异的 git fixture；
- `comparison.md` durable 结果；
- 必要的 `eval_metadata.json`，但不提交运行期产物。

## 8. 验证策略

确定性检查：

```bash
git diff --check
uv run scripts/check_repository_contract.py
uv run scripts/check_doc_contract.py
uv run --with pytest pytest agents/test_eval_contract.py
```

## 9. 回滚策略

标准 git revert 可回滚文档、skill 指令、contract checker、eval fixture 和
`skills-lock.json`。回滚后：

- `IMPLEMENTATION_PLAN.md` 活跃入口仍存在；
- closeout gate 继续生效；
- archive 目录不再作为新计划前置门禁的一部分。

## 10. 已决技术结论

| # | Decision | Rationale |
| --- | --- | --- |
| 1 | `previous_plan_archive` 的强制条件由 merge-base 上 active plan 的存在性和 `status` 决定。 | 覆盖第一次归档前直接改写已完成计划的场景，不依赖 archive 历史。 |
| 2 | `implementation_scope` 是否变化不作为 guard 触发条件。 | scope 命名可能保持笼统或不变，不能可靠表示是否进入下一轮计划。 |
| 3 | base `status` 非 `Implemented` 时允许继续更新；base `status` 为 `Implemented` 且 active 被修改时要求合法回链。 | 与 planner 已有“继续更新当前计划”和“归档后新建”两条合法路径一致。 |
| 4 | HEAD scope 命中本次新增或更新 archive scope 时保留 closeout + archive 同提交例外。 | 正确归档动作本身不应被误判为绕过归档门禁。 |
