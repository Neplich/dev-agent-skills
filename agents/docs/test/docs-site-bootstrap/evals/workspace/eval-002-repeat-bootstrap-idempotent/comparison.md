# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-site-bootstrap`
- Eval: `eval-002-repeat-bootstrap-idempotent`
- Review context: cumulative API, Database, Product, Design, and Ops deployment layering fixture refresh from PR #164 and PR #166

## Test Set / Fixture Version

- Fixture: `2026-07-ops` (cumulative from `issue-122-assets-v2-c5r`)
- Scope: 9 materialized targets; all omitted targets are explicitly assumed present and byte-identical to the current 40-file inventory
- Dependency fact under review: the representative `package.json` VitePress declaration is pinned exactly to `1.6.4`
- Asset refresh under review: materialized `standards/templates/api-template.md`, `standards/templates/database.md`, and `standards/templates/ops-runbook.md` match the current packaged assets; Product, Design, and Ops deployment layering in `standards/doc-granularity.md` plus `ops/index.md` remain covered by the explicit omitted-target assumption
- Actual validation date: `2026-07-22`

## Latest Result

**PASS（3/3 assertions）— 历史结论（适用旧 fixture），已被上方 fixture-stale BLOCKED 取代**

Overall result: BLOCKED

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `FAIL` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `produces_zero_diff` | PASS | PASS | 两条 lane 的工作区文件哈希均稳定，manifest 的 `createdAt` 保持为 `2026-07-16T08:00:00+08:00`；未发现重写后的文件内容。 |
| `reports_skipped_identical` | FAIL | FAIL | 两条 lane 的 manifest 都将 `feature-design.md` 和 `product-handbook.md` 标为 `skipped-identical`，但它们与源资产哈希不同：源资产分别为 `135360d…`、`2dbab2…`，工作区为 `5595820…`、`2c7b10…`。with_skill 报告了这两项冲突；without_skill 还错误报告 `standards/index.md` 冲突，而其哈希与源资产一致。 |
| `preserves_existing_state` | PASS | PASS | `standards/change-map.yaml` 与 `.meta/releases.json` 均存在，内容分别保持源资产哈希 `014f624…`、`c906ead…`；manifest 的既有 `createdAt` 也未被重置。阻塞时未写入宿主状态。 |

未满足断言（with/without 任一 FAIL）：``reports_skipped_identical``

Fixture 阻塞说明：已提交 fixture 的源资产（feature-design.md / product-handbook.md）与工作区哈希不一致，skill 如实报告冲突（未伪报 skipped-identical）属正确行为；需更新 fixture 后重跑。



## Current Asset-Set Drift

- The retained PASS above is the historical result for the former 40-asset, five-template inventory.
- The current packaged asset set contains 42 assets and six templates after
  adding `standards/templates/manual-guide.md` and `manual/index.md`.
- This changed inventory has not received fresh with-skill, same-run without-skill baseline, and independent judge validation, so the historical PASS does not establish the current result and the eval must be rerun.

## Assertions
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- `produces_zero_diff`: PASS. All nine materialized targets compared byte-identical to packaged assets; before/after SHA-256 sets and manifest hash `0bb02c44054da996a17a489f0453ced2c03cde6b9bf757d4a035ac5f3e90017b` matched, and `createdAt` remained `2026-07-16T08:00:00+08:00`.
- `reports_skipped_identical`: PASS. The nine representative paths remain persisted as `skipped-identical` in the existing manifest; refreshed `api-template.md`, `database.md`, and `ops-runbook.md` respectively match current assets at SHA-256 `d5186c628d6b9967f9343b22ac60e7b2a275ee70085523c133859cf696153231`, `da5fecfea765dce8cac4e0289d0371d34eca5bf6038589d024da8ae8946ff424`, and `038a8578d48f5d40bd4db74de96e1013524dba94e25f26f763285bd943ab88e4`.
- `preserves_existing_state`: PASS. `standards/change-map.yaml`, `.meta/releases.json`, standards pages, templates, package metadata, manifest, and all other fixture content remained unchanged.

## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- Source: fresh PR #164 review round 7 and PR #166 validation lanes under `tmp/eval-runs/pr164-review7-s4MWVn/with_skill` and `tmp/eval-runs/issue-161-review/eval-002/with_skill`, each executed by a new `codex exec` validation subagent using the current target skill, required internal inventory rules, the eval prompt, and a copied minimal fixture.
- Applied the 40-file inventory and persistent manifest rules while honoring the fixture's explicit omitted-target byte-equivalence assumption.
- Exact comparisons for all nine materialized targets returned equal; manifest read-back preserved all nine `skipped-identical` dispositions and the original timestamp.
- The refreshed materialized `api-template.md`, `database.md`, and `ops-runbook.md` matched their current packaged assets exactly. Product, Design, and Ops deployment layering in `standards/doc-granularity.md` plus `ops/index.md` are not materialized targets and remain within the fixture's explicit omitted-target byte-equivalence assumption.
- The representative package declares VitePress exactly as `1.6.4` and remained byte-identical to the current packaged asset.
- The fixture intentionally omits scripts, the lockfile, and most of the complete site, so host tests and builds are not applicable. Validation used exact asset comparisons, manifest parsing, and before/after content hashes; no complete-host checks are claimed.

## Fresh Without-Skill Baseline

- Source: fresh baseline lanes under `tmp/eval-runs/pr164-review7-s4MWVn/without_skill` and `tmp/eval-runs/issue-161-review/eval-002/without_skill`, each regenerated by its corresponding new `codex exec` validation subagent with the identical prompt and copied fixture; target skill, Docs README, internal instructions, packaged assets, old comparison, and with-skill output were prohibited in these lanes.
- Result: `PARTIAL / NO-OP`. It confirmed the nine materialized files, existing manifest shape and dispositions, fixed `createdAt`, and an unchanged before/after hash set, but could not perform a real asset-aware bootstrap without the target protocol or asset bytes.
- No historical baseline was reused. It could observe the fixture's existing `skipped-identical` declarations but could not independently prove host-to-asset byte equality; the with-skill lane supplied the authoritative inventory and asset-mapping evidence needed for the complete PASS.

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- No with-skill assertion failures or blocked checks.
- Host docs tests and builds are not applicable to this deliberately minimized fixture because the scripts, lockfile, and full site are not materialized.
- The baseline's missing runner and inventory source limit it to `PARTIAL`; this does not affect the complete with-skill byte and manifest evidence.

## Next Steps

- Re-run against the current 42-asset, six-template inventory with a fresh
  without-skill baseline and independent judge before restoring a PASS result.

## Runtime Artifact Policy

- Runtime copies, checksums, lane reports, and subagent verdicts remain under `tmp/eval-runs/pr164-review7-s4MWVn/` and `tmp/eval-runs/issue-161-review/eval-002/` and are not submitted.
- Only this durable comparison is retained; no runtime output, dependency directory, generated site, transcript, candidate, verdict, timing, or diagnostics are committed.
