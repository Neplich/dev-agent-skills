# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-site-bootstrap`
- Eval: `eval-003-block-bootstrap-conflict`

## Test Set / Fixture Version

- Fixture: `issue-122-assets-conflict-v1`，本轮 omitted assumption 已对齐 40 项 inventory
- Asset snapshot: PR #126 R3 工作树中的 40 项权威 bootstrap assets
- Fresh validation date: `2026-07-19`
- Fixture correction: `docs/site/package.json` 恢复 strict affected 命令并与当前权威 asset 字节对齐；未改变唯一预期冲突或 assertions

## Latest Result

**PASS（R3 fresh）** — 本轮全新 with-skill、同 prompt/fixture 的全新 without-skill baseline 与 assertion judge 已完成。`blocks_on_complete_conflict_list`、`does_not_overwrite_conflict`、`offers_explicit_resolution_choices` 三条 assertions 全部 PASS；40 项 inventory 下冲突 gate 行为不变。

## With-Skill Behavior

- 修复 fixture 漂移后，对 40 项静态 inventory 完整只读分类：37 个 missing、2 个 `skipped-identical`、1 个 conflict。
- 唯一冲突仍为宿主定制的 `docs/site/standards/index.md`；`package.json` 与 `.meta/releases.json` 均为 `skipped-identical`，新增 `package-lock.json` 与 `release-notes/README.md` 正确落在 missing 清单。
- 冲突文件前后 SHA-256 均为 `e5d8cccfa9cebeb2a16d191b58b709b67fd3b7b9fa412d4a7789e8e03cfbadfa`；manifest 前后 SHA-256 均为 `f9965422325e34c452ab3d07a21c6ea133d1bbc521160b75cf4f8cb0beccc0f7`。
- Manifest 只保留 package 与 releases 的两个 `skipped-identical` 状态，没有为冲突路径制造成功或 `kept-as-is` 状态；整个 fixture 前后文件 hash 清单一致。
- 明确 blocked 于用户逐文件选择，并提供 overwrite、显式 merge、keep 三类选择；只有用户选择 keep 后才可登记 `kept-as-is`。

## Without-Skill Baseline

- 来源：本轮全新 baseline，使用相同原始 prompt、修复后的 fixture 与 `fixture-scope.json`；明确不读取或应用目标 skill、内部指令、Docs Agent README、旧 comparison 或 with-skill 结果。
- baseline 能从 `known_conflict` 识别 `standards/index.md` 并保守停止写入，也给出 overwrite、merge、keep 三类选择。
- baseline 仅概括其余目标为 missing 或 identical，不能独立构建 40 项权威 inventory、逐项分类或说明 manifest disposition 的持久化边界；它不替代 with-skill 的 assertion 判定。

## Failures

- 无 assertion failure 或阻断项。
- 执行前发现并修复了一个 fixture 漂移：`package.json` 缺少 strict affected 参数会制造第二个非预期冲突。修复仅恢复与权威 asset 的字节一致性，未弱化 known conflict 或 assertions；修复后重新从同一 fixture fresh 执行 with/without。

## Next Steps

- 保留本轮 fresh PASS。真实 bootstrap 遇到同类冲突时继续等待用户逐文件选择；选择前不得覆盖、合并、格式化冲突文件或登记成功状态。
- 后续若 inventory、冲突分类或 manifest 状态机变化，重新生成同 prompt 的 fresh with/without validation。

## Runtime Artifact Policy

- 本轮隔离 fixture 副本、hash 快照、分类输出与 verdict 仅位于 `tmp/eval-runs/pr126-r3-20260719-1256/eval-003/`，不提交到 git。
- 长期提交结果仅为本 `comparison.md` 与本轮授权修复的 fixture `package.json`；responses、verdicts、日志和 diagnostics 均保持运行期隔离。
