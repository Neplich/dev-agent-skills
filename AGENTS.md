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

- 公开项目文档遵循 `docs/{agent}/{feature_path}/`，`feature_path` 可包含多级 lower kebab-case 路径段；不创建基于日期的子目录，也不为同一文档创建多个版本化文件（如 `PRD-v1.md`），版本历史通过 git 追踪
- 文档 frontmatter 包含 `feature`、`version`、`date` 和 `last_updated`；修改文档时更新 `last_updated`
- 仓库级发布变更记录按版本归档到 `docs/changelog/changelog-v{version}.md`；根目录 `CHANGELOG.md` 只作为索引，不重复维护 changelog 条目
- 窄例外（仅限实施计划归档）：`feature-implementor` 的完成态或废弃态实施计划经 closeout 和用户/维护者审批后，可归档到 `docs/engineer/{feature_path}/implementation-plans/archive/IMPLEMENTATION_PLAN-<scope>.md`，`<scope>` 使用 lower kebab-case 描述该次实现范围；当前活跃计划入口仍固定为 `docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md`。该例外只覆盖实施计划归档，不适用于 PRD、TRD 或其他文档类型
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

- 用户侧新需求、变更、bug、测试、部署、安全、交付或仓库状态诉求默认先进入 `pm-agent` 分类；用户未显式点名任何 skill 或 agent 时同样默认进入 `pm-agent`，显式点名是受支持的直达路径，但仍必须经过对应入口 gate 的安全网。下游 role router 和 specialist 只在 PM handoff packet 或等效已确认文档链存在时承接。
- 下游安全网包含前置与收尾两面：缺少 PM handoff packet、等效已确认文档链或 specialist entry basis 时，不执行下游协议，温和引导用户经 `pm-agent` 补齐前置并完成入口分类（脚手架请求同样走正常 PM 分类）；完成当前事项后，主动建议协作链下一步并等待确认，用户已授权 `auto-continue` 时可连续推进直到链路结束或用户喊停。
- SKILL.md frontmatter 的 `visibility: internal` 是声明层标记，Claude Code 与 Codex 都不消费该字段，不隐藏 slash 命令也不阻止显式直调；`pm-agent` 是默认入口，下游标记为 `internal` 仅表示非默认入口。
- 6 个 role router 只保留入口凭据检查和分流指针，其中 `docs-agent` 分流正式文档站点 bootstrap、API/database/design/ops/product 当前事实 sync、基于运行界面截图的图文用户操作手册、站内 Release Notes 和 audit；PM `github-release-gen` 按 SKILL.md 的宿主文档站适用性判断生成 GitHub Release：有文档站宿主要求站内 Release Notes 已确认且 docs-audit 门禁通过；无文档站宿主降级为维护者确认的版本事实源与维护者显式批准；具体执行 gate 的权威副本留在对应 specialist `SKILL.md`，例如 `feature-implementor` 的 PRD/TRD/plan/archive gate、`debugger` 的 expected-behavior gate、QA specialist 的 E2E gate，以及 Designer/DevOps/Security/Docs specialist 的 feature-scope gate。

**文档依赖**

