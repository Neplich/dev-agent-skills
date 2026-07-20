# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-agent`
- Eval: `eval-003-route-release-audit`

## Test Set / Fixture Version

- Fixture version: `issue #117 cross-doc audit 2026-07-19`（fixture 未变化）
- 本轮触发：issue #131 将 `docs-audit` frontmatter description 扩展为同时覆盖 pre-tag release audit 与 post-tag release verification 后的 routing 复验（2026-07-20）
- Fresh run：仓库外隔离 scratch Git 仓库（session scratchpad `eval-131-e003/`）
- Source head: `6040de9`（#131 与 #132 合并后的 main）

## Latest Result

**PASS（3/3 assertions）** — with-skill 接受等效确认 release chain，正确路由 `docs-agent:docs-audit`，只引用 specialist 权威执行 gate；并基于 fixture 中的实际版本 tag 主动区分出 post-tag release verification 入口语义，说明新 description 的双阶段表述被 router 正确消费。

## Assertions

- `accepts_equivalent_chain`：PASS。逐项识别已确认 scope、`verified_version_tag: v0.4.0`、已审阅 changelog、契约/CI 证据与既有 `docs/site/` 为等效确认入口。
- `routes_docs_audit`：PASS。明确“选定 specialist：`docs-agent:docs-audit`”，保留版本与 release 证据，执行责任交给 specialist，router 停在 handoff。
- `references_audit_gate_only`：PASS。以“由 `docs-audit` 按其权威执行门禁自行核验”指向 specialist gate，未复制 base/target、确定性层、事实层、三态或统一盖章协议。

## With-Skill Behavior

- fresh candidate 读取 main 上当前 `docs-agent` router SKILL.md、Docs README 与 `docs-audit` 新 frontmatter description，仅做入口检查、分流与上下文保留。
- 额外观察：candidate 依据 fixture 提供的实际 tag 判断应进入 post-tag verification，而非 pre-tag audit——这是 #131 description 变更后的预期新语义。

## Without-Skill Baseline

- 来源：同一 prompt 与 pristine fixture 副本的本轮 fresh `without_skill`，在仓库外隔离 scratch Git 仓库运行，禁止读取宿主仓库、skill 文档与历史输出；未复用历史 baseline。
- baseline 能泛化识别审计意图，但路由到自拟的 “Release Documentation Specialist” 而非 canonical `docs-agent:docs-audit`，缺少权威 gate 指针，且复制了五项审计检查与 `ready`/`blocked` 输出协议，违反 router 只引用 gate 的边界。
- 独立 judge 确认 baseline 输出无 skill 文档污染迹象。

## Failures

- 无 with-skill assertion failure。
- 上一轮记录的 harness limitation（baseline 可见父仓库 git 状态）本轮已通过仓库外隔离 scratch Git 仓库消除。

## Next Steps

- 保持 router 只引用 specialist gate；后续 router 或 `docs-audit` 入口语义再变化时重新 fresh 验证。

## Runtime Artifact Policy

- candidate、baseline、judge verdict 与 transcript 仅保留在会话 scratchpad 的隔离 scratch 仓库中，不提交到 git。
