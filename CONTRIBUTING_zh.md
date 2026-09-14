# 参与维护

本仓库维护七个插件和四十个可直接使用的 Skill。贡献可以改进专业方法、脚本、安装体验或文档。

在工作分支上完成修改，保护已有用户改动。同步受影响的注册路径、发现描述、能力目录和 lockfile 哈希，按实际行为补充必要验证。参考 [Skill 维护](docs/cookbook/maintain-skills.md) 与 [仓库架构](docs/architecture.md)。

```bash
uv run scripts/generate_shared_contracts.py --check
uv run scripts/check_repository_contract.py
uv run scripts/check_doc_contract.py
uv run --with pytest pytest
git diff --check
```

PR 标题采用 `<type>(<scope>): <中文描述>`，正文说明变更、验证和影响。PR 创建后追加提交，合并使用维护者明确授权。完整 Git 和权限说明见 [AGENTS.md](AGENTS.md)，版本发布见 [发布指南](docs/cookbook/release.md)。

[English](./CONTRIBUTING.md)
