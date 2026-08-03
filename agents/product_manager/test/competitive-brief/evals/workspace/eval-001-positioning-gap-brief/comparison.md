# Eval Result: eval-001-positioning-gap-brief

## Evaluation Target

- Agent: `product_manager`
- Skill: `competitive-brief`
- Eval: `eval-001-positioning-gap-brief`
- Test case: positioning-gap-brief
- Workspace: `workspace/eval-001-positioning-gap-brief`
- Classification: (c) 依赖实时公开网页研究。该场景验证从当前公开来源提炼竞品定位与 messaging gap，不应以静态 mock 或网页快照替代真实联网研究。
- Latest result: PASS - 2026-07-26 的 fresh same-agent judge 先后锁定独立联网研究的 `with_skill` 与新 `without_skill` baseline，再读取答案键逐项判定；两者均满足全部 assertions，with-skill 对公开事实、策略推断和待验证的我方定位假设给出了更系统的边界。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: 仅包含原始 prompt 与 eval metadata；未增加静态网页快照，因为竞品定位、功能、定价、客户数据和发布信息会持续变化。
- Expected output: 结构化竞品 brief，包含竞品定位、目标用户、核心卖点、内容空白、机会、威胁和证据边界。
- Research mode: 两个 arm 都真实联网访问公开网页，各自选择来源并记录实际访问时间与 URL。

## No-Leak Fresh Pair Method

本轮由当前会话中新启动的同一个 fresh Codex agent 按以下顺序执行：

1. 先只读取 `eval_metadata.json` 中的原始 prompt，未读取 `evals.json`、assertions、expected output 或旧 `comparison.md`。
2. with-skill arm 读取 PM Agent README 和当前 `competitive-brief/SKILL.md`，随后自行联网选择来源并生成候选结果。
3. with-skill 结果锁定后，同一 agent 进入 without-skill arm；该 arm 不再应用 skill 或 PM README，只依据原始 prompt 重新搜索并选择另一组来源，未读取答案键、旧 comparison，也未复用 with-skill 的预计算 source summary。
4. without-skill 结果锁定后，judge 才首次读取 `evals.json` 中的 expected output、assertions 与旧 comparison，并据两份已冻结结果逐项判定。

两个 arm 都由本 agent 亲自完成研究和判断，没有委派或复用历史 baseline。来源有少量同厂商域名重合是研究对象决定的自然结果，但页面集合和分析路径独立；未创建或保留网页快照、transcript、verdict、output 或 diagnostics。

## Fresh With Skill

- Actual access time: `2026-07-26 16:29–16:30 CST (Asia/Shanghai, UTC+08:00)`
- Actual source set selected by with-skill:
  - Linear homepage: https://linear.app/
  - Linear features: https://linear.app/features
  - Linear pricing: https://linear.app/pricing
  - Linear customers: https://linear.app/customers
  - Linear current updates: https://linear.app/now
  - Jira features: https://www.atlassian.com/software/jira/features
  - Jira pricing: https://www.atlassian.com/software/jira/jira/pricing
  - Jira Spring 2026 release: https://www.atlassian.com/software/jira/release

with-skill 候选的实际结论：

| 竞品 | 当前公开定位 | 主要目标用户 | 当前强调的卖点 |
| --- | --- | --- | --- |
| Linear | “The system for modern product development”，覆盖从 roadmap 到 release 的产品开发流程 | 产品、工程和设计协作团队，并通过企业客户、治理和迁移能力向更大组织扩展 | issues/projects/cycles/initiatives、低摩擦执行、客户请求与洞察、AI/agent 工作流、代码与产品上下文相连 |
| Jira | 帮助 “every team” 从想法走向交付的灵活、可扩展项目管理平台 | 软件、产品、营销、运营等跨职能团队，以及需要标准化、权限、合规和规模治理的复杂组织 | 多视图规划与跟踪、可配置 workflow、跨团队依赖、自动化与报告、3000+ integrations、企业安全治理与 Rovo/agent 能力 |

候选提出的 messaging gap 是：面向不想在“轻量速度”与“重型治理”之间二选一的产品组织，主张“低维护的跨角色可追溯协作”——把决策依据、责任、执行状态和结果证据连成一条默认可审计、但无需持续配置的协作链。该方向被明确标记为待验证假设：prompt 未提供我方产品、目标用户、可证明能力或客户研究，不能断言我方已经拥有该差异；厂商页面未突出某项叙事，也不能推导为竞品缺少对应能力。

机会与威胁同样保持证据边界：

- 机会：通过用户访谈和产品 proof 验证“低维护治理”“跨角色决策可追溯”与 “human-agent accountability” 是否比泛化的“更快、更简单”更有购买驱动力。
- 威胁：Linear 已把 agent-native 产品开发、代码执行与产品上下文纳入核心叙事；Jira 同时拥有广泛团队覆盖、企业治理、AI 和生态优势，宽泛的 AI 项目管理或一体化协作表述很快会同质化。
- 后续验证：补充我方能力清单、目标细分、产品试用、客户访谈和独立用户反馈后，才能把 gap 升级为正式 positioning。

