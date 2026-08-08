# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-006-design-gate-all-passed`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `98bf611a541c8fe0137472ae23a2bee304eb1dd895062850790d9e776e872e75` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-006-design-gate-all-passed`.
- Fixture SHA-256: `98bf611a541c8fe0137472ae23a2bee304eb1dd895062850790d9e776e872e75`
- Prompt SHA-256: `c76b170dd7794d3734918c7a765e05580924d97e899b93480f8dc75124874544`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `79b2ff102fa24fa224c9f24f44f3e648a1ae7eb9a7a10e639d8675db4454120a`
- Skill overlay SHA-256: `52a3ba7ee2d9485acf003417b40e0d0ca2ab263cbadde98fac58250b6c2a9778`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `409f0dff74eed97473da7310514056fa3150a1bcc243e245700365b8124e237d`
- Metadata SHA-256: `d850062d9ab19e577fb519798bc20c97592f06bfa16acdff382b6c2af72957e7`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `passes_completion_gates` | PASS | with_skill 明确逐项报告六项门禁通过；原始 PRD、TRD、实施计划、diff 与测试记录分别确认这些条件。 |
| `stops_at_scope_confirmation` | PASS | with_skill 展示了设计页、代码范围、证据、排除范围和待确认事项，并明确请求维护者确认；锁定 git 证据显示站点未被修改。 |
| `current_state_only` | PASS | with_skill 候选内容与原始代码及测试一致：固定 language→timezone→theme 顺序、忽略空值、compact 复用相同有序非空值；未加入无证据的未来行为。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c76b170dd7794d3734918c7a765e05580924d97e899b93480f8dc75124874544; fixture_sha256=98bf611a541c8fe0137472ae23a2bee304eb1dd895062850790d9e776e872e75; output_sha256=63058b2147d40ff251d8251e768a397ddf2ba113986981d2472fda75585883bb; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完成六项门禁核对，保留候选范围确认步骤，明确页面、映射、证据、排除项和未决项，未修改站点。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c76b170dd7794d3734918c7a765e05580924d97e899b93480f8dc75124874544; fixture_sha256=98bf611a541c8fe0137472ae23a2bee304eb1dd895062850790d9e776e872e75; output_sha256=2e0b167240c0fb164ad24c28349919757660a48d3449549f4d08c601b4c71076; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 列出设计页并提出同步 change-map，但未充分核对六项完成门禁，范围与依据表达较粗。
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
- Eval: `eval-006-design-gate-all-passed`

## Test Set / Fixture Version

- Fixture: `issue-121-s2-final`
- Run date: `2026-07-19`

## Latest Result

- Overall result: PASS
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `PASS` / Coverage `FULL`
- without_skill：Behavior `PASS` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| passes_completion_gates | PASS | PASS | 两条 lane 的 `PRD.md` 为 Approved、`TRD.md` 为 Confirmed、实施计划为 Confirmed；SCOPE-01/02 均 Complete；`actual-diff.patch` 覆盖 `src/preferences_summary.py`；`test-results.md` 中三项计划测试均 PASSED。 |
| stops_at_scope_confirmation | PASS | PASS | 两条 lane 均展示候选页面 `docs/site/design/preferences-summary.md`、代码路径 `src/preferences_summary.py`、证据、排除项和阻断项，并明确等待维护者确认；`actual-diff.patch` 未包含页面或 change-map 修改。 |
| current_state_only | PASS | PASS | 两条 lane 的源码与测试共同证明固定顺序 `language → timezone → theme`、省略空值、compact 复用相同非空值；候选描述未添加无证据的未来行为或实施结果。 |

本轮无 FAIL 断言。



## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 七项 design closeout 证据全部通过后仍停在候选范围确认，不提前写入。
- 候选内容仅使用最终代码与通过测试支持的当前事实，并保持后续 `unverified` 纪律。

## Without-Skill Baseline
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 全新 baseline 在该明确 fixture 上同样满足 3/3。

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- with-skill 无 assertion failure。

## Next Steps

- closeout 条件或候选确认协议变化时重跑。

## Runtime Artifact Policy

- 运行期证据仅保留在 `tmp/eval-runs/121/`，不提交。
