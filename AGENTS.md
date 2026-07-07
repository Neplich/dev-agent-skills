# 仓库指导

本文件为在本项目中工作的 AI coding agents 提供仓库级指导。

## 仓库架构

本仓库是一个多 Agent skill marketplace，发布 6 个按角色划分的 Agent，覆盖产品、工程、QA、DevOps、设计和安全工作流。每个 Agent 包含多个遵循统一结构的 skill。目前主要面向 Claude Code 和 Codex 编写。

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

**市场注册**

- `.claude-plugin/marketplace.json` 定义所有 Agent 及其 skills
- `.claude-plugin/marketplace.json` 的 `metadata.version` 必须等于当前仓库 release 版本但不带 `v` 前缀；每次创建 release tag 前，先把该字段更新到目标版本，并确认存在对应 `docs/changelog/changelog-v{version}.md` 与根 `CHANGELOG.md` 索引
- `skills-lock.json` 保存已安装 skill 的元数据

### Agent 协作流

```text
PM Agent → Designer Agent → Engineer Agent → QA Agent → DevOps Agent → Security Agent
   ↓           ↓               ↓              ↓           ↓              ↓
  PRD      UI/UX Spec        TRD          Test Report  Deploy Config  Security Review
  BRD      Visual System   Code Changes                  CI/CD
```

**PM 唯一入口与下游 gate 指针**

- 用户侧新需求、变更、bug、测试、部署、安全、交付或仓库状态诉求默认先进入 `pm-agent` 分类；下游 role router 和 specialist 只在 PM handoff packet 或等效已确认文档链存在时承接。
- 用户未显式点名任何 skill 或 agent 时，默认进入 `pm-agent`；用户显式点名某个 skill 或 agent 时，这是受支持的直达路径，但仍必须经过对应入口 gate 的安全网。
- PM handoff packet 字段定义以 `agents/product_manager/skills/idea-to-spec/_internal/_shared/skill-map.md` 为权威；`AGENTS.md` 不复制字段清单。
- 下游安全网包含前置与收尾两面：缺少 PM handoff packet、等效已确认文档链或 specialist entry basis 时，温和引导用户经 `pm-agent` 补齐前置；完成当前事项后，主动建议协作链下一步并等待确认，用户已授权 `auto-continue` 时可连续推进直到链路结束或用户喊停。
- 跨角色收尾与 `auto-continue` 的权威定义在 `agents/product_manager/skills/idea-to-spec/_internal/_shared/skill-map.md` 的 `Safety-Net Closeout and Auto-Continue` 节；`AGENTS.md` 只保留入口契约和指针。
- SKILL.md frontmatter 的 `visibility: internal` 是声明层标记，Claude Code 与 Codex 都不消费该字段，不隐藏 slash 命令也不阻止显式直调；`pm-agent` 是默认入口，下游标记为 `internal` 仅表示非默认入口。
- 5 个 role router 只保留入口凭据检查和分流指针；具体执行 gate 的权威副本留在对应 specialist `SKILL.md`，例如 `feature-implementor` 的 PRD/TRD/plan/archive gate、`debugger` 的 expected-behavior gate、QA specialist 的 E2E gate，以及 Designer/DevOps/Security specialist 的 feature-scope gate。
- 直接调用下游且没有 PM handoff packet、等效已确认文档链或 specialist entry basis 时，不执行下游协议，应温和引导用户经 `pm-agent` 补齐前置并完成入口分类；唯一例外是用户直接请求 `project-bootstrap` 且明确要求跳过 PM 并立即 scaffold，此时可进入 `project-bootstrap` 的最小脚手架 override。

**文档依赖**

- Engineer 读取 `docs/pm/{feature_path}/` 和 `docs/design/{feature_path}/`
- QA 读取 `docs/pm/{feature_path}/` 和实现代码
- QA 在进行广泛项目探索前，先读取已有的 `docs/qa/e2e/{feature_path}/TEST_SUITE.md`、`FLOW_INDEX.md`、`cases/*.md` 和 `scripts/*.spec.md`
- DevOps 读取 `docs/engineer/{feature_path}/TRD.md`
- Designer 读取 `docs/pm/{feature_path}/PRD.md` 和 `docs/pm/{feature_path}/BRD.md`
- Security 读取 `docs/pm/{feature_path}/` 和代码库

