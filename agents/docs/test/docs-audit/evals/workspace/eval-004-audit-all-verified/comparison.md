# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-004-audit-all-verified`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `877afc6a20a0a47433c20416263d7ec34d2ee62071ad1b0dbc64b35451cfe7b5` from `agents/docs/test/docs-audit/evals/workspace/eval-004-audit-all-verified`.
- Fixture SHA-256: `877afc6a20a0a47433c20416263d7ec34d2ee62071ad1b0dbc64b35451cfe7b5`
- Prompt SHA-256: `f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2baee6e542351d5b0c46e79c685dd29ff93f0fee4a45cf4485afee7656248cf7`
- Skill overlay SHA-256: `a2871f547194089c5425585467f9bee6e3c85ea103d77933d85a4c4cf246fa7c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `e14946c0514a89c80fbae0a1c2296f0621f94cff9935a850c07c617de54712b9`
- Metadata SHA-256: `4ac2733faccb7d81e868901a87caed3b09e67f0f580dbd1a3f001b98108909da`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `verifies_complete_affected_set` | FAIL | With-skill report verifies only the two required API pages and explicitly records a missing release-notes handoff as an unresolved evidence gap; it does not establish the complete affected set as verified. |
| `stamps_all_pages_together` | FAIL | With-skill output states that no unified version stamp was executed; all four affected pages remain unchanged in the manifest. |
| `verifies_release_metadata_read_only` | PASS | The report checks docs/site/.meta/releases.json as v1.1.0-consistent and states it was a read-only audit surface; the manifest hash is unchanged. |
| `normalizes_mixed_version_forms` | PASS | The report inventories v1.1.0 and 1.1.0 sources, records normalized result 1.1.0 for each, and treats the absent actual tag as pending_expected_absent. |
| `persists_candidate_producer_schema` | FAIL | The saved record is diagnostic and blocked, not candidate_verified, and lacks required candidate schema details including complete locator/inventory contract, digests, staged gates, post-stamp evidence, and exact claim/test evidence. |
| `anchors_candidate_then_discovers_success` | FAIL | With-skill output explicitly says no candidate commit, handoff, or tag was created, so the required anchor, discovery, integration, and ready_for_tag sequence did not occur. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c; fixture_sha256=877afc6a20a0a47433c20416263d7ec34d2ee62071ad1b0dbc64b35451cfe7b5; output_sha256=30fac7d5952c877acc41f3077460bbfa6b54f3d33cea55d25ab7c2689855fa40; snapshot_sha256=a7feb85c67e0e2892ec5638b972d12c291ddf12630c5c7a2c68551049c83aa87
- Behavior: Saved a structured diagnostic audit, verified the two required API pages and version sources, then blocked on the missing release-notes handoff without stamping or creating commits.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c; fixture_sha256=877afc6a20a0a47433c20416263d7ec34d2ee62071ad1b0dbc64b35451cfe7b5; output_sha256=9c817b5ffa956083119f324ef31a87fbebc0728f22bd6d3fec74cf8960830b25; snapshot_sha256=a4b5846f4088bf4ff7617a4326b78fb9b1bb8444c52977770f879bd2430bb96d
- Behavior: Saved an external audit report, found stale API-page metadata, and made no repository changes.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with-skill lane failed assertions requiring complete affected-set verification, unified stamping, complete candidate schema, and anchor/discovery handoff sequencing.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge package, verdict, timing, and diagnostics remain under ignored `tmp/eval-runs/` or short-lived CI artifacts and are not committed.
- This durable comparison retains only the reviewable summary and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-004-audit-all-verified`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `15ffe8d37dff57cc024ef91d1367c2695ae30d7652ffe146d828a4b684aa43ed` from `agents/docs/test/docs-audit/evals/workspace/eval-004-audit-all-verified`.
- Fixture SHA-256: `15ffe8d37dff57cc024ef91d1367c2695ae30d7652ffe146d828a4b684aa43ed`
- Prompt SHA-256: `f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2baee6e542351d5b0c46e79c685dd29ff93f0fee4a45cf4485afee7656248cf7`
- Skill overlay SHA-256: `a2871f547194089c5425585467f9bee6e3c85ea103d77933d85a4c4cf246fa7c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `e14946c0514a89c80fbae0a1c2296f0621f94cff9935a850c07c617de54712b9`
- Metadata SHA-256: `4ac2733faccb7d81e868901a87caed3b09e67f0f580dbd1a3f001b98108909da`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `verifies_complete_affected_set` | PASS | with_skill explicitly marks all four affected pages verified and documents page-level factual evidence. |
| `stamps_all_pages_together` | FAIL | with_skill explicitly states no version stamp was performed. |
| `verifies_release_metadata_read_only` | PASS | with_skill reports release metadata matches v1.1.0 and says it was not modified. |
| `normalizes_mixed_version_forms` | PASS | with_skill explicitly distinguishes raw v1.1.0 sources from package.json 1.1.0 and says they agree after normalization. |
| `persists_candidate_producer_schema` | FAIL | with_skill explicitly states no candidate record was created. |
| `anchors_candidate_then_discovers_success` | FAIL | with_skill explicitly states no anchor commit or discoverable pre-tag handoff was created and the result was not ready_for_tag. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c; fixture_sha256=15ffe8d37dff57cc024ef91d1367c2695ae30d7652ffe146d828a4b684aa43ed; output_sha256=b63d27e32d005c1da70fec4ecb128ac8080402568bf138f87e87af98eabbe922; snapshot_sha256=5b90d452c4f9150b80d8a21c8792a0b2d572bf89ae328a3f8e0a13c9e0665b21
- Behavior: Verified the affected-page facts and version sources, then correctly blocked on missing formal audit foundation and release-notes handoff; it performed no stamp or downstream publication workflow.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c; fixture_sha256=15ffe8d37dff57cc024ef91d1367c2695ae30d7652ffe146d828a4b684aa43ed; output_sha256=d9eff37efbe459e40603851cc4e6b4605e8982d47636dea5b4f1b2607dbc2023; snapshot_sha256=0ab72c88c3894e94c625d3aa0eb6968168763b9e5b290d81e9ddf0f155502d7f
- Behavior: Produced an uncommitted audit report, identified stale API verification markers, and did not perform the required unified stamp, candidate record, anchor, or handoff workflow.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- stamps_all_pages_together
- persists_candidate_producer_schema
- anchors_candidate_then_discovers_success
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

# eval-004-audit-all-verified Comparison

## Evaluation target

- Agent: `docs-agent`
- Skill: `docs-audit`
- Eval: `eval-004-audit-all-verified`
- Validation time: `2026-08-03 22:40:00 +0800`（fresh re-baseline，issue #188）
- Scope: complete affected-set verification, canonical version-source inventory and genesis digests, unified stamping, candidate/anchor/discovery transaction, and integration-gated `ready_for_tag`.

## Test set and method

This is a fresh paired validation against the current 6 assertions. The
`with_skill` and `without_skill` runs (2026-08-03, #188) each started from their own pristine fixture copy in
isolated directories (`tmp/eval-runs/issue-188-docs/with_skill/` and `tmp/eval-runs/issue-188-docs/without_skill/`),
executed independently without reading each other's outputs. The `without_skill` baseline read only
the current eval definition, metadata, prompt, and fixture files, and did not read the Docs Agent README,
`docs-audit` skill instructions, prior comparison, or historical output. The `with_skill` run read
`agents/docs/skills/docs-audit/SKILL.md`, `agents/docs/skills/docs-audit/_internal/INSTRUCTIONS.md`, and
`agents/docs/README.md` before executing. The fresh judge then read the frozen bilateral candidates and
the assertions, and produced the verdict in `tmp/eval-runs/issue-188-docs/judge/verdict.md`.

## Latest result

- Behavior result: `PASS`（with）/ `PASS`（without）— 本轮 #238 fresh 隔离重跑（2026-08-06）
- Coverage result: `PARTIAL`（with）/ `PARTIAL`（without）— Git 缺失导致成功事务未执行
- Overall result: BLOCKED
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `PASS` / Coverage `PARTIAL`
- without_skill：Behavior `PASS` / Coverage `PARTIAL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| verifies_complete_affected_set | NOT_EXERCISED | NOT_EXERCISED | 两条 lane 的 change-map 均列出 required docs，但因无 Git 无法解析 immutable target tree，完整 affected-set 核验未执行。 |
| stamps_all_pages_together | NOT_EXERCISED | NOT_EXERCISED | 统一盖章依赖前置 Git target-tree 核验；两条 lane 均在该基础设施门禁前停止并保持原版本。 |
| verifies_release_metadata_read_only | PASS | PASS | `docs/site/.meta/releases.json` 的 `latest` 与两个 API 条目均为 `v1.1.0`；`.eval/actual-diff.patch` 未包含该文件修改。 |
| normalizes_mixed_version_forms | PASS | PASS | Release Notes、索引和 `releases.json` 使用 `v1.1.0`，`package.json` 使用 `1.1.0`；两者可规范化为同一 SemVer。 |
| persists_candidate_producer_schema | NOT_EXERCISED | NOT_EXERCISED | 审计报告只有 `blocked` 诊断报告，不是 candidate record；缺少可解析 Git refs，无法执行候选记录生成与 staged gate。 |
| anchors_candidate_then_discovers_success | NOT_EXERCISED | NOT_EXERCISED | `docs/site/.meta/audit/handoffs/pre-tag-v1.1.0.md` 不存在，且两条 lane 均明确未创建 anchor、handoff 或返回 `ready_for_tag`。 |

