---
feature: pm-agent-skill-optimization
version: 1.1.0
date: 2026-04-06
last_updated: 2026-04-06
---

# PM Agent Skill 优化设计计划

## 背景

目标是解释为什么同样的开场提示下，`superpowers` 在功能设计对话里表现更稳、更像资深 PM，并据此为当前仓库的 PM Agent 制定一次结构化优化计划。

本次分析基于三类材料：

- 本地对话记录：`tmp/dev-agent-skills.md` 与 `tmp/superpowers.md`
- 本仓库 PM 相关 skill：`agents/product_manager/skills/pm-agent/` 与 `agents/product_manager/skills/idea-to-spec/`
- `superpowers` 仓库公开 skill：`skills/brainstorming/SKILL.md` 与 `skills/writing-skills/SKILL.md`

参考仓库：

- <https://github.com/obra/superpowers>

## 一、为什么 superpowers 的功能设计对话更强

不是因为它“信息更多”，而是因为它把设计对话变成了一个强约束流程。

### 1. 先设计，后实现，而且有硬性门禁

`superpowers/skills/brainstorming/SKILL.md` 明确要求：

- 在任何实现动作之前，必须先完成设计并拿到用户批准
- 设计通过后，必须写成 spec 文档
- spec 写完还要做一次自检，再让用户 review

这类门禁会强迫模型把精力放在“收敛设计”而不是“立刻给方案”。

### 2. 问题节奏被限制得很严格

同一个 skill 里要求：

- 先看项目上下文
- 一次只问一个问题
- 优先给多选题
- 如果项目过大，先拆子项目，再只推进第一个子项目

这直接提升了对话质量。模型不容易一次性把假设铺满，也更容易让用户逐步拍板。

### 3. 不是直接给一个方案，而是先给 2 到 3 个路线

`superpowers` 要求先提出 `2-3 approaches`，明确 trade-off，再给推荐方案。

这会带来两个结果：

- 模型更像在做真实设计权衡，而不是凭直觉拍脑袋
- 用户更容易参与决策，而不是只能接受或否定一个单点答案

### 4. 设计是分 section 递进的，不是一口气全吐出来

它要求：

- 按 section 展示设计
- 每个 section 后都问用户“是否看起来对”
- 发现不对就回退澄清

你在 `tmp/superpowers.md` 里看到的 `Section 2 / 3 / 4`，本质上就是这个机制的自然产物。它不是偶然写得更清楚，而是提示词要求它必须这么推进。

### 5. 它强制把“设计结论”沉淀到文档

`superpowers` 明确要求把设计写入固定 spec 路径，再做 self-review 和 user review gate。

这会让模型天然关注：

- 当前是否已经达成足够稳定的结论
- 哪些内容适合进文档
- 哪些地方还存在歧义

所以它的对话更有“文档化收束感”，而不是停留在聊天建议层。

### 6. 它的 skill 作者指南专门防止“描述字段偷走流程”

`superpowers/skills/writing-skills/SKILL.md` 有一个很关键的经验：

- `description` 只能写“什么时候用”
- 不能在 `description` 里总结 skill 的流程

原因是：如果描述字段把流程提前讲掉，模型可能直接照描述走，而跳过正文里的完整流程。

这点对我们当前 skill 很关键，因为我们现在正好踩中了这个坑。

## 二、我们当前 PM skill 的主要问题

### 1. `idea-to-spec` 的 description 过长，而且混入了流程摘要

文件：

- `agents/product_manager/skills/idea-to-spec/SKILL.md`

现状：

- description 很长
- 除了触发条件，还写了 greenfield、existing-project、internal routing 等流程信息

风险：

- 模型可能只读到“这是个会做若干阶段分析并路由的 skill”
- 但不会真正遵循正文里那些阶段性约束

这和 `superpowers` 在 `writing-skills` 里强调的反模式完全一致。

### 2. 我们的正文像操作手册，但不像强约束协议

`idea-to-spec/SKILL.md` 虽然写了很多 phase，但大多数是：

- should / goal / work through
- recommend next step
- confirm at least

缺少的是强制行为，比如：

- 一次只问一个问题
- 先给方案选项再收敛
- 每个 section 必须单独确认
- 在用户批准前，不得进入文档生成或后续技能

结果就是模型很容易“看起来遵守了大方向”，但实际对话仍然走成一次性咨询答复。

### 3. 缺少“设计对话协议”

当前 skill 有 lane、phase、handoff，但没有对功能设计对话最关键的协议层：

