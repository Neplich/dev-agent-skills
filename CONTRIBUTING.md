# 贡献指南

本文件只作为贡献者命令清单。仓库规则、文档契约、eval 策略、发布约束、commit / PR 文案和维护边界均以 [AGENTS.md](./AGENTS.md) 为权威。

## 本地验证

仓库内 Python 验证脚本和 eval runner 默认使用 `uv run ...`。

PR 检查按 CI 顺序执行：

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
  agents/test_doc_contract.py \
  agents/test_eval_contract.py \
  scripts/test_install_codex_skills.py
```

可选 JSON 静态格式检查：

```bash
uv run python -m json.tool .claude-plugin/marketplace.json >/tmp/marketplace.json.out
uv run python -m json.tool skills-lock.json >/tmp/skills-lock.json.out
```

## 手动 Eval

本地模型 eval 是质量检查，不属于第一版 PR 必跑 status check：

```bash
# Designer eval diagnostics
uv run agents/designer/test/run_all_evals.py

# QA model eval
uv run agents/qa/test/run_all_evals.py
```

涉及 skill 行为、routing、eval fixture 或 release readiness 的变更，按 [AGENTS.md](./AGENTS.md#skill-测试) 的 eval 策略执行。GitHub Actions 的 `Manual Evals` workflow 可选择 `all`、`designer` 或 `qa`；QA eval 需要仓库 `OPENAI_API_KEY` secret。

## Eval 维护清单

仓库只保留 eval 定义和最新持久化结论，运行日志和 transcript 不进 git。详细规则见 [AGENTS.md](./AGENTS.md#skill-测试)。

1. 新建或更新 skill 与 eval fixture。
2. 运行相关确定性检查和已批准的手动 eval。
3. 将最新持久化结果写入 `comparison.md`。
4. 开 PR 前删除运行期产物。
5. 只提交 eval 定义、metadata、fixture、README 文件和 `comparison.md`。

`comparison.md` 使用以下结构：

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

## 维护索引

- 仓库工作流、分支和 PR 规则：[AGENTS.md](./AGENTS.md#开发工作流)
- 文档结构与 frontmatter 契约：[AGENTS.md](./AGENTS.md#文档组织)
- release 与 changelog 规则：[AGENTS.md](./AGENTS.md#仓库治理)
- skill eval schema 与 artifact 策略：[AGENTS.md](./AGENTS.md#skill-测试)
- QA E2E 持久化与凭据处理：[AGENTS.md](./AGENTS.md#qa-e2e-测试用例持久化)
