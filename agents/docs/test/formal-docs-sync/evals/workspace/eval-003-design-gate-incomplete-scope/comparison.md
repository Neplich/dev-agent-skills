# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-003-design-gate-incomplete-scope`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `8aa9df65b73215302e91c3f000b2e01777ac5c79a5e42d477647ee57db58af66` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-003-design-gate-incomplete-scope`.
- Fixture SHA-256: `8aa9df65b73215302e91c3f000b2e01777ac5c79a5e42d477647ee57db58af66`
- Prompt SHA-256: `56246c4cc2593a4f68a5cab876eaee6a48761e04188d3c231558d5894f290174`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `52db6badcefada59a1d42e81de2581f06256f43c060b7699c281ab21bfb40949`
- Skill overlay SHA-256: `f896903fa1a8ae6886eb0b6365065625a2e60f6809acd0af6c7c8dc8f8f2bd40`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `b2bf4f8fb3d18226f8bc19c0ca91afcf8f927301ac6d8c89204f1fa6248c4f6b`
- Metadata SHA-256: `60fd8d12ce139674523c1a361254f5e8a91b8a162c74d8b2d6b08ca495888809`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_on_incomplete_scope` | PASS | with_skill 明确指出 SCOPE-02 compact summary rendering 仍为 TODO，属于本次 delivery scope，owner 为 Engineer，并要求完成实现与对应测试、更新完成态材料后重新发起同步。 |
| `design_zero_change` | PASS | with_skill 明确报告未修改 docs/site/design/** 或 change-map；其 git_status 与 git_diff 均为空，证明 design 原子范围零变化。 |
| `no_tentative_design` | PASS | with_skill 在门禁失败时未生成 provisional/tentative/planned/future-state 或部分设计正文，明确表示暂不能更新页面，并未将 compact rendering 描述为当前能力。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=56246c4cc2593a4f68a5cab876eaee6a48761e04188d3c231558d5894f290174; fixture_sha256=8aa9df65b73215302e91c3f000b2e01777ac5c79a5e42d477647ee57db58af66; output_sha256=e40573b560e51269084a82a1b26fdedfcc5ed1eca33ec5249a1099ffc23c5027; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确核验交付材料，因 SCOPE-02 未完成而阻断同步，并保持 design 范围零变化。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=56246c4cc2593a4f68a5cab876eaee6a48761e04188d3c231558d5894f290174; fixture_sha256=8aa9df65b73215302e91c3f000b2e01777ac5c79a5e42d477647ee57db58af66; output_sha256=d83ec041838372003aa484f8eaa0e98b5f84fcc9c8a180288aedfd70ef96497c; snapshot_sha256=6aed83c00679e9b98b1f66a13b7a2f9089f169f78f7759eae60953680d6497b6
- Behavior: 错误地宣称同步完成，并实际修改了 design 页面和 change-map。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-003-design-gate-incomplete-scope`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `8aa9df65b73215302e91c3f000b2e01777ac5c79a5e42d477647ee57db58af66` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-003-design-gate-incomplete-scope`.
- Fixture SHA-256: `8aa9df65b73215302e91c3f000b2e01777ac5c79a5e42d477647ee57db58af66`
- Prompt SHA-256: `56246c4cc2593a4f68a5cab876eaee6a48761e04188d3c231558d5894f290174`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `1e290565a84b926a128928ccdd91365a2235adff18f999307c0a3553f0b41f34`
- Skill overlay SHA-256: `0c6a49eed1db242a95632eb0d142c1760f60ffc995c96026908ec8c0e6bd8d63`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `b2bf4f8fb3d18226f8bc19c0ca91afcf8f927301ac6d8c89204f1fa6248c4f6b`
- Metadata SHA-256: `60fd8d12ce139674523c1a361254f5e8a91b8a162c74d8b2d6b08ca495888809`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_on_incomplete_scope` | PASS | with_skill 明确指出 SCOPE-02 compact rendering 仍为 TODO、属于当前交付范围，Owner 为 Engineer，并要求完成实现及对应测试后重新提交 Docs 同步。 |
| `design_zero_change` | PASS | with_skill 报告未修改正式文档或 change map；Changed docs 为无，且 git_status 与 git_diff 均为空。 |
| `no_tentative_design` | PASS | with_skill 在阻断状态下未生成设计正文，仅说明现有设计与实现不一致，明确不能发布部分完成态设计。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=56246c4cc2593a4f68a5cab876eaee6a48761e04188d3c231558d5894f290174; fixture_sha256=8aa9df65b73215302e91c3f000b2e01777ac5c79a5e42d477647ee57db58af66; output_sha256=632e60ff9642c6c33eac0910a08b4bb727fa8fe495d40af44c814f0c2a88b2ff; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 核验完成态材料后识别 SCOPE-02 未完成，阻断同步并保持 design 原子范围零变化。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=56246c4cc2593a4f68a5cab876eaee6a48761e04188d3c231558d5894f290174; fixture_sha256=8aa9df65b73215302e91c3f000b2e01777ac5c79a5e42d477647ee57db58af66; output_sha256=65934e036538d27690a9b6ecaa7c6fa558367cd4e6e881863b61f7c98786a6be; snapshot_sha256=278bec4873f9853b5b3caa7d2ead57363a8f4c68a2c4431966e7aac95b9c6940
- Behavior: 完成了 design 与 change-map 修改，虽指出 SCOPE-02 未实现，但未因未完成范围阻断同步。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-003-design-gate-incomplete-scope`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `8aa9df65b73215302e91c3f000b2e01777ac5c79a5e42d477647ee57db58af66` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-003-design-gate-incomplete-scope`.
- Fixture SHA-256: `8aa9df65b73215302e91c3f000b2e01777ac5c79a5e42d477647ee57db58af66`
- Prompt SHA-256: `56246c4cc2593a4f68a5cab876eaee6a48761e04188d3c231558d5894f290174`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `79b2ff102fa24fa224c9f24f44f3e648a1ae7eb9a7a10e639d8675db4454120a`
- Skill overlay SHA-256: `52a3ba7ee2d9485acf003417b40e0d0ca2ab263cbadde98fac58250b6c2a9778`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `b2bf4f8fb3d18226f8bc19c0ca91afcf8f927301ac6d8c89204f1fa6248c4f6b`
- Metadata SHA-256: `60fd8d12ce139674523c1a361254f5e8a91b8a162c74d8b2d6b08ca495888809`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_on_incomplete_scope` | PASS | With-skill output identifies SCOPE-02 as TODO, states Engineering must implement it and add passing tests before resubmitting synchronization; fixture evidence confirms it is in scope and owned by Engineer. |
| `design_zero_change` | PASS | With-skill output names both required design files as unmodified and reports empty git status/diff; locked git evidence confirms zero changes. |
| `no_tentative_design` | PASS | With-skill lane remains blocked, performs no writes, and generates no provisional, tentative, planned, future-state, or current-state compact-rendering design content. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=56246c4cc2593a4f68a5cab876eaee6a48761e04188d3c231558d5894f290174; fixture_sha256=8aa9df65b73215302e91c3f000b2e01777ac5c79a5e42d477647ee57db58af66; output_sha256=b986317f8ee9bd28d38c6da924aaf53c58f229866d0bb9f2b7ed43b338628252; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly blocked synchronization, preserving both design files unchanged until SCOPE-02 is implemented and tested.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=56246c4cc2593a4f68a5cab876eaee6a48761e04188d3c231558d5894f290174; fixture_sha256=8aa9df65b73215302e91c3f000b2e01777ac5c79a5e42d477647ee57db58af66; output_sha256=d7da61cf53a10bf3f9a120b5514c134cbf4b40cd02443702e0a43308da4b8357; snapshot_sha256=5b86b8cd4b274be1dba7940b71630fdbe13801b8bda7b19dfaec6a5abe73de00
- Behavior: Fresh baseline incorrectly synchronized both design files despite incomplete SCOPE-02 scope.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
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
- Eval: `eval-003-design-gate-incomplete-scope`

## Test Set / Fixture Version

- Fixture: `issue-121-s2-final`
- Run date: `2026-07-19`

## Latest Result

- Overall result: PASS
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `PASS` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `blocks_on_incomplete_scope` | PASS | FAIL | with_skill 明确指出 `SCOPE-02` 为 TODO、属于本次交付，Owner 为 Engineer，并要求完成代码与对应测试后重新提供 closeout 证据；without_skill 虽识别 TODO 和交付未关闭，但未明确给出 owner、完成代码与验证后重新提交 closeout 的阻断要求。 |
| `design_zero_change` | PASS | PASS | 两条 lane 的 `.eval/actual-diff.patch` 均仅包含 `src/preferences_summary.py`；设计页与 change-map 的 SHA-1 均分别为 `dfcee25...` 与 `bed32d5...`，保持一致。with_skill 报告也明确为“Changed docs: 无”。 |
| `no_tentative_design` | PASS | PASS | 两条 lane 均未修改设计正文；实际 diff 没有 `docs/site/design/preferences-summary.md` 或设计性新增内容，也未将紧凑摘要描述为当前状态。 |

未满足断言（with/without 任一 FAIL）：``blocks_on_incomplete_scope``



## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 只加载 design 模块，识别实施计划仍有未完成范围。
- design 页面与 change-map 均零变化，并将解锁动作交回 Engineer / feature-implementor owner。

## Without-Skill Baseline
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- baseline 同样停止写入，但未明确指名 Engineer / feature-implementor owner。

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- with-skill 无 assertion failure。

## Next Steps

- design closeout gate 变化时重跑。

## Runtime Artifact Policy

- 运行期证据仅保留在 `tmp/eval-runs/121/`，不提交。
