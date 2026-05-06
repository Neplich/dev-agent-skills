# 仓库指导

本文件为在本项目中工作的 AI coding agents 提供仓库级指导。

## 仓库架构

本仓库是一个多 Agent skill marketplace，发布 6 个按角色划分的 Agent，覆盖产品、工程、QA、DevOps、设计和安全工作流。每个 Agent 包含多个遵循统一结构的 skill。

### 核心概念

**Agent 结构**

- 每个 Agent 位于 `agents/{agent-name}/`
- 每个 Agent 包含 `README.md`、`skills/` 和 `test/`
- Agent 按角色组织，而不是按工具组织

**Skill 结构**

- `SKILL.md` 是公开 skill 文档
- `_internal/INSTRUCTIONS.md` 包含 Agent 的详细实现指导
- `_internal/modules/` 可包含可选支持模块
- Skill 使用 YAML frontmatter 保存元数据

**文档组织**

- 公开项目文档应遵循 `docs/{agent}/{feature-name}/`
- 文档 frontmatter 应包含 `feature`、`version`、`date` 和 `last_updated`
- 仓库级发布变更记录放在根目录 `CHANGELOG.md`；README 可以链接它，但不要重复维护 changelog 条目
- 版本历史通过 git 追踪，不要创建多个版本化文件
- QA feature 文档位于 `docs/qa/{feature-name}/`；`TEST_SPEC.md` 是测试套件索引，`test-cases/` 存放可复用用例，`FILE_EXPLORATION.md` 记录用于扩展覆盖范围的文件探索过程，`reports/` 存放 QA 执行产物

**市场注册**

- `.claude-plugin/marketplace.json` 定义所有 Agent 及其 skills
- `skills-lock.json` 保存已安装 skill 的元数据

### Agent 协作流

```text
PM Agent → Designer Agent → Engineer Agent → QA Agent → DevOps Agent → Security Agent
   ↓           ↓               ↓              ↓           ↓              ↓
  PRD      UI/UX Spec      Code Changes    Test Report  Deploy Config  Security Review
  BRD      Visual System                                  CI/CD
  TRD
```

**文档依赖**

- Engineer 读取 `docs/pm/{feature}/` 和 `docs/design/{feature}/`
- QA 读取 `docs/pm/{feature}/` 和实现代码
- QA 在进行广泛项目探索前，先读取已有的 `docs/qa/{feature}/TEST_SPEC.md` 和 `docs/qa/{feature}/test-cases/*.md`
- DevOps 读取 `docs/pm/{feature}/TRD.md`
- Designer 读取 `docs/pm/{feature}/PRD.md` 和 `docs/pm/{feature}/BRD.md`
- Security 读取 `docs/pm/{feature}/` 和代码库

**角色边界**

- Designer Agent 停在 `docs/design/{feature}/` 下的设计交付物，不实现代码
- Engineer Agent 负责把 PM 和 Designer 文档转成代码、测试和交付产物
- 读取 PM spec 或 design spec 不代表 Designer Agent 可以继续进入实现

## 开发工作流

> [!IMPORTANT]
> `AGENTS.md` 是仓库指导的唯一来源。`CLAUDE.md` 必须保持为指向 `AGENTS.md` 的相对软链接，不要单独编辑。

### 仓库治理

- Branch、tag、release、bypass 和仓库设置权限默认只授予唯一管理员；需要维护者或机器人时再显式添加。
- 维护变更不得直接在 `main` 上进行；开始修改前先创建工作分支，完成后通过 PR 合入。

### 新增 Agent

1. 创建目录结构：
   ```bash
   mkdir -p agents/{agent-name}/{skills,test}
   ```

2. 按现有 Agent 模式创建 `agents/{agent-name}/README.md`

3. 为每个 skill 创建：
   - `skills/{skill-name}/SKILL.md`
   - `skills/{skill-name}/_internal/INSTRUCTIONS.md`
   - `test/{skill-name}/evals/evals.json`

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

### QA 测试用例持久化

单独使用 QA 时，重新探索项目前必须先复用持久化测试用例记忆：

- 先读取 `docs/qa/{feature}/TEST_SPEC.md` 和 `docs/qa/{feature}/test-cases/*.md`
- 询问是否有新的 feature 变更，以及是否需要扩展项目文件探索来补充测试用例
- 如果需要探索，把已探索文件、发现和覆盖影响写入 `docs/qa/{feature}/FILE_EXPLORATION.md`
- 每个 E2E 测试用例单独存为 Markdown 文件，放在 `docs/qa/{feature}/test-cases/` 下，命名为 `TC-NNN-<short-slug>.md`
- 从这些用例文件执行 E2E 验证，只新增本次发现的用例，不要每次重新发现整个项目

### Skill 测试

每个 skill 应包含：

- `test/{skill-name}/evals/evals.json`，作为 eval case 定义
- `test/{skill-name}/workspace/...` 或 `test/{skill-name}/evals/workspace/...`，在 eval 需要 fixture 时作为 eval workspace
- 每个带 workspace 的 eval 中应有 `comparison.md`，作为使用 skill 与不使用 skill 的最新持久化对比结果

Skill eval 是 Agent skill 的可用性测试。它们必须验证 skill 能被触发、协议可执行，并能产出该角色预期的结构化产物。Eval 断言应检查 skill 特有行为，例如上下文读取、执行路径选择、证据处理、阻塞假设和 handoff 边界，而不是只检查泛化回答质量。

**Eval 定义契约**

