# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-site-bootstrap`
- Eval: `eval-003-block-bootstrap-conflict`
- Review context: issue #155 fresh paired eval

## Test Set / Fixture Version

- Fixture: `issue-122-assets-conflict-v1`
- Scope: one known host conflict plus representative identical targets; omitted targets follow the fixture's missing-or-identical assumption
- Dependency fact under review: the representative `package.json` VitePress declaration is pinned exactly to `1.6.4`
- Actual validation date: `2026-07-22`

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
| `blocks_on_complete_conflict_list` | PASS | PASS | 两条 lane 均明确列出 `docs/site/standards/index.md` 为冲突文件，说明“安全阻塞”，并承诺未收到决定前不生成部分脚手架或 manifest；实际 manifest 未将该文件标记为成功状态。 |
| `does_not_overwrite_conflict` | PASS | PASS | 两条 workspace 中 `docs/site/standards/index.md` 均保留 fixture 的宿主定制内容（“团队文档规范入口”、审批链接和 owner 约定），未被覆盖或部分规范化。 |
| `offers_explicit_resolution_choices` | PASS | PASS | 两条 lane 均明确提供 `overwrite`、`merge`、`keep` 三种选项，并说明只有选择 `keep` 后才记录 `kept-as-is`；当前 manifest 中没有该状态。 |

本轮无 FAIL 断言。



## Assertions
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- `blocks_on_complete_conflict_list`: PASS. `docs/site/standards/index.md` is the complete conflict list under the fixture scope; the unresolved overwrite stage remains blocked and the manifest has no success state for that path.
- `does_not_overwrite_conflict`: PASS. The target still matches the pristine host customization and differs from the packaged asset; before/after SHA-256 sets match, with no merge, formatting, normalization, or partial overwrite.
- `offers_explicit_resolution_choices`: PASS. The with-skill result requires the user to choose overwrite, an explicitly reviewed merge, or keep; `kept-as-is` is recorded only after an explicit keep decision.

## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- Source: fresh issue #155 with-skill lane under `tmp/eval-runs/issue-155/with_skill/eval-003`, using the current target skill and conflict protocol with the same eval prompt and copied minimal fixture.
- Classified `package.json` and `.meta/releases.json` as byte-identical and `standards/index.md` as the single known unresolved conflict; the representative package declares VitePress exactly as `1.6.4`.
- Read-back confirmed the customized index and manifest stayed byte-identical to input; the manifest still contains only the two pre-existing `skipped-identical` entries and no state for the conflict.
- The valid outcome is blocked pending overwrite, explicit merge, or keep. A future keep decision would add `kept-as-is`; no such decision was inferred in this run.
- The fixture deliberately omits executable site scripts and most inventory files, so host tests and builds are not applicable. Conflict comparison, manifest parsing, and before/after hashes are the executable evidence; no complete-host checks are claimed.

## Fresh Without-Skill Baseline

> ⚠️ 本节为历史轮执行证据（适用旧 run）；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

- Source: a newly spawned independent issue #155 baseline worker using the same prompt and copied fixture, with the target skill, Docs README, internal instructions, old comparisons, and with-skill output prohibited.
- Result: `BLOCKED`. It preserved the customized conflict and partial manifest, but lacked the full inventory source and could not complete omitted-target classification or bootstrap.
- The baseline identified keep and overwrite as decisions but omitted the required explicit-merge option, so its behavior satisfies conflict preservation but not the full three-choice assertion. No historical baseline was reused.

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- No with-skill assertion failures.
- The blocked overwrite stage is the expected successful behavior, not an eval failure.
- Host docs tests and builds are not applicable to this deliberately partial conflict fixture.
- The baseline did not provide the full three-option conflict protocol and remained blocked by missing inventory; this comparison does not promote it to PASS.

## Next Steps

- Retain this PASS. A real bootstrap remains paused until the maintainer selects overwrite, an approved explicit merge, or keep for every conflict.

## Runtime Artifact Policy

- Runtime copies, hashes, conflict evidence, and baseline reports remain under `tmp/eval-runs/issue-155/` and are not submitted.
- Only this durable comparison is retained; no runtime transcript, candidate, verdict, timing, diagnostics, dependencies, or generated site output is committed.
