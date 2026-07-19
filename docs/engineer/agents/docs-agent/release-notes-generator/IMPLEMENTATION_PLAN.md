---
title: "Release Notes Generator 实施计划"
type: IMPLEMENTATION_PLAN
version: "0.4.0"
status: Implemented
author: "Neplich Codex"
date: "2026-07-19"
last_updated: "2026-07-19"
feature: "release-notes-generator"
feature_path: "agents/docs-agent/release-notes-generator"
parent_feature: "agents/docs-agent"
feature_level: "3"
implementation_scope: "release-notes-generator-r1-r2"
related_prd: "docs/pm/agents/docs-agent/release-notes-generator/PRD.md"
related_trd: "docs/engineer/agents/docs-agent/release-notes-generator/TRD.md"
related_issues:
  - "https://github.com/Neplich/dev-agent-skills/issues/116"
  - "https://github.com/Neplich/dev-agent-skills/issues/117"
changelog:
  - version: "0.4.0"
    date: "2026-07-19"
    changes: "对齐 #117 pre-tag 消费面：site-ready handoff 显式传递维护者确认的 target_release_version 与确认来源"
  - version: "0.3.0"
    date: "2026-07-19"
    changes: "完成 R2 eval、fresh validation、全面自查和 PR 交付前验证"
  - version: "0.2.0"
    date: "2026-07-19"
    changes: "完成 R1 skill、注册、文档链和同名 skill 安装兼容"
---

# Release Notes Generator 实施计划

## 1. 实施依据

- 已批准 PRD：`docs/pm/agents/docs-agent/release-notes-generator/PRD.md`。
- 已批准 TRD：`docs/engineer/agents/docs-agent/release-notes-generator/TRD.md`。
- GitHub issue：#116；`request_type: existing_update`；`change_tier: major`。
- 功能路径：`agents/docs-agent/release-notes-generator`。
- issue #122 的 VitePress assets 只用于 AI Hub-shaped eval fixture，不是运行时依赖。

## 2. 完成范围

| 阶段 | 交付 | 完成证据 | 状态 |
| --- | --- | --- | --- |
| R1 — Skill 与注册 | 新增 Docs specialist、七步协议、确认与检查双门禁、site-ready handoff、docs-agent 分流、README/AGENTS/marketplace/skills-lock 注册，以及 PM/Docs 同名 skill 的 Codex 扁平安装兼容。 | R1 commit `a273a00`；仓库 checker 与 CI 同款 pytest 通过。 | Implemented |
| R2 — Eval 与全面自查 | 新增 3 个 specialist eval 和 router `eval-004`；基于 #122 资产提供可真实执行 `npm run test:docs` 的 fixture；刷新 docs-agent 全部 4 个 router eval 的 fresh 证据；修复入口、frontmatter、消费契约、注册描述、安装器测试和文档链 findings。issue #117 A2 对齐 site-ready handoff 的直接消费字段。 | 原 R2 fresh with/without、独立 judge 7/7 case、25/25 assertions PASS；#117 A2 对相关 3 个 specialist 与 2 个 router eval 重新生成 fresh 对照，5/5 case、18/18 assertions PASS。 | Implemented |

```mermaid
flowchart LR
    R1["R1 Skill + 注册 + 文档链"] --> R2["R2 Eval + Fresh Judge + 全面自查"]
    R2 --> PR["PR + CI + Review 等待"]
    PR --> DONE["Issue #116 交付完成；不自动 merge"]
```

## 3. Eval 资产

### 3.1 Release Notes specialist

1. `eval-001-generate-site-release-notes`：六类发布证据、`doc_type: release`、
   `last_verified_version: unverified`、确认后派生更新、真实宿主 checks 与完整 ready
   handoff。
2. `eval-002-confirmation-gate`：正文未确认时 index、metadata、导航零变化，handoff
   blocked 并等待明确确认。
3. `eval-003-github-release-boundary`：拒绝 GitHub Release 和 tag 操作，把外部发布交给
   #120，同时完成获授权的站内交付。

### 3.2 Docs router

`agents/docs/test/docs-agent/evals/` 新增 `eval-004-route-release-notes`，并对 router
`eval-001` 至 `eval-004` 全量刷新本轮 fresh with/without 与独立 judge 证据。router
只保留入口上下文并指向 specialist gate，不复制下游协议。

