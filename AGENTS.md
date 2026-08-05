# 仓库指导

本文件为在本项目中工作的 AI coding agents 提供仓库级指导。

## 仓库架构

本仓库是一个多 Agent skill marketplace，发布 7 个按角色划分的 Agent，覆盖产品、工程、QA、DevOps、设计、安全和正式文档工作流。每个 Agent 包含多个遵循统一结构的 skill。目前主要面向 Claude Code 和 Codex 编写。

### 核心概念

**Agent 结构**

- 每个 Agent 位于 `agents/{agent-name}/`
- 每个 Agent 包含 `README.md`、`skills/` 和 `test/`
- Agent 按角色组织，而不是按工具组织

**Skill 结构**

- `SKILL.md` 是公开 skill 文档
- `_internal/` 为可选目录，仅在 skill 需要分阶段或分模块渐进加载指令时使用；简单 skill 允许只有单文件 `SKILL.md`
- 使用 `_internal/` 时，每个内部模块目录只保留一个 `INSTRUCTIONS.md` 作为指令入口，跨模块共享内容放 `_internal/_shared/`
- Skill 使用 YAML frontmatter 保存元数据

**文档组织**

- 公开项目文档应遵循 `docs/{agent}/{feature_path}/`，`feature_path` 可包含多级 lower kebab-case 路径段
- 文档 frontmatter 应包含 `feature`、`version`、`date` 和 `last_updated`
- 仓库级发布变更记录按版本归档到 `docs/changelog/changelog-v{version}.md`；根目录 `CHANGELOG.md` 只作为索引，不重复维护 changelog 条目
- 除发布 changelog 归档外，文档版本历史通过 git 追踪，不要创建多个版本化文件
- 窄例外（仅限实施计划归档）：`feature-implementor` 的完成态或废弃态实施计划经 closeout 和用户/维护者审批后，可归档到 `docs/engineer/{feature_path}/implementation-plans/archive/IMPLEMENTATION_PLAN-<scope>.md`；`<scope>` 使用 lower kebab-case 描述该次实现范围。当前活跃计划入口仍固定为 `docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md`。该例外只覆盖实施计划归档，不适用于 PRD、TRD 或其他文档类型
- QA E2E 测试资产统一位于 `docs/qa/e2e/{feature_path}/`；`TEST_SUITE.md` 是功能测试套件索引，`FLOW_INDEX.md` 记录流程覆盖关系，`cases/` 存放 `TC-NNN-<short-slug>.md`，`scripts/` 存放可执行流程脚本片段，`results/` 按 TC 和平台版本追加执行结果，`_reports/{platform-version}/test-reports-{test-time}.md` 存放功能更新汇总报告；发版全量报告位于 `docs/qa/e2e/_reports/{platform-version}/test-reports-{test-time}.md`
- 文档功能树的全量结构梳理由 `pm-agent -> idea-to-spec:structure-governance` 进入，只读扫描角色过程文档并在运行期 tmp 生成报告；任何拆分或移动仍须提案确认后按 `major` 变更执行

**市场注册**

- `.claude-plugin/marketplace.json` 定义所有 Agent 及其 skills
- `.claude-plugin/marketplace.json` 的 `metadata.version` 必须等于当前仓库 release 版本但不带 `v` 前缀；每次创建 release tag 前，先把该字段更新到目标版本，并确认存在对应 `docs/changelog/changelog-v{version}.md` 与根 `CHANGELOG.md` 索引。`.kimi-plugin/plugin.json` 的 `version` 必须与 `metadata.version` 保持一致（由 `check_repository_contract.py` 强制校验）
- `skills-lock.json` 保存已安装 skill 的元数据

### Agent 协作流

```text
PM Agent → Designer Agent → Engineer Agent → QA Agent → DevOps Agent → Security Agent
   ↓           ↓               ↓              ↓           ↓              ↓
  PRD      UI/UX Spec        TRD          Test Report  Deploy Config  Security Review
           Visual System   Code Changes                  CI/CD

PM / Engineer / QA / DevOps（条件式）→ Docs Agent（正式文档生产 / 审计）
                                  ↓
                             Formal Docs
```

**PM 唯一入口与下游 gate 指针**

