# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-site-bootstrap`
- Eval: `eval-003-block-bootstrap-conflict`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `67d646aaa1407e943f08140487b646ac63c9406ed33f7972e7921d67116c9f4a` from `agents/docs/test/docs-site-bootstrap/evals/workspace/eval-003-block-bootstrap-conflict`.
- Fixture SHA-256: `67d646aaa1407e943f08140487b646ac63c9406ed33f7972e7921d67116c9f4a`
- Prompt SHA-256: `7e27a0b4acbeb0bbab6d1ce4f4eaef1707f80d3f366d62ddd92d0e2d6f621f17`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `4a398cfa9db1074844549bc002d7714ae1641dceb87757d5c772d45182765b8a`
- Skill overlay SHA-256: `4e5a2571a4a7180fe735bec31f7744892dd9b213e7966b85237f9d1c2b22d88a`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ef71b65d8d90e0a7a85b11140f77333b6bccfac4b39b25f67875d33153f0ebea`
- Metadata SHA-256: `f803e3375aba235a63dd71bd62cd38381ac769cf2c9e1bbcc4c0d413d0ba7769`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_on_complete_conflict_list` | FAIL | with_skill 将 docs/site/standards/index.md 标记为 kept-as-is，但未提供完整冲突清单、blocked 状态或证明未创建成功 manifest 状态。 |
| `does_not_overwrite_conflict` | PASS | with_skill 输出明确称该文件原样保留；git_status 未显示 standards/index.md 被修改，manifest 将其记录为 kept-as-is。 |
| `offers_explicit_resolution_choices` | FAIL | with_skill 输出未明确提供 overwrite、显式 merge、保留现有文件三种解决选项，也未证明仅在用户选择保留后记录 kept-as-is。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=7e27a0b4acbeb0bbab6d1ce4f4eaef1707f80d3f366d62ddd92d0e2d6f621f17; fixture_sha256=67d646aaa1407e943f08140487b646ac63c9406ed33f7972e7921d67116c9f4a; output_sha256=e5b3c4c006a129120ff7fa238ae4e6767a99cf5fd5eefcdb7bb4841b54332837; snapshot_sha256=690519ce7e657d395a43bda2b22155a0248a2d6366b6deef94074812a8ab5fe6
- Behavior: 生成文档站资产并保留冲突文件原样，将其记录为 kept-as-is；但未展示完整冲突清单、blocked 状态或三类解决选项。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=7e27a0b4acbeb0bbab6d1ce4f4eaef1707f80d3f366d62ddd92d0e2d6f621f17; fixture_sha256=67d646aaa1407e943f08140487b646ac63c9406ed33f7972e7921d67116c9f4a; output_sha256=5c0a32114d2c7e946fef6ce381d5abbd603fa34a20a8fcd50779876e329b097d; snapshot_sha256=91ce7bef7c7a597ad002960262fc199914c5d0ea1550449e1e2fb583893702f6
- Behavior: 生成文档站资产并修改 manifest，将冲突文件写入 ownership；未阻塞冲突，也未提供三类解决选项。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足完整冲突清单并阻塞未解决覆盖阶段的要求。
- with_skill 未明确提供 overwrite、显式 merge、保留现有文件三类解决选项。
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