- 如何分段推进
- 什么时候停止追问
- 什么时候必须让用户拍板
- 如何记录已确认决策
- 如何把确认过的决策带入下一段

所以输出容易变成：

- 先做一轮上下文总结
- 直接给推荐方案
- 顺手加几个默认假设

这正是 `tmp/dev-agent-skills.md` 里的表现。

### 4. 没有显式要求“比较备选方案”

当前 `idea-to-spec` 确实会讨论架构 options，但没有明确规定：

- 在需求和信息结构不稳定时，先给 2 到 3 个产品/交互/数据模型方案
- 每个方案必须给 trade-off
- 必须明确推荐一个默认路线，并说明原因

因此模型倾向于直接输出自己最先想到的解法。

### 5. 没有文档落地门禁

当前 skill 只说：

- Markdown by default
- 只有用户明确同意才写文件

这在“谨慎写文件”上是合理的，但副作用是：

- 模型不会自然把“写文档”当成设计流程的一部分
- 用户不额外提醒时，设计就容易停在聊天里

而 `tmp/superpowers.md` 中最强的一点，正是它会主动把“接下来写入 spec”变成对话目标的一部分。

### 6. 路径引用错误，说明技能文案是移植过来的，未完全本地化

当前 `idea-to-spec` 内部大量引用：

- `skills/product-dev/idea-to-spec/...`

但本仓库实际路径是：

- `agents/product_manager/skills/idea-to-spec/...`

这不是单纯文档小问题，而是信号问题：

- skill 看起来完整，但内部引用和仓库现实不一致
- 降低模型对“这是一份当前仓库真实协议”的可信度

### 7. `pm-agent` 应定义为 PM 能力入口、路由器和编排器

文件：

- `agents/product_manager/skills/pm-agent/SKILL.md`

`pm-agent` 更接近 `superpowers` 里的 `using superpowers`，应作为 PM skill 体系的 meta skill：

- PM 能力统一入口
- 意图判断与技能路由
- 必要时进行多 skill 编排

按照这个设计，`pm-agent` 应负责：

- 识别请求类型
- 选择最合适的下游 skill
- 在跨 skill 请求中定义主 skill 与后续链路
- 在意图不清时，只做路由级澄清

`pm-agent` 不负责：

- 主持完整的功能设计对话
- 承担 section-by-section 的设计收敛
- 生成 PRD / TRD 正文
- 复制 `idea-to-spec` 的协议、澄清流程和文档生成逻辑

- `pm-agent` 是 meta skill / dispatcher / orchestrator
- 功能设计质量的主战场在 `idea-to-spec`
- `pm-agent` 只需要保证功能设计类请求稳定路由到 `idea-to-spec`

### 8. 缺少针对“设计对话质量”的评测用例

当前 `product_manager/test/` 里几乎没有针对：

- 逐段确认
- 选项对比
- decision capture
- 文档落地承诺

的评估样例。

没有这类 eval，skill 质量只能靠主观感觉，很难稳定迭代。

## 三、优化目标

这次优化不应该只是“把文案写得更长”，而是把 PM skill 体系从“会写文档的工具集合”升级成“能稳定主持设计收敛并沉淀文档的体系”。

核心目标：

1. 对功能设计类请求，先进入设计收敛协议，而不是直接给方案
2. 强制多轮、单问题、可拍板的交互节奏
3. 强制备选方案比较，而不是单路推荐
4. 强制形成 decision ledger，避免对话上下文丢失
5. 把“写入文档”变成流程目标，而不是可有可无的附带动作
6. 用 eval 验证这些行为真的被触发，而不只是写在 skill 里

## 四、建议的改造方案

### Phase 1：修正入口触发与基础协议

目标：先解决最基础的触发和执行偏差问题。

#### 4.1 重写 `idea-to-spec` 的 description

设计原则：

- `description` 只描述触发条件和目标输出
- `description` 不描述工作流、lane、phase、routing、handoff、internal skill
- `description` 需要覆盖三类场景：新产品或新功能想法、已有项目新增能力、已有 spec 或设计变更

目标是让模型一眼知道何时触发这个 skill，而不是在 description 中提前消费正文协议。

建议控制在一句话，最多两句话。

#### 4.2 定义 `pm-agent` 作为入口 skill 的设计边界

`pm-agent` 的设计原则如下：

- 如果是功能设计、需求收敛、能力规划类问题，默认路由到 `idea-to-spec`
- 只有明确是竞品分析、roadmap、release notes 之类请求时，才路由到其他 skill
- 如果请求跨多个 skill，先确定主 skill，再定义后续链路
- 如果意图不清，只允许提出路由级问题，不进入具体设计细节

