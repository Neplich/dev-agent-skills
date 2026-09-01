---
feature: repository-ci-governance
version: 0.1.0-draft
date: 2026-05-06
last_updated: 2026-09-01
---

# Repository CI Governance Plan

## 目标

为 `dev-agent-skills` 仓库建立第一版 CI 门禁，用于支持从 `0.1.0`
开始的版本维护流程。

CI 的第一版目标是保护 `main`、skill 注册结构和基础测试。

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

## CI 启用前置任务

在把 CI 门禁加入 `main` required status checks 前，需要先完成以下整理：

1. [x] 扩展确定性 Python 测试
   - `python-tests` 覆盖仓库内所有确定性单元测试。
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

### 2. [x] python-tests

目的：执行当前已有的确定性 Python 测试。

第一版命令：

```bash
uv run --with pytest pytest \
  agents/test_doc_contract.py \
  scripts/test_generate_shared_contracts.py \
  scripts/test_install_codex_skills.py \
  scripts/test_check_repository_contract.py
```

说明：

- 该测试不依赖模型调用，适合作为 PR 硬门禁。
- 后续如果新增稳定的单元测试，可继续并入该 job。

## 第二阶段：Release CI

第二阶段用于版本发布和 tag 流程。

状态：当前不实现 Release CI；发布前采用手动 release checklist。

触发方式：

- [ ] 不新增 release workflow。
- [ ] 不配置 tag push 自动发布。

检查项：

- [ ] 复用第一阶段全部 PR 必跑 CI。
- [ ] 校验 release tag 格式为 `vMAJOR.MINOR.PATCH`，预发布按 SemVer 后缀扩展。
- [ ] 确认 `docs/changelog/changelog-v{version}.md` 存在并记录对应版本变更。
- [ ] 根目录 `CHANGELOG.md` 只作为版本索引。
- [ ] 按 `pm-agent → github-release-gen` 流程创建 GitHub Release draft 并交维护者审批；本仓无文档站宿主，使用维护者确认的版本事实源，不生成 `docs/release-notes/`。

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
- [x] `doc-contract`
- [x] `python-tests`

- [x] 通过后再把这三个 job 加入 `main` required status checks。

## 待确认问题

- [ ] 是否需要第一版就新增 `CODEOWNERS`。
- [x] required status checks 拆成 3 个 job：`repository-contract`、`doc-contract`、`python-tests`。
- [ ] `description` 是否需要最小长度校验。
- [ ] 是否需要在第一版 CI 中校验 README 中的本地验证命令仍存在。
- [x] 已新增 `CHANGELOG.md` 索引和 `docs/changelog/changelog-v0.1.0.md`。
- [x] 当前不启用 release CI。
