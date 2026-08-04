# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-015-flat-hierarchy-migration-proposal`
- Review context: issue #225，为已有扁平文档补上迁移触发机制

## Test Set / Fixture Version

- Fixture: `workspace/eval-015-flat-hierarchy-migration-proposal`，含 `.eval/actual-diff.patch` 与 handoff 内的测试结果引用，feature delivery 入口证据链完整
- Scenario: 宿主 API 根下 6 个稳定页面按 feature catalog 分属三个一级功能域却全部平铺，本批次要同步一个属于其中一个域的新会话消息 API 页；维护者只确认了新页面同步，未确认任何路径迁移
- Evidence set: PM handoff、actual diff、feature catalog、Approved PRD、Confirmed TRD、完成态实施计划、路由与 schema 源码、contract tests、既有 change map（含手工未知字段条目）、现有扁平 API 页与 host standards
- Actual validation date: `2026-08-05`
- Isolation: 三条互相独立的全新 `codex exec` 会话——`with_skill`、`without_skill`、judge，符合 `AGENTS.md` 的 Eval runner 约束（隔离全新上下文 + 独立评审方）。两条 lane 复制同一份 pristine fixture（排除 `comparison.md` 与 `eval_metadata.json`）到 `tmp/eval-runs/issue-225-20260805-r2/` 下各自目录；`without_skill` lane 被显式禁止读取任何 agent skill 文档、Agent README、仓库指导文件与历史 eval 结果；judge 以只读会话独立核对零写入，不采信任一 lane 的自述

## Latest Result

- Behavior result: PASS
- Coverage result: FULL
- With skill 5/5；fresh without_skill baseline 0/5

Overall result: PASS

## Assertions

- `detects_flat_hierarchy_drift`: with skill PASS；without skill FAIL。skill lane 报告 `Hierarchy drift: positive` 并点名 `research-conversations.md` 与 `graph-search.md`，归类证据用 feature catalog、owner、`feature_path` 与 route prefix；baseline 把新页面放进 API 根并称之为「稳定扁平路径」，没有识别两页共同缺失的域节点。
- `proposes_migration_before_write`: with skill PASS；without skill FAIL。skill lane 给出逐级 `index.md` 目标树、两个旧路径到新路径的映射、入链与递归导航 delta、两条 change-map `required_docs` delta、排除项与三个决策选项；baseline 只有「根目录新页 + API 索引 + change map」的扁平候选，没有目标子树、路径映射或迁移决策面。
- `does_not_deepen_flat_layout`: with skill PASS；without skill FAIL。skill lane 明确即使选择「仅确认本批次」，新页面也落在目标深度、绝不追加到 API 根；baseline 本轮虽零写入，但候选方案准备把新页面追加为 `docs/site/api/conversation-messages.md`，会继续加深扁平结构。
- `reports_out_of_batch_drift_read_only`: with skill PASS；without skill FAIL。skill lane 分别列出两组批次外 drift 的页面清单与建议目标节点并声明不移动、不改 map、不扩为全站重构；baseline 只笼统排除「其他 API 功能」。
- `loads_only_api_contract`: with skill PASS；without skill FAIL。skill lane 报告 `Loaded type modules: api` 与 `Hierarchy drift` 结论并点名 host API template；baseline 两个字段都不存在。

## With-Skill Behavior

- 选择 feature delivery 模式，消费 `.eval/actual-diff.patch` 作为入口证据，只加载 API 类型模块与 host API 模板。
- 在 Step 4 候选范围之前执行扁平层级 drift 检查，只读页面路径与 frontmatter，输出本批次 positive drift 与两组批次外 drift。
- 对本批次要写入的 `knowledge-discovery` 父节点给出一次性迁移提案：目标树、旧新路径映射、入链与递归导航修复、conversations 与 graph 两条 change-map entry 的闭包、排除项，以及新消息页在目标树中的位置。
- 因宿主未提供 redirect 机制，提案把两个旧路径保留为最小兼容页，而不是虚构 HTTP redirect。
- 给出「迁移 + 本批次一起确认（推荐）/ 仅确认本批次 / 全部暂缓」三个决策并等待确认，批次外两组 drift 保持只读。
- 对文档站零写入，未运行写后 read-back 与 host docs checks，未进入 docs-audit handoff。

## Fresh Without-Skill Baseline

- Source: 本轮新生成的 `without_skill` lane，使用同一条 prompt 与同一份 pristine fixture；未读取目标 skill、Docs Agent README、`_internal/**`、仓库指导文件、历史 `comparison.md` 或 with-skill 输出。未复用任何历史 baseline。
- baseline 核对了证据链、停在范围确认、保持零写入，这些一般性谨慎行为都做到了。
- 但它主动选择把新页面追加为 `docs/site/api/conversation-messages.md`，理由是「沿用现有 API 宿主的稳定扁平路径」，并判定按 `feature_path` 建多级目录「超出 handoff 已确认边界」。既有扁平页面的 drift、迁移提案、批次外观察、已加载模块与 drift 报告字段全部缺失——issue #225 描述的沉默行为在无 skill 条件下被完整复现，且这一轮它还主动加深了扁平结构。
- Baseline result: **0/5**。

## Failures

- With-skill assertion failures: 无。
- Baseline failures: 全部 5 条。
- Infrastructure blockers: 无。judge 通过比对两条 lane 工作副本与 pristine fixture 的全量文件哈希（三份 `docs/site/` 哈希一致）独立确认零写入。

## Next Steps

- 保持 fixture 中「三个域各 2 页平铺 + 只确认新增一页」的结构：它同时考验触发（本批次域）与克制（批次外域），是本 eval 区分度的来源。
- 本 eval 未覆盖「父目录已存在、旧扁平页仍在根」这一回流场景的独立断言；该场景由 `_internal/INSTRUCTIONS.md` 的本批次判定条款覆盖，如需固化为回归保护，应新增独立 eval 而不是扩大本 eval 范围。

## Runtime Artifact Policy

- 两条 lane 的 fixture 副本、lane 输出、judge verdict 与运行日志保留在 `tmp/eval-runs/issue-225-20260805-r2/` 与会话 scratchpad 中，不提交。
- 仅本 `comparison.md` 作为 durable result 提交；transcript、candidate output、verdict、timing、diagnostics 与生成站点均不入 git。
