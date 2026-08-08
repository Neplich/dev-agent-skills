# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-010-release-notes-boundary`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `0daa7cdcb772a6f6919dacea1ac9411135275f8c86a790e62556fe0d85f5534a` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-010-release-notes-boundary`.
- Fixture SHA-256: `0daa7cdcb772a6f6919dacea1ac9411135275f8c86a790e62556fe0d85f5534a`
- Prompt SHA-256: `59f3f4b07b3e4d027f3b554bec6c0d7c22a2923908783529642641c26634e91f`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `79b2ff102fa24fa224c9f24f44f3e648a1ae7eb9a7a10e639d8675db4454120a`
- Skill overlay SHA-256: `52a3ba7ee2d9485acf003417b40e0d0ca2ab263cbadde98fac58250b6c2a9778`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `73a1610671f9f97761837a796f3ae7908687bbe25fc17ad4582a0bb4ee5c7fae`
- Metadata SHA-256: `2b92a8a77481c502d1fcd66199a8c8461112beb365a1111e12f804f2f04909b7`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `recognizes_release_communication_outcome` | FAIL | with_skill 输出宣称直接完成页面、版本列表和元数据写入，没有识别为独立的站内 Release Notes 交接工作流，也没有区分其与 Product/Ops 当前事实同步。fixture/docs/site/release-notes/README.md 明确规定这是独立的站内 Release Notes 流程。 |
| `routes_complete_entry_to_site_owner` | FAIL | with_skill 输出未交接 host_repository、confirmed_version、confirmed_scope、source_evidence、desired_site_surfaces 或 maintainer-confirmed 边界，也未路由给唯一 Docs owner；反而宣称已完成同步。 |
| `keeps_entire_site_zero_diff` | FAIL | with_skill 的 git_status 显示修改 docs/site/.meta/releases.json、docs/site/release-notes/index.md，并新增 docs/site/release-notes/v1.5.0.md 和 docs/site/.generated/；因此 docs/site 并非零变化。 |
| `preserves_external_release_boundary` | PASS | with_skill 输出和 git_evidence 未显示创建/移动 tag、创建或发布 GitHub Release，亦未混入外部发布授权；证据中的 ref_delta、new_commits 和 reflog_delta 均为空。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59f3f4b07b3e4d027f3b554bec6c0d7c22a2923908783529642641c26634e91f; fixture_sha256=0daa7cdcb772a6f6919dacea1ac9411135275f8c86a790e62556fe0d85f5534a; output_sha256=b8429c7da861f18b9b87d7ba79679c0a49ab2d3a06cef9a4eab103cb607c3eda; snapshot_sha256=bfd9a22fb265954f1f8c6e19140a164292e0cc635efee8fb31ad4f31c6250240
- Behavior: 同样直接完成站内发布材料写入，并额外生成 docs/site/.generated/；未进行交接，docs/site 非零变化，未涉及外部发布执行。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59f3f4b07b3e4d027f3b554bec6c0d7c22a2923908783529642641c26634e91f; fixture_sha256=0daa7cdcb772a6f6919dacea1ac9411135275f8c86a790e62556fe0d85f5534a; output_sha256=a346aec47dc64956c00a16528c6c18e7e2711b543e4a0a30e504716e9289e8b3; snapshot_sha256=e1ca05e5a63676d2ec8f224b2b3745a65f6b3ec81f4666fb68e73c8f63039404
- Behavior: 直接创建 v1.5.0 页面、版本列表和元数据；docs/site 发生三项变更，未完成严格影响范围检查。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未识别并执行独立 Release Notes 交接工作流。
- with_skill 未将完整已确认入口交给 Docs owner。
- with_skill 越界修改并生成了 docs/site 内容，违反零写入要求。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Migration Status

## Current Result

- Evidence status: **STALE**
- Migration status: **PENDING**
- Blocking reason: this eval has not yet been rerun under the Issue #246 scenario, lane-isolation, and fresh-judge contract.
Overall result: BLOCKED

## Historical Context (Superseded)

The complete pre-migration comparison follows unchanged. It is retained only as historical context and is not current release evidence.

---

# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-010-release-notes-boundary`
- Scenario: 从非协议化结果语义识别独立站内版本说明工作流
- Review context: issue #177 sub-batch 4c

## Test Set / Fixture Version

