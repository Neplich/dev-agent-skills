# Eval Result: eval-001-positioning-gap-brief

## Evaluation Target

- Agent: `product_manager`
- Skill: `competitive-brief`
- Eval: `eval-001-positioning-gap-brief`
- Test case: positioning-gap-brief
- Workspace: `workspace/eval-001-positioning-gap-brief`
- Classification: (c) 依赖实时公开网页研究。该场景验证从当前公开来源提炼竞品定位与 messaging gap，不应以静态 mock 或网页快照替代真实联网研究。
- Latest result: PASS - 2026-07-26 的 fresh judge 基于相互隔离、各自独立联网研究的 `with_skill` 与新 `without_skill` baseline 判定两者均满足全部 assertions；with-skill 正确区分厂商公开事实与需要验证的我方定位假设。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: 仅包含原始 prompt 与 eval metadata；未增加静态网页快照，因为竞品定位、功能、定价和发布信息会持续变化。
- Expected output: 结构化竞品 brief，包含竞品定位、目标用户、核心卖点、内容空白、机会、威胁和证据边界。
- Research mode: 两次运行都真实联网访问公开网页，以 Linear 与 Atlassian/Jira 官方页面为主要证据。

## No-Leak Fresh Pair Method

本轮按以下顺序执行，避免 answer key、预计算来源集合或历史结论泄漏：

1. 主 judge 首先只读取 `eval_metadata.json` 中的原始 prompt，未读取 `evals.json`、assertions、expected output 或旧 `comparison.md`。
2. with-skill 候选仅在读取 PM Agent README 和当前 `competitive-brief/SKILL.md` 后自行搜索、访问并选择公开来源；候选结论锁定前仍未读取答案键或旧 comparison。
3. 候选锁定后才启动 `fork_turns=none` 的 fresh Codex subagent。baseline 只收到原始 prompt，以及“自行联网并返回实际访问时间和 URL”的运行要求；未提供 skill、PM README、assertions、expected output、旧 comparison、父候选、父来源集合或网页快照。
4. baseline 独立完成研究并锁定输出后，主 judge 才首次读取 assertions、expected output 与旧 comparison，并据两份新结果逐项判定。

两次运行自然都优先选择了厂商官网，且部分首页/定价 URL 重合；这是独立搜索同一竞品主题的合理结果，不是共享预计算 source set。

## Fresh With Skill

- Actual access time: `2026-07-26 15:51–15:53 CST (Asia/Shanghai, UTC+08:00)`
- Actual source set selected by with-skill:
  - Linear homepage: https://linear.app/homepage
  - Linear features: https://linear.app/features
  - Linear Timeline documentation: https://linear.app/docs/timeline
  - Atlassian products / Jira positioning: https://www.atlassian.com/software
  - Jira pricing: https://www.atlassian.com/software/jira/jira/pricing
  - Jira agile project management: https://www.atlassian.com/software/jira/agile

with-skill 候选的实际结论：

| 竞品 | 当前公开定位 | 主要目标用户 | 当前强调的卖点 |
| --- | --- | --- | --- |
| Linear | 面向现代产品开发、团队与 agents 的 product development system | 重视速度、专注和统一产品上下文的产品、工程与设计团队，并向更大组织扩展 | 从 roadmap 到 release、issues/projects/cycles、速度与低噪音、人与 agent 共享工作流、项目更新与洞察 |
| Jira | 面向所有团队的灵活项目管理与敏捷交付平台 | 软件团队、业务团队、跨团队项目以及需要规模化治理的复杂组织 | 多种敏捷方法、backlog/board/roadmap/report、可配置流程、跨团队规划与依赖、自动化、企业安全治理和 Atlassian 生态 |

候选提出的 messaging gap 是“在不要求各职能先统一工具配置或工作方法的前提下，把决策依据、责任边界和可验证结果持续连起来”。它明确将该方向标记为待验证假设：prompt 没有提供我方产品、目标用户、能力证据或客户研究，因此不能断言我方已经拥有该差异，也不能把厂商营销页未突出某项能力解释成竞品缺少该能力。

机会与威胁也保持证据边界：

