# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-004-audit-all-verified`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897` from `agents/docs/test/docs-audit/evals/workspace/eval-004-audit-all-verified`.
- Fixture SHA-256: `085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897`
- Prompt SHA-256: `f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9e9abf391c9ccd9564d35b5def50bc0374b1db0886710676c4d48422839746ae`
- Skill overlay SHA-256: `c66ac938bf9158faa694d7c3e311e913ddc4a06da11de703a881234f257c470c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `9d29cd503dc3f38e1235bc8d674c667f9fc3bef38d94569b7888bb0dfed80506`
- Metadata SHA-256: `4c1ab6c77122f43adf1cbc9d6f05aea7b2b047fe1e69ba225e32d03f006dc954`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `verifies_complete_affected_set` | PASS | with_skill 的 candidate record 列出 change-map 命中的两个 API 页面及 Release Notes 页和索引，逐页标记 verified，并明确无 blockers/unresolved gap。 |
| `stamps_all_pages_together` | PASS | candidate record 记录两张 API 页统一从 v1.0.0 更新为 v1.1.0；Release Notes 页和索引本已为 v1.1.0，最终四个受审页面一致。 |
| `verifies_release_metadata_read_only` | PASS | 记录核对了 docs/site/.meta/releases.json，声明其只读且未修改；manifest 中其 SHA-256 与初始值一致。 |
| `normalizes_mixed_version_forms` | PASS | version-source inventory 同时列出带 v 的来源、package.json 的无 v 版本，并统一规范化为 1.1.0；actual tag 明确为 pre-tag pending_expected_absent。 |
| `persists_candidate_producer_schema` | FAIL | 虽生成固定路径 candidate record 并结论为 candidate_verified，但缺少断言要求的完整 schema：逐页 mode/type/blob 与章后哈希、六字段 locator contract、canonical-json-rfc8259-sorted-v1 实算 digest、两次 staged gate inventory 等。 |
| `anchors_candidate_then_discovers_success` | FAIL | 虽有 anchor/handoff 文件和 ready_for_tag 结果，但 raw evidence 未提供要求的完整 post-stamp anchor 确认字段及外部包补充的 handoff commit/tree/path/blob、fast-forward 集成与回读证据，因此 ready_for_tag 是不受完整证据支持的声明。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c; fixture_sha256=085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897; output_sha256=8ee828113b0c8d62f5967c7a59c22860b163529faf11fc6b84132db2aabb0367; snapshot_sha256=1b554ebf60d81a2dece8c1a50ad3541bc9e7d5639d4fb2fc1b7d9dff82545ad5
- Behavior: 核对并生成了 candidate record，更新两张 API 页面，保留 release metadata 只读，并提交了 anchor/handoff；但 candidate schema 和最终 handoff 证据不完整。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c; fixture_sha256=085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897; output_sha256=a4ca00cf963e0c48264cf559e1129aa6110251e86d46994b939de6a5c1b6db2b; snapshot_sha256=d574c6ce38ef03b6b77cf01d014af6ad4043bd719d50527805a56429979fb387
- Behavior: 仅创建了 workspace 外的普通 release-evidence 报告；未修改正式文档、未生成固定 audit/handoff 记录，也未执行统一盖章。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- candidate producer record 未满足完整 schema 与 digest/gate inventory 要求。
- ready_for_tag 缺少完整 anchor 确认及外部 handoff 集成证据。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

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
- Fixture version/source: canonical manifest `085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897` from `agents/docs/test/docs-audit/evals/workspace/eval-004-audit-all-verified`.
- Fixture SHA-256: `085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897`
- Prompt SHA-256: `f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2d24da5f976a5ab2710c2c072a19015e074d314e0ebdb88f1c28831425f1b98c`
- Skill overlay SHA-256: `40330c17a3b77f25a1b1a716fa5e9355e0011db79d19014344ed516affba11c8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `9d29cd503dc3f38e1235bc8d674c667f9fc3bef38d94569b7888bb0dfed80506`
- Metadata SHA-256: `4c1ab6c77122f43adf1cbc9d6f05aea7b2b047fe1e69ba225e32d03f006dc954`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `verifies_complete_affected_set` | PASS | The with_skill candidate identifies both change-map-required API pages plus the release page and index, reports page-by-page fact verification, and marks all affected pages verified with no unresolved gap. |
| `stamps_all_pages_together` | PASS | The candidate records the four-page unified stamp set; both API markers changed to v1.1.0 and the release page and index already carried v1.1.0. |
| `verifies_release_metadata_read_only` | PASS | The candidate reports releases.json values as matching v1.1.0 and git evidence shows no metadata modification. |
| `normalizes_mixed_version_forms` | PASS | The candidate includes the required version-source inventory, distinguishes v-prefixed sources from package.json's unprefixed version, normalizes all to 1.1.0, and marks comparisons verified. |
| `persists_candidate_producer_schema` | FAIL | The candidate record is candidate_verified, but lacks the required complete target-tree mode/type/blob evidence, chapter before/after values, precise claim code/test blob evidence, post-stamp SHA-256, six-field locator contract, canonical inventory algorithm/digest details, staged gate inventories, and complete readback evidence. |
| `anchors_candidate_then_discovers_success` | FAIL | The handoff is included in the final fast-forward commit, but raw git evidence does not establish the required complete target_ref..anchor confirmation, separate handoff-only commit, external package integration, or consistent candidate blob/anchor lineage; the handoff references an unreachable anchor commit and a different candidate blob. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c; fixture_sha256=085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897; output_sha256=08d3e56c9cf159338038c82a5dc0023b6c4663d8c10724629d0f12eb85c00b23; snapshot_sha256=12a26856d17504e9c7d6f49295c216f00854818dd5eb22193c4fcd380e1e7dfb
- Behavior: Updated the two API markers and created audit/handoff records, but claimed ready_for_tag without satisfying the required candidate schema and anchor/discovery transaction evidence.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c; fixture_sha256=085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897; output_sha256=8c4c48f79a7ff9faa348ebffe5689decef4169dbb514e98fbae307cf20fc9cbe; snapshot_sha256=dafd65aa9e444d2525abefec0be6ada9333414efbb0d52b10fa2707950ee8345
- Behavior: Produced an untracked conditional-pass report, left all documentation markers unchanged, and did not create commits or handoff records.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- verifies_complete_affected_set
- stamps_all_pages_together
- verifies_release_metadata_read_only
- normalizes_mixed_version_forms
- persists_candidate_producer_schema
- anchors_candidate_then_discovers_success
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

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

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

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
