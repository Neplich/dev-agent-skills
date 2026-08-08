# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-site-bootstrap`
- Eval: `eval-001-bootstrap-empty-workspace`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/docs/test/docs-site-bootstrap/evals/workspace/eval-001-bootstrap-empty-workspace`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `8294223a6cc9320411b7f3ca9761133eeb49b555e990170abcfa40eeb8076bd8`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `4a398cfa9db1074844549bc002d7714ae1641dceb87757d5c772d45182765b8a`
- Skill overlay SHA-256: `4e5a2571a4a7180fe735bec31f7744892dd9b213e7966b85237f9d1c2b22d88a`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `0028d93b645e269e09fc6f6345ad073b0c2386395ad858bbd7693d057a9eca5f`
- Metadata SHA-256: `72695cba8eaf9810a85aa17ba3cc9622de1dd39f4d06db93fe0728a19509d73b`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_complete_inventory` | PASS | with_skill evidence reports 42/42 byte verification; manifest contains 42 created entries, all under docs/site/. |
| `delivers_deterministic_scaffold_assets` | PASS | Snapshot contains package.json with one new:doc script, both required scripts, six templates with exactly one docs-scaffold block each, and standards/index.md links all six. |
| `validates_seven_frontmatter_fields` | PASS | All 19 Markdown pages in the snapshot contain the seven required fields; owners and related_code are non-empty arrays, doc_type values are allowed, and last_verified_version is present. |
| `writes_only_docs_site` | PASS | All 42 manifest paths are within docs/site/; git evidence shows no tracked-file changes and only the docs directory untracked. |
| `requires_explicit_opt_in` | PASS | The prompt explicitly confirms the target repository, fixed docs/site root, and complete scaffold before the with_skill lane writes. |
| `reports_manifest_readback` | PASS | with_skill reports manifest parsing and path/status validation, plus repeat execution producing 42 skipped-identical files, zero conflicts, and zero content changes. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8294223a6cc9320411b7f3ca9761133eeb49b555e990170abcfa40eeb8076bd8; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=b94d3bc71ead18138be683dfdfb4ce717a4bb8b84236dc302dfe28186a27a095; snapshot_sha256=13b06c79556a034e84ca74d53414eac66892c7fad48ef238489f2cbc7275d24b
- Behavior: Created the complete 42-asset formal documentation scaffold under docs/site, validated manifest coverage and frontmatter, and reported deterministic zero-diff rerun behavior.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8294223a6cc9320411b7f3ca9761133eeb49b555e990170abcfa40eeb8076bd8; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=5face9b89423d7ac698448df35db8f8e53255cde6c5524d24fe775c1b9c7042a; snapshot_sha256=603023b347ba6e56192ea24250868340485c05ea2c579e7bf8b9a7903c705fb3
- Behavior: Created a small Docusaurus scaffold with 9 files, omitted the required 42-asset inventory and formal documentation scaffold, and reported repeat execution as unchanged.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
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



## Current Asset-Set Status

- The retained PASS above is the historical issue #155 result for the former 40-asset, five-template inventory.
- The current packaged asset set contains 42 assets and six templates after adding `standards/templates/manual-guide.md` and `manual/index.md`.
- The #238 paired rerun and independent judge validated the current inventory and scaffold surfaces. The current result remains `FAIL` only because `reports_manifest_readback` lacks an independently retained repeat-run snapshot or zero-diff evidence.

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

> ⚠️ 本节为历史轮执行证据（适用旧 run）；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

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
- Re-run the current 42-asset, six-template contract with an independently retained repeat-run snapshot or zero-diff evidence before replacing the current `FAIL` result.

## Runtime Artifact Policy

- Runtime lanes, manifests, checksums, `node_modules`, generated site trees, and baseline reports remain under `tmp/eval-runs/issue-155/` and are not durable repository artifacts.
- Only this `comparison.md` is retained; no transcript, candidate, verdict, timing, diagnostics, dependency directory, or generated site output is submitted.
