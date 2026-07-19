---
title: "Docs Authoring Foundation 实施计划"
type: IMPLEMENTATION_PLAN
version: "0.3.0"
status: Implemented
author: "Neplich Codex"
date: "2026-07-19"
last_updated: "2026-07-19"
feature: "docs-authoring-foundation"
feature_path: "agents/docs-agent/docs-authoring-foundation"
parent_feature: "agents/docs-agent"
feature_level: "3"
implementation_scope: "docs-authoring-foundation"
related_prd: "docs/pm/agents/docs-agent/docs-authoring-foundation/PRD.md"
related_trd: "docs/engineer/agents/docs-agent/docs-authoring-foundation/TRD.md"
related_issues:
  - "https://github.com/Neplich/dev-agent-skills/issues/122"
changelog:
  - version: "0.3.0"
    date: "2026-07-19"
    changes: "记录 C5R 全量自查、同类缺陷加固、eval-002 字节对齐与最终验证"
  - version: "0.2.0"
    date: "2026-07-19"
    changes: "按 C1-C4 实际交付重整 W1-W6 范围，并记录首轮 review 加固与验证收尾"
  - version: "0.1.0"
    date: "2026-07-19"
    changes: "记录 W1 至 W6 已批准实施总纲与分阶段验证门禁"
---

# Docs Authoring Foundation 实施计划

## 1. 前置对齐

- 已批准需求：`docs/pm/agents/docs-agent/docs-authoring-foundation/PRD.md`；该
  PRD 由维护者已确认的 GitHub issue #122 规格转化而来。
- 技术输入：本目录 `TRD.md`，版本 `0.2.0`，状态 `Approved`。
- Feature metadata：`agents/docs-agent/docs-authoring-foundation`，父功能
  `agents/docs-agent`，层级 `3`。
- `change_tier: major`：影响 bootstrap 静态交付方式、宿主命令、脚手架、测试和
  skill eval，保留完整计划、验证与维护者确认门禁。
- 维护者已批准实施总纲：W1 资产抽取 → W2 模板 scaffold 区块 → W3 确定性
  脚手架与测试 → W4 宿主命令契约 → W5 bootstrap 门禁保持 → W6 eval 与交付。
- 实际交付分为五轮：C1 完成 W1 与 PRD/TRD/实施计划文档链；C2 完成
  W2-W4；C3 完成 W6 的 eval 对齐与 fresh validation；C4 按 PR #125 review
  加固 W3/W4；C5R 接手 4 条 P2 后逐文件审查全部可执行资产，一次性修复同类
  缺陷并完成交付复核。W5 不是独立功能提交，其门禁保持要求贯穿 C1-C5R 并由
  bootstrap 与宿主回归验证。

## 2. 目标与非目标

目标是让 bootstrap、宿主写作流程和测试共享同一组真实资产；以五类宿主模板的
唯一 scaffold 区块作为文档骨架单一来源；交付唯一 `new:doc` 入口、确定性
change-map 合并、原子写入和完整测试证据，同时保持现有 bootstrap opt-in、
冲突、manifest、`kept-as-is`、回读与 zero-diff 语义。

非目标：引入 AI Hub 项目事实；修改 frontmatter 字段语义或 audit 盖章语义；
生成 Release Notes；替代 #121 的范围确认与事实写作；修改宿主 GitHub Actions；
自动发布、创建新 PR 或 merge。

## 3. 分阶段计划

