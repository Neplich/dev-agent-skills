# 维护 Skill

直接根据已授权的任务修改专业方法、脚本和参考。新增、重命名或调整能力范围时，同步检查注册、发现描述、文档与安装数据；[maintain-skills](../../.agents/skills/maintain-skills/SKILL.md) 提供具体参考。

1. 在工作分支上核实当前行为和预期结果。
2. 修改相关 Skill 与工具；同步 marketplace、插件描述、能力目录和 lockfile 内容哈希。
3. 共享参考源变更后运行 `uv run scripts/generate_shared_contracts.py`。
4. 执行相关行为测试与仓库检查，核对文档和实际产物一致。
5. 提交中文说明的 PR，记录结果与验证证据。

```bash
uv run scripts/generate_shared_contracts.py --check
uv run scripts/check_repository_contract.py
uv run scripts/check_doc_contract.py
git diff --check
```

## GitHub 配置

截至 2026-09-14，`main` 通过 PR 合入，合入前分支与 `main` 同步，以下三个 GitHub Actions 检查为必过项：`repository-contract`、`doc-contract`、`python-tests`。分支保护对管理员生效，保留 `main` 和已有提交历史。当前仅一位管理员，所需审阅批准数为 0；助手合并仍使用维护者的明确授权。

默认使用 squash merge。版本 tag 由 ruleset 保护，当前 Admin 具有 bypass 权限，发布按照手动清单执行。

配置复核：

```bash
gh api repos/Neplich/dev-agent-skills/branches/main/protection
```

检查结果中的三个 `required_status_checks.checks` 均绑定 GitHub Actions（`app_id: 15368`），`strict` 与 `enforce_admins.enabled` 为 `true`，`allow_force_pushes.enabled` 与 `allow_deletions.enabled` 为 `false`。
