# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-001-sync-feature-api`

## Test Set / Fixture Version

- Fixture version: `issue #117 cross-doc audit 2026-07-19`
- Fresh run: `tmp/eval-runs/117-adjacent/formal-docs-sync/eval-001-sync-feature-api/`
- Source head: `00c9741dabc24f6b6df377c69c42adb989722648` plus the current issue #117 working tree

## Latest Result

**PASS（5/5 assertions）** — with-skill 仅同步命中的 Search API 页面，从代码与测试恢复当前事实，保留 change-map 人工条目并将页面置为 `unverified`。

## Assertions

- `updates_only_mapped_api_doc`：PASS。diff 只修改 `docs/site/api/search.md`，database 与其他页面零变化。
- `extracts_current_api_facts`：PASS。记录 `GET /api/search`、必填 `q`、可选 `limit` 和 400 `invalid_query`，不延续旧路径。
- `merges_map_without_deleting_unknown`：PASS。现有映射无需文本变更，`plugins/manual/**` 及其 trigger/exclude 保留。
- `keeps_confirmed_type_scope`：PASS。识别五类型能力但本轮只读取 API 模块、API 模板与目标证据，没有读取其他类型模块内容。
- `marks_changed_page_unverified`：PASS。页面写成 current state，`last_verified_version: unverified`。

## With-Skill Behavior

- 锁定安装后在 `docs/site/` 真实执行 `npm run test:docs`，73/73 通过。
- 因缺少维护者确认的 `target_release_version`，#117 pre-tag handoff 正确 blocked，不从分支或 ref 推测版本。

## Without-Skill Baseline

- 来源：同一 prompt 与 pristine fixture 的本轮 fresh `without_skill`；不含目标 skill、Docs README、旧 comparison 或 with-skill 输出，未复用历史 baseline。
- baseline 完成主要 API 内容与宿主检查，但没有建立“五类型能力下只加载 API 模块”的 progressive-loading 证据，也仅静态核证 Python 测试。

## Failures

- 无 with-skill assertion failure。
- Harness limitation：baseline 的父仓库 Git 命令可见文件名/状态，未读取目标 skill 或 README 内容；未影响目标页面、类型加载与 handoff 判断。后续应隔离 scratch Git 元数据。

## Next Steps

- 保持单类型 progressive loading、`unverified` 与无确认版本时 blocked 的回归门禁。

## Runtime Artifact Policy

- workspace 副本、依赖、candidate、transcript、manifest、diff 与状态仅位于 `tmp/eval-runs/117-adjacent/`，不提交到 git。