- 用户侧新需求、变更、bug、测试、部署、安全、交付或仓库状态诉求默认先进入 `pm-agent` 分类；下游 role router 和 specialist 只在 PM handoff packet 或等效已确认文档链存在时承接。
- 用户未显式点名任何 skill 或 agent 时，默认进入 `pm-agent`；用户显式点名某个 skill 或 agent 时，这是受支持的直达路径，但仍必须经过对应入口 gate 的安全网。
- PM handoff packet 字段定义以 `agents/product_manager/skills/idea-to-spec/_internal/_shared/skill-map.md` 为权威；`AGENTS.md` 不复制字段清单。
- 下游安全网包含前置与收尾两面：缺少 PM handoff packet、等效已确认文档链或 specialist entry basis 时，温和引导用户经 `pm-agent` 补齐前置；完成当前事项后，主动建议协作链下一步并等待确认，用户已授权 `auto-continue` 时可连续推进直到链路结束或用户喊停。
- 跨角色收尾与 `auto-continue` 的权威定义在 `agents/product_manager/skills/idea-to-spec/_internal/_shared/skill-map.md` 的 `Safety-Net Closeout and Auto-Continue` 节；`AGENTS.md` 只保留入口契约和指针。
- SKILL.md frontmatter 的 `visibility: internal` 是声明层标记，Claude Code 与 Codex 都不消费该字段，不隐藏 slash 命令也不阻止显式直调；`pm-agent` 是默认入口，下游标记为 `internal` 仅表示非默认入口。
- 6 个 role router 只保留入口凭据检查和分流指针，其中 `docs-agent` 分流正式文档站点 bootstrap、API/database/design/ops/product 当前事实 sync、基于运行界面截图的图文用户操作手册、站内 Release Notes 和 audit；PM `github-release-generator` 按 SKILL.md 的宿主文档站适用性判断生成 GitHub Release：有文档站宿主要求站内 Release Notes 已确认且 docs-audit 门禁通过；无文档站宿主降级为维护者确认的版本事实源与维护者显式批准；具体执行 gate 的权威副本留在对应 specialist `SKILL.md`，例如 `feature-implementor` 的 PRD/TRD/plan/archive gate、`debugger` 的 expected-behavior gate、QA specialist 的 E2E gate，以及 Designer/DevOps/Security/Docs specialist 的 feature-scope gate。
- 直接调用下游且没有 PM handoff packet、等效已确认文档链或 specialist entry basis 时，不执行下游协议，应温和引导用户经 `pm-agent` 补齐前置并完成入口分类；脚手架请求同样走正常 PM 分类。

**文档依赖**

- 6 个现有 Agent 按 `agents/product_manager/skills/idea-to-spec/_internal/_shared/consumption-contract.md` 消费宿主正式文档
- Docs Agent 读取 `docs/pm/{feature_path}/`、`docs/engineer/{feature_path}/TRD.md` 与代码证据
- Security 的确认结论（审查发现，或对整改已落地的复审确认）改变正式文档事实、对外行为、运维事实或发版就绪状态时，按 `agents/product_manager/skills/idea-to-spec/_internal/_shared/skill-map.md` 的 `Security Conclusion Escalation to PM` 规则把结论与证据回交 `pm-agent` 分类并提 issue；后续 Docs / Engineer / 发版工作由 `pm-agent` 通过正常 handoff packet 分派，各 specialist 按既有门禁执行
- Engineer 读取 `docs/pm/{feature_path}/` 和 `docs/design/{feature_path}/`
- QA 读取 `docs/pm/{feature_path}/` 和实现代码
- QA 在进行广泛项目探索前，先读取已有的 `docs/qa/e2e/{feature_path}/TEST_SUITE.md`、`FLOW_INDEX.md`、`cases/*.md` 和 `scripts/*.spec.md`
- DevOps 读取 `docs/engineer/{feature_path}/TRD.md`
- Designer 读取 `docs/pm/{feature_path}/PRD.md`
- Security 读取 `docs/pm/{feature_path}/` 和代码库

**角色边界**