每个 eval 都有 schema 1.0 定义、显式 `workspace/...`、`execution_cleanup` 和 durable
`comparison.md`。运行期产物只位于 `tmp/eval-runs/116/`，不提交到 git。

## 4. 全面自查与修复

| Finding | 处理结果 |
| --- | --- |
| Specialist description 把 internal 误写成不可直调 | 改为非默认入口；显式直调仍必须通过 entry gate。 |
| 完成报告缺少入口依据 | 输出契约加入 accepted entry basis、release scope、证据边界和缺失凭据。 |
| Frontmatter 真源未登记新 producer/consumer | 在共享契约顶部和 Consumers 段加入 `release-notes-generator`。 |
| `stage` 规则与 TRD 存在例外差异 | 固定 `stage: release`。 |
| 证据读取缺少 consumption-contract 指针 | 宿主存在 change map 时按共享契约定位 required docs，并回到代码/测试核验；缺少 change map 不额外阻塞。 |
| Docs README 与 marketplace 总描述遗漏迁移后职责 | 改为 PM 提供分类和批准 scope，Docs 负责站内 Release Notes；marketplace 补 documentation。 |
| 安装器同名行为缺精准回归 | 断言 hidden mirror 同时保留 PM/Docs 两源，并新增同一 plugin 重名仍报错测试；既有安装路径回归保持通过。 |
| 文档链仍停在 R1/未实施状态 | TRD 和本计划同步为实际 R2 完成状态；计划状态更新为 `Implemented`。 |

注册面复核结果：根 README 中英、Docs README、AGENTS、marketplace 与 skills-lock 的
Docs `1 + 4`、全仓 33 specialist 计数和同名 source 解析一致。PM 侧同名 skill 未修改。

## 5. 职责边界

- #116 只交付站内 Release Notes 页面、确认后的索引/metadata、宿主 docs checks 和
  直接面向 #117 pre-tag audit 的 site-ready handoff；handoff 显式携带维护者确认的
  `target_release_version` 与确认来源。
- #117 继续拥有 pre-tag/post-tag audit 与 `last_verified_version` 统一盖章。
- #120 继续拥有 GitHub Release、compare/PR/贡献者信息、tag 与独立批准门禁。
- #121 继续拥有 API/database/design/ops/product 等一般正式文档同步。
- 本实施不 merge、不创建或移动 tag、不发布 GitHub Release、不部署、不修改 PM 侧同名
  skill。

## 6. 验证门禁

交付前按以下顺序执行：

```bash
uv run scripts/check_repository_contract.py
uv run scripts/check_eval_contract.py
uv run scripts/check_eval_artifacts.py
uv run scripts/check_doc_contract.py
uv run --with pytest pytest \
  agents/product_manager/test/idea-to-spec \
  agents/product_manager/test/pm-agent \
  agents/qa/test/test_qa_run_eval.py \
  agents/designer/test/test_designer_run_eval.py \
  agents/devops/test/test_devops_run_eval.py \
  agents/docs/test/test_docs_run_eval.py \
  agents/test_doc_contract.py \
  agents/test_eval_contract.py \
  scripts/test_install_codex_skills.py
```

AI Hub-shaped 成功路径另在隔离 workspace 执行 `npm run test:docs`。PR 创建后等待 CI
和 review 三信号，不自动合并。

## 7. 结果与残余限制

- Fresh judge 结论：原 R2 为 7/7 case、25/25 assertions PASS；issue #117 A2 的
  site-ready handoff 邻接回归为 5/5 case、18/18 assertions PASS，均使用新的
  without-skill baseline。
- 3 个 specialist with-skill 均在独立 Git 宿主的 `docs/site` 使用 #122 原版命令执行
  `GITHUB_BASE_SHA=HEAD npm run test:docs`，退出码为 0、74/74 tests PASS；eval-002
  只把该结果作为 harness preflight，正式 handoff 仍为 blocked/checks not-run，派生面
  保持零变化。
- Round2 增加确认前派生面 SHA 快照、原始 stdout/stderr、逐文件 manifest 和独立 Git
  状态证据。剩余限制仅是无法从隔离目录绝对证明外部系统零写入；eval-003 通过无
  remote、无 tag、ref 状态和运行产物核对满足当前 assertion，后续 runner 可增加
  gh/git/API 调用审计进一步强化。
- Issue #116 的实施范围已完成；计划保持活动入口但不自动归档，后续合并仍需维护者明确
  确认。
