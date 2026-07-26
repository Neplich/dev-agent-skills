# Eval Result: eval-001-positioning-gap-brief

## Evaluation Target

- Agent: `product_manager`
- Skill: `competitive-brief`
- Eval: `eval-001-positioning-gap-brief`
- Test case: positioning-gap-brief
- Workspace: `workspace/eval-001-positioning-gap-brief`
- Classification: (c) 依赖实时公开网页研究。该场景验证从当前公开来源提炼竞品定位与 messaging gap，不应以静态 mock 或网页快照替代真实联网研究。
- Latest result: PASS - 2026-07-26 的 fresh judge 使用同一组实时官方来源分别生成了新的 `with_skill` 与 `without_skill`；with-skill 满足全部 assertions，并正确区分公开事实、页面观察与待验证假设。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: 仅包含 prompt 与 eval metadata；未增加静态网页快照，因为竞品定位、功能与定价会变化。
- Expected output: 结构化竞品 brief，包含竞品定位、目标用户、核心卖点、内容空白、机会、威胁和证据边界。
- Research access time: `2026-07-26 15:22 CST (+0800)`
- Research mode: 真实联网访问公开网页；Linear 与 Jira 均优先采用厂商官方页面。

## Live Source Set

本轮 fresh pair 使用同一来源集合：

- Linear homepage: https://linear.app/
- Linear features: https://linear.app/features
- Linear pricing: https://linear.app/pricing
- Linear changelog: https://linear.app/changelog/page/1
- Atlassian products / Jira positioning: https://www.atlassian.com/software
- Jira features: https://www.atlassian.com/software/jira/features
- Jira pricing: https://www.atlassian.com/software/jira/jira/pricing
- Jira projects overview: https://www.atlassian.com/software/jira/guides/projects/overview

所有来源均为本轮访问时的公开页面，没有使用历史 baseline 或本地伪造数据。定价、套餐权益、AI 功能、产品数字、首页文案与 changelog 会持续变化；后续复验必须重新访问并记录时间，不能把本次内容当作长期事实快照。

## Fresh With Skill

应用 `competitive-brief` 后生成的 brief 摘要：

| 竞品 | 当前公开定位 | 主要目标用户 | 当前强调的卖点 |
| --- | --- | --- | --- |
| Linear | 面向现代产品开发的 system，强调团队与 agents 在同一结构化上下文中规划、构建与发布 | 产品、工程、设计等产品开发团队，并通过 Business / Enterprise 套餐覆盖更大组织 | 从 roadmap 到 release 的一体化流程、速度与专注、issues/projects/cycles/initiatives、AI agents、coding sessions、Loops、customer requests |
| Jira | 面向所有团队的 AI-powered project management，并通过 Atlassian System of Work 承接跨团队和组织级协作 | 开发、市场、业务团队、跨团队项目与需要企业治理的复杂组织 | 多视图规划与跟踪、可配置 workflow、目标和依赖管理、Rovo AI、自动化、企业安全治理、Marketplace 集成生态 |

结构化结论包括：

- 定位差异：Linear 的官方叙事更窄、更产品开发导向，强调 AI-native、速度和低噪音；Jira 的官方叙事更广，强调所有团队、规模化协作、灵活配置、治理和生态。
- messaging gap 假设 1：可以验证“让跨职能项目协作既易上手又保持决策可追溯”的叙事空间。所选 Linear 页面更强调产品开发速度，Jira 页面更强调广度、配置与规模；这只是样本页面上的 messaging white space，不代表两者缺少相关能力。
- messaging gap 假设 2：可以验证“从业务目标、证据、决策到交付结果的一条可解释闭环”。两家都强调上下文、目标或工作跟踪，但所选页面未把可审计的决策理由作为首要主张；仍需访谈目标用户并做更完整内容审计。
- 机会：若我方产品确有对应能力，可围绕“跨角色清晰度 + 可解释协作”做 landing-page message test，并用用户访谈、竞品 demo 和赢单/流失证据验证。
- 威胁：Linear 正快速扩展 agent、代码与循环自动化叙事；Jira 在跨团队规模、治理、AI 与集成生态上覆盖很广，宽泛的“更智能协作”主张很难形成差异。
- 证据边界：prompt 未提供我方产品、目标用户、能力或 proof，因此不能断言上述 gap 是我方已拥有的差异化，也不能据公开营销页判断实际体验、客户满意度、迁移成本或功能缺失。

## Fresh Without Skill / Baseline

在不读取或应用 `competitive-brief` 与 PM Agent README 的条件下，fresh baseline 仅依据相同 prompt 和同一来源集合重新生成。其摘要同样识别出：

- Linear 偏产品研发团队、速度、集中注意力与 AI agents；
- Jira 偏所有团队、灵活配置、跨团队规模化、治理、Rovo AI 与集成生态；
- 可探索“轻量但可治理的跨职能协作”和“从目标到结果的可解释闭环”等 gap。

baseline 覆盖了两家定位、用户和主要卖点，也能提出 messaging gap，因此不是内容失败。不过其默认输出更像功能/定位对照：来源映射、机会/威胁分区和 gap 验证动作较弱；若不主动约束，容易把“所选页面未突出某条信息”写成“竞品没有该能力”。fresh judge 在本轮 baseline 中显式保留了“需验证”措辞，未将假设伪装成事实。

## Assertion Results

| Assertion | With skill | Without skill | Fresh judge conclusion |
| --- | --- | --- | --- |
| `positioning` | PASS | PASS | with-skill 分别给出 Linear/Jira 的定位、目标用户与核心卖点，并能追溯到官方首页、功能和定价页。 |
| `messaging_gap` | PASS | PASS | 两者都提出未被充分占领的叙事机会；with-skill 进一步给出验证动作，并避免把页面空白等同于功能缺失。 |
| `evidence_boundary` | PASS | PASS | with-skill 明确标出缺少我方上下文、体验证据与完整内容审计；本轮 fresh baseline 也使用假设措辞，但边界说明不如 with-skill 系统。 |

## Failures and External-Service Triage

- 本轮未发生来源访问失败，未发现 assertion failure。
- 如果官方页面、DNS、搜索或联网工具不可用，应记为 external-service / research infrastructure failure，而不是 skill 回归；保留失败 URL、访问时间和错误类型后重试。
- 只有在来源可访问且提供足够证据时，with-skill 仍遗漏定位/目标用户/卖点、无法提出 gap，或把假设写成确定事实，才应判为 skill behavior regression。
- 若单个页面改版或移除，应先使用同厂商的官方替代页面；若来源集合发生实质变化，comparison 必须记录新 URL 与时间，不得直接与本轮文案做逐字比较。

## Next Steps

- 后续 fresh eval 继续实时访问官方来源，并用同一轮、同一来源集合生成成对结果。
- 若要把 gap 转成我方定位决策，必须补充我方产品上下文、目标用户访谈、实际产品试用和更完整的竞品内容审计。

## Runtime Artifacts Policy

- Runtime transcripts、完整模型输出、verdicts、timing、网页快照、outputs 与 diagnostics 不提交到 git。
- Durable 产物仅保留本 comparison 与 metadata；本轮没有新增静态 fixture。
