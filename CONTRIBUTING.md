# Contributing Guide

> Other languages: [中文](./CONTRIBUTING_zh.md)

This file is only a contributor command list. Repository rules, document contracts, eval strategy, release constraints, commit / PR wording, and maintenance boundaries are all governed by [AGENTS.md](./AGENTS.md) as the single source of authority.

## Local Validation

Python validation scripts and the eval runner in this repository use `uv run ...` by default.

PR checks run in CI order:

```bash
# 1. repository-contract
uv run scripts/check_repository_contract.py

# 2. eval-contract
uv run scripts/check_eval_contract.py
uv run scripts/check_eval_artifacts.py

# 3. doc-contract
uv run scripts/check_doc_contract.py

# 4. python-tests
uv run --with pytest pytest \
  agents/product_manager/test/idea-to-spec \
  agents/product_manager/test/pm-agent \
  agents/qa/test/test_qa_run_eval.py \
  agents/designer/test/test_designer_run_eval.py \
  agents/devops/test/test_devops_run_eval.py \
  agents/docs/test/test_docs_run_eval.py \
  agents/test_doc_contract.py \
  agents/test_eval_contract.py \
  scripts/test_eval_runtime.py \
  scripts/test_run_skill_eval.py \
  scripts/test_check_eval_artifacts.py \
  scripts/test_install_codex_skills.py \
  scripts/test_summarize_eval_results.py \
  scripts/test_check_repository_contract.py
```

Optional JSON static format check:

```bash
uv run python -m json.tool .claude-plugin/marketplace.json >/tmp/marketplace.json.out
uv run python -m json.tool skills-lock.json >/tmp/skills-lock.json.out
```

## Manual Eval

Local model evals are quality checks and are not part of the first-round required PR status checks. Designing, writing, running, rerunning, summarizing, or diagnosing evals must go through the project-level skill `.agents/skills/skill-eval-runner/SKILL.md`:

```bash
# One role (e.g. designer)
uv run scripts/run_skill_eval.py --agent designer --jobs 10

# All regular evals
uv run scripts/run_skill_eval.py --jobs 10
```

Changes involving skill behavior, routing, eval fixtures, or release readiness follow the eval strategy in [AGENTS.md](./AGENTS.md#skill-测试). The GitHub Actions `Manual Evals` workflow accepts `all`, `designer`, `devops`, `docs`, `engineer`, `product_manager`, `qa`, or `security`; every target requires the repository `OPENAI_API_KEY` secret.

## Eval Maintenance Checklist

The repository keeps only eval definitions and the latest persisted conclusions; run logs and transcripts do not enter git. See [AGENTS.md](./AGENTS.md#skill-测试) for the detailed rules.

1. Create or update the skill and eval fixtures.
2. Run the relevant deterministic checks and the approved manual evals.
3. Write the latest persisted result into `comparison.md`.
4. Remove runtime artifacts before opening a PR.
5. Commit only eval definitions, metadata, fixtures, README files, and `comparison.md`.

`comparison.md` uses the following structure:

```markdown
# Eval Result: <eval-name>

## Evaluation Target
## Test Set / Fixture Version
## Latest Result
## With Skill
## Without Skill / Baseline
## Failures
## Next Steps
## Runtime Artifacts Policy
```

## Maintenance Index

- Repository workflow, branch, and PR rules: [AGENTS.md](./AGENTS.md#开发工作流)
- Document structure and frontmatter contract: [AGENTS.md](./AGENTS.md#文档组织)
- Release and changelog rules: [AGENTS.md](./AGENTS.md#仓库治理)
- Skill eval schema and artifact policy: [AGENTS.md](./AGENTS.md#skill-测试)
- QA E2E persistence and credential handling: [AGENTS.md](./AGENTS.md#qa-e2e-测试用例持久化)
