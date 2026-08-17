# 贡献指南

> 其他语言：[English](./CONTRIBUTING.md)

本文件只作为贡献者命令清单。仓库规则、文档契约、发布约束、commit / PR 文案和维护边界均以 [AGENTS.md](./AGENTS.md) 为权威。

## 本地验证

仓库内 Python 验证脚本默认使用 `uv run ...`。

PR 检查按 CI 顺序执行：

```bash
# 1. repository-contract
uv run scripts/check_repository_contract.py

# 2. doc-contract
uv run scripts/check_doc_contract.py

# 3. python-tests
uv run --with pytest pytest \
  agents/test_doc_contract.py \
  scripts/test_generate_shared_contracts.py \
  scripts/test_install_codex_skills.py \
  scripts/test_check_repository_contract.py
```

可选 JSON 静态格式检查：

```bash
uv run python -m json.tool .claude-plugin/marketplace.json >/tmp/marketplace.json.out
uv run python -m json.tool skills-lock.json >/tmp/skills-lock.json.out
```

## 维护索引

- 仓库工作流、分支和 PR 规则：[AGENTS.md](./AGENTS.md#开发工作流)
- 文档结构与 frontmatter 契约：[AGENTS.md](./AGENTS.md#文档组织)
- release 与 changelog 规则：[AGENTS.md](./AGENTS.md#仓库治理)
- QA E2E 持久化与凭据处理：[AGENTS.md](./AGENTS.md#qa-e2e-测试用例持久化)
