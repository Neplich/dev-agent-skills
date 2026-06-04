---
feature: repository-ci-governance
version: 0.1.0-draft
date: 2026-05-06
last_updated: 2026-05-06
---

# Repository CI Governance Plan

## 目标

为 `dev-agent-skills` 仓库建立第一版 CI 门禁，用于支持从 `0.1.0`
开始的版本维护流程。

CI 的第一版目标是保护 `main`、skill 注册结构和基础测试，不把模型型
eval 一开始就放入 PR 硬门禁。

状态标记：

- `[x]` 已完成并落到仓库或 GitHub 配置。
- `[ ]` 未完成或仍需要单独实施。

## 当前已确认约束

- [x] `main` 已启用分支保护，后续变更默认通过 PR 合入。
- [x] 仓库限制性权限默认只授予唯一管理员，后续维护者或机器人再显式添加。
- [x] 合并方式默认只允许 squash merge。
- [x] tag 已通过 ruleset 保护，当前只允许 Admin bypass。
- [x] 版本 tag 从 `v0.1.0` 开始，统一使用 `v` 前缀 SemVer。
- [x] `AGENTS.md` 是仓库指导的唯一事实源。
- [x] `CLAUDE.md` 应保持为指向 `AGENTS.md` 的相对软链接。
- [x] Python 验证命令默认使用 `uv run`。
- [x] `docs/pm/` 当前是本地讨论文档位置，不作为第一版公开版本化文档入口。
- [x] eval 维护流程应只把评测任务、fixture 和最新评测比对结果提交到仓库，
  不提交 transcript、candidate output、verdict、timing、run status 等评测过程产物。

## Eval 维护流程

```text
新建/更新 skill
  → 使用已有测试集或更新后的测试集进行评测
  → 按固定格式编写最新评测比对结果
  → 删除评测过程文件
  → 提交 PR
```

该流程的目标是让仓库保持为 skill、测试集和最新结论的事实源，而不是模型
评测运行日志的归档目录。

## CI 启用前置任务

在把 CI 门禁加入 `main` required status checks 前，需要先完成以下整理：

1. [x] 明确 eval 产物分层
   - 应提交：`evals.json`、`eval_metadata.json`、fixture、必要的测试说明、
     最新评测比对结果。
   - 不应提交：`with_skill/outputs/`、`without_skill/outputs/`、
     `baseline/outputs/`、`transcript.md`、`candidate-output.md`、
     `subagent-verdict.md`、`timing.json`、`run_status.json` 等过程文件。

2. [x] 固定评测比对结果格式
   - 每个 eval workspace 保留一个最新结果文件，例如 `comparison.md`。
   - 结果文件应包含评测对象、测试集版本或 commit、执行入口、总体结论、
     with/without skill 对比、失败项和后续处理建议。
   - 结果文件只写结论和证据摘要，不内嵌完整 transcript 或模型长输出。

3. [x] 统一 eval runner 输出位置
   - runner 默认在临时目录或仓库外 scratch workspace 生成过程文件。
   - 如需在仓库内临时生成过程文件，runner 必须提供清理命令或自动清理。
   - runner 最终只同步固定格式的最新评测比对结果回 eval workspace。
   - 当前 runner 已统一使用 `tmp/eval-runs/...`，不再向 eval fixture 写入
     `comparison.auto.md`、transcript、verdict、diagnostics 或 run status。

4. [x] 整理现有历史过程产物
   - 先盘点当前已提交的 `outputs/`、`comparison.auto.md`、`timing.json`、
     `run_status.json` 等文件。
   - 将仍有价值的信息压缩进固定格式 `comparison.md`。
   - 删除不再需要保留的过程产物，再启用禁止过程产物入库的 CI 检查。

5. [x] 补充忽略规则和契约检查
   - 在 `.gitignore` 或等效检查中阻止常见过程产物再次入库。
   - `eval-contract` 应校验过程产物没有被提交。
   - `eval-contract` 只校验 metadata 中声明的输出配置格式，不要求输出文件存在。

6. [x] 扩展确定性 Python 测试
   - `python-tests` 覆盖所有 runner/parser/prompt/report 这类确定性单元测试。
   - Python 测试不得依赖上一次 eval 生成的过程文件。
   - Python 测试使用临时目录或最小 fixture 构造输入，避免污染仓库。

## 第一阶段：PR 必跑 CI

第一阶段 CI 用于作为 `main` required status checks。它只包含确定性、
低成本、可重复执行的检查。

### 1. [x] repository-contract

目的：确认仓库结构、注册文件和维护规则没有被破坏。

第一版命令：

```bash
uv run scripts/check_repository_contract.py
```

检查项：

- `CLAUDE.md` 必须是指向 `AGENTS.md` 的相对软链接。
- `.claude-plugin/marketplace.json` 必须是合法 JSON。
- `skills-lock.json` 必须是合法 JSON。
- marketplace 中注册的 agent 和 skill 路径必须存在。
- 每个注册 skill 必须存在 `SKILL.md`。
- 每个 `SKILL.md` 必须包含可解析的 YAML frontmatter。
- `SKILL.md` frontmatter 至少包含非空 `name` 和 `description`。
- `SKILL.md` 的 `name` 应与 skill 目录名一致。
- `name` 仅允许小写字母、数字和短横线。
- 禁止提交本地缓存或系统文件，例如 `.pytest_cache/`、`.DS_Store`。
- tracked 文件中不应再出现 `docs/superpowers/` 路径。

