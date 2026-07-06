---
feature: release-changelog
version: 0.2.1
date: 2026-07-06
last_updated: 2026-07-06
---

# Changelog - v0.2.1

## [v0.2.1] - 2026-07-06

### Added

- **Plugin manifests 与合约校验**：为 6 个 agent 补齐 `.claude-plugin/plugin.json`，`name` / `version` / `description` / `author` 与 `marketplace.json` 及 `metadata.version`、`owner` 对齐，符合 Claude Code 每插件 manifest 标准；`check_repository_contract.py` 增加校验，强制每个 plugin source 存在 manifest 且 `name` / `version` 与 marketplace 一致。([#83](https://github.com/Neplich/dev-agent-skills/pull/83))
- **下游安全网收尾与 `auto-continue` 入口规则**：明确「未显式点名 → 默认 `pm-agent`；显式点名 → 受支持直达」的入口模型，并在 `skill-map.md` 新增唯一权威定义 `Safety-Net Closeout and Auto-Continue`——完成当前事项后主动建议协作链下一步并等确认，用户可开启 `auto-continue` 连续推进；缺前置时经 `pm-agent` 软引导补齐。角色硬边界与 role-only gate 优先于 `auto-continue`：跨角色只自动交接，下一环由下一角色自身 agent 在其 gate 下执行（例如 Designer 停在设计交付、把实现交回 `engineer-agent`）。6 个 dispatcher 的 `Output Behavior` 以指针引用该权威定义。([#85](https://github.com/Neplich/dev-agent-skills/pull/85))
- **文档契约校验 `check_doc_contract`**：新增独立 checker，校验 `docs/pm/**`、`docs/engineer/**` 正式文档的必填 frontmatter（`feature` / `version` / `date` / `last_updated`），并加入 description 防回归 denylist（除 `pm-agent` 外的 skill description 不得含用户侧触发起点短语）；接入 CI `doc-contract` job，PR 必跑校验链更新为 `repository-contract → eval-contract → doc-contract → python-tests`。([#86](https://github.com/Neplich/dev-agent-skills/pull/86))

### Changed

- **`visibility: internal` 声明层语义对齐**：保留字段与其合约校验，明确 `visibility: internal` 是声明层标记——Claude Code 与 Codex 均不消费该字段，不隐藏 slash 命令、也不阻止用户显式直达；`pm-agent` 为默认入口，下游标记为「非默认入口」而非「不可直接调用」。同步更新合约脚本 docstring、`AGENTS.md` 与 PM 单一入口 TRD 的相关措辞。([#84](https://github.com/Neplich/dev-agent-skills/pull/84))
- **发版 eval 复验（安全网行为）**：对 `#85` 改动的 6 个 dispatcher（`pm-agent` / `engineer-agent` / `qa-agent` / `designer-agent` / `devops-agent` / `security-agent`）执行 fresh Codex subagent 验证，重新生成 `without_skill` baseline 并更新 25 个 durable `comparison.md`。全部 case PASS：原有路由 / gate 无回归，`auto-continue` 在各角色均只推进到建议 / 交接、不越界；Designer / QA / Security 硬边界在 `auto-continue` 下仍成立。([#87](https://github.com/Neplich/dev-agent-skills/pull/87))
- **README 与仓库状态同步**：`README.md` / `README_zh.md` 本地验证命令补齐 `doc-contract` 检查、`agents/product_manager/test/pm-agent` 与 `agents/test_doc_contract.py`，并将「必跑检查」计数从 3 更新为 4，与 `ci.yml` 逐行一致；`AGENTS.md` 当前状态块把 `pm-agent` specialist 数更新为 8、Specialist 总数更新为 29，对齐实际的 35 skills / 29 specialist。([#88](https://github.com/Neplich/dev-agent-skills/pull/88))
