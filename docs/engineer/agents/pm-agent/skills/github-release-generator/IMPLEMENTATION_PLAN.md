---
title: "PM Release skill 收敛为 github-release-generator（issue #120）实施计划"
type: IMPLEMENTATION_PLAN
feature: "skill-github-release-generator"
feature_path: "agents/pm-agent/skills/github-release-generator"
parent_feature: "agents/pm-agent/skills"
feature_level: "4"
version: "1.2.0"
status: Implemented
author: "Neplich Codex"
date: "2026-07-20"
last_updated: "2026-07-20"
generated_by: "feature-implementor"
implementation_scope: "issue-120-g1-g2-github-release-generator"
related_prd: "docs/pm/agents/pm-agent/skills/github-release-generator/PRD.md"
related_trd: "docs/engineer/agents/pm-agent/skills/github-release-generator/TRD.md"
related_issues:
  - "https://github.com/Neplich/dev-agent-skills/issues/120"
---

# PM Release skill 收敛为 github-release-generator（issue #120）实施计划

## 1. 计划状态与授权

本计划覆盖 issue #120 的 G1 收敛与 G2 eval/交付，`change_tier: major`。用户已明确授权
skill 更名、注册迁移、computedHash 校验、eval 语义重写、fresh paired validation、全面
自查、commit、push、创建 PR 和等待 CI，无需再次请求计划确认。

授权不包含 merge、amend、rebase、force push、`--admin`、tag 操作、GitHub Release 真实
发布、镜像/Helm/部署或等待 PR review。

## 2. 成功标准

1. PM 旧 `release-notes-generator` 目录原地迁移为 `github-release-generator`，旧目录消失。
2. 新 skill 实现 #116 ready handoff、#117 双态、预览/draft/publish/readback 门禁。
3. PM router 与共享 skill map 正确拆分站内 Release Notes 和 GitHub Release 路由。
4. marketplace、skills lock、安装器测试、README/AGENTS 和 PM eval 路径全部一致。
5. specialist 总数不变，Docs `release-notes-generator` 职责不变。
6. 4 个 specialist eval 与受影响 router eval 完成 fresh with/without 和独立 judge，durable comparison 全部 PASS。
7. 四项 checker 与 CI 同款 pytest 全部通过。
8. 生成指定中文 commit、push 并创建 PR；CI 全绿后切回 `main`，不等待 review、不 merge。

## 3. 精确文件清单

### 3.1 文档链

| 文件 | 操作 | 内容 |
| --- | --- | --- |
| `docs/pm/agents/pm-agent/skills/github-release-generator/PRD.md` | 新增 | issue #120 产品范围、门禁、边界与验收 |
| `docs/engineer/agents/pm-agent/skills/github-release-generator/TRD.md` | 新增 | 文件级设计、#116/#117 handoff、安装迁移与验证 |
| `docs/engineer/agents/pm-agent/skills/github-release-generator/IMPLEMENTATION_PLAN.md` | 新增并完成 | G1/G2 文件、顺序、验证、禁止项和 closeout |

### 3.2 Skill 与 eval

| 文件或目录 | 操作 | 内容 |
| --- | --- | --- |
| `agents/product_manager/skills/release-notes-generator/` | 删除/迁移 | 删除 PM 旧目录，不保留旧名 shim |
| `agents/product_manager/skills/github-release-generator/SKILL.md` | 新路径重写 | 入口、时序、职责、mutation 和边界门禁 |
| `agents/product_manager/skills/github-release-generator/reference/github-release-workflow.md` | 迁移并修改 | 只描述 preview/draft/publish/readback；删除 tag owner 与站内职责 |
| `agents/product_manager/skills/github-release-generator/reference/release-outline.md` | 迁移并修改 | 以已确认站内正文为事实基线，补 GitHub 追溯格式 |
| `agents/product_manager/test/release-notes-generator/` | 删除/迁移 | 移除旧 PM eval 路径 |
| `agents/product_manager/test/github-release-generator/evals/evals.json` | 迁移并重写 | 4 个用例覆盖 handoff 阻塞、双时序门禁、事实追溯与零写入，保持 schema `1.0` |
| `agents/product_manager/test/github-release-generator/evals/workspace/**` | 重建 | AI Hub-shaped fixture、`execution_cleanup` 与 fresh PASS durable comparison |
| `agents/product_manager/test/pm-agent/evals/**` | 增量更新 | 新增站内 Release Notes 与 GitHub Release 双路由用例并完成 fresh validation |

