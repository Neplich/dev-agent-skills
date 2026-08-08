# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-005-integration-release-chain`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `69659db940208abe97ba4ab195a49c736d9a7ba7e1e880c287d3bf12132c10a3` from `agents/docs/test/docs-agent/evals/workspace/eval-005-integration-release-chain`.
- Fixture SHA-256: `69659db940208abe97ba4ab195a49c736d9a7ba7e1e880c287d3bf12132c10a3`
- Prompt SHA-256: `62a386a246bcb0c7c5b2df7096cfd60c5023a6b28473d50af8f99649d1d3480e`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b04f0f833fdfe60f19dba4258110d7f6b0a3d6a6f2afb7034b0d3d883c30f83b`
- Skill overlay SHA-256: `960ab70564adb8fafabb98cb333bec48d92a317614465aaf97d281e6a5484a8c`
- Judge schema SHA-256: `1f2ea17b811fce39b8e906ef0e0a70b6a6223a188a2f4a05f2f0a88c54c6aceb`
- Eval definition SHA-256: `05d8b9eb5ccf6bbc077dad850c79899562c5b4ed9bbb4187abffd82f21410ea3`
- Metadata SHA-256: `af301306a3e584e9c32987cd73e02ac298dcd98f38208af58ca0764e8b5a4154`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_release_audit_entry` | PASS | With-skill output identifies the confirmed v1.4.0 entry, scope, evidence sources, and read-only execution boundary. |
| `evaluates_site_release_notes_gate` | PASS | It rejects the handoff as consumable without pre-tag authority/inventory and routes follow-up to docs-audit. |
| `validates_release_window_basis` | FAIL | It references the signed snapshot and target version, but does not explicitly validate the previous-tag comparison anchor v1.3.0. |
| `rejects_missing_pre_tag_authority` | PASS | It explicitly states that no consumable pre-tag audit authority exists and does not claim pre-tag success. |
| `detects_post_tag_evidence_drift` | PASS | It identifies the mismatch between the candidate/tag-entry tree and the actual v1.4.0 tag tree and blocks readiness. |
| `blocks_github_release_handoff` | PASS | It blocks GitHub Release preparation, provides no preview/draft/publish handoff, and assigns docs-audit follow-up. |
| `preserves_no_mutation_boundaries` | PASS | Git evidence shows no ref, commit, worktree, or index mutations; output also states that no tag or GitHub Release writes occurred. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=62a386a246bcb0c7c5b2df7096cfd60c5023a6b28473d50af8f99649d1d3480e; fixture_sha256=69659db940208abe97ba4ab195a49c736d9a7ba7e1e880c287d3bf12132c10a3; output_sha256=cb591b80a100bb926a6f2670a80d48742ab6461da52e05dfc9ea5565debbb4b4; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly preserves the read-only boundary, detects missing audit authority and tag/tree drift, blocks GitHub Release, and routes the next audit step to docs-audit; it omits the explicit previous-tag anchor check.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=62a386a246bcb0c7c5b2df7096cfd60c5023a6b28473d50af8f99649d1d3480e; fixture_sha256=69659db940208abe97ba4ab195a49c736d9a7ba7e1e880c287d3bf12132c10a3; output_sha256=9cd45fb8769d56c2fa4301a7f764ca81b5a45b13d0ab52acf28d2427dff43c6d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline correctly blocks release because the actual tag differs from the audited candidate and authority is missing, but gives a less precise phase/owner handoff.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- validates_release_window_basis
- Next: Explicitly verify and report the v1.3.0 previous tag and v1.4.0 target comparison anchors from the signed snapshot.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-005-integration-release-chain`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `69659db940208abe97ba4ab195a49c736d9a7ba7e1e880c287d3bf12132c10a3` from `agents/docs/test/docs-agent/evals/workspace/eval-005-integration-release-chain`.
- Fixture SHA-256: `69659db940208abe97ba4ab195a49c736d9a7ba7e1e880c287d3bf12132c10a3`
- Prompt SHA-256: `62a386a246bcb0c7c5b2df7096cfd60c5023a6b28473d50af8f99649d1d3480e`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b04f0f833fdfe60f19dba4258110d7f6b0a3d6a6f2afb7034b0d3d883c30f83b`
- Skill overlay SHA-256: `14d196833dce28912d8b0b555bccdba07e09dd666cd5fbd0bbf5033b1450392d`
- Judge schema SHA-256: `1f2ea17b811fce39b8e906ef0e0a70b6a6223a188a2f4a05f2f0a88c54c6aceb`
- Eval definition SHA-256: `05d8b9eb5ccf6bbc077dad850c79899562c5b4ed9bbb4187abffd82f21410ea3`
- Metadata SHA-256: `af301306a3e584e9c32987cd73e02ac298dcd98f38208af58ca0764e8b5a4154`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `5a4d229da9707c7ce22c80b66e92baafd2ef50f8fc9733b6b61f658aabf3dd17`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_release_audit_entry` | PASS | 明确接受 release-chain-entry.md 作为 docs-audit 入口，保留 v1.4.0、AI search 范围、证据来源和只读边界。 |
| `evaluates_site_release_notes_gate` | PASS | 识别 handoff 虽为 ready 但 release_execution_authorized 为 false，并将不一致项返回 Release Manager/维护者及文档审计责任人。 |
| `validates_release_window_basis` | PASS | 引用并正确使用 previous tag v1.3.0、release-base、release-candidate 及签认的 Git reference snapshot。 |
| `rejects_missing_pre_tag_authority` | PASS | 指出已有 v1.4.0 tag 越过 pre-tag 窗口且缺少可验证的最终审计权威，没有宣称 pre-tag 通过。 |
| `detects_post_tag_evidence_drift` | PASS | 根据快照识别 v1.4.0 tag tree 490d0b… 与 candidate/tag-entry/evidence-expected tree 7c8b9b… 不一致，并阻塞后续流程。 |
| `blocks_github_release_handoff` | PASS | 明确不能进入 GitHub Release 准备，未生成 preview、draft 或 publish handoff，并指定 Release Manager/维护者处理。 |
| `preserves_no_mutation_boundaries` | PASS | 候选输出明确声明不执行真实 tag 或 GitHub Release 写入；git evidence 显示无 ref、提交或工作区变更。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=62a386a246bcb0c7c5b2df7096cfd60c5023a6b28473d50af8f99649d1d3480e; fixture_sha256=69659db940208abe97ba4ab195a49c736d9a7ba7e1e880c287d3bf12132c10a3; output_sha256=09881bed9c4b912a01172b2967249faabc43e0cdd70451fc26f9dc9451079e0f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完整识别入口、版本窗口、handoff 门禁、pre-tag 权威缺失及 tag tree 漂移，正确阻塞 GitHub Release 并保持只读边界。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=62a386a246bcb0c7c5b2df7096cfd60c5023a6b28473d50af8f99649d1d3480e; fixture_sha256=69659db940208abe97ba4ab195a49c736d9a7ba7e1e880c287d3bf12132c10a3; output_sha256=c0ef7d797fbe13f57a1f31bc813974355d1450693a33beb71972deea8f20744d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 同样得出不能继续的结论并识别主要 tag 漂移，但范围覆盖和门禁/责任路由说明较不完整。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 由 Release Manager/维护者确认或纠正 v1.4.0 tag 与 release-candidate 的差异，并补齐 post-tag 审计凭据。
- Next: 由正式文档审计责任人重新执行 post-tag audit；通过后再交给 GitHub release preparation owner。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-005-integration-release-chain`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `69659db940208abe97ba4ab195a49c736d9a7ba7e1e880c287d3bf12132c10a3` from `agents/docs/test/docs-agent/evals/workspace/eval-005-integration-release-chain`.
- Fixture SHA-256: `69659db940208abe97ba4ab195a49c736d9a7ba7e1e880c287d3bf12132c10a3`
- Prompt SHA-256: `62a386a246bcb0c7c5b2df7096cfd60c5023a6b28473d50af8f99649d1d3480e`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b04f0f833fdfe60f19dba4258110d7f6b0a3d6a6f2afb7034b0d3d883c30f83b`
- Skill overlay SHA-256: `14d196833dce28912d8b0b555bccdba07e09dd666cd5fbd0bbf5033b1450392d`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `05d8b9eb5ccf6bbc077dad850c79899562c5b4ed9bbb4187abffd82f21410ea3`
- Metadata SHA-256: `af301306a3e584e9c32987cd73e02ac298dcd98f38208af58ca0764e8b5a4154`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_release_audit_entry` | PASS | with_skill identifies the release-chain entry, confirmed v1.4.0 scope, evidence sources, audit phases, and read-only execution boundary. |
| `evaluates_site_release_notes_gate` | PASS | with_skill treats the handoff's ready status as insufficient, cites missing audit authority and unverified surfaces, and routes remediation to the documentation audit owner. |
| `validates_release_window_basis` | FAIL | with_skill cites the tag-entry and actual tag trees, but does not explicitly validate the configured version window and comparison anchors (previous tag/base and target refs) from the signed snapshot. |
| `rejects_missing_pre_tag_authority` | PASS | with_skill explicitly states that no ready_for_tag or usable pre-tag audit authority exists and does not claim pre-tag success. |
| `detects_post_tag_evidence_drift` | PASS | with_skill identifies the existing v1.4.0 tag and the mismatch between the tag-entry tree (7c8b9b...) and actual tag tree (490d0b...), concluding blocked. |
| `blocks_github_release_handoff` | PASS | with_skill concludes GitHub Release preparation/publication cannot continue, produces no executable preview/draft/publish handoff, and assigns remediation to the formal documentation audit owner. |
| `preserves_no_mutation_boundaries` | PASS | with_skill states that no tag or GitHub Release writes occurred; locked git evidence shows no status, diff, ref, commit, or reflog changes. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=62a386a246bcb0c7c5b2df7096cfd60c5023a6b28473d50af8f99649d1d3480e; fixture_sha256=69659db940208abe97ba4ab195a49c736d9a7ba7e1e880c287d3bf12132c10a3; output_sha256=c1d6413fac110951b0936848393e40711379a4238038710f6594ef68f7a95c67; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly accepts the audit entry, evaluates the handoff, rejects missing pre-tag authority, detects tag/tree drift, blocks release handoff, and preserves read-only boundaries; it omits explicit validation of the full release-window comparison anchors.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=62a386a246bcb0c7c5b2df7096cfd60c5023a6b28473d50af8f99649d1d3480e; fixture_sha256=69659db940208abe97ba4ab195a49c736d9a7ba7e1e880c287d3bf12132c10a3; output_sha256=2bacbbd8052b3e33d42da9a01213d15562580e67d18c3b6dfe5d44c1676c27fc; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly blocks GitHub Release and identifies tag/tree drift, but gives a less structured audit and includes unsupported or less relevant evidence claims.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill does not explicitly confirm the previous-tag/base/target comparison anchors from the signed Git reference snapshot, as required by validates_release_window_basis.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-005-integration-release-chain`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `69659db940208abe97ba4ab195a49c736d9a7ba7e1e880c287d3bf12132c10a3` from `agents/docs/test/docs-agent/evals/workspace/eval-005-integration-release-chain`.
- Fixture SHA-256: `69659db940208abe97ba4ab195a49c736d9a7ba7e1e880c287d3bf12132c10a3`
- Prompt SHA-256: `62a386a246bcb0c7c5b2df7096cfd60c5023a6b28473d50af8f99649d1d3480e`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e64e4dc492a2ff92be09822529f9abb1fbd17f4d0148b3045e0162382c5d46d3`
- Skill overlay SHA-256: `3eaa5c3784c96e8dc4ef11789d79c826391bf168fdf53216b77982b9667daae3`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `05d8b9eb5ccf6bbc077dad850c79899562c5b4ed9bbb4187abffd82f21410ea3`
- Metadata SHA-256: `c1ee9aeb87a312a5a12a5c6bde57cbe238245b2c2b0147ad5f64c990238e5981`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_release_audit_entry` | PASS | with_skill识别v1.4.0及维护者确认，依据签认快照和文档证据进行只读审计，并保留发布范围与无写入边界。 |
| `evaluates_site_release_notes_gate` | PASS | 指出handoff虽为ready且docs checks通过，但关键pre-tag审计authority缺失，不能被下游消费，并将修复交给docs-audit owner。 |
| `validates_release_window_basis` | PASS | 明确release-base到release-candidate及two-dot diff；这些ref和语义均由入口与签认snapshot提供，未猜测缺失锚点。 |
| `rejects_missing_pre_tag_authority` | PASS | 明确缺少可验证的pre-tag audit authority和candidate record，因此不宣称pre-tag通过，也不返回ready_for_tag。 |
| `detects_post_tag_evidence_drift` | PASS | 根据snapshot指出v1.4.0 tag树490d…与候选树7c8…不一致，判定tag-tree drift并阻塞。 |
| `blocks_github_release_handoff` | PASS | 明确当前不能进入GitHub Release preparation，不创建draft或publish handoff，并指定release owner和docs-audit owner后续处理。 |
| `preserves_no_mutation_boundaries` | PASS | 明确本次未执行任何tag或GitHub Release写入，且建议均为后续责任人处理，不声称已进行变更。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=62a386a246bcb0c7c5b2df7096cfd60c5023a6b28473d50af8f99649d1d3480e; fixture_sha256=69659db940208abe97ba4ab195a49c736d9a7ba7e1e880c287d3bf12132c10a3; output_sha256=5a4c25abca675f226ddc432c7bb37f1c23c3414207184327b2baddc026567b3e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完整执行只读发布审计判断：保留入口边界，验证窗口，识别缺少pre-tag authority及tag/tree漂移，阻止GitHub Release并交回责任人。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=62a386a246bcb0c7c5b2df7096cfd60c5023a6b28473d50af8f99649d1d3480e; fixture_sha256=69659db940208abe97ba4ab195a49c736d9a7ba7e1e880c287d3bf12132c10a3; output_sha256=50cef841d95d7ea43089159b1f80b89c3aca213a6df47fb9ca1458f5e55a0950; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确判定发布链阻塞并识别tag/tree漂移和缺少post-tag证据，但未完整指出缺少pre-tag authority。
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
- Skill: `docs-agent`
- Eval: `eval-005-integration-release-chain`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1632db2ef57cd08fd5111dc591159b38c9384e4241c7c2810f25eebdc67d578a` from `agents/docs/test/docs-agent/evals/workspace/eval-005-integration-release-chain`.
- Fixture SHA-256: `1632db2ef57cd08fd5111dc591159b38c9384e4241c7c2810f25eebdc67d578a`
- Prompt SHA-256: `62a386a246bcb0c7c5b2df7096cfd60c5023a6b28473d50af8f99649d1d3480e`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e64e4dc492a2ff92be09822529f9abb1fbd17f4d0148b3045e0162382c5d46d3`
- Skill overlay SHA-256: `2b78d9a9f27e14686e353416ca51ebbc0b93a1511fb165c6da87d481cf0eda24`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `05d8b9eb5ccf6bbc077dad850c79899562c5b4ed9bbb4187abffd82f21410ea3`
- Metadata SHA-256: `c1ee9aeb87a312a5a12a5c6bde57cbe238245b2c2b0147ad5f64c990238e5981`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_release_audit_entry` | PASS | 以 v1.4.0 发布链为目标，保留只读审计边界，并引用入口与 Git snapshot。 |
| `evaluates_site_release_notes_gate` | FAIL | 承认 handoff 的 ready 状态不足以进入后续门禁，但未识别 Release Notes 的 last_verified_version=unverified 与 metadata 的 released/verifiedDocs 矛盾，也未将 site Release Notes owner 作为修复责任人。 |
| `validates_release_window_basis` | FAIL | 未确认 snapshot 中 v1.3.0、release-base、release-candidate 等版本窗口和比较锚点可解析，且未明确指出这些锚点不能被替代。 |
| `rejects_missing_pre_tag_authority` | PASS | 明确指出缺少可验证的 pre-tag 审计权威，不据此宣称 pre-tag 已通过。 |
| `detects_post_tag_evidence_drift` | FAIL | 未依据签认 snapshot 识别 v1.4.0 tag/release-evidence 树为 490d，而 candidate、tag-entry、evidence-expected 树为 7c8b 的实际漂移；改称当前工作区缺少 refs/objects，未完成要求的漂移判断。 |
| `blocks_github_release_handoff` | PASS | 明确结论为 blocked，禁止准备或写入 GitHub Release，并交回 release manager/Git owner 与 docs-audit owner。 |
| `preserves_no_mutation_boundaries` | PASS | 明确声明未创建 tag、未准备或写入 GitHub Release；锁定证据中的 git 状态也无变更。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=62a386a246bcb0c7c5b2df7096cfd60c5023a6b28473d50af8f99649d1d3480e; fixture_sha256=1632db2ef57cd08fd5111dc591159b38c9384e4241c7c2810f25eebdc67d578a; output_sha256=88dd810a54b4774549063932c787e0a6e152f9500ef1481df44a67b5bc6c1aca; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确保持只读边界并阻塞 GitHub Release，但遗漏或错误处理了站内门禁矛盾、发布窗口锚点和签认 snapshot 中的具体 post-tag 漂移。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=62a386a246bcb0c7c5b2df7096cfd60c5023a6b28473d50af8f99649d1d3480e; fixture_sha256=1632db2ef57cd08fd5111dc591159b38c9384e4241c7c2810f25eebdc67d578a; output_sha256=9830e38b71e31625b03bb98cb41c1a60f109ec45b4f8b031f812a9cc1ab91b55; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确阻塞发布并识别 tag/tree 漂移、post-tag 证据错误绑定、Release Notes 状态矛盾及责任人。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未识别 Release Notes handoff 与文档/metadata 验证状态的矛盾及正确的文档 owner。
- with_skill 未验证发布窗口及 v1.3.0 比较锚点。
- with_skill 未识别签认 Git snapshot 中 v1.4.0 tag 与 candidate/evidence-expected 树之间的具体漂移。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-005-integration-release-chain`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1632db2ef57cd08fd5111dc591159b38c9384e4241c7c2810f25eebdc67d578a` from `agents/docs/test/docs-agent/evals/workspace/eval-005-integration-release-chain`.
- Fixture SHA-256: `1632db2ef57cd08fd5111dc591159b38c9384e4241c7c2810f25eebdc67d578a`
- Prompt SHA-256: `62a386a246bcb0c7c5b2df7096cfd60c5023a6b28473d50af8f99649d1d3480e`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9fbb92b16f91777ce613be24ad3cd630730cfccd4cce1cf1d33c3b6c917671d6`
- Skill overlay SHA-256: `5c882a57295d157e3993960abec476d2e269c34163ca7490bf29b90ab3d78823`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `05d8b9eb5ccf6bbc077dad850c79899562c5b4ed9bbb4187abffd82f21410ea3`
- Metadata SHA-256: `c1ee9aeb87a312a5a12a5c6bde57cbe238245b2c2b0147ad5f64c990238e5981`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_release_audit_entry` | PASS | With-skill output recognizes v1.4.0 maintainer confirmation, the documented release scope, and the read-only/no-write boundary. |
| `evaluates_site_release_notes_gate` | FAIL | It calls the Release Notes handoff ready and does not return the site Release Notes owner as responsible for the incomplete handoff credentials, despite the missing pre-tag authority and release verification. |
| `validates_release_window_basis` | FAIL | It identifies the candidate/tag tree mismatch but does not verify the configured previous-tag and base-ref comparison window from the signed snapshot. |
| `rejects_missing_pre_tag_authority` | PASS | It explicitly states that formal pre-tag audit authority is missing and refuses to infer that the tag is bound to an audited document tree. |
| `detects_post_tag_evidence_drift` | PASS | It correctly identifies that the v1.4.0 tag tree differs from the release-candidate/tag-entry tree and concludes the chain is blocked. |
| `blocks_github_release_handoff` | PASS | It concludes GitHub Release preparation or publication cannot continue and does not generate a preview, draft, or publish handoff. |
| `preserves_no_mutation_boundaries` | PASS | It explicitly states that no tag or GitHub Release writes were performed. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=62a386a246bcb0c7c5b2df7096cfd60c5023a6b28473d50af8f99649d1d3480e; fixture_sha256=1632db2ef57cd08fd5111dc591159b38c9384e4241c7c2810f25eebdc67d578a; output_sha256=15a71edc0f173c63796641377b57dcd988a934565232df33e561a67a3335ea76; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly blocks GitHub Release progression, detects tag/tree drift, rejects missing pre-tag authority, and preserves read-only boundaries, but misses the required release-window validation and assigns incomplete handoff remediation to the wrong owner.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=62a386a246bcb0c7c5b2df7096cfd60c5023a6b28473d50af8f99649d1d3480e; fixture_sha256=1632db2ef57cd08fd5111dc591159b38c9384e4241c7c2810f25eebdc67d578a; output_sha256=f4d26bf940bfd37291e2232f0112fd75227e9663d79f489f37d17f7faa0d5810; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly blocks release progression and identifies tree drift, missing post-tag evidence, and inconsistent documentation verification, but provides less explicit pre-tag authority analysis.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with-skill output does not validate the previous-tag/base-ref release window and comparison anchor.
- It treats the site Release Notes handoff as ready and does not return the site Release Notes owner for incomplete gate credentials.
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

