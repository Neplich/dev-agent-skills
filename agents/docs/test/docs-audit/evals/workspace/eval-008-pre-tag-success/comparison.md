# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-008-pre-tag-success`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `188f1d4d85d9c539fa3ce7acd636673ee316e8a8c7f692533cb806966484f84f` from `agents/docs/test/docs-audit/evals/workspace/eval-008-pre-tag-success`.
- Fixture SHA-256: `188f1d4d85d9c539fa3ce7acd636673ee316e8a8c7f692533cb806966484f84f`
- Prompt SHA-256: `c716eb0f2d2753ceb3a2258e2367701a57faeef420e346b4fa18dc3a1677c0e3`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8588a4fc6bb55ff6a1ce485f659334cabf6f9624098f4db4f1066bdacc1fc3ec`
- Skill overlay SHA-256: `09c184e9256c59e7718f2b61600ec30436b550d1692a7c65f8b8e6c64fc491f3`
- Judge schema SHA-256: `4cd14ef8cd033d31b5bb9ce50a786ad0b7d18c7ff4f682d88505eac53b634ecf`
- Eval definition SHA-256: `4d1aa7f3a07c406f7e925f931c91ea28170bd7650629aa75bcd06b4f58bba0c7`
- Metadata SHA-256: `6adbc51a2dc07674edf9fca71addc72bccaccf75ae663c41fbf3725d8c48b107`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_confirmed_version_without_tag` | PASS | With-skill output records base_ref, target_ref, confirmed v1.2.0, and absent tag, while identifying a separate metadata contradiction as the blocker. |
| `verifies_complete_set_and_surfaces` | PASS | With-skill output includes both change-map API pages, reports all four affected pages verified, and surfaces the conflicting .meta/releases.json state. |
| `normalizes_mixed_version_forms` | NOT_EXERCISED | The output uses v1.2.0 for the confirmed target and page values but does not provide enough evidence of source-form normalization against package.json and metadata. |
| `records_pre_stamp_values` | PASS | All four pre-stamp values are explicitly recorded: v1.1.0, unverified, unverified, and v1.1.0. |
| `stamps_complete_set_atomically` | NOT_EXERCISED | The candidate correctly reports that unified stamping was not executed because the audit is blocked; later stamping cannot proceed without correcting the surfaced blocker. |
| `builds_isolated_candidate_transaction` | NOT_EXERCISED | No candidate was built, and the locked evidence cannot prove the hidden isolation and captured-state process. |
| `candidate_record_has_no_ready_result` | NOT_EXERCISED | No candidate record exists because the audit stopped before candidate construction. |
| `validates_two_complete_staged_gates` | NOT_EXERCISED | No staged gates were executed because the audit stopped at the precondition blocker. |
| `confirms_anchor_commit_before_discovery` | NOT_EXERCISED | No anchor commit or post-stamp validation was created because stamping did not occur. |
| `persists_fixed_discovery_handoff` | NOT_EXERCISED | No discovery handoff was written because no anchor commit was created. |
| `returns_ready_only_after_integration` | NOT_EXERCISED | Integration and downstream readiness were not reached after the metadata blocker was surfaced. |
| `returns_ready_for_tag_not_published` | NOT_EXERCISED | The correct pre-tag outcome is blocked by the contradictory released/latest metadata, so ready_for_tag was not reachable in this run. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c716eb0f2d2753ceb3a2258e2367701a57faeef420e346b4fa18dc3a1677c0e3; fixture_sha256=188f1d4d85d9c539fa3ce7acd636673ee316e8a8c7f692533cb806966484f84f; output_sha256=8a96fe1aba2b23602273d1cd6e861d642e6dc6530d66d939af60720d41305bca; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly audited the confirmed refs/version, verified the affected documentation surfaces, surfaced the release metadata contradiction, and preserved the workspace without performing downstream mutations.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c716eb0f2d2753ceb3a2258e2367701a57faeef420e346b4fa18dc3a1677c0e3; fixture_sha256=188f1d4d85d9c539fa3ce7acd636673ee316e8a8c7f692533cb806966484f84f; output_sha256=ba68143435d49013938be6175eba28c5597c751d3f112746836ea5d5888dcc7a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline also blocked on release metadata, but reported stale verification markers and an alleged diff-evidence mismatch instead of the with-skill complete-surface verification and bound blocker handling.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Correct the contradictory release metadata, then rerun the complete pre-tag workflow.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-008-pre-tag-success`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `188f1d4d85d9c539fa3ce7acd636673ee316e8a8c7f692533cb806966484f84f` from `agents/docs/test/docs-audit/evals/workspace/eval-008-pre-tag-success`.
- Fixture SHA-256: `188f1d4d85d9c539fa3ce7acd636673ee316e8a8c7f692533cb806966484f84f`
- Prompt SHA-256: `c716eb0f2d2753ceb3a2258e2367701a57faeef420e346b4fa18dc3a1677c0e3`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a40b9426c3ece6f787614183ce8478f0aacaf94802441ebb84796853c2c8848e`
- Skill overlay SHA-256: `6cbf5a99cea4bf2bfd3e91f9b1e261a828b8b62ab73699f7ed3de43f33d01739`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `4d1aa7f3a07c406f7e925f931c91ea28170bd7650629aa75bcd06b4f58bba0c7`
- Metadata SHA-256: `6adbc51a2dc07674edf9fca71addc72bccaccf75ae663c41fbf3725d8c48b107`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_confirmed_version_without_tag` | PASS | Candidate record and handoff retain base_ref v1.1.0, target_ref release-head, confirmed v1.2.0, and pending absent tag. |
| `verifies_complete_set_and_surfaces` | PASS | Candidate record covers both API pages, handoff, release page, index, metadata, and package version; all four pages are marked verified. |
| `normalizes_mixed_version_forms` | PASS | Inventory records v1.2.0 forms for release sources, 1.2.0 for package.json, and normalized equality. |
| `records_pre_stamp_values` | PASS | Candidate record records catalog-items and index as v1.1.0, catalog-status and release page as unverified, with no baseline frontmatter field. |
| `stamps_complete_set_atomically` | PASS | Locked blobs and diffs show exactly four pages changed to v1.2.0; releases metadata is unchanged. |
| `builds_isolated_candidate_transaction` | NOT_EXERCISED | The artifacts show candidate, anchor, and integration commits, but raw evidence does not prove the temporary worktree/branch and captured index isolation process. |
| `candidate_record_has_no_ready_result` | PASS | Candidate record contains candidate_verified, inventories, digests, pending tag entry, and review commands, without ready_for_tag or post-commit fields. |
| `validates_two_complete_staged_gates` | PASS | Raw commit diffs show the authorized four-page M set, 100644 modes, ordinary blob additions, full patch content, and no unauthorized paths or rename/copy/type changes. |
| `confirms_anchor_commit_before_discovery` | NOT_EXERCISED | An anchor commit and post-commit confirmation are recorded, but the raw evidence does not independently prove the complete rerun of every anchor gate before handoff creation. |
| `persists_fixed_discovery_handoff` | PASS | Locked handoff blob contains schema, refs, ready_for_tag, timestamp, inventory digest, anchor and candidate identities, lineage, prior absence, and post-commit confirmation; it is committed and reachable. |
| `returns_ready_only_after_integration` | PASS | Git evidence shows release-head fast-forwarded from target_ref to the integrated handoff commit, with clean host state and the handoff blob reachable. |
| `returns_ready_for_tag_not_published` | PASS | Output and handoff report ready_for_tag, explicitly limited to tag creation; tag remains absent and publication is not claimed. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c716eb0f2d2753ceb3a2258e2367701a57faeef420e346b4fa18dc3a1677c0e3; fixture_sha256=188f1d4d85d9c539fa3ce7acd636673ee316e8a8c7f692533cb806966484f84f; output_sha256=d715270540b4a892c0df267fdc95b933569bc8425ecba94087f1e8ce01d26226; snapshot_sha256=4920b999e98cfddddf6e8fc3205d4c2075b48673398e98fba52175b39ff72522
- Behavior: Completed the pre-tag audit, candidate/anchor/handoff flow, fast-forward integration, and returned ready_for_tag.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c716eb0f2d2753ceb3a2258e2367701a57faeef420e346b4fa18dc3a1677c0e3; fixture_sha256=188f1d4d85d9c539fa3ce7acd636673ee316e8a8c7f692533cb806966484f84f; output_sha256=92f82536b9e289171dd60bceeb0788948571309263221e7417838ba92957f0ee; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline identified blockers and performed no delivery mutation.
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
- Eval: `eval-008-pre-tag-success`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `188f1d4d85d9c539fa3ce7acd636673ee316e8a8c7f692533cb806966484f84f` from `agents/docs/test/docs-audit/evals/workspace/eval-008-pre-tag-success`.
- Fixture SHA-256: `188f1d4d85d9c539fa3ce7acd636673ee316e8a8c7f692533cb806966484f84f`
- Prompt SHA-256: `c716eb0f2d2753ceb3a2258e2367701a57faeef420e346b4fa18dc3a1677c0e3`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5d2042a1a550e9bb3ae1ab775ff298d7368e3095f84097bc1ec5245f12b2ef69`
- Skill overlay SHA-256: `7611a201c389fbd5d4ead2394aea925facba8910dc630970a9c0c73508434d7c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `4d1aa7f3a07c406f7e925f931c91ea28170bd7650629aa75bcd06b4f58bba0c7`
- Metadata SHA-256: `6adbc51a2dc07674edf9fca71addc72bccaccf75ae663c41fbf3725d8c48b107`
- Executor SHA-256: `6c1c50885619c5add1ae9c7d9faf1fa39e905346d86059a01403ae742d286478`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_confirmed_version_without_tag` | PASS | with_skill 记录了 base_ref、target_ref、维护者确认的 v1.2.0，并确认同名 tag 不存在；未因缺少 tag 阻塞。 |
| `verifies_complete_set_and_surfaces` | PASS | with_skill 纳入了 change-map 要求的两张 API 页面、Release Notes、索引、release metadata、handoff 与 package.json，并报告 API 页面及 Release Notes/索引事实复核通过。 |
| `normalizes_mixed_version_forms` | PASS | with_skill 明确核对并将 v1.2.0 与 1.2.0 归一化为同一 SemVer，未将合法 v 前缀差异判为阻塞。 |
| `records_pre_stamp_values` | PASS | with_skill 记录 catalog-items 与索引为 v1.1.0、catalog-status 与 Release Notes 页为 unverified，并说明未修改工作区或新增 baseline frontmatter。 |
| `stamps_complete_set_atomically` | NOT_EXERCISED | 版本源 inventory 不完整，前置条件未满足；候选输出明确未盖章。 |
| `builds_isolated_candidate_transaction` | NOT_EXERCISED | 因缺少完整版本源 inventory，未创建候选事务或进行盖章构建。 |
| `candidate_record_has_no_ready_result` | NOT_EXERCISED | 候选输出明确无法创建 candidate record，因此该记录内容要求未进入可判断阶段。 |
| `validates_two_complete_staged_gates` | NOT_EXERCISED | 未生成初稿或最终 candidate，故 staged raw metadata gates 未执行。 |
| `confirms_anchor_commit_before_discovery` | NOT_EXERCISED | 未创建 candidate 或 anchor commit；后续提交确认未执行。 |
| `persists_fixed_discovery_handoff` | NOT_EXERCISED | 候选输出明确无法创建 discoverable handoff，因而固定 handoff 流程未执行。 |
| `returns_ready_only_after_integration` | NOT_EXERCISED | 没有 candidate、handoff 或集成提交，无法进入宿主分支集成阶段。 |
| `returns_ready_for_tag_not_published` | NOT_EXERCISED | with_skill 正确停留在 blocked；由于缺少完整 inventory，后续 ready_for_tag 阶段尚未可执行。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c716eb0f2d2753ceb3a2258e2367701a57faeef420e346b4fa18dc3a1677c0e3; fixture_sha256=188f1d4d85d9c539fa3ce7acd636673ee316e8a8c7f692533cb806966484f84f; output_sha256=29bc8d0f9232387e5b7993e1e084f98d45d5f4cf08a23be6bb994551c8d6a028; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确确认 refs、版本形态、tag 状态、影响页面及事实核验，并因 handoff 缺少完整版本源 inventory 安全阻塞，未进行盖章、候选、提交或 ready 暴露。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c716eb0f2d2753ceb3a2258e2367701a57faeef420e346b4fa18dc3a1677c0e3; fixture_sha256=188f1d4d85d9c539fa3ce7acd636673ee316e8a8c7f692533cb806966484f84f; output_sha256=1b137900e9f7b887c9eabbc39a9eecdba94de1d87ba46bb4ebcc8af20552ac3a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 基线识别了 tag 不存在、版本事实和工作区未修改，但错误地将补丁空行与 releases metadata 状态作为阻断，未完成系统化影响域与审计流程。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 补充完整版本源 inventory 后，重新执行同一 refs 与 target_release_version 的 pre-tag 审计。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-008-pre-tag-success`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `188f1d4d85d9c539fa3ce7acd636673ee316e8a8c7f692533cb806966484f84f` from `agents/docs/test/docs-audit/evals/workspace/eval-008-pre-tag-success`.
- Fixture SHA-256: `188f1d4d85d9c539fa3ce7acd636673ee316e8a8c7f692533cb806966484f84f`
- Prompt SHA-256: `c716eb0f2d2753ceb3a2258e2367701a57faeef420e346b4fa18dc3a1677c0e3`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9e9abf391c9ccd9564d35b5def50bc0374b1db0886710676c4d48422839746ae`
- Skill overlay SHA-256: `c66ac938bf9158faa694d7c3e311e913ddc4a06da11de703a881234f257c470c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `4d1aa7f3a07c406f7e925f931c91ea28170bd7650629aa75bcd06b4f58bba0c7`
- Metadata SHA-256: `6adbc51a2dc07674edf9fca71addc72bccaccf75ae663c41fbf3725d8c48b107`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_confirmed_version_without_tag` | PASS | 明确记录了 base_ref、target_ref、维护者确认的 v1.2.0，并确认同名 tag 不存在且未因此阻塞。 |
| `verifies_complete_set_and_surfaces` | NOT_EXERCISED | 确认列出四个文档页面并判为 verified，但因 handoff 版本源清单不完整，完整版本表面核验流程未完成。 |
| `normalizes_mixed_version_forms` | NOT_EXERCISED | 未完成所需版本源 inventory 校验；输出未证明各来源 raw form 的规范化与等价比较。 |
| `records_pre_stamp_values` | NOT_EXERCISED | 未进入盖章事务，未报告四页统一盖章集的盖章前值。 |
| `stamps_complete_set_atomically` | NOT_EXERCISED | 由于 handoff 清单缺失，候选事务未启动；没有可评估的原子盖章操作。 |
| `builds_isolated_candidate_transaction` | NOT_EXERCISED | 未创建候选记录或隔离事务，无法评估隔离构建流程。 |
| `candidate_record_has_no_ready_result` | NOT_EXERCISED | 未创建 candidate record。 |
| `validates_two_complete_staged_gates` | NOT_EXERCISED | 未进入 staged gate 流程。 |
| `confirms_anchor_commit_before_discovery` | NOT_EXERCISED | 未创建 anchor commit 或 discovery handoff。 |
| `persists_fixed_discovery_handoff` | NOT_EXERCISED | 输出明确未创建 handoff；该后续阶段未执行。 |
| `returns_ready_only_after_integration` | NOT_EXERCISED | 由于前置版本源 inventory 缺失，未进行集成及集成后回读。 |
| `returns_ready_for_tag_not_published` | NOT_EXERCISED | 输出正确地报告 blocked；因前置条件未满足，ready_for_tag 阶段未到达。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c716eb0f2d2753ceb3a2258e2367701a57faeef420e346b4fa18dc3a1677c0e3; fixture_sha256=188f1d4d85d9c539fa3ce7acd636673ee316e8a8c7f692533cb806966484f84f; output_sha256=762eaddd967f0354736ab05a5d9b230122c77d28ee8837a2460ca555bb4473cc; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确接受已确认版本和缺失 tag，核验四个文档页面，并在发现 handoff 缺少完整版本源 selector/extractor/required_raw_form 后安全阻塞，未进行写入或候选构建。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c716eb0f2d2753ceb3a2258e2367701a57faeef420e346b4fa18dc3a1677c0e3; fixture_sha256=188f1d4d85d9c539fa3ce7acd636673ee316e8a8c7f692533cb806966484f84f; output_sha256=c3abb8efb34fecf5e780eafb6348467b331a04f7cdc75f12b25e955c14ea88a0; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 发现 releases.json 将 v1.2.0 标为已发布并阻塞，但未执行结构化 pre-tag 审计流程。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 补充完整版本源 inventory 后重新运行 pre-tag 审计。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-008-pre-tag-success`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `188f1d4d85d9c539fa3ce7acd636673ee316e8a8c7f692533cb806966484f84f` from `agents/docs/test/docs-audit/evals/workspace/eval-008-pre-tag-success`.
- Fixture SHA-256: `188f1d4d85d9c539fa3ce7acd636673ee316e8a8c7f692533cb806966484f84f`
- Prompt SHA-256: `c716eb0f2d2753ceb3a2258e2367701a57faeef420e346b4fa18dc3a1677c0e3`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2d24da5f976a5ab2710c2c072a19015e074d314e0ebdb88f1c28831425f1b98c`
- Skill overlay SHA-256: `40330c17a3b77f25a1b1a716fa5e9355e0011db79d19014344ed516affba11c8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `4d1aa7f3a07c406f7e925f931c91ea28170bd7650629aa75bcd06b4f58bba0c7`
- Metadata SHA-256: `6adbc51a2dc07674edf9fca71addc72bccaccf75ae663c41fbf3725d8c48b107`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_confirmed_version_without_tag` | PASS | with_skill 明确记录 base_ref=v1.1.0、target_ref=release-head、确认版本=v1.2.0，并说明同名 tag 不存在但未因此阻塞。 |
| `verifies_complete_set_and_surfaces` | FAIL | 虽列出两张 API 页面为 verified，但未证明已核对 handoff、Release Notes、索引、releases.json 与宿主版本事实，也未证明 Release Notes 和索引已完成事实核验。 |
| `normalizes_mixed_version_forms` | FAIL | 未记录各版本来源的 required raw form、selector/extractor、规范化比较或 SemVer 等价校验。 |
| `records_pre_stamp_values` | FAIL | 仅概括列出 v1.1.0 和 unverified，未逐页明确四个页面的盖章前值，也未说明未新增 baseline_verified_version frontmatter。 |
| `stamps_complete_set_atomically` | FAIL | with_skill 明确因阻塞项未创建记录、未统一更新 last_verified_version；因此未完成原子盖章和回读，也无法证明 releases.json 未修改。 |
| `builds_isolated_candidate_transaction` | FAIL | 没有隔离 worktree/branch/index、target commit 初始化或宿主状态保持捕获的证据；git_evidence 中 temporary_worktree 使用状态为 unknown。 |
| `candidate_record_has_no_ready_result` | FAIL | 未创建 candidate record，因而没有完整 producer schema、四页章前后值、SHA-256、inventory/digest、差异 inventory、回读命令等要求字段。 |
| `validates_two_complete_staged_gates` | FAIL | 未执行或报告两次完整 raw metadata gate、name-status、summary、full binary patch、类型/mode/路径和单行变更约束。 |
| `confirms_anchor_commit_before_discovery` | FAIL | 未创建 post-stamp anchor commit，也未对 target_ref..anchor_commit 执行确认检查。 |
| `persists_fixed_discovery_handoff` | FAIL | 未写入或提交固定 discovery handoff，未提供 anchor、candidate、digest、preimage 或 post-commit confirmation。 |
| `returns_ready_only_after_integration` | FAIL | 未执行临时分支 fast-forward 集成、集成后 handoff 回读、CAS 回退或并发移动处理。 |
| `returns_ready_for_tag_not_published` | FAIL | 结果明确为 blocked，不能返回 ready_for_tag；未满足“可创建 tag 但尚未发布”的最终状态输出。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c716eb0f2d2753ceb3a2258e2367701a57faeef420e346b4fa18dc3a1677c0e3; fixture_sha256=188f1d4d85d9c539fa3ce7acd636673ee316e8a8c7f692533cb806966484f84f; output_sha256=7ae632405d8c50457fed1453f10cac71805031ee6834242c7959c261ae9beb2e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别出两张 API 页面并记录部分上下文，但因 handoff 缺少完整版本源清单而提前 blocked，未执行候选构建、盖章、anchor、handoff、集成或 ready 输出。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c716eb0f2d2753ceb3a2258e2367701a57faeef420e346b4fa18dc3a1677c0e3; fixture_sha256=188f1d4d85d9c539fa3ce7acd636673ee316e8a8c7f692533cb806966484f84f; output_sha256=d4e6cb4630716c64e1e69034dcfd75b95c51e718930abc9943417d08584f7d68; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: fresh baseline 未执行发布前审计变更，因 releases.json 状态冲突和范围疑点阻塞。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 只完成部分发现与页面核对，未完成版本规范化、完整事实核验、候选事务、双阶段 gate、anchor、handoff、集成及最终 ready_for_tag。
- Next: 补齐 handoff 的完整版本源 inventory（source_id、locator_kind、selector、extractor、required_raw_form），然后重新执行完整 pre-tag 流程。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-008-pre-tag-success`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `b1af296f57c9472641aa2fbf552cc05b76e8658e900bc4d5f0a34e60133977ab` from `agents/docs/test/docs-audit/evals/workspace/eval-008-pre-tag-success`.
- Fixture SHA-256: `b1af296f57c9472641aa2fbf552cc05b76e8658e900bc4d5f0a34e60133977ab`
- Prompt SHA-256: `c716eb0f2d2753ceb3a2258e2367701a57faeef420e346b4fa18dc3a1677c0e3`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2baee6e542351d5b0c46e79c685dd29ff93f0fee4a45cf4485afee7656248cf7`
- Skill overlay SHA-256: `a2871f547194089c5425585467f9bee6e3c85ea103d77933d85a4c4cf246fa7c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `9e8cd9d72ce0e98552272f26978823af26e642ab29487b2f1519c46898c21493`
- Metadata SHA-256: `8bf9eed51fb7f0c370d32001c1771329090952db5672ea9c398b67465aa72d50`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_confirmed_version_without_tag` | PASS | with_skill records base_ref, target_ref, confirmed v1.2.0, and absent tag; it blocks for missing handoff/inventory rather than tag absence. |
| `verifies_complete_set_and_surfaces` | FAIL | It verifies the four listed pages, but does not establish the complete required surface set or successful handoff, metadata, and host-version verification. |
| `normalizes_mixed_version_forms` | FAIL | It notes an incomplete version-source inventory and does not demonstrate required raw-form validation, normalization, or SemVer equality. |
| `records_pre_stamp_values` | PASS | It records the exact required pre-stamp values for all four pages. |
| `stamps_complete_set_atomically` | NOT_EXERCISED | The output explicitly says no document fields were modified because the audit was blocked. |
| `builds_isolated_candidate_transaction` | NOT_EXERCISED | No isolated candidate transaction or temporary build is reported; the audit stopped before construction. |
| `candidate_record_has_no_ready_result` | NOT_EXERCISED | No candidate record was created or reported. |
| `validates_two_complete_staged_gates` | NOT_EXERCISED | No staging, raw metadata gate, or candidate replacement gate was performed. |
| `confirms_anchor_commit_before_discovery` | NOT_EXERCISED | No anchor commit or post-stamp confirmation was created. |
| `persists_fixed_discovery_handoff` | NOT_EXERCISED | The output explicitly says no audit record or handoff was created. |
| `returns_ready_only_after_integration` | NOT_EXERCISED | Integration and downstream ready handoff were not reached because the audit was blocked. |
| `returns_ready_for_tag_not_published` | FAIL | The output returns blocked rather than the required pre-tag ready_for_tag result. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c716eb0f2d2753ceb3a2258e2367701a57faeef420e346b4fa18dc3a1677c0e3; fixture_sha256=b1af296f57c9472641aa2fbf552cc05b76e8658e900bc4d5f0a34e60133977ab; output_sha256=398e5f83753be86170ff333d79b71d66251164b780867e05af976ee7880965be; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly accepted the confirmed pre-tag version and absent tag, verified the four listed pages and pre-stamp values, then blocked on missing release-notes handoff and incomplete version-source inventory.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c716eb0f2d2753ceb3a2258e2367701a57faeef420e346b4fa18dc3a1677c0e3; fixture_sha256=b1af296f57c9472641aa2fbf552cc05b76e8658e900bc4d5f0a34e60133977ab; output_sha256=2b16be09888ad63a1d710e91fccfe240755b1009b7b08ef88744e422973f9abb; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline misclassified the release metadata as a blocking publication conflict and did not perform the required audit workflow.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The complete required surface and source-normalization verification were not demonstrated.
- The required ready_for_tag result was not returned.
- Next: Provide the required Release Notes handoff and complete version-source inventory, then rerun the full pre-tag workflow.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-008-pre-tag-success`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `588924b9e745bd0282560429ce305f14ce4c254eb94edfc5269a128aff4ece1b` from `agents/docs/test/docs-audit/evals/workspace/eval-008-pre-tag-success`.
- Fixture SHA-256: `588924b9e745bd0282560429ce305f14ce4c254eb94edfc5269a128aff4ece1b`
- Prompt SHA-256: `c716eb0f2d2753ceb3a2258e2367701a57faeef420e346b4fa18dc3a1677c0e3`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2baee6e542351d5b0c46e79c685dd29ff93f0fee4a45cf4485afee7656248cf7`
- Skill overlay SHA-256: `a2871f547194089c5425585467f9bee6e3c85ea103d77933d85a4c4cf246fa7c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `9e8cd9d72ce0e98552272f26978823af26e642ab29487b2f1519c46898c21493`
- Metadata SHA-256: `8bf9eed51fb7f0c370d32001c1771329090952db5672ea9c398b67465aa72d50`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_confirmed_version_without_tag` | PASS | with_skill 明确记录 base_ref、target_ref、维护者确认的 v1.2.0，并确认同名 tag 不存在且未因此阻塞。 |
| `verifies_complete_set_and_surfaces` | FAIL | 虽列出两张 API 页面及两份 Release Notes 为 verified，但未验证 release-notes-gen handoff，且将 .meta/releases.json 的状态矛盾作为阻塞。 |
| `normalizes_mixed_version_forms` | FAIL | 仅记录 v1.2.0，未分别核对带 v、无 v 的来源形态并规范化比较。 |
| `records_pre_stamp_values` | FAIL | 未在审计结果中逐页记录四页的盖章前值。 |
| `stamps_complete_set_atomically` | FAIL | 明确表示未执行统一 stamp。 |
| `builds_isolated_candidate_transaction` | FAIL | 未构建隔离 candidate 事务，也未提供相关工作树、分支或 index 证据。 |
| `candidate_record_has_no_ready_result` | FAIL | 未生成 candidate record。 |
| `validates_two_complete_staged_gates` | FAIL | 未执行初稿和最终 candidate 的完整 raw metadata gate。 |
| `confirms_anchor_commit_before_discovery` | FAIL | 未创建或确认 post-stamp anchor commit。 |
| `persists_fixed_discovery_handoff` | FAIL | 未写入固定 discovery handoff。 |
| `returns_ready_only_after_integration` | FAIL | 未进行临时分支集成、handoff 回读或 CAS 条件验证。 |
| `returns_ready_for_tag_not_published` | FAIL | 结果为 blocked，未返回 ready_for_tag。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c716eb0f2d2753ceb3a2258e2367701a57faeef420e346b4fa18dc3a1677c0e3; fixture_sha256=588924b9e745bd0282560429ce305f14ce4c254eb94edfc5269a128aff4ece1b; output_sha256=a45a3c4acd5b72016a062f78253ede63f0a4de14dc1e8fe824dd0ba8cb82ed48; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确接受已确认版本和不存在的 tag，并识别影响页面；但因 handoff、版本源清单和发布元数据问题错误阻塞，未完成 pre-tag 事务或返回 ready_for_tag。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c716eb0f2d2753ceb3a2258e2367701a57faeef420e346b4fa18dc3a1677c0e3; fixture_sha256=588924b9e745bd0282560429ce305f14ce4c254eb94edfc5269a128aff4ece1b; output_sha256=e235a73d9646053f8c746bfa2b819574c83f013b509a71e85d091be8fba89804; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别 refs、版本和缺失 tag，但错误地将 .meta/releases.json 的预发布状态作为阻塞。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- verifies_complete_set_and_surfaces
- normalizes_mixed_version_forms
- records_pre_stamp_values
- stamps_complete_set_atomically
- builds_isolated_candidate_transaction
- candidate_record_has_no_ready_result
- validates_two_complete_staged_gates
- confirms_anchor_commit_before_discovery
- persists_fixed_discovery_handoff
- returns_ready_only_after_integration
- returns_ready_for_tag_not_published
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