- 下游协议的权威定义统一放在 `agents/product_manager/skills/idea-to-spec/_internal/_shared/`：6 个现有 Agent 按 `consumption-contract.md` 消费宿主正式文档；`skill-map.md` 定义 PM handoff packet 字段、跨角色收尾与 `auto-continue`（`Safety-Net Closeout and Auto-Continue` 节）以及 Security 结论升级（`Security Conclusion Escalation to PM` 节）。`AGENTS.md` 不复制字段清单，只保留入口契约和指针。
- Security 的确认结论（审查发现，或对整改已落地的复审确认）改变正式文档事实、对外行为、运维事实或发版就绪状态时，按 `skill-map.md` 的 `Security Conclusion Escalation to PM` 规则把结论与证据回交 `pm-agent` 分类并提 issue；后续 Docs / Engineer / 发版工作由 `pm-agent` 通过正常 handoff packet 分派，各 specialist 按既有门禁执行
- Docs Agent 读取 `docs/pm/{feature_path}/`、`docs/engineer/{feature_path}/TRD.md` 与代码证据
- Engineer 读取 `docs/pm/{feature_path}/` 和 `docs/design/{feature_path}/`
- QA 读取 `docs/pm/{feature_path}/` 和实现代码
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
- 当前仓库仍处于早期维护阶段，暂不新增 Release CI；发布前使用手动 release checklist：按「市场注册」节的版本规则核对 `metadata.version` 与 `.kimi-plugin/plugin.json` 的 `version`，确认对应 `docs/changelog/changelog-v{version}.md` 存在并被根 `CHANGELOG.md` 索引，tag 使用 `v` 前缀 SemVer，PR 必跑 CI 全部通过，必要时手动触发 eval workflow 并记录结果；每次使用 tag 发版时，按 skill 维度汇总 skill eval 后的 `comparison.md` 最新结论。每次 tag 发版后，由 `pm-agent → github-release-gen` 使用 skill 流程自动创建 GitHub Release draft，并直接交维护者审批；draft 的发布（publish）仍必须等待维护者显式批准。不要自动上传 marketplace package，也不要配置 release bot bypass tag ruleset。

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

3. 为每个 skill 创建 `skills/{skill-name}/SKILL.md`；除项目级 `skill-eval-runner` 登记的 manual-only 例外外，同时创建 `test/{skill-name}/evals/evals.json`，仅在需要渐进加载时创建 `skills/{skill-name}/_internal/`

4. 在 `.claude-plugin/marketplace.json` 注册 Agent：
   ```json
   {
     "name": "{agent-name}-agent",
     "description": "...",
     "skills": ["./agents/{agent-name}/skills/{skill-name}"]
   }
   ```
   随后用新 skill 元数据更新 `skills-lock.json`

5. 为可常规评测的 skill 添加 eval 并对比使用与不使用 skill 的结果；manual-only skill 按项目级 `skill-eval-runner` 记录真实使用反馈与当前结论，再按下节「新增或重命名 Skill 的同步面」逐面核对遗漏项

### 新增或重命名 Skill 的同步面

向既有 Agent 增加一个 specialist 时，改动会扇出到注册、路由、发现、Agent 文档、顶层入口、eval 和过程文档多个面。任一面漏改都不会被契约脚本拦住，但会让 skill 在实际使用中不可达或不可信。按下表逐项核对，不要只改「主要」文件。

| 面 | 必改项 |
| --- | --- |
| 注册 | `.claude-plugin/marketplace.json` 的 `skills` 数组；`skills-lock.json` 条目与 `computedHash` |
| 路由 | router `SKILL.md` 的 Available Skills、Routing Signals、Specialist Gate Pointers、Role Boundary 中列举 specialist 的那句 |
| **发现** | `.claude-plugin/marketplace.json` 的 agent `description`；router `SKILL.md` 的 frontmatter `description`；`AGENTS.md` 中描述该 router 分流范围的根路由指针句 |
| Agent 文档 | `agents/{agent}/README.md` 的 skills 表、计数与 **Routing Rules 小节**；`README_zh.md` 同步 |
| 顶层入口 | 根 `README.md` / `README_zh.md` 的 Agent 表计数与能力描述；**`pm-agent/SKILL.md` 的 handoff targets、请求分类行与 Default Routes** |
| eval | 新 skill 自己的 evals；**router 的路由 eval**；被本次改动影响的既有 skill 的断言与其 durable `comparison.md` |
| 过程文档 | PRD/TRD/实施计划的触点表与禁止区必须与实际 diff 一致；父 PRD 的 `child_features` 与其中描述注册面的行 |

加粗项是最容易漏的：