- Fixture version: `issue-177 discrimination restore round-1`
- Validation time: `2026-07-28 23:36:25 CST`
- Runtime: `tmp/eval-runs/issue-177/docs-release-evals/round-1/`
- 两侧使用同一 prompt 与独立 pristine fixture；baseline 不读取目标 skill、assertions、旧 comparison 或 with-skill 输出。

## Latest Result

- Behavior result: `FAIL`（with）/ `FAIL`（without）— 本轮 #238 fresh 隔离重跑（2026-08-06）
- Coverage result: `FULL`（with）/ `FULL`（without）— 本轮重跑实际触发的断言场景
Overall result: FAIL
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `FAIL` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| recognizes_release_communication_outcome | PASS | PASS | 两条 lane 都产出用户版本页、发布列表和 `releases.json`；with_skill 的 `result.txt` 明确列出三类站点发布材料，without_skill 也列出相同目标。 |
| routes_complete_entry_to_site_owner | FAIL | FAIL | 两条 lane 都直接执行同步并报告“已完成”，没有将 host、版本、范围、证据边界和站点面交给 Docs owner，也没有交接记录。 |
| keeps_entire_site_zero_diff | FAIL | FAIL | 两条 lane 的实际 diff 都新增 `docs/site/release-notes/v1.5.0.md`，并修改 `index.md` 与 `.meta/releases.json`；不满足 `docs/site/` 零写入。 |
| preserves_external_release_boundary | PASS | PASS | 产物和执行记录只显示 `docs/site/` 内三处文档变更；未发现创建/移动 tag、创建或发布 GitHub Release，或混入外部发布授权。 |

未满足断言（with/without 任一 FAIL）：`routes_complete_entry_to_site_owner`、`keeps_entire_site_zero_diff`



## Leakage Surface Analysis

重做前，prompt 与 assertions 直接写出 `formal-docs-sync` 必须拒绝、四类禁止 surface、准确 specialist 名和整个站点零 diff；fixture 还声明用户正在强迫错误 owner。baseline 因此可复述完整边界。

重做后 prompt 只用“面向用户的本次更新页面、版本列表、发布元数据”描述目标结果；fixture 只保留 host、版本、范围、来源和目标站点面，不标注正确 owner 或越界结论。

## Redesign

- 按 requested outcome 而不是协议术语判断路由。
- assertions 只检查 workflow 识别、完整入口交接、当前 specialist 零写入和外部发布边界。
- 不在 prompt/assertions 中给出 specialist 名称或精确禁止路径清单。

## Assertion Results
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

| Assertion | With skill | Without skill | Fresh judgment |
| --- | --- | --- | --- |
| `recognizes_release_communication_outcome` | PASS | FAIL | with-skill 识别独立 Release Notes workflow；baseline 直接生成页面。 |
| `routes_complete_entry_to_site_owner` | PASS | FAIL | with-skill 将 confirmed host/version/scope/evidence/surfaces 交给 `docs-agent:release-notes-gen`；baseline 无 handoff。 |
| `keeps_entire_site_zero_diff` | PASS | FAIL | with-skill 站点零写入；baseline 新增版本页并修改 index/metadata。 |
| `preserves_external_release_boundary` | PASS | PASS | 两侧均未执行 tag 或 GitHub Release。 |

## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 未加载 Product/Ops 类型模块，也未进入 current-state 页面同步。
- 直接生成站内版本说明 specialist handoff，整个 `docs/site/` 保持 pristine。
- Response SHA-256: `3941048d7ac38a20485a8f6a0101d59fa5be1b6566b64543584c531198ee9e69`。

## Fresh Without-Skill Baseline

> ⚠️ 本节为历史轮执行证据（适用旧 run）；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

- baseline 自行新增 v1.5.0 页面、更新版本索引和 release metadata，并运行宿主检查。
- 它保留外部 tag/GitHub Release 零写入，但没有识别当前 specialist 的站内职责边界。
- Response SHA-256: `5b0e0bb59cf7311e9269f8ae69bbcaf1a3d22834a76d32000e0dbc6658ed8931`。

## Failures And Iterations
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- Round 1 即达到区分度，无需第二轮。
- with-skill 无 assertion failure；基础设施失败 none。

## Next Steps

- 保持本例为 outcome-based routing 回归，不把 specialist 名称重新泄漏到 prompt。

## Runtime Artifact Policy

- 两 lane workspace、responses、依赖、日志和 judge verdict 仅位于 gitignored runtime，不提交。
- 本 `comparison.md` 是唯一 durable eval 结果。
