# Changelog

本项目从 `v0.1.0` 开始按正式维护流程记录版本变更。

## [Unreleased]

## [0.1.0] - 2026-05-06

### Added

- 发布多角色 agent marketplace 初版，覆盖 PM、Designer、Engineer、QA、DevOps、Security 6 个 role agents。
- 提供 33 个可触发 skills，包括 6 个 dispatcher skills 和 27 个 specialist skills。
- 增加 Claude Code marketplace registry 与 Codex 安装入口，支持按 agent 独立安装和发现。
- 增加 Designer Agent 的 reference-backed visual design data，用于视觉系统、产品类型、配色、字体、UX 规则和技术栈设计参考。

### Changed

- 统一仓库治理与文档规范：`AGENTS.md` 作为唯一仓库指导源，`CLAUDE.md` 保持为指向 `AGENTS.md` 的相对软链。
- 形成英文 `README.md` 与中文 `README_zh.md` 的双语入口。
- 明确文档驱动协作模型和角色边界，Designer 停在设计交付，Engineer 承接代码、测试和交付产物。

### Fixed

- 修复 greenfield/new-repo 场景的 PM-first routing，避免需求澄清未完成时过早进入工程实现。
- 修复 Claude plugin root 作用域，按 agent 目录隔离 plugin source，降低跨 agent skill 暴露和路由污染风险。

### Test

- 建立共享 eval contract，统一所有 agent skill eval 的 `evals.json` schema v1.0。
- 增加 repository contract，校验 marketplace registry、skill frontmatter、`CLAUDE.md` 软链、`skills-lock.json` 和禁止提交的本地/运行期文件。
- 增加 PM、Designer、QA、DevOps 的确定性 pytest 覆盖，区分 durable `comparison.md` 与临时 runtime artifacts。
- 补齐 PM specialist eval、QA durable comparison 和 eval artifact 检查，保持仓库只提交评测任务、fixture 和最新结论。

### CI

- 增加 PR 和 `main` push 必跑 GitHub Actions workflow。
- 将 `repository-contract`、`eval-contract`、`python-tests` 配置为 `main` required status checks。
