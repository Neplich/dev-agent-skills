# 文档说明

文档记录当前可用的能力、操作方法与经过核实的事实。按读者任务组织内容，每个主题维护一个清晰入口。

| 位置 | 内容 |
| --- | --- |
| 根 README | 能力介绍、安装与首次使用 |
| 根 AGENTS.md | 本仓库维护方式与权限 |
| docs/architecture.md | 当前能力组织与分发结构 |
| docs/README.codex.md | Codex 安装方式与维护 |
| docs/cookbook/ | Skill 维护与手动发布步骤 |
| agents/*/README*.md | 各插件的能力目录 |
| agents/*/skills/*/ | 专业方法、脚本、模板与参考 |
| docs/changelog/ | 已发布版本的事实记录 |

需要长期保存需求、技术方案、API、决策或测试结果时，沿用项目合适的文档位置。内容详略以实际读者和维护价值为依据。更新文档时同步相关入口，合并重复说明，保留最终结论和必要证据。历史修改可通过 Git 查阅。

选择使用 frontmatter 时保持字段准确；状态值沿用所选文档格式。链接指向仓库内真实文件，标题锚点与目标标题一致。

## QA E2E 资产

已有可复用 E2E 用例优先作为回归依据。需要持久化时可使用 `docs/qa/e2e/{feature_path}/`，凭据保存在被 Git 忽略的本地账号文件中，报告保留经过脱敏的结果和证据。QA Skill 的用例、凭据和报告参考提供具体格式。

## 共享参考与版本记录

`_internal/_generated/shared-contracts/` 由生成脚本维护，编辑源文件后重新生成。它们提供按需使用的协作和文档参考。

`docs/changelog/changelog-v{version}.md` 记录对应历史版本，根 `CHANGELOG.md` 提供索引。当前使用方式见 README 与架构说明。

```bash
uv run scripts/check_doc_contract.py
```