若旧目录中存在上述未列出的合法 reference 或 eval fixture 文件，按同目录整体迁移并只做
名称/路径/checker 所需的最小修改，不删除有效资产。

### 3.3 路由、注册与文案

| 文件 | 操作 | 内容 |
| --- | --- | --- |
| `agents/product_manager/skills/pm-agent/SKILL.md` | 修改 | 可用 skill、route matrix、signals、chains 改为 GitHub/Docs 双路由 |
| `agents/product_manager/skills/idea-to-spec/_internal/_shared/skill-map.md` | 修改 | 更新 `release_notes` 分类、handoff 和 closeout owner |
| `.claude-plugin/marketplace.json` | 修改 | PM skills 数组旧名替换为新名；Docs 数组不动 |
| `README.md` | 修改 | 英文能力表、路由和协作说明更新 |
| `README_zh.md` | 修改 | 中文能力表、路由和协作说明更新 |
| `agents/product_manager/README.md` | 修改 | PM skill 名、职责和典型流程更新 |
| `AGENTS.md` | 修改 | 描述性更新；7 Agents / 33 specialists 总数不变 |

### 3.4 安装、lock 与测试

| 文件 | 操作 | 内容 |
| --- | --- | --- |
| `skills-lock.json` | 修改 | 删除 `pm-release-notes-generator` 和遗留 PM 旧记录；新增 `github-release-generator`；Docs 恢复朴素 `release-notes-generator` |
| `scripts/install_codex_skills.py` | 复核/必要最小修改 | 保留通用同名限定机制；确保唯一名称朴素安装，无具体 skill hardcode |
| `scripts/test_install_codex_skills.py` | 修改 | 更新本仓库真实安装断言，并保留合成同名冲突回归 |

### 3.5 computedHash

刷新所有实际受影响 skill 的 lock hash，至少覆盖：

- `pm-agent`；
- `github-release-generator`；
- Docs `release-notes-generator`；
- 因共享 `skill-map.md` 被 hash 输入覆盖而变化的关联 skill。

以 repository checker 报告为准补齐，不手工忽略 stale hash。

## 4. 实施顺序

```mermaid
flowchart TD
    A["确认分支与工作树"] --> B["建立 PRD/TRD/计划"]
    B --> C["迁移并收敛 PM skill"]
    C --> D["迁移并重写 PM eval"]
    D --> E["更新 router 与 skill-map"]
    E --> F["更新 marketplace/lock/README/AGENTS"]
    F --> G["更新安装器回归"]
    G --> H["刷新 computedHash"]
    H --> I["四项 checker + pytest"]
    I --> J["范围审查、commit、PR 与 CI"]
```

### Step 1：分支与基线

- 从最新 `main` 创建并停留在 `feat/120-github-release-generator`。
- 记录初始 `git status --short --branch`，保留所有范围外用户改动。
- 复核 issue #120、#116/#117 契约和旧 PM skill/eval 当前文件集合。

验证：当前分支名正确；没有覆盖并行或用户已有改动。

### Step 2：建立确认文档链

- 写入本计划 §3.1 三个文件。
- frontmatter 使用 `feature_path: agents/pm-agent/skills/github-release-generator`、
  `parent_feature: agents/pm-agent/skills`、`feature_level: "4"`、`status: Approved`、
  日期 `2026-07-20` 和 issue #120 URL。

验证：`uv run scripts/check_doc_contract.py` 可读取三文件且层级一致。

### Step 3：迁移并收敛 PM skill

- 用 Git 可追踪的目录迁移保留历史，再重写 `SKILL.md` 和 references。
- 入口先验证 #116 ready handoff，再验证版本/compare，再消费 #117 `ready_for_tag`。
- preview 永远先于写 draft；draft 写入只响应本次明确请求并回读。
- publish 要求实际 tag、`release_verified` 与另行明确批准，并在发布后回读。
- 删除创建/移动 tag、生成站内页面、运行 docs check、镜像/Helm/部署等旧越界行为。

验证：旧 PM skill 目录不存在；新 `SKILL.md` 同时含四类门禁和边界禁令。

### Step 4：迁移并重写 eval