目标是把 `pm-agent` 明确定义为 PM 能力入口、路由器和编排器，而不是功能设计执行器。

#### 4.3 修正所有错误的内部路径引用

将 `skills/product-dev/idea-to-spec/...` 统一修正为当前仓库真实路径，避免提示词与代码结构脱节。

### Phase 2：为功能设计引入显式对话协议

目标：把 `superpowers` 最有效的部分内化成我们自己的 PM 设计流程。

建议在 `idea-to-spec` 顶层增加一个新段落，明确功能设计默认采用如下协议。

#### 4.4 功能设计对话协议

对功能设计类请求，`idea-to-spec` 应默认采用如下协议：

1. 读取项目上下文与现状
2. 输出一段简短 context summary
3. 以单决策点方式推进当前回合
4. 遇到关键设计取舍时，先给 `2-3` 个候选方案
5. 用户拍板后，再展开当前 section 的细化设计
6. 每完成一个设计 section，都要求用户确认
7. 所有确认项写入 `DECISIONS.md`
8. 已收敛的 section 及时写入 feature 文档
9. 每个阶段结束后做一次统一收束

#### 4.5 引入单决策点推进协议

这里不采用字面意义上的“每次只能有一个问句”，而是采用更适合 PM 设计的规则：

- 每个回合只解决一个待确认决策点
- 必要时可以附带 `2-3` 个选项和推荐方案
- 不得并行推进多个未确认议题
- 如果用户要求一次看完整设计，可以先给完整草案，但必须明确哪些内容仍未确认

这样既能保持对话节奏清晰，也能避免模型用隐含假设补全未回答问题。

#### 4.6 强制先出备选路线

对关键设计点，默认先做备选方案比较。

适用范围包括：

- 数据模型
- 交互形态
- 查询 / 筛选语义
- 权限边界
- 删除 / 迁移 / 兼容策略
- 分阶段实施方式

协议要求：

- 默认提出 `2-3` 个可行方案
- 每个方案必须附带一句 trade-off
- 必须推荐一个默认方案
- 用户拍板前，不进入该决策点的细化设计

#### 4.7 引入 section-based 设计推进

对功能设计类请求，采用固定的 section 顺序逐段推进：

1. 范围与目标
2. 核心对象与数据模型
3. 接口与查询/写入语义
4. 前端交互形态
5. 异常与边界处理
6. 分阶段实施与测试范围

协议要求：

- 每完成一个 section，必须等待用户确认或修改
- 当前 section 未确认前，不进入下一个 section
- 如果用户要求先看全稿，可以先给完整草案，但必须显式标记未确认的 section

#### 4.8 引入 decision ledger

对功能设计类请求，维护一份 feature 级的轻量决策账本。

文档路径采用短命名体系：

- `docs/pm/{feature-name}/DECISIONS.md`

该文档至少包含四类内容：

- 已确认决策
- 待确认问题
- 被否决方案
- 默认假设

使用规则：

- 用户拍板后的结论立即写入“已确认决策”
- 为了推进而采用的临时默认值写入“默认假设”
- 已否定路线写入“被否决方案”，防止后续回绕
- 后续 section 推进和文档生成必须以该账本为准

`DECISIONS.md` 作为 feature 的上游决策主档，供 `docs/design/`、`docs/engineer/`、`docs/qa/`、`docs/devops/`、`docs/security/` 下的文档统一引用。

### Phase 3：加强“文档化收束”

目标：让设计对话自然落到文档，而不是停在聊天里。

#### 4.9 新增文档落地规则

文档化不应只发生在对话最后，而应采用“增量落档 + 阶段收束”协议。

目录空间统一采用短命名体系：

- `docs/pm/`
- `docs/design/`
- `docs/engineer/`
- `docs/qa/`
- `docs/devops/`
- `docs/security/`

PM 侧默认文档路径：

- `docs/pm/{feature-name}/DECISIONS.md`
- `docs/pm/{feature-name}/PRD.md`
- `docs/pm/{feature-name}/BRD.md`
- 在尚未拆分前允许使用 `docs/pm/{feature-name}/design.md` 作为过渡草稿

协议要求：

- 当用户明确要求落文档时，必须写文档
- 当一个关键决策被确认时，必须及时更新 `DECISIONS.md`
- 当一个 section 收敛时，必须及时写入对应 PM 文档
- 长对话继续前，应优先回读 feature 文档，而不是只依赖对话上下文