- 机会：验证“跨角色清晰度 + 可解释、可追溯协作”以及 human-agent accountability 的信息主张。
- 威胁：Linear 正强化 agent-native 产品开发和端到端执行叙事；Jira 已覆盖广泛团队、企业治理、AI 与生态，宽泛的“更简单”或“AI 项目管理”很难形成稳定差异。
- 验证要求：补充我方定位与能力证据、目标用户访谈、产品试用和更完整的竞品内容审计后，才能把 gap 变成正式定位决策。

## Fresh Without Skill / Baseline

- Actual access time: `2026-07-26 15:54:10–15:54:57 CST (Asia/Shanghai, UTC+08:00)`
- Actual source set independently selected by baseline:
  - https://linear.app/
  - https://linear.app/method
  - https://linear.app/method/introduction
  - https://linear.app/pricing
  - https://linear.app/security
  - https://linear.app/customers
  - https://linear.app/customers/automattic
  - https://linear.app/customers/klaviyo
  - https://linear.app/docs/customer-requests
  - https://linear.app/docs/timeline
  - https://www.atlassian.com/software/jira
  - https://www.atlassian.com/software/jira/features
  - https://www.atlassian.com/software/jira/features/workflows
  - https://www.atlassian.com/software/jira/jira/pricing
  - https://www.atlassian.com/software/jira/guides/getting-started/introduction
  - https://support.atlassian.com/jira-product-discovery/docs/what-is-jira-product-discovery/
  - https://www.atlassian.com/software/jira/product-discovery/features
  - https://www.atlassian.com/software/jira/product-discovery/features/roadmaps

baseline 独立识别出 Linear 的 purpose-built、低噪音、产品开发一体化和 agent-native 叙事，以及 Jira 的 all-teams、高度可配置、跨团队规划、企业治理和 Atlassian 生态。它提出“可验证交付链”“低维护治理”“human-agent accountability”“single source of decision”等 messaging 假设，同时明确这些是基于公开定位的策略推断，不是竞品官方自述。

本轮 baseline 也给出了机会、威胁、推荐主线、不建议使用的同质化表述和研究边界，质量足以满足全部 assertions。fresh judge 不以“没有使用 skill”作为降级理由；实际差异是 with-skill 依据固定 competitive-brief 协议更稳定地组织证据边界，而该次 baseline 通过自主研究也达到了同等断言门槛。

## Assertion Results

| Assertion | With skill | Without skill | Fresh judge conclusion |
| --- | --- | --- | --- |
| `positioning` | PASS | PASS | 两者都分别说明 Linear 与 Jira 的定位、目标用户和核心卖点，并给出实际官方来源。 |
| `messaging_gap` | PASS | PASS | 两者都识别了未被充分占领的叙事机会；这些机会均被表述为需要结合我方能力与用户研究验证的假设。 |
| `evidence_boundary` | PASS | PASS | 两者都区分厂商公开信息与策略推断，未把页面未强调的内容写成确定的功能缺失，也未虚构我方差异。 |

## Failures and External-Service Triage

- 本轮两次运行均成功访问公开来源，未发生 research infrastructure failure，也未发现 assertion failure。
- 若官方页面、DNS、搜索或联网工具不可用，应记为 external-service / research infrastructure failure，而不是 skill regression；记录失败 URL、访问时间、HTTP 或工具错误后重试。
- 若单个页面改版、重定向或移除，应先使用同厂商官方替代页面，并在 comparison 中记录实际 URL 与访问时间；不得按历史页面文案做逐字断言。
- 只有在公开来源可访问且证据足够时，with-skill 仍遗漏两家竞品的定位/目标用户/卖点、无法提出 messaging gap，或把推断伪装成确定事实，才判为 skill behavior regression。
- 定价、套餐权益、AI/agent 功能、客户数量、首页主标题、案例和发布说明都具有时效性；本 comparison 记录的是本轮研究证据，不是永久事实快照。

## Next Steps

- 后续 fresh eval 继续让 with-skill 与 baseline 各自实时联网、独立选择来源并记录实际时间与 URL；不要预先共享 source set。
- 若要把本轮 gap 转成我方定位决策，必须补充我方产品上下文、能力 proof、目标用户访谈、实际产品试用和更完整的竞品内容审计。

## Runtime Artifacts Policy

- Runtime transcripts、完整模型输出、verdicts、timing、网页快照、outputs 与 diagnostics 不提交到 git。
- Durable 产物仅更新本 `comparison.md`；本轮未修改 fixture、metadata、skill 或 eval 定义。
