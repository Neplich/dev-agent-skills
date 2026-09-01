---
title: "human-writing 产品决策记录"
type: DECISIONS
feature: "skill-human-writing"
feature_path: "agents/pm-agent/skills/human-writing"
parent_feature: "agents/pm-agent/skills"
feature_level: "4"
version: "1.2.2"
status: Approved
author: "Neplich Codex"
date: "2026-08-19"
last_updated: "2026-09-01"
generated_by: "idea-to-spec"
related_docs:
  - "docs/pm/agents/pm-agent/skills/human-writing/PRD.md"
changelog:
  - version: "1.2.2"
    date: "2026-09-01"
    changes: "记录 D-023，明确人工语义验收为迭代原则并限缩 D-022"
  - version: "1.2.1"
    date: "2026-08-24"
    changes: "移除外部项目遗留描述，纳入文档站维护者整站优化用户场景"
  - version: "1.2.0"
    date: "2026-08-20"
    changes: "记录编写范围判断、必要结构权限、高风险事实回传和整站模式归属等决策（Issue #313）"
  - version: "1.1.0"
    date: "2026-08-19"
    changes: "确认周边 Router 与 Specialist 的直接调用适配范围"
  - version: "1.0.0"
    date: "2026-08-19"
    changes: "记录名称、位置、组合关系、输入方式和首批实施边界"
---

# human-writing 产品决策记录

## 已确认决策

| ID | 决策 | 理由 |
| --- | --- | --- |
| D-001 | Skill 名固定为 `human-writing`。 | 名称直观，也与参考方法论保持一致。 |
| D-002 | Skill 位于 `agents/product_manager/skills/human-writing/`，随 PM 插件发布。 | PM 是仓库统一入口；复用现有插件和安装结构，不新增根 `/share` 目录模型。 |
| D-003 | `human-writing` 保持独立能力，不并入 `pm-agent` 或某个文档生成 Skill。 | 所有文种可以复用同一写作规则，避免规则散落和单独 slash 调用时能力下降。 |
| D-004 | 主 Skill 与 `human-writing` 动态共同加载，同一个 Agent 同时读取两套规则并直接产出文档。 | 两者是组合关系，不是消费者、上游下游或完成后的润色流水线。 |
| D-005 | 用户输入保持开放。Agent 先从请求、主 Skill、目标文件和相邻文档推断读者、文种与语气。 | 固定表单会降低自然语言交互体验。 |
| D-006 | 用户明确要求高于主 Skill，主 Skill 的事实和交付契约高于 `human-writing` 的表达规则。 | 写作改善不能改坏事实、流程、安全边界和文件格式。 |
| D-007 | “活人感”由真实材料、明确读者、内容推进和自然中文产生。 | 俚语、网络梗、假第一人称、假细节和故意错字只会制造另一种机器感。 |
| D-008 | 原始项目的全局冒号、破折号等硬禁令不进入本 Skill。 | 论坛长文规则会误伤技术文档、API、表格、代码和操作说明。 |
| D-009 | 首版只提供 Skill 契约、按需参考文件、发现与注册信息，不增加 prose lint 脚本。 | 语义和文种判断比字面扫描更重要，首版保持最小实现。 |
| D-010 | 本批次只建立并注册 `human-writing`，同步 PM 发现面；全 Router 与文档生成类 Skill 的共同加载条件下一批实施。 | 先确认写作规则，再扩大触发面，便于单独验收能力本身。 |
| D-011 | 第二批修改六个下游 Router 和三十二个 Specialist；`pm-agent` 沿用第一批实现，`human-writing` 本体不重复修改。 | 同时覆盖正常 handoff 和直接 slash 调用，且避免无关改动。 |
| D-012 | Router 在选定主 Specialist 后判断是否共同加载；Router 不把 `human-writing` 作为主 route。 | 保持既有角色与 artifact owner 不变。 |
| D-013 | Specialist 在生成或大幅更新读者向正文时自行加载；纯代码、配置、schema、lockfile 和数据输出不触发。 | 直接调用不会降级，也不会把所有写文件任务都变成写作任务。 |
| D-014 | 主 Skill 与 `human-writing` 在同一上下文中共同生效，不交接草稿，不增加后处理轮次。 | 延续已确认的组合关系。 |
| D-015 | 下游插件按注册名引用 `human-writing`，不写跨插件相对路径。 | Claude 插件复制边界内不存在可靠的跨插件相对目录。 |
| D-016 | `human-writing` 覆盖创建、改写和审查三种工作方式，并在写作前判断范围（句子或段落、单篇文档、文档集合、文档站）。 | 某一个项目的整站实践证明整站任务会被"只改命中段落"缩减成局部润色；范围判断同时防止局部任务被迫全站盘点。 |
| D-017 | 范围判断写入 `SKILL.md` 主体，不拆分新参考文件。 | 当前体量未到拆分程度；范围判断是每次写作的必经动作，应在主契约内。 |
| D-018 | "保留结构"统一指主 Skill 规定的必要结构与真实流程，不等于保留现有信息布局；用户或主 Skill 授权时可重分类、拆分、合并或移动文档内容，结构性修改交回主 Skill 验证。 | 消除"必要结构"被读成"现有结构"的歧义，同时固定主 Skill 对真实流程、必需章节和验证的所有权。 |
| D-019 | 权限、数据边界、自动行为、删除影响面、失败恢复等高风险事实存在疑问时，停止润色并返回主 Skill 核验。 | 不确定描述不能被润色成更肯定的说法；事实研究和确认始终归主 Skill。 |
| D-020 | 文档集合与整站写作指导作为 `document-patterns.md` 的一个模式，不新增文档架构或网站架构 Skill。 | 整站优化是多文档写作的尺度之一，不值得独立 Skill；也避免接管 Designer 的产品 UX 信息架构职责。 |
| D-021 | 周边 Router 与 Specialist 共同加载条款中的 "structure" 统一改为 "required structure"，一词同步。 | 保持所有权表述与 D-018 一致，改动最小且语义自洽。 |
| D-022 | 验收继续依赖真实项目案例和人工语义验收，不恢复已移除的 Skill eval 体系，也不新增写作评分或禁词统计。（已由 D-023 限缩） | 延续 #301 的移除结论；能力质量由真实用户体验判定。 |
| D-023 | "真实项目案例与人工语义验收"是能力质量的迭代原则，不作为完成门禁；能力完成验收以 PRD 确定性验收标准为准；不恢复 Skill eval 体系的结论不变。 | 限缩 D-022：#301 移除 eval 机制后完成验收只承载确定性口径，人工语义验收回归迭代依据定位。 |

## 约束

- 不改变七个 Agent 的角色边界和正式文档 owner。
- 不新建共享运行时、配置中心、模板引擎或长期作者记忆。
- 不把内部写作检查过程附在最终文档后面。
- 不修改 Router 的主路由表、Specialist entry gate、frontmatter 描述、共享 handoff 或产物格式。