**角色边界**

- Designer Agent 停在 `docs/design/{feature_path}/` 下的设计交付物，不实现代码
- Engineer Agent 在 PM 范围确认后负责 `docs/engineer/{feature_path}/TRD.md`
- Engineer Agent 负责把 PM 和 Designer 文档转成代码、测试和交付产物
- 读取 PM spec 或 design spec 不代表 Designer Agent 可以继续进入实现
- TRD 确认后，`feature-implementor` 负责产出 `docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md` 并按计划实现
- 新文档编写任务默认委派给 sub-agent，主进程保留上下文、审查结果并决定 handoff

## 开发工作流

> [!IMPORTANT]
> `AGENTS.md` 是仓库指导的唯一来源。`CLAUDE.md` 必须保持为指向 `AGENTS.md` 的相对软链接，不要单独编辑。

### 仓库治理

- Branch、tag、release、bypass 和仓库设置权限默认只授予唯一管理员；需要维护者或机器人时再显式添加。
- 维护变更不得直接在 `main` 上进行；开始修改前先创建工作分支，完成后通过 PR 合入。
- PR 创建后的更新默认追加新 commit 并普通 push；除非用户明确要求整理提交历史，否则不要 amend、rebase 或 force push。
- 创建 PR 后不要直接合并；必须等待维护者明确确认“可以合并”后再执行 merge / squash / rebase 合并操作。
- 当前仓库仍处于早期维护阶段，暂不新增 Release CI；发布前使用手动 release checklist：确认 `.claude-plugin/marketplace.json` 的 `metadata.version` 已更新为目标版本且不带 `v` 前缀，确认 `docs/changelog/changelog-v{version}.md` 存在并已被根 `CHANGELOG.md` 索引，tag 使用 `v` 前缀 SemVer，PR 必跑 CI 全部通过，必要时手动触发 eval workflow 并记录结果；每次使用 tag 发版时，按 skill 维度汇总 skill eval 后的 `comparison.md` 最新结论。不要自动创建 GitHub Release，不要自动上传 marketplace package，也不要配置 release bot bypass tag ruleset。

### 变更分级契约

本节是变更分级（`change_tier`）的唯一定义源。所有角色的门禁按 `change_tier` 取强度，不再各自默认最严；分级只调整门禁的形态和确认次数，不取消任何证据要求，`hotfix` 仍必须留下验证证据和结果记录。

| 等级 | 典型场景 | 判定信号 |
| --- | --- | --- |
| `hotfix` | 单文件轻量修复、typo、配置修正、已有失败测试的直接修复 | 不改变已批准 PRD/TRD 预期；变更可由一条验证命令覆盖 |
| `standard` | 常规功能实现、现有功能行为调整、多文件重构 | 有对应 `feature_path`；预期可能变化，需要 PRD/TRD 对齐 |
| `major` | 跨角色大功能、新增 agent/skill、契约面变更、发布 | 影响多个角色文档、marketplace 注册表或 contract 脚本 |

判定入口：PM 唯一入口（issue #52）落地前，由承接请求的 skill 按上表自判并在产出中记录 `change_tier`；#52 落地后由 `pm-agent` 在入口分类时判级，并把 `change_tier` 写入 handoff packet，fast lane 判定直接引用本契约的 `hotfix` 判定。判定信号不满足、预期可能变化或无法判级时，一律按 `standard` 处理；试图以 `hotfix` 名义跳过预期变更对齐的请求必须 blocked 或回 PM。

各门禁按等级取强度：

| 门禁 | `hotfix` | `standard` / `major` |
| --- | --- | --- |
| plan gate（`feature-implementor`） | 允许轻量计划形态：在现有活跃计划中追加 scope 条目或使用简化模板，具体形态由 TRD 阶段确定；仍需一次用户确认 | 维持完整 `IMPLEMENTATION_PLAN.md` 确认流程 |
| closeout / archive gate（archive gate 见 issue #54） | 合并 closeout 与归档为一次确认 | 维持独立审批 |
| QA E2E 门禁 | 只要求验证直接影响路径并追加结果 | 维持 PRD/TRD 预期对齐门禁 |
| PM entry gate（issue #52 落地后生效） | 与交付类请求（delivery / 状态查询）走 fast lane，分类后立即放行 | 新需求、预期变更、范围不清一律留在 PM |

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

