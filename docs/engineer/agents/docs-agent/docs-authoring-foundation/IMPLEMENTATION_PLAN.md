---
title: "Docs Authoring Foundation 实施计划"
type: IMPLEMENTATION_PLAN
version: "0.1.0"
status: Approved
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
  - version: "0.1.0"
    date: "2026-07-19"
    changes: "记录 W1 至 W6 已批准实施总纲与分阶段验证门禁"
---

# Docs Authoring Foundation 实施计划

## 1. 前置对齐

- 已批准需求：`docs/pm/agents/docs-agent/docs-authoring-foundation/PRD.md`；该
  PRD 由维护者已确认的 GitHub issue #122 规格转化而来。
- 技术输入：本目录 `TRD.md`，版本 `0.1.0`，状态 `Approved`。
- Feature metadata：`agents/docs-agent/docs-authoring-foundation`，父功能
  `agents/docs-agent`，层级 `3`。
- `change_tier: major`：影响 bootstrap 静态交付方式、宿主命令、脚手架、测试和
  skill eval，保留完整计划、验证与维护者确认门禁。
- 维护者已批准实施总纲：W1 资产抽取 → W2 模板 scaffold 区块 → W3 确定性
  脚手架与测试 → W4 宿主命令契约 → W5 bootstrap 门禁保持 → W6 eval 与交付。
- 本轮只执行 W1 和本计划落盘；W2 至 W6 仅记录，不能据此在本轮提前修改。

## 2. 目标与非目标

目标是让 bootstrap、宿主写作流程和测试共享同一组真实资产；以五类宿主模板的
唯一 scaffold 区块作为文档骨架单一来源；交付唯一 `new:doc` 入口、确定性
change-map 合并、原子写入和完整测试证据，同时保持现有 bootstrap opt-in、
冲突、manifest、`kept-as-is`、回读与 zero-diff 语义。

非目标：引入 AI Hub 项目事实；修改 frontmatter 字段语义或 audit 盖章语义；
生成 Release Notes；替代 #121 的范围确认与事实写作；修改宿主 GitHub Actions；
自动发布、push、开 PR 或 merge。

## 3. 分阶段计划

| 阶段 | 内容 | 验证方式 |
| --- | --- | --- |
| W1 静态资产抽取（本轮已确认并执行） | 新建 `assets/docs/site/**`，将基线 `_internal/INSTRUCTIONS.md` 中每个 `Target:` 静态正文按相同宿主相对路径逐字节迁出；指令收敛为 gate、inventory、冲突、manifest、顺序、资产索引、回读和 zero-diff；同步 `SKILL.md` 资产化措辞并只刷新 `docs-site-bootstrap` lock hash。 | 临时脚本从 W1 基线提取每个目标正文，输出“资产路径 ← 原行区间 ← 一致性”表并逐字节全通过；资产清单无 `bootstrap-manifest.json`；`INSTRUCTIONS.md` 不超过 400 行；4 个 contract checker 和 CI 同款 pytest 通过。 |
| W2 五模板 scaffold 区块 | 在 api、database、design、ops、product 五个宿主模板中各加入唯一 `docs-scaffold:start/end` 区块；各模板使用目标 `doc_type`，`standards/templates/**` 保留 frontmatter / 结构校验但免类型化事实核查；formal-docs-sync 单类型流程只渐进读取当前模板。 | 解析测试证明每个模板恰有一组有序标记和可解析 `md` 围栏；五种 `doc_type` 与目标目录对应；全仓检查不存在第二份完整骨架；internal 站点检查通过。 |
| W3 确定性脚手架与测试 | 新增 `scripts/scaffold-doc.mjs`，实现显式输入、路径与类型约束、固定 `unverified`、dry-run、默认拒绝覆盖、显式 change-map merge、未知内容保留、页面与 map 原子写入、回读和 `test:docs`；change-map 头部校验归本 feature 工具链。 | `scaffold-doc.test.mjs` 覆盖五类成功路径、未知类型、越界、类型错配、覆盖拒绝、区块异常、dry-run 零写入、merge 去重稳定排序、未知内容保留、失败回滚与写后校验；fixture 无独立模板正文。 |
| W4 宿主命令契约 | 在宿主资产 `package.json` 只暴露 `new:doc`，指向唯一 `scaffold-doc.mjs`；保持 prepare、dev、build、frontmatter、affected、version 与 `test:docs` 命令组织，Release Notes 请求拒绝并 handoff #116。 | 在隔离 AI Hub-shaped fixture 执行 `npm run new:doc -- ...` 的 dry-run / 写入用例和 `npm run test:docs`；分别执行 public / internal build；确认无 `new-doc` 或第二个 scaffold 命令。 |
| W5 Bootstrap 门禁保持 | 让 bootstrap 从资产复制完整宿主基础，保持显式 opt-in、全量 inventory、冲突汇总、overwrite / merge / `kept-as-is` 选择、动态 manifest、写后回读、人工内容保护和重复 zero-diff；渐进加载不削弱完整交付。 | 现有 bootstrap 确定性测试全部通过，并新增或调整资产源断言；空目录、identical、conflict、`kept-as-is`、无效 manifest、已填充 change map / release metadata、重复运行均符合原语义。 |
| W6 Eval 与交付 | 更新受影响 eval 定义和 durable `comparison.md`，重做资产化后 `eval-002` 字节 fixture；执行 fresh with-skill 与同 prompt / fixture 的 fresh without-skill baseline；刷新最终 lock hash并完成全量检查、review 与交付。 | 4 个 contract checker、CI 同款 9 路径 pytest、宿主 Node 测试全部通过；fresh judge 结论写入 `comparison.md`；运行期 transcript / verdict / diagnostics 不提交；diff 无 AI Hub 事实、无无关变更，维护者确认后才进入 PR / merge 流程。 |