## Fresh Without Skill / Baseline

- Actual access time: `2026-07-26 16:30 CST (Asia/Shanghai, UTC+08:00)`
- Actual source set independently selected by baseline:
  - Linear Method: https://linear.app/method/introduction
  - Linear switch positioning: https://linear.app/switch
  - Linear Jira Sync documentation: https://linear.app/docs/jira
  - Linear migration guide: https://linear.app/switch/migration-guide
  - Jira spaces/projects guide: https://www.atlassian.com/software/jira/guides/projects/overview
  - Jira navigation guide: https://www.atlassian.com/software/jira/guides/navigation/overview
  - Jira boards guide: https://www.atlassian.com/software/jira/guides/boards/overview
  - Jira getting-started guide: https://www.atlassian.com/software/jira/guides/getting-started/basics
  - Atlassian customer stories: https://www.atlassian.com/customers/

baseline 独立识别出：

- Linear 以 creators、purpose-built workflow、健康节奏和聚焦 backlog 为方法论，面向希望降低协调开销、快速推进产品开发的团队；Jira Sync 和迁移材料也显示其主动承接现有 Jira 团队的渐进迁移。
- Jira 面向组织内任何需要计划、组织和跟踪工作的团队，以高度可配置的 spaces、workflow、board、多项目导航和跨团队可视性支持从团队自治到公司级标准化的不同治理模式。
- 可切入的假设方向是“默认清晰但不牺牲治理”：用更少配置提供跨产品、工程和业务协作者都能理解的责任、决策和进展链。baseline 明确说明这只是从厂商公开定位推导的市场假设，尚未由我方能力、买家研究或竞品实测证明。

baseline 也指出两项威胁：Linear 已直接把传统协调工具描述为面向较慢时代，并提供 Jira 迁移路径；Atlassian 则以大规模客户基础、可配置性和跨产品平台覆盖复杂组织。它建议以用户访谈、迁移成本测试和我方能力 proof 验证 gap，避免直接使用无法证明的“兼具 Linear 简洁与 Jira 强大”表述。

## Assertion Results

| Assertion | With skill | Without skill | Fresh judge conclusion |
| --- | --- | --- | --- |
| `positioning` | PASS | PASS | 两者都分别说明 Linear 与 Jira 的定位、目标用户和核心卖点，并给出本轮实际访问的官方来源。 |
| `messaging_gap` | PASS | PASS | 两者都识别了未被充分占领的叙事机会；with-skill 进一步把机会、威胁和验证动作组织成完整 brief。 |
| `evidence_boundary` | PASS | PASS | 两者都将 messaging gap 标记为待验证策略假设，未把网页未强调的内容写成确定功能缺失，也未虚构我方能力。 |

## Failures and External-Service Triage

- 本轮两个 arm 均成功访问公开来源，未发生 research infrastructure failure，也未发现 assertion failure。
- 若官方页面、DNS、搜索或联网工具不可用，应记为 external-service / research infrastructure failure，而不是 skill regression；记录失败 URL、访问时间、HTTP 或工具错误后重试。
- 若单个页面改版、重定向或移除，应优先使用同厂商官方替代页面，并在 comparison 中记录实际 URL 与访问时间；不得沿用历史页面文案作为当前事实。
- 只有在公开来源可访问且证据足够时，with-skill 仍遗漏两家竞品的定位/目标用户/卖点、无法提出 messaging gap，或把推断伪装成确定事实，才判为 skill behavior regression。
- 定价、套餐权益、AI/agent 功能、客户数量、首页主标题、案例和发布说明都具有时效性；本 comparison 仅记录 2026-07-26 本轮访问时的研究结果，不是永久事实快照。

## Next Steps

- 后续 fresh eval 继续让 with-skill 与 baseline 各自实时联网、独立选择来源并记录实际时间和 URL，保持先锁定双 arm、再读取答案键的顺序。
- 若要把本轮 gap 转成我方定位决策，必须补充我方产品上下文、能力 proof、目标用户访谈、实际产品试用和更完整的第三方竞品验证。

## Runtime Artifacts Policy

- Runtime transcripts、完整模型输出、verdicts、timing、网页快照、outputs 与 diagnostics 不提交到 git。
- Durable 产物仅更新本 `comparison.md`；本轮未修改 fixture、metadata、skill 或 eval 定义。

## 2026-08-03 变更后回归（issue #188）

- 变更：删除 Analysis Frameworks 节并保留 Battlecard Mode 条件模式（A 维实测确认磨平）。
- 验证：L3 A 维 with/without 实测确认磨平（judge 独立判定，证据 `tmp/eval-runs/issue-188-l3/`）；删除后以原 eval prompt + fixture 重跑 with-skill，fresh judge 逐条判定原断言全部 PASS（3/3 PASS），Behavior result **PASS**，**无回归**（证据 `tmp/eval-runs/issue-188-regress/`）。

