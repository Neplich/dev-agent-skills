---
title: "Eval 真实场景与 Lane 隔离重构决策记录"
type: DECISIONS
version: "1.3.0"
status: Approved
author: "Neplich Codex"
date: "2026-08-07"
last_updated: "2026-08-12"
generated_by: "idea-to-spec"
feature: "eval-scenario-isolation"
feature_path: "repository-governance/eval-scenario-isolation"
parent_feature: "repository-governance"
feature_level: "2"
related_issue:
  - "https://github.com/Neplich/dev-agent-skills/issues/246"
  - "https://github.com/Neplich/dev-agent-skills/issues/275"
  - "https://github.com/Neplich/dev-agent-skills/issues/277"
related_docs:
  - "docs/pm/repository-governance/eval-scenario-isolation/PRD.md"
changelog:
  - version: "1.3.0"
    date: "2026-08-12"
    changes: "确认 identity schema v2 七字段、协议模块边界与 196 份常规 comparison 的一次性单轨迁移"
  - version: "1.2.0"
    date: "2026-08-12"
    changes: "确认冻结后 eval 不登记迁移清单，并区分 trd-gen eval-006 的断言缺陷与 skill 执行缺陷"
  - version: "1.1.0"
    date: "2026-08-12"
    changes: "分离辅助 skill 的运行锁定证据与 comparison 历史重跑判定"
  - version: "1.0.0"
    date: "2026-08-07"
    changes: "初始版本，记录 Issue #246 已确认的范围与评测隔离决策"
---

# Eval 真实场景与 Lane 隔离重构决策记录

## 已确认决策