- Designer Agent 停在 `docs/design/{feature_path}/` 下的设计交付物，不实现代码
- Engineer Agent 在 PM 范围确认后负责 `docs/engineer/{feature_path}/TRD.md`
- Engineer Agent 负责把 PM 和 Designer 文档转成代码、测试和交付产物
- 读取 PM spec 或 design spec 不代表 Designer Agent 可以继续进入实现
- TRD 确认后，`feature-implementor` 负责产出 `docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md` 并按计划实现
- Docs Agent 负责宿主 `docs/site/` 正式文档层，不修改其他角色拥有的过程文档契约
- 新文档编写任务默认委派给 sub-agent，主进程保留上下文、审查结果并决定 handoff

## 开发工作流

> [!IMPORTANT]
> `AGENTS.md` 是仓库指导的唯一来源。`CLAUDE.md` 必须保持为指向 `AGENTS.md` 的相对软链接，不要单独编辑。

### 仓库治理

- Branch、tag、release、bypass 和仓库设置权限默认只授予唯一管理员；需要维护者或机器人时再显式添加。
- 维护变更不得直接在 `main` 上进行；开始修改前先创建工作分支，完成后通过 PR 合入。
- PR 创建后的更新默认追加新 commit 并普通 push；除非用户明确要求整理提交历史，否则不要 amend、rebase 或 force push。
- 创建 PR 后不要直接合并；必须等待维护者明确确认“可以合并”后再执行 merge / squash / rebase 合并操作。
- 当前仓库仍处于早期维护阶段，暂不新增 Release CI；发布前使用手动 release checklist：确认 `.claude-plugin/marketplace.json` 的 `metadata.version` 已更新为目标版本且不带 `v` 前缀，确认 `docs/changelog/changelog-v{version}.md` 存在并已被根 `CHANGELOG.md` 索引，tag 使用 `v` 前缀 SemVer，PR 必跑 CI 全部通过，必要时手动触发 eval workflow 并记录结果；每次使用 tag 发版时，按 skill 维度汇总 skill eval 后的 `comparison.md` 最新结论。每次 tag 发版后，由 `pm-agent → github-release-generator` 使用 skill 流程自动创建 GitHub Release draft，并直接交维护者审批；draft 的发布（publish）仍必须等待维护者显式批准。不要自动上传 marketplace package，也不要配置 release bot bypass tag ruleset。

### 变更分级契约

本节是变更分级（`change_tier`）的唯一定义源。所有角色的门禁按 `change_tier` 取强度，不再各自默认最严；分级只调整门禁的形态和确认次数，不取消任何证据要求，`hotfix` 仍必须留下验证证据和结果记录。

| 等级 | 典型场景 | 判定信号 |
| --- | --- | --- |
| `hotfix` | 单文件轻量修复、typo、配置修正、已有失败测试的直接修复 | 不改变已批准 PRD/TRD 预期；变更可由一条验证命令覆盖 |
| `standard` | 常规功能实现、现有功能行为调整、多文件重构 | 有对应 `feature_path`；预期可能变化，需要 PRD/TRD 对齐 |
| `major` | 跨角色大功能、新增 agent/skill、契约面变更、发布 | 影响多个角色文档、marketplace 注册表或 contract 脚本 |

判定入口：由 `pm-agent` 在入口分类时判级，并把 `change_tier` 写入 handoff packet，fast lane 判定直接引用本契约的 `hotfix` 判定。判定信号不满足、预期可能变化或无法判级时，一律按 `standard` 处理；试图以 `hotfix` 名义跳过预期变更对齐的请求必须 blocked 或回 PM。

各门禁按等级取强度：

| 门禁 | `hotfix` | `standard` / `major` |
| --- | --- | --- |
| plan gate（`feature-implementor`） | 允许轻量计划形态：在现有活跃计划中追加 scope 条目或使用简化模板，具体形态由 TRD 阶段确定；仍需一次用户确认 | 维持完整 `IMPLEMENTATION_PLAN.md` 确认流程 |
| closeout / archive gate（archive gate 见 issue #54） | 合并 closeout 与归档为一次确认 | 维持独立审批 |
| QA E2E 门禁 | 只要求验证直接影响路径并追加结果 | 维持 PRD/TRD 预期对齐门禁 |
| PM entry gate | 与交付类请求（delivery / 状态查询）走 fast lane，分类后立即放行 | 新需求、预期变更、范围不清一律留在 PM |

skill eval 的 Fresh Sub-Agent 门禁作用于 skill 自身的测试流程，不参与本分级。

### 新增 Agent

1. 创建目录结构：
   ```bash
   mkdir -p agents/{agent-name}/{skills,test}
   ```

