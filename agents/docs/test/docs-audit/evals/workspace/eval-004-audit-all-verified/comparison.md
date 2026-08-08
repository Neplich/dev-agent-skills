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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8588a4fc6bb55ff6a1ce485f659334cabf6f9624098f4db4f1066bdacc1fc3ec`
- Skill overlay SHA-256: `09c184e9256c59e7718f2b61600ec30436b550d1692a7c65f8b8e6c64fc491f3`
- Judge schema SHA-256: `a043187f1d82deb6ceb1f6f2a8dbb12db6dd01c71ced16d224de3ae50ca31c3b`
- Eval definition SHA-256: `9d29cd503dc3f38e1235bc8d674c667f9fc3bef38d94569b7888bb0dfed80506`
- Metadata SHA-256: `4c1ab6c77122f43adf1cbc9d6f05aea7b2b047fe1e69ba225e32d03f006dc954`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `verifies_complete_affected_set` | PASS | With-skill candidate records all four affected pages as verified with no unresolved evidence gap; final stamped page snapshots are present. |
| `stamps_all_pages_together` | PASS | Final snapshots show all four required surfaces at v1.1.0, and the candidate records a unified stamp set with successful read-back. |
| `verifies_release_metadata_read_only` | PASS | Release metadata remains unchanged in the final manifest and is explicitly audited as read-only. |
| `normalizes_mixed_version_forms` | PASS | The candidate inventory records prefixed and unprefixed sources, their raw forms, normalized SemVer values, and matching comparison results. |
| `persists_candidate_producer_schema` | PASS | The reachable candidate record contains the required schema, evidence, inventories, digests, staged gates, read-back commands, and candidate_verified conclusion without ready_for_tag or post-commit fields. |
| `anchors_candidate_then_discovers_success` | PASS | Locked git evidence shows candidate, anchor, handoff, and fast-forward commits; the final handoff snapshot contains ready_for_tag discovery metadata and final confirmation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c; fixture_sha256=085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897; output_sha256=9ea839124b6074d747cba3957e5de386641ed4bae73f3f6693c75d987cb7b704; snapshot_sha256=acf4e1a516b0333f8cd4cdae012b72808d7ac7311a7beef62c17d3621bcfd788
- Behavior: Completed the documentation audit, persisted the candidate and handoff records, stamped the required pages, and returned ready_for_tag without creating a tag.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c; fixture_sha256=085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897; output_sha256=55b450d620370fbd825c4c3c1e56fecd8215255d744b6e756266089d6ecdbb5a; snapshot_sha256=9247dc286f355dc7e7351dbe582724d218bb7d11dbfe5340c27e67ed6c0ea897
- Behavior: Produced a standalone audit report identifying the metadata inconsistency, but did not stamp pages or create the required audit/handoff records.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8588a4fc6bb55ff6a1ce485f659334cabf6f9624098f4db4f1066bdacc1fc3ec`
- Skill overlay SHA-256: `09c184e9256c59e7718f2b61600ec30436b550d1692a7c65f8b8e6c64fc491f3`
- Judge schema SHA-256: `a043187f1d82deb6ceb1f6f2a8dbb12db6dd01c71ced16d224de3ae50ca31c3b`
- Eval definition SHA-256: `9d29cd503dc3f38e1235bc8d674c667f9fc3bef38d94569b7888bb0dfed80506`
- Metadata SHA-256: `4c1ab6c77122f43adf1cbc9d6f05aea7b2b047fe1e69ba225e32d03f006dc954`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `verifies_complete_affected_set` | PASS | Candidate record covers both change-map required docs and all four affected pages, each marked `verified`, with `blockers: []`. |
| `stamps_all_pages_together` | PASS | The four-page unified stamp set is recorded; both API pages are updated to `v1.1.0`, while the release notes and index already have that value, and the changes are committed together. |
| `verifies_release_metadata_read_only` | PASS | The release metadata hash is unchanged and its values are recorded as read-only source locators. |
| `normalizes_mixed_version_forms` | PASS | The inventory records raw and normalized values for v-prefixed sources and the unprefixed package version, all normalizing to `1.1.0`. |
| `persists_candidate_producer_schema` | FAIL | The candidate record lacks explicit comparison results and precise code/test blob evidence required by the schema; code evidence is only a commit/path reference. |
| `anchors_candidate_then_discovers_success` | FAIL | The handoff references candidate blob `93f82fa...`, but the locked delivered candidate record has SHA-256 `d727fa...`; the evidence also does not establish the required external-package handoff confirmation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c; fixture_sha256=085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897; output_sha256=ff71c307e9ca553035585db5f5b1e2ac389f12af5756abe99641bb6cc073f7fb; snapshot_sha256=49e2eba4c992e2b76c6455b97fad6a11b73e62ea09625c16e028b7af930e29b0
- Behavior: Updated the API verification stamps and created candidate, anchor, and handoff artifacts, but the candidate schema and lineage evidence are inconsistent.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c; fixture_sha256=085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897; output_sha256=fbd7a593fc7800b479f62c87412aa17f9e33f95845273b8905b4b049f8673c1b; snapshot_sha256=59504bcc7a49b5662c8112307321177a561278dd7e440a2d71a956be5ca78123
- Behavior: Produced a read-only conditional audit identifying stale API metadata, without applying the required updates or handoff workflow.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The candidate producer record does not satisfy the complete evidence/schema contract.
- The anchor-to-handoff lineage is inconsistent and the full handoff confirmation is unsupported.
- Next: Regenerate the complete candidate record with explicit comparison and code/test blob evidence.
- Next: Re-anchor and recreate the handoff so its candidate blob matches the final candidate record and confirm the external integration evidence.

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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a40b9426c3ece6f787614183ce8478f0aacaf94802441ebb84796853c2c8848e`
- Skill overlay SHA-256: `6cbf5a99cea4bf2bfd3e91f9b1e261a828b8b62ab73699f7ed3de43f33d01739`
- Judge schema SHA-256: `a043187f1d82deb6ceb1f6f2a8dbb12db6dd01c71ced16d224de3ae50ca31c3b`
- Eval definition SHA-256: `9d29cd503dc3f38e1235bc8d674c667f9fc3bef38d94569b7888bb0dfed80506`
- Metadata SHA-256: `4c1ab6c77122f43adf1cbc9d6f05aea7b2b047fe1e69ba225e32d03f006dc954`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `verifies_complete_affected_set` | PASS | 候选记录列出两个 change-map required docs、四个 affected pages，逐页 final_status 均为 verified，且 blockers 为空。 |
| `stamps_all_pages_together` | PASS | 锁定的最终文件中四个页面的 last_verified_version 均为 v1.1.0；git evidence 显示 API 页在同一候选/集成变更中更新，Release Notes 页面原已为目标版本。 |
| `verifies_release_metadata_read_only` | PASS | releases.json 的锁定内容未变，候选 inventory 记录 latest 与 target_release_version 均为 v1.1.0，git diff 未包含该文件。 |
| `normalizes_mixed_version_forms` | PASS | 候选 inventory 正确记录带 v 与不带 v 的来源形式，并将其归一化为 1.1.0；actual tag 明确为 pending_expected_absent。 |
| `persists_candidate_producer_schema` | PASS | 固定路径 candidate 文件包含 schema、attempt/phase、不可变 refs、影响域、逐页 tree/stamp/evidence/hash、版本 inventory、digest、两阶段 inventory、回读、命令和 candidate_verified 结论，未包含 ready_for_tag 或 post-commit 结果。 |
| `anchors_candidate_then_discovers_success` | FAIL | 锁定 handoff 声称 anchor_commit 为 ee1eae7，但该 commit 在 git evidence 中 final_reachable=false；最终可达 041311e 提交同时包含 candidate、handoff 和 API 修改，并非只含 handoff 路径；handoff 的 candidate_record_blob 也与实际 candidate blob 不一致。因此其 ready_for_tag 交接链未被完整确认。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c; fixture_sha256=085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897; output_sha256=9c63860f02b9829d32b1110bdb5592ddaf1b8fba3c852aaee78587a1503e4d22; snapshot_sha256=83a91a53361e74e72c01e5f4237f8a9292bb20c5857f96bf77968fee3e53167e
- Behavior: 完成四页核验、API 页面盖章、候选记录和 handoff 交付，但最终 anchor/handoff 链不完整且自相矛盾。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c; fixture_sha256=085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897; output_sha256=3108f4c49b9bc5c15d5f46e7f96fc6b7f939c79a0852ee877c6e3d7c92896a97; snapshot_sha256=99f5df196269c857be0f6a730540346617af041f9ba9edc62e697014236a9ad8
- Behavior: 仅生成未纳入固定审计路径的报告，未更新页面或创建候选/handoff 记录；作为新鲜基线对照。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill lane 的 handoff/anchor 证据存在可验证矛盾，不能支持完整的 ready_for_tag discovery 流程。
- Next: 重新生成并确认可达的 post-stamp anchor、仅含 handoff 路径的 handoff commit，以及与实际 candidate blob 匹配的 handoff 元数据。

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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a40b9426c3ece6f787614183ce8478f0aacaf94802441ebb84796853c2c8848e`
- Skill overlay SHA-256: `6cbf5a99cea4bf2bfd3e91f9b1e261a828b8b62ab73699f7ed3de43f33d01739`
- Judge schema SHA-256: `a043187f1d82deb6ceb1f6f2a8dbb12db6dd01c71ced16d224de3ae50ca31c3b`
- Eval definition SHA-256: `9d29cd503dc3f38e1235bc8d674c667f9fc3bef38d94569b7888bb0dfed80506`
- Metadata SHA-256: `4c1ab6c77122f43adf1cbc9d6f05aea7b2b047fe1e69ba225e32d03f006dc954`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `5a4d229da9707c7ce22c80b66e92baafd2ef50f8fc9733b6b61f658aabf3dd17`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `verifies_complete_affected_set` | PASS | The candidate record enumerates both change-map-required API docs plus the release page and index, marks all four verified, and reports no blockers or unresolved evidence gaps. |
| `stamps_all_pages_together` | PASS | Locked git blobs show both API pages stamped to v1.1.0 while the release page and index already carry v1.1.0; the candidate records the unified affected and stamp sets and staged convergence. |
| `verifies_release_metadata_read_only` | PASS | docs/site/.meta/releases.json remains unchanged in the manifest, while the candidate records target-tree metadata and read-only comparison evidence. |
| `normalizes_mixed_version_forms` | PASS | The candidate inventory explicitly records v-prefixed release forms, the unprefixed package.json form, normalized SemVer 1.1.0 equality, and the canonical normalization algorithm. |
| `persists_candidate_producer_schema` | PASS | The locked audit-v1.1.0.md blob contains candidate schema, attempt/phase, immutable refs, affected/stamp sets, per-page tree locators and evidence, SHA-256 values, complete version inventory including pending tag, canonical digest, staged gates, commands, and candidate_verified; it contains no ready_for_tag or post-commit success fields. |
| `anchors_candidate_then_discovers_success` | FAIL | The handoff claims ready_for_tag, but locked git evidence shows no commit containing only docs/site/.meta/audit/handoffs/pre-tag-v1.1.0.md and no external-package supplement with the required commit/tree/path/blob; the final integration commit contains the handoff together with the audit record and API changes. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c; fixture_sha256=085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897; output_sha256=9dac924f14e1449802a62e6d05dae98a53f2fb17fe28f6ad994133341f80b920; snapshot_sha256=7352c1c49424e1cd57f6004ef44492d2b41fba74b81533514096ce4b46184449
- Behavior: Audited and stamped the affected documentation, preserved release metadata, persisted a detailed candidate record, and produced a ready_for_tag handoff, but did not satisfy the required isolated handoff commit and external supplement sequence.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c; fixture_sha256=085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897; output_sha256=8053e63a83e0af5236fe461cc77676c30ed8e2635a0342357532e444ff615309; snapshot_sha256=d5e9037ce838a1eded7db6bdfd63f4fcdc85b022e0fe1f28d30f77ebbfe1296b
- Behavior: Produced a report only; left API pages at v1.0.0 and identified the release metadata conflict, with no formal audit changes.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill lane claims ready_for_tag despite lacking evidence of the required handoff-only commit and external-package supplement/readback sequence.
- Next: Create and verify a commit containing only docs/site/.meta/audit/handoffs/pre-tag-v1.1.0.md, record the external package supplement commit/tree/path/blob, then fast-forward integrate and re-read before returning ready_for_tag.

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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a40b9426c3ece6f787614183ce8478f0aacaf94802441ebb84796853c2c8848e`
- Skill overlay SHA-256: `6cbf5a99cea4bf2bfd3e91f9b1e261a828b8b62ab73699f7ed3de43f33d01739`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `9d29cd503dc3f38e1235bc8d674c667f9fc3bef38d94569b7888bb0dfed80506`
- Metadata SHA-256: `4c1ab6c77122f43adf1cbc9d6f05aea7b2b047fe1e69ba225e32d03f006dc954`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `verifies_complete_affected_set` | PASS | with_skill audit records all four affected pages as verified and reports no stale, mismatch, or unresolved factual evidence. |
| `stamps_all_pages_together` | FAIL | with_skill explicitly states that no unified version stamp was executed, although all affected pages were reported verified. |
| `verifies_release_metadata_read_only` | PASS | with_skill inventories docs/site/.meta/releases.json, confirms the v1.1.0 values, and git evidence shows no file modification. |
| `normalizes_mixed_version_forms` | PASS | with_skill records normalization of v1.1.0 sources to 1.1.0, preserves package.json as unprefixed 1.1.0, and identifies the expected absent tag as pending. |
| `persists_candidate_producer_schema` | FAIL | The delivered audit file is phase_result blocked rather than candidate_verified and lacks the required candidate record, gate inventories, detailed evidence fields, post-stamp hash, and other schema elements. |
| `anchors_candidate_then_discovers_success` | NOT_EXERCISED | No candidate, anchor, or handoff commit was created, so the later anchoring and discovery workflow cannot be evaluated from the delivered execution. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c; fixture_sha256=085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897; output_sha256=00f55ed4326e9714eb1c6fd6674db98b06fda98f125f727a7cd034714b4256d0; snapshot_sha256=41ec57bc6384b822f22963cdfba143a1f079694b319a4a6f461ce1e10a1c94f8
- Behavior: Created a structured pre-tag audit identifying the affected pages as factually verified and normalizing versions, but incorrectly treated the confirmed release-notes handoff as missing and stopped before stamping or producing candidate artifacts.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c; fixture_sha256=085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897; output_sha256=79635595257745be0a53fb82db3917929f99a888b841b997fe1fd6f559fed065; snapshot_sha256=e0a2324807264a1db2bea6a29c2e3c7d04300c4268d91cd5d53290202ce5ca6e
- Behavior: Saved a prose report, identified stale API verification markers, and made no repository commit or page updates.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill lane omitted the required unified page and release-Markdown stamp.
- The with_skill delivery was blocked and did not produce the required candidate_verified producer record.
- The claimed missing release-notes handoff conflicts with the locked fixture evidence showing confirmed status.
- Next: Use the confirmed release-notes handoff evidence, perform the unified stamp, and generate the complete candidate record before attempting anchor and discovery steps.

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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a40b9426c3ece6f787614183ce8478f0aacaf94802441ebb84796853c2c8848e`
- Skill overlay SHA-256: `6cbf5a99cea4bf2bfd3e91f9b1e261a828b8b62ab73699f7ed3de43f33d01739`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `9d29cd503dc3f38e1235bc8d674c667f9fc3bef38d94569b7888bb0dfed80506`
- Metadata SHA-256: `4c1ab6c77122f43adf1cbc9d6f05aea7b2b047fe1e69ba225e32d03f006dc954`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `verifies_complete_affected_set` | PASS | Candidate record identifies both required API documents, records page-by-page verified status, and reports no unresolved evidence gap. |
| `stamps_all_pages_together` | PASS | Locked snapshots show both API pages stamped v1.1.0; the Release Notes page and index already carry v1.1.0 and are included in the unified stamp/readback set. |
| `verifies_release_metadata_read_only` | PASS | The candidate inventory verifies releases.json and its manifest hash is unchanged; no modification is shown. |
| `normalizes_mixed_version_forms` | PASS | The candidate record includes the required source forms, normalizes v1.1.0 and 1.1.0 to SemVer 1.1.0, and includes the actual-tag pending entry. |
| `persists_candidate_producer_schema` | PASS | The locked candidate record contains candidate_verified, immutable refs, affected and stamp sets, page/blob evidence, version-source locator inventory, canonical inventory and lineage digests, staged inventories, readback evidence, and review commands without ready_for_tag or post-commit result fields. |
| `anchors_candidate_then_discovers_success` | NOT_EXERCISED | The evidence shows a ready_for_tag handoff and integrated commit, but does not directly prove that the handoff was created in a commit containing only that path together with the complete external handoff commit/tree/path/blob readback contract. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c; fixture_sha256=085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897; output_sha256=7b750056a19be9f15fed5fbe24bc715f0b3be6d17210ae6553c35558e32da727; snapshot_sha256=8200603f19e6c48750b4077c78b6b233eaad9d14d3d48f560b8e8ff9e40a73e5
- Behavior: Produced and integrated the candidate audit, stamped the API pages, preserved release metadata, recorded normalized evidence, and reported ready_for_tag; the final handoff-only commit contract is not fully directly evidenced.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c; fixture_sha256=085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897; output_sha256=fd57e43f1dc4f8a38eba214527cf0197ce64afc9b59c4d0d3ea0a63f05973332; snapshot_sha256=beadc7192cdb7f93c84d70f0bb470777baeff913e01b54957cd25e1f5d9a4ea5
- Behavior: Saved a separate report, left the worktree with an untracked file, identified the metadata conflict, and did not perform the required audit/stamping workflow.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5966d0a29df39d7d8fb5c9be9181fc2cdb7b15c5bfd70164d13594692a24601b`
- Skill overlay SHA-256: `a8c63c52f42aa02d6c7d9974165a4661e6346623c534d7d516ef50e982500617`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `9d29cd503dc3f38e1235bc8d674c667f9fc3bef38d94569b7888bb0dfed80506`
- Metadata SHA-256: `4c1ab6c77122f43adf1cbc9d6f05aea7b2b047fe1e69ba225e32d03f006dc954`
- Executor SHA-256: `6c1c50885619c5add1ae9c7d9faf1fa39e905346d86059a01403ae742d286478`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `verifies_complete_affected_set` | PASS | The with_skill candidate record lists all four affected pages, marks each verified, and reports no blockers or unresolved evidence gap. |
| `stamps_all_pages_together` | PASS | The locked candidate record and git snapshot show the two API pages updated to v1.1.0 while the Release Notes page and index already had v1.1.0; the unified stamp set was read back. |
| `verifies_release_metadata_read_only` | PASS | The release metadata version matches v1.1.0, and locked git evidence shows no modification to docs/site/.meta/releases.json. |
| `normalizes_mixed_version_forms` | PASS | The candidate record explicitly records raw prefixed and unprefixed values, normalization to 1.1.0, matching results, and the expected absent tag. |
| `persists_candidate_producer_schema` | FAIL | The candidate file contains the forbidden literal `ready_for_tag` in its final explanatory paragraph, and its source-locator section does not provide the required complete six-field locator contract for every source. |
| `anchors_candidate_then_discovers_success` | NOT_EXERCISED | The locked evidence shows candidate, anchor, handoff, and final commits, but does not fully prove the required ordering and the handoff commit containing only the handoff path with complete external commit/tree/path/blob confirmation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c; fixture_sha256=085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897; output_sha256=db268c316a0c826de7027316dd4fdbd8f2c9a99728b3ae3b2707d82597d022b9; snapshot_sha256=4fda892acd18a3ef7a781b92e768b06f4e63d70166a7b548d1c177b7086043c1
- Behavior: Audited and stamped the affected documentation, created candidate and handoff records, and integrated commits; the candidate schema has a forbidden ready_for_tag reference and incomplete locator details.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c; fixture_sha256=085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897; output_sha256=c4da11b472e837015a00ed86fcc4066fb7689eb2689c8b72ee6700445efe8cbb; snapshot_sha256=5c310e9f8e59705d3457fba5e2b3a2ac0ad960ccd28c570ac210f62d6ddd8618
- Behavior: Created an ad hoc release-evidence report only; left the worktree unchanged and reported unresolved metadata/version issues.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- persists_candidate_producer_schema fails because the candidate record includes `ready_for_tag` and lacks the complete required locator contract.
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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `45d27392cd49bf15e334bac5545e255c08c8e0d6f5d3e48c16e46ffadfa40185`
- Skill overlay SHA-256: `616b45956bb1db6bdbd7ad6ef23b3fcf791f7e2616f000bc8b52d859654ab6da`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `9d29cd503dc3f38e1235bc8d674c667f9fc3bef38d94569b7888bb0dfed80506`
- Metadata SHA-256: `4c1ab6c77122f43adf1cbc9d6f05aea7b2b047fe1e69ba225e32d03f006dc954`
- Executor SHA-256: `6c1c50885619c5add1ae9c7d9faf1fa39e905346d86059a01403ae742d286478`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `verifies_complete_affected_set` | PASS | Candidate record lists the two change-map required API docs plus both Release Notes surfaces, gives per-page claims and target-tree evidence, and marks all four verified with no blockers or unresolved gaps. |
| `stamps_all_pages_together` | PASS | Locked git evidence shows both API pages changed to v1.1.0 in the candidate/anchor flow; the two Release Notes files already contain v1.1.0, and the candidate record reports a unified four-page stamp set with successful readback. |
| `verifies_release_metadata_read_only` | PASS | The candidate inventory records releases.json latest and released entries as v1.1.0, while locked git diffs show no modification to releases.json. |
| `normalizes_mixed_version_forms` | PASS | The candidate record explicitly records v1.1.0 raw/normalized as 1.1.0, package.json raw 1.1.0, and all release metadata/notes sources raw v1.1.0, with component-wise equality. |
| `persists_candidate_producer_schema` | FAIL | The candidate record exists at the required path and concludes candidate_verified, but it omits required complete locator-contract fields and exact canonical-json-rfc8259-sorted-v1 naming, records only one staged-gate inventory rather than two, and does not contain the required complete post-stamp SHA-256/schema evidence. |
| `anchors_candidate_then_discovers_success` | FAIL | The handoff claims ready_for_tag and fast-forward integration, but locked evidence lacks the required complete anchor confirmation fields and external handoff-commit/readback proof; additionally, handoff record_blob 5d90ad3... contradicts the delivered audit file SHA-256 f87f94ae.... |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c; fixture_sha256=085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897; output_sha256=7033b1f50c37fd3b1b64eca4adb8f97ade8bf967a46ebaad14a477c4277e0d76; snapshot_sha256=e87a4844706f3c755a05632b8ac3acaa475f4a81b2c87370a401c6e58188dfa9
- Behavior: Verified and stamped the affected documentation, preserved releases.json, created candidate and handoff artifacts, and fast-forwarded integration, but overstated readiness and failed the required candidate-schema and anchor/handoff evidence requirements.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c; fixture_sha256=085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897; output_sha256=bb9d1e85280353ccd9090286879c6f91f97e0667f2afa923650c85cef2f69f7f; snapshot_sha256=18f4b9a1f49f8fdfd5c508ead90a70c7f1efa3b0c87dbfe1ef243a7c81ba165f
- Behavior: Produced only an untracked audit report, made no repository changes, and reported metadata/version-stamp problems rather than completing the audit workflow.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- persists_candidate_producer_schema is not satisfied by the incomplete candidate record schema and staged-gate evidence.
- anchors_candidate_then_discovers_success is contradicted by incomplete confirmation evidence and the handoff record_blob mismatch.
- Next: Regenerate the candidate record with the complete required schema, locator contract, canonical digest, two staged-gate inventories, and post-stamp hash evidence.
- Next: Re-run anchor and handoff confirmation, including complete target_ref..anchor evidence and matching candidate blob identity before returning ready_for_tag.

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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `7c0f91bb371a1fed70a6062246798b7923ededb39ec9484b8ac28dc701e2b627`
- Skill overlay SHA-256: `711cdcc6277bd3c611c1c6b223145505abdb64b2093d96af87cbf17f59a18497`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `9d29cd503dc3f38e1235bc8d674c667f9fc3bef38d94569b7888bb0dfed80506`
- Metadata SHA-256: `4c1ab6c77122f43adf1cbc9d6f05aea7b2b047fe1e69ba225e32d03f006dc954`
- Executor SHA-256: `6c1c50885619c5add1ae9c7d9faf1fa39e905346d86059a01403ae742d286478`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `verifies_complete_affected_set` | FAIL | with_skill verifies the two API pages but explicitly records an incomplete release handoff and unresolved version-source evidence gap, contradicting the requirement for no unresolved evidence gap. |
| `stamps_all_pages_together` | NOT_EXERCISED | The with_skill report explicitly says pages were not stamped because the required handoff/inventory prerequisite was missing. |
| `verifies_release_metadata_read_only` | PASS | The with_skill report records that releases metadata contains v1.1.0 for both API pages, identifies it as read-only, and git evidence shows no repository mutation. |
| `normalizes_mixed_version_forms` | PASS | The with_skill report explicitly normalizes v1.1.0 and 1.1.0 to the same SemVer identity and inventories the prefixed release sources versus unprefixed package.json version. |
| `persists_candidate_producer_schema` | FAIL | The delivered audit file is a blocked pre-tag report, not the required candidate_verified record, and omits the required complete schema, staged gates, evidence locators, digests, and other candidate-record fields. |
| `anchors_candidate_then_discovers_success` | NOT_EXERCISED | The with_skill report correctly stops before candidate, anchor, handoff, and ready_for_tag creation because the required producer handoff/inventory is missing. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c; fixture_sha256=085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897; output_sha256=8d56663d8cd2c09e2487e6e4d3d905e69f48a0b5153b7a9d0ff7c265187699ae; snapshot_sha256=01e3f3e37f08ed3c93158c05a2b4435db3be2ad79b5b1b27bad4197cf07d5157
- Behavior: Created the fixed-path audit report, verified page and version facts, and blocked before stamping or creating candidate/anchor/discovery artifacts because the required producer handoff inventory was incomplete.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c; fixture_sha256=085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897; output_sha256=ec692484411642f90e32ac5a4d5ea779f77ff38c96a12c0debb549051a9eab97; snapshot_sha256=59472205840fa78604908892b20dc9e4f96a9b2f80f8956ae885d1c964fef6b8
- Behavior: Produced an external conditional-pass report, detected stale API verification markers, and made no repository mutation.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill lane leaves an unresolved evidence gap while claiming the affected pages are verified.
- The with_skill lane does not produce the required candidate_verified producer-schema record.
- Next: Supply the complete producer version-source inventory, rerun the pre-tag audit, then evaluate stamping and post-stamp discovery assertions.

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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `db1c342ca91a7c5561bf9a25e69f9d7391ef1a0976e07f5199051446101fa25e`
- Skill overlay SHA-256: `c412b1941949bc50388cc9d557ccf540b6dd69868115298f64b2e0a8c36aec77`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `9d29cd503dc3f38e1235bc8d674c667f9fc3bef38d94569b7888bb0dfed80506`
- Metadata SHA-256: `4c1ab6c77122f43adf1cbc9d6f05aea7b2b047fe1e69ba225e32d03f006dc954`
- Executor SHA-256: `6c1c50885619c5add1ae9c7d9faf1fa39e905346d86059a01403ae742d286478`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `verifies_complete_affected_set` | FAIL | with_skill 报告将四个受影响正式页面均判为 verified，但同时明确存在完整版本源清单的 protocol/schema evidence gap，因此不满足“无 unresolved evidence gap”。 |
| `stamps_all_pages_together` | NOT_EXERCISED | with_skill 明确因 handoff 清单缺失而未修改页面版本戳；统一盖章步骤尚未具备执行条件。 |
| `verifies_release_metadata_read_only` | PASS | 报告逐项核对 docs/site/.meta/releases.json 的版本值，并通过未修改文件的 manifest/git 状态证明其保持只读；其值为 v1.1.0。 |
| `normalizes_mixed_version_forms` | PASS | 报告完整列出带 v 的 release/context、Release Notes、索引和 metadata 来源，以及无 v 的 package.json version，均归一化为 1.1.0 并判定 equal；未来 tag 作为 pre-tag pending。 |
| `persists_candidate_producer_schema` | FAIL | with_skill 仅生成 blocked 的审计报告，未生成要求的 candidate_verified candidate record；报告缺少 assertion 所要求的完整 attempt、统一盖章前后字段、六字段 locator contract、canonical inventory digest、两次 staged gate 等完整结构，且结论明确为 blocked。 |
| `anchors_candidate_then_discovers_success` | NOT_EXERCISED | with_skill 明确未创建 candidate commit、anchor 或 handoff；由于前置 handoff inventory evidence gap，后续 discovery/fast-forward 流程尚不能执行。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c; fixture_sha256=085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897; output_sha256=95bcafd9c87f90e5feb2c19a73d466d49db2fa1023cecf874c906db986f056f6; snapshot_sha256=34221c040799d887e485a4e97df19f6bb9070a51a60f1bc35a5286cf54bc6ecb
- Behavior: 在固定正式审计路径生成报告，核实四个页面和版本来源，但识别到 handoff 缺少完整 locator contract 后安全阻塞，未执行盖章、提交、anchor 或 handoff。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c; fixture_sha256=085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897; output_sha256=613f12db36e319176611e231fc7125d1b80ff1b295b17a81029c613df55afbae; snapshot_sha256=59600d860175dcda8a57a7837c5a82f9e4df477e2e811cfea6581cabe909572a
- Behavior: fresh baseline 仅在 release-evidence/ 下生成非正式报告，未修改正式文档或创建提交；未完成所需的正式审计协议。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- verifies_complete_affected_set：报告明确存在 unresolved protocol/schema evidence gap。
- persists_candidate_producer_schema：未生成完整且结论为 candidate_verified 的 candidate record。
- Next: 补发包含每个版本源完整 locator contract 的 handoff，并在相同 immutable refs 上重跑 pre-tag audit。

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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5d2042a1a550e9bb3ae1ab775ff298d7368e3095f84097bc1ec5245f12b2ef69`
- Skill overlay SHA-256: `7611a201c389fbd5d4ead2394aea925facba8910dc630970a9c0c73508434d7c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `9d29cd503dc3f38e1235bc8d674c667f9fc3bef38d94569b7888bb0dfed80506`
- Metadata SHA-256: `4c1ab6c77122f43adf1cbc9d6f05aea7b2b047fe1e69ba225e32d03f006dc954`
- Executor SHA-256: `6c1c50885619c5add1ae9c7d9faf1fa39e905346d86059a01403ae742d286478`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `verifies_complete_affected_set` | PASS | Candidate record identifies both change-map-required API documents, records page-level code evidence and concludes both `verified`; it also records release surfaces verified and no blockers. |
| `stamps_all_pages_together` | FAIL | The locked diff modifies only the two API pages. The candidate record explicitly says the Release Notes page and index were read-only and not modified, so the asserted unified update of all four surfaces is not satisfied. |
| `verifies_release_metadata_read_only` | PASS | The candidate inventory includes `.meta/releases.json` values matching `v1.1.0`, while the locked result diff contains no modification to that file. |
| `normalizes_mixed_version_forms` | PASS | The candidate inventory records `v1.1.0` sources normalized to `1.1.0`, `package.json` as `1.1.0`, matching results, and an absent-but-expected pre-tag actual tag. |
| `persists_candidate_producer_schema` | FAIL | The candidate record exists at the fixed path and includes core schema, refs, evidence, hashes, and candidate_verified conclusion, but its version inventory lacks the required per-source path/mode/type/blob/hash locator fields and it does not provide two complete staged-gate inventories. |
| `anchors_candidate_then_discovers_success` | FAIL | A handoff and fast-forward merge are evidenced, but the locked evidence does not establish the required complete raw metadata/status/type/mode/path/content/tree confirmations, nor the required external-package handoff commit/tree/path/blob confirmation before returning ready_for_tag. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c; fixture_sha256=085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897; output_sha256=bafe4407e2b81dc7eb09d3475dc360287e0e3e8f5413834c8d89059da9cb7752; snapshot_sha256=3a15108b7864efb5a8cd6b0af840579e5b4de34dfef3ed0d8721e6cfb00832c2
- Behavior: Verified the API facts, stamped the two API pages, created candidate and handoff records, committed and fast-forwarded them, and reported ready_for_tag; it did not satisfy all required all-surface stamping and evidence-schema details.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c; fixture_sha256=085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897; output_sha256=e6e1ea6447cacc3422e31928bef6b5c00ea5b0b923bc8f32577add024a6fe71f; snapshot_sha256=dd703744b55e52f50c18e96a6608800a589ca25dca90436bf58fc00a7878ce7d
- Behavior: Created an untracked prose audit outside the required fixed path, left the worktree and target documents unchanged, and reported a conditional pass due to stale API metadata.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- Release Notes and index were explicitly treated as read-only rather than stamped in the same audit operation.
- The candidate record lacks the required complete locator contract and two staged-gate inventories.
- The handoff evidence lacks the required complete confirmation and external-package commit details.
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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `d339a8370a29b3fb2a69aa1879b1226165ec088d306a4e2e7a01258df2326973`
- Skill overlay SHA-256: `0bc7243cbb5cff3e77d9ba448e020a1a1f279639f8db6a365faac208b8e1dcc7`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `9d29cd503dc3f38e1235bc8d674c667f9fc3bef38d94569b7888bb0dfed80506`
- Metadata SHA-256: `4c1ab6c77122f43adf1cbc9d6f05aea7b2b047fe1e69ba225e32d03f006dc954`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `verifies_complete_affected_set` | PASS | The candidate record lists four affected pages, marks each verified, and reports no unresolved evidence gap or blockers. |
| `stamps_all_pages_together` | PASS | The final commit updates both API pages to v1.1.0; the release notes page and index already had v1.1.0, and the candidate reports a unified four-page stamp set. |
| `verifies_release_metadata_read_only` | PASS | The metadata version is inventoried as v1.1.0, while git evidence shows no modification to docs/site/.meta/releases.json. |
| `normalizes_mixed_version_forms` | PASS | The candidate inventory records v-prefixed forms for release sources, unprefixed package.json version 1.1.0, normalized comparisons, and the actual tag as pending absent. |
| `persists_candidate_producer_schema` | FAIL | The candidate record omits the required complete per-source locator fields and does not provide two completed staged-gate inventories or completed readback evidence; it explicitly says the final staged gate and post-commit readback are pending. |
| `anchors_candidate_then_discovers_success` | FAIL | Although anchor and handoff records are present, raw git evidence shows the final integration commit contains the candidate, handoff, and API changes together rather than a handoff-only commit; the evidence does not establish the required staged sequence and readback. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c; fixture_sha256=085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897; output_sha256=4749859df3736d8f999605060612b7f57e2cb7049b94c413a00b68013c552434; snapshot_sha256=7fd91977039877293025f248c572627603849a974010cf398623942f8811a776
- Behavior: Updated and stamped the two API pages, produced candidate and handoff records, and claimed ready_for_tag, but the persisted audit record and commit sequence do not satisfy the required evidence and handoff protocol.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c; fixture_sha256=085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897; output_sha256=2087ef7d91532450da1ef3bc7a6b68156121027d6a2ef330dde129f037c63b55; snapshot_sha256=46ff2456e9d06ba6d180a33e2cc31dfcc231f029eb50f59b50c75d535da0dc39
- Behavior: Produced only an external audit report, claimed no API documentation change was needed, and left the workspace without official documentation updates.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The candidate record is incomplete against the required schema and leaves staged-gate/readback evidence pending.
- The handoff was not proven to be created and integrated through the required handoff-only commit sequence.
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
