# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-001-sync-feature-api`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `a02cecead0666327de493458ce5b7665c4330c17675060cfa33039c7bc6f5032` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-001-sync-feature-api`.
- Fixture SHA-256: `a02cecead0666327de493458ce5b7665c4330c17675060cfa33039c7bc6f5032`
- Prompt SHA-256: `cd2f08c41a6ec95815793c80de00d9c220026a6632090c7da71f54b61e0f767a`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `79b2ff102fa24fa224c9f24f44f3e648a1ae7eb9a7a10e639d8675db4454120a`
- Skill overlay SHA-256: `52a3ba7ee2d9485acf003417b40e0d0ca2ab263cbadde98fac58250b6c2a9778`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ce743547e06014367140716bb2c97c1db58eb733e797662e8b4bd6eca00be3ee`
- Metadata SHA-256: `e71fe1ba5d6339777690bef42456f363050aa1a29a7cf722a403bab61da88105`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `selects_backfill_mode_and_api_contract` | FAIL | With-skill output selects existing-system backfill and cites the request, handoff, catalog, and site, but does not state loading the host standards entry, change map, or API template, nor explicitly confirm those non-API templates were not read or applied. |
| `derives_complete_api_candidate_tree` | FAIL | It lists the required five pages and supports them with catalog paths, routes, owner, schema, and contract-test evidence, while deferring Billing; however, route tag evidence is not stated. |
| `presents_per_node_confirmation_matrix` | FAIL | The page table has only page, role, and evidence, and the mapping section has change-map entries. It does not provide per-node parent, exact code boundary, owner, classification/route evidence, delta, and exclusions for every domain, subfeature, index, and leaf. |
| `proposes_exact_atomic_change_map` | FAIL | The route, schema, and contract-test mappings cover the five-page tree and preserve the manual-plugin fields, but the output does not state stable deduplicated sorting of mappings/navigation or explicitly preserve all unrelated entries. |
| `preserves_stable_paths_and_scope_boundaries` | FAIL | It keeps Billing and Search out of batch and explicitly excludes database, design, ops, product, and release documentation, but does not explicitly exclude src/api/internal/** or state the required migration-plan-and-confirmation rule for any stable-path move. |
| `keeps_unconfirmed_batch_read_only` | FAIL | It clearly says no documents or change map are written and waits for confirmation before creation, but does not explicitly state that no next batch, post-write host checks, or docs-agent:docs-audit handoff will occur. |
| `defaults_new_pages_to_internal_visibility` | PASS | It assigns visibility: internal to new pages and keeps the existing API root both-visible because the existing external Search page remains in scope for that root. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cd2f08c41a6ec95815793c80de00d9c220026a6632090c7da71f54b61e0f767a; fixture_sha256=a02cecead0666327de493458ce5b7665c4330c17675060cfa33039c7bc6f5032; output_sha256=11161bded73630a85cd31368c0e218e82be9fad772da28eb2071f2a299fc0a09; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: The candidate selects the correct Identity/Sessions backfill and page paths, adds richer evidence and mappings, preserves existing Search/manual-plugin context, and pauses before writes, but omits several required per-node, exclusion, and confirmation-boundary details.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cd2f08c41a6ec95815793c80de00d9c220026a6632090c7da71f54b61e0f767a; fixture_sha256=a02cecead0666327de493458ce5b7665c4330c17675060cfa33039c7bc6f5032; output_sha256=4ca78b03d9e770f30a2c191b37277e80501b4d504ccfee8590cc220140b63de0; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline proposes a narrower four-page subtree with create.md/revoke.md names, incomplete ancestor/change-map coverage, and no visibility or explicit read-only handoff safeguards.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- With-skill output fails six assertions due to omitted required evidence or safeguards; the without-skill lane was used only as comparison context.
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
- Eval: `eval-001-sync-feature-api`
- Review context: PR #164 second-round review for skill-specific eval discrimination

## Test Set / Fixture Version

- Fixture: current pristine `workspace/eval-001-sync-feature-api` snapshot for issue #159
- Scenario: an existing-system API backfill request authorizes bounded discovery for the Identity / Sessions catalog branch but does not confirm candidate pages, hierarchy, mappings, navigation, or writes
- Evidence set: PM handoff, bounded-discovery request, feature catalog, host standards and change map, route/schema/handler code, contract tests, existing stable Search page, and Billing as an out-of-batch control
- Actual validation date: `2026-07-22`
- Isolation: fresh `codex exec` copied the same fixture without historical comparison into independent with-skill and without-skill lanes; the start manifests matched, both end manifests remained identical to their starts, and a third fresh `codex exec` judge reviewed the final assertions and both outputs

## Latest Result

- Overall result: FAIL

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `FAIL` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `selects_backfill_mode_and_api_contract` | FAIL | FAIL | 两者都提出 API 回填，但未明确引用 host standards、change map、API template/type module，也未证明未读取 database/design/ops/product 模块；with_skill 仅列出 API 证据（`with_skill/result.txt:13-24`），without_skill 还引入了 `docs/pm/feature-catalog.md` 映射（`without_skill/result.txt:43-48`）。 |
| `derives_complete_api_candidate_tree` | FAIL | FAIL | 两者都列出了完整五节点树（`result.txt:3-11`），但未用 catalog 父子关系、route prefix/tag、owner、schema、contract tests 完整解释层级，也未明确说明不是按源码文件机械拆分。 |
| `presents_per_node_confirmation_matrix` | FAIL | FAIL | 两者没有逐 domain、subfeature、index、route leaf 的 confirmation matrix；仅有树状图和 change-map。缺少逐节点的完整 page path、代码边界、owner、分类证据、delta 和 exclusions 配对。 |
| `proposes_exact_atomic_change_map` | FAIL | FAIL | with_skill 的 `required_docs` 覆盖五个页面（`with_skill/result.txt:26-53`），但未明确递归导航、原子更新、稳定去重排序及保留 `plugins/manual/**` 全部字段；without_skill 的映射遗漏 API/Identity/Sessions ancestor index，并额外加入 `docs/pm/feature-catalog.md`（`without_skill/result.txt:23-49`）。 |
| `preserves_stable_paths_and_scope_boundaries` | FAIL | FAIL | 两者都排除了 Billing、Search 和内部 API（with `:56`；without `:51`），但未明确排除 database/design/ops/product/release，也未完整声明既有 `search.md` 及其 change-map 映射保持不动，或提供迁移计划要求。 |
| `keeps_unconfirmed_batch_read_only` | PASS | PASS | 两者均明确“不写入站点”、要求维护者确认后再写入（with `:1,58`；without `:1,51`）。实际目录仅有 `result.txt` 和 `run_status.json`，没有页面、change-map、index、导航或 handoff 产物。 |
| `defaults_new_pages_to_internal_visibility` | FAIL | FAIL | 两者均未为候选页面或映射声明 `visibility: internal`，也未解释 `both/public` 例外。 |

未满足断言（with/without 任一 FAIL）：``selects_backfill_mode_and_api_contract``、``derives_complete_api_candidate_tree``、``presents_per_node_confirmation_matrix``、``proposes_exact_atomic_change_map``、``preserves_stable_paths_and_scope_boundaries``、``defaults_new_pages_to_internal_visibility``



## Assertions
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- `selects_backfill_mode_and_api_contract`: with skill PASS; without skill FAIL. The skill lane selected `existing-system backfill`, accepted the bounded-discovery entry basis, and loaded only the host API contract; the baseline did not establish mode or progressive-loading semantics.
- `derives_complete_api_candidate_tree`: both PASS. Both lanes derived the API root, Identity and Sessions indexes, and the create/revoke route leaves from catalog, route, owner, schema, and contract-test evidence while keeping Billing for a later batch.
- `presents_per_node_confirmation_matrix`: with skill PASS; without skill FAIL. The skill lane's node matrix and mapping section jointly paired every node with parent, path, code boundary, owner, evidence, mapping delta, and exclusions; the baseline could not pair ancestor indexes with proposed mapping deltas.
- `proposes_exact_atomic_change_map`: with skill PASS; without skill FAIL. The skill lane's route mapping included both leaves plus the Sessions, Identity, and API ancestor indexes and preserved unrelated entries and unknown fields; the baseline mapped only leaf pages.
- `preserves_stable_paths_and_scope_boundaries`: both PASS. Both lanes preserved Search and its mappings and excluded Billing, internal API, non-API surfaces, stable-path migration, and later batches.
- `keeps_unconfirmed_batch_read_only`: both PASS. Both lanes waited for explicit candidate-batch confirmation, produced zero workspace changes, and did not run write-after checks or hand off to docs-audit.

## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- Read `formal-docs-sync` entry and common instructions, the API type module, the host standards entry, API template, change map, implementation evidence, tests, and the shared frontmatter contract; no non-API type module was loaded.
- Chose existing-system backfill rather than feature delivery and treated the maintainer request as discovery authorization rather than write confirmation.
- Proposed one coherent Identity / Sessions subtree with all ancestor indexes and two independently locatable route leaves.
- Presented the full candidate scope and an ancestor-aware atomic change-map delta, preserved manual unknown fields and stable Search mappings, and kept Billing and all non-API surfaces out of batch.
- Stopped before writes, host checks, the next batch, or a `docs-agent:docs-audit` handoff.

## Fresh Without-Skill Baseline

> ⚠️ 本节为历史轮执行证据（适用旧 run）；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

- Source: fresh `without_skill` lane from the same final prompt and identical pristine fixture; it did not read the target skill, Docs Agent README, internal/shared skill instructions, historical comparison, or with-skill output.
- The baseline correctly derived the five-node Identity / Sessions tree, protected Search and out-of-batch surfaces, and stayed read-only.
- It did not select the formal-docs-sync backfill mode or API-only progressive-loading path, did not complete the per-node confirmation mapping for ancestor indexes, and omitted all ancestor indexes from the proposed change-map `required_docs`.
- Baseline result: **3/6**.

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- With-skill assertion failures: none.
- Baseline failures: mode/progressive loading, per-node candidate confirmation mapping, and ancestor-aware atomic change-map coverage.
- Infrastructure blockers: none. The recurring local Codex model-cache warning did not prevent either lane or the judge from completing and did not affect semantic evidence.

## Next Steps

- Keep the bounded-discovery request distinct from candidate confirmation so future regressions cannot pass by copying a prompt-prescribed tree.
- Preserve the ancestor-index mapping assertion; it is the strongest observed discriminator between skill-guided synchronization and the generic baseline.

## Runtime Artifact Policy

- Source copy, both isolated lanes, candidate outputs, manifests, workspace diffs, and fresh judge verdict remain under `tmp/eval-runs/issue-159-review2-20260722-v2/` and are not submitted.
- Only this `comparison.md` is durable; no transcript, candidate output, verdict, timing, diagnostics, dependency directory, or generated site is tracked.