- 删除旧 PM Release Notes 语义用例，建立 4 个 issue #120 specialist 用例。
- 用 AI Hub-shaped fixture 覆盖 #116 ready handoff、#117 双态、事实一致、GitHub 追溯、
  `docs/site/`/tag 零写入及 missing-tag 下禁止 `gh release create`。
- 新增 pm-agent 双路由 eval，区分 `docs-agent:release-notes-generator` 与 PM
  `github-release-generator`。
- 每个用例先生成 fresh with-skill，再用同一 prompt/fixture 生成全新 without-skill，最后
  由独立 judge 逐 assertion 判定；runtime 只保留在 `tmp/eval-runs/120*`。

验证：5/5 eval、21/21 assertions PASS；`check_eval_contract.py` 与
`check_eval_artifacts.py` 通过，无 runtime artifact 被提交。

### Step 5：更新路由和共享指针

- PM `release_notes`/沟通类请求拆分：站内或用户侧版本说明经 PM handoff 到
  `docs-agent:release-notes-generator`；GitHub Release 到 `github-release-generator`。
- 更新 Available Skills、route matrix、routing signals、dispatch table、multi-skill chain 和
  closeout 指针中的 PM 旧名。
- 不改变 Docs specialist gate 权威副本或 docs-audit 双态定义。

验证：全仓逐条审查旧名命中；PM GitHub owner 不再指向旧 skill。

### Step 6：更新注册、安装和仓库说明

- marketplace PM 数组替换目录；Docs 数组保持原样。
- lock 按朴素安装名迁移两条记录并刷新 hash。
- 安装器算法保留；测试断言真实仓库现在安装 `github-release-generator` 与
  `release-notes-generator`，合成 collision 用例仍覆盖限定名。
- 根 README 中英、PM README、AGENTS 只做本次职责和名称的描述性更新。

验证：marketplace specialist 数量不变；安装器测试不依赖本例同名 hardcode。

### Step 7：验证与修复

严格按 §5 命令顺序运行。失败时只修复与本次变更直接相关的契约、路径、hash 或测试
期望，不顺手重构邻接代码。

### Step 8：范围审查与 PR 交付

- 执行 `git diff --check`、`git status --short`、`git diff --stat`。
- 确认无 `docs/site/`、tag、部署资产和范围外改动。
- 使用 `git commit -F <message-file>`，G1 与 G2 分别保留指定中文 commit。
- push 功能分支并创建标题为 `feat: PM Release skill 收敛为 github-release-generator` 的 PR。
- PR 正文记录 G1/G2、自查、eval 表、边界和 issue 关联；另以 PR 评论提交自查 findings。
- `gh pr checks --watch` 确认 CI 全绿后切回 `main`，不等待 review、不 merge。

验证：记录 G2 commit、PR URL 与 CI 结果；本地最终分支为 `main`。

## 5. 验证命令

```bash
uv run scripts/check_repository_contract.py
uv run scripts/check_eval_contract.py
uv run scripts/check_eval_artifacts.py
uv run scripts/check_doc_contract.py
uv run --with pytest pytest \
  agents/product_manager/test/idea-to-spec \
  agents/product_manager/test/pm-agent \
  agents/qa/test/test_qa_run_eval.py \
  agents/designer/test/test_designer_run_eval.py \
  agents/devops/test/test_devops_run_eval.py \
  agents/docs/test/test_docs_run_eval.py \
  agents/test_doc_contract.py \
  agents/test_eval_contract.py \
  scripts/test_install_codex_skills.py
git diff --check
```

若 checker 或 CI 测试清单在最新 `main` 已更新，以仓库当前 required workflow/文档记录
的同款显式 pytest 清单为准，报告实际命令与结果。

## 6. 禁止项

- 不 merge，不 amend/rebase/force push，不使用 `--admin`。
- 不创建、移动、删除或重打 tag，不发布真实 GitHub Release。
- 不生成或修改站内 Release Notes，不改 `docs/site/`。
- 不改变 Docs `release-notes-generator` 的职责或 `docs-audit` 权威协议。
- 不运行或替代宿主文档站 `test:docs`。
- 不发布镜像、不更新 Helm、不执行部署。
- 不复用历史 baseline；fresh validation 运行期产物不提交。
- 不清理与本任务无关的代码、文档、测试或用户改动。

## 7. Closeout

完成后输出一次简洁报告，必须包含：

