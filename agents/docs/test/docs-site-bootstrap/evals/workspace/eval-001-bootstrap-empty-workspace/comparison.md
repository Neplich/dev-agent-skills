# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-site-bootstrap`
- Eval: `eval-001-bootstrap-empty-workspace`
- Review context: issue #155 fresh paired eval

## Test Set / Fixture Version

- Fixture: pristine empty host from `workspace/eval-001-bootstrap-empty-workspace`
- Historical asset snapshot: 40-file `assets/docs/site/` inventory
- Current contract: 42 packaged assets and six templates
- Dependency fact under review: the VitePress declaration is pinned exactly to `1.6.4` in both `package.json` and the root and resolved entries of `package-lock.json`
- Actual validation date: `2026-07-22`
- Execution cleanup: isolated lane started without `docs/site/`

## Latest Result

**PASS (6/6 assertions)** — the historical fresh with-skill lane created the complete bounded scaffold for the then-current 40-asset, five-template contract, generated and read back a sorted 40-entry manifest, passed the applicable host checks and both site builds with VitePress 1.6.4, and demonstrated a zero-content-diff repeat classification.

Overall result: FAIL

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `FAIL` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `creates_complete_inventory` | PASS | FAIL | with_skill 源资产 42 项全部逐字节匹配，manifest 含 42 条记录；without_skill 仅生成 6 个文件且无 manifest。 |
| `delivers_deterministic_scaffold_assets` | PASS | FAIL | with_skill `new:doc` 唯一存在，两个脚本齐全，六个模板各有一个完整区块并被 `standards/index.md` 索引；without_skill 均不存在。 |
| `validates_seven_frontmatter_fields` | PASS | FAIL | with_skill 的 19 个正式 Markdown 页面均有七字段，`doc_type` 均在允许集合内，数组非空且版本为 `unverified`；without_skill 页面无 frontmatter。 |
| `writes_only_docs_site` | PASS | PASS | 两条 lane 的实际生成文件均位于各自 workspace 的 `docs/site/` 下，未发现目标根外文件。 |
| `requires_explicit_opt_in` | PASS | PASS | 两条 lane 使用的 prompt 均明确确认当前仓库、固定 `docs/site/` 根及正式文档站初始化。 |
| `reports_manifest_readback` | FAIL | FAIL | with_skill manifest 可独立解析且路径/状态正确，但没有独立保留的重复运行快照或 diff 证据；without_skill 没有 manifest。 |

未满足断言（with/without 任一 FAIL）：``creates_complete_inventory``、``delivers_deterministic_scaffold_assets``、``validates_seven_frontmatter_fields``、``reports_manifest_readback``



## Current Asset-Set Drift

- The retained PASS above is the historical issue #155 result for the former 40-asset, five-template inventory.
- The current packaged asset set contains 42 assets and six templates after adding `standards/templates/manual-guide.md` and `manual/index.md`.
- This changed inventory has not received fresh with-skill, same-run without-skill baseline, and independent judge validation, so the historical PASS does not establish the current result and no current PASS conclusion is claimed.

## Assertions
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- `creates_complete_inventory`: PASS. All 40 packaged assets were copied byte-for-byte; manifest parsing returned 40 sorted `created` entries.
- `delivers_deterministic_scaffold_assets`: PASS. `package.json` has exactly one `new:doc`; the scaffold script and test exist; each of five templates has exactly one `docs-scaffold` block and all five are indexed.
- `validates_seven_frontmatter_fields`: PASS. `npm run test:docs` passed the shared frontmatter checker and all 74 Node tests.
- `writes_only_docs_site`: PASS. The generated scaffold and runtime manifest were confined to the isolated `docs/site/` root; evaluation evidence remained outside the generated host root under the issue scratch directory.
- `requires_explicit_opt_in`: PASS. Execution relied on the prompt's explicit host fixture, fixed `docs/site/` root, full scaffold, and manifest authorization; without that entry basis the skill gate stops before writes.
- `reports_manifest_readback`: PASS. The manifest parsed with 40 valid paths and dispositions, and a second full static-content checksum comparison was zero-diff with the original `createdAt` unchanged.

## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- Source: fresh issue #155 with-skill lane under `tmp/eval-runs/issue-155/with_skill/eval-001`, using the current Docs README, target skill, internal inventory protocol, shared frontmatter contract, eval prompt, and pristine fixture.
- Copied 40/40 static assets exactly, created `.meta/bootstrap-manifest.json` with stable sorted paths, and read every generated static target back against its packaged source.
- Confirmed `vitepress: "1.6.4"` in `package.json`, the lockfile root dependency, and the resolved `node_modules/vitepress` record.
- Ran `npm ci`, `npm run test:docs`, `npm run build:public`, and `npm run build:internal`; all exited `0`, and both build logs identified VitePress 1.6.4.
- Reclassified the complete static inventory and compared checksums after host checks; scaffold content and manifest remained zero-diff. Generated `.generated/**` trees and `node_modules/**` were treated only as runtime evidence.

## Fresh Without-Skill Baseline

- Source: a newly spawned independent issue #155 baseline worker using the same prompt and empty scratch fixture. It was explicitly prohibited from reading the target skill, Docs README, internal instructions, old comparisons, with-skill output, and packaged assets.
- Result: `BLOCKED`. The empty scratch exposed no scaffold source, complete inventory, manifest rules, or runner, so the worker correctly refused to guess and created no `docs/site/` output.
- No historical baseline was reused. The inability to generate the requested scaffold demonstrates the behavioral value of the skill and does not block the valid with-skill result.

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- No with-skill assertion failures or blocked checks.
- The fresh without-skill lane was blocked by absent implementation sources and satisfied none of the artifact assertions.
- `npm ci` reported 3 audit advisories (2 moderate, 1 high); installation, 74/74 tests, and both required builds still passed, so this is recorded as non-blocking runtime evidence rather than an eval failure.

## Next Steps

- Retain the PASS only as the historical issue #155 result for the 40-asset, five-template contract.
- Run fresh paired validation for the current 42-asset, six-template contract, including a newly generated `without_skill` baseline, before replacing the BLOCKED result.

## Runtime Artifact Policy

- Runtime lanes, manifests, checksums, `node_modules`, generated site trees, and baseline reports remain under `tmp/eval-runs/issue-155/` and are not durable repository artifacts.
- Only this `comparison.md` is retained; no transcript, candidate, verdict, timing, diagnostics, dependency directory, or generated site output is submitted.