| 阶段 | 内容 | 验证方式 |
| --- | --- | --- |
| W1 静态资产抽取（C1） | 新建 `assets/docs/site/**`，将基线 `_internal/INSTRUCTIONS.md` 的静态正文按宿主相对路径逐字节迁出；同时建立 PRD、TRD 与本实施计划文档链，收敛 Skill 指令并刷新 lock hash。 | 字节映射、资产清单、指令规模、仓库 checker 与 pytest 在 C1 验证通过。 |
| W2 五模板 scaffold 区块（C2） | 在五类宿主模板中交付唯一 `docs-scaffold:start/end` 区块，并补 standards 索引与单类型渐进读取约束。 | 模板 marker、`md` 围栏、`doc_type` 与目录映射由脚手架测试和文档检查覆盖。 |
| W3 确定性脚手架与测试（C2，C4/C5R 加固） | C2 交付 `scaffold-doc.mjs`、五类创建、dry-run、覆盖拒绝、change-map merge、原子写入与回滚；C4/C5R 补齐 realpath、隐藏段、额外 mapping target、repo-relative glob、schema、回滚失败和写前复验。 | `scaffold-doc.test.mjs` 覆盖五类成功路径及 symlink、Windows、畸形 schema、CLI、原子回滚和失败清理。 |
| W4 宿主命令契约（C2，C4/C5R 加固） | 保持唯一 `new:doc` 和 prepare/dev/build/check/test 命令；C5R 让 `test:docs` 严格阻断 affected-doc 缺口，生成目录采用 staging 替换，watcher、child、timer 与信号在错误路径也清理。 | 隔离宿主执行 `npm run test:docs` 及 public/internal build；Node 回归覆盖平台命令、进程生命周期、symlink 扫描和稳定排序。 |
| W5 Bootstrap 门禁保持（C1-C5R 持续验证） | 资产复制继续保持显式 opt-in、完整 inventory、冲突汇总、`kept-as-is`、动态 manifest、回读、人工内容保护和重复 zero-diff。 | C3 fresh eval 证明完整交付、冲突阻断和幂等语义；C5R 对物化 `package.json` 重新做字节对齐。 |
| W6 Eval 与交付（C3-C5R） | C3 完成 fresh with/without 与 durable comparison；C5R 核查物化清单、同步变化的 fixture，刷新 lock hash，执行宿主与仓库全量检查后一次提交、push、review 与 CI。 | 不提交运行期产物，不 merge；是否重跑模型 eval与实际执行情况分别如实记录。 |

```mermaid
flowchart LR
    W1["W1 资产抽取"] --> W2["W2 模板唯一 scaffold 区块"]
    W2 --> W3["W3 脚手架与测试"]
    W3 --> W4["W4 new:doc 命令契约"]
    W4 --> W5["W5 Bootstrap 门禁回归"]
    W5 --> W6["W6 Fresh eval 与交付"]
```

## 4. 实际交付分组

1. **C1 / `5f39454`**：完成 W1 静态资产化，并建立 PRD、TRD、实施计划文档链。
2. **C2 / `a2a30a3`**：完成 W2 五模板区块、W3 脚手架与测试、W4 宿主命令。
3. **C3 / `c4e7026`**：完成 W6 的 eval 定义、fixture、fresh with/without
   validation 与 durable comparison；同时补齐 bootstrap 入口报告协议。
4. **C4 / PR #125 review 修复**：只处理 7 条已核实 P2，补充相应回归测试，
   按 eval-002 物化清单决定是否重验，刷新 lock hash并完成 push、review 与 CI
   复核；禁止 merge、amend、rebase、force push 或提交 `tmp/`。
5. **C5R / PR #125 全面自查加固**：接手 3 个未提交文件和 4 条 P2，逐文件
   审查全部宿主可执行资产，修复同类问题、同步文档与 eval-002 物化字节，一次
   commit 与 push 后只触发一轮 review；新意见只记录不继续修改。

## 5. 验证命令

W1 至交付阶段至少依序执行：

```bash
uv run scripts/check_repository_contract.py
uv run scripts/check_eval_contract.py
uv run scripts/check_eval_artifacts.py
uv run scripts/check_doc_contract.py
```

随后执行 `.github/workflows/ci.yml` 当前定义的 9 路径 pytest 命令；W3 起再执行
宿主 `scripts/__tests__/*.test.mjs`，W4 起在隔离 fixture 执行
`npm run test:docs`、`npm run build:public` 和 `npm run build:internal`。实际命令
和测试数量以运行时仓库状态记录，不能用计划值代替验证证据。

W1 的临时自检必须逐文件报告：

```text
assets/docs/site/<relative-path> <- INSTRUCTIONS.md:<start>-<end> <- identical
```

所有条目均为 `identical` 才能提交。若现有 docs eval 只因仍断言“内嵌正文”而
失败，本轮如实报告，不修改 eval；修复归 W6 / 后续已确认的 eval 阶段。

## 6. 风险与缓解

