# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-site-bootstrap`
- Eval: `eval-001-bootstrap-empty-workspace`

## Test Set / Fixture Version

- Fixture: `issue-126-r3-assets-40-v1`
- Asset snapshot: PR #126 R3 工作树中的 40 项权威 bootstrap assets
- Fresh validation date: `2026-07-19`
- Execution cleanup: 隔离空宿主 `docs/site`

## Latest Result

**PASS（R3 fresh）** — 本轮全新 with-skill 执行、同 prompt/fixture 的全新 without-skill baseline 与 assertion judge 已完成。6 条 assertions 全部 PASS；新增 `package-lock.json` 与 `release-notes/README.md` 已纳入 inventory、manifest、read-back 和 zero-diff 检查。

## With-Skill Behavior

- 入口依据完整：prompt 明确确认当前 fixture 仓库、固定 `docs/site/` 根、完整 scaffold 与 manifest；缺少任一显式 opt-in 时必须在写入前停止。
- 从权威 assets 逐字节物化 40/40 个静态目标，另生成 1 个 runtime manifest；40 项 asset mismatch 为 0，manifest 的 `files` 覆盖 40 项且 disposition 均为 `created`。
- `package-lock.json` 与 `release-notes/README.md` 均已物化；17 个 Markdown 页面通过七字段 frontmatter checker，`doc_type`、数组字段和 `last_verified_version` 契约均通过。
- `package.json` 只有一个 `new:doc` 命令，scaffold 实现与测试存在；五个模板各含恰好一个 `docs-scaffold` 区块并全部由 `standards/index.md` 索引。
- 在隔离宿主执行 `npm ci --ignore-scripts` 后，`npm run test:docs` 全部通过：frontmatter、strict affected、version metadata 和 Node tests 73/73 通过。
- 排除运行期 `node_modules` 后，首次完成快照与再次完整分类后的 41 文件 SHA-256 清单一致；manifest `createdAt` 与 40 项持久状态不变，重复执行为 zero-diff。

## Without-Skill Baseline

- 来源：本轮全新 baseline，使用相同原始 prompt 与 cleanup 后空 fixture；生成时不读取或应用目标 skill、`_internal/INSTRUCTIONS.md`、Docs Agent README、旧 comparison 或 with-skill 结果。
- baseline 因 prompt 本身没有提供 packaged inventory、asset bytes 或 manifest 状态协议而停止写入，未臆造 scaffold；因此没有 40 项资产、规定的 manifest、Release Notes 规范、脚手架测试或 read-back 证据。
- baseline 保住了目标根边界，但不能满足完整资产与确定性 scaffold assertions；它仅作为本轮对照输入，不替代 with-skill 判定。

## Failures

- 无 assertion failure 或阻断项。
- `npm ci` 报告依赖树中 3 条 audit advisory（2 moderate、1 high），但安装退出码为 0，且 `npm run test:docs` 全绿；这不属于本 eval 的资产确定性或功能 assertion failure。

## Next Steps

- 保留本轮 fresh PASS。后续若 40 项 inventory、frontmatter 契约、脚手架行为或 manifest 状态机变化，重新生成同 prompt 的 fresh with/without validation。

## Runtime Artifact Policy

- 本轮隔离宿主、hash 快照、依赖安装与测试输出仅位于 `tmp/eval-runs/pr126-r3-20260719-1256/eval-001/`，不提交到 git。
- 长期提交结果仅为本 `comparison.md`；`node_modules`、responses、verdicts、日志和 diagnostics 均保持运行期隔离。