- 目录迁移、注册、lock、安装、router/skill-map 和 README/AGENTS 变更清单；
- #116 入口门禁、#117 pre-tag/draft/publish 三重门禁及回读验证落点；
- 四项 checker、CI 同款 pytest 和 `git diff --check` 的实际结果；
- G1/G2 commit、PR URL、CI 状态和最终 `main` 分支；
- 明确说明未等待 review、未 merge、未执行 tag/Release/部署操作。

本轮 closeout 以 PR required checks 全绿并切回 `main` 为终点，不等待外部 review。

## 8. 实施结果

| 项目 | 结果 |
| --- | --- |
| 文档链 | PRD、TRD 与本 `IMPLEMENTATION_PLAN` 已完成；计划状态为 `Implemented`，层级、日期和 issue #120 关联通过文档契约检查。 |
| Skill 收敛 | PM 旧目录已迁移为 `github-release-generator`；#116 入口、#117 双态、事实一致性、preview/draft/publish/readback 与全部边界已落地。 |
| Draft 安全边界 | `ready_for_tag` 后可生成完整 draft 预览；无现有 draft 且无实际 tag 时不调用 GitHub create；新建远端 draft 强制绑定已存在 tag，更新已有 draft 强制验证远端 tag 零变化。 |
| 路由与注册 | PM router、共享 skill map、marketplace、README/AGENTS 和当前态文档指针已拆清 Docs 站内说明与 PM GitHub Release；specialist 总数不变。 |
| 安装与 lock | 安装器通用同名限定机制保持不变；真实仓库恢复两个朴素名；lock key/source 与受影响 computedHash 已同步。 |
| Eval | 4 个 specialist eval 与 1 个 router eval 已完成语义重写；fresh with/without 与独立 judge 结论为 5/5 PASS、21/21 assertions PASS。 |
| 独立验收 | eval-001 的最小页面/source evidence 建议已修复并完成 R2 重验；无剩余 blocking 或非阻塞 fixture finding。 |

实际验证结果：

- `uv run scripts/check_repository_contract.py`：PASS。
- `uv run scripts/check_eval_contract.py`：PASS。
- `uv run scripts/check_eval_artifacts.py`：PASS。
- `uv run scripts/check_doc_contract.py`：PASS。
- CI 同款显式 pytest：以 G2 最终执行结果为准。
- `git diff --check`：PASS。
- 仓库根 `docs/site/` 与 `agents/docs/skills/`：零内容变更；测试 fixture 中的最小站内页面仅用于 eval。

G1 与 G2 的实现、fresh validation 和本地确定性验证均已完成；commit、PR 与 CI 交付按
Step 8 执行，不改变本计划的 `Implemented` 结论。

## 9. G5 latest-release 指针保护修复轮

PR #129 的 G5 修复范围已由维护者明确确认，不改变已批准 PRD 的产品范围：

1. skill 与 workflow 增加 SemVer latest/prerelease 决策。仅去掉一个仓库标准 `v` 前缀；
   prerelease 固定 `--prerelease --latest=false`；稳定版仅在严格高于当前 latest 时使用
   `--latest`，无法安全解析或比较时使用 `--latest=false`。
2. pre-write preview 展示当前 latest 证据、规范化版本、比较结果和最终 flag，由维护者
   连同标题、正文确认；draft create/update 与 publish 每次写前重读 latest，证据未漂移
   时复用最近一次确认的 flag，漂移时停止并刷新 preview、重新取得维护者确认。
3. TRD 同步技术契约；eval-002 改为严格 SemVer prerelease fixture，并新增
   `--latest=false` assertion。
4. 对受影响 eval 重新执行 fresh with-skill/without-skill validation，更新 durable
   `comparison.md`；随后刷新 computedHash，并执行四项 checker、CI 同款 pytest 与安装器
   测试。

本轮仍禁止真实 tag/Release 操作、merge、amend、rebase、force push、`--admin`、复用历史
baseline、提交 `tmp/` 或在会话内等待 review。

G5 实施结果：受影响 eval-002 已使用本轮全新 with-skill、without-skill 与独立 judge
完成验证，6/6 assertions PASS；durable `comparison.md` 已同步，并如实记录 fixture 提示较强、
without-skill 同为 6/6 的非阻塞区分度 finding。`github-release-generator` computedHash 已刷新。
四项 checker 全部 PASS，CI 同款 pytest 为 133 passed，安装器独立测试为 23 passed。