#### 4.10 增加阶段收束与文档自检环节

增量落档解决的是持久记忆，阶段收束解决的是文档表达一致性。

每个设计阶段结束后，必须对当前 feature 文档做一次统一收束，目标是把过程性表达整理为正式、稳定、可引用的文档语言。

收束要求：

- 正文只陈述当前有效设计
- 不保留“纠正上一版说法”的辩解式表述
- 不在正文中保留过程性的来回讨论痕迹
- 若需保留演进过程，放入 changelog 或 decision history，而不是正文设计章节

文档自检检查项：

- 是否还存在 TBD / TODO / 模糊表述
- section 之间是否矛盾
- 是否缺失边界条件
- 是否已经足够支撑工程实现与 QA 测试

这个自检逻辑可以放在 `idea-to-spec` 末尾，也可以落到 `prd-gen` / `trd-gen` 的 shared conventions。

### Phase 4：建立 PM skill 评测闭环

目标：避免优化只停在“我们觉得更好”。

#### 4.11 为 `idea-to-spec` 新增对话式 eval

最少补 3 类样例：

1. 已有项目新增功能
2. 已有功能变更
3. 纯新想法探索

每类 eval 不只看最终文档，还要看中间行为是否符合协议。

#### 4.12 评测指标从“内容完整”升级为“对话行为 + 结果质量”

建议加入以下检查点：

- 是否先读项目上下文
- 是否采用单决策点推进
- 是否给出 2 到 3 个方案
- 是否逐 section 推进
- 是否维护 `DECISIONS.md`
- 是否进行增量落档
- 是否执行阶段收束
- 是否在用户确认前避免进入实现态

## 五、建议修改的文件范围

首轮优化建议只动以下文件：

- `agents/product_manager/skills/pm-agent/SKILL.md`
- `agents/product_manager/skills/idea-to-spec/SKILL.md`
- `agents/product_manager/skills/idea-to-spec/_internal/_shared/skill-map.md`
- `agents/product_manager/skills/idea-to-spec/_internal/_shared/gen-conventions.md`
- `agents/product_manager/skills/idea-to-spec/_internal/_shared/quality-rules.md`
- `agents/product_manager/test/idea-to-spec/` 下新增 eval 用例

第二轮再决定是否下沉到各个 `*_gen`、`*_iteration`、`*_validator` 的细节指令。

## 六、建议的实施顺序

### Milestone 1：协议修正

- 重写 `description`
- 补充 design protocol
- 加入单问题与 section gate
- 修复错误路径

预期收益：

- 立刻改善第一轮对话表现
- 降低“直接给答案”的倾向

### Milestone 2：文档化收束

- 引入 `docs/pm/{feature-name}/DECISIONS.md`
- 统一短命名文档路径体系
- 增加增量落档规则
- 增加阶段收束与文档自检

预期收益：

- 长对话中的设计信息不丢失
- 文档表达更稳定、可引用
- 与跨 agent 协作文档结构一致

### Milestone 3：评测闭环

- 新增 eval
- 以 `tmp/dev-agent-skills.md` 中的标签功能设计场景作为回归样例
- 与优化前输出做对比

预期收益：

- 后续每次调 prompt 都能知道有没有退化

## 七、验收标准

优化完成后，针对“已有项目新增一个标签系统”这类请求，PM Agent 应表现出以下特征：

1. 先由正确 skill 接住请求；功能设计类请求应稳定进入 `idea-to-spec`
2. 在 `idea-to-spec` 中先总结现状，再提问，而不是直接给完整方案
3. 每次只推进一个待决策问题
4. 在关键设计点至少提出 2 个可比较路线
5. 能把设计拆成多个 section 逐段确认
6. 会把已确认决策及时写入 `docs/pm/{feature-name}/DECISIONS.md`
7. 会把已收敛内容增量写入 PM 文档，而不是只依赖对话上下文
8. 会在阶段结束后统一收束文档表述，避免正文残留过程性纠偏语言
9. 最终 PRD/TRD 的内容能直接继承前面对话结论，而不是重新发明

## 八、结论

`superpowers` 的优势不在“它更会写 PRD”，而在“它把设计讨论写成了强协议”。

我们当前 PM Agent 的主要短板也不是知识不够，而是：

- 触发描述不够干净
- 对话协议不够硬
- 决策收敛机制不够明确
- 文档化闭环不够强

因此最值得做的不是继续加更多 schema，而是先把 `idea-to-spec` 改造成一个真正的“设计主持 skill”。