未触发断言：`verifies_complete_affected_set`、`stamps_all_pages_together`、`persists_candidate_producer_schema`、`anchors_candidate_then_discovers_success`

基础设施阻塞说明：Git 仓库缺失；对应断言不构成 skill 行为回归。



## Fixture Drift Notice

fixture 身份文本已于 2026-07-29 从 issue 编号更新为 skill 名，旧 PASS 反映变更前 run。**2026-08-03（#188）已对当前 fixture 完成 fresh re-baseline**（with/without 双侧验证，judge 独立判定，证据见 `tmp/eval-runs/issue-188-docs/`），BLOCKED 状态消解；本节保留作为历史记录。

## Historical results
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 2026-07-20（fixture 身份文本变更前）：旧 run 结果，按 Fixture Drift Notice 不再作为当前证据。

## Canonical digest verification

> ⚠️ 本节为 2026-08-03 #188 历史轮执行证据；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

The with-skill run reconstructed the exact six-field inventory rather than
trusting the fixture literals. It sorted **6 entries** by `source_id`:
`actual_tag`, `host_package`, `release_index`, `release_metadata`,
`release_notes`, and `target_version`. Each object contains exactly
`source_id`, `locator_kind`, `locator`, `selector`, `extractor`, and
`required_raw_form`; compact RFC 8259 JSON uses sorted object keys, UTF-8, no
insignificant whitespace, and no trailing newline.