| 风险 | 缓解 |
| --- | --- |
| `eval-002` 保存了旧内嵌正文的字节 fixture，资产化后失去来源或产生假失败 | W1 保留现状并报告；W6 从真实资产重做 fixture 和断言，同轮 fresh 生成 without-skill baseline 并更新 durable `comparison.md`。 |
| `formal-docs-sync` 的渐进加载被误解为 bootstrap 按类型裁剪 | Bootstrap 始终复制完整资产；W2 只让编写流程读取 standards 公共规则和当前类型模板，W5 增加全量 inventory 回归。 |
| W1 提取器错误处理代码围栏或末尾换行 | 以基线 blob 和二进制读取为准，记录源行区间，同时比较长度与字节；不经 Markdown formatter。 |
| 五模板或测试形成第二份 scaffold 正文 | 唯一正文留在模板标记区块；实现做解析，测试使用最小 fixture 和结构断言。 |
| change-map merge 覆盖宿主人工内容 | W3 先解析、只改显式键、保留未知内容并稳定合并，页面和 map 原子提交后回读。 |
| `new:doc` 被误当成事实写作能力 | 输出只含明确输入和类型骨架，固定 `unverified`；事实填充交给 #121。 |
| Release Notes 误入通用脚手架 | 类型白名单不含 release，拒绝并 handoff #116。 |
| issue #122 的 `feature_level` 标注与仓库路径层级契约不一致 | 同路径 PRD、TRD 与计划统一按三段 `feature_path` 记录为 level 3；不扩展 checker。 |

## 7. 阶段门禁与收尾

- W1-W4 已按 C1/C2 完成，W5 门禁保持已由 C3 eval 与 C4/C5R 回归继续验证。
- C3 已完成 W6 的 fresh eval；C5R 的 `package.json` 属于 eval-002 物化目标，
  因此同步 fixture 字节与版本说明，但不把未执行的模型 eval 声称为 fresh PASS。
- C5R 完成后记录最终文件、命令、eval 决策和残余风险，普通 commit 并 push 到
  既有 PR 分支；等待 review 三信号和 CI 全绿后切回 `main`。
- 活动计划不在本轮归档；PR #125 不 merge，不 amend、rebase、force push 或使用
  管理员绕过。

## 8. 实施结果

### 8.1 C4 与 C5R 完成范围

- `scaffold-doc.mjs` 已拒绝非仓库相对 code glob、非 Markdown page 的
  change-map target，并在写 change map 前校验其真实父路径仍位于 `docs/site/`。
- `check-affected.mjs` 已把工作区中不存在的 required doc 判为缺失，即使删除路径
  同时出现在 Git changed set 中。
- `dev-site.mjs` 已在 VitePress 子进程退出时清理 watcher 与信号监听，并传播数字
  退出码；脚手架写后检查在 Windows 使用 `npm.cmd`。
- `scaffold-doc.test.mjs` 已加入上述边界和跨平台回归测试；未新增第二份模板正文。
- C5R 继续完成 Windows 回滚路径、额外 mapping target realpath、隐藏路径段和缺失
  顶层 `change_map` 4 条 P2，并补齐 change-map rule schema、required-doc symlink、
  NUL Git 路径、CLI 重复参数、exclude/related-code 路径和回滚失败传播。
- 页面与静态资产扫描不再跟随外部 symlink；生成站点以 staging 目录替换，失败
  保留上一份完整输出；导航/文本写入使用 UTF-8 临时文件再 rename。
- dev 生命周期覆盖 child spawn error、watcher error、SIGINT/SIGTERM、timer 和
  listener 清理；sidebar 改为与 locale 数据无关的稳定码点排序。

### 8.2 验证记录

| 命令 / 检查 | 结果 |
| --- | --- |
| 临时宿主 `npm run test:docs` | PASS，67 tests，0 failures |
| `uv run scripts/check_repository_contract.py` | PASS |
| `uv run scripts/check_eval_contract.py` | PASS |
| `uv run scripts/check_eval_artifacts.py` | PASS |
| `uv run scripts/check_doc_contract.py` | PASS |
| `.github/workflows/ci.yml` 同款 pytest 命令 | PASS，126 tests |

### 8.3 Eval 与残余风险

- eval-002 未重跑模型 eval。其 9 个物化目标包含本轮修改的 `package.json`，已将
  fixture 字节与范围版本同步到 C5R 资产；manifest 的 9 个路径与
  `skipped-identical` 状态不变。C3 的 fresh PASS 仍是最近一次模型结论，本轮只
  记录确定性 byte-for-byte 对齐，不伪造新的 with/without 结果。
- Windows shim 与 child-exit 生命周期由确定性单元测试覆盖；最终跨平台状态仍以
  PR CI 和后续真实 Windows 宿主运行为准。
- 下一所有者为 PR #125 review 与 CI 复核；本轮不需要新增 QA E2E 文档，原因是
  变更只影响 docs bootstrap 开发者脚本和单元测试，不改变终端产品用户流程。
