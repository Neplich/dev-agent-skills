# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-015-flat-hierarchy-migration-proposal`
- Review context: issue #225，为已有扁平文档补上迁移触发机制

## Test Set / Fixture Version

- Fixture: `workspace/eval-015-flat-hierarchy-migration-proposal` 初始快照（issue #225 新增）
- Scenario: 宿主 API 根下 6 个稳定页面按 feature catalog 分属三个一级功能域却全部平铺，本批次要同步一个属于其中一个域的新会话消息 API 页；维护者只确认了新页面同步，未确认任何路径迁移
- Evidence set: PM handoff、feature catalog、Approved PRD、Confirmed TRD、完成态实施计划、路由与 schema 源码、contract tests、既有 change map（含手工未知字段条目）、现有扁平 API 页与 host standards
- Actual validation date: `2026-08-05`
- Isolation: 三条互相独立的 fresh `codex exec` 会话——`with_skill`、`without_skill`、judge。两条 lane 复制同一份 pristine fixture（排除 `comparison.md` 与 `eval_metadata.json`）到 `tmp/eval-runs/issue-225-20260805/` 下各自目录；`without_skill` lane 被显式禁止读取任何 agent skill 文档、Agent README、仓库指导文件与历史 eval 结果

## Latest Result

- Behavior result: PASS
- Coverage result: FULL
- With skill 5/5；fresh without_skill baseline 1/5

Overall result: PASS

## Assertions

- `detects_flat_hierarchy_drift`: with skill PASS；without skill FAIL。skill lane 在候选范围前基于 frontmatter 与 feature catalog 点名 `research-conversations.md` 与 `graph-search.md` 属于缺失的 `knowledge-discovery` 父节点；baseline 虽新建了嵌套目录，却没有识别既有页面构成 drift，也没有给出共同父节点的判定证据。
- `proposes_migration_before_write`: with skill PASS；without skill FAIL。skill lane 在同一次确认里给出目标子树、两个旧路径到 canonical 新路径及兼容入口的映射、入链与递归导航 delta、两条 change-map 映射闭包、排除边界和新页面落位；baseline 没有任何旧新路径映射或迁移 delta。
- `does_not_deepen_flat_layout`: 两条 lane 均 PASS。两者都把新页面放在目标深度、未移动既有页面，且目录比较确认对 fixture 零写入。
- `reports_out_of_batch_drift_read_only`: with skill PASS；without skill FAIL。skill lane 分别列出 `knowledge-building` 与 `platform-governance` 两组批次外 drift 的页面清单与建议目标节点并标为只读观察；baseline 完全没有提及。
- `loads_only_api_contract`: with skill PASS；without skill FAIL。skill lane 实际应用了 API 模块的嵌套层级、route grouping、原子 mapping closure 与 internal visibility 规则，并在固定报告中给出 `Loaded type modules: api` 和具体 `Hierarchy drift` 结论；baseline 两个字段都不存在。

## With-Skill Behavior

- 选择 feature delivery 模式，只加载 API 类型模块与 host API 模板。
- 在 Step 4 候选范围之前执行扁平层级 drift 检查，只读页面路径与 frontmatter，输出三组正向 drift 及其建议目标节点。
- 对本批次要写入的 `knowledge-discovery` 父节点给出一次性迁移提案：目标树、旧新路径映射、入链与递归导航修复、conversations 与 graph 两条 change-map entry 的闭包、排除项，以及新消息页在目标树中的位置。
- 因宿主未提供 redirect 机制，提案改为把两个旧路径保留为最小兼容页，而不是虚构 HTTP redirect。
- 给出「迁移 + 本批次一起确认（推荐）/ 仅确认本批次 / 全部暂缓」三个决策并等待确认，批次外两组 drift 保持只读。
- 对文档站零写入，未运行写后 read-back 与 host docs checks，未进入 docs-audit handoff；同时报告了实际 diff 缺失与本地无 `pytest` 两项证据缺口，未把未执行命令写成通过记录。

## Fresh Without-Skill Baseline

- Source: 本轮新生成的 `without_skill` lane，使用同一条 prompt 与同一份 pristine fixture；未读取目标 skill、Docs Agent README、`_internal/**`、仓库指导文件、历史 `comparison.md` 或 with-skill 输出。未复用任何历史 baseline。
- baseline 自行按 `feature_path` 推导出 `api/knowledge-discovery/conversations/` 嵌套路径，把新页面放在正确深度，明确不移动既有稳定页面，并守住零写入与范围排除边界。
- baseline 没有识别既有扁平 drift、没有迁移提案、没有批次外 drift 观察，也没有已加载模块与 Hierarchy drift 报告字段——即 issue #225 描述的沉默行为在无 skill 条件下被完整复现。
- Baseline result: **1/5**。

## Failures

- With-skill assertion failures: 无。
- Baseline failures: drift 识别、迁移提案、批次外 drift 只读报告、类型契约与 drift 报告字段。
- Infrastructure blockers: 无。两条 lane 均在缺少本地 `pytest` 的环境中如实报告该限制，未影响任一 assertion 的判定。

## Next Steps

- 保持 fixture 中「三个域各 2 页平铺 + 只确认新增一页」的结构：它同时考验触发（本批次域）与克制（批次外域），是本 eval 区分度的来源。
- 若后续放宽或收紧 drift 判定阈值，需重跑本 eval，确认 baseline 仍不会偶然满足 `detects_flat_hierarchy_drift`。

## Runtime Artifact Policy

- 两条 lane 的 fixture 副本、lane 输出、judge verdict 与运行日志保留在 `tmp/eval-runs/issue-225-20260805/` 与会话 scratchpad 中，不提交。
- 仅本 `comparison.md` 作为 durable result 提交；transcript、candidate output、verdict、timing、diagnostics 与生成站点均不入 git。