| ID | 决策 | 理由 |
| --- | --- | --- |
| D-001 | 本请求分类为 `existing_update`、`change_tier: major`。 | 变更覆盖 38 个 skill 的 eval、七个角色 runner、仓库检查与 durable comparison，属于跨角色契约面重构。 |
| D-002 | 功能路径固定为 `repository-governance/eval-scenario-isolation`，父功能为 `repository-governance`。 | Issue #246 调整的是仓库级 eval 治理、执行隔离和 release 证据，不改变某一业务 skill 的功能归属。 |
| D-003 | 审计基线固定为 38 个常规 skill、193 条 eval；每条旧 eval 必须有保留、合并或删除结论。 | 完成标准需要覆盖全部已知评测，不能只迁移明显测试化的样本。 |
| D-004 | Eval 必须先定义真实用户场景，再编写 prompt 和 assertions。 | 从内部协议或评分项反向构造 prompt 会让 baseline 猜到答案，无法衡量真实用户收益。 |
| D-005 | 先完成 designer、devops、docs、engineer、product_manager、qa、security 七角色 pilot，全部通过后再批量迁移。 | Pilot 用于验证场景、fixture、runner、preflight 和 comparison 的端到端方法，避免批量复制错误设计。 |
| D-006 | 两条 lane 的唯一变量是目标 skill 是否加载；prompt、fixture 和其余执行条件必须一致。 | 只有控制其他变量，with-skill 与 without-skill 的差异才能归因于目标 skill。 |
| D-007 | 所有角色共用统一 scratch materializer 和隔离 preflight，不保留角色自定义的重复隔离语义。 | 分散实现会造成目录、skill 可见性、禁止文件和运行时重置规则漂移。 |
| D-008 | Candidate lane 物理排除 `evals.json`、`eval_metadata.json`、历史 `comparison.md`、assertions、expected answer、judge 资料、answer-bearing README 和 runtime artifacts。 | 仅依赖 prompt 约束不能证明 candidate 没有读取脚手架；物理隔离是可复核边界。 |
| D-009 | QA runner 的已知确定性泄漏必须修复，其他专用 runner 必须完成同类审计和回归测试。 | Runner 消息、启动 cwd 或源仓库可见性都可能破坏唯一变量，即使 eval 定义本身已重写。 |
| D-010 | 进程、端口、数据库、浏览器、登录态和下载目录必须隔离或恢复到相同初始状态；无法证明时结果为 `BLOCKED`。 | 文件隔离不能覆盖运行时副作用，污染后的 lane 不能生成可信 PASS。 |
| D-011 | Judge 使用第三个全新只读 `gpt-5.6-luna` medium 上下文，并在两条输出锁定后才读取 assertions 和必要原始证据。 | Candidate 自评或继承 lane 上下文不能作为独立判定；judge 也不能提前影响 candidate 输出。 |
| D-012 | 每轮重新生成 without-skill baseline；旧 comparison 在完成新标准重跑前视为 stale，不作为 release 依据。 | 历史 baseline 与旧场景、旧 fixture 或旧隔离条件绑定，不能充当本轮对照。 |
| D-013 | Runtime artifact 只写入 scratch 或短期 CI artifact，不提交仓库。 | Durable comparison 保存长期结论；transcript、输出、verdict 和 diagnostics 会污染 fixture 与 git 历史。 |
| D-014 | `manual-gen` 不进入本次常规 paired eval 重构。 | 它依赖真实登录环境、运行界面、源码和用户反馈，已由 manual-only 契约单独治理。 |
| D-015 | 本 issue 不修改目标 skill 的业务协议，也不引入无关抽象或功能。 | 本轮只修复 eval 的用户代表性、lane 隔离与证据可信度；业务协议缺陷应另行分类。 |
| D-016 | Eval 只对所属目标 skill 的设计结论负责；辅助 skill 的完整内容继续参与当次运行锁定和证据记录，但其后续内容变化不连带使其他目标 skill 的 comparison 失效。 | `skill_dependencies` 用于构建可信运行环境，不等同于跨 skill 回归依赖图；跨 skill 协作应由有明确归属的集成 eval 覆盖。 |
| D-017 | `migration-inventory.json` 永久保持 Issue #246 冻结的 193 条历史迁移记录；冻结后新增 eval 不登记到该清单。 | 迁移清单用于证明旧基线的逐条去向，不是常规 eval 注册表；扩充清单会破坏冻结 commit、计数和 schema 语义。 |
| D-018 | Durable writer 对 retained identity 使用三态规则：零匹配只写 comparison，唯一匹配同步更新 inventory，多匹配拒绝持久化。 | 新增 eval 必须能生成 fresh 证据，历史迁移记录仍需保持事务一致，多匹配代表不可接受的清单歧义。 |
| D-019 | `trd-gen` eval-006 是混合缺陷：允许完成 TRD 后在交付摘要中提示合法的 `feature-implementor` 下一阶段，但不得转交本轮 TRD 更新职责；正文归一化和 frontmatter changelog 断言保持不变，并强化 skill 交付前自检。 | 原“不得把任务路由给别人”断言误伤了 `trd-gen` 的强制 handoff 契约；旧方案状态标注和正文 changelog 则确实违反现行 current-state 文档规则，不能通过弱化断言掩盖。 |
| D-020 | 静态 eval checker 对所有当前常规 eval 使用同一严格输入契约，不再以是否存在 complete migration identity 决定校验强度。 | 冻结后新增 eval 也必须满足 scenario、自然 prompt、metadata、依赖、runtime isolation 和 fixture 规则；历史迁移身份不能成为质量降级开关。 |
| D-021 | Durable comparison identity schema v2 的跨版本 freshness 只包含七字段：`target_skill_sha256`、`eval_definition_sha256`、`metadata_sha256`、`fixture_sha256`、`execution_protocol_sha256`、`runtime_protocol_sha256`、`judge_schema_sha256`。 | 这七项覆盖目标 skill、eval 自身输入、执行/判定协议和隔离协议；persistence、inventory 与报告格式变化不应连锁作废行为证据。 |
| D-022 | 模块边界固定为 execution/judging、runtime/isolation、persistence/inventory；identity helper 单独计算七字段，`run_skill_eval.py` 只保留薄 CLI 与 orchestration。 | 协议 hash 必须来自清晰文件边界，不能用函数过滤或启发式排除推断哪些源码影响行为。 |
| D-023 | 完整 runner、identity、execution、judging、runtime、persistence、inventory 和报告格式源码 manifest 只用于同轮 source-drift lock；持久化前任一 bytes 变化均 `BLOCKED`。 | 跨版本 freshness 与同轮输入稳定是不同安全属性；后者不能因 persistence 不参与历史 identity 而放松。 |
| D-024 | V1 到 v2 只执行一次迁移；迁移前可以核验旧 Executor hash 的可信 Git 来源并把实际 hash/source commit 写入 audit JSON，但正常 writer/checker 不调用 Git、不硬编码旧 hash。迁移后 checker 只接受 v2。 | 永久兼容桥会形成双轨并把历史实现细节带入正常检查；来源核验属于一次性迁移证据。 |
| D-025 | 196 份常规 comparison 分为 187 份机械迁移、6 份 `trd-gen` 保持 stale、3 份 PM scope-guard 保持 PENDING；1 份 manual-only 原样不迁移。187 份的 verdict/evidence 逐字保持。 | 审计分布为 127 PASS/FULL、46 PASS/PARTIAL、12 FAIL/FULL、2 FAIL/PARTIAL；807 assertions 为 717 PASS、70 NOT_EXERCISED、20 FAIL。`trd-gen` 输入已变化，不能继承 FRESH；PM 三条尚无 fresh 证据。 |
| D-026 | #277 的模型回归范围为 `trd-gen` 全部 6 条加 PM eval-017/018/019，共 9 条；模型调用仍未授权。 | 文档与确定性实现授权不等同于模型成本授权；9 条必须在计划再次确认并单独授权后运行。 |