- **发现层**决定客户端在读正文之前是否会选中这个 skill。计数和正文改全了、描述没改，等于新能力在元数据层不存在。
- **router 路由 eval** 缺失时，路由分支写错也能全绿通过。
- **PM 入口分类**：`pm-agent` 是默认用户入口，用户不点名 skill 时全部经它分类。下游 router 认识新 specialist，但 PM 的分类词典里没有对应说法时，该能力对普通用户不可达。
- **既有 skill 的 eval 与 comparison**：改动若影响断言依赖的契约，必须通过项目级 `skill-eval-runner` 识别受影响范围并处理 fresh 证据；不得沿用或手工伪造旧结论。
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
- 先读取「文档组织」节列出的 `docs/qa/e2e/{feature_path}/` 下索引、用例、脚本与历史结果（`TEST_SUITE.md`、`FLOW_INDEX.md`、`cases/*.md`、`scripts/*.spec.md`、`results/`、`_reports/`）
- 基于 PRD/TRD 生成 E2E 测试时，直接按 `docs/qa/e2e/{feature_path}/` 分类和记录，不再新增 `docs/qa/{feature}` 入口
- 每个 E2E 测试用例单独存为 Markdown 文件，放在功能目录的 `cases/` 下，命名为 `TC-NNN-<short-slug>.md`；对应流程脚本放在 `scripts/TC-NNN-<short-slug>.spec.md`
- `scripts/*.spec.md` 可以保存可执行脚本片段以保证重复执行一致，但不得包含明文账号、密码、token、cookie、session、SSH 密码或 SSH key 内容
- 多个 TC 复用 `docs/qa/e2e/_shared/login-flows/` 下的登录方式；测试账号只引用账号 ID
- 平台账号和 SSH 账号统一存放在本地 `.qa/e2e/accounts.local.json`，该文件必须被 `.gitignore` 屏蔽；账号落盘格式遵循 `agents/qa/skills/qa-agent/references/e2e-credential-store.md`
- 执行入口优先级为 repo harness > Chrome plugin / browser connector > Playwright fallback；repo harness 存在且覆盖当前 TC 时必须优先使用
- 单个 E2E 测试任务默认由 subagent 执行，主 agent 负责范围确认、拆分、结果确认和按 `agents/qa/skills/qa-agent/references/e2e-test-report.md` 生成汇总报告
- 现有功能变更或 bug 修复触发 E2E 文档更新前，必须先完成 PRD/TRD 预期对齐；预期变化回 PM，TRD gap 回 `trd-gen`，文档缺失或预期不清时 blocked；门禁强度按「变更分级契约」的 `change_tier` 取值
- 代码完成后的 E2E 文档补充必须引用已确认的 `docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md`；任何等级都不能跳过实施计划门禁（`hotfix` 轻量形态按「变更分级契约」）
- 已有 E2E 测试基于功能更新增量更新，历史结果只追加不覆盖

### Skill 测试

本仓库 skill eval 的设计、编写、静态校验、fresh paired 执行、并发、judge、
durable `comparison.md`、运行期清理与失败分诊，统一由项目级
`.agents/skills/skill-eval-runner/SKILL.md` 负责。任何创建、修改、运行、重跑、
汇总或诊断 eval 的任务都必须使用该 skill；具体字段约束以
`scripts/check_eval_contract.py`，具体执行语义以 `scripts/run_skill_eval.py` 与
`scripts/eval_runtime.py` 为准。`AGENTS.md` 不再复制第二份 eval 流程。

## 重要文件

- `.claude-plugin/marketplace.json` - Agent 和 skill registry
- `scripts/install_codex_skills.py` - Codex 复制式 skill 安装脚本，避免祖先 plugin manifest 造成 namespace 前缀
- `skills-lock.json` - 已安装 skill metadata
- `AGENTS.md` - 通用仓库指导的唯一来源；专项 eval 工作流只保留上方项目 skill 指针
- `agents/{agent}/README.md` - Agent 级文档
