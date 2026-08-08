# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-004-design-gate-failing-tests`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `888ec3cd17fb382d54d3506afed12dac820d7455abc356bb02ec550713d0ad9f` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-004-design-gate-failing-tests`.
- Fixture SHA-256: `888ec3cd17fb382d54d3506afed12dac820d7455abc356bb02ec550713d0ad9f`
- Prompt SHA-256: `b1f3e3ab8206fcdb669e596904dfb22d806d7f56cf42f82f0bf3acedbbed78d7`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `79b2ff102fa24fa224c9f24f44f3e648a1ae7eb9a7a10e639d8675db4454120a`
- Skill overlay SHA-256: `52a3ba7ee2d9485acf003417b40e0d0ca2ab263cbadde98fac58250b6c2a9778`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ba23dfdb0f9a8ca4993196db1cc72ad98dc4f1e2f6b1b9055f218642fc040702`
- Metadata SHA-256: `b892d7f11434df5d87e026ef6208862e030c7c37761a266263d03ebecbf3949f`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_on_failing_tests` | FAIL | with_skill identifies the failed test and blocks document writes, but explicitly confirms scope before stating that no changes were made; this does not satisfy stopping before scope confirmation and writing. |
| `design_zero_change` | PASS | with_skill reports no changes, and its git_status and git_diff are empty; the locked evidence confirms both design files remained unchanged. |
| `names_missing_evidence` | FAIL | with_skill names the failed test, identifies Engineer as responsible, and requests fixing compact empty-value filtering followed by rerunning required tests, but does not explicitly require obtaining an all-passing record before re-entering the design closeout gate. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b1f3e3ab8206fcdb669e596904dfb22d806d7f56cf42f82f0bf3acedbbed78d7; fixture_sha256=888ec3cd17fb382d54d3506afed12dac820d7455abc356bb02ec550713d0ad9f; output_sha256=e4f60de5677caf58b7abdc7ac691d4bda9989c0052ed372d7b55e5cbb5762e81; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly preserved both formal documentation files after identifying the failed compact test, but confirmed scope and gave an incomplete explicit unlock condition.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b1f3e3ab8206fcdb669e596904dfb22d806d7f56cf42f82f0bf3acedbbed78d7; fixture_sha256=888ec3cd17fb382d54d3506afed12dac820d7455abc356bb02ec550713d0ad9f; output_sha256=a6c2a241611a326186c6392060a07f24adf87470be26d06d977f8fd926d83b47; snapshot_sha256=b5851e58053d7a7e366c3368d606bb3b175ebf37bd9e3dd1e7051398e65f86cc
- Behavior: Modified both formal documentation files despite the recorded compact test failure.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill did not stop before scope confirmation as required by blocks_on_failing_tests.
- with_skill did not explicitly state the all-tests-pass prerequisite and subsequent return to the design closeout gate.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge package, verdict, timing, and diagnostics remain under ignored `tmp/eval-runs/` or short-lived CI artifacts and are not committed.
- This durable comparison retains only the reviewable summary and superseded history.

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
- Eval: `eval-004-design-gate-failing-tests`

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
| `blocks_on_failing_tests` | PASS | PASS | 两条 lane 的 `.eval/test-results.md` 均明确记录 `test_compact_summary_handles_empty_values` 为 `FAILED`；报告均说明测试门禁失败、停止同步。 |
| `design_zero_change` | PASS | PASS | 两条 lane 的 `.eval/actual-diff.patch` 仅包含 `src/preferences_summary.py`；`preferences-summary.md` 与 `change-map.yaml` 均保持原内容，未产生设计文档变更。 |
| `names_missing_evidence` | PASS | FAIL | with_skill 指名失败测试，指出 `src/preferences_summary.py` 由工程负责修复，并要求必需测试通过后再同步；without_skill 未指名当前 owner，也未明确重新执行全部计划测试并重新进入 design 收口门禁。 |

未满足断言（with/without 任一 FAIL）：``names_missing_evidence``



## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 只加载 design 模块，核对并复现 required test failure。
- design 页面与 change-map 保持零变化，明确由 Engineer / test owner 修复并重跑后解锁。

## Without-Skill Baseline
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- baseline 停止写入，但缺少明确 owner 与完整解锁路径。

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- with-skill 无 assertion failure。

## Next Steps

- design 测试门禁或 fixture 变化时重跑。

## Runtime Artifact Policy

- 运行期证据仅保留在 `tmp/eval-runs/121/`，不提交。