- 所有 Agent skill eval 定义必须使用共享的 `evals.json` schema version `1.0`；不允许 Agent 专属 schema 例外
- 每个 `evals.json` 必须位于 `agents/{agent}/test/{skill-name}/evals/evals.json`，设置顶层 `schema_version`、`agent`、`skill_name` 和非空 `evals`，并保持 `skill_name` 与 `agents/{agent}/skills/{skill-name}/SKILL.md` 对齐
- 每个 eval item 必须包含字符串 `id`，格式为 `eval-NNN-short-slug`，并包含非空 `name`、`description`、`prompt`、`expected_output`、显式 `workspace`（值为 `workspace/...` 或 `null`）以及非空对象形式 assertions
- 每个 assertion 必须包含 lower snake_case `id`、非空 `description` 和非空语义化 `text`；不允许使用纯字符串 assertion
- 提交 eval 定义变更前运行 `uv run scripts/check_eval_contract.py`

**Eval 产物策略**

- 提交 eval 定义、metadata、fixtures、README 文件和最新 `comparison.md`；不要提交运行期产物，例如 `with_skill/`、`without_skill/`、`baseline/`、`iteration2/`、`outputs/`、`comparison.auto.md`、`transcript.md`、`candidate-output.md`、`subagent-verdict.md`、`timing.json`、`run_status.json` 或 diagnostics 目录
- `with_skill_outputs`、`without_skill_outputs` 和 baseline output metadata 只作为 runner 的运行期预期，不代表这些文件必须存在于已提交 workspace 中。长期提交的结果是 `comparison.md`；新的 metadata schema 应显式区分 runtime-output 字段和 durable-result 字段
- 现有 eval runner 在本地运行时可能会在 eval fixture 下生成运行期文件；这些文件只是临时文件，提交前必须删除，并由 `uv run scripts/check_eval_artifacts.py` 阻断。新的 eval runner 应优先使用隔离的临时目录或 scratch workspace，例如系统临时目录或 `tmp/eval-runs/...`，再只把最新结果汇总回 `comparison.md`。模型 eval transcripts、verdicts、timing data 和 diagnostics 可作为短期 CI artifact 上传用于排查，但不要提交到 git
- `comparison.md` 应包含 evaluation target、test set 或 fixture version、latest result、with-skill behavior、without-skill 或 baseline behavior、failures、next steps 和 runtime artifact policy
- Python eval 测试不能依赖上一次 eval run 的运行期输出。使用临时目录或最小 fixtures，避免跨测试根目录出现重复测试模块名，确保 pytest 能在同一进程中收集它们；提交 eval 变更前运行 `uv run scripts/check_eval_artifacts.py`
- PR 必跑校验顺序是 `repository-contract -> eval-contract -> python-tests`；先运行 `uv run scripts/check_repository_contract.py`，再运行 `uv run scripts/check_eval_contract.py` 和 `uv run scripts/check_eval_artifacts.py`，最后运行确定性 pytest 命令

**Eval runner 约束**

- 最终 eval 验证必须由当前会话中的全新 Codex subagent 直接执行。Subagent 应读取 skill 文档、相关 Agent README、eval fixture workspace 和 `evals.json`，再判断 skill 行为是否满足 eval assertions
- 不要把后台 CLI transcript 生成当作 eval pass/fail 的事实来源。CLI 生成的 transcripts 只能作为诊断产物保留，最终可用性判断必须来自 subagent validation
- Baseline outputs 仍然必需。不要为了隐藏 transcript-generation 失败，把 eval 弱化成可选 `without_skill`
- 旧 transcript 生成仍用于 comparison artifacts 时，优先使用结构化输出并提取最终结果字段，不要依赖纯文本 stdout
- 在隔离临时 workspace 中生成 transcripts，不要直接写入已提交的 eval fixture。历史输出或已生成 PM docs 可能污染 empty-workspace routing 等上下文敏感用例
- 对每次运行前必须从临时 workspace 删除的路径，使用 `eval_metadata.json` 中的 `execution_cleanup`，例如 stale `PRD.md`、`docs/pm/` 或 prior output folders
- 持久化 run diagnostics，例如 command、cwd、timeout、return code 和 stdout length，便于区分基础设施失败和 assertion 失败
- 优先使用语义断言，避免脆弱的精确字符串检查。行为在语言或格式上可以合理变化时，例如本地化或等价的 PM-first lane labels，只要保持预期路由语义即可接受

### 文档版本维护

**建议**

- 使用 feature-based 目录，例如 `docs/{agent}/{feature-name}/`
- 添加包含 version metadata 的 frontmatter
- 面向用户或开发者的发布变更记录写入根目录 `CHANGELOG.md`
- 依赖 git history 追踪版本历史
- 修改文档时更新 `last_updated`

**避免**

- 不要创建基于日期的子目录
- 不要创建多个版本化文件，例如 `PRD-v1.md` 和 `PRD-v2.md`

## 当前状态

**已实现 Agent（6 个）**

- `pm-agent` - 7 个 specialist skills
- `engineer-agent` - 6 个 specialist skills
- `qa-agent` - 4 个 specialist skills
- `devops-agent` - 4 个 specialist skills
- `designer-agent` - 2 个 specialist skills
- `security-agent` - 4 个 specialist skills

**Specialist skills 总数：** 27

**计划中的 Agent**

- `growth_ops`（P1）- analytics、funnel analysis、feedback synthesis
- `orchestrator`（P2）- request routing、project status summarization

## 重要文件

- `.claude-plugin/marketplace.json` - Agent 和 skill registry
- `skills-lock.json` - 已安装 skill metadata
- `AGENTS.md` - 仓库指导的唯一来源
- `CLAUDE.md` - 指向 `AGENTS.md` 的相对软链接，用于 Claude Code 兼容
- `agents/{agent}/README.md` - Agent 级文档