- Recomputed v1.1.0 inventory digest:
  `sha256:109170c373e9aab353ff234d73d7fb28ca70e464cab3d2019dfa79928365a787`
- Fixture inventory digest:
  `sha256:109170c373e9aab353ff234d73d7fb28ca70e464cab3d2019dfa79928365a787`
- Recomputed empty prior-lineage digest from exact bytes `[]`:
  `sha256:4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`
- Fixture genesis digest:
  `sha256:4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`

Both comparisons are exact matches. The `actual_tag` entry is
`git-ref / refs/tags/v1.1.0 / tag-name / git-tag-name-v1 / vX.Y.Z`; its
pre-tag value remains `pending_expected_absent`, so expected absence is not a
version mismatch and does not represent publication.

## Assertion results
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

| Assertion | without_skill | with_skill | Evidence summary |
| --- | --- | --- | --- |
| `verifies_complete_affected_set` | PASS | PASS | The endpoint diff matches `src/catalog/**`; both required API pages are included and their method, path, auth, query, success, error, streaming, and file claims match the route evidence. Exactly **2/2 affected pages** are `verified`, with zero unresolved gaps. |
| `stamps_all_pages_together` | PASS | PASS | Exactly **4 pages** form the unified stamp set: two API pages, v1.1.0 Release Notes, and the Markdown index. They are updated and read back together as `v1.1.0` only after the complete set passes. |
| `verifies_release_metadata_read_only` | PASS | PASS | `.meta/releases.json` agrees with the target version and remains read-only; no candidate delta includes it. |
| `normalizes_mixed_version_forms` | PASS | PASS | Required `v1.1.0` sources and package `1.1.0` pass source-form validation and normalize to the same case-sensitive SemVer identity. |
| `persists_candidate_producer_schema` | FAIL | PASS | The baseline can repeat the supplied digest literal but cannot reconstruct the exact six-entry/six-field canonical inventory or prove the genesis digest, and it lacks the full identity, per-page blob/hash, lineage, dual-gate, and no-premature-success producer contract. The skill-guided result recomputes both digests exactly and requires the complete fixed-path candidate with conclusion only `candidate_verified`. |
| `anchors_candidate_then_discovers_success` | FAIL | PASS | The baseline does not make committed raw metadata/content/tree/blob confirmation, fixed discovery, handoff-only commit, external package, normal fast-forward integration, and integrated readback one indivisible success gate. The skill does. |

## With-skill behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

The skill keeps `base_ref`, `target_ref`, and the maintainer-confirmed target
version independent, accepts the absent future tag for pre-tag, verifies all
facts from target-tree ordinary blobs, and keeps `.meta/releases.json`
read-only. It builds the four-page stamp and fixed candidate only in an
isolated worktree/branch/index. The candidate records the complete producer
schema, actual-tag pending contract, exact recomputed inventory and prior
lineage digests, and only `candidate_verified`—never `ready_for_tag`, success
time, containing commit/tree, or post-commit confirmation.

The initial and atomically replaced final candidate each pass the complete raw
metadata, unfolded name-status, summary, and full binary-patch gate. Only then
is the anchor committed and checked. The fixed discovery is written only after
anchor confirmation, then committed as the sole handoff delta and anchored by
the external package. `ready_for_tag` is returned only after normal
fast-forward integration and integrated readback, and is explicitly not a
publication result.

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- `with_skill`: none.
- `without_skill`: `persists_candidate_producer_schema` and
  `anchors_candidate_then_discovers_success` fail.

## Next steps

> ⚠️ 本节为 2026-08-03 #188 历史轮后续建议；当前 #238 重跑因 Git 仓库缺失保持 `BLOCKED`。

No skill change is required. Preserve the exact canonical digest input schema,
actual-tag pending entry, genesis bytes `[]`, and anchor/discovery/integration
ordering in future edits.

## Runtime artifact policy

> ⚠️ 本节仅描述 2026-08-03 #188 历史轮运行产物；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

- Runtime artifacts（双侧 candidate、judge verdict、隔离目录执行产物）在本次 fresh re-baseline 中真实生成，位于被 gitignore 覆盖的 `tmp/eval-runs/issue-188-docs/`；未提交到 git。长期 durable 产物仅为本 `comparison.md`。