```mermaid
flowchart LR
    W1["W1 资产抽取"] --> W2["W2 模板唯一 scaffold 区块"]
    W2 --> W3["W3 脚手架与测试"]
    W3 --> W4["W4 new:doc 命令契约"]
    W4 --> W5["W5 Bootstrap 门禁回归"]
    W5 --> W6["W6 Fresh eval 与交付"]
```

## 4. W1 本轮精确范围

### 4.1 允许修改

- 新增 `agents/docs/skills/docs-site-bootstrap/assets/docs/site/**`，逐一对应基线
  `INSTRUCTIONS.md` 的静态 `Target:`。
- 重写 `agents/docs/skills/docs-site-bootstrap/_internal/INSTRUCTIONS.md`，只保留
  执行协议与资产索引，控制在 400 行以内。
- 必要时只修改 `agents/docs/skills/docs-site-bootstrap/SKILL.md` 的“内嵌模板”
  表述为“资产文件”，不改变 gate。
- 新增本目录 `TRD.md` 与 `IMPLEMENTATION_PLAN.md`。
- 仅刷新 `skills-lock.json` 中 `docs-site-bootstrap.computedHash`。
- 临时字节自检脚本和结果写入 `tmp/`，不得提交。

### 4.2 禁止修改

- 不改变任何迁移正文的字节，包括格式、注释、依赖版本和结尾换行。
- 不创建静态 `assets/docs/site/.meta/bootstrap-manifest.json`。
- 不修改 eval fixture、`evals.json` 或 `comparison.md`；这些属于 W6。
- 不实现 scaffold 标记、`scaffold-doc.mjs`、`new:doc` 或新测试；这些属于
  W2 至 W4。
- 不加入 AI Hub 名称、owners、业务路径、版本、change map 或 release 数据。
- 不 push、开 PR、merge、amend、rebase 或 force push。

### 4.3 W1 操作顺序

1. 记录分支创建前的 `INSTRUCTIONS.md` blob，枚举全部 `Target:` 与代码围栏边界。
2. 逐目标创建同构资产，保留原正文和结尾字节。
3. 运行临时提取器逐字节比较；任何不一致先修复资产，不进入下一步。
4. 将 `INSTRUCTIONS.md` 改为协议与逐文件映射索引，回读确认完整 inventory、
   冲突、`kept-as-is`、manifest 和 zero-diff 规则仍在。
5. 同步 `SKILL.md` 的资产化措辞；刷新单一 lock hash 字段。
6. 执行 contract checker、CI pytest、字节映射检查和 diff 审核。
7. 按维护者指定文案创建一次普通 commit；不 push，并停在功能分支。

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

- W1 已获维护者确认，本轮可以执行；完成 W1 后停下报告，不自动进入 W2。
- W2 至 W6 每阶段开始前回读 issue #122、TRD、当前计划与前一阶段证据；若范围、
  scaffold 标记、命令名、模板类型或 issue 边界变化，先更新批准文档。
- 每阶段只处理该行文件与验证，发现无关问题仅报告。
- 实施完成后记录最终文件、命令、结果、eval 证据和残余风险；只有维护者明确批准
  closeout 后才能归档活动计划。
- 本轮 Git 交付只允许指定普通 commit，不 push，并停在
  `feat/122-docs-authoring-foundation`。