2. 按现有 Agent 模式创建 `agents/{agent-name}/README.md`

3. 为每个 skill 创建：
   - `skills/{skill-name}/SKILL.md`
   - `test/{skill-name}/evals/evals.json`
   - 仅在需要渐进加载时创建 `skills/{skill-name}/_internal/`

4. 在 `.claude-plugin/marketplace.json` 注册 Agent：
   ```json
   {
     "name": "{agent-name}-agent",
     "description": "...",
     "skills": ["./agents/{agent-name}/skills/{skill-name}"]
   }
   ```

5. 使用新 skill 元数据更新 `skills-lock.json`

6. 添加 eval 测试，并对比使用 skill 与不使用 skill 的结果

### 新增或重命名 Skill 的同步面

向既有 Agent 增加一个 specialist 时，改动会扇出到注册、路由、发现、文档、eval 和过程文档六个面。任一面漏改都不会被契约脚本拦住，但会让 skill 在实际使用中不可达或不可信。按下表逐项核对，不要只改「主要」文件。

| 面 | 必改项 |
| --- | --- |
| 注册 | `.claude-plugin/marketplace.json` 的 `skills` 数组；`skills-lock.json` 条目与 `computedHash` |
| 路由 | router `SKILL.md` 的 Available Skills、Routing Signals、Specialist Gate Pointers、Role Boundary 中列举 specialist 的那句 |
| **发现** | `.claude-plugin/marketplace.json` 的 agent `description`；router `SKILL.md` 的 frontmatter `description`；`AGENTS.md` 中描述该 router 分流范围的根路由指针句 |
| 仓库指导 | `AGENTS.md` 的该 Agent specialist 计数与 Specialist skills 总数 |
| Agent 文档 | `agents/{agent}/README.md` 的 skills 表、计数与 **Routing Rules 小节**；`README_zh.md` 同步 |
| 顶层入口 | 根 `README.md` / `README_zh.md` 的 Agent 表计数与能力描述；**`pm-agent/SKILL.md` 的 handoff targets、请求分类行与 Default Routes** |
| eval | 新 skill 自己的 evals；**router 的路由 eval**；被本次改动影响的既有 skill 的断言与其 durable `comparison.md` |
| 过程文档 | PRD/TRD/实施计划的触点表与禁止区必须与实际 diff 一致；父 PRD 的 `child_features` 与其中描述注册面的行 |

加粗项是最容易漏的：

- **发现层**决定客户端在读正文之前是否会选中这个 skill。计数和正文改全了、描述没改，等于新能力在元数据层不存在。
- **router 路由 eval** 缺失时，路由分支写错也能全绿通过。
- **PM 入口分类**：`pm-agent` 是默认用户入口，用户不点名 skill 时全部经它分类。下游 router 认识新 specialist，但 PM 的分类词典里没有对应说法时，该能力对普通用户不可达。
- **既有 skill 的 eval 与 comparison**：本次改动若扩展了它们断言依赖的契约（例如资产数量、类型枚举），旧断言会 stale，旧 `comparison.md` 会让发版评审读到过时结论。此时保留历史结论并标注其适用的旧契约，`Overall result` 记为 `BLOCKED` 待重跑，不要伪造成新的 PASS。
- **过程文档与实际 diff 的一致性**：计划里写成禁止区、实际却改了的文件，会让后续维护者按文档回退掉必要修改。

扩展共享契约（如 `doc_type` 枚举）时，还要同步其全部副本：权威定义、消费方 skill 中的复制表、以及 `docs-site-bootstrap` 交付给宿主的脚本资产与模板。交付给宿主的脚本副本不会随 marketplace 更新自动升级，存量宿主需重跑 bootstrap，PR 中要说明这一点。

### Skill 设计原则

- **文档驱动**：skill 消费和产出 Markdown 文档
- **技术栈无关**：除非项目要求，否则不要假设特定框架
- **最小且聚焦**：每个 skill 只承担一个清晰职责
- **可独立触发**：skill 应能独立工作，而不是只能作为链路一环
- **业务友好**：尽量优先保证非技术用户也能理解

### QA E2E 测试用例持久化

单独使用 QA 或执行 E2E 时，重新探索项目前必须先复用功能树下的持久化测试用例记忆：