- Skill: `docs-agent`
- Eval: `eval-005-integration-release-chain`
- Scenario: 基于原始站内 Release Notes 与 synthetic Git 对象判断发布链是否具备 GitHub Release 资格
- Review context: issue #177 sub-batch 4a

## Test Set / Fixture Version

- Fixture version: `issue-177 discrimination restore round-2b`
- Actual validation date: `2026-07-28`
- Fresh run: `tmp/eval-runs/issue-177/docs-agent-eval-005/round-2b-fixture-correction/`
- with-skill 与 without-skill 使用同一 prompt 和独立 pristine fixture；两侧均只在各自隔离 workspace 执行 setup。
- with-skill 读取 Docs router、`release-notes-gen`、`docs-audit` 与 PM `github-release-gen` 契约；without-skill 未读取或应用目标 skill、Agent README、assertions、旧 comparison、历史 baseline 或 with-skill 输出。

## Latest Result

- Behavior result: `PASS`（with）/ `PASS`（without）— 本轮 #238 fresh 隔离重跑（2026-08-06）
- Coverage result: `PARTIAL`（with）/ `PARTIAL`（without）— 本轮重跑实际触发的断言场景
Overall result: BLOCKED
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `PASS` / Coverage `PARTIAL`
- without_skill：Behavior `PASS` / Coverage `PARTIAL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `accepts_release_audit_entry` | PASS | PASS | `release-chain-entry.md` 明确给出 `target_release_version: v1.4.0`、维护者确认、审计阶段、范围及“仅资格审查、不写入”限制。 |
| `evaluates_site_release_notes_gate` | PASS | PASS | `release-notes-handoff.md` 虽为 `handoff_status: ready` 且 `blockers: []`，但两条 lane 均识别 `evidence/docs-checks.md` 缺失，并将责任交回 `release-notes-gen`。 |
| `validates_release_window_basis` | NOT_EXERCISED | NOT_EXERCISED | 入口虽声明 `previous_tag: v1.3.0`、`intended_target_tag: v1.4.0` 及多个 ref，但 `.git` 初始化失败且 `.eval/runtime-git-evidence.md` 不存在，版本窗口与比较锚点未在 synthetic repository 中实际解析。 |
| `rejects_missing_pre_tag_authority` | PASS | PASS | 两条结果均明确：不能继续 `docs-audit pre-tag`，不能将 handoff 自称的 `passed` 视为可复核的 pre-tag 权威。 |
| `detects_post_tag_evidence_drift` | NOT_EXERCISED | NOT_EXERCISED | `setup-git-fixture.sh` 虽定义了 drift commit 和漂移 tag，但 `.git` 初始化失败，未生成 runtime Git 对象，也未实际完成 post-tag 对象比较。 |
| `blocks_github_release_handoff` | PASS | PASS | 两条结果均明确不得进入 GitHub Release handoff；`release_execution_authorized: false`，且要求等待 `ready_for_tag`、实际 tag、`release_verified` 和独立批准。 |
| `preserves_no_mutation_boundaries` | PASS | PASS | with_skill 明确“未执行任何真实 tag 或 GitHub Release 写入”；without_skill 仅尝试隔离 synthetic fixture setup，因 `.git` 写入受限失败，未修改真实 tag 或 Release。 |

本轮无 FAIL 断言。

未触发断言：`validates_release_window_basis`、`detects_post_tag_evidence_drift`

基础设施阻塞说明：Git 仓库缺失；对应断言不构成 skill 行为回归。



## Leakage Surface Analysis

重做前，baseline 可直接看到并复用以下协议：

- prompt 明示临时 worktree、object reads、两次 staged gate、committed delta gate、CAS、三项 GitHub Release 上游门禁和输出结构。
- assertions 复制七字段 frontmatter、API 细节、Git 命令、candidate/discovery/post-tag schema、路径互指和 handoff 字段清单。
- 910 行 setup 生成并自检 `candidate_verified`、`ready_for_tag` 和 `release_verified`，完成 schema、delta、CAS、readback 与末尾全等 self-check。
- candidate、discovery、成功/阻塞 post-tag 模板直接提供预期记录；baseline 只需复述 setup 已证明的成功结论。
- fixture 文案残留本仓库历史 issue 身份引用，使责任链可从编号而非 skill 语义推断。

## Redesign

- prompt 仅保留任务意图、入口指针、隔离范围与禁止真实写入边界。
- assertions 收敛为 7 条语义结果，不复制字段清单、命令序列或记录 schema；judge 必须对照 skill 文档判断。
- setup 从 910 行缩减为 70 行，只构造 base/target、previous tag、进入检查时的 tag snapshot、漂移后的实际 tag、预期 evidence ref 和并发移动后的 evidence branch。
- 删除 pre-tag candidate/discovery、post-tag success/blocked 模板及全部 setup 协议自检；setup 不生成任何 audit record、success handoff、`ready_for_tag` 或 `release_verified`。
- fixture 增加一个自称 `ready` 但缺少正文确认凭据的站内 handoff，并保留 tag tuple 与 expected-head 漂移，使 skill 门禁而非 setup 成为判定来源。
- 将 fixture 与脚手架中的历史 issue 身份引用替换为 `docs-agent:release-notes-gen`、`docs-agent:docs-audit`、`pm-agent:github-release-gen`。

## Assertions
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- `accepts_release_audit_entry`: with-skill PASS；baseline PASS。两侧均接受已确认版本、范围与只读边界。
- `evaluates_site_release_notes_gate`: with-skill PASS；baseline **FAIL**。with-skill 拒绝缺少正文确认凭据的 ready handoff，并返回 `docs-agent:release-notes-gen`；baseline 将其视为可进入 docs-audit。
- `validates_release_window_basis`: with-skill PASS；baseline **FAIL**。with-skill 解析 base、target、previous tag 与版本 surfaces；baseline 未验证完整 compare window。
- `rejects_missing_pre_tag_authority`: with-skill PASS；baseline PASS。两侧均未从原始目标树推断 `ready_for_tag`。
- `detects_post_tag_evidence_drift`: with-skill PASS；baseline PASS。两侧均发现实际 tag/tree 与 snapshot 不同，且 evidence branch 不等于 expected ref。
- `blocks_github_release_handoff`: with-skill PASS；baseline **FAIL**。with-skill 按依赖顺序返回 Release Notes owner、宿主 tag owner 与 docs-audit；baseline 跳过正文确认 owner，直接交给 docs-audit。
- `preserves_no_mutation_boundaries`: with-skill PASS；baseline PASS。两侧均未执行真实 tag、远端或 GitHub Release 写入。

## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 将现有 `docs/site/` 识别为 site-enabled host，不允许以无文档站路径降级。
- 发现 `release-notes-handoff.md` 自称 ready，但缺少正文确认凭据，因此不能作为 docs-audit 的有效上游 handoff。
- 从实际 Git 对象确认 `v1.3.0` 指向 base，target/tag-entry snapshot 指向目标 commit，当前 `v1.4.0` tag 多出 `.eval-drift-marker`。
- 确认 target 与 tag tree 均缺少固定 pre-tag candidate/discovery 权威，不能产生 `ready_for_tag` 或 `release_verified`。
- 确认 release-evidence branch 已偏离 expected ref，禁止覆盖并发移动。
- 结果：7/7 PASS；Behavior PASS；Coverage FULL。

## Fresh Without-Skill Baseline

> ⚠️ 本节为历史轮执行证据（适用旧 run）；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

- 来源：同一新 prompt 与独立 pristine fixture 的 fresh baseline；未复用历史 baseline。
- 正确识别 tag/tree 漂移、evidence branch 漂移、缺少 pre/post-tag 成功证据和零写入边界。
- 未识别站内 ready handoff 缺少权威正文确认凭据，未证明完整 release window，并把首要补救直接交给 docs-audit。
- 结果：4/7 PASS、3/7 FAIL；相对 with-skill 存在 3 条可测量差距。

## Failures And Iterations
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- Round 1：with-skill 与 baseline 均识别对象漂移并阻止 GitHub Release，仍无区分度。
- Round 2：加入站内 handoff 语义门禁后产生 +2 uplift，但简化 setup 时遗漏入口声明的 synthetic `v1.3.0`，导致双方漏过 release-window assertion；judge 判 with-skill 6/7、Behavior FAIL。
- Round 2 fixture correction：只在 base commit 补回已声明的 `v1.3.0`，不改变 prompt、assertions 或目标阻塞场景；fresh paired rerun 与 fresh judge 得到 with-skill 7/7、baseline 4/7。
- Setup/API/docs command failures: none。

## Next Steps

- 保持本用例为阻塞型集成回归：它衡量完整上游资格与 owner 边界，不把总体 `blocked` 文案当作通过依据。
- 后续若修改 Release Notes、docs-audit 或 GitHub Release gate，应重跑 fresh paired validation，并以本 comparison 的 7 条语义 assertions 判断回归和 uplift。

## Runtime Artifact Policy

- Synthetic repositories、`response.md`、judge verdict、setup logs、runtime object index 与依赖目录仅位于 `tmp/eval-runs/issue-177/docs-agent-eval-005/` 或系统临时目录，不提交。
- 本 `comparison.md` 是唯一 durable eval 结果。
