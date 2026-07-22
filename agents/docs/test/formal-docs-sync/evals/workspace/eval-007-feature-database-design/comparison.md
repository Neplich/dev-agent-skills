# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-007-feature-database-design`
- Mode / types: feature delivery / Database + Design

## Test Set / Fixture Version

- Fixture version: `issue-160 design information architecture v3`
- Evidence: Approved PRD、Confirmed TRD、已关闭计划、actual diff、可执行
  pytest fixture、schema、invitation service、membership repository 与 audit writer
- Fresh paired run:
  `tmp/eval-runs/pr-165-review-round3d-20260722-210000/eval-007/`
- Actual validation date: `2026-07-22`

## Latest Result

**PASS（with-skill 8/8；fresh without-skill 6/8）** — 全新 paired judge
确认 with-skill 已逐页执行七项 Design Delivery Closeout Gate，并在正式写入前固化
运行期矩阵；每个相关 `code_glob` 也分别包含页面、互链面和全部已变更祖先
index 的原子映射闭包。两条 lane 的 required pytest 均为 4/4，宿主检查均为
74/74。

## Assertions

- `loads_only_database_design_contracts`: with-skill PASS；without-skill FAIL。
  只有 with-skill 有 common、Database 与 Design 模块的实际加载证据。
- `passes_design_closeout_gate`: 两边 PASS。两条 lane 均在正式写入前生成未覆盖的
  runtime-only `sync-report.md`，包含 9 个拟写 Design 页面 × 7 项门禁的逐页证据、
  生成时间和写前 clean changed-path 状态。
- `synchronizes_database_current_state`: 两边 PASS。Database 页面准确记录组合唯一、
  允许角色、必填时间、逻辑引用及不存在物理外键。
- `creates_domain_component_flow_tree`: 两边 PASS。系统/领域索引、组件、唯一流程、
  授权边界与兼容入口完整。
- `keeps_reciprocal_and_authority_links`: 两边 PASS。组件和流程双向链接，Design 只链接
  API/Database 权威页而不复制完整 contract。
- `keeps_cross_domain_authority_unique`: 两边 PASS。邀请接受流程只有一份权威正文，
  Audit Log 通过链接引用。
- `updates_atomic_map_and_unverified_pages`: with-skill PASS；without-skill FAIL。
  with-skill 对每个相关 glob 单独纳入叶子/兼容页、互链面、Design 根、各级已变更
  祖先 index 及 Database 祖先/权威页；without-skill 只在整体并集上看似覆盖，逐条
  mapping 闭包仍有缺口。未知 `plugins/manual/**` 条目均被保留，所有改页均为
  `unverified`。
- `runs_host_checks_and_handoffs_audit`: 两边 PASS。宿主检查和 #117 handoff 均完整。

## With-Skill Behavior

- 只加载 common contract 与 Database、Design 类型模块。
- 在任何 `docs/site/**` 或 change-map 写入前固化逐页七项 closeout matrix；写后未
  覆盖该运行期证据。
- 生成准确的 Database 当前事实、已确认 Design 分层、双向互链、唯一跨领域权威页。
- 按每个 `code_glob` 生成完整原子 mapping closure；共享祖先在相关 mapping 中重复
  显式出现，而不是依赖其他 mapping 的并集。

## Fresh Without-Skill Baseline

- Source: 同一 prompt、fixture、metadata、完整 evals 与 assertions 的全新 pristine
  copy；不包含或读取目标 skill、with-skill 输出、旧 comparison 或历史 baseline。
- Result: 6/8 PARTIAL。页面内容、逐页 closeout 与测试能够通过，但缺少目标类型模块
  加载证据，且逐 `code_glob` 的原子映射闭包不完整。
- Skill-specific uplift: +2 assertions，即 +25 percentage points。

## Required Test Reproduction

全新 judge 在两条原 lane 根目录分别运行：

`PYTHONDONTWRITEBYTECODE=1 uv run --with pytest python -m pytest tests/test_workspace_access.py -q -p no:cacheprovider`

- with-skill: exit `0`，`4 passed`
- without-skill: exit `0`，`4 passed`

judge 还在两条 lane 的只读临时副本中分别运行：

`GITHUB_BASE_SHA=HEAD npm run test:docs`

- with-skill: exit `0`，Node `74 passed, 0 failed`
- without-skill: exit `0`，Node `74 passed, 0 failed`

## Failures

- With-skill: 无；8 条 assertions 全部通过。
- Without-skill: `loads_only_database_design_contracts`、
  `updates_atomic_map_and_unverified_pages`。

## Next Steps

- 当前 eval 无待修复 assertion；保留逐页写前证据与逐 mapping closure 作为后续回归
  门禁。

## Runtime Artifact Policy

- 两条 lane、依赖、candidate outputs、judge verdict、日志和临时测试副本只保留在
  `tmp/eval-runs/` 或 `/tmp`，不提交。
- 仅本 `comparison.md` 为 durable result；不提交 `with_skill/`、`without_skill/`、
  transcript、verdict、timing、diagnostics、dependency、generated-site 或 cache artifact。