- 先确认测试场景：`feature-update` 表示功能更新，在开发环境本地验证更新功能和直接影响路径；`release` 表示发版，在发版版本测试环境执行全部 active E2E 用例
- 先确认测试平台版本；缺失时必须 blocked 并询问用户，不得使用 `unknown` 目录归档
- 先读取 `docs/qa/e2e/{feature_path}/TEST_SUITE.md`、`FLOW_INDEX.md`、`cases/*.md`、`scripts/*.spec.md`、历史 `results/` 和 `_reports/`
- 基于 PRD/TRD 生成 E2E 测试时，直接按 `docs/qa/e2e/{feature_path}/` 分类和记录，不再新增 `docs/qa/{feature}` 入口
- 每个 E2E 测试用例单独存为 Markdown 文件，放在功能目录的 `cases/` 下，命名为 `TC-NNN-<short-slug>.md`；对应流程脚本放在 `scripts/TC-NNN-<short-slug>.spec.md`
- `scripts/*.spec.md` 可以保存可执行脚本片段以保证重复执行一致，但不得包含明文账号、密码、token、cookie、session、SSH 密码或 SSH key 内容
- 多个 TC 复用 `docs/qa/e2e/_shared/login-flows/` 下的登录方式；测试账号只引用账号 ID
- 平台账号和 SSH 账号统一存放在本地 `.qa/e2e/accounts.local.json`，该文件必须被 `.gitignore` 屏蔽；账号落盘格式遵循 `agents/qa/skills/qa-agent/references/e2e-credential-store.md`
- 执行入口优先级为 repo harness > Chrome plugin / browser connector > Playwright fallback；repo harness 存在且覆盖当前 TC 时必须优先使用
- 单个 E2E 测试任务默认由 subagent 执行，主 agent 负责范围确认、拆分、结果确认和按 `agents/qa/skills/qa-agent/references/e2e-test-report.md` 生成汇总报告
- 现有功能变更或 bug 修复触发 E2E 文档更新前，必须先完成 PRD/TRD 预期对齐；预期变化回 PM，TRD gap 回 `trd-gen`，文档缺失或预期不清时 blocked；门禁强度按「变更分级契约」的 `change_tier` 取值，`hotfix` 只要求验证直接影响路径并追加结果，`standard` 以上维持预期对齐门禁
- 代码完成后的 E2E 文档补充必须引用已确认的 `docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md`；任何等级都不能跳过实施计划门禁，`hotfix` 可引用「变更分级契约」允许的轻量计划形态
- 已有 E2E 测试基于功能更新增量更新，历史结果只追加不覆盖

### Skill 测试

每个 skill 包含 `test/{skill-name}/evals/evals.json`、eval workspace，以及每个 eval 的 `comparison.md`（使用与不使用 skill 的最新持久化对比结果）。

Skill eval 是可用性测试：验证 skill 能被触发、协议可执行、能产出该角色预期的结构化产物。断言检查 skill 特有行为——上下文读取、执行路径选择、证据处理、阻塞假设、handoff 边界，而不是泛化回答质量。

更新 skill 文档、内部指令或影响 skill 行为的 fixture 后，主动询问是否运行对应 eval。实际执行过 eval 就必须在同一轮变更中更新 durable `comparison.md`；无法生成 baseline、没有可更新文件或不适用时，写明 blocked 或不适用原因。缺少 runner、凭据或外部服务导致无法执行时明确记 blocked，不得静默降级成只读静态验证。

**Eval 定义契约**

- 使用共享 `evals.json` schema version `1.0`，不允许 Agent 专属例外
- 位于 `agents/{agent}/test/{skill-name}/evals/evals.json`，顶层含 `schema_version`、`agent`、`skill_name`、非空 `evals`；`skill_name` 与对应 `SKILL.md` 对齐
- 每个 eval item 含 `id`（格式 `eval-NNN-short-slug`）、非空 `name`/`description`/`prompt`/`expected_output`、显式 `workspace`（值为 `workspace/...`）、非空对象形式 assertions
- 每个 assertion 含 lower snake_case `id`、非空 `description` 和非空语义化 `text`；不允许纯字符串 assertion
- 优先语义断言，避免脆弱的精确字符串检查。语言或格式可合理变化时（如本地化、等价的 lane label），保持预期语义即可
- 提交前运行 `uv run scripts/check_eval_contract.py`