## 假设与约束

| ID | 假设或约束 | 如果不成立的处理 |
| --- | --- | --- |
| A-001 | Issue #246 的 38 skill / 193 eval 是本轮冻结审计基线。 | 仓库存在新增或删除时先记录漂移，仍须保持 193 条原基线逐条有去向。 |
| A-002 | 保留、合并或删除是允许的迁移结论，最终 eval 数量不预设。 | 合并或删除必须记录理由、替代覆盖和对应 durable 证据。 |
| A-003 | 指定模型和隔离运行环境可用于 fresh paired eval 与独立 judge。 | 能力不可用时标记 `BLOCKED` 并保留 stale 状态，不静默替换模型或复用历史结果。 |
| A-004 | 宿主原生 README 或证据文件可能是合法 fixture。 | 仅在其描述真实产品或仓库事实且不承载评分答案时保留，并由正反测试防止静态检查误报。 |
| A-005 | Issue #277 的三个 PM scope-guard eval 是冻结后新增资产。 | 它们按零匹配语义生成 fresh comparison，不改写 Issue #246 的 193 条 inventory。 |
| A-006 | 一次性 migration audit 能定位旧 Executor hash 的可信 Git source commit。 | 无法验证来源的 comparison 不机械迁移为 FRESH，改为 stale 等待重跑。 |

## 已排除方案

| ID | 方案 | 排除理由 |
| --- | --- | --- |
| R-001 | 保持旧 eval 定义，只重新执行 193 条 baseline。 | 不能解决 prompt、fixture 和 assertions 缺少真实用户代表性的问题。 |
| R-002 | 只删除“用户说：”和显眼测试词，不重建场景。 | 表面措辞变化不能消除路由字段、答案材料和断言反向设计。 |
| R-003 | 各角色继续维护独立 scratch 复制与 preflight 逻辑。 | 规则会持续漂移，无法形成仓库级一致证据。 |
| R-004 | 仅靠 prompt 告知 candidate 不要读取脚手架。 | Candidate 仍能访问文件、父上下文或源仓库，无法证明没有泄漏。 |
| R-005 | 复用历史 baseline 或 comparison 以降低批量执行成本。 | 不同场景、fixture 或隔离条件下的结果不是同轮有效对照。 |
| R-006 | 把所有旧 comparison 删除后再迁移。 | 会丢失历史结论和迁移追溯；stale 标记可以保留历史且阻止误用。 |
| R-007 | 用源码结构过滤、函数排除表或完整 runner hash 作为跨版本行为身份。 | 前两者依赖启发式边界，后者继续让 persistence/report 机械变化批量作废证据；显式协议模块更直接。 |
| R-008 | 在正常 checker 中保留 Git 历史查询或 v1/v2 双轨。 | 增加长期复杂度且让迁移永不结束；可信来源核验只属于一次性 migration audit。 |

## 待确认问题

无阻塞性产品决策。统一 materializer 的文件位置、CLI 入口、迁移清单的具体文件格式和角色批次顺序由 Engineer TRD 与实施计划决定，但必须满足 PRD 中的 P0 验收标准。