每个 skill 应包含：

- `test/{skill-name}/evals/evals.json`，作为 eval case 定义
- `test/{skill-name}/workspace/...` 或 `test/{skill-name}/evals/workspace/...`，在 eval 需要 fixture 时作为 eval workspace
- 每个 eval 都必须有显式 workspace，并包含 `comparison.md`，作为使用 skill 与不使用 skill 的最新持久化对比结果

Skill eval 是 Agent skill 的可用性测试。它们必须验证 skill 能被触发、协议可执行，并能产出该角色预期的结构化产物。Eval 断言应检查 skill 特有行为，例如上下文读取、执行路径选择、证据处理、阻塞假设和 handoff 边界，而不是只检查泛化回答质量。

- 每次更新 skill 文档、内部指令或会影响 skill 行为的测试 fixture 后，必须主动询问是否运行对应 skill 的 eval；用户确认后默认执行模型 transcript 生成/检查和全新 Codex subagent validation，并按产物策略更新结果。Fresh Sub-Agent 门禁：每次通过 fresh Codex subagent validation 执行 skill eval 时，必须基于同一份 eval prompt 和 fixture 重新生成新的 `without_skill` baseline，不得复用历史 baseline；`without_skill` 运行结果作为 comparison 的 baseline 对照输入。只要实际执行了 skill eval 或 fresh Codex subagent validation，就必须在同一轮变更中更新对应 durable `comparison.md`；如果无法生成新的 baseline、没有可更新文件或不适用，必须写明 blocked 或不适用原因。若缺少 runner、凭据或外部服务导致 transcript 无法生成，必须明确记录 blocked 原因，不能静默降级成只读静态验证。

**Eval 定义契约**

- 所有 Agent skill eval 定义必须使用共享的 `evals.json` schema version `1.0`；不允许 Agent 专属 schema 例外
- 每个 `evals.json` 必须位于 `agents/{agent}/test/{skill-name}/evals/evals.json`，设置顶层 `schema_version`、`agent`、`skill_name` 和非空 `evals`，并保持 `skill_name` 与 `agents/{agent}/skills/{skill-name}/SKILL.md` 对齐
- 每个 eval item 必须包含字符串 `id`，格式为 `eval-NNN-short-slug`，并包含非空 `name`、`description`、`prompt`、`expected_output`、显式 `workspace`（值必须为 `workspace/...`）以及非空对象形式 assertions
- 每个 assertion 必须包含 lower snake_case `id`、非空 `description` 和非空语义化 `text`；不允许使用纯字符串 assertion
- 提交 eval 定义变更前运行 `uv run scripts/check_eval_contract.py`

**Eval 产物策略**

