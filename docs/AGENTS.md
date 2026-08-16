# 文档治理

## 职责归属

| 位置 | 唯一职责 | 禁止承载 |
| --- | --- | --- |
| 根 `AGENTS.md` | 每次工作都要加载的仓库不变量、权限、变更分级和 owner 指针 | Specialist 协议或长操作清单 |
| `docs/architecture.md` | 当前 Agent、安装、路由、协作和扩展架构 | 操作步骤或决策历史 |
| `docs/AGENTS.md` | 文档层级、职责、生命周期、归档和链接规则 | Agent 执行协议 |
| `docs/cookbook/` | 指向权威 Skill 的简短顺序化维护流程 | 重复的 schema 或契约 |
| `docs/pm/{feature_path}/` | 产品需求和已接受的产品决策 | 技术实现取舍 |
| `docs/engineer/{feature_path}/` | 当前技术设计、ADR 和活跃实施范围 | 产品决策或活跃入口中的已完成计划历史 |
| `agents/*/README*.md` | 角色能力目录、输入输出、边界和导航 | 共享契约或 Specialist 执行细节 |
| `agents/*/skills/*/` | Router 路由或 Specialist 专属协议 | 人工复制的跨角色契约 |

产品决策留在功能路径下的 `DECISIONS.md`，技术理由留在 `TRD.md` 或
`ADR-*.md`。不要创建中央 `docs/decisions/` 目录。

## 功能文档

公开过程文档使用 `docs/{role}/{feature_path}/`，每个路径段均为 lower
kebab-case。新功能文档的 frontmatter 包含 `feature`、`feature_path`、
`parent_feature`、`feature_level`、`version`、`date` 和 `last_updated`。
当前事实变化时同步更新 `last_updated` 和文档 changelog。

不要为了目录对称创建空的 Design、QA、DevOps 或 Security 文档树。只有角色确实存在
交付物时才创建对应路径。

## 实施计划生命周期

- 活跃入口固定为 `docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md`。
- 活跃计划表示已批准但尚未完成的工作，因此状态不得为 `Implemented` 或 `Archived`。
- closeout 完成并取得明确归档批准后，移动到
  `archive/IMPLEMENTATION_PLAN-<scope>.md`。
- 归档 scope 使用 lower kebab-case，并与 `implementation_scope` 一致。
- 冻结计划只使用 `Archived` 或 `Superseded`，并包含 `archived_at`、
  `archive_approved_by` 和 `source_plan`。
- 除非另有已批准的治理修正，不编辑冻结历史。

## QA E2E 资产

持久化 E2E 资产位于 `docs/qa/e2e/{feature_path}/`。QA Router 的以下 reference
分别是凭据存储、用例/脚本格式和报告格式的唯一权威：

- `agents/qa/skills/qa-agent/references/e2e-credential-store.md`
- `agents/qa/skills/qa-agent/references/e2e-case-format.md`
- `agents/qa/skills/qa-agent/references/e2e-test-report.md`

历史结果只追加不覆盖。Secret 只保存在被 Git 忽略的本地账号文件中，不进入用例、脚本
或报告。

## 派生内容与历史内容

Router 的 `_internal/_generated/shared-contracts/` 是只读派生物。修改 PM 权威源后运行
`scripts/generate_shared_contracts.py`，禁止手改副本。

版本 changelog 位于 `docs/changelog/changelog-v{version}.md`，根 `CHANGELOG.md`
只维护索引。冻结归档、changelog 历史、生成契约和 eval workspace 都不是当前规则源。

## 链接与检查

活跃 Markdown 的本地链接必须解析到仓库内。带 fragment 的链接必须匹配 GitHub 风格
heading slug，包括重复标题的序号后缀；路径不得逃出仓库。被排除为链接来源的历史文件
仍可作为有效链接目标。

运行：

```bash
uv run scripts/check_doc_contract.py
uv run scripts/check_repository_contract.py
```