**Eval 执行契约**

- 最终验证必须在与被测会话隔离的全新上下文中执行。全新 Codex subagent 与各自独立启动的 `codex exec` 会话都可接受，本质都是干净上下文。
- 每轮必须重新生成 `without_skill` baseline，**不得复用历史 baseline**，也不得为掩盖执行失败把 baseline 弱化成可选项。
- 判定由独立评审方（fresh subagent 或独立 judge）对照 assertions 得出。**被测 lane 的自评不算判定**，评审方须独立核对零写入等关键事实。批量 transcript 生成脚本的输出只是诊断产物，不是 pass/fail 事实来源。
- 运行期文件写隔离 scratch workspace（如 `tmp/eval-runs/...`），不得写入已提交 fixture——历史输出会污染 empty-workspace 这类上下文敏感用例。每轮运行前需清理的路径用 `eval_metadata.json` 的 `execution_cleanup` 声明。
- 只在实际存在 deterministic runner 时声明 run diagnostics（command、cwd、timeout、return code 等），便于区分基础设施失败与 assertion 失败。

**Eval prompt 与 lane 隔离契约**

`with_skill` 与 `without_skill` 的**唯一变量是「是否加载被测 skill 文档」**：prompt 逐字相同，可见 fixture 完全相同。任何把 skill 规则提前透给 baseline 的做法都会让两条 lane 拉不开差距，eval 失去判别力。

prompt 写成自然用户目标。判据：*删掉这句话，一个不懂 skill 协议的 agent 就不知道该怎么做了——那它就是泄漏。*

| 不得写进 prompt | 应当写进 prompt |
| --- | --- |
| 协议名与步骤名：「按八步契约执行」 | 自然目标：「写一份用户操作手册，要有操作步骤和对应截图」 |
| 行为规则与禁令：「不要替维护者确认」「保持零启动命令」 | 环境客观事实：「当前没有可通过域名访问的部署环境」 |
| skill 专有分类术语：「这是 feature-update 场景」 | 入口凭据：「pm-agent 已分类并路由至此，packet 见 `PM_HANDOFF.md`」 |
| 产物字段清单、目录分层、命名规范、工具与参数 | 自然授权：「范围我已经定好了，不用再跟我确认」 |

最后一行是测试**需要用户确认的门禁**的正确方式：用真实用户会说的话表达授权，而不是「Step N 门禁视为已通过」这类协议术语——后者直接把门禁的存在告诉了 baseline。

lane 可见素材只给宿主环境事实，评测脚手架一律不给：`eval_metadata.json` 含评判意图，运行目录中应物理移除；`pm-handoff.md` 的 `required_output` 写产出形态而非期望行为，`blockers_risks` 写客观风险而非禁令；专为 eval 造的、写着答案的示例脚本不进 lane 目录。宿主本来就该有的资产（文档站模板、standards、已有配置）**不算泄漏**——baseline 会不会主动去翻、翻到了会不会照做，本身就是要观测的行为差异。

零区分度先判成因，不得为制造区分度而伪造结果或弱化断言：

| 成因 | 动作 |
| --- | --- |
| prompt 或 fixture 规则泄漏 | 修 eval，按上表改成自然表述 |
| 规则天然存在于 skill 交付物（模板、脚手架本就承载字段与命名） | 不是缺陷。如实记录，观测重心移到门禁与纪律类断言 |
| 模型基线能力已覆盖该行为 | 记为 skill 生命周期信号交 issue 审查，不硬修 |

**Eval 产物策略**

- 提交 eval 定义、metadata、fixtures、README 与最新 `comparison.md`。不提交运行期产物：`with_skill/`、`without_skill/`、`baseline/`、`outputs/`、`comparison.auto.md`、`transcript.md`、`candidate-output.md`、`subagent-verdict.md`、`timing.json`、`run_status.json`、diagnostics 目录
- metadata 中的 `with_skill_outputs` / `without_skill_outputs` 只是 deterministic runner 的运行期产物预期，不要求存在于已提交 workspace。`with_skill_outputs` 可作 runner 门禁；baseline 类输出只报告，不作失败条件。无 deterministic 产物的 eval 不声明 runner output
- `eval_metadata.json` 不声明 `validation_method`；skill eval 默认执行 fresh subagent validation
- 模型 transcript、verdict、timing、diagnostics 可作短期 CI artifact 上传排查，但不入 git
- PR 评论或对话中的 eval 结论必须与已提交或拟提交的 `comparison.md` 一致
- Python eval 测试不得依赖上次运行的输出；用临时目录或最小 fixture，避免跨测试根目录重名模块。提交前运行 `uv run scripts/check_eval_artifacts.py`