暂不检查：

- `description` 的业务质量。
- skill 版本号。
- frontmatter 的完整 schema。

### 2. [x] eval-contract

目的：校验 eval 定义、fixture 和元数据结构，不在 PR 中生成模型输出。

第一版命令：

```bash
uv run scripts/check_eval_contract.py
```

检查项：

- `evals.json` 必须是合法 JSON。
- 带 workspace 的 eval 必须提交对应 `eval_metadata.json` 和 durable `comparison.md`。
- `eval_metadata.json` 的 `eval_id` 必须匹配同一 skill 的 `evals.json`。
- metadata 中声明的 workspace、fixture、with/without skill、baseline 输出和 `execution_cleanup` 路径必须是 eval workspace 内的相对路径。
- `with_skill`、`without_skill`、baseline 输出配置格式必须保持完整，
  但不要求对应过程输出文件已提交。
- `execution_cleanup` 只能指向 eval workspace 内的相对路径。
- eval 断言字段必须存在，不能是空列表。
- 不应提交 eval 过程产物，例如 transcript、candidate output、verdict、
  timing、run status 和临时 outputs 目录。

暂不检查：

- 不运行 `codex exec`。
- 不刷新 transcript。
- 不用模型裁判判断 eval pass/fail。

### 3. [x] python-tests

目的：执行当前已有的确定性 Python 测试。

第一版命令：

```bash
uv run --with pytest pytest \
  agents/product_manager/test/idea-to-spec \
  agents/qa/test/test_qa_run_eval.py \
  agents/designer/test/test_designer_run_eval.py \
  agents/devops/test/test_devops_run_eval.py \
  agents/test_eval_contract.py
```

说明：

- 该测试不依赖模型调用，适合作为 PR 硬门禁。
- 后续如果新增稳定的单元测试，可继续并入该 job。

## 第二阶段：手动或定时 Eval

第二阶段用于质量回归，不作为第一版 PR 必跑门禁。

状态：

- [x] 已创建独立手动 workflow：`.github/workflows/evals.yml`。
- [x] 已支持 `workflow_dispatch` 手动触发，并可选择 `all`、`designer` 或 `qa`。
- [x] Designer eval 在 workflow 中作为 diagnostics 运行，运行期输出缺口以
  warning 和 artifact 形式呈现。
- [x] QA eval 保留模型执行路径，并要求仓库 secret `OPENAI_API_KEY`。
- [ ] 尚未启用 nightly 定时触发。

当前手动入口：

```bash
uv run agents/designer/test/run_all_evals.py
uv run agents/qa/test/run_all_evals.py
```

触发方式：

- [x] `workflow_dispatch` 手动触发。
- [ ] 后续可选 nightly 定时触发。
- [x] release 前由管理员手动执行。

原因：

- QA eval 当前会调用 `codex exec`。
- 模型输出、token、超时和运行环境会影响稳定性。
- 第一版不应让模型型 eval 阻塞普通 PR。

## 第三阶段：Release CI

第三阶段用于版本发布和 tag 流程。

状态：当前不实现 Release CI；发布前采用手动 release checklist。

触发方式：

- [ ] 不新增 release workflow。
- [ ] 不配置 tag push 自动发布。

检查项：

- [ ] 复用第一阶段全部 PR 必跑 CI。
- [ ] 校验 release tag 格式为 `vMAJOR.MINOR.PATCH`，预发布按 SemVer 后缀扩展。
- [ ] 确认 `docs/changelog/changelog-v{version}.md` 存在并记录对应版本变更。
- [ ] 根目录 `CHANGELOG.md` 只作为版本索引。
- [ ] 必要时手动触发 eval workflow 并记录结果。
- [ ] 必要时生成 `docs/release-notes/` 下的 release notes。

暂不实现：

- 自动发 GitHub Release。
- 自动上传 marketplace package。
- release bot bypass tag ruleset。

## 第一版 Workflow 建议

### [x] `.github/workflows/ci.yml`

触发：

- [x] pull request
- [x] push 到 `main`

jobs：

- [x] `repository-contract`
- [x] `eval-contract`
- [x] `python-tests`

- [x] 通过后再把这三个 job 加入 `main` required status checks。

### [x] `.github/workflows/evals.yml`

触发：

- [x] `workflow_dispatch`

jobs：

- [x] `designer-evals`
- [x] `qa-evals`

该 workflow 第一版只作为管理员手动质量检查。

## 待确认问题

- [ ] 是否需要第一版就新增 `CODEOWNERS`。
- [x] required status checks 拆成 3 个 job：`repository-contract`、`eval-contract`、`python-tests`。
- [ ] `description` 是否需要最小长度校验。
- [ ] 是否需要在第一版 CI 中校验 README 中的本地验证命令仍存在。
- [x] 已新增 `CHANGELOG.md` 索引和 `docs/changelog/changelog-v0.1.0.md`。
- [x] 当前不启用 release CI。