- 提交 eval 定义、metadata、fixtures、README 文件和最新 `comparison.md`；不要提交运行期产物，例如 `with_skill/`、`without_skill/`、`baseline/`、`iteration2/`、`outputs/`、`comparison.auto.md`、`transcript.md`、`candidate-output.md`、`subagent-verdict.md`、`timing.json`、`run_status.json` 或 diagnostics 目录
- `with_skill_outputs`、`without_skill_outputs` 和 baseline output metadata 只作为 deterministic runner 能真实生成或检查的运行期产物预期，不代表这些文件必须存在于已提交 workspace 中。`with_skill_outputs` 可作为 runner 门禁；`without_skill_outputs` 和 baseline output metadata 是 baseline 对照证据，只报告不作为 deterministic runner 失败条件。无 deterministic 产物的 eval 不要声明 runner output；长期提交的结果是 `comparison.md`；新的 metadata schema 应显式区分 runtime-output 字段和 durable-result 字段
- `eval_metadata.json` 不应声明 `validation_method`；skill eval 默认按当前流程执行 fresh subagent validation。`subagent-verdict.md` 只是 Codex 或 Claude Code subagent validation 的运行期诊断产物，不能提交，也不能写入 metadata output 字段作为 runner 必检产物
- eval runner 默认将运行期文件写入隔离的 scratch workspace，例如 `tmp/eval-runs/...`，再只把人工确认后的最新结果汇总回 `comparison.md`。模型 eval transcripts、verdicts、timing data 和 diagnostics 可作为短期 CI artifact 上传用于排查，但不要提交到 git
- PR 评论或对话中的 eval 结论必须与已提交或拟提交的 `comparison.md` 保持一致。
- `comparison.md` 应包含 evaluation target、test set 或 fixture version、latest result、with-skill behavior、without_skill baseline 的运行来源与行为摘要、failures、next steps 和 runtime artifact policy
- Baseline 的作用是为 comparison 提供不使用 skill 时的对照输入，不是独立的机器判定对象。`Latest result` 是 sub-agent、fresh judge 或人工 reviewer 基于 with-skill、without_skill、assertions 和上下文得出的结论；deterministic contract checker 只校验 eval 定义、workspace、durable `comparison.md` 和 runtime artifact 策略，不根据 baseline 自由文本判断 PASS、PARTIAL 或 BLOCKED。
- Python eval 测试不能依赖上一次 eval run 的运行期输出。使用临时目录或最小 fixtures，避免跨测试根目录出现重复测试模块名，确保 pytest 能在同一进程中收集它们；提交 eval 变更前运行 `uv run scripts/check_eval_artifacts.py`
- PR 必跑校验顺序是 `repository-contract -> eval-contract -> doc-contract -> python-tests`；先运行 `uv run scripts/check_repository_contract.py`，再运行 `uv run scripts/check_eval_contract.py` 和 `uv run scripts/check_eval_artifacts.py`，再运行 `uv run scripts/check_doc_contract.py`，最后运行确定性 pytest 命令
- 模型 eval 不作为 required status check；但只要实际执行 skill eval，默认应包含模型 transcript 生成/检查。涉及 skill 行为、routing、eval fixture 或 release 前变更时，管理员应在合并前手动触发 eval workflow，并把 transcript 结果和 subagent validation 结果一起作为 merge 判断依据

**Eval runner 约束**

- 最终 eval 验证必须由当前会话中的全新 Codex subagent 直接执行。Subagent 应读取 skill 文档、相关 Agent README、eval fixture workspace 和 `evals.json`，先在应用 skill 的条件下运行 `with_skill`，再在不读取或应用该 skill / Agent README 的条件下重新生成新的 `without_skill` baseline，并基于可用证据判断 skill 行为是否满足 eval assertions
- 不要把后台 CLI transcript 生成当作 eval pass/fail 的事实来源。CLI 生成的 transcripts 只能作为诊断产物保留，最终可用性判断必须来自 subagent validation
- Baseline outputs 是 comparison 证据输入。不要为了隐藏 transcript-generation 失败，把 eval 弱化成可选 `without_skill`，也不要复用历史 baseline 充当本次 Fresh Sub-Agent 结果；如果新的 `without_skill` baseline 没有成功生成或无法被 subagent 评审，应由 subagent 或 reviewer 在 `comparison.md` 中说明其对 `Latest result` 的影响。
- 旧 transcript 生成仍用于 comparison artifacts 时，优先使用结构化输出并提取最终结果字段，不要依赖纯文本 stdout
- 在隔离临时 workspace 中生成 transcripts，不要直接写入已提交的 eval fixture。历史输出或已生成 PM docs 可能污染 empty-workspace routing 等上下文敏感用例
- 对每次运行前必须从临时 workspace 删除的路径，使用 `eval_metadata.json` 中的 `execution_cleanup`，例如 stale `PRD.md`、`docs/pm/` 或 prior output folders
- 只有实际存在 deterministic runner 流程时才声明和持久化 run diagnostics，例如 command、cwd、timeout、return code 和 stdout length，便于区分基础设施失败和 assertion 失败
- 优先使用语义断言，避免脆弱的精确字符串检查。行为在语言或格式上可以合理变化时，例如本地化或等价的 PM-first lane labels，只要保持预期路由语义即可接受

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

**已实现 Agent（6 个）**

- `pm-agent` - 8 个 specialist skills
- `engineer-agent` - 7 个 specialist skills
- `qa-agent` - 4 个 specialist skills
- `devops-agent` - 4 个 specialist skills
- `designer-agent` - 2 个 specialist skills
- `security-agent` - 4 个 specialist skills

**Specialist skills 总数：** 29

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