**Eval 结果模型**

`comparison.md` 含 evaluation target、fixture version、latest result、with-skill 行为、`without_skill` baseline 的运行来源与行为摘要、failures、next steps、runtime artifact policy。

`Latest result` 分两维，结果区必须含一行 `Overall result: <PASS | PASS (partial coverage) | FAIL | BLOCKED>` 供 `scripts/summarize_eval_results.py` 解析：

| 维度 | 含义 | 取值 |
| --- | --- | --- |
| Behavior result | 本轮实际触发的路径上是否满足 assertions、有无回归 | `PASS` / `FAIL` |
| Coverage result | 本轮实际覆盖了多少 assertion 场景 | `FULL` / `PARTIAL`（取 `PARTIAL` 须列出未覆盖项及原因） |

组合规则：Behavior `FAIL` → `FAIL`；Behavior `PASS` + Coverage `FULL` → `PASS`；Behavior `PASS` + Coverage `PARTIAL` → `PASS (partial coverage)`。

依赖实时外部数据的 eval，若外部当时缺少特定实体（open milestone、eligible PR、breaking marker 等）导致 assertion 未触发，记 `NOT EXERCISED`，只计入 Coverage，不得计入 Behavior 的 `FAIL`。发版或 review 汇总引用结论时，必须能仅从两维区分 skill 回归与实时样本缺口。

Baseline 是 comparison 的对照输入，不是独立的机器判定对象。两维结果由 subagent、fresh judge 或人工 reviewer 基于 with_skill、without_skill、assertions 与上下文得出；deterministic contract checker 只校验 eval 定义、workspace、durable `comparison.md` 与产物策略，不根据 baseline 自由文本判断结果。

**校验与 CI**

- PR 必跑顺序：`repository-contract` → `eval-contract` → `doc-contract` → `python-tests`，即 `check_repository_contract.py` → `check_eval_contract.py` 与 `check_eval_artifacts.py` → `check_doc_contract.py` → 确定性 pytest
- 模型 eval 不作 required status check。涉及 skill 行为、routing、eval fixture 或发版前变更时，管理员应在合并前手动触发 eval workflow，把 transcript 与 subagent validation 结果一并作为 merge 依据

### 文档版本维护

**建议**

- 使用 feature-based 目录，例如 `docs/{agent}/{feature_path}/`
- 添加包含 version metadata 的 frontmatter
- 面向用户或开发者的发布变更记录写入 `docs/changelog/changelog-v{version}.md`
- 依赖 git history 追踪版本历史
- 修改文档时更新 `last_updated`

**避免**

- 不要创建基于日期的子目录
- 不要为 feature 文档创建多个版本化文件，例如 `PRD-v1.md` 和 `PRD-v2.md`

## 当前状态

**已实现 Agent（7 个）**

- `pm-agent` - 7 个 specialist skills
- `engineer-agent` - 6 个 specialist skills
- `qa-agent` - 4 个 specialist skills
- `devops-agent` - 4 个 specialist skills
- `designer-agent` - 2 个 specialist skills
- `security-agent` - 4 个 specialist skills
- `docs-agent` - 5 个 specialist skills

**Specialist skills 总数：** 32

**计划中的 Agent**

- `growth_ops`（P1）- analytics、funnel analysis、feedback synthesis
- `orchestrator`（P2）- request routing、project status summarization

## 重要文件

- `.claude-plugin/marketplace.json` - Agent 和 skill registry
- `scripts/install_codex_skills.py` - Codex 复制式 skill 安装脚本，避免祖先 plugin manifest 造成 namespace 前缀
- `skills-lock.json` - 已安装 skill metadata
- `AGENTS.md` - 仓库指导的唯一来源
- `CLAUDE.md` - 指向 `AGENTS.md` 的相对软链接，用于 Claude Code 兼容
- `agents/{agent}/README.md` - Agent 级文档