# eval-008-pre-tag-success Comparison

## Evaluation target

- Agent: `docs-agent`
- Skill: `docs-audit`
- Eval: `eval-008-pre-tag-success`
- Validation time: `2026-08-03 22:40:00 +0800`（fresh re-baseline，issue #188）
- Scope: full pre-tag candidate transaction, canonical inventory/genesis digests, actual-tag pending contract, two staged gates, anchor/discovery commits, integration readback, and post-FF CAS rollback.

## Test set and method

This is a fresh paired validation against the current 12 assertions. The
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
- Coverage result: `PARTIAL`（with）/ `PARTIAL`（without）— Git 缺失导致 pre-tag 成功路径未执行
- Overall result: BLOCKED
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `PASS` / Coverage `PARTIAL`
- without_skill：Behavior `PASS` / Coverage `PARTIAL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| accepts_confirmed_version_without_tag | PASS | PASS | 两边均记录 `target_release_version: v1.2.0`、`base_ref: v1.1.0`、`target_ref: release-head`，并明确同名 tag 不存在；阻塞原因均为缺少 Git 仓库，而非 tag 不存在（两边 `result.txt` 第 5–11 行）。 |
| verifies_complete_set_and_surfaces | NOT_EXERCISED | NOT_EXERCISED | 未生成正式审计报告；两边均因无法解析 refs 而阻塞，未逐页产出 `verified` 结果。 |
| normalizes_mixed_version_forms | NOT_EXERCISED | NOT_EXERCISED | 未生成包含完整版本来源 inventory 的审计记录；without_skill 仅声称静态版本一致，未核验 `.meta/releases.json`。 |
| records_pre_stamp_values | NOT_EXERCISED | NOT_EXERCISED | with_skill 明确“未写入审计报告、版本戳”；两边均无审计报告文件。 |
| stamps_complete_set_atomically | NOT_EXERCISED | NOT_EXERCISED | 两边均未执行版本戳写入；with_skill 明确未写入版本戳。 |
| builds_isolated_candidate_transaction | NOT_EXERCISED | NOT_EXERCISED | 未产生隔离 worktree、临时分支或 candidate 产物；两边均报告当前工作区不是 Git 仓库。 |
| candidate_record_has_no_ready_result | NOT_EXERCISED | NOT_EXERCISED | 未生成 candidate record；两边仅返回 `blocked`，无法验证 schema、digest、inventory 等完整字段。 |
| validates_two_complete_staged_gates | NOT_EXERCISED | NOT_EXERCISED | 未执行或记录初稿/最终 raw metadata gate，也无 staged candidate 文件。 |
| confirms_anchor_commit_before_discovery | NOT_EXERCISED | NOT_EXERCISED | 未创建 anchor commit；两边均无法验证提交树、diff、blob 类型和 refs。 |
| persists_fixed_discovery_handoff | NOT_EXERCISED | NOT_EXERCISED | 未生成 `docs/site/.meta/audit/handoffs/pre-tag-v1.2.0.md` 或 handoff commit。 |
| returns_ready_only_after_integration | NOT_EXERCISED | NOT_EXERCISED | 未进入临时分支集成、FF、回读或 CAS 恢复路径。 |
| returns_ready_for_tag_not_published | NOT_EXERCISED | NOT_EXERCISED | 两条 lane 均因无 Git 无法进入 pre-tag 成功事务，正确停在 `blocked`；成功态 `ready_for_tag` 未执行。 |

未触发断言：除 `accepts_confirmed_version_without_tag` 外的 11 条成功路径断言。

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

- Recomputed v1.2.0 inventory digest:
  `sha256:bd935efb92eedfb3facbfe867542687802159c700fa73dee1d2a896deac041a8`
- Fixture inventory digest:
  `sha256:bd935efb92eedfb3facbfe867542687802159c700fa73dee1d2a896deac041a8`
- Recomputed empty prior-lineage digest from exact bytes `[]`:
  `sha256:4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`
- Fixture genesis digest:
  `sha256:4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`

Both comparisons are exact matches. The `actual_tag` entry is
`git-ref / refs/tags/v1.2.0 / tag-name / git-tag-name-v1 / vX.Y.Z`; its
pre-tag value remains `pending_expected_absent`. Tag absence is expected and
does not represent publication or a failed version comparison.

## Assertion results
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

| Assertion | without_skill | with_skill | Evidence summary |
| --- | --- | --- | --- |
| `accepts_confirmed_version_without_tag` | PASS | PASS | 双侧都分别记录 `v1.1.0`、`release-head` 与维护者确认的 `v1.2.0`，并把同名 tag 不存在视为正常 pre-tag 状态。 |
| `verifies_complete_set_and_surfaces` | PASS | PASS | 双侧均覆盖 change-map 命中的两张 API 页、release-notes handoff、Release Notes、索引、只读 releases metadata 与宿主版本；with-skill 逐页记录 target blob 和 verified 事实。 |
| `normalizes_mixed_version_forms` | PASS | PASS | 双侧均校验 `v1.2.0` 与 `package.json` 的 `1.2.0` 来源形态，并在规范化后判等。 |
| `records_pre_stamp_values` | FAIL | PASS | with-skill 精确记录四页章前值 `v1.1.0 / unverified / unverified / v1.1.0`，且页面未新增 `baseline_verified_version`；without-skill 只列最终 stamp，未持久化四个章前值。 |
| `stamps_complete_set_atomically` | PASS | PASS | 双侧实际四页均更新为 `v1.2.0` 且 releases metadata 未改；with-skill anchor commit 显示四页各只改一行 stamp 并与 candidate 同批提交。 |
| `builds_isolated_candidate_transaction` | FAIL | PASS | with-skill 存在从精确 target commit 建立的 `.git/audit-worktree-v1.2.0` 与独立 branch/index，宿主仅在最终 FF 后移动；without-skill 只是普通复制目录，无 worktree/target-tree index/宿主指纹证据。 |
| `candidate_record_has_no_ready_result` | FAIL | PASS | with-skill 固定 record 含完整逐页证据/hash、actual-tag pending inventory、canonical/prior-lineage digest、差异 inventory 与命令，且全文无 `ready_for_tag`、结果时间、anchor 或 post-commit 字段；without-skill record 缺完整 producer/gate/回读内容。 |
| `validates_two_complete_staged_gates` | FAIL | PASS | with-skill 留存 gate1 与最终 gate2 full-index patch，只含四张 100644 stamp 页和固定 candidate；without-skill 未执行或持久化两次 staged gate。 |
| `confirms_anchor_commit_before_discovery` | FAIL | PASS | with-skill anchor 的 parent 是精确 target，candidate blob、tree 与 target→anchor delta 均可回读，discovery 只在后续 commit 出现；without-skill 无 anchor 或 discovery。 |
| `persists_fixed_discovery_handoff` | FAIL | PASS | with-skill 固定 discovery 实际存在，含 phase/version/refs、`ready_for_tag`、时间、inventory digest、anchor/candidate identity、post-commit confirmation、preimage、current 与 lineage digest，handoff commit 只新增该 100644 blob；without-skill 无此产物与提交。 |
| `returns_ready_only_after_integration` | FAIL | PASS | with-skill 宿主分支最终同指 handoff commit，candidate 记录 FF 前指纹复核、FF 后 commit/tree/blob 回读及失败时 CAS 边界，随后才返回 ready；without-skill 未集成也未返回 ready。 |
| `returns_ready_for_tag_not_published` | FAIL | PASS | with-skill 最终为 `ready_for_tag`，并明确仅允许创建 tag、不是 published 或 `release_verified`；without-skill 仅返回 `candidate_verified`，不满足成功场景的阶段结果。 |

## With-skill behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

The skill-guided run validates the full affected set and release surfaces from
the exact target tree, applies the four-page stamp only after all evidence and
version identities pass, and builds a fixed-path candidate whose positive
conclusion is only `candidate_verified`. Its exact canonical inventory and
genesis digests match the fixture values; any mismatch would instead be
`blocked` and fail this eval.

Both staged gates inspect raw modes, object types, unfolded statuses, summary,
and full binary patch. Anchor confirmation precedes discovery; the discovery
handoff is committed separately and anchored by an external package. The host
branch is fast-forwarded only if its ref and captured worktree/index
fingerprints remain unchanged. Final authority appears only after integrated
commit/tree/discovery-blob readback.

If that readback fails after fast-forward, rollback to `target_ref` is allowed
only when compare-and-swap proves the branch still equals the just-integrated
handoff commit. The process then restores and verifies every captured
fingerprint. A concurrent move is never overwritten: the result remains
`blocked`, names the residual ref/commit and exact maintainer recovery command,
and prohibits tag creation.

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- `with_skill`: none。
- `without_skill`: 4/12 PASS（accepts_confirmed_version_without_tag、verifies_complete_set_and_surfaces、normalizes_mixed_version_forms、stamps_complete_set_atomically）；其余 8 条 FAIL（records_pre_stamp_values、builds_isolated_candidate_transaction、candidate_record_has_no_ready_result、validates_two_complete_staged_gates、confirms_anchor_commit_before_discovery、persists_fixed_discovery_handoff、returns_ready_only_after_integration、returns_ready_for_tag_not_published）——隔离事务、双 staged gate、anchor/discovery、FF 集成与阶段结果语义保持 with-skill 专属增量。

## Next steps

> ⚠️ 本节为 2026-08-03 #188 历史轮后续建议；当前 #238 重跑因 Git 仓库缺失保持 `BLOCKED`。

No skill change is required. Preserve exact canonical inventory fields and
ordering, actual-tag pending semantics, genesis bytes `[]`, and the guarded
post-FF CAS rollback language in future protocol edits.

## Runtime artifact policy

> ⚠️ 本节仅描述 2026-08-03 #188 历史轮运行产物；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

- Runtime artifacts（双侧 candidate、judge verdict、隔离目录执行产物）在本次 fresh re-baseline 中真实生成，位于被 gitignore 覆盖的 `tmp/eval-runs/issue-188-docs/`；未提交到 git。长期 durable 产物仅为本 `comparison.md`。
