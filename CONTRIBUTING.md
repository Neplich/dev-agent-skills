# Contributing Guide

> Other languages: [中文](./CONTRIBUTING_zh.md)

This file is only a contributor command list. Repository rules, document contracts, release constraints, commit / PR wording, and maintenance boundaries are all governed by [AGENTS.md](./AGENTS.md) as the single source of authority.

## Local Validation

Python validation scripts in this repository use `uv run ...` by default.

PR checks run in CI order:

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

Optional JSON static format check:

```bash
uv run python -m json.tool .claude-plugin/marketplace.json >/tmp/marketplace.json.out
uv run python -m json.tool skills-lock.json >/tmp/skills-lock.json.out
```

## Maintenance Index

- Repository workflow, branch, and PR rules: [AGENTS.md](./AGENTS.md#开发工作流)
- Document structure and frontmatter contract: [AGENTS.md](./AGENTS.md#文档组织)
- Release and changelog rules: [AGENTS.md](./AGENTS.md#仓库治理)
- QA E2E persistence and credential handling: [AGENTS.md](./AGENTS.md#qa-e2e-测试用例持久化)
