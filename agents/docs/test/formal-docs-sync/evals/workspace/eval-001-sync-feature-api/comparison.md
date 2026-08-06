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
- 注：PASS 结论基于旧断言（6 条）评测记录保留；断言已按 #239 增强（新增 internal 收紧断言，共 7 条），待 fresh eval 重跑验证新断言。
- Discrimination note: 修复后隔离重跑（2026-08-05，fresh 会话、workspace 仓库外拷贝）with/without 均满足旧断言（6 条，增强前）。成因：宿主 handoff 材料（pm-handoff.md 的 required_output、change-map.yaml 模板、feature-catalog）天然承载候选树/change-map/零写入结构，按 AGENTS.md 泄漏判定表属「规则天然存在于 skill 交付物」，非泄漏缺陷，如实记录。skill 特有行为差异（新增页面 internal 收紧、change-map exclude 完整性）未落入断言粒度，建议后续增强断言。

**PASS (with skill 6/6; without skill 3/6, 旧断言)** — the skill lane satisfied the full unconfirmed-batch protocol, while the fresh baseline retained only generic tree derivation, scope protection, and read-only behavior. Comparative discrimination is restored.

## Assertions

- `selects_backfill_mode_and_api_contract`: with skill PASS; without skill FAIL. The skill lane selected `existing-system backfill`, accepted the bounded-discovery entry basis, and loaded only the host API contract; the baseline did not establish mode or progressive-loading semantics.
- `derives_complete_api_candidate_tree`: both PASS. Both lanes derived the API root, Identity and Sessions indexes, and the create/revoke route leaves from catalog, route, owner, schema, and contract-test evidence while keeping Billing for a later batch.
- `presents_per_node_confirmation_matrix`: with skill PASS; without skill FAIL. The skill lane's node matrix and mapping section jointly paired every node with parent, path, code boundary, owner, evidence, mapping delta, and exclusions; the baseline could not pair ancestor indexes with proposed mapping deltas.
- `proposes_exact_atomic_change_map`: with skill PASS; without skill FAIL. The skill lane's route mapping included both leaves plus the Sessions, Identity, and API ancestor indexes and preserved unrelated entries and unknown fields; the baseline mapped only leaf pages.
- `preserves_stable_paths_and_scope_boundaries`: both PASS. Both lanes preserved Search and its mappings and excluded Billing, internal API, non-API surfaces, stable-path migration, and later batches.
- `keeps_unconfirmed_batch_read_only`: both PASS. Both lanes waited for explicit candidate-batch confirmation, produced zero workspace changes, and did not run write-after checks or hand off to docs-audit.

## With-Skill Behavior

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

- With-skill assertion failures: none.
- Baseline failures: mode/progressive loading, per-node candidate confirmation mapping, and ancestor-aware atomic change-map coverage.
- Infrastructure blockers: none. The recurring local Codex model-cache warning did not prevent either lane or the judge from completing and did not affect semantic evidence.

## Next Steps

- Keep the bounded-discovery request distinct from candidate confirmation so future regressions cannot pass by copying a prompt-prescribed tree.
- Preserve the ancestor-index mapping assertion; it is the strongest observed discriminator between skill-guided synchronization and the generic baseline.

## Runtime Artifact Policy

- Source copy, both isolated lanes, candidate outputs, manifests, workspace diffs, and fresh judge verdict remain under `tmp/eval-runs/issue-159-review2-20260722-v2/` and are not submitted.
- Only this `comparison.md` is durable; no transcript, candidate output, verdict, timing, diagnostics, dependency directory, or generated site is tracked.
