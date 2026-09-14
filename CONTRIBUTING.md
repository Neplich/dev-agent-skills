# Contributing

This repository maintains seven plugins and forty directly usable Skills. Contributions can improve professional methods, tools, installation or documentation.

Work on a branch and preserve unrelated user changes. Synchronize affected registration paths, discovery descriptions, capability directories and lockfile hashes. Verify the behavior that changed. See [Skill maintenance](docs/cookbook/maintain-skills.md) and [architecture](docs/architecture.md).

```bash
uv run scripts/generate_shared_contracts.py --check
uv run scripts/check_repository_contract.py
uv run scripts/check_doc_contract.py
uv run --with pytest pytest
git diff --check
```

Use `<type>(<scope>): <中文描述>` for commit and PR titles and Chinese PR bodies describing changes, validation and impact. Append commits after opening a PR. Merge with explicit maintainer authorization. See [repository guidance](AGENTS.md) and the [manual release procedure](docs/cookbook/release.md).

[中文](./CONTRIBUTING_zh.md)
