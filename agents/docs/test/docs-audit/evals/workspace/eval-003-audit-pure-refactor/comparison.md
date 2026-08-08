# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-003-audit-pure-refactor`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `a0071569c74867aaacfda16310f9f4a06e50a375aa0e6b62ee25e801db096677` from `agents/docs/test/docs-audit/evals/workspace/eval-003-audit-pure-refactor`.
- Fixture SHA-256: `a0071569c74867aaacfda16310f9f4a06e50a375aa0e6b62ee25e801db096677`
- Prompt SHA-256: `20617e4b8714b5129b537177e8c463822eec4083d7fdd0d6520c27013f94489f`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2baee6e542351d5b0c46e79c685dd29ff93f0fee4a45cf4485afee7656248cf7`
- Skill overlay SHA-256: `a2871f547194089c5425585467f9bee6e3c85ea103d77933d85a4c4cf246fa7c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `a7212e3282f2eaaa660e0675fb965d5050f366a07c153f3821d78fdab8976de5`
- Metadata SHA-256: `1e20c97bb5ffc477023f6bbbd217e71d747297cb0b8f52652660b6b2d10adc7a`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `sends_refactor_suspect_to_fact_layer` | PASS | with_skill identifies the affected, unchanged API page and explicitly reports that the fact layer checked it, concluding verified rather than directly passing or marking it stale. |
| `classifies_accurate_refactor_verified` | PASS | with_skill states that GET path, optional limit, 200/400 responses, error structure, and transport behavior remain accurate, with page conclusion verified. |
| `does_not_force_noop_doc_edit` | PASS | with_skill treats the change as an implementation-only refactor with no API contract change and does not perform a documentation or version-stamp edit. |
| `does_not_block_for_unchanged_accurate_doc` | PASS | with_skill does not mark the accurate page stale; its blocked status is attributed to missing Release Notes, version index, releases.json, version-source inventory, and pre-tag handoff evidence, and it does not return ready_for_tag or stamp the release. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=20617e4b8714b5129b537177e8c463822eec4083d7fdd0d6520c27013f94489f; fixture_sha256=a0071569c74867aaacfda16310f9f4a06e50a375aa0e6b62ee25e801db096677; output_sha256=4acac3f10f391c48e50bbb30b62517a634172f8e42490b2dc01bea38f92e225f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Routes the unchanged page through fact checking, verifies its contract, avoids a no-op documentation edit, and blocks only for missing release-version surface evidence.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=20617e4b8714b5129b537177e8c463822eec4083d7fdd0d6520c27013f94489f; fixture_sha256=a0071569c74867aaacfda16310f9f4a06e50a375aa0e6b62ee25e801db096677; output_sha256=e215bc71fe576e33bcc2bcdaee8d89c10d6561226fae93a3e266ef870f7d1d5d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly recognizes the API as unchanged and accurate, but recommends updating the verification version and does not report the required blocked release-audit conclusion.
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

- Skill: `docs-audit`
- Eval: `eval-003-audit-pure-refactor`

## Test Set / Fixture Version

- Fixture version: docs-audit A2 / 2026-07-19
- Assertions: 4

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
| `sends_refactor_suspect_to_fact_layer` | PASS | FAIL | with_skill 明确写明页面“先列为 `suspect`；复核后确认”；without_skill 直接称“审计结论：通过”，未将未更新页面交给事实层。 |
| `classifies_accurate_refactor_verified` | PASS | FAIL | with_skill 最终明确标为 `verified`，并核对了 GET、limit、200、400 等事实；without_skill 仅称页面“当前内容仍准确”，没有 `verified` 的事实层结论。 |
| `does_not_force_noop_doc_edit` | PASS | PASS | 两条 lane 均明确说明纯实现重构无需更新 API 页面。 |
| `does_not_block_for_unchanged_accurate_doc` | PASS | PASS | 两条 lane 均未将页面判为 `stale`；with_skill 仅因缺少 Git 元数据而不能签发 `ready_for_tag`，without_skill 也未返回 `ready_for_tag` 或盖章。 |

未满足断言（with/without 任一 FAIL）：``sends_refactor_suspect_to_fact_layer``、``classifies_accurate_refactor_verified``



## Assertion Results
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

| Assertion | Result | Evidence summary |
| --- | --- | --- |
| `sends_refactor_suspect_to_fact_layer` | PASS | change-map 命中且文档未同批更新时先标 `suspect`，继续事实核对。 |
| `classifies_accurate_refactor_verified` | PASS | GET 路径、limit、200、400、鉴权、流式和文件行为逐项与代码一致，页面 `verified`。 |
| `does_not_force_noop_doc_edit` | PASS | 报告明确实现重构未改变 API，无需为同 diff 编辑准确文档。 |
| `does_not_block_for_unchanged_accurate_doc` | PASS | 页面未因“未修改”判 stale；整体只因 `docs-agent:release-notes-gen` handoff、Release Notes、索引、metadata 和宿主版本事实缺失而 blocked。 |

## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 来源：本轮 fresh session `019f7a73-2dfe-7161-b291-285f043ab1c7`，位于 `tmp/eval-runs/117/eval-003-audit-pure-refactor/with_skill/`。
- 候选只新增审计报告，未改页面、代码或 release metadata，未返回 `ready_for_tag`。

## Without-Skill Baseline
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 来源：本轮独立 fresh session `019f7a77-670e-7572-bc70-e597b5a8bcaa`，同一 prompt 与 pristine fixture；未复用历史 baseline。
- baseline 同样识别纯重构与版本表面缺口，并保持零写入，但没有持久化契约化审计报告。

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 无 assertion failure。合成 refs 使用 `.eval/actual-diff.patch`，是 harness 限制而非协议缺陷。

## Next Steps

- 保留本结果；纯重构放行语义或 release-surface gate 变化时重跑。

## Runtime Artifact Policy

- 本轮运行期证据仅位于 `tmp/eval-runs/117/`，不提交；durable 产物仅为本 `comparison.md`。
