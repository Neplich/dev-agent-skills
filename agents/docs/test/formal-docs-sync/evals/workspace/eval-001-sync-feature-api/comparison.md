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

未满足断言：``selects_backfill_mode_and_api_contract``、``derives_complete_api_candidate_tree``、``presents_per_node_confirmation_matrix``、``proposes_exact_atomic_change_map``、``preserves_stable_paths_and_scope_boundaries``、``defaults_new_pages_to_internal_visibility``

- 注：PASS 结论基于旧断言（6 条）评测记录保留；断言已按 #239 增强（新增 internal 收紧断言，共 7 条），待 fresh eval 重跑验证新断言。
- Discrimination note: 修复后隔离重跑（2026-08-05，fresh 会话、workspace 仓库外拷贝）with/without 均满足旧断言（6 条，增强前）。成因：宿主 handoff 材料（pm-handoff.md 的 required_output、change-map.yaml 模板、feature-catalog）天然承载候选树/change-map/零写入结构，按 AGENTS.md 泄漏判定表属「规则天然存在于 skill 交付物」，非泄漏缺陷，如实记录。skill 特有行为差异（新增页面 internal 收紧、change-map exclude 完整性）未落入断言粒度，建议后续增强断言。

**PASS (with skill 6/6; without skill 3/6, 旧断言)** — the skill lane satisfied the full unconfirmed-batch protocol, while the fresh baseline retained only generic tree derivation, scope protection, and read-only behavior. Comparative discrimination is restored.

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
